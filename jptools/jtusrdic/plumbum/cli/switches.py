import six
import inspect
from plumbum import local


class SwitchError(Exception):
    """A general switch related-error (base class of all other switch errors)"""
    pass
class PositionalArgumentsError(SwitchError):
    """Raised when an invalid number of positional arguments has been given"""
    pass
class SwitchCombinationError(SwitchError):
    """Raised when an invalid combination of switches has been given"""
    pass
class UnknownSwitch(SwitchError):
    """Raised when an unrecognized switch has been given"""
    pass
class MissingArgument(SwitchError):
    """Raised when a switch requires an argument, but one was not provided"""
    pass
class MissingMandatorySwitch(SwitchError):
    """Raised when a mandatory switch has not been given"""
    pass
class WrongArgumentType(SwitchError):
    """Raised when a switch expected an argument of some type, but an argument of a wrong
    type has been given"""
    pass
class SubcommandError(SwitchError):
    """Raised when there's something wrong with subcommands"""
    pass


#===================================================================================================
# The switch decorator
#===================================================================================================
class SwitchInfo(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

def switch(names, argtype = None, argname = None, list = False, mandatory = False, requires = (),
        excludes = (), help = None, overridable = False, group = "Switches"):
    """
    A decorator that exposes functions as command-line switches. Usage::

        class MyApp(Application):
            @switch(["-l", "--log-to-file"], argtype = str)
            def log_to_file(self, filename):
                handler = logging.FileHandler(filename)
                logger.addHandler(handler)

            @switch(["--verbose"], excludes=["--terse"], requires=["--log-to-file"])
            def set_debug(self):
                logger.setLevel(logging.DEBUG)

            @switch(["--terse"], excludes=["--verbose"], requires=["--log-to-file"])
            def set_terse(self):
                logger.setLevel(logging.WARNING)

    :param names: The name(s) under which the function is reachable; it can be a string
                  or a list of string, but at least one name is required. There's no need
                  to prefix the name with ``-`` or ``--`` (this is added automatically),
                  but it can be used for clarity. Single-letter names are prefixed by ``-``,
                  while longer names are prefixed by ``--``

    :param argtype: If this function takes an argument, you need to specify its type. The
                    default is ``None``, which means the function takes no argument. The type
                    is more of a "validator" than a real type; it can be any callable object
                    that raises a ``TypeError`` if the argument is invalid, or returns an
                    appropriate value on success. If the user provides an invalid value,
                    :func:`plumbum.cli.WrongArgumentType`

    :param argname: The name of the argument; if ``None``, the name will be inferred from the
                    function's signature

    :param list: Whether or not this switch can be repeated (e.g. ``gcc -I/lib -I/usr/lib``).
                 If ``False``, only a single occurrence of the switch is allowed; if ``True``,
                 it may be repeated indefinitely. The occurrences are collected into a list,
                 so the function is only called once with the collections. For instance,
                 for ``gcc -I/lib -I/usr/lib``, the function will be called with
                 ``["/lib", "/usr/lib"]``.

    :param mandatory: Whether or not this switch is mandatory; if a mandatory switch is not
                      given, :class:`MissingMandatorySwitch <plumbum.cli.MissingMandatorySwitch>`
                      is raised. The default is ``False``.

    :param requires: A list of switches that this switch depends on ("requires"). This means that
                     it's invalid to invoke this switch without also invoking the required ones.
                     In the example above, it's illegal to pass ``--verbose`` or ``--terse``
                     without also passing ``--log-to-file``. By default, this list is empty,
                     which means the switch has no prerequisites. If an invalid combination
                     is given, :class:`SwitchCombinationError <plumbum.cli.SwitchCombinationError>`
                     is raised.

                     Note that this list is made of the switch *names*; if a switch has more
                     than a single name, any of its names will do.

                     .. note::
                        There is no guarantee on the (topological) order in which the actual
                        switch functions will be invoked, as the dependency graph might contain
                        cycles.

    :param excludes: A list of switches that this switch forbids ("excludes"). This means that
                     it's invalid to invoke this switch if any of the excluded ones are given.
                     In the example above, it's illegal to pass ``--verbose`` along with
                     ``--terse``, as it will result in a contradiction. By default, this list
                     is empty, which means the switch has no prerequisites. If an invalid
                     combination is given, :class:`SwitchCombinationError
                     <plumbum.cli.SwitchCombinationError>` is raised.

                     Note that this list is made of the switch *names*; if a switch has more
                     than a single name, any of its names will do.

    :param help: The help message (description) for this switch; this description is used when
                 ``--help`` is given. If ``None``, the function's docstring will be used.

    :param overridable: Whether or not the names of this switch are overridable by other switches.
                        If ``False`` (the default), having another switch function with the same
                        name(s) will cause an exception. If ``True``, this is silently ignored.

    :param group: The switch's *group*; this is a string that is used to group related switches
                  together when ``--help`` is given. The default group is ``Switches``.

    :returns: The decorated function (with a ``_switch_info`` attribute)
    """
    if isinstance(names, six.string_types):
        names = [names]
    names = [n.lstrip("-") for n in names]
    requires = [n.lstrip("-") for n in requires]
    excludes = [n.lstrip("-") for n in excludes]

    def deco(func):
        if argname is None:
            argspec = inspect.getargspec(func)[0]
            if len(argspec) == 2:
                argname2 = argspec[1]
            else:
                argname2 = "VALUE"
        else:
            argname2 = argname
        help2 = inspect.getdoc(func) if help is None else help
        if not help2:
            help2 = str(func)
        func._switch_info = SwitchInfo(names = names, argtype = argtype, list = list, func = func,
            mandatory = mandatory, overridable = overridable, group = group,
            requires = requires, excludes = excludes, argname = argname2, help = help2)
        return func
    return deco

def autoswitch(*args, **kwargs):
    """A decorator that exposes a function as a switch, "inferring" the name of the switch
    from the function's name (converting to lower-case, and replacing underscores with hyphens).
    The arguments are the same as for :func:`switch <plumbum.cli.switch>`."""
    def deco(func):
        return switch(func.__name__.replace("_", "-"), *args, **kwargs)(func)
    return deco

#===================================================================================================
# Switch Attributes
#===================================================================================================
class SwitchAttr(object):
    """
    A switch that stores its result in an attribute (descriptor). Usage::

        class MyApp(Application):
            logfile = SwitchAttr(["-f", "--log-file"], str)

            def main(self):
                if self.logfile:
                    open(self.logfile, "w")

    :param names: The switch names
    :param argtype: The switch argument's (and attribute's) type
    :param default: The attribute's default value (``None``)
    :param argname: The switch argument's name (default is ``"VALUE"``)
    :param kwargs: Any of the keyword arguments accepted by :func:`switch <plumbum.cli.switch>`
    """
    def __init__(self, names, argtype = str, default = None, list = False, argname = "VALUE", **kwargs):
        self.__doc__ = "Sets an attribute"  # to prevent the help message from showing SwitchAttr's docstring
        if "help" in kwargs and default:
            kwargs["help"] += "; the default is %r" % (default,)

        switch(names, argtype = argtype, argname = argname, list = list, **kwargs)(self)
        listtype = type([])
        if list:
            if default is None:
                self._value = []
            elif isinstance(default, (tuple, listtype)):
                self._value = listtype(default)
            else:
                self._value = [default]
        else:
            self._value = default
    def __call__(self, _, val):
        self._value = val
    def __get__(self, cls, inst):
        if inst is None:
            return self
        else:
            return self._value
    def __set__(self, inst, val):
        if inst is None:
            raise AttributeError("cannot set an unbound SwitchAttr")
        else:
            self._value = val

class Flag(SwitchAttr):
    """A specialized :class:`SwitchAttr <plumbum.cli.SwitchAttr>` for boolean flags. If the flag is not
    given, the value of this attribute is the ``default``; if it is given, the value changes
    to ``not default``. Usage::

        class MyApp(Application):
            verbose = Flag(["-v", "--verbose"], help = "If given, I'll be very talkative")

    :param names: The switch names
    :param default: The attribute's initial value (``False`` by default)
    :param kwargs: Any of the keyword arguments accepted by :func:`switch <plumbum.cli.switch>`,
                   except for ``list`` and ``argtype``.
    """
    def __init__(self, names, default = False, **kwargs):
        SwitchAttr.__init__(self, names, argtype = None, default = default, list = False, **kwargs)
    def __call__(self, _):
        self._value = not self._value

class CountOf(SwitchAttr):
    """A specialized :class:`SwitchAttr <plumbum.cli.SwitchAttr>` that counts the number of
    occurrences of the switch in the command line. Usage::

        class MyApp(Application):
            verbosity = CountOf(["-v", "--verbose"], help = "The more, the merrier")

    If ``-v -v -vv`` is given in the command-line, it will result in ``verbosity = 4``.

    :param names: The switch names
    :param default: The default value (0)
    :param kwargs: Any of the keyword arguments accepted by :func:`switch <plumbum.cli.switch>`,
                   except for ``list`` and ``argtype``.
    """
    def __init__(self, names, default = 0, **kwargs):
        SwitchAttr.__init__(self, names, argtype = None, default = default, list = True, **kwargs)
    def __call__(self, _, v):
        self._value = len(v)

#===================================================================================================
# Switch type validators
#===================================================================================================
class Range(object):
    """
    A switch-type validator that checks for the inclusion of a value in a certain range.
    Usage::

        class MyApp(Application):
            age = SwitchAttr(["--age"], Range(18, 120))

    :param start: The minimal value
    :param end: The maximal value
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __repr__(self):
        return "[%d..%d]" % (self.start, self.end)
    def __call__(self, obj):
        obj = int(obj)
        if obj < self.start or obj > self.end:
            raise ValueError("Not in range [%d..%d]" % (self.start, self.end))
        return obj

class Set(object):
    """
    A switch-type validator that checks that the value is contained in a defined
    set of values. Usage::

        class MyApp(Application):
            mode = SwitchAttr(["--mode"], Set("TCP", "UDP", case_insensitive = False))

    :param values: The set of values (strings)
    :param case_insensitive: A keyword argument that indicates whether to use case-sensitive
                             comparison or not. The default is ``True``
    """
    def __init__(self, *values, **kwargs):
        self.case_sensitive = kwargs.pop("case_sensitive", False)
        if kwargs:
            raise TypeError("got unexpected keyword argument(s): %r" % (kwargs.keys(),))
        self.values = dict(((v if self.case_sensitive else v.lower()), v) for v in values)
    def __repr__(self):
        return "{%s}" % (", ".join(repr(v) for v in self.values.values()))
    def __call__(self, obj):
        if not self.case_sensitive:
            obj = obj.lower()
        if obj not in self.values:
            raise ValueError("Expected one of %r" % (list(self.values.values()),))
        return self.values[obj]

class Predicate(object):
    def __str__(self):
        return self.__class__.__name__

class ExistingDirectory(Predicate):
    """A switch-type validator that ensures that the given argument is an existing directory"""
    def __call__(self, val):
        p = local.path(val)
        if not p.isdir():
            raise ValueError("%r is not a directory" % (val,))
        return p
ExistingDirectory = ExistingDirectory()

class ExistingFile(Predicate):
    """A switch-type validator that ensures that the given argument is an existing file"""
    def __call__(self, val):
        p = local.path(val)
        if not p.isfile():
            raise ValueError("%r is not a file" % (val,))
        return p
ExistingFile = ExistingFile()

class NonexistentPath(Predicate):
    """A switch-type validator that ensures that the given argument is an nonexistent path"""
    def __call__(self, val):
        p = local.path(val)
        if p.exists():
            raise ValueError("%r already exists" % (val,))
        return p
NonexistentPath = NonexistentPath()



