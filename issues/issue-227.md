---
title: Error Libuv I can donate if is work
source_url: https://github.com/xmrig/xmrig/issues/227
author: LearnMiner
assignees: []
labels: []
created_at: '2017-11-28T11:42:09+00:00'
updated_at: '2018-03-14T23:29:35+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:29:35+00:00'
---

# Original Description
I downloaded xmrig-deps-v2 and extract folder in C:\ and C:\msys64\ and C:\msys64\home. Im using mingw64, but when i compile i have this error :

[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.obj
make[2]: *** No hay ninguna regla para construir el objetivo 'C:/<path/gcc/libuv/x86/lib/libuv.a', necesario para 'xmrig.exe'. Alto.
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

what can i do?

# Discussion History
## Bendr0id | 2017-12-11T08:11:00+00:00
Hey man, should be simple. Looks like the linker is not able to find your libuv. Seems that your cmake cointains "<path" within the path. I think you just missed to replace it.

If you extract xmrig-deps-v2 to c:\xmrig-deps-v2 folder the call should be:

cmake .. -G "Unix Makefiles" -DUV_INCLUDE_DIR="c:\xmrig-deps-v2\gcc\libuv\x64\include" -DUV_LIBRARY="c:\xmrig-deps-v2\gcc\libuv\x64\lib\libuv.a" -DMHD_INCLUDE_DIR="c:\xmrig-deps-v2\gcc\libmicrohttpd\x64\include" -DMHD_LIBRARY="c:\xmrig-deps-v2\gcc\libmicrohttpd\x64\lib\libmicrohttpd.a"

Hope this helps. And sorry for the 13 delay on this simple topic.

XMR:
46FkYo7x6LqYjLQo4Jd84UTGBybW7tsWqJaQVLPhbUSK19ajSTMY9T2Sa2LH6CfWhSingjvQARtfeM4Feekpp2yFR1wsFNT





# Action History
- Created by: LearnMiner | 2017-11-28T11:42:09+00:00
- Closed at: 2018-03-14T23:29:35+00:00
