copy c:\work\nvda\jpmain\source\locale\ja\characters.dic characters-ja.dic
rem build
python make_timestamp.py
cd htsengineapi
nmake -f Makefile.mak
cd ..
cd libopenjtalk
nmake -f Makefile.mak
cd ..
rem mecab-dict-index
cd libopenjtalk\mecab\src
nmake -f Makefile.mak all
cd ..\..\..
rem dic-build
python make_jdic.py
