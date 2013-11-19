# jtalkRunner.py
# -*- coding: utf-8 -*-
# Japanese speech engine test module
# by Takuya Nishimoto
# http://ja.nishimotz.com/project:libopenjtalk
# Usage:
# > cd source
# > python synthDrivers/jtalk/_jtalk_runner.py
# requires pyaudio (PortAudio wrapper)
# http://people.csail.mit.edu/hubert/pyaudio/

from __future__ import unicode_literals, print_function
import os
import sys
import wave
import time
import pyaudio
import cProfile
import pstats
sys.path.append(r'..\source\synthDrivers\jtalk')
from _jtalk_core import *
import _nvdajp_predic 

JT_DIR = r'..\source\synthDrivers\jtalk'
JT_DLL = os.path.join(JT_DIR, 'libopenjtalk.dll')
VOICE_DIR = os.path.join(JT_DIR, 'm001')

def pa_play(data, samp_rate = 16000):
	p = pyaudio.PyAudio()
	stream = p.open(format = p.get_format_from_width(2),
		channels = 1, rate = samp_rate, output = True)
	size = len(data)
	pos = 0 # byte count
	while pos < size:
		a = stream.get_write_available() * 2
		o = data[pos:pos+a]
		stream.write(o)
		pos += a
	time.sleep(float(size) / 2 / samp_rate)
	stream.close()
	p.terminate()

def __print(s):
	print(s.encode('cp932', 'ignore'))

def print_code(msg):
	s = ''
	for c in msg:
		s += '%04x ' % ord(c)
	print(s)

def do_synthesis(msg, voice_args, do_play):
	msg = _nvdajp_predic.convert(msg)
	s = Mecab_text2mecab(msg, CODE_='utf-8')
	__print("utf-8: (%s)" % s.decode('utf-8', 'ignore'))
	mf = MecabFeatures()
	Mecab_analysis(s, mf)
	Mecab_print(mf, __print, CODE_='utf-8')
	Mecab_correctFeatures(mf, CODE_='utf-8')
	fperiod = voice_args['fperiod']
	data_array = []
	ar = Mecab_splitFeatures(mf, CODE_='utf-8')
	__print('array size %d' % len(ar))
	for a in ar:
		__print('feature size %d' % a.size)
		Mecab_print(a, __print, CODE_='utf-8')
		Mecab_utf8_to_cp932(a)
		data = libjt_synthesis(a.feature,
							   a.size,
							   fperiod_ = fperiod,
							   logwrite_ = __print)
		if data:
			__print('data size %d' % len(data))
			data_array.append(data)
		libjt_refresh()
		del a
	del mf
	for data in data_array:
		if data and do_play:
			pa_play(data, samp_rate = voice_args['samp_rate'])
			w = wave.Wave_write("_test.wav")
			w.setparams( (1, 2, voice_args['samp_rate'], len(data)/2,
						  'NONE', 'not compressed') )
			w.writeframes(data)
			w.close()

