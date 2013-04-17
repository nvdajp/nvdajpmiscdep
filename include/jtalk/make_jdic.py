# coding: utf-8
# make_jdic.py
# Copyright (C) 2010-2013 Takuya Nishimoto (NVDA Japanese Team)

from __future__ import unicode_literals
import os
from os import path
import shutil
import subprocess
from datetime import datetime
import errno

import eng_dic_maker
import tankan_dic_maker
import custom_dic_maker
import roma_dic_maker

# MECAB_DICT_INDEX と OUTDIR は libopenjtalk/mecab-naist-jdic/_temp が基準
THISDIR = path.join(path.dirname(path.abspath(__file__)), "libopenjtalk", "mecab-naist-jdic")
OUTDIR = path.normpath(path.join(THISDIR, "dic"))
TEMPDIR = path.normpath(path.join(THISDIR, "_temp"))
ENGDIC = path.normpath(path.join(path.dirname(path.abspath(__file__)), "bep-eng.dic"))
MECAB_DICT_INDEX = path.normpath(path.join(THISDIR, "..", "mecab", "src", "mecab-dict-index.exe"))
CS_FILE = path.join(path.dirname(path.abspath(__file__)), "characters-ja.dic")

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
roma_dic_maker.make_dic(CODE, THISDIR)

def convert_file(src_file, src_enc, dest_file, dest_enc):
	print "converting %s to %s" % (src_file, dest_file)
	with open(src_file) as sf:
		with open(dest_file, "w") as df:
			while 1:
				s = sf.readline()
				if not s:
					break
				s = s.decode(src_enc)
				df.write(s.encode(dest_enc))

