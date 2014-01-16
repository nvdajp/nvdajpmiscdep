rem build
cd ..\python-jtalk
call build.cmd

rem dic-build
cd ..\jtalk
cd libopenjtalk\mecab\src
nmake -f Makefile.mak all
cd ..\..\..
python make_jdic.py
