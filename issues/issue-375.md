---
title: Error's compiling xmrig
source_url: https://github.com/xmrig/xmrig/issues/375
author: axe-usat
assignees: []
labels:
- bug
created_at: '2018-01-30T19:53:34+00:00'
updated_at: '2018-11-05T12:48:41+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:48:41+00:00'
---

# Original Description
i get the following errors when i try to compile it with visual studio:
![capture](https://user-images.githubusercontent.com/23561866/35593367-0460934e-0610-11e8-9696-3fcf93262fcf.JPG)

Errors with gcc:

> C:/msys32/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0\libstdc++.a(vterminate.o):(.text$_ZN9__gnu_cxx27__verbose_terminate_handlerEv+0x66): undefined reference to `_imp____acrt_iob_func'
> C:/msys32/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0\libstdc++.a(vterminate.o):(.text$_ZN9__gnu_cxx27__verbose_terminate_handlerEv+0xf6): undefined reference to `_imp____acrt_iob_func'
> C:/msys32/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0\libstdc++.a(vterminate.o):(.text$_ZN9__gnu_cxx27__verbose_terminate_handlerEv+0x13a): undefined reference to `_imp____acrt_iob_func'
> collect2.exe: error: ld returned 1 exit status
> MAKE[2]: *** [CMakeFiles/xmrig.dir/build.make:1145: xmrig.exe] Error 1
> MAKE[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
> MAKE: *** [Makefile:84: all] Error 2
> 

# Discussion History
## xmrig | 2018-01-31T08:58:31+00:00
For msvc you probably set path to wrong libuv.lib file, for example x86 for your x64 build.
For gcc not sure I wasn't update gcc to 7.3.0, need check.
Thank you.

## axe-usat | 2018-01-31T18:30:03+00:00
thank u awesome minner :+1:  it's possible to put two address to donate i want todonate of my mining for this awesome project!

## bobbieltd | 2018-02-02T07:43:48+00:00
I got this errors with gcc x32 too

## bobbieltd | 2018-02-03T09:53:19+00:00
Temporary solution by downgrading gcc. Guide (for x32, x64 need name change):
- pacman -R mingw-w64-i686-gcc
- pacman -U http://repo.msys2.org/mingw/i686/mingw-w64-i686-gcc-libs-7.1.0-1-any.pkg.tar.xz
- pacman -U http://repo.msys2.org/mingw/i686/mingw-w64-i686-gcc-7.1.0-1-any.pkg.tar.xz

It works with gcc 7.1.0

## RansomFuck | 2018-02-12T22:17:50+00:00
Project -> Properties: xmrig -> and experement with "Unicode" and "Multi-byte" symbol`s settings.

## erotavlasme | 2018-03-18T15:45:52+00:00
@bobbieltd your solution works only for 32 bit, but not for 64 bit.

> $ make
> [ 12%] Built target cpuid
> [ 14%] Linking CXX executable xmrig.exe
> C:/Users/user/Desktop/gcc/x64/lib/libuv.a(libuv_la-error.o): In function `uv_fatal_error':
> C:\msys64\home\farm\libuv-1.19.2/src/win/error.c:52: undefined reference to `__imp___acrt_iob_func'
> C:\msys64\home\farm\libuv-1.19.2/src/win/error.c:54: undefined reference to `__imp___acrt_iob_func'
> collect2.exe: error: ld returned 1 exit status
> make[2]: *** [CMakeFiles/xmrig.dir/build.make:1146: xmrig.exe] Error 1
> make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
> make: *** [Makefile:84: all] Error 2

## bobbieltd | 2018-03-18T16:29:00+00:00
@erotavlas85 You need downgrade gcc x64 (gcc --version to check). Here are commands for msys2 x64 : 
$ pacman -R mingw-w64-x86_64-gcc
$ pacman -U http://repo.msys2.org/mingw/x86_64/mingw-w64-x86_64-gcc-libs-7.1.0-1-any.pkg.tar.xz
$ pacman -U http://repo.msys2.org/mingw/x86_64/mingw-w64-x86_64-gcc-7.1.0-1-any.pkg.tar.xz
$ gcc --version

It should display : gcc.exe (Rev1, Built by MSYS2 project) 7.1.0
Good to go compiling xmrig x64 after that.

## erotavlasme | 2018-03-18T16:43:56+00:00
@bobbieltd Yes, of course. I already did it:
gcc -v gcc version 7.1.0 (Rev1, Built by MSYS2 project)
I'm using latest [xmrig v. 2.5.0](https://github.com/xmrig/xmrig/releases) and [latest v. 3.0 libraries](https://github.com/xmrig/xmrig-deps/releases).

## bobbieltd | 2018-03-18T17:11:23+00:00
@erotavlas85 I've tested again with the latest xmrig code. It runned msys2 64 bits without any issues. Perhaps, you did not remove old cmake files (C:\msys64\home\farm\) and rerun with cmake after downgrading. Redo cmake with 7.1.0 at first and then make.

![msys2x64](https://user-images.githubusercontent.com/29669374/37568601-f14b23ae-2b09-11e8-9be0-4b51ff7aeda1.png)


## bobbieltd | 2018-03-18T17:20:20+00:00
@erotavlas85 Your error message : [ 14%] Linking CXX executable xmrig.exe , at 14% I think it's too soon. You should try to see if you did cmake correctly. One more cmake screenshot to help you to follow (you need to check if your cmake run like that, delete all files at msys64 home every time you rerun cmake).
 
![msys2x64second](https://user-images.githubusercontent.com/29669374/37568675-3874a268-2b0b-11e8-929b-4d7c13239777.png)


## erotavlasme | 2018-03-18T17:42:42+00:00
@bobbieltd thank you, it is strange. I used until yesterday gcc 7.2.0 with latest xmrig v. 2.5.0 and v. 2.1 libraries and it worked.
I reinstalled from scratch msys2 and all the dependencies.

> $ cmake -G "Unix Makefiles" -DXMRIG_DEPS=C:/Users/user/Desktop/gcc/x64
> -- The C compiler identification is GNU 7.1.0
> -- The CXX compiler identification is GNU 7.1.0
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
> -- Found UV: C:/Users/user/Desktop/gcc/x64/lib/libuv.a
> -- Looking for syslog.h
> -- Looking for syslog.h - not found
> -- Found MHD: C:/Users/user/Desktop/gcc/x64/lib/libmicrohttpd.a
> -- Configuring done
> -- Generating done
> -- Build files have been written to: C:/Users/user/Desktop/xmrig
> 
> $ make
> Scanning dependencies of target cpuid
> [  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.obj
> [  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.obj
> [  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.obj
> [  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.obj
> [ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.obj
> [ 12%] Linking C static library libcpuid.a
> [ 12%] Built target cpuid
> Scanning dependencies of target xmrig
> [ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.obj
> [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.obj
> [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.obj
> [ 21%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.obj
> [ 23%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.obj
> [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.obj
> [ 27%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.obj
> [ 29%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.obj
> [ 31%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.obj
> [ 34%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.obj
> [ 36%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.obj
> [ 38%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.obj
> [ 40%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.obj
> [ 42%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.obj
> [ 44%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.obj
> [ 46%] Building CXX object CMakeF[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.obj
> [ 48%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.obj
> [ 51%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.obj
> [ 53%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.obj
> [ 55%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.obj
> [ 57%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.obj
> [ 59%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.obj
> [ 61%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.obj
> [ 63%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.obj
> [ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.obj
> [ 68%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.obj
> [ 70%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.obj
> [ 72%] Building RC object CMakeFiles/xmrig.dir/res/app.rc.obj
> [ 74%] Building CXX object CMakeFiles/xmrig.dir/src/App_win.cpp.obj
> [ 76%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_win.cpp.obj
> [ 78%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_win.cpp.obj
> [ 80%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_win.cpp.obj
> [ 82%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.obj
> [ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.obj
> [ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.obj
> [ 89%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.obj
> [ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.obj
> [ 93%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.obj
> [ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.obj
> [ 97%] Building CXX object CMakeFiles/xmrig.dir/src/api/Httpd.cpp.obj
> [100%] Linking CXX executable xmrig.exe
> C:/Users/user/Desktop/gcc/x64/lib/libuv.a(libuv_la-error.o): In function `uv_fatal_error':
> C:\msys64\home\farm\libuv-1.19.2/src/win/error.c:52: undefined reference to `__imp___acrt_iob_func'
> C:\msys64\home\farm\libuv-1.19.2/src/win/error.c:54: undefined reference to `__imp___acrt_iob_func'
> collect2.exe: error: ld returned 1 exit status
> make[2]: *** [CMakeFiles/xmrig.dir/build.make:1146: xmrig.exe] Error 1
> make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
> make: *** [Makefile:84: all] Error 2

It could be a problem of libuv v. 1.19.x with gcc above 7.1.0 since up to libuv v. 1.18.x it worked well.


## bobbieltd | 2018-03-18T18:09:35+00:00
@erotavlas85 You are right. I still use old libuv.

## erotavlasme | 2018-03-18T20:31:35+00:00
@bobbieltd well, so it seems that it is not possible to build x64 binary with gcc and libuv v. 1.19.x under windows.
@xmrig can you confirm this?

## xmrig | 2018-03-18T23:23:46+00:00
About linker errors `__imp___acrt_iob_func`, duplicate #448, update MSYS2 to recent version should help.

But before you do it, can you please check try build with this libuv.a https://github.com/xmrig/xmrig-deps/commit/fc0d62b829a3d39866abb7e58c264fb22d6a7703

Previous version was built with gcc 7.3.0 and looks like it was bad idea, I rebuild it with older gcc.
Thank you.

## erotavlasme | 2018-03-25T20:01:38+00:00
@xmrig I updated MSYS2 as described in the link.
Now, I can successfully compile with gcc 7.3.0 and v. 2.1 libraries the latest xmrig v. 2.5.0 (x86 and x64).

# Action History
- Created by: axe-usat | 2018-01-30T19:53:34+00:00
- Closed at: 2018-11-05T12:48:41+00:00
