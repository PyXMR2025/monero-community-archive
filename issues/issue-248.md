---
title: Linux Debian 8, libuv "Unable to locate package" solved
source_url: https://github.com/xmrig/xmrig/issues/248
author: Zelecktor
assignees: []
labels:
- libuv
created_at: '2017-12-09T01:40:45+00:00'
updated_at: '2019-03-08T12:16:08+00:00'
type: issue
status: closed
closed_at: '2018-02-12T13:21:45+00:00'
---

# Original Description
Hello.
Im trying to mine on a Linux debian 8.

Already i followed this instructions and installed all libraries.

Note*** that libuv1-dev says that that directory doesnt exist so i cant install it via command.

sudo apt-get install git build-essential cmake libmicrohttpd-dev
sudo apt-get install git build-essential cmake libcurl4-openssl-dev
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake .. -DUV_INCLUDE_DIR=path/to/libuv/include -DUV_LIBRARY=path/to/libuv.a
sudo make

So when making it says this error:

root@openkore:~/xmrig/build# sudo make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 11%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[ 11%] Built target cpuid
Scanning dependencies of target xmrig
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
In file included from /root/xmrig/src/api/Api.cpp:27:0:
/root/xmrig/src/api/Api.h:28:16: fatal error: uv.h: No such file or directory
 #include <uv.h>
                ^
compilation terminated.
CMakeFiles/xmrig.dir/build.make:54: recipe for target 'CMakeFiles/xmrig.dir/src/api/Api.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/Api.cpp.o] Error 1
CMakeFiles/Makefile2:60: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:76: recipe for target 'all' failed
make: *** [all] Error 2

![captura](https://user-images.githubusercontent.com/19712343/33791305-85141dc0-dc68-11e7-9652-11d19ab77045.PNG)

There is another method to compile or get a compiled version because i think that linux debian is not supported :(
Please i need some help. thanks in advance


# Discussion History
## xmrig | 2017-12-11T10:27:56+00:00
You need libuv1 to build it required dependency.
Thank you.

## Zelecktor | 2017-12-11T16:13:15+00:00
how to install libuv1 on debian 8? it says "directory not found" on web :(


## ShadowJonathan | 2017-12-16T14:55:06+00:00
@Zelecktor 
>cmake .. -DUV_INCLUDE_DIR=path/to/libuv/include -DUV_LIBRARY=path/to/libuv.a

change those to the respective paths

## ShadowJonathan | 2017-12-18T12:49:18+00:00
run this
```
sudo apt-get install git build-essential cmake libmicrohttpd-dev libcurl4-openssl-dev
sudo apt-get install libuv1-dev
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake ..
```

## Zelecktor | 2017-12-31T15:15:07+00:00
root@dsifidhfisdf:~# sudo apt-get install libuv1-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package libuv1-dev

## z3dm4n | 2018-02-12T11:08:56+00:00
@Zelecktor Are you sure you're running Debian 8 aka Jessie? What does `cat /etc/debian_version` say?

## Zelecktor | 2018-02-12T13:21:44+00:00
@z3dm4n

Already solved.
Yes it was Debian 8 Jessie and debian 7 Wheezy
Just installed libuv with this command

`sudo apt-get install libuv-dev`

"libuv1-dev" says "Unable to locate package" but with libuv-dev worked fine.

## mbehrsf | 2019-03-08T12:16:08+00:00
I used to build xmrig 2.8.0 on debian 8 using the libuv-dev package from the debian backports repo: https://packages.debian.org/jessie-backports/libuv1-dev .

This doesn't seem to work anymore with xmrig 2.14.1, getting similar errors to the ones Zelecktor is describing. Upgrading to debian 9 fixed the problem.

# Action History
- Created by: Zelecktor | 2017-12-09T01:40:45+00:00
- Closed at: 2018-02-12T13:21:45+00:00
