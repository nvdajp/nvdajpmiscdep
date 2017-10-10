# coding: utf-8
# make_jdic.py
# Copyright (C) 2010-2013 Takuya Nishimoto (NVDA Japanese Team)

from __future__ import unicode_literals, print_function
import os
from os import path
import shutil
import subprocess
from datetime import datetime
import errno

import eng_dic_maker
import tankan_dic_maker
import custom_dic_maker
from filter_jdic import filter_jdic

# MECAB_DICT_INDEX と OUTDIR は libopenjtalk/mecab-naist-jdic/_temp が基準
JTDIR = path.dirname(path.abspath(__file__))
ENGDIC = path.normpath(path.join(JTDIR, "bep-eng.dic"))
CS_FILE = path.normpath(path.join(JTDIR, "characters-ja.dic"))

#THISDIR = path.normpath(path.join(JTDIR, "..", "python-jtalk", "libopenjtalk", "mecab-naist-jdic"))
THISDIR = path.normpath(path.join(JTDIR, "libopenjtalk", "mecab-naist-jdic"))
OUTDIR = path.normpath(path.join(THISDIR, "dic"))
TEMPDIR = path.normpath(path.join(THISDIR, "_temp"))
MECAB_DICT_INDEX = path.normpath(path.join(THISDIR, "..", "mecab", "src", "mecab-dict-index.exe"))

CODE = 'utf-8' # cp932

def mkdir_p(path):
	try:
		os.makedirs(path)
	except OSError as exc:
		if exc.errno == errno.EEXIST:
			pass
		else: raise exc

mkdir_p(OUTDIR)
mkdir_p(TEMPDIR)

eng_dic_maker.make_dic(ENGDIC, CODE, THISDIR)
tankan_dic_maker.make_dic(CODE, CS_FILE, THISDIR)
custom_dic_maker.make_dic(CODE, THISDIR)

def convert_file(src_file, src_enc, dest_file, dest_enc):
	print("converting %s to %s" % (src_file, dest_file))
	with open(src_file) as sf:
		with open(dest_file, "w") as df:
			while 1:
				s = sf.readline()
				if not s:
					break
				s = s.decode(src_enc)
				df.write(s.encode(dest_enc))

def convert_jdic_file(src_file, src_enc, dest_file, dest_enc):
	print("converting %s to %s" % (src_file, dest_file))
	with open(src_file) as sf:
		with open(dest_file, "w") as df:
			while 1:
				s = sf.readline()
				if not s:
					break
				s = s.decode(src_enc).rstrip()
				s = filter_jdic(s)
				if s:
					s += "\n" # do not use os.linesep here
					df.write(s.encode(dest_enc))

files = ['dicrc',
		 'nvdajp-eng-dic.csv','nvdajp-tankan-dic.csv',
		 'nvdajp-custom-dic.csv',
		 ]

euc_files = ['char.def','feature.def','left-id.def','matrix.def',
	'pos-id.def','rewrite.def','right-id.def', 'unk.def']

jdic_file = 'naist-jdic.csv'

for f in files:
	print("copy %s to %s" % (path.join(THISDIR, f), TEMPDIR))
	shutil.copy(path.join(THISDIR, f), TEMPDIR)

for f in euc_files:							 
	convert_file(path.join(THISDIR, f), 'euc-jp', path.join(TEMPDIR, f), CODE)

convert_jdic_file(path.join(THISDIR, jdic_file), 'euc-jp', path.join(TEMPDIR, jdic_file), CODE)

print(TEMPDIR, [MECAB_DICT_INDEX, '-d','.', '-o',OUTDIR, '-f',CODE, '-c',CODE])
subprocess.check_call([MECAB_DICT_INDEX, '-d','.', '-o',OUTDIR, '-f',CODE, '-c',CODE], cwd=TEMPDIR)

print("copy %s to %s" % (path.join(THISDIR, 'dicrc'), OUTDIR))
shutil.copy(path.join(THISDIR, 'dicrc'), OUTDIR)
dic_version_file = path.join(OUTDIR, "DIC_VERSION")
print("dic version file: " + dic_version_file)
version = "nvdajp-jtalk-dic " + '(' + CODE + ') ' + datetime.utcnow().strftime('%Y%m%d-%H%M%S')
print(version)
with open(dic_version_file, "wb") as f:
	f.write(version + os.linesep) 

# end of file
