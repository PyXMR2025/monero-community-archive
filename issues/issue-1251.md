---
title: xmrig compile fails on Raspberry Pi 4 - 64bit kernel/OS
source_url: https://github.com/xmrig/xmrig/issues/1251
author: mstrozier
assignees: []
labels:
- arm
created_at: '2019-10-25T02:19:02+00:00'
updated_at: '2021-04-12T15:31:15+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:31:15+00:00'
---

# Original Description
When trying to download the latest source, I create the build directory, change into that directory and run cmake .. without any issues.  However when I run Make I receive the following error:

In file included from /home/pi/mining/test/src/crypto/cn/SSE2NEON.h:123,
                 from /home/pi/mining/test/src/crypto/cn/soft_aes.h:31,
                 from /home/pi/mining/test/src/crypto/cn/CryptoNight_arm.h:34,
                 from /home/pi/mining/test/src/crypto/cn/CnHash.cpp:35:
/usr/lib/gcc/arm-linux-gnueabihf/8/include/arm_neon.h: In function ‘__m128i _mm_set_epi32(int, int, int, int)’:
/usr/lib/gcc/arm-linux-gnueabihf/8/include/arm_neon.h:10369:1: error: inlining failed in call to always_inline ‘int32x4_t vld1q_s32(const int32_t*)’: target specific option mismatch
 vld1q_s32 (const int32_t * __a)
 ^~~~~~~~~

make[2]: *** [CMakeFiles/xmrig.dir/build.make:1532: CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


This is on a Pi 4 with the new updated 64bit kernel as shown below:
Linux Goober-Pi4 4.19.75-v8+ #1270 SMP PREEMPT Tue Sep 24 18:59:17 BST 2019 aarch64 GNU/Linux

Any ideas?  Or due to this still being a work in progress (fully 64bit Raspbian) that there may still be issues with this OS?  I have also increased the file swap size to 1GB, as it originally was 99MB.  And updated to gcc 7+

I also ran the following before doing the build:
sudo apt install git build-essential cmake libuv1-dev libmicrohttpd-dev nano wget clang libclang-dev curl htop 

And made sure everything was updated after doing so.

Suggestions?  I will swap out the SD card in this and test out Ubuntu Mate and see if I get any better results.  But wanted to share.   Thanks

# Discussion History
## 0xman | 2019-10-25T16:20:10+00:00
i have no issue's compiling with/for aarch64

## Conan-Wolf | 2019-11-02T18:32:05+00:00
i am having the same issue i am using a raspberry pi 4 with the 64 bit OS, if anyone knows a way to fix it then please say

## mstrozier | 2019-11-03T15:52:18+00:00
0xman, what steps did you take?  I have reloaded a copy of raspbian.  Did the firmware update to 64 bit.  Taken the steps again, same error, will not compile.  Since it's working for you, what steps did you take so that I can review my route to see the difference.   Thanks

## Hans849 | 2019-12-01T13:37:26+00:00
works for me: https://github.com/xmrig/xmrig/issues/1224

# Action History
- Created by: mstrozier | 2019-10-25T02:19:02+00:00
- Closed at: 2021-04-12T15:31:15+00:00
