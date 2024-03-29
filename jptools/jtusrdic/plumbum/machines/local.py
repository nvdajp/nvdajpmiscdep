from __future__ import with_statement
import os
import sys
import subprocess
import logging
import stat
import time
import six
import re
from plumbum.path.local import LocalPath, LocalWorkdir
from tempfile import mkdtemp
from contextlib import contextmanager
from plumbum.path.remote import RemotePath
from plumbum.commands import CommandNotFound, ConcreteCommand
from plumbum.machines.session import ShellSession
from plumbum.lib import ProcInfo, IS_WIN32
from plumbum.commands.daemons import win32_daemonize, posix_daemonize
from plumbum.machines.env import BaseEnv
if sys.version_info >= (3, 2):
    # python 3.2 has the new-and-improved subprocess module
    from subprocess import Popen, PIPE
    has_new_subprocess = True
else:
    # otherwise, see if we have subprocess32
    try:
        from subprocess32 import Popen, PIPE
        has_new_subprocess = True
    except ImportError:
        from subprocess import Popen, PIPE
        has_new_subprocess = False


logger = logging.getLogger("plumbum.local")


#===================================================================================================
# Environment
#===================================================================================================
class LocalEnv(BaseEnv):
    """The local machine's environment; exposes a dict-like interface"""
    __slots__ = []
    CASE_SENSITIVE = not IS_WIN32

    def __init__(self):
        # os.environ already takes care of upper'ing on windows
        self._curr = os.environ.copy()
        BaseEnv.__init__(self, LocalPath, os.path.pathsep)
        if IS_WIN32 and "HOME" not in self and self.home is not None:
            self["HOME"] = self.home

    def expand(self, expr):
        """Expands any environment variables and home shortcuts found in ``expr``
        (like ``os.path.expanduser`` combined with ``os.path.expandvars``)

        :param expr: An expression containing environment variables (as ``$FOO``) or
                     home shortcuts (as ``~/.bashrc``)

        :returns: The expanded string"""
        prev = os.environ
        os.environ = self.getdict()
        try:
            output = os.path.expanduser(os.path.expandvars(expr))
        finally:
            os.environ = prev
        return output

    def expanduser(self, expr):
        """Expand home shortcuts (e.g., ``~/foo/bar`` or ``~john/foo/bar``)

        :param expr: An expression containing home shortcuts

        :returns: The expanded string"""
        prev = os.environ
        os.environ = self.getdict()
        try:
            output = os.path.expanduser(expr)
        finally:
            os.environ = prev
        return output

#===================================================================================================
# Local Commands
#===================================================================================================
class LocalCommand(ConcreteCommand):
    __slots__ = []
    QUOTE_LEVEL = 2

    def __init__(self, executable, encoding = "auto"):
        ConcreteCommand.__init__(self, executable,
            local.encoding if encoding == "auto" else encoding)

    def __repr__(self):
        return "LocalCommand(%r)" % (self.executable,)

    def popen(self, args = (), cwd = None, env = None, **kwargs):
        if isinstance(args, six.string_types):
            args = (args,)
        return local._popen(self.executable, self.formulate(0, args),
            cwd = self.cwd if cwd is None else cwd, env = self.env if env is None else env,
            **kwargs)

