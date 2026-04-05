---
title: 'fatal error C1083: Cannot open include file: ''syslog.h'''
source_url: https://github.com/xmrig/xmrig/issues/895
author: pekster85
assignees: []
labels: []
created_at: '2018-12-13T14:38:17+00:00'
updated_at: '2019-08-02T13:03:54+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:03:54+00:00'
---

# Original Description
I'm experimenting here.absolute greenhorn. no results in issues, so new thread.
Did XMR-STAK before, found it educational, wanted to test this one, and compare, without their respective donation levels to compare effectiveness more accurately. (same coin-same pc-same algo) So.
Followed the guide
figured out the deps-catch [little expedition here]
Got to the point where it all does what its suppossed to do,compile,
except for 
(1)CMake Error at CMakeLists.txt:182 (add_subdirectory):
  add_subdirectory given source "src/3rdparty/libcpuid" which is not an
  existing directory.(wich it SO IS!!) [if i say this PC is made in Mongolia, i offend the Mongolians]
and(2)actually writing output due to 
fatal error C1083: Cannot open include file: 'syslog.h'
wich i have down in the CmakeError.txt after the compile attempt according to guide.

Hereby my cmd story, and yes i tried MSYS(seems MSYS & "mingw64.exe" are two diffrent things-still figuring that out) so, any help is greatly appreciated.

Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

K:\Users\amo>cd K:\MINER\xmrig-2.8.3\src\build

K:\MINER\xmrig-2.8.3\src\build>cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG
_DEPS=K:\xmrig-deps\msvc2017\x64
CMake Error at CMakeLists.txt:182 (add_subdirectory):
  add_subdirectory given source "src/3rdparty/libcpuid" which is not an
  existing directory.


-- Configuring incomplete, errors occurred!
See also "K:/MINER/xmrig-2.8.3/src/build/CMakeFiles/CMakeOutput.log".
See also "K:/MINER/xmrig-2.8.3/src/build/CMakeFiles/CMakeError.log".

K:\MINER\xmrig-2.8.3\src\build>cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG
_DEPS=K:\xmrig-deps\msvc2017\x64
-- The C compiler identification is MSVC 19.16.27025.1
-- The CXX compiler identification is MSVC 19.16.27025.1
-- Check for working C compiler: K:/Program Files (x86)/Microsoft Visual Studio/
2017/Community/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/cl.exe
-- Check for working C compiler: K:/Program Files (x86)/Microsoft Visual Studio/
2017/Community/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/cl.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: K:/Program Files (x86)/Microsoft Visual Studi
o/2017/Community/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/cl.exe
-- Check for working CXX compiler: K:/Program Files (x86)/Microsoft Visual Studi
o/2017/Community/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/cl.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: K:/xmrig-deps/msvc2017/x64/lib/libuv.lib
CMake Error at CMakeLists.txt:182 (add_subdirectory):
  add_subdirectory given source "src/3rdparty/libcpuid" which is not an
  existing directory.


-- Found OpenSSL: K:/xmrig-deps/msvc2017/x64/lib/libcrypto.lib (found version "1
.1.1")
-- The ASM_MASM compiler identification is MSVC
-- Found assembler: K:/Program Files (x86)/Microsoft Visual Studio/2017/Communit
y/VC/Tools/MSVC/14.16.27023/bin/Hostx86/x64/ml64.exe
-- Looking for syslog.h
-- Looking for syslog.h - not found
-- Found MHD: K:/xmrig-deps/msvc2017/x64/lib/libmicrohttpd.lib
-- Configuring incomplete, errors occurred!
See also "K:/MINER/xmrig-2.8.3/src/build/CMakeFiles/CMakeOutput.log".
See also "K:/MINER/xmrig-2.8.3/src/build/CMakeFiles/CMakeError.log".

K:\MINER\xmrig-2.8.3\src\build>




# Discussion History
## DeadManWalkingTO | 2019-03-17T15:22:41+00:00
Please try to build the [latest XMRig version](https://github.com/xmrig/xmrig/releases/latest) with `-DWITH_LIBCPUID=OFF` to remove cpuid lib.

Take a look to the issue #894.

Does the issue still exist?
Feedback please.
Thank you!

# Action History
- Created by: pekster85 | 2018-12-13T14:38:17+00:00
- Closed at: 2019-08-02T13:03:54+00:00
