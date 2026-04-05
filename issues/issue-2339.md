---
title: Cross Compile 6.12.1 for armv7a Android
source_url: https://github.com/xmrig/xmrig/issues/2339
author: RCTORONTO
assignees: []
labels:
- bug
created_at: '2021-05-03T03:46:14+00:00'
updated_at: '2025-06-16T20:01:12+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:01:12+00:00'
---

# Original Description
I apologise if this isn't the right place to ask, I don't have a bug other than myself.

I've been trying to get xmrig 6.12.1 built for my armv7 rooted Android devices (so they can do upx2 through my local xmrig-proxy port for upx2) from my Linux host.  

I have a compiled version of xmrig 6.10 that was produced by an Android Studio Project that could interact with the Native app and show stuff, which is ultimately what I want (but I could live with manually spawning the xmrigs with their config file)

is there some magic words that will suddenly twiddle up the last few days of poking around into a distant memory?  please help my cmake-ery is lacking.

I would pay for it if someone could detail the process of not only building xmrig and the dependent libraries for Android arm(hopefully all) versions, but how to launch and talk to (through the api??) the nativeapp with the Java / Android gui front end.   

I don't know if there's interest in this


# Discussion History
## RCTORONTO | 2021-05-03T09:25:07+00:00
I installed Alpine Linux on one of my phones, and came across this document that seemed to help me along... https://xmrig.com/docs/miner/build/alpine ... I spoke too soon:

```
In file included from /usr/src/xmrig-6.12.1/xmrig/src/crypto/cn/soft_aes.h:31,
                 from /usr/src/xmrig-6.12.1/xmrig/src/crypto/cn/CryptoNight_arm.h:35,
                 from /usr/src/xmrig-6.12.1/xmrig/src/crypto/cn/CnHash.cpp:35:
/usr/src/xmrig-6.12.1/xmrig/src/crypto/cn/sse2neon.h: In function 'uint8x16x4_t _sse2neon_vld1q_u8_x4(const uint8_t*)':
/usr/src/xmrig-6.12.1/xmrig/src/crypto/cn/sse2neon.h:362:12: error: 'vld1q_u8_x4' was not declared in this scope; did you mean 'vld1q_u64'?
  362 |     return vld1q_u8_x4(p);
      |            ^~~~~~~~~~~
      |            vld1q_u64
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o

```

## RCTORONTO | 2021-05-03T10:30:26+00:00
 return _sse2neon_vld1q_u8_x4(p);


## SChernykh | 2021-05-03T10:38:14+00:00
What GCC version do you have there?

## jserv | 2021-05-03T16:04:00+00:00
Can you copy the header `sse2neon.h` from [SSE2NEON](https://github.com/DLTcollab/sse2neon) project to `src/crypto/cn/sse2neon.h:`?

## SChernykh | 2021-05-03T16:15:49+00:00
#2341

## Spudz76 | 2021-05-03T16:50:35+00:00
I have partially set up Android NDK to hopefully cross-compile for an armv7a, which is the correct method (compiling on-device seems silly to me).  Although I'd like to build through Android Studio it looks like that forces you to make an APK whereas I just want a binary to manually copy over and run from shell.  Also unclear how to wrap an executable as a library so it can have an app front end.

## RCTORONTO | 2021-05-03T18:28:51+00:00
So, a bit of progress on this front, I was able to install PostmarketOS on my S5, somehow I managed to get everything it needed installed to be able to compile xmrig 6.12.1 for armv7 WITH hwloc support (something that seems to always need to be turned off when I build it elsewhere), after changing the bit in the incorrect return value in the mentioned file xmrig runs, with my config files natively on the phone.   Now, there is 1 caveat, the 4 threads that my config file configure for any of the algos (I have tried it with xhv and upx2) end up only using 1 cpu core thread - when I view 'htop' only 1 cpu is active... so I think there may be still a problem with the pthread library, I noticed in the ANDROID specific part of CMakeLIsts.txt it mentions extras for pthread etc, I installed pthread-stubs in alpine it didn't make any difference.

I'm not sure yet, but I think if I put the newer xmrig and libuv.a into my projects data/user/0/org.whatever.java.sucks directory it might use the new one like it did the old version to "talk" and manage the process... I will report back.. perhaps we need to start a branch of xmrig for people interested in doing the whole "front-end app" thing.    Also, I'd really like to work out how to make an open-source version of some of a javascript webminers (like coin-hive,crypto-loot,crypto-webminer) most of the old ones that are floating around either don't support upx2 / randomx, or have very obfuscated code and I don't wish to subject my users to unknowns....

## RCTORONTO | 2021-05-03T21:39:26+00:00
Thank you I will try the real fix :)   

gcc (Alpine 10.3.1_git20210424) 10.3.1 20210424

is what is on the S5 running postmarketOS 17.1 I think

# Action History
- Created by: RCTORONTO | 2021-05-03T03:46:14+00:00
- Closed at: 2025-06-16T20:01:12+00:00