def main(do_play = True):
	njd = NJD()
	jpcommon = JPCommon()
	engine = HTS_Engine()
	voice_args = {
		"id": "V1",
		"name": "m001",
		"lang":"ja",
		"samp_rate": 48000,
		"fperiod": 240,
		"alpha": 0.55,
		"lf0_base":5.0,
		"use_lpf":1,
		"speaker_attenuation":1.0,
		"dir": VOICE_DIR
		}
	libjt_initialize(JT_DLL, **voice_args)
	libjt_load(voice_args['dir'].encode('mbcs'))
	Mecab_initialize(__print, JT_DIR)
	_nvdajp_predic.setup()

	msgs = [
		'100.25ドル。ウェルカムトゥー nvda テンキーのinsertキーと、メインのinsertキーの両方が、nvdaキーとして動作します',
		'You Tube i Tunes Store sjis co jp',
		'十五絡脈病証。', # nvdajp ticket 29828
		'マーク。まーく。', # nvdajp ticket 29859
		'∫⣿♪ ウェルカムトゥー 鈹噯呃瘂蹻脘鑱涿癃 十五絡脈病証 マーク。まーく。ふぅー。ふぅぅぅぅぅー。ぅー。ぅぅー。',
		'更新履歴\r\n\r\n==== Ver 1.5.3.0\r\n * CHG: RT発言のふぁぼられ数を他のRT発言にも反映するよう変更\r\n * CHG: 検索やLists等のタブで取得した返信もReplyタブに追加するよう変更。その他＠取得漏れの調整。\r\n * FIX: 起動時に例外が発生する場合があったので修正\r\n * FIX: バージョンアップ時に＠、DMの最終未読発言がクリアされてしまうバグ修正\r\n * FIX: ふぁぼられ時に未読数が更新されないケースがあったので修正\r\n * FIX: ブロックされているユーザーの発言をFavoriteQueue追加すると失敗し続ける問題に対処\r\n==== Ver 1.5.2.0\r\n * CHG: FavQueueViewerとイベントビューワをダイアログ表示に変更し、閉じやすくするように\r\n * CHG: RT発言のふぁぼられ数を反映するように修正\r\n * FIX: Twitterからの定期取得および起動時取得が失敗する場合があったので修正\r\n * FIX: 画像投稿先からLockerz消し忘れていたので対応。投稿先の選択が初期化されているので、再度選択をお願いします。\r\n * FIX: イベントビューワのボタンが画面サイズ変更に追従しないバグ修正\r\n * FIX: 検索結果取得時にTwitterからユーザー情報のない発言が返される場合があったので対処\r\n==== Ver 1.5.1.0\r\n * NEW: 他ユーザー発言のふぁぼられ数表示のオン・オフ設定を追加（設定-表示-発言一覧）。デフォルト：オン\r\n * FIX: 自分の発言がふぁぼられた時にUserStreamが切断される場合がある問題を修正\r\n==== Ver 1.5.0.0\r\n * NEW: 他ユーザーの発言にもふぁぼられ数（+1など）を表示するように。発言取得時の情報でありリアルタイムに書き換わりません\r\n * CHG: 認証をアプリ内ブラウザではなくOSデフォルトブラウザで行うよう変更。PINはTweenに戻って手入力してください。（使用しているIEバージョンによってはエラー表示されるための対処）\r\n * CHG: LockerzのAPI提供が終了したため関連機能削除\r\n * FIX: タブへの発言追加／削除で例外が発生する場合があったので修正\r\n * FIX: 残API数が正しく表示されない問題を修正\r\n * FIX: ふぁぼ追加時に例外が発生する場合があったので修正\r\n * FIX: インターネット接続チェックを廃止\r\n * FIX: 検索結果のRT発言にRTしたユーザー情報抜きで応答返ってくるTwitterの問題に対処\r\n * FIX: 出島表示でフォーカスが移らない場合があったので修正\r\n==== Ver 1.4.9.0\r\n * FIX: 設定ファイル保存時に例外が発生する場合があったので修正\r\n * FIX: 新着通知および発言ソート時に例外発生する場合があったので修正\r\n * FIX: 複数発言をFav追加する時例外発生する場合があったので修正\r\n * FIX: 着せ替えアイコンの設置先フォルダを設定ファイルのある場所のものを参照するよう修正\r\n==== Ver 1.4.8.0\r\n * FIX: Twitterの応答変更によりタイムラインが読み込めなくなる問題に対処\r\n==== Ver 1.4.7.0\r\n * NEW: FavorieQueue機能追加。ふぁぼ失敗した場合のリトライや、一度にたくさんふぁぼった場合にキューから間をおいてふぁぼることで規制にかかりにくくします。設定画面から有効にする必要があります。その他機能にFavoriteQueueViewer追加。\r\n * NEW: 出島実装。大陸的なアレ。使うためには設定画面でホットキーを設定してください。\r\n * NEW: ヘルプメニューに「Twitterサーバーステータスページ」、「Twitterステータスブログ」、Tweenの「フォーラム」を開くメニューを追加\r\n * NEW: Vine、Gyazoのサムネイル表示に対応\r\n * NEW: 発言詳細内で展開された関連発言の日時右クリックメニューにFav、RT等のメニューを追加\r\n * NEW: イベントログビューワにクリアボタン追加\r\n * NEW: ユーザープロフィール画面にプロフィールバナー／アイコン／背景イメージをブラウザで表示するメニュー追加\r\n * CHG: 発言内のURLを開く際、複数URLがあった場合の選択画面に関連発言の発言パーマリンク等余分なものも表示されていたので修正\r\n * CHG: 発言内のURLを開く際のロジックを変更（動作は変わりません）\r\n * CHG: 画像サムネイル取得ロジックをTwitterCardsを考慮したものに変更\r\n * CHG: 「ヘルプ」-「Tweenについて」画面のサイズ変更を可能に。更新履歴が見やすくなります。\r\n * CHG: Webでの「このユーザーのRTを表示しない」設定がAPI1.1でも取得できるようになったので対応（API1.0対応バージョン相当に戻りました）\r\n * CHG: Twitterが公開するAPI情報（残API数やリセット時刻など）に対象となるAPI種類が何点か追加されたので対応\r\n * CHG: DMの解釈方式を変更しました。RepostLinkが展開されたりします。\r\n * CHG: 内部の発言保持方法を一部変更し、同一発言の状態不整合がなくなるようにしました。（基本的に動作は変わりません。）\r\n * FIX: 発言詳細の右クリックメニュー「全ユーザーのフォロー状態確認」で複数回同一ユーザーの状態が表示される問題を修正\r\n * FIX: 発言内のURLを開く時のロジックを変更（動作は変わりません）\r\n * FIX: 文字化けする場合があったので修正\r\n * FIX: httpsの画像直リンクURLでもサムネイル表示されるよう修正\r\n * FIX: タイトルにフォロワー数を表示している設定でアカウントを切り替えると、切り替え前のフォロワー数を基準に増減数を表示していた問題を修正\r\n==== Ver 1.4.6.0\r\n * NEW: タッチモードを追加。メニュー等の選択操作を容易にする余白調整と、発言一覧を2本指タッチで未読ジャンプします\r\n * CHG: プロフィール表示でのURLリンクなどをWebと合わせるよう変更\r\n * FIX: 認証時の時刻補正により通信ができなくなる場合があったので機能を削除\r\n * FIX: 通信回線の変更やプロキシ設定に誤りがある場合に固まる問題を修正\r\n * FIX: pixivのサムネイル表示で例外が発生する問題を修正\r\n * FIX: img.lyの変更に伴い画像投稿・サムネイル表示が出来なくなっていた問題を修正\r\n * FIX: 新着通知がオンでないと新着サウンドが再生されない問題を修正\r\n * FIX: Replyタブ・DMタブで未読管理オフだと最終未読位置が更新されない問題を修正\r\n==== Ver 1.4.5.0\r\n * NEW: 設定画面のAPI使用数予測表示をAPI1.1対応にして復活させました。\r\n * NEW: 投稿欄へ画像ペーストで画像投稿が出来るようになりました。\r\n * NEW: 設定画面と振分け画面にサウンドファイル置き場をエクスプローラーで開くボタンを追加しました。1.4.4.0で音が鳴らなくなった方は、このボタンで開いたフォルダにサウンドファイルを移動してください。\r\n * NEW: 検索タブの公式RTが通常のタイムラインと同様の表示になりました。\r\n * CHG: 動作要件を.NET Framework 4 (Client Profile)に変更しました。Full版のインストールは不要です。既にFull版をインストールされている方はそのままお使いいただけます。\r\n * CHG: 検索を使用して関連発言の補完を行うようにしました。ツイートの非公開ユーザーは検索出来ないため補完出来ません。\r\n * CHG: Instagramのサムネイル取得方法を変更しました。\r\n * CHG: 一部環境でサウンドの再生が正しく行われないことがあるため、サウンド再生方法を変更しました。\r\n * CHG: OAuth認証の際にサーバーの時刻との差を考慮するようにしました。パソコンの時計がずれていても認証を始めとしたTwitterとの通信が出来るようになります。\r\n * FIX: 起動に失敗する場合があったので再起動を試みるように変更しました。（.NET Frameworkの不具合でシステムが高負荷の際ハッシュテーブル挿入の例外が発生する場合への対処です）\r\n * FIX: API情報ダイアログにおいて、「Tweenで使用するAPIのみ表示する」チェックを入れていた場合に検索用API（/search/tweets）の情報が表示されない不具合を修正しました。\r\n * FIX: Lists取得の際にRTを除外する設定でもRTが含まれていた不具合を修正しました。再度ListsにRTを含める場合は、設定画面の[表示]-[発言一覧]の「Listの発言取得に公式RTを含める」をオンにしてください。\r\n * FIX: 検索タブにおいて前データ取得が動作していなかった不具合を修正しました。\r\n * FIX: DMの削除に失敗する不具合を修正しました。\r\n==== Ver 1.4.4.0\r\n * CHG: [キーで返信先を辿るとき、返信先が削除されていたらブラウザで開く前に確認メッセージ表示するよう変更\r\n * FIX: 関連発言表示で返信先発言が取得出来なかった場合にAPI消費し続ける問題を修正\r\n * FIX: イン',
		]
	s = msgs[5]
	print(len(s))
	do_synthesis(s, voice_args, do_play)

if __name__ == '__main__':
	prof = cProfile.run("main(do_play=False)", '_cprof.prof')
	p = pstats.Stats('_cprof.prof')
	p.strip_dirs()
	p.sort_stats('time', 'calls')
	p.print_stats()
