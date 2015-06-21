# eng_dic_maker.py for nvdajp_jtalk
# -*- coding: utf-8 -*-
# since 2010-12-05 by Takuya Nishimoto
# bep-eng.dic is available at:
# http://cpansearch.perl.org/src/MASH/Lingua-JA-Yomi-0.01/lib/Lingua/JA/bep-eng.dic
from __future__ import unicode_literals

IN_FILE_DEFAULT = 'c:/work/nvda/bep-eng.dic'
OUT_FILE = 'nvdajp-eng-dic.csv'
DEFAULT_COST = 1600

import os
from os import path
from alpha2mb import alpha2mb

def make_dic(IN_FILE, CODE, THISDIR):
	import re
	d = [
		['alt', 	'オルト'],
		['acrobat', 'アクロバット'],
		['adobe', 	'アドビー', "1/4", 1000],
		['about', 	'アバウト', '2/4'],
		['ass', 	'アス', "1/2", 10000],
		['azure', 	'アジュール', None, 100],
		['api',     'エーピーアイ', None, 500],
		['animations',     'アニメイションズ'],
		['blank', 	'ブランク'],
		['biz', 	'ビズ'],
		['bazaar', 	'バザール'],
		['cam', 	'キャム'],
		['ctrl', 	'コントロール'],
		['console', 'コンソール'],
		['caps', 	'キャプス'],
		['cygwin', 	'シグウィン'],
		['choose',  'チュウズ', None, 1000],
		['delete', 	'デリート'],
		['del', 	'デリート'],
		['doxygen', 'ドキシゲン'],
		['explorer', 'エクスプローラ'],
		['esc', 	'エスケープ'],
		['enter', 	'エンター'],
		['editions', 'エディションズ'],
		['essentials', 'エセンシャルズ'],
		['extentions', 'エクステンションズ'],
		['firefox', 'ファイアフォックス'],
		['for', 	'フォー'],
		['foryou', 	'フォーユー'],
		['folders', 'フォルダーズ'],
		['favo', 'ファボ'],
		['failed', 'フェイルド'],
		['guide', 	'ガイド', None, 1000],
		['google', 	'グーグル'],
		['gnu', 	'グニュー'],
		['home', 	'ホーム'],
		['hub', 	'ハブ'],
		['href',	'エイチレフ'],
		['internet', 'インターネット'],
		['insert', 	'インサート'],
		['iis', 	'アイアイエス'],
		['impaired', 'インペアド'],
		['incorporate', 'インコーポレイト'],
		['incorporates', 'インコーポレイツ'],
		['java', 	'ジャバ'],
		['jaxa',    'ジャクサ'],
		['konica', 	'コニカ'],
		['kinect', 	'キネクト'],
		['kddi', 	'ケーディーディーアイ'],
		['manage',  'マネイジ', None, 1000],
		['micro', 	'マイクロ'],
		['mozilla', 'モジラ'],
		['media',   'メディア', "1/3", 1000],
		['mixi', 	'ミクシー'],
		['open', 	'オープン'],
		['office', 	'オフィス'],
		['operation', 	'オペレーション', None, 1000],
		['python', 	'パイソン'],
		['pro', 	'プロ'],
		['radio', 	'ラジオ', "1/3", 800],
		['shift', 	'シフト'],
		['skype', 	'スカイプ', "2/4"],
		['soft', 	'ソフト'],
		['setup',	'セットアップ'],
		['systems', 'システムズ'],
		['shared',  'シェアード'],
		['shares',  'シェアーズ'],
		['think', 	'シンク'],
		['threatened', 'スレッテンド'],
		['thoroughly', 'サラフリィ'],
		['talk', 	'トーク'],
		['tab', 	'タブ'],
		['tunes', 	'チューンズ', '1/4', 10],
		['tools', 	'ツールズ', '1/4'],
		['togetter', 	'トゥギャッター'],
		['tube', 	'チューブ', '1/3', 600],
		['update', 	'アップデート'],
		['ui', 	'ユーアイ'],
		['uac', 	'ユーエーシー'],
		['version', 'バージョン'],
		['versions', 'バージョンズ'],
		['vantage', 'バンテージ'],
		['wave', 	'ウェーブ'],
		['welcome', 'ウェルカム'],
		['windows', 'ウィンドウズ'],
		['xna',     'エクスエヌエー'],
		['you', 	'ユー', None, 660],
		['zune', 	'ズーン'],
		
		['dev',			'デブ'],
		['jis', 		'ジス', 			"1/2", 1000],
		['audio', 		'オーディオ', 		"1/4", 610],
		['suite', 		'スイート', 		"2/4", 1000],
		['opensource', 	'オープンソース', None, 1000],
		['notepad', 	'ノートパッド', None, 1000],
		['guidebook', 	'ガイドブック', None, 1000],
		['blog', 		'ブログ', None, 1000],
		['matlab', 		'マトラブ', None, 1000],
		['keyboard', 	'キーボード', None, 1000],
		['plugins', 	'プラグインズ', None, 1000],
		['facebook', 	'フェイスブック', None, 1000],
		['desktop', 	'デスクトップ', None, 1000],
		['output', 		'アウトプット', None, 1000],
		['nullsoft', 	'ヌルソフト', None, 1000],
		['cygdrive', 	'シグドライブ', None, 1000],
		['ustream', 	'ユーストリーム', None, 1000],
		['ubuntu', 		'ウブンツー', None, 1000],
		['ware', 		'ウェアー', None, 1000],
		['warranties', 		'ワランティーズ'],
		
		['time', 		'タイム', None, 1000],
		['home', 		'ホーム', None, 1000],
		['wikipedia', 	'ウイキペディーア',	"0/8", 1000],
		['tepco', 		'テプコ',			"1/3", 1000],
		['yahoo', 		'ヤフー',			"2/3", 1000],
		['japan', 		'ジャパン',		"2/3", 1000],
		['japanese', 	'ジャパニーズ',	"3/5", 900],
		['favorites',   'フェイバリッツ', "1/6"],
		['documents',   'ドキュメンツ', "1/5"],
		['settings',    'セッティングズ', "1/6"],
		['distributable', 'ディストリビュータブル', "5/9"],
		['redistributable', 'リディストリビュータブル', "6/10"],
		['app',         'アップ'],
		['types',       'タイプス'],
		['mouse',       'マウス', "1/3", 500],
		
		['pref', 		'プリフ',			"1/3", 1000],
		['anpi', 		'アンピ',			"1/3", 1000],
		['asian',		'アジアン',		"1/4", 1000],
		['asahi', 		'アサヒ',			"1/3", 1000],
		['edu',			'エデュー',		"1/3", 1000],
		['gamba', 		'ガンバ', 			"1/3", 1000],
		['genpatsu',	'ゲンパツ',		"1/4", 1000],
		['hinan', 		'ヒナン', 			"1/3", 1000],
		['horijun',		'ホリジュン',		"1/4", 1000],
		['inosenaoki',	'イノセナオキ',	"1/7", 1000],
		['kahoku', 		'カホク', 			"1/3", 1000],
		['kurogen',		'クロゲン',		"1/4", 1000],
		['medic', 		'メディック',		"1/4", 1000],
		['mizu',			'ミズ',			"2/2", 1000],
		['minpo', 		'ミンポー',		"1/4", 1000],
		['seikatsu',	'セーカツ',		"1/4", 1000],
		['sagasu',		'サガス',			"1/3", 1000],
		['shimpo', 		'シンポー', 		"1/4", 1000],
		['shimbun', 	'シンブン',		"1/4", 1000],
		['teiden', 		'テーデン',		"1/4", 1000],
		['tokuho',		'トクホー',		"1/4", 1000],
		['takeyama', 	'タケヤマ',		"1/4", 1000],
		['takeshi',		'タケシ',			"1/3", 1000],

		['hokkaido', 	'ホッカイドー', 	None, 1000],
		['yamagata', 	'ヤマガタ', None, 1000],
		['akita', 		'アキタ', None, 1000],
		['aomori', 		'アオモリ', None, 1000],
		['iwate', 		'イワテ', None, 1000],
		['tsukuba', 	'ツクバ', None, 1000],
		['oshu', 		'オーシュー', None, 1000],
		['hachinohe', 	'ハチノヘ', None, 1000],
		['kesennuma', 	'ケセンヌマ', None, 1000],
		['kantei', 		'カンテー', None, 1000],
		['saigai', 		'サイガイ', None, 1000],
		['tochigi', 	'トチギ', None, 1000],
		['kashima', 	'カシマ', None, 1000],
		['morioka', 	'モリオカ', 		"2/4", 1000],
		['miyagi', 		'ミヤギ',			"1/3", 1000],
		['fukushima', 	'フクシマ', 		"2/4", 1000],
		['niigata', 	'ニーガタ', 		"0/4", 1000],
		['asshuku',		'アッシュク',		"0/4",	],
		['mei',			'メイ',			"1/2", 100],
		
		['akb', 		'エーケービー',		"1/6", 1000],
		['npo', 		'エヌピーオー',		"2/6", 1000],
		['nec',			'エヌイーシー',		"1/6",	],
		['nvda', 		'エヌブイディーエー', 	"1/8", 1000],
		['nico', 		'ニコ', 				"1/2", 1000],
		['jp', 			'ジェーピー', 			"1/4", 1000],
		['co', 			'シーオー', 			"1/4", 1000],
		['usb', 		'ユーエスビー',		"1/6", 1000],
		['faq', 		'エフエーキュー',		"1/6", 1000],
		['iaea', 		'アイエーイーエー',	"7/8", 1000],
		['sjis', 		'エスジス', 			"0/4", 1000],
		['euc', 		'イーユーシー', 		"1/6", 1000],
		['au', 			'エーユー', 			"1/4", 600],
		['id', 			'アイディー', 			"3/4", 1000],
		#['it', 			'アイティー', 			"3/4", 1000],
		['adsl',		'エーディーエスエル'	"1/8",	],
		['ime',			'アイエムイー', 		"0/6", 600],
		['files',		'ファイルズ', 			"1/4", 600],
		['docs',		'ドックス', 			"1/4", 600],
		['page',		'ページ', 			"1/3", 600],
		['everyone', 'エブリワン', "1/5"],
		['users', 'ユーザーズ', "1/5"],
		['allowed', 'アラウド', "2/4"],
		['designed', 'デザインド', "2/5"],
		['database', 'デイタベイス', "1/5"],
		['butt', 'バットゥ', "1/4", 10000],
		['opened', 'オープンド', "1/5"],
		['closed', 'クローズド', "2/5"],
		['contributions', 'コントリビューションズ'],
		['layered', 'レイヤード', '1/5'],
		['required', 'リクワイアード', '3/7'],
		['iconified', 'アイコニファイド', '1/8'],
		['interactively', 'インタラクティブリィ'],
		['focusable', 'フォウカサブル', '1/6'],
		['editable', 'エディタブル', '1/5'],
		['draggable', 'ドゥラッガブル', '2/6'],
		['contains', 'コンテインズ', '3/6'],
		['covered', 'カバード', '1/4'],
		['considered', 'コンシダード'],
		['errors', 'エラーズ'],
		['previously', 'プリビアスリ'],
		['permission', 'パーミッション'],
		['entered', 'エンタード'],
		['turns', 'ターンズ'],
		['toggles', 'トグルズ'],
		['clicks', 'クリックス'],
		['unlocks', 'アンロックス'],
		['locks', 'ロックス'],
		['controls', 'コントゥロウルズ'],
		['currently', 'カレントリ'],
		['synth', 'シンセ'],
		['moves', 'ムーブズ'],
		['characters', 'キャラクターズ'],
		['keys', 'キーズ'],
		['cycles', 'サイクルズ'],
		['conspicuously', 'コンスピシャスリィ'],
		['changed', 'チェインジド'],
		['appropriately', 'アプロプリエトリィ'],
		['agreed', 'アグリード'],
		['levels', 'レベルズ'],
		['speaks', 'スピークス'],
		['simultaneously', 'サイマルテニアスリィ'],
		['untitled', 'アンタイトルド'],
		['flanger', 'フランジャー'],
		['resample', 'リサンプル'],
		['reuse', 'リユーズ'],
		['runs', 'ランズ'],
		['rendered', 'レンダード'],
		['inaccurate', 'インアキュレイト'],
		['epub', 'イーパブ'],
		['expressly', 'エクスプレスリィ'],
		['libre', 'リブレ'],
		['gpu', 'ジーピーユー'],
		['unicode', 'ユニコウドゥ'],
		['drivers', 'ドゥライバーズ'],
		['directly', 'ダイレクトリィ'],
		['unicode', 'ユニコウドゥ'],
		['usa',	'ユーエスエー', "0/6"],
		['unenforceable', 'アンエンフォーサブル'],
		['visum', 'ビズム'],
	]
	k = {}
	for i in d:
		k[i[0]] = True
	for line in open(IN_FILE):
		if line[0] == '#': continue
		a1, a2 = line.rstrip().decode('UTF-8').split(' ')
		a1 = re.sub("'", "\\'", a1)
		a1 = a1.lower()
		if not k.has_key(a1):
			d.append([a1, a2])
			k[a1] = True
	d.sort()
	with open(path.join(THISDIR, OUT_FILE), "w") as file:
		for i in d:
			k = i[0]
			# skip such as SHE'LL
			if "'" in k:
				continue
			alpha_count = len(k)
			k1 = alpha2mb(k.lower())
			y = i[1]
			# default pros
			mora_count = len(y)
			pros = "1/%d" % mora_count
			# default cost
			cost = DEFAULT_COST
			if alpha_count <= 2: cost = cost * 5
			# override by entry
			if len(i) >= 3:
				if i[2] != None: pros = i[2]
			if len(i) >= 4: cost = i[3]
			# 表層形,左文脈ID,右文脈ID,コスト,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
			s = "%s,,,%d,名詞,一般,*,*,*,*,%s,%s,%s,%s,C0\n" % (k1,cost,k1,y,y,pros)
			file.write(s.encode(CODE))

if __name__ == '__main__':
	make_dic(IN_FILE_DEFAULT)
