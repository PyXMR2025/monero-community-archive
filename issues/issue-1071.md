---
title: "LNK2001\tunresolved external symbol _randomx_program_end"
source_url: https://github.com/xmrig/xmrig/issues/1071
author: joey-crypto
assignees: []
labels:
- wontfix
created_at: '2019-07-23T23:40:00+00:00'
updated_at: '2019-08-09T09:56:40+00:00'
type: issue
status: closed
closed_at: '2019-08-09T09:56:40+00:00'
---

# Original Description
when i build xmrig 2.99 in windows7 through cmake 3.15 and vs 2017, it shows these problem. 

Error	LNK2001	unresolved external symbol _randomx_program_end	xmrig-notls	D:\xmrig-2.99.0-beta\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_epilogue	xmrig-notls	D:\xmrig-2.99.0-beta\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_loop_begin	xmrig-notls	D:\xmrig-2.99.0-beta\build\jit_compiler_x86.obj	1	
Error	LNK2001	unresolved external symbol _randomx_program_loop_end	xmrig-notls	D:\xmrig-2.99.0-beta\build\jit_compiler_x86.obj	1

# Discussion History
## joey-crypto | 2019-07-23T23:40:53+00:00
how to solve these problems.


## xmrig | 2019-08-09T09:56:40+00:00
32 bit builds for Visual Studio not supported.
Thank you.

# Action History
- Created by: joey-crypto | 2019-07-23T23:40:00+00:00
- Closed at: 2019-08-09T09:56:40+00:00
