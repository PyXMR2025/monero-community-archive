---
title: v2.6.0-beta1 still trying to link to http with -DWITH-HTTPD=OFF option
source_url: https://github.com/xmrig/xmrig/issues/513
author: bittaurus
assignees: []
labels:
- duplicate
created_at: '2018-04-07T13:20:16+00:00'
updated_at: '2018-04-07T13:26:25+00:00'
type: issue
status: closed
closed_at: '2018-04-07T13:26:25+00:00'
---

# Original Description
[build]$ cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/local/lib/libuv.a -DWITH_HTTPD=OFF
-- The C compiler identification is GNU 4.8.5
-- The CXX compiler identification is GNU 4.8.5
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Found UV: /usr/local/lib/libuv.a  
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ec2-user/xmrig-2.6.0-beta1/build
[build]$ make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o

... nothing fatal until ...

[ 95%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 97%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[100%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
Linking CXX executable xmrig
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::start(xmrig::Controller*)':
Api.cpp:(.text+0x1d): undefined reference to `ApiRouter::ApiRouter(xmrig::Controller*)'
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::exec(xmrig::HttpRequest const&, xmrig::HttpReply&)':
Api.cpp:(.text+0x7c): undefined reference to `ApiRouter::exec(xmrig::HttpRequest const&, xmrig::HttpReply&)'
Api.cpp:(.text+0x81): undefined reference to `ApiRouter::get(xmrig::HttpRequest const&, xmrig::HttpReply&) const'
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::tick(Hashrate const*)':
Api.cpp:(.text+0xa3): undefined reference to `ApiRouter::tick(Hashrate const*)'
CMakeFiles/xmrig.dir/src/api/Api.cpp.o: In function `Api::tick(NetworkState const&)':
Api.cpp:(.text+0xd3): undefined reference to `ApiRouter::tick(NetworkState const&)'
collect2: error: ld returned 1 exit status
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


# Discussion History
## xmrig | 2018-04-07T13:26:25+00:00
Duplicate #502. Already fixed.

# Action History
- Created by: bittaurus | 2018-04-07T13:20:16+00:00
- Closed at: 2018-04-07T13:26:25+00:00
