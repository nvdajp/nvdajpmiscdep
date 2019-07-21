# -*- coding: utf-8 -*-
#A part of NonVisual Desktop Access (NVDA)
# speech engine nvdajp_jtalk
# Copyright (C) 2010-2014 Takuya Nishimoto (nishimotz.com)

import os
import sys
from glob import glob
import tempfile
import shutil

if sys.version_info[0] > 2:
	getcwd = os.getcwd
	encode_str = lambda s, c : s
else:
	getcwd = os.getcwdu
	encode_str = lambda s, c : unicode(s, c)

jtalk_dir = encode_str(os.path.dirname(__file__), 'mbcs')
if hasattr(sys,'frozen'):
	d = os.path.join(getcwd(), 'synthDrivers', 'jtalk')
	if os.path.isdir(d):
		jtalk_dir = d

dic_dir = os.path.join(jtalk_dir, 'dic')

configDir = getcwd()
try:
	import globalVars
	configDir = globalVars.appArgs.configPath
except:
	pass
user_dics_org = [os.path.normpath(d) for d in glob(os.path.join(configDir, 'jtusr.dic'))]

tempDir = encode_str(tempfile.mkdtemp(), 'mbcs')
user_dics = []
for u in user_dics_org:
	b = os.path.basename(u)
	d = os.path.join(tempDir, b)
	shutil.copyfile(u, d)
	user_dics.append(d)