# 0:表層形,1:左文脈ID,2:右文脈ID,3:コスト,
# 4:品詞,5:品詞細分類1,6:品詞細分類2,7:品詞細分類3,
# 8:活用形,9:活用型,10:原形,11:読み,12:発音,
# 13:アクセント位置/モーラ数,14:アクセント属性, (Open JTalk の拡張情報)
# 15:点訳 (拡張情報)
def filter_jdic(s):
	a = s.split(',')
	if a[0] == '盲' and a[11] == 'メクラ':
		a[11], a[12], a[13] = "モウ", "モー", "1/2"
		s = ",".join(a)
	elif a[0] == '聾' and a[11] == 'ツンボ':
		a[11], a[12], a[13] = "ロウ", "ロー", "1/2"
		s = ",".join(a)
	elif a[0] == 'ｚ' and a[11] == 'ズィー':
		s = ""
	elif a[0] == '規' and a[11] == 'ブンマワシ':
		s = ""
	elif a[0] == '全' and a[11] == 'チョン':
		s = ""
	elif a[0] == '００７' and a[11] == 'ゼロゼロセブン':
		s = ""
	elif a[0] == '未曾有' and a[12] == 'ミゾー':
		a[12] = 'ミゾウ'
		s = ",".join(a)
	elif a[0] == '言う' and a[12] == 'ユウ':
		a[12] = 'イウ'
		s = ",".join(a)
	elif a[0] == 'まごう' and a[12] == 'マゴウ':
		a[12] = 'マゴー'
		s = ",".join(a)
	elif a[0] == 'ゆう' and a[12] == 'ユウ':
		a[12] = 'ユー'
		s = ",".join(a)
	elif a[0] == '思う' and a[12] == 'オモウ':
		a[12] = 'オモー'
		s = ",".join(a)
	elif a[0] == '吸う' and a[12] == 'スウ':
		a[12] = 'スー'
		s = ",".join(a)
	elif a[0] == '繕う' and a[12] == 'ツクロウ':
		a[12] = 'ツクロー'
		s = ",".join(a)
	elif a[0] == '大きい' and a[12] == 'オーキイ':
		a[12] = 'オオキイ'
		s = ",".join(a)
	elif a[0] == '仰せ' and a[12] == 'オーセ':
		a[12] = 'オオセ'
		s = ",".join(a)
	elif a[0] == 'おおせる' and a[12] == 'オーセル':
		a[12] = 'オオセル'
		s = ",".join(a)
	elif a[0] == '車前草' and a[12] == 'オーバコ':
		a[12] = 'オオバコ'
		s = ",".join(a)
	elif a[0] == '概ね' and a[12] == 'オームネ':
		a[12] = 'オオムネ'
		s = ",".join(a)
	elif a[0] == '公' and a[12] == 'オーヤケ':
		a[12] = 'オオヤケ'
		s = ",".join(a)
	elif a[0] == '氷' and a[12] == 'コーリ':
		a[12] = 'コオリ'
		s = ",".join(a)
	elif a[0] == '凍る' and a[12] == 'コール':
		a[12] = 'コオル'
		s = ",".join(a)
	elif a[0] == '滞る' and a[12] == 'トドコール':
		a[12] = 'トドコオル'
		s = ",".join(a)
	elif a[0] == '憤る' and a[12] == 'イキドール':
		a[12] = 'イキドオル'
		s = ",".join(a)
	elif a[0] == '蟋蟀' and a[12] == 'コーロギ':
		a[12] = 'コオロギ'
		s = ",".join(a)
	elif a[0] == '遠い' and a[12] == 'トーイ':
		a[12] = 'トオイ'
		s = ",".join(a)
	elif a[0] == '通る' and a[12] == 'トール':
		a[12] = 'トオル'
		s = ",".join(a)
	elif a[0] == '頬' and a[12] == 'ホー':
		a[12] = 'ホオ'
		s = ",".join(a)
	elif a[0] == '酸漿' and a[12] == 'ホーズキ':
		a[12] = 'ホオズキ'
		s = ",".join(a)
	elif a[0] == '大目' and a[12] == 'オーメ':
		a[12] = 'オオメ'
		s = ",".join(a)
	elif a[0] == '大通り' and a[12] == 'オードーリ':
		a[12] = 'オオドオリ'
		s = ",".join(a)
	elif a[0] == '凍り付く' and a[12] == 'コーリツク':
		a[12] = 'コオリツク'
		s = ",".join(a)
	elif a[0] == '遠ざかる' and a[12] == 'トーザカル':
		a[12] = 'トオザカル'
		s = ",".join(a)
	elif a[0] == '通す' and a[12] == 'トース':
		a[12] = 'トオス'
		s = ",".join(a)
	elif a[0] == '頬張る' and a[12] == 'ホーバル':
		a[12] = 'ホオバル'
		s = ",".join(a)
	elif a[0] == 'いとおしい' and a[12] == 'イトーシイ':
		a[12] = 'イトオシイ'
		s = ",".join(a)
	elif a[0] == '凡そ' and a[12] == 'オヨソ':
		a[11] = a[12] = 'オオヨソ'
		a[13] = '0/4'
		s = ",".join(a)
	elif a[0] == '無花果' and a[12] == 'イチジュク':
		a[11] = a[12] = 'イチジク'
		s = ",".join(a)
	elif a[0] == '鼓' and a[12] == 'コ':
		a[11] = a[12] = 'ツヅミ'
		s = ",".join(a)
	elif a[0] == '葛籠' and a[12] == 'ツズロ':
		s = ""
	elif a[0] == '葛籠' and a[12] == 'ツズラ':
		a[12] = 'ツヅラ'
		s = ",".join(a)
	elif a[0] == '提灯' and a[12] == 'ヂョウチン':
		a[11] = a[12] = 'ヂョーチン'
		s = ",".join(a)
	elif a[0] == '青梅' and a[12] == 'オウメ':
		a[11] = a[12] = 'オーメ'
		s = ",".join(a)
	elif a[0] == 'クヮルテット' and a[12] == 'クヮルテット':
		a[11] = a[12] = 'クァルテット'
		s = ",".join(a)
	elif a[0] == 'スェーター' and a[12] == 'スェーター':
		a[11] = a[12] = 'スエーター'
		s = ",".join(a)
	elif a[0] == '憤る' and a[12] in ('ムズカル', 'ムツカル'):
		s = ""
	elif a[0] == 'いひ' and a[12] in ('ユイ', 'イイ'):
		s = ""
	elif a[0] == '八幡平' and a[12] == 'ヤワタダイラ':
		s = ""
	elif a[0] == '好かん' and a[12] == 'コーカン':
		s = ""
	elif a[0] == 'おおきに' and a[12] == 'オーキニ':
		s = s + "," + a[11]
	elif a[0] == 'かほる' and a[11] == 'カホル' and a[12] == 'カオル':
		s = s + "," + a[11]
	elif a[0] == 'かほる' and a[11] == 'カホル' and a[12] == 'カホル':
		s = ""
	elif a[0] == 'さをり' and a[12] == 'サオリ':
		s = s + "," + a[11]
	elif a[0] == '透' and a[12] == 'トール':
		s = s + "," + a[11]
	elif a[0] == '大阪' and a[12] == 'オーサカ':
		s = s + "," + a[11]
	elif a[0] == '遠野' and a[12] == 'トーノ':
		s = s + "," + a[11]
	elif a[0] == 'みさを' and a[12] == 'ミサオ':
		s = s + "," + a[11]
	elif a[0] == 'そういう' and a[12] == 'ソーユウ':
		s = s + ",ソー イウ"
	elif a[0] == 'どうして' and a[12] == 'ドーシテ':
		s = s + ",ドー シテ"
	elif a[0] == 'フィードバック' and len(a) == 15:
		a.append('フィード バック')
		a[11] = a[12] = a[15].replace(' ', '')
		s = ",".join(a)
	elif a[0] == 'インターフェース' and len(a) == 15:
		a.append('インター フェース')
		a[11] = a[12] = a[15].replace(' ', '')
		s = ",".join(a)
	elif a[0] == 'オペレーティングシステム' and len(a) == 15:
		a.append('オペレーティング システム')
		a[11] = a[12] = a[15].replace(' ', '')
		s = ",".join(a)
	elif a[0] == 'アイスクリーム' and len(a) == 15:
		a.append('アイス クリーム')
		a[11] = a[12] = a[15].replace(' ', '')
		s = ",".join(a)
	elif a[0] == '日本点字図書館' and len(a) == 15:
		a.append('ニッポン テンジ トショカン')
		a[11] = a[12] = a[15].replace(' ', '')
		s = ",".join(a)
	elif a[0] == '通り' and a[11] == 'トオリ' and len(a) == 15:
		a.append(a[11])
		s = ",".join(a)
	elif a[0] == '狼' and a[11] == 'オオカミ' and len(a) == 15:
		a.append(a[11])
		s = ",".join(a)
	elif a[0] == '多い' and a[11] == 'オオイ' and len(a) == 15:
		a.append(a[11])
		s = ",".join(a)
	elif a[0] == '多く' and a[11] == 'オオク' and len(a) == 15:
		a.append(a[11])
		s = ",".join(a)
	elif a[0] == '大晦日' and a[11] == 'オオミソカ' and len(a) == 15:
		a.append(a[11])
		s = ",".join(a)
	elif a[0] == '手作り' and a[11] == 'テヅクリ' and len(a) == 15:
		a.append(a[11])
		s = ",".join(a)
	elif a[0] == '南半球' and len(a) == 15:
		a.append('ミナミ ハンキュー')
		s = ",".join(a)
	elif a[0] == 'アメリカ合衆国' and len(a) == 15:
		a.append('アメリカ ガッシューコク')
		s = ",".join(a)
	elif a[0] == '第一人者' and len(a) == 15:
		a.append('ダイ1ニンシャ')
		s = ",".join(a)
	elif a[0] == '一流' and len(a) == 15:
		a.append('1リュー')
		s = ",".join(a)
	elif a[0] == '一月' and len(a) == 15:
		a.append('1ガツ')
		s = ",".join(a)
	elif a[0] == '二月' and len(a) == 15:
		a.append('2ガツ')
		s = ",".join(a)
	elif a[0] == '四方' and len(a) == 15:
		a.append('4ホー')
		s = ",".join(a)
	elif a[0] == '六法全書' and len(a) == 15:
		a.append('6ポー ゼンショ')
		s = ",".join(a)
	elif a[0] == '百人一首' and len(a) == 15:
		a.append('100ニン 1シュ')
		s = ",".join(a)
	elif a[0] == '日本コロムビア' and len(a) == 15:
		a.append('ニッポン コロムビア')
		a[11] = a[12] = a[15].replace(' ', '')
		s = ",".join(a)
	elif a[0] == 'ビタミンＥ' and len(a) == 15:
		a.append('ビタミン E')
		s = ",".join(a)
	elif a[0] == '劇団四季' and len(a) == 15:
		a.append('ゲキダン 4キ')
		s = ",".join(a)
	elif a[0] == '四季' and len(a) == 15:
		a.append('4キ')
		s = ",".join(a)
	elif a[0] == '四半期' and len(a) == 15:
		a.append('4ハンキ')
		s = ",".join(a)
	elif a[0] == '四角形' and len(a) == 15:
		a.append('4カクケイ')
		s = ",".join(a)
	elif a[0] == '四条' and len(a) == 15:
		a.append('4ジョー')
		s = ",".join(a)
	elif a[0] == '二男' and len(a) == 15:
		a.append('2ナン')
		s = ",".join(a)
	elif a[0] == '十数' and len(a) == 15:
		a.append('10スー')
		s = ",".join(a)
	elif a[0] == '一輪車' and len(a) == 15:
		a.append('1リンシャ')
		s = ",".join(a)
	elif a[0] == '三塁打' and len(a) == 15:
		a.append('3ルイダ')
		s = ",".join(a)
	elif a[0] == '一汁一菜' and len(a) == 15:
		a.append('1ジュー 1サイ')
		s = ",".join(a)
	elif a[0] == '五臓六腑' and len(a) == 15:
		a.append('5ゾー 6プ')
		s = ",".join(a)
	elif a[0] == '一段' and len(a) == 15:
		a.append('1ダン')
		s = ",".join(a)
	elif a[0] == '七転び八起き' and len(a) == 15:
		a.append('ナナコロビ ヤオキ')
		s = ",".join(a)
	elif a[0] == '十重二十重' and len(a) == 15:
		a.append('トエ ハタエ')
		s = ",".join(a)
	elif a[0] == '３ラン' and len(a) == 15:
		a.append('3ラン')
		s = ",".join(a)
	elif a[0] == 'さんりんしゃ' and len(a) == 15:
		a.append('3リンシャ')
		s = ",".join(a)
	elif a[0] == 'いちばん' and len(a) == 15:
		a.append('1バン')
		s = ",".join(a)
	elif a[0] == 'Ｘ線' and len(a) == 15:
		a.append('Xセン')
		s = ",".join(a)
	elif a[0] == '二・二六事件' and len(a) == 15:
		a.append('2⠼26 ジケン')
		s = ",".join(a)
	elif a[0] == 'Ｂ５判' and len(a) == 15:
		a.append('B5ハン')
		s = ",".join(a)
	elif a[0] == 'この間' and a[12] == 'コノカン':
		s = ""
	elif a[0] == 'インターネット' and len(a) == 15:
		a.append('インター ネット')
		s = ",".join(a)
	elif a[0] == '各党' and len(a) == 15:
		a.append('カク トー')
		s = ",".join(a)
	return s

