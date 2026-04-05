---
title: 'Unifiqued DLL Cuda '
source_url: https://github.com/xmrig/xmrig/issues/1302
author: LearnMiner
assignees: []
labels:
- question
created_at: '2019-11-19T02:59:12+00:00'
updated_at: '2019-12-22T19:38:08+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:38:08+00:00'
---

# Original Description
How can I put all in same exe? without dll

# Discussion History
## xmrig | 2019-11-19T10:38:26+00:00
There 2 types of dll:
1. `xmrig-cuda.dll` itself, technically possible make it static, it has some restrictions for example not possible use gcc, because CUDA not support this compiler on Windows, it require write some code anyway, right now it not possible. 
2. NVRTC libraries, for example `nvrtc64_101_0.dll` and `nvrtc-builtins64_101.dll`, only way to avoid these dlls is remove algorithms where it used, for example `cn/r` and it also require write some code.

Thank you.

# Action History
- Created by: LearnMiner | 2019-11-19T02:59:12+00:00
- Closed at: 2019-12-22T19:38:08+00:00
