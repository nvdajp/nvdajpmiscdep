rem build
cd ..\include
rmdir /s /q python-jtalk\htsengineapi
xcopy /e /i /h /k /x /y htsengineapi python-jtalk\htsengineapi
rmdir /s /q python-jtalk\libopenjtalk
xcopy /e /i /h /k /x /y libopenjtalk python-jtalk\libopenjtalk
cd python-jtalk
call build.cmd

rem dic-build
cd ..\..\jtalk
cd libopenjtalk\mecab\src
nmake -f Makefile.mak all
cd ..\..\..
python make_jdic.py
@if not "%ERRORLEVEL%"=="0" goto onerror

exit /b 0

:onerror
exit /b -1