#===================================================================================================
# Local Machine
#===================================================================================================
class LocalMachine(object):
    """The *local machine* (a singleton object). It serves as an entry point to everything
    related to the local machine, such as working directory and environment manipulation,
    command creation, etc.

    Attributes:

    * ``cwd`` - the local working directory
    * ``env`` - the local environment
    * ``encoding`` - the local machine's default encoding (``sys.getfilesystemencoding()``)
    """
    cwd = LocalWorkdir()
    env = LocalEnv()
    encoding = sys.getfilesystemencoding()

    def __init__(self):
        self._as_user_stack = []

    if IS_WIN32:
        _EXTENSIONS = [""] + env.get("PATHEXT", ":.exe:.bat").lower().split(os.path.pathsep)

        @classmethod
        def _which(cls, progname):
            progname = progname.lower()
            for p in cls.env.path:
                try:
                    filelist = dict((n.basename, n) for n in p.list())
                except OSError:
                    continue
                for ext in cls._EXTENSIONS:
                    n = progname + ext
                    if n in filelist:
                        return filelist[n]
            return None
    else:
        @classmethod
        def _which(cls, progname):
            for p in cls.env.path:
                try:
                    filelist = dict((n.basename, n) for n in p.list())
                except OSError:
                    continue
                if progname in filelist:
                    f = filelist[progname]
                    if not f.stat().st_mode & stat.S_IXUSR:
                        continue
                    return f
            return None

    @classmethod
    def which(cls, progname):
        """Looks up a program in the ``PATH``. If the program is not found, raises
        :class:`CommandNotFound <plumbum.commands.CommandNotFound>`

        :param progname: The program's name. Note that if underscores (``_``) are present
                         in the name, and the exact name is not found, they will be replaced
                         by hyphens (``-``) and the name will be looked up again

        :returns: A :class:`LocalPath <plumbum.machines.local.LocalPath>`
        """
        alternatives = [progname]
        if "_" in progname:
            alternatives.append(progname.replace("_", "-"))
        for pn in alternatives:
            path = cls._which(pn)
            if path:
                return path
        raise CommandNotFound(progname, list(cls.env.path))

    def path(self, *parts):
        """A factory for :class:`LocalPaths <plumbum.path.local.LocalPath>`.
        Usage: ``p = local.path("/usr", "lib", "python2.7")``
        """
        parts2 = [str(self.cwd)]
        for p in parts:
            if isinstance(p, RemotePath):
                raise TypeError("Cannot construct LocalPath from %r" % (p,))
            parts2.append(self.env.expanduser(str(p)))
        return LocalPath(os.path.join(*parts2))

    def __getitem__(self, cmd):
        """Returns a `Command` object representing the given program. ``cmd`` can be a string or
        a :class:`LocalPath <plumbum.path.local.LocalPath>`; if it is a path, a command
        representing this path will be returned; otherwise, the program name will be looked up
        in the system's ``PATH`` (using ``which``). Usage::

            ls = local["ls"]
        """
        if isinstance(cmd, LocalPath):
            return LocalCommand(cmd)
        elif not isinstance(cmd, RemotePath):
            if "/" in cmd or "\\" in cmd:
                # assume path
                return LocalCommand(local.path(cmd))
            else:
                # search for command
                return LocalCommand(self.which(cmd))
        else:
            raise TypeError("cmd must not be a RemotePath: %r" % (cmd,))

    def _popen(self, executable, argv, stdin = PIPE, stdout = PIPE, stderr = PIPE,
            cwd = None, env = None, new_session = False, **kwargs):
        if new_session:
            if has_new_subprocess:
                kwargs["start_new_session"] = True
            elif subprocess.mswindows:
                kwargs["creationflags"] = kwargs.get("creationflags", 0) | subprocess.CREATE_NEW_PROCESS_GROUP 
            else:
                def preexec_fn(prev_fn = kwargs.get("preexec_fn", lambda: None)):
                    os.setsid()
                    prev_fn()
                kwargs["preexec_fn"] = preexec_fn

        if subprocess.mswindows and "startupinfo" not in kwargs and stdin not in (sys.stdin, None):
            kwargs["startupinfo"] = sui = subprocess.STARTUPINFO()
            if hasattr(subprocess, "_subprocess"):
                sui.dwFlags |= subprocess._subprocess.STARTF_USESHOWWINDOW  # @UndefinedVariable
                sui.wShowWindow = subprocess._subprocess.SW_HIDE  # @UndefinedVariable
            else:
                sui.dwFlags |= subprocess.STARTF_USESHOWWINDOW  # @UndefinedVariable
                sui.wShowWindow = subprocess.SW_HIDE  # @UndefinedVariable
        
        if not has_new_subprocess and "close_fds" not in kwargs:
            if subprocess.mswindows and (stdin is not None or stdout is not None or stderr is not None):
                # we can't close fds if we're on windows and we want to redirect any std handle
                kwargs["close_fds"] = False
            else:
                kwargs["close_fds"] = True

        if cwd is None:
            cwd = self.cwd
        if env is None:
            env = self.env
        if isinstance(env, BaseEnv):
            env = env.getdict()

        if self._as_user_stack:
            argv, executable = self._as_user_stack[-1](argv)

        logger.debug("Running %r", argv)
        proc = Popen(argv, executable = str(executable), stdin = stdin, stdout = stdout,
            stderr = stderr, cwd = str(cwd), env = env, **kwargs)  # bufsize = 4096
        proc._start_time = time.time()
        proc.encoding = self.encoding
        proc.argv = argv
        return proc

    def daemonic_popen(self, command, cwd = "/"):
        """
        On POSIX systems
        ~~~~~~~~~~~~~~~~
        Run ``command`` as a UNIX daemon: fork a child process to setpid, redirect std handles to /dev/null,
        umask, close all fds, chdir to ``cwd``, then fork and exec ``command``. Returns a ``Popen`` process that
        can be used to poll/wait for the executed command (but keep in mind that you cannot access std handles)

        On Windows
        ~~~~~~~~~~
        Run ``command`` as a "Windows daemon": detach from controlling console and create a new process group.
        This means that the command will not receive console events and would survive its parent's termination.
        Returns a ``Popen`` object.

        .. note:: this does not run ``command`` as a system service, only detaches it from its parent.

        .. versionadded:: 1.3
        """
        if IS_WIN32:
            return win32_daemonize(command, cwd)
        else:
            return posix_daemonize(command, cwd)

    if IS_WIN32:
        def list_processes(self):
            """
            Returns information about all running processes (on Windows: using ``tasklist``)

            .. versionadded:: 1.3
            """
            import csv
            tasklist = local["tasklist"]
            lines = tasklist("/V", "/FO", "CSV").encode("utf8").splitlines()
            rows = csv.reader(lines)
            header = rows.next()
            imgidx = header.index('Image Name')
            pididx = header.index('PID')
            statidx = header.index('Status')
            useridx = header.index('User Name')
            for row in rows:
                yield ProcInfo(int(row[pididx]), row[useridx].decode("utf8"), 
                    row[statidx].decode("utf8"), row[imgidx].decode("utf8"))
    else:
        def list_processes(self):
            """
            Returns information about all running processes (on POSIX systems: using ``ps``)

            .. versionadded:: 1.3
            """
            ps = self["ps"]
            lines = ps("-e", "-o", "pid,uid,stat,args").splitlines()
            lines.pop(0) # header
            for line in lines:
                parts = line.strip().split()
                yield ProcInfo(int(parts[0]), int(parts[1]), parts[2], " ".join(parts[3:]))

    def pgrep(self, pattern):
        """
        Process grep: return information about all processes whose command-line args match the given regex pattern
        """
        pat = re.compile(pattern)
        for procinfo in self.list_processes():
            if pat.search(procinfo.args):
                yield procinfo 

    def session(self):
        """Creates a new :class:`ShellSession <plumbum.session.ShellSession>` object; this
        invokes ``/bin/sh`` and executes commands on it over stdin/stdout/stderr"""
        return ShellSession(self["sh"].popen())

    @contextmanager
    def tempdir(self):
        """A context manager that creates a temporary directory, which is removed when the context
        exits"""
        dir = self.path(mkdtemp())  # @ReservedAssignment
        try:
            yield dir
        finally:
            dir.delete()

    @contextmanager
    def as_user(self, username = None):
        """Run nested commands as the given user. For example::

            head = local["head"]
            head("-n1", "/dev/sda1")    # this will fail...
            with local.as_user():
                head("-n1", "/dev/sda1")

        :param username: The user to run commands as. If not given, root (or Administrator) is assumed
        """
        if IS_WIN32:
            if username is None:
                username = "Administrator"
            self._as_user_stack.append(lambda argv: (["runas", "/savecred", "/user:%s" % (username,),
                '"' + " ".join(str(a) for a in argv) + '"'], self.which("runas")))
        else:
            if username is None:
                self._as_user_stack.append(lambda argv: (["sudo"] + list(argv), self.which("sudo")))
            else:
                self._as_user_stack.append(lambda argv: (["sudo", "-u", username] + list(argv), self.which("sudo")))
        try:
            yield
        finally:
            self._as_user_stack.pop(-1)

    def as_root(self):
        """A shorthand for :func:`as_user("root") <plumbum.machines.local.LocalMachine.as_user>`"""
        return self.as_user()

    python = LocalCommand(sys.executable, encoding)
    """A command that represents the current python interpreter (``sys.executable``)"""

local = LocalMachine()
"""The *local machine* (a singleton object). It serves as an entry point to everything
related to the local machine, such as working directory and environment manipulation,
command creation, etc.

Attributes:

* ``cwd`` - the local working directory
* ``env`` - the local environment
* ``encoding`` - the local machine's default encoding (``sys.getfilesystemencoding()``)
"""
