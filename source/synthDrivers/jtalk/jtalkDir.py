# -*- coding: utf-8 -*-
#A part of NonVisual Desktop Access (NVDA)
# speech engine nvdajp_jtalk
# Copyright (C) 2010-2014 Takuya Nishimoto (nishimotz.com)

import os
import sys

jtalk_dir = unicode(os.path.dirname(__file__), 'mbcs')
if hasattr(sys,'frozen'):
	d = os.path.join(os.getcwdu(), 'synthDrivers', 'jtalk')
	if os.path.isdir(d):
		jtalk_dir = d

dic_dir = os.path.join(jtalk_dir, 'dic')
