---
title: Segmentation fault compiling on ARM
source_url: https://github.com/monero-project/monero/issues/1256
author: abelboldu
assignees: []
labels: []
created_at: '2016-10-24T14:14:49+00:00'
updated_at: '2017-08-20T07:30:11+00:00'
type: issue
status: closed
closed_at: '2017-08-20T07:30:11+00:00'
---

# Original Description
I tried to compile on a RPi 2, because of that issue:

https://github.com/monero-project/monero/issues/1148

but also fails to compile:

```
[ 25%] Built target obj_ringct
make[3]: Entering directory '/home/vdo/src/monero/build/release'
Scanning dependencies of target ringct
make[3]: Leaving directory '/home/vdo/src/monero/build/release'
make[3]: Entering directory '/home/vdo/src/monero/build/release'
[ 25%] Linking CXX static library libringct.a
make[3]: Leaving directory '/home/vdo/src/monero/build/release'
[ 25%] Built target ringct
make[3]: Entering directory '/home/vdo/src/monero/build/release'
[ 26%] Generating testnet_blocks.o
Segmentation fault (core dumped)
make[3]: *** [src/blocks/CMakeFiles/blocks.dir/build.make:66: src/blocks/testnet_blocks.o] Error 139
make[3]: *** Deleting file 'src/blocks/testnet_blocks.o'
make[3]: Leaving directory '/home/vdo/src/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:1664: src/blocks/CMakeFiles/blocks.dir/all] Error 2
make[2]: Leaving directory '/home/vdo/src/monero/build/release'
make[1]: *** [Makefile:139: all] Error 2
make[1]: Leaving directory '/home/vdo/src/monero/build/release'
make: *** [Makefile:59: release-all] Error 2
```


# Discussion History
## ghost | 2016-10-24T14:22:18+00:00
Would you be able to include the entire compilation sequence to include the setting up of the flags at the beginning?


## abelboldu | 2016-10-24T15:31:15+00:00
http://pastebin.ca/3732366


## moneromooo-monero | 2016-10-24T16:34:33+00:00
Looks the same as https://github.com/monero-project/monero/issues/1131


## ghost | 2016-10-24T22:01:04+00:00
May also be related to #355 - there's no C standard for converting between `int` (as used in the functions in `blockexports.c`) and C++ `bool` used to define `m_testnet` which is how values are passed in.

Is there a way we can either drop `bool` entirely, or define it somewhere so it's internally consistent, as per http://stackoverflow.com/questions/1921539/using-boolean-values-in-c

Can I also ask why `blockexports` needs to be in C rather than C++?


## ghost | 2016-10-28T13:57:23+00:00
#1269 

I've brushed the dust off my RPi 2 and successfully built from scratch. I think your issues are with your installation of boost. 

Please delete all previous boost installs with `apt-get remove --purge libboost*` and then `sudo rm -rf /usr/local/lib/libboost*` and `sudo rm -rf /usr/local/include/boost`

Then install boost from scratch by pulling down with `wget`. Building and installing will take at least 12 hours, then building monero itself will take another 4. You will hit an out-of-memory issue linking the daemon so increase the swap size as per: https://www.bitpi.co/2015/02/11/how-to-change-raspberry-pis-swapfile-size-on-rasbian/


## radfish | 2016-11-18T23:07:45+00:00
See #974. Try Invoking cmake with: `-DCMAKE_LINKER=/usr/bin/ld.gold`


## moneromooo-monero | 2017-08-13T15:47:41+00:00
Is gold something that'd be installed with fairly high probability ? If so, it might be a good thing if someone wanted to autodetect it in cmake.

## radfish | 2017-08-20T06:06:17+00:00
@moneromooo-monero On Arch and on Ubuntu ld.gold is owned by binutils package, so high probability. But, iiurc, the build failure with ld has been fixed already after I reported it at the time: http://lists.gnu.org/archive/html/bug-binutils/2016-08/msg00165.html

## moneromooo-monero | 2017-08-20T07:27:09+00:00
Nice, thanks.
I'll just call it fixed then.

+resolved

# Action History
- Created by: abelboldu | 2016-10-24T14:14:49+00:00
- Closed at: 2017-08-20T07:30:11+00:00
