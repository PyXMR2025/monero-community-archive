---
title: Cmake shows error during building xmrig-2.6.0-beta2 with MSYS2 on Windows
source_url: https://github.com/xmrig/xmrig/issues/555
author: adem4ik
assignees: []
labels: []
created_at: '2018-04-15T12:57:21+00:00'
updated_at: '2018-04-24T11:57:55+00:00'
type: issue
status: closed
closed_at: '2018-04-15T13:30:20+00:00'
---

# Original Description
**Preconditions:**
- Windows 10 x64
- MSYS2 64 bit
- Source from https://github.com/xmrig/xmrig/releases/tag/v2.6.0-beta2
- Dependencies from https://github.com/xmrig/xmrig-deps/releases/tag/v3.0

Follow the steps from https://github.com/xmrig/xmrig/wiki/Windows-Build for building with MSYS2 64 bit

**Result after making 'cmake' configuration:**

> adem4@DESKTOP-0G24H6R MINGW64 ~/xmrig-2.6.0-beta2
> $ cmake . -G "Unix Makefiles" -DXMRIG_DEPS=C:\msys64\home\adem4\xmrig-deps-3.0\gcc\x64
> -- The C compiler identification is GNU 7.3.0
> -- The CXX compiler identification is GNU 7.3.0
> -- Check for working C compiler: C:/msys64/mingw64/bin/cc.exe
> -- Check for working C compiler: C:/msys64/mingw64/bin/cc.exe -- works
> -- Detecting C compiler ABI info
> -- Detecting C compiler ABI info - done
> -- Detecting C compile features
> -- Detecting C compile features - done
> -- Check for working CXX compiler: C:/msys64/mingw64/bin/c++.exe
> -- Check for working CXX compiler: C:/msys64/mingw64/bin/c++.exe -- works
> -- Detecting CXX compiler ABI info
> -- Detecting CXX compiler ABI info - done
> -- Detecting CXX compile features
> -- Detecting CXX compile features - done
> -- Found UV: C:/msys64/mingw64/lib/libuv.a
> -- Looking for syslog.h
> -- Looking for syslog.h - not found
> -- Could NOT find MHD (missing: MHD_LIBRARY MHD_INCLUDE_DIR)
> CMake Error at CMakeLists.txt:227 (message):
>   microhttpd NOT found: use `-DWITH_HTTPD=OFF` to build without http deamon
>   support
> 
> 
> -- Configuring incomplete, errors occurred!
> See also "C:/msys64/home/adem4/xmrig-2.6.0-beta2/CMakeFiles/CMakeOutput.log".
> See also "C:/msys64/home/adem4/xmrig-2.6.0-beta2/CMakeFiles/CMakeError.log".


# Discussion History
## xmrig | 2018-04-15T13:05:27+00:00
~Looks like you not specify `-DXMRIG_DEPS=` or set wrong path or some other error.~

`-- Found UV: C:/msys64/mingw64/lib/libuv.a` this libuv.a from MSYS2 installation not from xmrig-deps.

Try `-DXMRIG_DEPS=C:/msys64/home/adem4/xmrig-deps-3.0/gcc/x64`
Thank you.

## adem4ik | 2018-04-15T13:15:46+00:00
@xmrig I believe that I've followed the instructions from https://github.com/xmrig/xmrig/wiki/Windows-Build correctly

I have extracted deps to `C:\msys64\home\adem4\`, so I used `-DXMRIG_DEPS=C:\msys64\home\adem4\xmrig-deps-3.0\gcc\x64`

![image](https://user-images.githubusercontent.com/4707112/38778835-5285cbde-40d0-11e8-983f-d72850bb221a.png)

## xmrig | 2018-04-15T13:20:44+00:00
In build docs used `/` instead of `\`, so use `-DXMRIG_DEPS=C:/msys64/home/adem4/xmrig-deps-3.0/gcc/x64`. Check all cmake output, everywhere used `/` not `\`.
Thank you.

## adem4ik | 2018-04-15T13:28:20+00:00
@xmrig Thank you very much, that fixed the problem. It's my bad >.<

Btw, can you update https://github.com/xmrig/xmrig/wiki/Windows-Build for MSYS2 builds? I think it should be
`cmake . -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64`
instead of
`cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64`

## xmrig | 2018-04-15T13:33:37+00:00
Missing part, before run cmake
```
mkdir build
cd build
```

Benefit of create directory (name not important) and run `cmake ..` is all build files will be located in this directory and don't mess with source files.
Thank you.

## ciamita | 2018-04-24T11:57:55+00:00
Hi i love you program is simply and best, work fin in xmr, but i want ask you you dont have and for eth same program ?

# Action History
- Created by: adem4ik | 2018-04-15T12:57:21+00:00
- Closed at: 2018-04-15T13:30:20+00:00
