# -*- coding: utf-8 -*-
# jptools/eng2Harness.py
# A part of NonVisual Desktop Access (NVDA)
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Copyright (C) 2023 Takuya Nishimoto
#
# For output field, blank should be 0x20 (not 0x2800).
# output の空白は 0x2800 ではなく 0x20 を使います

tests = [
    {"note": "+ 日本語点字と英語2級の併用モード +"},
    {
        # "text": "NonVisual Desktop Access (NVDA)",
        "input": "⠦NonVisual Desktop Access (NVDA)⠴",
        "output": "⠦⠠⠝⠕⠝⠠⠧⠊⠎⠥⠁⠇ ⠠⠙⠑⠎⠅⠞⠕⠏ ⠠⠁⠉⠉⠑⠎⠎ ⠶⠠⠠⠝⠧⠙⠁⠶⠴",
        # "output-eng2": "⠦⠠⠝⠕⠝⠠⠧⠊⠎⠥⠁⠇ ⠠⠙⠑⠎⠅⠞⠕⠏ ⠠⠁⠒⠑⠎⠎ ⠶⠠⠠⠝⠧⠙⠁⠶⠴",
    },
    {
        # "text": "Microsoft Windows",
        "input": "⠦Microsoft Windows⠴",
        "output": "⠦⠠⠍⠊⠉⠗⠕⠎⠕⠋⠞ ⠠⠺⠊⠝⠙⠕⠺⠎⠴",
        # "output-eng2": ⠦⠠⠍⠊⠉⠗⠕⠎⠷⠞ ⠠⠺⠔⠙⡪⠎⠴⠊⠠⠯⠛⠒⠈⠗⠴",
    },
    {
        # "text": "NonVisual Desktop Access (NVDA) は、Microsoft Windowsオペレーティングシステム用の無料でオープンソースのスクリーンリーダーです。",
        "input": "⠦NonVisual Desktop Access (NVDA)⠴ ハ、⠦Microsoft Windows⠴ オペレーティング システムヨーノ ムリョーデ オープン ソースノ スクリーン リーダーデス。",
        "output": "⠦⠠⠝⠕⠝⠠⠧⠊⠎⠥⠁⠇ ⠠⠙⠑⠎⠅⠞⠕⠏ ⠠⠁⠉⠉⠑⠎⠎ ⠶⠠⠠⠝⠧⠙⠁⠶⠴ ⠥⠰ ⠦⠠⠍⠊⠉⠗⠕⠎⠕⠋⠞ ⠠⠺⠊⠝⠙⠕⠺⠎⠴ ⠊⠠⠯⠛⠒⠈⠗⠴⠐⠩ ⠳⠹⠟⠽⠜⠒⠎ ⠽⠈⠚⠒⠐⠟ ⠊⠒⠠⠭⠴ ⠺⠒⠹⠎ ⠹⠩⠓⠒⠴ ⠓⠒⠐⠕⠒⠐⠟⠹⠲",
        # "output-eng2": "⠦⠠⠝⠕⠝⠠⠧⠊⠎⠥⠁⠇ ⠠⠙⠑⠎⠅⠞⠕⠏ ⠠⠁⠒⠑⠎⠎ ⠶⠠⠠⠝⠧⠙⠁⠶⠴ ⠥⠰ ⠦⠠⠍⠊⠉⠗⠕⠎⠷⠞ ⠠⠺⠔⠙⡪⠎⠴⠊⠠⠯⠛⠒⠈⠗⠴⠐⠩ ⠳⠹⠟⠽⠜⠒⠎ ⠽⠈⠚⠒⠐⠟ ⠊⠒⠠⠭⠴ ⠺⠒⠹⠎ ⠹⠩⠓⠒⠴ ⠓⠒⠐⠕⠒⠐⠟⠹⠲",
    },
]