def convert_jdic_file(src_file, src_enc, dest_file, dest_enc):
	print "converting %s to %s" % (src_file, dest_file)
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
		 'nvdajp-custom-dic.csv','nvdajp-roma-dic.csv',
		 ]

euc_files = ['char.def','feature.def','left-id.def','matrix.def',
	'pos-id.def','rewrite.def','right-id.def', 'unk.def']

jdic_file = 'naist-jdic.csv'

for f in files:
	print "copy %s to %s" % (path.join(THISDIR, f), TEMPDIR)
	shutil.copy(path.join(THISDIR, f), TEMPDIR)

for f in euc_files:							 
	convert_file(path.join(THISDIR, f), 'euc-jp', path.join(TEMPDIR, f), CODE)

convert_jdic_file(path.join(THISDIR, jdic_file), 'euc-jp', path.join(TEMPDIR, jdic_file), CODE)

print TEMPDIR, [MECAB_DICT_INDEX, '-d','.', '-o',OUTDIR, '-f',CODE, '-c',CODE]
subprocess.check_call([MECAB_DICT_INDEX, '-d','.', '-o',OUTDIR, '-f',CODE, '-c',CODE], cwd=TEMPDIR)

print "copy %s to %s" % (path.join(THISDIR, 'dicrc'), OUTDIR)
shutil.copy(path.join(THISDIR, 'dicrc'), OUTDIR)
dic_version_file = path.join(OUTDIR, "DIC_VERSION")
print "dic version file: " + dic_version_file
version = "nvdajp-jtalk-dic " + '(' + CODE + ') ' + datetime.utcnow().strftime('%Y%m%d-%H%M%S')
print version
with open(dic_version_file, "wb") as f:
	f.write(version + os.linesep) 

# end of file
