# _nvdajp_unicode.py 
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unicodedata

def unicode_normalize(s):
	s = s.replace('\u00a0', ' ')  # Unicode no break space
	s = s.replace('\u2002', ' ')  # Unicode en space
	s = s.replace('\u2003', ' ')  # Unicode em space
	s = s.replace('\u2004', ' ')  # Unicode 1/3 em space
	s = s.replace('\u2005', ' ')  # Unicode 1/4 em space
	s = s.replace('\u2009', ' ')  # Unicode 1/5 em space
	s = s.replace('\u2006', ' ')  # Unicode 1/6 em space
	s = s.replace('\u2007', ' ')  # Unicode figure space
	s = s.replace('\u2008', ' ')  # Unicode punctuation space
	s = s.replace('\u200a', ' ')  # Unicode hair space
	#              \u200b           Unicode zero width space
	s = s.replace('\u200e', '')   # Unicode LEFT-TO-RIGHT MARK
	s = s.replace('\u200f', '')   # Unicode RIGHT-TO-LEFT MARK
	s = s.replace('\ufffd', '')   # Unicode REPLACEMENT CHARACTER
	# Mecab_text2mecab() で全角に変換され NFKC で戻せない文字
	s = s.replace('．', '.')
	s = unicodedata.normalize('NFKC', s)
	s = s.replace('\u2212', '-')  # 0x2212 MUNUS SIGN to 0x002D HYPHEN-MINUS
	s = s.replace('\u00a5', '\\') # 0x00A5 YEN SIGN
	s = s.replace('\u301c', '~')  # 0x301C WAVE DASH
	s = s.replace('é', 'e')       # 0x00e9
	return s

