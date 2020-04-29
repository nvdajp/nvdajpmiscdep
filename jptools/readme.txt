A part of NonVisual Desktop Access (NVDA)
This file is covered by the GNU General Public License.
See the file COPYING for more details.
Copyright (C) 2015-2020 Takuya Nishimoto

setup:

> python -VV
Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 09:44:33) [MSC v.1900 32 bit (Intel)]

Visual Studio 2019 (Ver.16.4 for Windows Desktop x64)

> git clone https://github.com/nvdajp/nvdajpmiscdeps.git miscDepsJp
> cd miscDepsJp
> git submodule sync
> git submodule update --init --recursive

build-and-test.cmd

> cd jptools
> build-and-test.cmd
