---
title: 'Error compile 2.8 xmrig '
source_url: https://github.com/xmrig/xmrig/issues/773
author: LearnMiner
assignees: []
labels:
- question
created_at: '2018-10-03T16:22:35+00:00'
updated_at: '2018-11-05T14:19:33+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:19:33+00:00'
---

# Original Description
Bat:
mkdir build
cd build
cmake .. -G "Visual Studio 15 2017" -DXMRIG_DEPS=c:\xmrig-deps-3.3\msvc2017\x86
pause


![image](https://user-images.githubusercontent.com/34003340/46424325-1b4e9c00-c739-11e8-8005-8fd17518f184.png)


# Discussion History
## xmrig | 2018-10-03T16:37:56+00:00
Make sure your update your Visual Studio to recent version, 15.8.6 at this moment. xmrig-deps compatible only with MSVC 2017 15.8+.
Thank you.

## xmrig | 2018-10-03T16:40:11+00:00
Generally bad idea use x86 miner, it much slower that x64, especially for upcoming `cn/2`.

## LearnMiner | 2018-10-03T17:15:24+00:00
@xmrig I know but i test always all miners 32 and 64 for see % lose
I will update and say if worked

## LearnMiner | 2018-10-04T12:24:19+00:00
Worked! Thanks @xmrig I love your miners :)

But why this new miner have 2mg?

## xmrig | 2018-10-06T11:57:47+00:00
@LearnMiner Sorry, I missed you was edit your comment, because of TLS support, it can be disabled `-DWITH_TLS=OFF`.

# Action History
- Created by: LearnMiner | 2018-10-03T16:22:35+00:00
- Closed at: 2018-11-05T14:19:33+00:00
