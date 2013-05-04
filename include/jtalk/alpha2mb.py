# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def alpha2mb(s):
	# 'abc' -> 'ａｂｃ'
	import string
	from_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	to_table = 'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
	result = ''
	for ch in s:
		pos = string.find(from_table, ch)
		if pos >= 0:
			result += to_table[pos]
	return result
