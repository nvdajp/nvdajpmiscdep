# -*- coding: utf-8 -*-
#jptools/harness.py
#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2014 Takuya Nishimoto
# 
# For output field, blank should be 0x20 (not 0x2800).
# output の空白は 0x2800 ではなく 0x20 を使います

from __future__ import unicode_literals

tests = [
	{ 'note': '+ 日本語点字とNABCCの併用モード +' },
	{
		'mode':   'NABCC',
		'input':  'abcdefghijklmnopqrstuvwxyz',
		'output': '⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵',
		},
	{
		'mode':   'NABCC',
		'input':  '1234567890',
		'output': '⠂⠆⠒⠲⠢⠖⠶⠦⠔⠴',
		},
	{
		'mode':   'NABCC',
		'input':  'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
		'output': '⡁⡃⡉⡙⡑⡋⡛⡓⡊⡚⡅⡇⡍⡝⡕⡏⡟⡗⡎⡞⡥⡧⡺⡭⡽⡵',
		},
	{
		'mode':   'NABCC',
		'input':  ',;:.!"',
		'output': '⠠⠰⠱⠨⠮⠐',
		},
	{
		'mode':   'NABCC',
		'input':  "'()-",
		'output': '⠄⠷⠾⠤',
		},
	{
		'mode':   'NABCC',
		'input':  '_<=>%+~`',
		'output': '⠸⠣⠿⠜⠩⠬⠘⠈',
		},
	{
		'mode':   'NABCC',
		'input':  '&$?{[}]',
		'output': '⠯⠫⠹⠪⡪⠻⡻',
		},
	{
		'mode':   'NABCC',
		'input':  '^@#\\|/*',
		'output': '⡘⡈⠼⡳⠳⠌⠡',
		},
	]
