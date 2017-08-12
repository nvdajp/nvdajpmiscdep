# tankan_dic_maker.py for nvdajp_jtalk
# -*- coding: utf-8 -*-
# since 2010-12-20 by Takuya Nishimoto
from __future__ import unicode_literals

# IN_DIR : location of nvdajp_dic.py
# IN_DIR  = '/work/nvda/jp2011.1/source'
OUT_FILE = 'nvdajp-tankan-dic.csv'

import re
import os
from os import path

def contains_hankaku_katakana(k):
	# hankaku katakana check
	# http://programmer-toy-box.sblo.jp/article/24644519.html
	regexp = re.compile(r'(?:\xEF\xBD[\xA1-\xBF]|\xEF\xBE[\x80-\x9F])|[\x20-\x7E]')
	result = regexp.search(k.encode('utf-8'))
	if result: return True
	return False

def read_characters_file(cs_file):
	with open(cs_file) as ch:
		ar = {}
		c = 0
		for line in ch:
			c += 1
			line = line.rstrip().decode('utf-8')
			if len(line) == 0: continue
			#print line.encode('cp932', 'ignore')
			if line[0] == '#': continue
			if line[0:2] == '\\#': 
				line = '#' + line[2:]
			a = line.split('\t')
			if len(a) >= 2 and a[2].startswith('[') and a[2].endswith(']'):
				k = a[0]
				rd = a[2][1:-1]
				# braille pattern ⣿
				#if 0x2800 <= ord(k) and ord(k) <= 0x28ff: continue
				rd = rd.replace('0', 'ゼロ')
				rd = rd.replace('1', 'イチ')
				rd = rd.replace('2', 'ニー')
				rd = rd.replace('3', 'サン')
				rd = rd.replace('4', 'ヨン')
				rd = rd.replace('5', 'ゴー')
				rd = rd.replace('6', 'ロク')
				rd = rd.replace('7', 'ナナ')
				rd = rd.replace('8', 'ハチ')
				rd = rd.replace('9', 'キュー')
				ar[k] = rd
	return ar

def make_dic(CODE, CS_FILE, THISDIR):
	char_dic = read_characters_file(CS_FILE)
	print 'char_dic %d' % len(char_dic)
	import csv
	jdic_tankan = {}
	reader = csv.reader(open(path.join(THISDIR, "naist-jdic.csv"), 'r'))
	for row in reader:
		hyousou = row[0].decode('euc-jp') # naist-jdic.csv is euc-jp
		if len(hyousou) == 1:
			if hyousou == '盲': continue
			if hyousou == '聾': continue
			jdic_tankan[hyousou] = row
	with open(path.join(THISDIR, OUT_FILE), "w") as file:
		for k,v in char_dic.items():
			if contains_hankaku_katakana(k): continue
			if k in jdic_tankan:
				continue # print "%s in hyousou" % k.encode(CODE)
			try:
				dummy = k.encode(CODE)
			except Exception, e:
				print e
				continue
			k1 = k
			y = v
			# ー,,,5000,名詞,サ変接続,*,*,*,*,ー,チョーオン,チョーオン,0/5,C0
			if k1 == 'ー':
				continue
			if 'コモジノ' in y:
				continue
			y = y.replace(' ', '')
			mora_count = len(y)
			cost = 15000
			# 表層形,左文脈ID,右文脈ID,コスト,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
			# 名詞,普通名詞
			s = "%s,,,%d,名詞,サ変接続,*,*,*,*,%s,%s,%s,0/%d,C0" % (k1,cost,k1,y,y,mora_count)
			# braille pattern
			if len(k1) == 1 and 0x2800 <= ord(k1) <= 0x28ff:
				s += ",%s" % k1
			s += "\n"
			file.write(s.encode(CODE))

if __name__ == '__main__':
	make_dic('utf-8')
