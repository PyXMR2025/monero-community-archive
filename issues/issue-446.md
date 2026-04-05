---
title: Bus error
source_url: https://github.com/xmrig/xmrig/issues/446
author: jovan2009
assignees: []
labels:
- bug
- arm
created_at: '2018-03-14T14:58:18+00:00'
updated_at: '2022-02-10T08:39:24+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:59:45+00:00'
---

# Original Description
Hi, I compiled latest xmrig v 2.5.0 on my android phone (arm v7a, cortex a53, android 5.1) in termux and now when I try to run the executable I get the message "Bus error". The compiler is Clang 5.0.1 and I ran simply 
`cmake .. -DWITH_AEON=OFF -DWITH_HTTPD=OFF`
Previously I compiled xmrig successfully many times with the same setup, so it's something that has changed lately that gives this error.

# Discussion History
## 2010phenix | 2018-03-14T15:05:40+00:00
Can i ask, how much you have H\s on your miner 2.4  ?

## jovan2009 | 2018-03-14T15:07:46+00:00
About 8 - 8.5 max. There is an app NeoNeonMiner that gets to 9-9.2 H/s but it hasn't nicehash support and I need it to use it with xmrig-proxy.

## xmrig | 2018-03-14T16:38:51+00:00
@jovan2009 can you make debug build?
Change [this line](https://github.com/xmrig/xmrig/blob/master/cmake/flags.cmake#L55) to:
```
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -Wall -fno-exceptions -fno-rtti -Wno-missing-braces")
```
Difference is added `-g`.

Then rebuild, after that run `gdb ./xmrig`, enter command `r`.
If miner crashed, enter command `bt` and show output.
Thank you.

## jovan2009 | 2018-03-14T22:29:25+00:00
Here we go:
![screenshot_2018-03-15-00-19-54](https://user-images.githubusercontent.com/36099360/37434318-df21d8d2-27e7-11e8-807f-b0b9dcbdfafe.png)


## xmrig | 2018-03-14T22:32:50+00:00
You need type `r` then press enter or if you not use config file `r all command line options`, after that miner will be started.

## jovan2009 | 2018-03-14T22:58:48+00:00
(gdb) r -o xxxxxx -u Lenovo+100 -p x -k --nicehash --cpu-priority 0
Starting program: /data/data/com.termux/files/home/xmrig/build/xmrig -o xxxxxx -u Lenovo+100 -p x -k --nicehash --cpu-priority 0
WARNING: linker: /data/data/com.termux/files/home/xmrig/build/xmrig: unused DT entry: type 0x6ffffef5 arg 0x13bc

Program received signal SIGBUS, Bus error.
cryptonight_single_hash<524288u, 2097152u, 2097136u, true, 1> (
    input=0x2a039b80 <test_input>,
    size=<optimized out>,
    output=0xbefffa10, ctx=0xb644e1c0)
    at /data/data/com.termux/files/home/xmrig/src/crypto/CryptoNight_arm.h:340
340         VARIANT1_INIT(0);
(gdb) bt
#0  cryptonight_single_hash<524288u, 2097152u, 2097136u, true, 1> (
    input=0x2a039b80 <test_input>,
    size=<optimized out>,
    output=0xbefffa10, ctx=0xb644e1c0)
    at /data/data/com.termux/files/home/xmrig/src/crypto/CryptoNight_arm.h:340
#1  0x2a0336d8 in CryptoNight::selfTest (
    algo=<optimized out>)
    at /data/data/com.termux/files/home/xmrig/src/crypto/CryptoNight.cpp:179
#2  0x2a011b64 in App::exec (
    this=0xbefffa84)
    at /data/data/com.termux/files/home/xmrig/src/App.cpp:125
#3  0x2a0255fc in main (
    argc=<optimized out>,
    argv=<optimized out>)
---Type <return> to continue, or q <return> to quit---
   .termux/files/home/xmrig/src/xmrig.cpp:30
(gdb)

## jovan2009 | 2018-03-14T23:05:17+00:00
I clicked on link #3 and apparently I referenced a pull request... Not sure how to undo that.

## xmrig | 2018-03-14T23:13:31+00:00
Thank you, I get exactly what I need from gdb, I will better look into tomorrow.
Short conclusion new PoW is somehow broken on you device, for temporary solution you can remove new PoW self check. Remove anything from line 178 to 186 https://github.com/xmrig/xmrig/blob/master/src/crypto/CryptoNight.cpp#L178

## ghost | 2018-03-15T03:47:03+00:00
Same issue compiling for Raspberry Pi 2 and 3 (ARMv7 and ARMv8), compiler gcc 6.3.0.  Commenting out lines 178-186 in CryptoNight.cpp did the trick for now.

## xmrig | 2018-03-15T04:13:13+00:00
Bad issue, on all my ARM hardware, includes Raspberry Pi 3 with gcc 6.3.0 no crashes appear.

## ghost | 2018-03-15T11:51:26+00:00
You're right. I recompiled without adding any additional flags (for the Pi's architecture) and it works fine on the Pi 3. I'll figure which flags. Sorry for the bad issue.

## xmrig | 2018-03-15T14:35:13+00:00
Sorry I mean "bad" because hard to fix, I can't reproduce the crash, but definitely there is a bug.
Thank you.

## ghost | 2018-03-15T17:04:06+00:00
The flag causing the issue for the Raspberry Pi 3 was -mneon-for-64bits, not a noticeable performance hit for me not including it, but interesting that it did not cause problems earlier.

Other flags added (and not causing problems) for around +15% in hashrate are:

(for the Pi 3)
-mcpu=cortex-a53 -mfloat-abi=hard -mfpu=neon-fp-armv8 -mtune=cortex-a53 -ffast-math -funsafe-math-optimizations -funsafe-loop-optimizations

(for the Pi 2):
-mcpu=cortex-a7 -mfloat-abi=hard -mfpu=neon-vfpv4 -mtune=cortex-a7 -ffast-math -funsafe-math-optimizations -funsafe-loop-optimizations

## xmrig | 2018-03-15T22:21:30+00:00
I found what cause crash, when use `-mneon-for-64bits` compiler use instruction `vldr` to load data from input buffer, but this instruction works only with aligned data (8 bytes, 16 bytes, ...) new algorithm required to load data with offset 35 bytes it caused SIGBUS (Bus error). With offset 32 or 40 bytes we newer know about this issue. I will try find workaround, but if not success, can't use `-mneon-for-64bits` in future.
Thank you.

## jovan2009 | 2018-03-15T22:45:39+00:00
Is this flag causing trouble in my case too? Because I didn't modify flags.cmake, just git cloned xmrig and built it.

## xmrig | 2018-03-15T23:08:29+00:00
Probably clang enable equivalent of this flag, by default.

## xmrig | 2018-03-16T01:19:32+00:00
Likely fixed, changes in `bug-446` branch, to switch branch in git use following commands:
```
git pull
git checkout bug-446
```
Then use `make` as usual.
Thank you.

## jovan2009 | 2018-03-16T01:55:29+00:00
Unfortunately the same error. I made again a debug build, this gdb output (mangled by copy paste from termux, but I think is usable):

"apropos word" to search for commands related to "word"...                       Reading symbols from ./xmrig...done.       (gdb) r -o xxx -u Lenovo+100 -k --nicehash                                Starting program: /data/data/com.termux/files/home/xmrig250/build/xmrig -o xxx -u Lenovo+100 -k --nicehash           WARNING: linker: /data/data/com.termux/files/home/xmrig250/build/xmrig: unused DT entry: type 0x6ffffef5 arg 0x13d4                                                         Program received signal SIGBUS, Bus error. cryptonight_single_hash<524288u, 2097152u, 2097136u, true, 1> (                           input=0x2a03bd50 <test_input>,             size=<optimized out>,                      output=0xbefffa18, ctx=0xb644e1c0)         at /data/data/com.termux/files/home/xmrig250/src/crypto/CryptoNight_arm.h:340     340         VARIANT1_INIT(0);              (gdb) bt                                   #0  cryptonight_single_hash<524288u, 2097152u, 2097136u, true, 1> (                       input=0x2a03bd50 <test_input>,             size=<optimized out>,                      output=0xbefffa18, ctx=0xb644e1c0)         at /data/data/com.termux/files/home/xmrig250/src/crypto/CryptoNight_arm.h:340     #1  0x2a033ca4 in CryptoNight::selfTest (      algo=0)                                    at /data/data/com.termux/files/home/xmrig250/src/crypto/CryptoNight.cpp:179       #2  0x2a011dd4 in App::exec (                  this=0xbefffa94)                           at /data/data/com.termux/files/home/xmrig250/src/App.cpp:125                      #3  0x2a025b5c in main (                       argc=<optimized out>,                      argv=<optimized out>)                  ---Type <return> to continue, or q <return> to quit---                                    at /data/data/com.termux/files/home/xmrig250/src/xmrig.cpp:30                     (gdb)


