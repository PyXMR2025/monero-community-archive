---
title: 32-bit compilation problems with unresolved external symbol _randomx_*****
source_url: https://github.com/xmrig/xmrig/issues/1472
author: chelmedvedosvin
assignees: []
labels:
- wontfix
created_at: '2019-12-30T11:00:42+00:00'
updated_at: '2020-01-01T12:08:05+00:00'
type: issue
status: closed
closed_at: '2020-01-01T12:08:05+00:00'
---

# Original Description
I tried to compile version 3.2 and 5.3 in 32bit mode.
I used cmake-3.16.2-win32-x86 and VS2017 15.9.18
Deps ver 3.5 and 4.0. I even noticed that randomx lib is included only in x64 dep's folder. I tried to copy randomx.lib and randomx.h from x64 to x86 folder but still didn't help. I always get:

`Severity	Code	Description	Project	File	Line	Suppression State
Error	LNK2001	unresolved external symbol _randomx_program_loop_end	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_prefetch_scratchpad_end	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_dataset_init	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_epilogue	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_end	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_loop_store	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_read_dataset_sshash_init	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_sshash_end	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_sshash_init	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_sshash_prefetch	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_sshash_load	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_loop_load	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_loop_begin	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_start	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_prefetch_scratchpad	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_prologue_first_load	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_prologue	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_read_dataset_sshash_fin	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\jit_compiler_x86.obj	1	
Error	LNK1120	18 unresolved externals	xmrig-notls	C:\msys32\msvs\xmrig-5.3.0\build\Release\xmrig-notls.exe	1	
`
If i compile as x64 - all working well.

# Discussion History
## xmrig | 2020-01-01T12:08:05+00:00
32bit builds for MSVC not supported.
Thank you.

# Action History
- Created by: chelmedvedosvin | 2019-12-30T11:00:42+00:00
- Closed at: 2020-01-01T12:08:05+00:00
