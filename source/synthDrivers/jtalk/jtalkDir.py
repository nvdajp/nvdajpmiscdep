# -*- coding: utf-8 -*-
# A part of NonVisual Desktop Access (NVDA)
# speech engine nvdajp_jtalk
# Copyright (C) 2010-2014 Takuya Nishimoto (nishimotz.com)

from __future__ import absolute_import

import os
import sys
from glob import glob
import tempfile
import shutil


getcwd = os.getcwd
encode_str = lambda s, c: s




jtalk_dir = encode_str(os.path.dirname(__file__), "mbcs")
if hasattr(sys, "frozen"):
    d = os.path.join(getcwd(), "synthDrivers", "jtalk")
    if os.path.isdir(d):
        jtalk_dir = d

configDir = getcwd()
try:
    import globalVars

    configDir = globalVars.appArgs.configPath
    d = os.path.join(
        globalVars.appArgs.configPath, "addons", "nvdajp_jtalk", "synthDrivers", "jtalk"
    )
    if os.path.isdir(d):
        jtalk_dir = d
except:
    pass

dic_dir = os.path.join(jtalk_dir, "dic")

user_dics_org = [
    os.path.normpath(d) for d in glob(os.path.join(configDir, "jtusr.dic"))
]

tempDir = encode_str(tempfile.mkdtemp(), "mbcs")
user_dics = []
for u in user_dics_org:
    b = os.path.basename(u)
    d = os.path.join(tempDir, b)
    shutil.copyfile(u, d)
    user_dics.append(d)
