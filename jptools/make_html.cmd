python jpBrailleRunner.py -m
for /F "usebackq" %%t in (`python -c "from __future__ import print_function; import sys; print(sys.version_info[0])"`) do set PYTHONVERSION=%%t
if not "%PYTHONVERSION%"=="2" goto notpythontwo
python txt2tags.py -t xhtml --toc __jpBrailleHarness.t2t
python -c "import sys;lines = [line.strip() for line in sys.stdin.readlines()];import re;p = re.compile(r'<a href=\x22(mailto|http):[^>]+>([^<]+)</a>');print '\n'.join(map(lambda l:p.sub(r'\2', l), lines))" < __jpBrailleHarness.xhtml > jpBrailleHarness.xhtml
exit /b 0
:notpythontwo
python py3/txt2tags.py -t xhtml --toc jpBrailleHarness.xhtml