## xmrig | 2018-03-16T02:07:58+00:00
Weird, file `CryptoNight_monero.h` look like https://github.com/xmrig/xmrig/blob/bug-446/src/crypto/CryptoNight_monero.h#L41 ?

## jovan2009 | 2018-03-16T02:18:03+00:00
![screenshot_2018-03-16-04-11-20](https://user-images.githubusercontent.com/36099360/37500236-fd300404-28d0-11e8-9984-7c4161d75683.png)


## xmrig | 2018-03-16T02:21:46+00:00
Okay, thank you, fix not help in your case :-(
This code work fine with enabled flag `-mneon-for-64bits`

## jovan2009 | 2018-03-16T10:57:17+00:00
I managed to compile it with GCC 7.2.1... I made a single modification to flags.cmake to make it compile with GCC:
https://github.com/xmrig/xmrig/blob/3d41629170afcfe26d08d4c1b8ce97e38285fea6/cmake/flags.cmake#L31
to
`set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -shared-libgcc")`

...Same error, so it's not only in Clang.

I made a debug compile also, added -g flag, this is full termux transcript:

```
Welcome to Termux!

Wiki:            https://wiki.termux.com
Community forum: https://termux.com/community
IRC channel:     #termux on freenode
Gitter chat:     https://gitter.im/termux/termux
Mailing list:    termux+subscribe@groups.io

Search packages:   pkg search <query>
Install a package: pkg install <package>
Upgrade packages:  pkg upgrade
Learn more:        pkg help
$ git clone --branch bug-446 https://github.com/xmrig/xmrig.git xmrigb446
Cloning into 'xmrigb446'...
remote: Counting objects: 2913, done.
Receiving objects:  17% (496/2913), 180.01 Receiving objects:  18% (525/2913), 180.01 Receiving objects:  19% (554/2913), 180.01 Receiving objects:  20% (583/2913), 180.01 Receiving objects:  21% (612/2913), 180.01 Receiving objects:  22% (641/2913), 180.01 Receiving objects:  23% (670/2913), 180.01 Receiving objects:  24% (700/2913), 180.01 Receiving objects:  24% (727/2913), 180.01 Receiving objects:  25% (729/2913), 180.01 Receiving objects:  26% (758/2913), 180.01 Receiving objects:  27% (787/2913), 180.01 Receiving objects:  28% (816/2913), 180.01 Receiving objects:  29% (845/2913), 460.01 Receiving objects:  30% (874/2913), 460.01 Receiving objects:  31% (904/2913), 460.01 Receiving objects:  32% (933/2913), 460.01 Receiving objects:  33% (962/2913), 460.01 Receiving objects:  34% (991/2913), 460.01 Receiving objects:  35% (1020/2913), 460.01Receiving objects:  36% (1049/2913), 460.01Receiving objects:  37% (1078/2913), 460.01Receiving objects:  38% (1107/2913), 460.01Receiving objects:  39% (1137/2913), 460.01Receiving objects:  40% (1166/2913), 460.01Receiving objects:  41% (1195/2913), 460.01Receiving objects:  42% (1224/2913), 460.01Receiving objects:  43% (1253/2913), 460.01Receiving objects:  44% (1282/2913), 460.01Receiving objects:  45% (1311/2913), 460.01Receiving objects:  46% (1340/2913), 460.01Receiving objects:  47% (1370/2913), 460.01Receiving objects:  48% (1399/2913), 460.01Receiving objects:  49% (1428/2913), 460.01Receiving objects:  50% (1457/2913), 460.01Receiving objects:  51% (1486/2913), 460.01Receiving objects:  52% (1515/2913), 460.01Receiving objects:  53% (1544/2913), 460.01Receiving objects:  54% (1574/2913), 460.01Receiving objects:  55% (1603/2913), 460.01Receiving objects:  56% (1632/2913), 460.01Receiving objects:  57% (1661/2913), 460.01Receiving objects:  58% (1690/2913), 460.01Receiving objects:  59% (1719/2913), 460.01Receiving objects:  60% (1748/2913), 460.01Receiving objects:  61% (1777/2913), 460.01Receiving objects:  62% (1807/2913), 460.01Receiving objects:  63% (1836/2913), 460.01Receiving objects:  64% (1865/2913), 460.01Receiving objects:  65% (1894/2913), 460.01Receiving objects:  66% (1923/2913), 460.01Receiving objects:  67% (1952/2913), 460.01Receiving objects:  68% (1981/2913), 460.01Receiving objects:  69% (2010/2913), 460.01Receiving objects:  70% (2040/2913), 460.01Receiving objects:  71% (2069/2913), 460.01Receiving objects:  72% (2098/2913), 460.01Receiving objects:  73% (2127/2913), 460.01Receiving objects:  74% (2156/2913), 460.01Receiving objects:  75% (2185/2913), 460.01Receiving objects:  76% (2214/2913), 460.01Receiving objects:  77% (2244/2913), 804.01Receiving objects:  78% (2273/2913), 804.01Receiving objects:  79% (2302/2913), 804.01Receiving objects:  80% (2331/2913), 804.01Receiving objects:  81% (2360/2913), 804.01Receiving objects:  82% (2389/2913), 804.01Receiving objects:  83% (2418/2913), 804.01Receiving objects:  84% (2447/2913), 804.01Receiving objects:  85% (2477/2913), 804.01Receiving objects:  86% (2506/2913), 804.01Receiving objects:  87% (2535/2913), 804.01Receiving objects:  88% (2564/2913), 804.01Receiving objects:  89% (2593/2913), 804.01Receiving objects:  90% (2622/2913), 804.01Receiving objects:  91% (2651/2913), 804.01Receiving objects:  92% (2680/2913), 804.01Receiving objects:  93% (2710/2913), 804.01Receiving objects:  94% (2739/2913), 804.01Receiving objects:  95% (2768/2913), 804.01Receiving objects:  96% (2797/2913), 804.01Receiving objects:  97% (2826/2913), 804.01Receiving objects:  98% (2855/2913), 804.01remote: Total 2913 (delta 0), reused 0 (delta 0), pack-reused 2913
Receiving objects:  99% (2884/2913), 804.01Receiving objects: 100% (2913/2913), 804.01Receiving objects: 100% (2913/2913), 912.32 KiB | 535.00 KiB/s, done.
Resolving deltas: 100% (2101/2101), done.
$ cp $HOME/storage/shared/flags.cmake $HOME/xmrigb446/cmake
$ cd xmrigb446/
$ mkdir build && cd build
$ cmake .. -DWITH_HTTPD=OFF -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_CXX_COMPILER=g++-7       -- The C compiler identification is GNU 7.2.1
-- The CXX compiler identification is GNU 7.2.1
-- Check for working C compiler: /data/data/com.termux/files/usr/bin/gcc-7
-- Check for working C compiler: /data/data/com.termux/files/usr/bin/gcc-7 -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /data/data/com.termux/files/usr/bin/g++-7
-- Check for working CXX compiler: /data/data/com.termux/files/usr/bin/g++-7 -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: /data/data/com.termux/files/usr/lib/libuv.so
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /data/data/com.termux/files/home/xmrigb446/build
$ make
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_unix.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_arm.cpp.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
[100%] Linking CXX executable xmrig
[100%] Built target xmrig
$ ./xmrig -o xxx -u Lenovo+100 -p x -k --nicehash --cpu-priority 0
WARNING: linker: ./xmrig: unused DT entry: type 0x6ffffef5 arg 0x1350
Bus error
$ gdb ./xmrig
GNU gdb (GDB) 8.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "arm-linux-androideabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation---Type <return> to continue, or q <return> to quit---
 resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./xmrig...done.
(gdb) r -o xxx -u Lenovo+100 -p x -k --nicehash --cpu-priority 0
Starting program: /data/data/com.termux/files/home/xmrigb446/build/xmrig -o xxx -u Lenovo+100 -p x -k --nicehash --cpu-priority 0
WARNING: linker: /data/data/com.termux/files/home/xmrigb446/build/xmrig: unused DT entry: type 0x6ffffef5 arg 0x1350

Program received signal SIGBUS, Bus error.
cryptonight_single_hash<524288u, 2097152u, 2097136u, true, 1> (ctx=0xb644e1c0,
    output=0x0, size=<optimized out>,
    input=0x2a0665d0 <test_input>)
    at /data/data/com.termux/files/home/xmrigb446/src/crypto/CryptoNight_arm.h:340
340         VARIANT1_INIT(0);
(gdb) bt
#0  cryptonight_single_hash<524288u, 2097152u, 2097136u, true, 1> (ctx=0xb644e1c0,
    output=0x0, size=<optimized out>,
    input=0x2a0665d0 <test_input>)
    at /data/data/com.termux/files/home/xmrigb446/src/crypto/CryptoNight_arm.h:340
#1  cryptonight_av3_softaes (
    input=0x2a0665d0 <test_input>,
    size=<optimized out>, output=0x0,
    ctx=0xb644e1c0, variant=1)
    at /data/data/com.termux/files/home/xmrigb446/src/crypto/CryptoNight.cpp:73
#2  0x2a054244 in CryptoNight::selfTest (
    algo=0)
    at /data/data/com.termux/files/home/xmrigb446/src/crypto/CryptoNight.cpp:179
#3  0x2a061194 in CryptoNight::selfTest (
    algo=<optimized out>)
---Type <return> to continue, or q <return> to quit---
    at /data/data/com.termux/files/home/xmrigb446/src/crypto/CryptoNight.cpp:159
#4  CryptoNight::init (
    algo=<optimized out>,
    variant=<optimized out>)
    at /data/data/com.termux/files/home/xmrigb446/src/crypto/CryptoNight.cpp:148
#5  0x2a016570 in App::exec (
    this=0xbefffa7c)
    at /data/data/com.termux/files/home/xmrigb446/src/App.cpp:125
#6  0x2a00a008 in main (
    argc=<optimized out>,
    argv=<optimized out>)
    at /data/data/com.termux/files/home/xmrigb446/src/xmrig.cpp:30
(gdb)
```


## xmrig | 2018-03-16T20:24:28+00:00
@jovan2009 one more try, please check this commit https://github.com/xmrig/xmrig/commit/5648b5a8035f08e67a5193729a2310228f144a56

If it not helps, please run following commands:
```
gdb ./xmrig
```

```
break cryptonight_av3_softaes
r -o xxx -u Lenovo+100 -p x -k --nicehash --cpu-priority 0
disassemble
```

And show output.

## jovan2009 | 2018-03-16T23:29:33+00:00
I did `git pull` inside xmrigb446 folder, I hope it was enough to get the updated CryptoNight_monero.h 
Compiled with GCC, didn't work unfortunately:
```
cd xmrigb446/
$ git checkout
M       cmake/flags.cmake
Your branch is up to date with 'origin/bug-446'.
$ git pull
remote: Counting objects: 40, done.        remote: Compressing objects:  90% (10/11)  remote: Compressing objects: 100% (11/11)  remote: Compressing objects: 100% (11/11), done.
remote: Total 40 (delta 29), reused 40 (delta 29), pack-reused 0
 Unpacking objects: 100% (40/40), done.     From https://github.com/xmrig/xmrig           9891614..5648b5a  bug-446    -> origin/bug-446
* [new branch]      feature-donate-failover -> origin/feature-donate-failover           3d41629..38c3932  master     -> origin/master
Updating 9891614..5648b5a
Fast-forward
src/crypto/CryptoNight_monero.h | 3 ++-    1 file changed, 2 insertions(+), 1 deletion(-)
$ git checkout
M       cmake/flags.cmake
Your branch is up to date with 'origin/bug-446'.
$ cd build/
$ rm -rf *
$ cmake .. -DWITH_HTTPD=OFF -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_CXX_COMPILER=g++-7
-- The C compiler identification is GNU 7.2.1
-- The CXX compiler identification is GNU 7.2.1
-- Check for working C compiler: /data/data/com.termux/files/usr/bin/gcc-7
-- Check for working C compiler: /data/data/com.termux/files/usr/bin/gcc-7 -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /data/data/com.termux/files/usr/bin/g++-7
-- Check for working CXX compiler: /data/data/com.termux/files/usr/bin/g++-7 -- works -- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done  -- Detecting CXX compile features
-- Detecting CXX compile features - done   -- Found UV: /data/data/com.termux/files/usr/lib/libuv.so
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /data/data/com.termux/files/home/xmrigb446/build $ make
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_unix.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_arm.cpp.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
[100%] Linking CXX executable xmrig
[100%] Built target xmrig
$ ./xmrig -o xxx -u Lenovo1+100 -p x -k --nicehash --cpu-priority 0 --donate-level=1
WARNING: linker: ./xmrig: unused DT entry: type 0x6ffffef5 arg 0x1350
Bus error
$ gdb ./xmrig
GNU gdb (GDB) 8.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "arm-linux-androideabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation---Type <return> to continue, or q <return> to quit---
resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./xmrig...done.
(gdb) break cryptonight_av3_softaes
Breakpoint 1 at 0x60be4: file /data/data/com.termux/files/home/xmrigb446/src/crypto/CryptoNight.cpp, line 72.
(gdb) r -o xxx -u Lenovo+100 -p x -k --nicehash --cpu-priority 0
Starting program: /data/data/com.termux/files/home/xmrigb446/build/xmrig -o xxx -u Lenovo+100 -p x -k --nicehash --cpu-priority 0
WARNING: linker: /data/data/com.termux/files/home/xmrigb446/build/xmrig: unused DT entry: type 0x6ffffef5 arg 0x1350             
Breakpoint 1, cryptonight_av3_softaes (
input=0x2a0665a0 <test_input>,
size=76, output=0xbefffa00,
ctx=0xb644e1c0, variant=0)
at /data/data/com.termux/files/home/xmrigb446/src/crypto/CryptoNight.cpp:72
72      static void cryptonight_av3_softaes(const void *input, size_t size, void *output, cryptonight_ctx *ctx, int variant) {
(gdb) disassemble
 Dump of assembler code for function cryptonight_av3_softaes(void const*, size_t, void*, cryptonight_ctx*, int):
=> 0x2a060be4 <+0>:     push    {r4, r5, r6, r7, r8, r9, r10, r11, lr}
0x2a060be8 <+4>:     sub     sp, sp, #124       ; 0x7c
0x2a060bec <+8>:     mov     r6, r3        0x2a060bf0 <+12>:    ldr     r12, [sp, #160]    ; 0xa0
0x2a060bf4 <+16>:    str     r2, [sp, #100]     ; 0x64
0x2a060bf8 <+20>:    cmp     r12, #0       0x2a060bfc <+24>:    str     r3, [sp, #96]      ; 0x60
0x2a060c00 <+28>:    beq     0x2a060e94 <cryptonight_av3_softaes(void const*, size_t, void*, cryptonight_ctx*, int)+688>
---Type <return> to continue, or q <return> to quit---
0x2a060c04 <+32>:    cmp     r12, #1       0x2a060c08 <+36>:    bne     0x2a060e8c <cryptonight_av3_softaes(void const*, size_t, void*, cryptonight_ctx*, int)+680>         0x2a060c0c <+40>:    mov     r2, r6        0x2a060c10 <+44>:    mov     r3, #200  ; 0xc8
   0x2a060c14 <+48>:    mov     r4, r0        0x2a060c18 <+52>:    bl      0x2a03d8d0 <keccak>
0x2a060c1c <+56>:    add     r1, r4, #35; 0x23
  0x2a060c20 <+60>:    ldrd    r2, [r6, #192]     ; 0xc0
       0x2a060c24 <+64>:    movw    r5, #65520; 0xfff0
 0x2a060c28 <+68>:    movt    r5, #31       0x2a060c2c <+72>:    ldrd    r8, [r1]   ---Type <return> to continue, or q <return> to quit---
          0x2a060c30 <+76>:    mov     r0, r6        0x2a060c34 <+80>:    str     r5, [sp, #88]      ; 0x58
       0x2a060c38 <+84>:    mov     r10, r6       0x2a060c3c <+88>:    ldr     r1, [r6, #416]     ; 0x1a0
      0x2a060c40 <+92>:    movw    r7, #21264; 0x5310
 0x2a060c44 <+96>:    strd    r8, [sp, #104]     ; 0x68
       0x2a060c48 <+100>:   movt    r7, #7        0x2a060c4c <+104>:   strd    r2, [sp, #112]     ; 0x70
       0x2a060c50 <+108>:   mov     r9, #524288; 0x80000
            0x2a060c54 <+112>:   ldrd    r4, [sp, #104]     ; 0x68
       0x2a060c58 <+116>:   ldrd    r2, [sp, #1---Type <return> to continue, or q <return> to quit---
12]     ; 0x70
       0x2a060c5c <+120>:   str     r7, [sp, #92]      ; 0x5c
       0x2a060c60 <+124>:   eor     r8, r4, r2    0x2a060c64 <+128>:   str     r9, [sp, #48]      ; 0x30
   0x2a060c68 <+132>:   eor     r9, r5, r3    0x2a060c6c <+136>:   strd    r8, [sp, #72]      ; 0x48
       0x2a060c70 <+140>:   bl      0x2a0542ac <cn_explode_scratchpad<2097152, true>(__m128i const*, __m128i*)>
0x2a060c74 <+144>:   ldrd    r2, [r6, #24]
   0x2a060c78 <+148>:   ldrd    r0, [r6, #56]      ; 0x38
   0x2a060c7c <+152>:   mov     r12, r10      0x2a060c80 <+156>:   ldrd    r4, [r10, #---Type <return> to continue, or q <return> to quit---
48]     ; 0x30
       0x2a060c84 <+160>:   ldrd    r6, [r6, #16]
  0x2a060c88 <+164>:   eor     r9, r3, r1    0x2a060c8c <+168>:   mov     r3, r10       0x2a060c90 <+172>:   eor     r8, r2, r0    0x2a060c94 <+176>:   eor     r1, r5, r7    0x2a060c98 <+180>:   eor     r0, r4, r6    0x2a060c9c <+184>:   ldrd    r2, [r3, #32]
   0x2a060ca0 <+188>:   vmov    d19, r8, r9   0x2a060ca4 <+192>:   ldrd    r10, [r10]
   0x2a060ca8 <+196>:   ldr     r6, [r12, #416]    ; 0x1a0
   0x2a060cac <+200>:   vmov    d18, r0, r1   0x2a060cb0 <+204>:   eor     r10, r10, r---Type <return> to continue, or q <return> to quit---
2
   0x2a060cb4 <+208>:   ldrd    r0, [r12, #8]
  0x2a060cb8 <+212>:   eor     r11, r11, r3
   0x2a060cbc <+216>:   ldrd    r2, [r12, #40]     ; 0x28
       0x2a060cc0 <+220>:   str     r6, [sp, #84]      ; 0x54
       0x2a060cc4 <+224>:   eor     r4, r0, r2
   0x2a060cc8 <+228>:   eor     r5, r1, r3    0x2a060ccc <+232>:   strd    r4, [sp, #16]
  0x2a060cd0 <+236>:   ldr     r8, [sp, #88]      ; 0x58
       0x2a060cd4 <+240>:   vmov    d0, r10, r11
   0x2a060cd8 <+244>:   ldr     r5, [sp, #8---Type <return> to continue, or q <return> to quit---
4]      ; 0x54
       0x2a060cdc <+248>:   mov     r7, #0
   0x2a060ce0 <+252>:   and     r0, r8, r10   0x2a060ce4 <+256>:   vldr    d1, [sp, #16]
  0x2a060ce8 <+260>:   add     r4, r5, r0
   0x2a060cec <+264>:   mov     r0, r4        0x2a060cf0 <+268>:   bl      0x2a053be8 <soft_aesenc(uint32_t const*, __m128i)>       0x2a060cf4 <+272>:   ldr     r6, [sp, #92]      ; 0x5c
       0x2a060cf8 <+276>:   veor    q1, q0, q9
   0x2a060cfc <+280>:   vst1.64 {d0-d1}, [sp :64]
   0x2a060d00 <+284>:   ldr     r2, [sp]      0x2a060d04 <+288>:   vorr    q9, q0, q0
   0x2a060d08 <+292>:   ldr     lr, [sp, #4---Type <return> to continue, or q <return> to quit---
       ]
   0x2a060d0c <+296>:   vst1.32 {d2-d3}, [r4]
   0x2a060d10 <+300>:   and     r1, r2, r8    0x2a060d14 <+304>:   ldrb    r9, [r4, #11]
  0x2a060d18 <+308>:   add     r12, r5, r1
   0x2a060d1c <+312>:   mov     r0, r2        0x2a060d20 <+316>:   and     r3, r9, #1
   0x2a060d24 <+320>:   asr     r8, r9, #3    0x2a060d28 <+324>:   and     r5, r8, #6
   0x2a060d2c <+328>:   orr     r2, r5, r3    0x2a060d30 <+332>:   lsl     r1, r2, #1
   0x2a060d34 <+336>:   lsr     r3, r6, r1    0x2a060d38 <+340>:   mov     r1, r7
   0x2a060d3c <+344>:   and     r8, r3, #48; 0x30
---Type <return> to continue, or q <return> to quit---
   0x2a060d40 <+348>:   mov     r3, #0        0x2a060d44 <+352>:   eor     r9, r9, r8
   0x2a060d48 <+356>:   strb    r9, [r4, #11]
   0x2a060d4c <+360>:   ldrd    r8, [r12]     0x2a060d50 <+364>:   umull   r4, r5, r0, r9
 0x2a060d54 <+368>:   umull   r6, r7, lr, r8
 0x2a060d58 <+372>:   umlal   r10, r11, r9, lr
   0x2a060d5c <+376>:   adds    r6, r6, r4    0x2a060d60 <+380>:   mla     r5, r9, r1, r5
   0x2a060d64 <+384>:   str     r6, [sp, #28]
   0x2a060d68 <+388>:   mla     r7, lr, r3, r7
  ---Type <return> to continue, or q <return> to quit---
          0x2a060d6c <+392>:   strd    r10, [sp, #64]     ; 0x40
       0x2a060d70 <+396>:   mov     r11, r1       0x2a060d74 <+400>:   mov     r10, r0       0x2a060d78 <+404>:   strd    r10, [sp, #56]     ; 0x38
       0x2a060d7c <+408>:   adcs    r4, r7, r5    0x2a060d80 <+412>:   mov     r1, r3        0x2a060d84 <+416>:   ldr     r5, [sp, #56]      ; 0x38
       0x2a060d88 <+420>:   ldrd    r2, [r12, #8]
   0x2a060d8c <+424>:   mul     r0, r10, r1   0x2a060d90 <+428>:   mov     r10, r11
   0x2a060d94 <+432>:   mla     lr, r8, r10, r0
0x2a060d98 <+436>:   strd    r2, [sp]   ---Type <return> to continue, or q <return> to quit---
          0x2a060d9c <+440>:   umull   r2, r3, r5, r8
 0x2a060da0 <+444>:   mov     r0, #0
   0x2a060da4 <+448>:   str     r0, [sp, #24]
  0x2a060da8 <+452>:   ldrd    r6, [sp, #24]
   0x2a060dac <+456>:   add     r1, lr, r3    0x2a060db0 <+460>:   str     r4, [sp, #32]
  0x2a060db4 <+464>:   str     r0, [sp, #36]      ; 0x24
       0x2a060db8 <+468>:   movcs   r0, #1
   0x2a060dbc <+472>:   adds    lr, r2, r6    0x2a060dc0 <+476>:   ldrd    r10, [sp, #64]     ; 0x40
       0x2a060dc4 <+480>:   adcs    r7, r1, r7    0x2a060dc8 <+484>:   ldrd    r2, [sp, #3---Type <return> to continue, or q <return> to quit---
       2]
  0x2a060dcc <+488>:   str     r0, [sp, #44]      ; 0x2c
       0x2a060dd0 <+492>:   movcs   r6, #1        0x2a060dd4 <+496>:   adds    r10, r10, r2
   0x2a060dd8 <+500>:   adc     r11, r11, r3
   0x2a060ddc <+504>:   str     r3, [sp, #40]      ; 0x28
       0x2a060de0 <+508>:   ldrd    r2, [sp, #16]
  0x2a060de4 <+512>:   ldrd    r4, [sp, #40]      ; 0x28
       0x2a060de8 <+516>:   adds    r2, r2, lr    0x2a060dec <+520>:   ldr     lr, [sp, #48]      ; 0x30
       0x2a060df0 <+524>:   adc     r3, r3, r7 ---Type <return> to continue, or q <return> to quit---
          0x2a060df4 <+528>:   adds    r10, r4, r10
   0x2a060df8 <+532>:   adc     r11, r5, r11
   0x2a060dfc <+536>:   ldrd    r4, [sp]      0x2a060e00 <+540>:   eor     r4, r4, r2    0x2a060e04 <+544>:   eor     r5, r5, r3
   0x2a060e08 <+548>:   strd    r4, [sp, #16]
   0x2a060e0c <+552>:   ldrd    r4, [sp, #72]      ; 0x48
       0x2a060e10 <+556>:   eor     r4, r4, r2    0x2a060e14 <+560>:   eor     r5, r5, r3
   0x2a060e18 <+564>:   mov     r2, r4        0x2a060e1c <+568>:   adds    r4, r10, r6   0x2a060e20 <+572>:   mov     r3, r5        0x2a060e24 <+576>:   adc     r5, r11, #0---Type <return> to continue, or q <return> to quit---

           0x2a060e28 <+580>:   subs    r7, lr, #1    0x2a060e2c <+584>:   strd    r4, [r12]     0x2a060e30 <+588>:   str     r7, [sp, #48]      ; 0x30
       0x2a060e34 <+592>:   eor     r10, r4, r8   0x2a060e38 <+596>:   eor     r11, r5, r9   0x2a060e3c <+600>:   strd    r2, [r12, #8]
  0x2a060e40 <+604>:   bne     0x2a060cd0 <cryptonight_av3_softaes(void const*, size_t, void*, cryptonight_ctx*, int)+236>         0x2a060e44 <+608>:   ldr     r9, [sp, #96]      ; 0x60
       0x2a060e48 <+612>:   ldr     r8, [pc, #568]     ; 0x2a061088 <cryptonight_av3_softa---Type <return> to continue, or q <return> to quit---
       es(void const*, size_t, void*, cryptonight_ctx*, int)+1188>
     0x2a060e4c <+616>:   mov     r1, r9        0x2a060e50 <+620>:   ldr     r0, [r9, #416]     ; 0x1a0
      0x2a060e54 <+624>:   bl      0x2a05e378 <cn_implode_scratchpad<2097152, true>(__m128i const*, __m128i*)>
0x2a060e58 <+628>:   mov     r0, r9        0x2a060e5c <+632>:   mov     r1, #24
   0x2a060e60 <+636>:   add     r7, pc, r8    0x2a060e64 <+640>:   bl      0x2a03c814 <keccakf>
            0x2a060e68 <+644>:   ldrb    r12, [r9]
   0x2a060e6c <+648>:   mov     r0, r9        0x2a060e70 <+652>:   and     r6, r12, #3
   0x2a060e74 <+656>:   ldr     r2, [sp, #1---Type <return> to continue, or q <return> to quit---
       00]     ; 0x64
       0x2a060e78 <+660>:   mov     r1, #200  ; 0xc8
   0x2a060e7c <+664>:   ldr     r3, [r7, r6, lsl #2]
            0x2a060e80 <+668>:   add     sp, sp, #124       ; 0x7c
       0x2a060e84 <+672>:   pop     {r4, r5, r6, r7, r8, r9, r10, r11, lr}
     0x2a060e88 <+676>:   bx      r3            0x2a060e8c <+680>:   add     sp, sp, #124       ; 0x7c
       0x2a060e90 <+684>:   pop     {r4, r5, r6, r7, r8, r9, r10, r11, pc}
     0x2a060e94 <+688>:   mov     r2, r6        0x2a060e98 <+692>:   mov     r4, r3        0x2a060e9c <+696>:   mov     r3, #200  ; 0xc8
---Type <return> to continue, or q <return> to quit---
          0x2a060ea0 <+700>:   mov     r10, r6       0x2a060ea4 <+704>:   bl      0x2a03d8d0 <keccak>
0x2a060ea8 <+708>:   ldr     r1, [r6, #416]     ; 0x1a0
      0x2a060eac <+712>:   mov     r0, r6        0x2a060eb0 <+716>:   movw    r5, #65520; 0xfff0
 0x2a060eb4 <+720>:   bl      0x2a0542ac <cn_explode_scratchpad<2097152, true>(__m128i const*, __m128i*)>
0x2a060eb8 <+724>:   movt    r5, #31       0x2a060ebc <+728>:   ldrd    r2, [r6, #24]
  0x2a060ec0 <+732>:   mov     r11, #524288       ; 0x80000
    0x2a060ec4 <+736>:   ldrd    r0, [r6, #56]      ; 0x38
    ---Type <return> to continue, or q <return> to quit---
          0x2a060ec8 <+740>:   str     r5, [sp, #84]      ; 0x54
       0x2a060ecc <+744>:   ldrd    r6, [r6, #16]
  0x2a060ed0 <+748>:   eor     r8, r2, r0    0x2a060ed4 <+752>:   ldrd    r4, [r4, #48]      ; 0x30
       0x2a060ed8 <+756>:   eor     r9, r3, r1    0x2a060edc <+760>:   mov     r0, r10       0x2a060ee0 <+764>:   str     r11, [sp, #24]
 0x2a060ee4 <+768>:   eor     r2, r4, r6    0x2a060ee8 <+772>:   eor     r3, r5, r7    0x2a060eec <+776>:   mov     r6, r10       0x2a060ef0 <+780>:   ldrd    r10, [r10]    0x2a060ef4 <+784>:   vmov    d18, r2, r3   0x2a060ef8 <+788>:   ldrd    r2, [r0, #3---Type <return> to continue, or q <return> to quit---
       2]
  0x2a060efc <+792>:   ldrd    r4, [r0, #8]
   0x2a060f00 <+796>:   eor     r11, r11, r3
   0x2a060f04 <+800>:   ldr     r3, [r6, #416]     ; 0x1a0
      0x2a060f08 <+804>:   ldrd    r0, [r0, #40]      ; 0x28
       0x2a060f0c <+808>:   vmov    d19, r8, r9   0x2a060f10 <+812>:   eor     r10, r10, r2
   0x2a060f14 <+816>:   str     r3, [sp, #72]      ; 0x48
       0x2a060f18 <+820>:   eor     r2, r4, r0    0x2a060f1c <+824>:   eor     r3, r5, r1    0x2a060f20 <+828>:   strd    r2, [sp, #1---Type <return> to continue, or q <return> to quit---
       6]
  0x2a060f24 <+832>:   ldr     r7, [sp, #84]      ; 0x54
       0x2a060f28 <+836>:   vmov    d0, r10, r11
   0x2a060f2c <+840>:   ldr     r9, [sp, #72]      ; 0x48
       0x2a060f30 <+844>:   and     r1, r7, r10   0x2a060f34 <+848>:   vldr    d1, [sp, #16]
  0x2a060f38 <+852>:   add     r8, r9, r1    0x2a060f3c <+856>:   mov     r0, r8        0x2a060f40 <+860>:   bl      0x2a053be8 <soft_aesenc(uint32_t const*, __m128i)>       0x2a060f44 <+864>:   mov     r1, #0        0x2a060f48 <+868>:   mov     r3, #0        0x2a060f4c <+872>:   vst1.64 {d0-d1}, [s---Type <return> to continue, or q <return> to quit---
       p :64]
  0x2a060f50 <+876>:   veor    q3, q0, q9    0x2a060f54 <+880>:   ldr     r2, [sp]      0x2a060f58 <+884>:   vorr    q9, q0, q0    0x2a060f5c <+888>:   ldr     lr, [sp, #4]
   0x2a060f60 <+892>:   and     r12, r2, r7   0x2a060f64 <+896>:   vst1.32 {d6-d7}, [r8]
  0x2a060f68 <+900>:   add     r12, r9, r12
   0x2a060f6c <+904>:   mov     r0, r2        0x2a060f70 <+908>:   ldrd    r8, [r12]     0x2a060f74 <+912>:   umull   r6, r7, lr, r8
 0x2a060f78 <+916>:   umull   r4, r5, r0, r9
  ---Type <return> to continue, or q <return> to quit---
          0x2a060f7c <+920>:   umlal   r10, r11, r9, lr
   0x2a060f80 <+924>:   adds    r4, r6, r4
   0x2a060f84 <+928>:   mla     r7, lr, r3, r7
 0x2a060f88 <+932>:   str     r4, [sp, #52]      ; 0x34
       0x2a060f8c <+936>:   mla     r5, r9, r1, r5
   0x2a060f90 <+940>:   strd    r10, [sp, #40]     ; 0x28
       0x2a060f94 <+944>:   mov     r11, r1       0x2a060f98 <+948>:   mov     r10, r0       0x2a060f9c <+952>:   strd    r10, [sp, #32]
 0x2a060fa0 <+956>:   adcs    r6, r7, r5    0x2a060fa4 <+960>:   mov     r1, r3        0x2a060fa8 <+964>:   ldr     r5, [sp, #3---Type <return> to continue, or q <return> to quit---
       2]
   0x2a060fac <+968>:   ldrd    r2, [r12, #8]
   0x2a060fb0 <+972>:   mul     r0, r10, r1   0x2a060fb4 <+976>:   mov     r10, r11      0x2a060fb8 <+980>:   mla     lr, r8, r10, r0
0x2a060fbc <+984>:   strd    r2, [sp]      0x2a060fc0 <+988>:   umull   r2, r3, r5, r8
 0x2a060fc4 <+992>:   mov     r0, #0
   0x2a060fc8 <+996>:   str     r0, [sp, #48]      ; 0x30
       0x2a060fcc <+1000>:  str     r6, [sp, #56]      ; 0x38
   0x2a060fd0 <+1004>:  add     r1, lr, r3    0x2a060fd4 <+1008>:  ldrd    r6, [sp, #4---Type <return> to continue, or q <return> to quit---
       8]      ; 0x30
       0x2a060fd8 <+1012>:  str     r0, [sp, #60]      ; 0x3c
       0x2a060fdc <+1016>:  movcs   r0, #1        0x2a060fe0 <+1020>:  adds    lr, r2, r6    0x2a060fe4 <+1024>:  ldrd    r10, [sp, #40]     ; 0x28
       0x2a060fe8 <+1028>:  ldrd    r2, [sp, #56]      ; 0x38
       0x2a060fec <+1032>:  adcs    r7, r1, r7    0x2a060ff0 <+1036>:  str     r0, [sp, #68]      ; 0x44
       0x2a060ff4 <+1040>:  movcs   r6, #1        0x2a060ff8 <+1044>:  adds    r10, r10, r2
   0x2a060ffc <+1048>:  adc     r11, r11, r3
   0x2a061000 <+1052>:  str     r3, [sp, #6---Type <return> to continue, or q <return> to quit---
       4]      ; 0x40
       0x2a061004 <+1056>:  ldrd    r2, [sp, #16]
  0x2a061008 <+1060>:  adds    r4, r2, lr    0x2a06100c <+1064>:  adc     r3, r3, r7    0x2a061010 <+1068>:  mov     r5, r3        0x2a061014 <+1072>:  ldrd    r2, [sp, #64]      ; 0x40
       0x2a061018 <+1076>:  strd    r4, [r12, #8]
  0x2a06101c <+1080>:  adds    r10, r2, r10
   0x2a061020 <+1084>:  adc     r11, r3, r11
   0x2a061024 <+1088>:  ldrd    r2, [sp]      0x2a061028 <+1092>:  eor     r2, r2, r4    0x2a06102c <+1096>:  eor     r3, r3, r5    0x2a061030 <+1100>:  strd    r2, [sp, #1---Type <return> to continue, or q <return> to quit---
       6]
  0x2a061034 <+1104>:  adds    r4, r10, r6   0x2a061038 <+1108>:  ldr     r2, [sp, #24]
  0x2a06103c <+1112>:  adc     r5, r11, #0   0x2a061040 <+1116>:  eor     r10, r4, r8   0x2a061044 <+1120>:  strd    r4, [r12]     0x2a061048 <+1124>:  subs    lr, r2, #1    0x2a06104c <+1128>:  eor     r11, r5, r9   0x2a061050 <+1132>:  str     lr, [sp, #24]
  0x2a061054 <+1136>:  bne     0x2a060f24 <cryptonight_av3_softaes(void const*, size_t, void*, cryptonight_ctx*, int)+832>      ---Type <return> to continue, or q <return> to quit---
          0x2a061058 <+1140>:  ldr     r9, [sp, #96]      ; 0x60
       0x2a06105c <+1144>:  ldr     r5, [pc, #40]      ; 0x2a06108c <cryptonight_av3_softaes(void const*, size_t, void*, cryptonight_ctx*, int)+1192>
     0x2a061060 <+1148>:  mov     r1, r9        0x2a061064 <+1152>:  ldr     r0, [r9, #416]     ; 0x1a0
      0x2a061068 <+1156>:  bl      0x2a05e378 <cn_implode_scratchpad<2097152, true>(__m128i const*, __m128i*)>
0x2a06106c <+1160>:  mov     r0, r9        0x2a061070 <+1164>:  mov     r1, #24       0x2a061074 <+1168>:  add     r7, pc, r5    0x2a061078 <+1172>:  bl      0x2a03c814 <keccakf>
            0x2a06107c <+1176>:  mov     r0, r9     ---Type <return> to continue, or q <return> to quit---
          0x2a061080 <+1180>:  ldrb    r12, [r9]     0x2a061084 <+1184>:  b       0x2a060e70 <cryptonight_av3_softaes(void const*, size_t, void*, cryptonight_ctx*, int)+652>         0x2a061088 <+1188>:  muleq   r1, r0, sp    0x2a06108c <+1192>:  andeq   r7, r1, r12, ror r11
         End of assembler dump.
(gdb)
```


## sahaab | 2018-03-30T22:59:54+00:00
Not able to build on armv7 either, tried different devices, and different forks as well.
Edit: commenting out line 178 to 186 is a temporary fix, it works with it

## jovan2009 | 2018-04-11T07:26:09+00:00
Well, it works with the above-mentioned lines commented out but as soon the donating process begins the program stops with the same bus error. I mine electroneum which I guess didn't change POW and still works but donation requires new POW it seems so I have to restart miner on regular basis.

![screenshot_2018-04-11-10-28-29](https://user-images.githubusercontent.com/36099360/38602448-6e2665a2-3d73-11e8-9f4e-ab3b10c11335.png)


## Patometro06 | 2018-04-20T22:08:04+00:00
Same type problem here.
I try to compile on Swiss Mobility ZEI 403 with an ARMV7 SC7731C quad core processor.

Android 6.0, Termux with llvm6.0.

My debug:
[debug.txt](https://github.com/xmrig/xmrig/files/1933808/debug.txt)

GNU gdb (GDB) 8.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "arm-linux-androideabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./xmrig...done.
(gdb) break cryptonight_av3_d[Ksoftaes
Breakpoint 1 at 0x35258: file /data/data/com.termux/files/home/xmrig/src/crypto/CryptoNight.cpp, line 73.
(gdb) r-o xxx Lenovo+q[K100 -p x -k --nicehash 
 --cpu-priority 0
(gdb) r -o xxx -u Leb[Knovo+100 -p x -k --nice 
hash --cpu-priority 0
Starting program: /data/data/com.termux/files/home/xmrig/build/xmrig -o xxx -u Lenovo+100 -p x -k --nicehash --cpu-priority 0

Breakpoint 1, cryptonight_av3_softaes (
    input=0x2a03d6a0 <test_input> "\001", 
    size=76, output=0xbefffa08 " ", 
    ctx=0x2a0553f0, variant=0)
    at /data/data/com.termux/files/home/xmrig/src/crypto/CryptoNight.cpp:73
73	    CRYPTONIGHT_HASH(single, MONERO_ITER, MONERO_MEMORY, MONERO_MASK, true)
(gdb) disassemble
Dump of assembler code for function cryptonight_av3_softaes(unsigned char const*, unsigned int, unsigned char*, cryptonight_ctx*, int):
   0x2a035254 <+0>:	ldr	r12, [sp]
=> 0x2a035258 <+4>:	cmp	r12, #0
   0x2a03525c <+8>:	beq	0x2a03526c <cryptonight_av3_softaes(unsigned char const*, unsigned int, unsigned char*, cryptonight_ctx*, int)+24>
   0x2a035260 <+12>:	cmp	r12, #1
   0x2a035264 <+16>:	bxne	lr
   0x2a035268 <+20>:	b	0x2a037414 <cryptonight_single_hash<524288u, 2097152u, 2097136u, true, 1>(unsigned char const*, unsigned int, unsigned char*, cryptonight_ctx*)>
   0x2a03526c <+24>:	b	0x2a0377a8 <cryptonight_single_hash<524288u, 2097152u, 2097136u, true, 0>(unsigned char const*, unsigned int, unsigned char*, cryptonight_ctx*)>
End of assembler dump.


## xmrig | 2018-06-01T21:41:06+00:00
Finally got device where I can reproduce the issue. Please check it, this issue should be solved in dev branch. https://github.com/xmrig/xmrig/commit/d900a6d9dd091008b0366fb73a01aac6d910168f
Thank you.

## philtimmes | 2018-06-01T21:49:39+00:00
I solved it with memcpy. Thanks.

On Fri, Jun 1, 2018, 2:41 PM xmrig <notifications@github.com> wrote:

> Finally got device where I can reproduce the issue. Please check it, this
> issue should be solved in dev branch. d900a6d
> <https://github.com/xmrig/xmrig/commit/d900a6d9dd091008b0366fb73a01aac6d910168f>
> Thank you.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/446#issuecomment-394016611>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AFPVhx_PcrrxotM7ZWK1RwMKRf1BX2Paks5t4bT5gaJpZM4SqlyN>
> .
>


## iranagame | 2018-06-03T21:41:09+00:00
@xmrig Not fixed, still facing with BUS Error on ARMv7 :(

## xmrig | 2018-06-03T21:48:41+00:00
@iranagame Did you switch to dev branch? `git checkout dev && git pull`.
Thank you.

## iranagame | 2018-06-03T21:54:39+00:00
@xmrig Just manually editing `CryptoNight_monero.h` isn't enough?

## xmrig | 2018-06-03T21:59:20+00:00
Should enough, but use git instead is better.
Thank you.

## iranagame | 2018-06-03T22:01:54+00:00
@xmrig Thanks,
Done but still getting Bus Error on my Galaxy S III device.
@sahaab commenting out those lines on which classes?

## xmrig | 2018-06-03T22:24:25+00:00
@iranagame So you rebuild source too as well too `make clean && make`? memcpy should solve this issue.

## iranagame | 2018-06-03T23:29:08+00:00
![1397-03-14 03 57 35](https://user-images.githubusercontent.com/34863253/40892378-9913f434-67ab-11e8-9151-063e0906f26c.jpg)

Yes, I'm building it through NDK cmake, arm-v8 version works fine but v7 not even with memcpy.


## iranagame | 2018-06-04T11:01:37+00:00
@xmrig Any ideas? is it possible that using dev version of libuv caused to this error?


## jovan2009 | 2018-06-06T10:17:09+00:00
I try to compile the dev branch but I get a compilation error:
```
$ git clone --branch dev https://github.com/xmrig/xmrig.git xmrigdev
Cloning into 'xmrigdev'...
remote: Counting objects: 4511, done.
remote: Compressing objects: 100% (10/10)  remote: Compressing objects: 100% (10/10), done.
Receiving objects:  15% (677/4511), 180.01 Receiving objects:  16% (722/4511), 180.01 Receiving objects:  17% (767/4511), 180.01 Receiving objects:  17% (789/4511), 380.01 Receiving objects:  18% (812/4511), 380.01 Receiving objects:  19% (858/4511), 380.01 Receiving objects:  20% (903/4511), 380.01 Receiving objects:  21% (948/4511), 380.01 Receiving objects:  22% (993/4511), 380.01 Receiving objects:  23% (1038/4511), 380.01Receiving objects:  24% (1083/4511), 380.01Receiving objects:  25% (1128/4511), 380.01Receiving objects:  26% (1173/4511), 380.01Receiving objects:  27% (1218/4511), 380.01Receiving objects:  28% (1264/4511), 628.01Receiving objects:  29% (1309/4511), 628.01Receiving objects:  30% (1354/4511), 628.01Receiving objects:  31% (1399/4511), 628.01Receiving objects:  32% (1444/4511), 628.01Receiving objects:  33% (1489/4511), 628.01Receiving objects:  34% (1534/4511), 628.01Receiving objects:  35% (1579/4511), 628.01Receiving objects:  36% (1624/4511), 628.01Receiving objects:  37% (1670/4511), 628.01Receiving objects:  38% (1715/4511), 628.01Receiving objects:  39% (1760/4511), 628.01Receiving objects:  40% (1805/4511), 628.01Receiving objects:  41% (1850/4511), 628.01Receiving objects:  42% (1895/4511), 628.01Receiving objects:  42% (1909/4511), 628.01Receiving objects:  43% (1940/4511), 628.01Receiving objects:  44% (1985/4511), 628.01Receiving objects:  45% (2030/4511), 628.01Receiving objects:  46% (2076/4511), 628.01Receiving objects:  47% (2121/4511), 628.01Receiving objects:  48% (2166/4511), 628.01Receiving objects:  49% (2211/4511), 924.01Receiving objects:  50% (2256/4511), 924.01Receiving objects:  51% (2301/4511), 924.01Receiving objects:  52% (2346/4511), 924.01Receiving objects:  53% (2391/4511), 924.01Receiving objects:  54% (2436/4511), 924.01Receiving objects:  55% (2482/4511), 924.01Receiving objects:  56% (2527/4511), 924.01Receiving objects:  57% (2572/4511), 924.01Receiving objects:  58% (2617/4511), 924.01Receiving objects:  59% (2662/4511), 924.01Receiving objects:  60% (2707/4511), 924.01Receiving objects:  61% (2752/4511), 924.01Receiving objects:  62% (2797/4511), 924.01Receiving objects:  63% (2842/4511), 924.01Receiving objects:  64% (2888/4511), 924.01Receiving objects:  65% (2933/4511), 924.01Receiving objects:  66% (2978/4511), 924.01Receiving objects:  67% (3023/4511), 924.01Receiving objects:  68% (3068/4511), 924.01Receiving objects:  69% (3113/4511), 924.01Receiving objects:  70% (3158/4511), 924.01Receiving objects:  71% (3203/4511), 924.01Receiving objects:  72% (3248/4511), 924.01Receiving objects:  73% (3294/4511), 924.01Receiving objects:  74% (3339/4511), 924.01Receiving objects:  75% (3384/4511), 924.01Receiving objects:  76% (3429/4511), 924.01Receiving objects:  77% (3474/4511), 924.01Receiving objects:  78% (3519/4511), 924.01Receiving objects:  79% (3564/4511), 924.01Receiving objects:  80% (3609/4511), 924.01Receiving objects:  81% (3654/4511), 924.01Receiving objects:  82% (3700/4511), 924.01Receiving objects:  83% (3745/4511), 924.01Receiving objects:  84% (3790/4511), 924.01Receiving objects:  85% (3835/4511), 924.01Receiving objects:  86% (3880/4511), 924.01Receiving objects:  87% (3925/4511), 924.01Receiving objects:  88% (3970/4511), 1.25 MReceiving objects:  89% (4015/4511), 1.25 MReceiving objects:  90% (4060/4511), 1.25 MReceiving objects:  91% (4106/4511), 1.25 MReceiving objects:  92% (4151/4511), 1.25 MReceiving objects:  93% (4196/4511), 1.25 MReceiving objects:  94% (4241/4511), 1.25 MReceiving objects:  95% (4286/4511), 1.25 MReceiving objects:  96% (4331/4511), 1.25 MReceiving objects:  97% (4376/4511), 1.25 MReceiving objects:  98% (4421/4511), 1.25 Mremote: Total 4511 (delta 1), reused 1 (delta 0), pack-reused 4501
Receiving objects:  99% (4466/4511), 1.25 MReceiving objects: 100% (4511/4511), 1.25 MReceiving objects: 100% (4511/4511), 1.35 MiB | 500.00 KiB/s, done.
Resolving deltas: 100% (3313/3313), done.
$ cd xmrigdev/
$ git checkout
Your branch is up to date with 'origin/dev'.
$ mkdir build
$ cd build/
$ cmake .. -DWITH_HTTPD=OFF                -- The C compiler identification is Clang 6.0.0
-- The CXX compiler identification is Clang 6.0.0
-- Check for working C compiler: /data/data/com.termux/files/usr/bin/cc
-- Check for working C compiler: /data/data/com.termux/files/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /data/data/com.termux/files/usr/bin/c++
-- Check for working CXX compiler: /data/data/com.termux/files/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: /data/data/com.termux/files/usr/lib/libuv.so
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Configuring done
-- Generating done
-- Build files have been written to: /data/data/com.termux/files/home/xmrigdev/build
$ make
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
In file included from /data/data/com.termux/files/home/xmrigdev/src/core/Controller.cpp:41:
/data/data/com.termux/files/home/xmrigdev/src/common/log/SysLog.h:28:10: fatal error:
      'interfaces/ILogBackend.h' file not
      found
#include "interfaces/ILogBackend.h"
         ^~~~~~~~~~~~~~~~~~~~~~~~~~
1 error generated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:310: CMakeFiles/xmrig.dir/src/core/Controller.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:68: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```
I tried both GCC and Clang and the errors are about the same.

## iranagame | 2018-06-06T11:32:28+00:00
@jovan2009 I compiled latest `dev` branch through native NDK and it's works fine, I can share binaries if you're interested.
@xmrig I find the problem on my arm-v7 device, if I set `--threads` flags to half my actual available threads (for ie `--threads=2` on Galaxy S III) then it will works fine otherwise, I got bus error. Any ideas? 

## philtimmes | 2018-06-06T21:53:12+00:00
Also, try updating CMake to a newer version... That appears to be a
problems with CMake.

On Sun, Jun 3, 2018, 2:48 PM xmrig <notifications@github.com> wrote:

> @iranagame <https://github.com/iranagame> Did you switch to dev branch? git
> checkout dev && git pull.
> Thank you.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/446#issuecomment-394194158>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AFPVh5YW_e4bh4Wl3JxTyPL-Rpd9Sim0ks5t5Fm_gaJpZM4SqlyN>
> .
>


## xmrig | 2018-06-07T00:35:50+00:00
@jovan2009 fixed in https://github.com/xmrig/xmrig/commit/974cb4162accd74836effe314c83d8ee62664605
@iranagame debug it, maybe bus error appear in different place.

## jovan2009 | 2018-06-07T09:59:44+00:00
@xmrig Yes, it works for me. Thank you!

## philtimmes | 2018-06-15T23:13:29+00:00
I do... philtimmes

On Fri, Jun 15, 2018, 2:05 PM Nathaniel Hayes <notifications@github.com>
wrote:

> @iranagame <https://github.com/iranagame> So you do have working arm v7
> binaries?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/446#issuecomment-397742191>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AFPVh_gBJZrIfANdg0gD7K-RIUs-TtCtks5t9CGlgaJpZM4SqlyN>
> .
>


## philtimmes | 2018-06-16T01:18:05+00:00
the only bugs I found were in the aes_ni instructions...

On Fri, Jun 15, 2018 at 5:01 PM Nathaniel Hayes <notifications@github.com>
wrote:

> Can you post a link to them? I am betting there are multiple bugs for x86
> devices
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/446#issuecomment-397770043>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AFPVh6IuHAOSyDZndUdumIOzictZQJNHks5t9ErBgaJpZM4SqlyN>
> .
>


## wyattzheng | 2018-06-30T11:19:18+00:00
@iranagame my problem is similar,i set --threads=1 ,and xmrig work well,but when --threads>1 ,it got bus error

## saeed-parsaee | 2018-07-30T18:44:34+00:00
Having the same problem. when i disable debug mode its works fine

## DJManas | 2021-06-01T09:59:22+00:00
I am sorry I dunno if I should open new ticket or can extend this one. I recently tried to install on my OPi and I get bus error. I had compiled it using the debug CFLAGS and launched through gdb and I am getting this:

```
2021-06-01 11:49:03.985]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[New Thread 0xb41ff450 (LWP 22853)]
[New Thread 0xb39fe450 (LWP 22854)]
[New Thread 0xb2fff450 (LWP 22855)]
[New Thread 0xb25ff450 (LWP 22856)]
[2021-06-01 11:49:05.660]  net      new job from xmr-eu1.nanopool.org:14444 diff 480045 algo rx/0 height 2373559

Thread 57 "xmrig" received signal SIGBUS, Bus error.
[Switching to Thread 0xb2fff450 (LWP 22855)]
0x0052eb7e in xmrig::CpuWorker<1u>::CpuWorker(unsigned int, xmrig::CpuLaunchData const&) ()
```

Questions:
- Should I switch from stable to dev branch?
- Should I build dependencies instead of installing them on Armbian level?

Thanks,
Regards,
Petr Sourek

## teacupx | 2021-06-09T17:15:57+00:00
Same error here in Odroid-XU4 (armv7-a).  @xmrig  The code has changed a lot since 2018, maybe the fix is not present for the new algos?

## swanserquack | 2021-06-10T18:44:40+00:00
Same error here, compiled on a raspberry pi 4 and run's fine until a reboot when it spits out bus error.

## philtimmes | 2021-06-14T08:57:12+00:00
Bus error simply on arm simply means the read or write was not aligned to
cache. Find the misaligned cache read or write and replace with memcpy.
That's how I fixed it 2 years ago.
export ARGSVAR="insert arguments here"
gdb --args ./xmrig $ARGSVAR


Then press r

When crash, type bt

Use the answer given to find the offending code... Since is a bus error you will need to fix the pointer assignment with memcpy.

Good luck.


Letting someone fix it for you every time teaches you nothing. Learn, and then you can fix it yourself.


On Thu, Jun 10, 2021, 2:44 PM swanserquack ***@***.***> wrote:

> Same error here, compiled on a raspberry pi 4 and run's fine until a
> reboot when it spits out bus error.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/446#issuecomment-858898818>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABJ5LB7SOSGZZDGNRTQYRULTSEB2RANCNFSM4EVKLSGQ>
> .
>


## bitmastercoin | 2022-02-09T11:32:59+00:00
RaspberryPi4 running [xmrig/xmrig](https://github.com/xmrig/xmrig.git). after building and compiling making and cmaking with hwloc disabled. i run to get the error Bus error. So heres the output from `gdb --args ./xmrig $ARGSVAR="SIGBUS" `

> [2022-02-09 11:15:45.661]  randomx  init dataset algo rx/0 (4 threads) seed 0478070098bd2c7f...
> [Thread 0xb1dbe440 (LWP 8016) exited]
> [Thread 0xb13ff440 (LWP 8015) exited]
> [Thread 0xb0bfe440 (LWP 8014) exited]
> [2022-02-09 11:15:45.662]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (195 tx)
> [2022-02-09 11:15:45.662]  randomx  failed to allocate RandomX dataset, switching to slow mode (1 ms)
> [2022-02-09 11:15:49.931]  randomx  dataset ready (4269 ms)
> [2022-02-09 11:15:49.932]  cpu      use profile  rx  (3 threads) scratchpad 2048 KB
> [New Thread 0xb1dbe440 (LWP 8017)]
> [New Thread 0xb13ff440 (LWP 8018)]
> [New Thread 0xb0bfe440 (LWP 8019)]
> --Type <RET> for more, q to quit, c to continue without paging--c
> 
> Thread 44 "xmrig" received signal SIGBUS, Bus error.
> [Switching to Thread 0xb13ff440 (LWP 8018)]
> 0x0017f75c in xmrig::CpuWorker<1u>::CpuWorker(unsigned int, xmrig::CpuLaunchData const&) ()
> (gdb) 
> 

i am getting bus error. running RPI4 with xmrig/xmrig the main git

here is some more output from further continuing to run in dbg:

> 
> (gdb) cont
> Continuing.
> [2022-02-09 11:20:34.498]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (195 tx)
> [2022-02-09 11:20:34.498]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (195 tx)
> [2022-02-09 11:20:34.498]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (195 tx)
> [2022-02-09 11:20:34.498]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (195 tx)
> [2022-02-09 11:20:34.498]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (195 tx)
> [2022-02-09 11:20:34.499]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (165 tx)
> [2022-02-09 11:20:34.499]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (165 tx)
> [2022-02-09 11:20:34.499]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (162 tx)
> [2022-02-09 11:20:34.499]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (162 tx)
> [2022-02-09 11:20:34.499]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (162 tx)
> [2022-02-09 11:20:34.499]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555683 (162 tx)
> [2022-02-09 11:20:34.499]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (155 tx)
> [2022-02-09 11:20:34.499]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (155 tx)
> [2022-02-09 11:20:34.500]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (155 tx)
> [2022-02-09 11:20:34.500]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (155 tx)
> [2022-02-09 11:20:34.500]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (155 tx)
> [2022-02-09 11:20:34.500]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (155 tx)
> [2022-02-09 11:20:34.500]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (155 tx)
> [2022-02-09 11:20:34.500]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (155 tx)
> [2022-02-09 11:20:34.500]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (164 tx)
> [2022-02-09 11:20:34.500]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (164 tx)
> [2022-02-09 11:20:34.500]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2555684 (164 tx)
> [Thread 0xb6ff8100 (LWP 7973) exited]
> 
> Thread 45 received signal SIGBUS, Bus error.
> [Switching to Thread 0xb0bfe440 (LWP 8019)]
> 0x0017f75c in xmrig::CpuWorker<1u>::CpuWorker(unsigned int, xmrig::CpuLaunchData const&) ()
> (gdb) 
> (gdb) c
> Continuing.
> /build/gdb-vC73A7/gdb-10.1/gdb/linux-nat.c:1724: internal-error: virtual void linux_nat_target::resume(ptid_t, int, gdb_signal): Assertion `signo == GDB_SIGNAL_0' failed.
> A problem internal to GDB has been detected,
> further debugging may prove unreliable.
> Quit this debugging session? (y or n) n
> 
> This is a bug, please report it.  For instructions, see:
> <https://www.gnu.org/software/gdb/bugs/>.
> 
> /build/gdb-vC73A7/gdb-10.1/gdb/linux-nat.c:1724: internal-error: virtual void linux_nat_target::resume(ptid_t, int, gdb_signal): Assertion `signo == GDB_SIGNAL_0' failed.
> A problem internal to GDB has been detected,
> further debugging may prove unreliable.
> Create a core file of GDB? (y or n) y
[config.json.txt](https://github.com/xmrig/xmrig/files/8032223/config.json.txt)

> Command aborted.
> (gdb) 
> Program terminated with signal SIGBUS, Bus error.
> The program no longer exists.
> 


attached is my config.json file in txt format.

please help as i am a noob to this.

## SChernykh | 2022-02-10T08:39:24+00:00
@bitmastercoin if you're using RPi4, you should use 64-bit OS and compiler.

# Action History
- Created by: jovan2009 | 2018-03-14T14:58:18+00:00
- Closed at: 2018-11-05T12:59:45+00:00
