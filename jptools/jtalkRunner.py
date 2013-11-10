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
		]

	do_synthesis(msgs[0] * 10, voice_args, do_play)

if __name__ == '__main__':
	prof = cProfile.run("main(do_play=False)", '_cprof.prof')
	p = pstats.Stats('_cprof.prof')
	p.strip_dirs()
	p.sort_stats('time', 'calls')
	p.print_stats()
