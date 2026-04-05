---
title: x86 xmrig.exe not working.
source_url: https://github.com/xmrig/xmrig/issues/1728
author: snipeTR
assignees: []
labels:
- bug
created_at: '2020-06-10T10:38:07+00:00'
updated_at: '2020-08-19T01:14:50+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:14:50+00:00'
---

# Original Description
I did not change the code either. all libraries are up to date. compiler is up to date. There is no error in the compilation process. I have tried many CMAKE options. the program does not work in any way.
cmd %errorlevel% value =-1073741819
x86 compile complate but not run xmrig.exe
standart config.json

compile command 
------------------
mkdir build
cd build
cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x86
make

MSYS2 32 bit updated

no error.
no log.
no dry run.
yes --help.
yes "no config error".

exe file.
https://gofile.io/d/j1H64P


# Discussion History
## xmrig | 2020-06-10T16:14:03+00:00
Fixed, as a workaround you can set any string value for `"user-agent"` option, it solves the crash without changing code.

Please note using x86 is pretty bad idea especially for RandomX, it almost useless for mining.
Thank you.

# Action History
- Created by: snipeTR | 2020-06-10T10:38:07+00:00
- Closed at: 2020-08-19T01:14:50+00:00
