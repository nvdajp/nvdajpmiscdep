xcopy /E /Y .\jtalk ..\include\jtalk
xcopy /E /Y ..\include\htsengineapi ..\include\python-jtalk\htsengineapi
xcopy /E /Y ..\include\libopenjtalk ..\include\python-jtalk\libopenjtalk
copy /Y ..\include\python-jtalk\jtalkCore.py ..\source\synthDrivers\jtalk\jtalkCore.py
copy /Y ..\include\python-jtalk\mecab.py ..\source\synthDrivers\jtalk\mecab.py
copy /Y ..\include\python-jtalk\text2mecab.py ..\source\synthDrivers\jtalk\text2mecab.py
copy /Y ..\include\python-jtalk\jtalkRunner.py .\jtalkRunner.py

call ..\include\python-jtalk\vcsetup.cmd
cd /d %~dp0
cd ..\include\jtalk
call all-clean.cmd
@if not "%ERRORLEVEL%"=="0" goto onerror
call all-build.cmd
@if not "%ERRORLEVEL%"=="0" goto onerror
call all-install.cmd
@if not "%ERRORLEVEL%"=="0" goto onerror
cd ..\python-jtalk
call clean.cmd
cd ..\..\jptools
call test.cmd

exit /b 0

:onerror
exit /b -1
