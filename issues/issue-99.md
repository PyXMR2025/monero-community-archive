---
title: Please Renew Windows 7/10 build instructions with Visual Studio 17.2
source_url: https://github.com/xmrig/xmrig/issues/99
author: dorimanx
assignees: []
labels: []
created_at: '2017-09-07T18:15:30+00:00'
updated_at: '2017-10-22T05:26:50+00:00'
type: issue
status: closed
closed_at: '2017-10-22T05:26:50+00:00'
---

# Original Description
Hi,

I have spent hours trying to build with visual studio and cmake 3.9.1 and libuv 1.40

when trying to build with:
e:\Dorimanx\xmrig\build>cmake .. -G "Visual Studio 15 2017 Win64" -T v140_xp -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="c:\Pro
gram Files\libuv\include" -DUV_LIBRARY="c:\Program Files\libuv\libuv.lib"

it's fail on unknown compiler. tried to install 2015 and 2013 tools and still the same.
when trying to build with -T v140 it's work.

then i compile with:
"e:\Microsoft Visual Studio\2017\Community\MSBuild\15.0\Bin\msbuild" xmrig.sln /p:Configuration=Release

get the file, but it's will not start, and demand libuv.dll, i add the same libuv.dll from used folder.
and application just blink on start and nothing.

same with -T v141

Please write all needed applications to be able to build your source.

Thank you.


# Discussion History
# Action History
- Created by: dorimanx | 2017-09-07T18:15:30+00:00
- Closed at: 2017-10-22T05:26:50+00:00
