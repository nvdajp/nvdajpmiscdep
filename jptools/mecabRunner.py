# mecabRunner.py 
# -*- coding: utf-8 -*-
# Japanese text processor test module
# by Takuya Nishimoto

from __future__ import unicode_literals
import os
import sys
from glob import glob
from mecabHarness import tasks
jt_dir = os.path.normpath(
	os.path.join(os.getcwdu(), '..', 'source', 'synthDrivers', 'jtalk')
	)
sys.path.append(jt_dir)
from mecab import *
import jtalkDir

dic = os.path.join(jt_dir, 'dic')
user_dics_org = jtalkDir.user_dics_org
user_dics = jtalkDir.user_dics

def __print(s):
	print s.encode('utf-8', 'ignore')

_buffer = ''

def clear_morph_buffer():
	global _buffer
	_buffer = ''
	
def print_morph_buffer():
	__print(_buffer)
	
def __print_dummy(s):
	global _buffer
	_buffer += s + '\n'

def Mecab_get_reading(mf, CODE_=CODE):
	reading = ''
	braille = ''
	for pos in xrange(0, mf.size):
		ar = Mecab_getFeature(mf, pos, CODE_=CODE_).split(',')
		rd = ''
		if len(ar) > 9:
			rd = ar[9].replace('\u3000', ' ')
		elif ar[0] != 'ー':
			rd = ar[0]
		reading += rd
		if len(ar) > 12:
			braille += ar[12] + r"/"
		else:
			braille += rd + r"/"
	return (reading, braille.rstrip(r" /"))

def get_reading(msg):
	s = text2mecab(msg)
	mf = MecabFeatures()
	Mecab_analysis(s, mf)
	Mecab_correctFeatures(mf)
	Mecab_print(mf, logwrite_=__print_dummy)
	Mecab_print(mf)
	reading = Mecab_get_reading(mf)
	mf = None
	return reading

def runTasks(enableUserDic=False):
	if enableUserDic:
		print jt_dir, dic, user_dics
		Mecab_initialize(__print, jt_dir, dic, user_dics)
	else:
		print jt_dir, dic
		Mecab_initialize(__print, jt_dir, dic)
	count = 0
	for i in tasks:
		if isinstance(i, dict):
			if 'braille' in i:
				if 'speech' in i:
					item = [ i['text'], i['speech'], i['braille'] ]
				else:
					s = i['braille'].replace(' ', '').replace('/', '')
					item = [ i['text'], s, i['braille'] ]
			elif 'input' in i:
				if 'speech' in i:
					item = [ i['text'], i['speech'], i['input'] ]
				else:
					s = i['input'].replace(' ', '').replace('/', '')
					item = [ i['text'], s, i['input'] ]
			else:
				item = [ i['text'], i['speech'] ]
		else:
			item = i
		clear_morph_buffer()
		result = get_reading(item[0])
		if item[1] is not None and result[0] != item[1]:
			__print('')
			__print('')
			print_morph_buffer()
			__print('input:    ' + item[0])
			__print('reading expected: ' + item[1])
			__print('reading result:   ' + result[0])
			count += 1
		if len(item) > 2 and result[1] != item[2]:
			__print('')
			__print('')
			print_morph_buffer()
			__print('input:            ' + item[0])
			__print('braille expected: ' + item[2])
			__print('braille result:   ' + result[1])
			count += 1

	return count

if __name__ == '__main__':
	runTasks(enableUserDic=True)
