if exist "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\vcvars32.bat" goto x64
call "C:\Program Files\Microsoft Visual Studio 14.0\VC\bin\vcvars32.bat"
goto done
:x64
call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\vcvars32.bat"
:done

del __*.txt
del *.pyc
del jtusr.dic
del ..\source\synthDrivers\jtalk\*.pyc
del ..\source\synthDrivers\jtalk\dic\DIC_VERSION
del ..\source\synthDrivers\jtalk\dic\*.dic
del ..\source\synthDrivers\jtalk\libopenjtalk.dll
cd ..\include\jtalk
call all-clean.cmd
cd ..\..\jptools
