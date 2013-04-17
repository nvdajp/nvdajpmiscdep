rem all-clean

cd htsengineapi
nmake -f Makefile.mak clean
cd ..
cd libopenjtalk
nmake -f Makefile.mak clean
cd ..

del libopenjtalk\lib\libopenjtalk-timestamp.h

cd libopenjtalk\mecab-naist-jdic
rmdir /S /Q dic
rmdir /S /Q _temp
del nvdajp-custom-dic.csv
del nvdajp-eng-dic.csv
del nvdajp-roma-dic.csv
del nvdajp-tankan-dic.csv
cd ..\..

