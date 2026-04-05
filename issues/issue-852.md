---
title: '''cx'': formal parameter with requested alignment of 16 won''t be aligned'
source_url: https://github.com/xmrig/xmrig/issues/852
author: ggfdocker
assignees: []
labels:
- question
created_at: '2018-10-27T03:05:57+00:00'
updated_at: '2018-11-05T11:14:34+00:00'
type: issue
status: closed
closed_at: '2018-11-05T11:14:34+00:00'
---

# Original Description
Hi,
I cannot compile the last v2.8.3 xmrig with vs2015.
I make project with such cmdline:
cmake -G "Visual Studio 14 2015" -DXMRIG_DEPS=c:\deps\msvc2015\x86
Used xmrig-deps-3.3, also tried xmrig-deps-3.0.

x86 project not compiles generated project with error:
Error	C2719	'cx': formal parameter with requested alignment of 16 won't be aligned

Error is in CryptoNight_86.h file and cryptonight_monero_tweak() function.

Also it's all ok with x64 project version,
cmake -G "Visual Studio 14 2015 x64" -DXMRIG_DEPS=c:\deps\msvc2015\x64
no erorrs

How can i fix this? Thank you

# Discussion History
## jiaxu2000 | 2018-11-05T09:48:42+00:00
windows 32 bit x86 only support gcc compile

## xmrig | 2018-11-05T11:14:34+00:00
Build can easily fixed, see this pending PR https://github.com/xmrig/xmrig/pull/800, however MSYS2 for 32 bit faster 10%+.

# Action History
- Created by: ggfdocker | 2018-10-27T03:05:57+00:00
- Closed at: 2018-11-05T11:14:34+00:00
