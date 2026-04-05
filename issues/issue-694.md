---
title: '/usr/bin/ld: final link failed: Bad value'
source_url: https://github.com/xmrig/xmrig/issues/694
author: kuttkutt
assignees: []
labels: []
created_at: '2018-06-15T09:34:20+00:00'
updated_at: '2018-11-05T13:56:50+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:56:50+00:00'
---

# Original Description
Hi, I have some trouble to compile xmrig v2.6.3

I use libuv1-dev 1.20.3-1 and libuv1 1.20.3-1

cmake.. looks fin 



>-- The C compiler identification is GNU 4.9.2
>-- The CXX compiler identification is GNU 4.9.2
>-- Check for working C compiler: /usr/bin/cc
>-- Check for working C compiler: /usr/bin/cc -- works
>-- Detecting C compiler ABI info
>-- Detecting C compiler ABI info - done
>-- Check for working CXX compiler: /usr/bin/c++
>-- Check for working CXX compiler: /usr/bin/c++ -- works
>-- Detecting CXX compiler ABI info
>-- Detecting CXX compiler ABI info - done
>-- Found UV: /usr/lib/x86_64-linux-gnu/libuv.a
>-- Looking for syslog.h
>-- Looking for syslog.h - found
>-- Found MHD: /usr/lib/x86_64-linux-gnu/libmicrohttpd.so
>-- Configuring done
>-- Generating done
>-- Build files have been written to: /home/kutt/src/xmrig-master/build


however "make" shoots an error on final build :/

>[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/Httpd.cpp.o
>[100%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/HttpRequest.cpp.o
>Linking CXX executable xmrig
>/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/4.9/../../../x86_64-linux-gnu/libuv.a(libuv_la-loop.o): >unrecognized relocation (0x2a) in section `.text'
>/usr/bin/ld: final link failed: Bad value
>collect2: error: ld returned 1 exit status
>CMakeFiles/xmrig.dir/build.make:1188: recipe for target 'xmrig' failed
>make[2]: *** [xmrig] Error 1
>CMakeFiles/Makefile2:60: recipe for target 'CMakeFiles/xmrig.dir/all' failed
>make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
>Makefile:76: recipe for target 'all' failed
>make: *** [all] Error 2


I have no clue what could be the caus of this - any ideas?

# Discussion History
## kuttkutt | 2018-06-18T07:28:57+00:00
Hmm .. so no ideas ;) 

may I ask what the minimum version of gcc and gcc++ ist to compile xmrig 2.6.3?

## xmrig | 2018-06-18T07:59:14+00:00
I think you should try use older libuv version, according your logs error somewhere in libuv, actually very strange error. gcc 4.9 it is a minimum, at least I never heard about successful builds with more older versions.
Thank you.

## kuttkutt | 2018-06-18T08:34:44+00:00
Hello, 
I added the Stretch repo to my sources and installed gcc-6 and gcc++-6

The build worked without any problems. 
So I guess gcc-4.9 is too old

# Action History
- Created by: kuttkutt | 2018-06-15T09:34:20+00:00
- Closed at: 2018-11-05T13:56:50+00:00
