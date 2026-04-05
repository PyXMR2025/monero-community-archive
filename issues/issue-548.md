---
title: mac os, dev version (2.6.0b2 not compiling)
source_url: https://github.com/xmrig/xmrig/issues/548
author: steelrayx
assignees: []
labels:
- bug
created_at: '2018-04-12T16:33:47+00:00'
updated_at: '2018-05-24T17:11:44+00:00'
type: issue
status: closed
closed_at: '2018-04-12T22:30:15+00:00'
---

# Original Description
git checkout dev
Already on 'dev'
Your branch is up-to-date with 'origin/dev'.
MacBook-Pro-DMITRY-2:xmrig dmitry$ git pull
Already up-to-date.
MacBook-Pro-DMITRY-2:xmrig dmitry$ mkdir build
MacBook-Pro-DMITRY-2:xmrig dmitry$ cd build
MacBook-Pro-DMITRY-2:build dmitry$ cmake ..
-- The C compiler identification is AppleClang 9.1.0.9020039
-- The CXX compiler identification is AppleClang 9.1.0.9020039
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: /usr/local/lib/libuv.a  
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found MHD: /usr/local/lib/libmicrohttpd.dylib  
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/dmitry/Downloads/xmrig/build
MacBook-Pro-DMITRY-2:build dmitry$ make
Scanning dependencies of target cpuid
[  1%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  3%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  5%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  7%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[  9%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[ 11%] Linking C static library libcpuid.a
[ 11%] Built target cpuid
Scanning dependencies of target xmrig
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
/Users/dmitry/Downloads/xmrig/src/core/Config.cpp:282:28: warning: comparison of unsigned expression >= 0 is always true [-Wtautological-compare]
        if (m_threadsCount >= 0 && arg < 1024) {
            ~~~~~~~~~~~~~~ ^  ~
1 warning generated.
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/core/ConfigLoader.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/core/ConfigWatcher.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/core/CommonConfig.cpp.o
/Users/dmitry/Downloads/xmrig/src/core/CommonConfig.cpp:269:50: error: cannot pass object of non-trivial type 'xmrig::c_str' through variadic method; call will abort at runtime [-Wnon-pod-varargs]
    LOG_NOTICE("configuration saved to: \"%s\"", m_fileName);
                                                 ^
1 error generated.
make[2]: *** [CMakeFiles/xmrig.dir/src/core/CommonConfig.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


# Discussion History
## BigslimVdub | 2018-04-12T21:51:35+00:00
Did you edit the cmakeList before compiling? I couldn’t get it to compile turning httpd or sumo to off. What OS are you using? What ver of Brew are you using?

## steelrayx | 2018-04-12T21:54:22+00:00
Did you edit the cmakeList before compiling? - NO
What OS are you using? 10.13.4 (17E199)
brew info cmake - cmake: stable 3.10.2 (bottled), HEAD

## xmrig | 2018-04-12T22:06:38+00:00
Fixed. Thank you.

## steelrayx | 2018-04-12T22:30:15+00:00
Thank you!

## 2010phenix | 2018-05-24T16:55:23+00:00
@xmrig MAN )))
someone even make famous xmrig ))))))))))
https://www.coindesk.com/new-strain-of-malware-hijacks-apple-macs-to-mine-monero/

## xmrig | 2018-05-24T17:11:44+00:00
In v2.5.1 broken reconnect to pool I also deleted this release, but that someone use this version...

# Action History
- Created by: steelrayx | 2018-04-12T16:33:47+00:00
- Closed at: 2018-04-12T22:30:15+00:00
