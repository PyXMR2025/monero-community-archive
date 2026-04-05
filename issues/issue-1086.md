---
title: evo v2.99.3-beta breaks RaspberryPi aarch64 GCC builds
source_url: https://github.com/xmrig/xmrig/issues/1086
author: resistor4u
assignees: []
labels:
- need feedback
created_at: '2019-07-30T18:30:34+00:00'
updated_at: '2020-10-16T04:14:18+00:00'
type: issue
status: closed
closed_at: '2020-10-16T04:14:18+00:00'
---

# Original Description
I'm working from commit 962f0cdd8 on an aarch64 RPi 3b+. There are no issues with the following cmake assembly
```
cmake .. -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -DWITH_HTTP=OFF -DWITH_TLS=OFF
```
But running `make -j4` throws several segmentation faults that seem to deal mostly with json and rapidjson but are of the following kind:
```
[  4%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/JsonChain.cpp.o
during GIMPLE pass: einline
/root/xmrig/src/base/io/Console.cpp: In static member function ‘static void xmrig::Handle::deleteLater(T) [with T = uv_tty_s*]::<lambda(uv_handle_t*)>::_FUN(uv_handle_t*)’:
/root/xmrig/src/base/io/Console.cpp:80:1: internal compiler error: Segmentation fault
 }
 ^
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-8/README.Bugs> for instructions.
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:76: CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o] Error 1
```
I'm using `gcc (Debian 8.3.0-19) 8.3.0`. I also have `clang version 7.0.1-8 (tags/RELEASE_701/final)`. Both gcc and clang fail to build evo v2.99.3-beta. When I switch back to master branch and try building with gcc, I get the same sorts of errors. But using clang on the master branch builds and runs fine.

Are these errors with gcc version 8.3.0-19 or with xmrig?

# Discussion History
## Spudz76 | 2019-07-30T22:27:29+00:00
1GB of ram means probably no `-j` beyond `1` due to compiler needing more memory.  The most common cause of Segmentation fault during compile is running out of memory (none of them say they ran out they just blindly allocate more and catch the segmentation fault trying to use the null pointer from mmap).
Less than 3GB also means no RandomX (you did not disable)
Wouldn't pico and/or lite be some of the better performers on such a CPU (I see you disabled them)

I have been using clang-9 on x86-64 and it works great.  Haven't tried clang-7 in a while, but clang-3.5.0 definitely broken.  gcc-9 and gcc-7 and gcc-6 and gcc-5 all work on x86-64 as well, but anything less than 5 seems broken now.  4.9.3 used to compile a few steps ago before the redesigned RandomX, as did the old clang.

I have not tried either gcc-8 nor clang-7 ironically.

## Spudz76 | 2019-07-31T01:47:58+00:00
gcc-8 of version `gcc version 8.3.0 (Ubuntu 8.3.0-6ubuntu1~18.04.1)` worked fine for build on x86-64

So it's not a gcc-8 thing...

## Spudz76 | 2019-07-31T02:00:19+00:00
clang-7 of version `7.1.0-svn353565-1~exp1~20190406090509.61 (branches/release_70)` also worked fine on x86-64

unless a slot problem with 7.0.1 then I'd call clang-7 series ok in general

## resistor4u | 2019-08-01T00:28:40+00:00
Even after switching off randomx simply running `make` with gcc-8 I get:
```
[  1%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
during GIMPLE pass: einline
/root/xmrig/src/backend/cpu/CpuLaunchData.cpp: In member function ‘bool xmrig::Assembly::operator==(const xmrig::Assembly&) const’:
/root/xmrig/src/backend/cpu/CpuLaunchData.cpp:64:1: internal compiler error: Segmentation fault
 }
 ^
Please submit a full bug report,
with preprocessed source if appropriate.
See <file:///usr/share/doc/gcc-8/README.Bugs> for instructions.
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:63: CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```
You mentioned building for x86-64 fine, but have you tried for `aarch64` or `arm64`?

## xmrig | 2019-08-01T01:52:46+00:00
Try create swap file.
Thank you.

## Spudz76 | 2019-08-02T19:16:11+00:00
Really feels like lack of memory.  Build on a real computer with cross-tools?

## resistor4u | 2019-08-05T20:51:47+00:00
@xmrig @Spudz76 I pulled changes from 66d8598f9f6. I created a swapfile with `dphys-swapfile` and started the service with the default size of 356Mi. Using the same build settings from above, gcc 8.3.0-19 fails with the same seg faults. `make` fails almost immediately, but `make -j4` goes a bit farther before failing.

I tried to monitor the memory and swap usages during building, and it seems the build process never used more than 617Mi of the total 917Mi of physical memory available, and only 5.0Mi of swap was used before the build failed.

However, when I switch to gcc-9 and g++-9 using the same build settings, the build succeeds. I'm seeing minuscule performance increase of 0.1-0.2 H/s.

