---
title: Can't compile on Centos 6
source_url: https://github.com/xmrig/xmrig/issues/831
author: rampso
assignees: []
labels: []
created_at: '2018-10-21T04:35:16+00:00'
updated_at: '2018-10-21T23:12:04+00:00'
type: issue
status: closed
closed_at: '2018-10-21T23:12:04+00:00'
---

# Original Description
[  1%] Built target xmrig-asm
[  3%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
cc1: error: invalid option argument ‘-Ofast’
make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/build.make:59: src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:150: src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
make: *** [Makefile:76: all] Error 2

Running into a issue when running "make" command
I have gone through a few issues on here with no luck. Would appreciate some help
using 
gcc (GCC) 7.3.1 20180303 (Red Hat 7.3.1-5)
with latest libuv from github. 

Any suggestions?

# Discussion History
## srwx666 | 2018-10-21T14:37:11+00:00
cc1: error: invalid option argument ‘-Ofast’
means that You are not using gcc7.3 defenetley....



## rampso | 2018-10-21T15:56:05+00:00
I managed to get it working by compiling it on a alpine linux VM, then copied the required files from /lib/ to all my boxs and it appears to be running on all of them now. 
Could this cause any issues for me in the future or should I be good?

# Action History
- Created by: rampso | 2018-10-21T04:35:16+00:00
- Closed at: 2018-10-21T23:12:04+00:00
