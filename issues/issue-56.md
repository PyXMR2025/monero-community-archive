---
title: Where i can find libuv.a?
source_url: https://github.com/xmrig/xmrig/issues/56
author: Omnividente
assignees: []
labels: []
created_at: '2017-08-06T18:55:37+00:00'
updated_at: '2017-12-28T22:03:48+00:00'
type: issue
status: closed
closed_at: '2017-08-17T14:31:26+00:00'
---

# Original Description
Hi, i try compiled x32 version on win 10x64
I installed msys64, installed Libuv x32 (libuv-x86-v1.13.1.build12.exe), then
pacman -Sy
pacman -S mingw-w64-i686-gcc
pacman -S make
pacman -S mingw-w64-i686-cmake
pacman -S mingw-w64-i686-pkg-config

cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="c:\libuvx32\include" -DUV_LIBRARY="c:\libuvx32\libuv.lib"
make

And i get error 
https://farm5.staticflickr.com/4386/35575418664_407eb9845d_o.png

Where i can find libuv.a 1.13.1? i find it in version libuv 1.8.0, but it very old version.



# Discussion History
## sk3lk0 | 2017-12-28T22:03:47+00:00
ты нашел?


# Action History
- Created by: Omnividente | 2017-08-06T18:55:37+00:00
- Closed at: 2017-08-17T14:31:26+00:00
