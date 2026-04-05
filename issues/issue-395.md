---
title: Mingw64 build needs dlls
source_url: https://github.com/xmrig/xmrig/issues/395
author: cpucoin
assignees: []
labels: []
created_at: '2018-02-09T20:00:10+00:00'
updated_at: '2019-01-30T12:36:28+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:11:47+00:00'
---

# Original Description
I have tried building with mingw64 with the newest source and the newest versions of libuv and microhttpd from this repository but when I try to run it needs extra dlls. When I copy the libwinpthread-1.dll to the same directory as the exe, it then crashes. Any ideas?

# Discussion History
## RansomFuck | 2018-02-12T22:09:11+00:00
Installed with MSYS64? And you install all step-by-step to you Mingw*version* in wiki?

## cpucoin | 2018-02-12T22:52:11+00:00
Followed instructions on build wiki for windows.
New install of mingw64 on win7
New source and assets from github
exe builds fine with newest version of gcc
using: 
cmake .. -G "Unix Makefiles" -DWITH_HTTPD=OFF -DWITH_AEON=OFF -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="C:\msys64\mingw64\include" -DUV_LIBRARY="C:\msys64\mingw64\lib\libuv.a"

When i try to run it complains about missing dll, if I copy it over the exe crashes on boot with error 0xc000007b


## cpucoin | 2018-02-14T21:16:20+00:00
Tried fresh install of msys2-x86_64-20161025, with xmrig-2.4.4, cmake of: cmake .. -G "Unix Makefiles" -DWITH_HTTPD=OFF -DWITH_AEON=OFF -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="C:\msys64\mingw64\include" -DUV_LIBRARY="C:\msys64\mingw64\lib\libuv.a" same results, then added xmrig-deps-v2_1, same result, then tried xmrig-deps-v2_2, same results. Needs dll and if you add dll, crashes on startup. Any ideas?

## ghost | 2018-10-31T12:19:12+00:00
Have you solved the problem, please? I showed up in the same situation as you. 

## sanitariu | 2019-01-29T17:38:46+00:00
I have the same problem

# Action History
- Created by: cpucoin | 2018-02-09T20:00:10+00:00
- Closed at: 2018-11-05T07:11:47+00:00
