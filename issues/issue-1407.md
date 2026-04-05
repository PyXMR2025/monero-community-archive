---
title: Help me
source_url: https://github.com/xmrig/xmrig/issues/1407
author: John-xmrig
assignees: []
labels: []
created_at: '2019-12-12T12:48:13+00:00'
updated_at: '2019-12-21T19:47:55+00:00'
type: issue
status: closed
closed_at: '2019-12-21T19:47:55+00:00'
---

# Original Description
1-cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS=C:\Users\John\Desktop\xmrig-deps-3.1\msvc2019\x64
2-cmake --build . --config Release


"C: \ Users \ John \ Desktop \ xmrig-deps-3.1 \ xmrig-5.2.0 \ build \ ALL_BUILD.vcxproj" (default
Recognize goals
) (1)->
"C: \ Users \ John \ Desktop \ xmrig-deps-3.1 \ xmrig-5.2.0 \ build \ xmrig.vcxproj" (default
Standard) (1
0)->
(Link target)->
   LINK: fatal error C1007: Unrecognized flag "-pdbrpc" (in "p2") [C: \ Users \ John
\ Desktop \ xmr
ig-deps-3.1 \ xmrig-5.2.0 \ build \ xmrig.vcxproj]
   LINK: fatal error LNK1257: Code generation failed [C: \ Users \ John \ Desktop \ xmrig-deps-3.1
\ xmri
g-5.2.0 \ build \ xmrig.vcxproj]

     89 warnings
     2 errors

Elapsed time 00: 03: 47.32

# Discussion History
## flippp0 | 2019-12-17T20:36:35+00:00
Did you try the latest release of xmrig-deps?
It was updated a few days ago.
also try "C:\Users\John\Desktop\xmrig-deps-3.1\msvc20**17**\x64" if you use VS 2017

# Action History
- Created by: John-xmrig | 2019-12-12T12:48:13+00:00
- Closed at: 2019-12-21T19:47:55+00:00