### Update:
After 1.5 hours of mining I see that none of my shares are accepted, but none are rejected either. The device is consistently mining at 3.2 H/s (about 0.8 H/s per thread). The pool keeps assigning new jobs to the device, but on the pool's side it does not show the miner is logged in or mining. Also, the difficulty of new jobs is shown as `1000225` whereas it used to show as `1063`. (The pool auto-adjusts diff.) @xmrig did I miss something in the changes regarding how the diff is reported?

In the past, this would happen until the first share is accepted and the pool then shows the miner as logged in, etc. And in previous builds, my 3.1 H/s RPi shares were accepted usually within the first five minutes, but now there are zero accepted results after 1.5 hours. Ideas about what's happening?

## xmrig | 2019-08-06T05:04:49+00:00
Looks like you don't change pool settings, donate.v2.xmrig.com use this diff.
Thank you.

## resistor4u | 2019-08-07T10:36:23+00:00
@xmrig I'm sorry, but I'm confused. I am not using the example config.json (or any config file) - I am setting everything from the command line. Where are the pool settings?

## xmrig | 2019-08-07T10:46:40+00:00
Remove `config.json` if miner can't get valid configuration it fallback to config.json, however I recommended use config file, it more human friendly and flexible.

Try use https://config.xmrig.com/ it outdated but helps with command line (you will need replace `variant` to `algo`), if you still get issues, please show you command line (wallet address can be truncated).
Thank you. 

## resistor4u | 2019-08-07T11:30:52+00:00
I don't use config files at all, and I only set settings from the command line. `xmrig-notls -o xmr.pool.minergate.com:45700 -u somebum -p x` and I get
```
 * ABOUT        XMRig/2.99.5-evo clang/10.0.0
 * LIBS         libuv/2.0.0-dev
 * CPU          ARMv8 (1) x64 AES -AVX2
                threads:2
 * DONATE       2%
 * POOL #1      xmr.pool.minergate.com:45700 algo cn/2
 * COMMANDS     hashrate, pause, resume
[2019-08-07 04:24:27.251] use pool xmr.pool.minergate.com:45700  46.4.119.208
[2019-08-07 04:24:27.253] new job from xmr.pool.minergate.com:45700 diff 1000225 algo cn/r height 1895558
[2019-08-07 04:24:27.253]  cpu  use profile  cn  (2 threads) scratchpad 2048 KB
[2019-08-07 04:24:38.316]  cpu  READY threads 2(2) huge pages 0/2 0% memory 4096 KB (11062 ms)
[2019-08-07 04:25:34.832] speed 10s/60s/15m 4.4 n/a n/a H/s max 4.5 H/s
```
I notice it says at pool #1 the algo is cn/2 but the console notes it is cn/r. I cannot get the miner to change algos by the `--algo` option added to the simple run command above. The miner continues like this for 1.5 hours with no accepted shares and no change in diff. The pool doesn't show me as mining.

Note** the above output is from an iphone, but it is the exact same as the RPi. I am testing the binary on an iphone now because I'm away from the RPi.

## xmrig | 2019-08-07T11:39:38+00:00
Looks like minergate added some filters, if add `--user-agent XMRig/2.14.0` to command line diff return to normal.

## xmrig | 2019-08-07T11:46:46+00:00
Also this pool now use algorithm negotiation, so it means don't need specify algo option at all, pool override it anyway.
Thank you.

## resistor4u | 2019-08-07T19:01:29+00:00
> Looks like minergate added some filters, if add `--user-agent XMRig/2.14.0` to command line diff return to normal.

will test in about 1.5 hours. Without the useragent of the older release, what do you think the pool was effectively treating the miner as?

## resistor4u | 2019-08-08T10:12:39+00:00
Setting the useragent fixed the diff issue for both aarch64 device types - thanks. However, I still cannot get a successful build on the RPi using gcc-8 :-\

## Spudz76 | 2019-08-10T18:19:57+00:00
No I do not have any non-AMD64 units to test on.  Was sharing the fact that gcc-8 works fine on 4GB ram with a "standard" cpu so it's not gcc-8 itself that doesn't work.  I have had it fail where I didn't have several GB free memory (not sure if swap makes any difference).

If the unroll expands into more than your system memory it can't swap it anyway.  Mining kernels use extensive unrolling of loops into long-form during compilation which explodes memory.  Betting gcc-9 uses some method of dealing with lack of physical memory during unroll explosion and optimization.

Every time I hit the compiler-segfault it was lack of physical memory for whatever complicated unroll or template expansions.

I have done lots of work with OpenWRT so I am familiar with limited platforms (routers have so little memory you didn't even have compilers on the device, everything was cross-compile from a "real" computer with "real" amounts of ram)

# Action History
- Created by: resistor4u | 2019-07-30T18:30:34+00:00
- Closed at: 2020-10-16T04:14:18+00:00
