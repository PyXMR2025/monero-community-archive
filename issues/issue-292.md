---
title: Can't compile on debian  / ROCK64 arm board
source_url: https://github.com/xmrig/xmrig/issues/292
author: peioe
assignees:
- xmrig
labels:
- arm
created_at: '2017-12-24T14:59:31+00:00'
updated_at: '2019-02-03T19:26:03+00:00'
type: issue
status: closed
closed_at: '2019-02-03T19:26:02+00:00'
---

# Original Description
I get this: 
make
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
c++: error: unrecognized argument in option ‘-march=armv8-a+crypto’
c++: note: valid arguments to ‘-march=’ are: armv2 armv2a armv3 armv3m armv4 armv4t armv5 armv5e armv5t armv5te armv6 armv6-m armv6j armv6k armv6s-m armv6t2 armv6z armv6zk armv7 armv7-a armv7-m armv7-r armv7e-m armv7ve armv8-a armv8-a+crc iwmmxt iwmmxt2 native
CMakeFiles/xmrig.dir/build.make:54: recipe for target 'CMakeFiles/xmrig.dir/src/api/Api.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/Api.cpp.o] Error 1
CMakeFiles/Makefile2:60: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:76: recipe for target 'all' failed
make: *** [all] Error 2

It should work with an up to date clone though right ?

# Discussion History
## adampointer | 2017-12-24T15:02:54+00:00
Master compiled ok for me on a rock64 running the xenial-minimal image . What are you thinking of mining on the rock64 out of interest?

## peioe | 2017-12-24T15:03:56+00:00
I'm using the OMV image. Not sure tbh, monero for now, I'm just mucking around ..

## adampointer | 2017-12-24T15:06:24+00:00
Looks like the crypto extensions are not recognised by the compiler. I would just try a different OS image and see if that works. Its going to have a terrible hashrate if it cannot use AES and NEON.

## peioe | 2017-12-24T15:08:09+00:00
OK, I might try with another image if I can.

Edit: I am flashing the xenial minimal image to a spare µSD.

## xmrig | 2019-02-03T19:26:02+00:00
https://github.com/xmrig/xmrig/commit/7e4858db2a537b4777073814157ce17a90740fab compilers without `-march=armv8-a+crypto` now supported.
Thank you.

# Action History
- Created by: peioe | 2017-12-24T14:59:31+00:00
- Closed at: 2019-02-03T19:26:02+00:00
