---
title: XMRig fails to run when using --no-cpu
source_url: https://github.com/xmrig/xmrig/issues/3178
author: ghost
assignees: []
labels:
- question
created_at: '2022-12-13T04:46:39+00:00'
updated_at: '2022-12-18T14:04:47+00:00'
type: issue
status: closed
closed_at: '2022-12-18T14:04:46+00:00'
---

# Original Description
```
./xmrig --opencl -o xmrpool.eu:9999 -u 4Ax4xrtEBb386TN9zxYAGVSMjc6zzs4Xqf6B3pNvSYz8U6cA7LCyBxHGsuXbyK7xFmA2a1N8jQAL3aGBzBCE2GgXHB8tRko --algo='rx/0' -k --tls
```
This works but I am not sure if it mines by GPU.
```
./xmrig --no-cpu --opencl -o xmrpool.eu:9999 -u 4Ax4xrtEBb386TN9zxYAGVSMjc6zzs4Xqf6B3pNvSYz8U6cA7LCyBxHGsuXbyK7xFmA2a1N8jQAL3aGBzBCE2GgXHB8tRko --algo='rx/0' -k --tls
```
This gives this error
```
[2022-12-13 10:31:17.098]  net      xmrpool.eu:9999 incompatible/disabled algorithm "rx/0" detected, reconnect
[2022-12-13 10:31:17.098]  net      xmrpool.eu:9999 login error code: 6
```

# Discussion History
## ghost | 2022-12-13T04:49:06+00:00
```
Also there's this weird ./xmrig: unrecognized option: opencl
```

## ghost | 2022-12-13T04:50:24+00:00
```
./xmrig: unrecognized option: opencl
 * ABOUT        XMRig/6.18.1 gcc/9.3.0
 * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Athlon Silver 3050U with Radeon Graphics (1) 64-bit AES
                L2:1.0 MB L3:4.0 MB 2C/2T NUMA:1
 * MEMORY       4.7/5.7 GB (82%)
                Bottom - Slot 1 (left): <empty>
                Bottom - Slot 2 (right): 8 GB DDR4 @ 2400 MHz M471A1K43EB1-CWE    
 * MOTHERBOARD  HP - 8706
 * DONATE       2%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmrpool.eu:9999 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
```

## Sstealther0101 | 2022-12-13T04:52:13+00:00
Hello good morning I did upload one code that found on net and recreate it
and just uploaded I did apologize I'm not expert it's my literary first day
sundries with people living to seel from social media. I'm sorry if I did
anything wrong but how could I help

On Tue, 13 Dec 2022, 06:46 Neo Machine, ***@***.***> wrote:

> ./xmrig --opencl -o xmrpool.eu:9999 -u 4Ax4xrtEBb386TN9zxYAGVSMjc6zzs4Xqf6B3pNvSYz8U6cA7LCyBxHGsuXbyK7xFmA2a1N8jQAL3aGBzBCE2GgXHB8tRko --algo='rx/0' -k --tls
>
> This works but I am not sure if it mines by GPU.
>
> ./xmrig --no-cpu --opencl -o xmrpool.eu:9999 -u 4Ax4xrtEBb386TN9zxYAGVSMjc6zzs4Xqf6B3pNvSYz8U6cA7LCyBxHGsuXbyK7xFmA2a1N8jQAL3aGBzBCE2GgXHB8tRko --algo='rx/0' -k --tls
>
> This gives this error
>
> [2022-12-13 10:31:17.098]  net      xmrpool.eu:9999 incompatible/disabled algorithm "rx/0" detected, reconnect
> [2022-12-13 10:31:17.098]  net      xmrpool.eu:9999 login error code: 6
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3178>, or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A4WBK442NV75MVAUERT6DTLWM75TVANCNFSM6AAAAAAS4XV5LY>
> .
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


## Sstealther0101 | 2022-12-13T04:54:05+00:00
What's this all this emails all about can you specify?

On Tue, 13 Dec 2022, 06:50 Neo Machine, ***@***.***> wrote:

> ./xmrig: unrecognized option: opencl
>  * ABOUT        XMRig/6.18.1 gcc/9.3.0
>  * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
>  * HUGE PAGES   supported
>  * 1GB PAGES    disabled
>  * CPU          AMD Athlon Silver 3050U with Radeon Graphics (1) 64-bit AES
>                 L2:1.0 MB L3:4.0 MB 2C/2T NUMA:1
>  * MEMORY       4.7/5.7 GB (82%)
>                 Bottom - Slot 1 (left): <empty>
>                 Bottom - Slot 2 (right): 8 GB DDR4 @ 2400 MHz M471A1K43EB1-CWE
>  * MOTHERBOARD  HP - 8706
>  * DONATE       2%
>  * ASSEMBLY     auto:ryzen
>  * POOL #1      xmrpool.eu:9999 algo rx/0
>  * COMMANDS     hashrate, pause, resume, results, connection
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3178#issuecomment-1347744613>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A4WBK47YTM7KOZZYJRSQZCLWM76BXANCNFSM6AAAAAAS4XV5LY>
> .
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


## Sstealther0101 | 2022-12-13T04:55:05+00:00
It's first day in GitHub and  don't got a nap from social media because of
this condition now what I can resolve

On Tue, 13 Dec 2022, 06:53 Stealther93 Stealther1993, ***@***.***>
wrote:

> What's this all this emails all about can you specify?
>
> On Tue, 13 Dec 2022, 06:50 Neo Machine, ***@***.***> wrote:
>
>> ./xmrig: unrecognized option: opencl
>>  * ABOUT        XMRig/6.18.1 gcc/9.3.0
>>  * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
>>  * HUGE PAGES   supported
>>  * 1GB PAGES    disabled
>>  * CPU          AMD Athlon Silver 3050U with Radeon Graphics (1) 64-bit AES
>>                 L2:1.0 MB L3:4.0 MB 2C/2T NUMA:1
>>  * MEMORY       4.7/5.7 GB (82%)
>>                 Bottom - Slot 1 (left): <empty>
>>                 Bottom - Slot 2 (right): 8 GB DDR4 @ 2400 MHz M471A1K43EB1-CWE
>>  * MOTHERBOARD  HP - 8706
>>  * DONATE       2%
>>  * ASSEMBLY     auto:ryzen
>>  * POOL #1      xmrpool.eu:9999 algo rx/0
>>  * COMMANDS     hashrate, pause, resume, results, connection
>>
>> —
>> Reply to this email directly, view it on GitHub
>> <https://github.com/xmrig/xmrig/issues/3178#issuecomment-1347744613>, or
>> unsubscribe
>> <https://github.com/notifications/unsubscribe-auth/A4WBK47YTM7KOZZYJRSQZCLWM76BXANCNFSM6AAAAAAS4XV5LY>
>> .
>> You are receiving this because you are subscribed to this thread.Message
>> ID: ***@***.***>
>>
>


## SChernykh | 2022-12-13T08:54:11+00:00
@neomachiney 
You use invalid wallet address (checksum test fails). Double check it. When I change this wallet address to my own, everything works fine and xmrig mines RandomX on my GPU.

## Sstealther0101 | 2022-12-13T16:05:10+00:00
Where should I. Input the address then??(\¢

On Tue, 13 Dec 2022, 10:54 SChernykh, ***@***.***> wrote:

> @neomachiney <https://github.com/neomachiney>
> You use invalid wallet address (checksum test fails). Double check it.
> When I change this wallet address to my own, everything works fine and
> xmrig mines RandomX on my GPU.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3178#issuecomment-1347950610>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A4WBK45NZOZAIEYAVYSJX2TWNA2T7ANCNFSM6AAAAAAS4XV5LY>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


## Sstealther0101 | 2022-12-14T07:56:53+00:00
h2y bro look at logs of mining all corrrrect changed yesterday formula to
my my RandmomXMyGPU etc and with simple mode combini£ but didn't get any
mining farm all though was appeareaing
Wed Dec 14 2022 00:09:13 GMT+0200  * ABOUT        XMRig/6.17.0 clang/9.0.9
Wed Dec 14 2022 00:09:14 GMT+0200  * LIBS         libuv/1.43.0
OpenSSL/1.1.1m hwloc/2.7.2rc1-git
Wed Dec 14 2022 00:09:14 GMT+0200  * HUGE PAGES   supported
Wed Dec 14 2022 00:09:14 GMT+0200  * 1GB PAGES    unavailable
Wed Dec 14 2022 00:09:14 GMT+0200  * CPU          ARM Cortex-A55 (2) 64-bit
AES
Wed Dec 14 2022 00:09:15 GMT+0200                 L2:0.0 MB L3:0.0 MB 8C/8T
NUMA:1
Wed Dec 14 2022 00:09:15 GMT+0200  * MEMORY       2.7/5.6 GB (49%)
Wed Dec 14 2022 00:09:15 GMT+0200  * DONATE       4%
Wed Dec 14 2022 00:09:15 GMT+0200  * POOL #1      pool.minexmr.com:4444
algo auto
Wed Dec 14 2022 00:09:15 GMT+0200  * COMMANDS     hashrate, pause, resume,
results, connection
Wed Dec 14 2022 00:09:16 GMT+0200  * HTTP API     127.0.0.1:50080
Wed Dec 14 2022 00:09:16 GMT+0200  config   configuration saved to:
"/data/user/0/com.xmrigforandroid/files/config.json"
Wed Dec 14 2022 00:09:16 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:09:18 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:09:26 GMT+0200  * ABOUT        XMRig/6.17.0 clang/9.0.9
Wed Dec 14 2022 00:09:26 GMT+0200  * LIBS         libuv/1.43.0
OpenSSL/1.1.1m hwloc/2.7.2rc1-git
Wed Dec 14 2022 00:09:27 GMT+0200  * HUGE PAGES   supported
Wed Dec 14 2022 00:09:27 GMT+0200  * 1GB PAGES    unavailable
Wed Dec 14 2022 00:09:27 GMT+0200  * CPU          ARM Cortex-A55 (2) 64-bit
AES
Wed Dec 14 2022 00:09:27 GMT+0200                 L2:0.0 MB L3:0.0 MB 8C/8T
NUMA:1
Wed Dec 14 2022 00:09:28 GMT+0200  * MEMORY       2.7/5.6 GB (49%)
Wed Dec 14 2022 00:09:28 GMT+0200  * DONATE       4%
Wed Dec 14 2022 00:09:28 GMT+0200  * POOL #1      pool.minexmr.com:4444
algo auto
Wed Dec 14 2022 00:09:28 GMT+0200  * COMMANDS     hashrate, pause, resume,
results, connection
Wed Dec 14 2022 00:09:29 GMT+0200  * HTTP API     127.0.0.1:50080
Wed Dec 14 2022 00:09:29 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:09:32 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:09:38 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:09:43 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:09:49 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:10:18 GMT+0200  * ABOUT        XMRig/6.17.0 clang/9.0.9
Wed Dec 14 2022 00:10:19 GMT+0200  * LIBS         libuv/1.43.0
OpenSSL/1.1.1m hwloc/2.7.2rc1-git
Wed Dec 14 2022 00:10:19 GMT+0200  * HUGE PAGES   supported
Wed Dec 14 2022 00:10:19 GMT+0200  * 1GB PAGES    unavailable
Wed Dec 14 2022 00:10:20 GMT+0200  * CPU          ARM Cortex-A55 (2) 64-bit
AES
Wed Dec 14 2022 00:10:20 GMT+0200                 L2:0.0 MB L3:0.0 MB 8C/8T
NUMA:1
Wed Dec 14 2022 00:10:20 GMT+0200  * MEMORY       2.7/5.6 GB (49%)
Wed Dec 14 2022 00:10:21 GMT+0200  * DONATE       4%
Wed Dec 14 2022 00:10:21 GMT+0200  * POOL #1      pool.minexmr.com:4444
algo auto
Wed Dec 14 2022 00:10:21 GMT+0200  * COMMANDS     hashrate, pause, resume,
results, connection
Wed Dec 14 2022 00:10:21 GMT+0200  * HTTP API     127.0.0.1:50080
Wed Dec 14 2022 00:10:22 GMT+0200  config   configuration saved to:
"/data/user/0/com.xmrigforandroid/files/config.json"
Wed Dec 14 2022 00:10:22 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:10:23 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:10:28 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:10:33 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:10:38 GMT+0200  net      pool.minexmr.com:4444 DNS
error: "no address"
Wed Dec 14 2022 00:10:46 GMT+0200  * ABOUT        XMRig/6.17.0 clang/9.0.9
Wed Dec 14 2022 00:10:47 GMT+0200  * LIBS         libuv/1.43.0
OpenSSL/1.1.1m hwloc/2.7.2rc1-git
Wed Dec 14 2022 00:10:48 GMT+0200  * HUGE PAGES   supported
Wed Dec 14 2022 00:10:48 GMT+0200  * 1GB PAGES    unavailable
Wed Dec 14 2022 00:10:48 GMT+0200  * CPU          ARM Cortex-A55 (2) 64-bit
AES
Wed Dec 14 2022 00:10:49 GMT+0200                 L2:0.0 MB L3:0.0 MB 8C/8T
NUMA:1
Wed Dec 14 2022 00:10:50 GMT+0200  * MEMORY       2.6/5.6 GB (47%)
Wed Dec 14 2022 00:10:51 GMT+0200  * DONATE       4%
Wed Dec 14 2022 00:10:52 GMT+0200  * POOL #1      pool.hashvault.pro:80
algo auto
Wed Dec 14 2022 00:10:52 GMT+0200  * COMMANDS     hashrate, pause, resume,
results, connection
Wed Dec 14 2022 00:10:53 GMT+0200  * HTTP API     127.0.0.1:50080
Wed Dec 14 2022 00:10:54 GMT+0200  config   configuration saved to:
"/data/user/0/com.xmrigforandroid/files/config.json"
Wed Dec 14 2022 00:10:55 GMT+0200  net      use pool pool.hashvault.pro:80
TLSv1.3 37.203.243.102
Wed Dec 14 2022 00:10:56 GMT+0200  net      fingerprint (SHA-256):
"420c7850e09b7c0bdcf748a7da9eb3647daf8515718f36d9ccfdd6b9ff834b14"
Wed Dec 14 2022 00:10:56 GMT+0200  net      new job from
pool.hashvault.pro:80 diff 36000 algo rx/0 height 2776699 (105 tx)
Wed Dec 14 2022 00:10:57 GMT+0200  cpu      use argon2 implementation
default
Wed Dec 14 2022 00:10:58 GMT+0200  randomx  init dataset algo rx/0 (8
threads) seed 57b68fb274733d17...
Wed Dec 14 2022 00:10:59 GMT+0200  randomx  allocated 2336 MB (2080+256)
huge pages 0% 0/1168 +JIT (0 ms)
Wed Dec 14 2022 00:11:00 GMT+0200  net      new job from
pool.hashvault.pro:80 diff 36000 algo rx/0 height 2776700 (18 tx)
Wed Dec 14 2022 00:11:02 GMT+0200  net      new job from
pool.hashvault.pro:80 diff 50233 algo rx/0 height 2776700 (18 tx)
Wed Dec 14 2022 00:11:07 GMT+0200  randomx  dataset ready (20799 ms)
Wed Dec 14 2022 00:11:08 GMT+0200  cpu      use profile  rx  (8 threads)
scratchpad 2048 KB
Wed Dec 14 2022 00:11:09 GMT+0200  cpu      READY threads 8/8 (8) huge
pages 0% 0/8 memory 16384 KB (13 ms)
Wed Dec 14 2022 00:11:19 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s
Wed Dec 14 2022 00:11:24 GMT+0200  cpu      accepted (1/0) diff 50233 (145
ms)
Wed Dec 14 2022 00:11:28 GMT+0200  miner    speed 10s/60s/15m 200.6 n/a n/a
H/s max 292.6 H/s
Wed Dec 14 2022 00:12:15 GMT+0200  * ABOUT        XMRig/6.16.5-mo1
clang/9.0.9
Wed Dec 14 2022 00:12:18 GMT+0200  * LIBS         libuv/1.43.0
OpenSSL/1.1.1m hwloc/2.7.2rc1-git
Wed Dec 14 2022 00:12:20 GMT+0200  * HUGE PAGES   supported
Wed Dec 14 2022 00:12:23 GMT+0200  * 1GB PAGES    unavailable
Wed Dec 14 2022 00:12:25 GMT+0200  * CPU          ARM Cortex-A55 (2) 64-bit
AES
Wed Dec 14 2022 00:12:27 GMT+0200                 L2:0.0 MB L3:0.0 MB 8C/8T
NUMA:1
Wed Dec 14 2022 00:12:30 GMT+0200  * MEMORY       2.5/5.6 GB (46%)
Wed Dec 14 2022 00:12:32 GMT+0200  * DONATE       4%
Wed Dec 14 2022 00:12:35 GMT+0200  * POOL #1      xmr.hashcity.org:4444
algo auto
Wed Dec 14 2022 00:12:38 GMT+0200  * COMMANDS     hashrate, pause, resume,
results, connection
Wed Dec 14 2022 00:12:40 GMT+0200  config   configuration saved to:
"/data/user/0/com.xmrigforandroid/files/config.json"
Wed Dec 14 2022 00:12:40 GMT+0200  benchmk   STARTING ALGO PERFORMANCE
CALIBRATION (with 20 seconds round)
Wed Dec 14 2022 00:12:41 GMT+0200  benchmk   Algo ghostrider Preparation
Wed Dec 14 2022 00:12:42 GMT+0200  cpu      use profile  ghostrider  (8
threads) scratchpad 2048 KB
Wed Dec 14 2022 00:12:43 GMT+0200  cpu      GhostRider algo 1: cn/dark (512
KB)
Wed Dec 14 2022 00:12:44 GMT+0200  cpu      GhostRider algo 2: cn/fast (2
MB)
Wed Dec 14 2022 00:12:44 GMT+0200  cpu      GhostRider algo 3: cn/turtle
(256 KB)
Wed Dec 14 2022 00:12:45 GMT+0200  cpu      READY threads 8/8 (64) huge
pages 0% 0/64 memory 131072 KB (2228 ms)
Wed Dec 14 2022 00:12:46 GMT+0200  benchmk   Algo ghostrider Starting test
Wed Dec 14 2022 00:12:47 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s avg 52.99 H/s
Wed Dec 14 2022 00:12:48 GMT+0200  miner    speed 10s/60s/15m 65.63 n/a n/a
H/s max 65.63 H/s avg 59.02 H/s
Wed Dec 14 2022 00:12:48 GMT+0200  miner    speed 10s/60s/15m 64.80 n/a n/a
H/s max 67.32 H/s avg 60.69 H/s
Wed Dec 14 2022 00:12:49 GMT+0200  benchmk   Algo ghostrider hashrate:
65.594450
Wed Dec 14 2022 00:12:50 GMT+0200  benchmk   Algo cn/r Preparation
Wed Dec 14 2022 00:12:51 GMT+0200  cpu      stopped (856 ms)
Wed Dec 14 2022 00:12:52 GMT+0200  cpu      use profile  cn/2  (8 threads)
scratchpad 2048 KB
Wed Dec 14 2022 00:12:53 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s
Wed Dec 14 2022 00:12:54 GMT+0200  benchmk   Algo cn/r Starting test
Wed Dec 14 2022 00:12:56 GMT+0200  cpu      READY threads 8/8 (8) huge
pages 0% 0/8 memory 16384 KB (10290 ms)
Wed Dec 14 2022 00:12:59 GMT+0200  miner    speed 10s/60s/15m 14.41 n/a n/a
H/s max 14.41 H/s
Wed Dec 14 2022 00:13:07 GMT+0200  miner    speed 10s/60s/15m 16.83 n/a n/a
H/s max 17.10 H/s
Wed Dec 14 2022 00:13:09 GMT+0200  benchmk   Algo cn/r hashrate: 16.621081
Wed Dec 14 2022 00:13:13 GMT+0200  benchmk   Algo cn-lite/1 Preparation
Wed Dec 14 2022 00:13:17 GMT+0200  cpu      stopped (545 ms)
Wed Dec 14 2022 00:13:21 GMT+0200  cpu      use profile  cn-lite  (8
threads) scratchpad 1024 KB
Wed Dec 14 2022 00:13:25 GMT+0200  benchmk   Algo cn-lite/1 Starting test
Wed Dec 14 2022 00:13:29 GMT+0200  cpu      READY threads 8/8 (8) huge
pages 0% 0/8 memory 8192 KB (304 ms)
Wed Dec 14 2022 00:13:33 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s
Wed Dec 14 2022 00:13:37 GMT+0200  miner    speed 10s/60s/15m 80.90 n/a n/a
H/s max 81.46 H/s
Wed Dec 14 2022 00:13:41 GMT+0200  benchmk   Algo cn-lite/1 hashrate:
81.359857
Wed Dec 14 2022 00:13:45 GMT+0200  benchmk   Algo cn-heavy/xhv Preparation
Wed Dec 14 2022 00:13:49 GMT+0200  cpu      stopped (76 ms)
Wed Dec 14 2022 00:13:52 GMT+0200  cpu      use profile  cn-heavy  (8
threads) scratchpad 4096 KB
Wed Dec 14 2022 00:13:56 GMT+0200  cpu      READY threads 8/8 (8) huge
pages 0% 0/16 memory 32768 KB (882 ms)
Wed Dec 14 2022 00:13:59 GMT+0200  benchmk   Algo cn-heavy/xhv Starting
test
Wed Dec 14 2022 00:14:03 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s
Wed Dec 14 2022 00:14:06 GMT+0200  miner    speed 10s/60s/15m 46.62 n/a n/a
H/s max 46.72 H/s
Wed Dec 14 2022 00:14:10 GMT+0200  benchmk   Algo cn-heavy/xhv hashrate:
45.229831
Wed Dec 14 2022 00:14:13 GMT+0200  benchmk   Algo cn-pico Preparation
Wed Dec 14 2022 00:14:17 GMT+0200  cpu      stopped (142 ms)
Wed Dec 14 2022 00:14:21 GMT+0200  cpu      use profile  cn-pico  (8
threads) scratchpad 256 KB
Wed Dec 14 2022 00:14:25 GMT+0200  benchmk   Algo cn-pico Starting test
Wed Dec 14 2022 00:14:28 GMT+0200  cpu      READY threads 8/8 (8) huge
pages 0% 0/8 memory 2048 KB (48 ms)
Wed Dec 14 2022 00:14:33 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s
Wed Dec 14 2022 00:14:38 GMT+0200  miner    speed 10s/60s/15m 1626.8 n/a
n/a H/s max 1662.7 H/s
Wed Dec 14 2022 00:14:42 GMT+0200  benchmk   Algo cn-pico hashrate:
1503.367712
Wed Dec 14 2022 00:14:46 GMT+0200  benchmk   Algo cn/ccx Preparation
Wed Dec 14 2022 00:14:52 GMT+0200  cpu      stopped (6 ms)
Wed Dec 14 2022 00:14:58 GMT+0200  cpu      use profile  cn  (8 threads)
scratchpad 2048 KB
Wed Dec 14 2022 00:15:01 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s
Wed Dec 14 2022 00:15:07 GMT+0200  benchmk   Algo cn/ccx Starting test
Wed Dec 14 2022 00:15:13 GMT+0200  cpu      READY threads 8/8 (8) huge
pages 0% 0/8 memory 16384 KB (9254 ms)
Wed Dec 14 2022 00:15:18 GMT+0200  miner    speed 10s/60s/15m 67.97 n/a n/a
H/s max 67.97 H/s
Wed Dec 14 2022 00:15:24 GMT+0200  miner    speed 10s/60s/15m 64.93 n/a n/a
H/s max 77.47 H/s
Wed Dec 14 2022 00:15:28 GMT+0200  benchmk   Algo cn/ccx hashrate:
64.933698
Wed Dec 14 2022 00:15:33 GMT+0200  benchmk   Algo cn/gpu Preparation
Wed Dec 14 2022 00:15:38 GMT+0200  benchmk   Algo cn/gpu Starting test
Wed Dec 14 2022 00:15:42 GMT+0200  miner    speed 10s/60s/15m 11.04 n/a n/a
H/s max 63.87 H/s
Wed Dec 14 2022 00:15:43 GMT+0200  miner    speed 10s/60s/15m 6.52 n/a n/a
H/s max 63.87 H/s
Wed Dec 14 2022 00:15:43 GMT+0200  benchmk   Algo cn/gpu hashrate: 6.627393
Wed Dec 14 2022 00:15:46 GMT+0200  benchmk   Algo argon2/chukwav2
Preparation
Wed Dec 14 2022 00:15:48 GMT+0200  cpu      use argon2 implementation
default
Wed Dec 14 2022 00:15:50 GMT+0200  cpu      stopped (940 ms)
Wed Dec 14 2022 00:15:52 GMT+0200  cpu      use profile  argon2  (8
threads) scratchpad 1024 KB
Wed Dec 14 2022 00:15:55 GMT+0200  benchmk   Algo argon2/chukwav2 Starting
test
Wed Dec 14 2022 00:15:58 GMT+0200  cpu      READY threads 8/8 (8) huge
pages 0% 0/8 memory 8192 KB (114 ms)
Wed Dec 14 2022 00:16:02 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s
Wed Dec 14 2022 00:16:06 GMT+0200  miner    speed 10s/60s/15m 362.4 n/a n/a
H/s max 362.4 H/s
Wed Dec 14 2022 00:16:09 GMT+0200  benchmk   Algo argon2/chukwav2 hashrate:
367.435007
Wed Dec 14 2022 00:16:12 GMT+0200  benchmk   Algo astrobwt/v2 Preparation
Wed Dec 14 2022 00:16:15 GMT+0200  cpu      stopped (15 ms)
Wed Dec 14 2022 00:16:21 GMT+0200  cpu      use profile  astrobwt/v2  (8
threads) scratchpad 128 KB
Wed Dec 14 2022 00:16:27 GMT+0200  benchmk   Algo astrobwt/v2 Starting test
Wed Dec 14 2022 00:16:34 GMT+0200  cpu      READY threads 8/8 (8) huge
pages 0% 0/8 memory 1024 KB (8 ms)
Wed Dec 14 2022 00:16:37 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s
Wed Dec 14 2022 00:16:40 GMT+0200  miner    speed 10s/60s/15m 12807.0 n/a
n/a H/s max 12807.0 H/s
Wed Dec 14 2022 00:16:42 GMT+0200  benchmk   Algo astrobwt/v2 hashrate:
15065.677297
Wed Dec 14 2022 00:16:43 GMT+0200  benchmk   Algo rx/0 Preparation
Wed Dec 14 2022 00:16:45 GMT+0200  cpu      stopped (1 ms)
Wed Dec 14 2022 00:16:47 GMT+0200  randomx  init dataset algo rx/0 (8
threads) seed 0000000000000000...
Wed Dec 14 2022 00:16:50 GMT+0200  randomx  allocated 2336 MB (2080+256)
huge pages 0% 0/1168 +JIT (0 ms)
Wed Dec 14 2022 00:16:53 GMT+0200  randomx  dataset ready (33378 ms)
Wed Dec 14 2022 00:16:55 GMT+0200  cpu      use profile  rx  (8 threads)
scratchpad 2048 KB
Wed Dec 14 2022 00:16:58 GMT+0200  cpu      READY threads 8/8 (8) huge
pages 0% 0/8 memory 16384 KB (5 ms)
Wed Dec 14 2022 00:17:00 GMT+0200  benchmk   Algo rx/0 Starting test
Wed Dec 14 2022 00:17:03 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s
Wed Dec 14 2022 00:17:10 GMT+0200  miner    speed 10s/60s/15m 245.6 n/a n/a
H/s max 245.6 H/s
Wed Dec 14 2022 00:17:18 GMT+0200  benchmk   Algo rx/0 hashrate: 243.030101
Wed Dec 14 2022 00:17:22 GMT+0200  benchmk   Algo rx/graft Preparation
Wed Dec 14 2022 00:17:24 GMT+0200  cpu      stopped (19 ms)
Wed Dec 14 2022 00:17:27 GMT+0200  randomx  init dataset algo rx/graft (8
threads) seed 0000000000000000...
Wed Dec 14 2022 00:17:36 GMT+0200  randomx  dataset ready (25363 ms)
Wed Dec 14 2022 00:17:38 GMT+0200  cpu      use profile  rx  (8 threads)
scratchpad 2048 KB
Wed Dec 14 2022 00:17:41 GMT+0200  cpu      READY threads 8/8 (8) huge
pages 0% 0/8 memory 16384 KB (15 ms)
Wed Dec 14 2022 00:17:44 GMT+0200  benchmk   Algo rx/graft Starting test
Wed Dec 14 2022 00:17:46 GMT+0200  miner    speed 10s/60s/15m n/a n/a n/a
H/s max n/a H/s
Wed Dec 14 2022 00:17:51 GMT+0200  miner    speed 10s/60s/15m 226.8 n/a n/a
H/s max 226.8 H/s
Wed Dec 14 2022 00:17:59 GMT+0200  benchmk   Algo rx/graft hashrate:
220.187349
Wed Dec 14 2022 00:18:05 GMT+0200  benchmk   Algo rx/arq Preparation
Wed Dec 14 2022 00:18:11 GMT+0200  cpu      stopped (35 ms)
Wed Dec 14 2022 00:18:17 GMT+0200  randomx  init dataset algo rx/arq (8
threads) seed 0000000000000000...

On Tue, 13 Dec 2022, 18:04 Stealther93 Stealther1993, ***@***.***>
wrote:

> Where should I. Input the address then??(\¢
>
> On Tue, 13 Dec 2022, 10:54 SChernykh, ***@***.***> wrote:
>
>> @neomachiney <https://github.com/neomachiney>
>> You use invalid wallet address (checksum test fails). Double check it.
>> When I change this wallet address to my own, everything works fine and
>> xmrig mines RandomX on my GPU.
>>
>> —
>> Reply to this email directly, view it on GitHub
>> <https://github.com/xmrig/xmrig/issues/3178#issuecomment-1347950610>, or
>> unsubscribe
>> <https://github.com/notifications/unsubscribe-auth/A4WBK45NZOZAIEYAVYSJX2TWNA2T7ANCNFSM6AAAAAAS4XV5LY>
>> .
>> You are receiving this because you commented.Message ID:
>> ***@***.***>
>>
>


## ghost | 2022-12-18T05:45:01+00:00
@SChernykh
Is this wallet address okay: `4Ax2xrtEBb386TN9zxYAGVSMjc6zzs4Xqf6B3pNvSYz8U6cA7LCyBxHGsuXbyK7xFmA2a1N8jQAL3aGBzBCE2GgXHB8tRko`.

https://minerstat.com/wallet-address-validator/monero tells it is. I am not sure how 2 got replaced by 4 when I was copying wallet address that day (it got fucked probably when I was using vim) but anways I get same `incompatible/disabled algorithm "rx/0" detected, reconnect`
```
./xmrig --no-cpu --opencl -o xmrpool.eu:9999 -u 4Ax2xrtEBb386TN9zxYAGVSMjc6zzs4Xqf6B3pNvSYz8U6cA7LCyBxHGsuXbyK7xFmA2a1N8jQAL3aGBzBCE2GgXHB8tRko --algo='rx/0' -k --tls
./xmrig: unrecognized option: opencl
 * ABOUT        XMRig/6.18.1 gcc/9.3.0
 * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Athlon Silver 3050U with Radeon Graphics (1) 64-bit AES
                L2:1.0 MB L3:4.0 MB 2C/2T NUMA:1
 * MEMORY       2.4/5.7 GB (43%)
                Bottom - Slot 1 (left): <empty>
                Bottom - Slot 2 (right): 8 GB DDR4 @ 2400 MHz M471A1K43EB1-CWE    
 * MOTHERBOARD  HP - 8706
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmrpool.eu:9999 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
[2022-12-18 11:29:07.442]  net      xmrpool.eu:9999 incompatible/disabled algorithm "rx/0" detected, reconnect
[2022-12-18 11:29:07.443]  net      xmrpool.eu:9999 login error code: 6
[2022-12-18 11:29:13.331]  net      xmrpool.eu:9999 incompatible/disabled algorithm "rx/0" detected, reconnect
[2022-12-18 11:29:13.331]  net      xmrpool.eu:9999 login error code: 6
[2022-12-18 11:29:14.046]  signal   Ctrl+C received, exiting
```
I have tried other pools in xmrig only and all seems to have problems with algorithm. However, xmrig-amd works but doesn't have randomx
```
./xmrig-amd -c xpool.json 
 * ABOUT        XMRig-AMD/2.14.6 gcc/5.4.0
 * LIBS         libuv/1.31.0 OpenCL/2.0 OpenSSL/1.1.1c microhttpd/0.9.62 
 * CPU          AMD Athlon Silver 3050U with Radeon Graphics    x64 AES
 * ALGO         cryptonight, donate=5%
 * POOL #1      xmrpool.eu:5555 variant auto
 * COMMANDS     hashrate, pause, resume
[2022-12-18 11:32:32] compiling code and initializing GPUs. This will take a while...
[2022-12-18 11:32:32] found AMD platform index: 0, name: Advanced Micro Devices, Inc.
[2022-12-18 11:32:32] found OpenCL GPU: AMD Athlon Silver 3050U with Radeon Graphics (gfx902:xnack+), cu: 11
[2022-12-18 11:32:32] #00, GPU #00 AMD Athlon Silver 3050U with Radeon Graphics (gfx902:xnack+), i:480 (8/256), si:2/2, u:8, cu:11
[2022-12-18 11:32:32]              0.94/2.43/3 GB
[2022-12-18 11:32:35] #01, GPU #00 AMD Athlon Silver 3050U with Radeon Graphics (gfx902:xnack+), i:480 (8/256), si:2/2, u:8, cu:11
[2022-12-18 11:32:35]              0.94/2.43/3 GB
[2022-12-18 11:32:35] configuration saved to: "xpool.json"
[2022-12-18 11:32:35] [xmrpool.eu:5555] error: "Please upgrade 'XMRig-AMD/2.14.6 (Linux x86_64) libuv/1.31.0 gcc/5.4.0' to v3.2.0+ to support new rx/0 Monero algo", code: -1                                                                                                                                                                   
[2022-12-18 11:32:37] Ctrl+C received, exiting
```
Config:
```
{
    "algo": "cryptonight",
    "api": {
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "cache": true,
    "colors": true,
    "donate-level": 5,
    "log-file": null,
    "opencl-platform": "AMD",
    "opencl-loader": "libOpenCL.so",
    "pools": [
        {
            "url": "xmrpool.eu:5555",
            "user": "4Ax2xrtEBb386TN9zxYAGVSMjc6zzs4Xqf6B3pNvSYz8U6cA7LCyBxHGsuXbyK7xFmA2a1N8jQAL3aGBzBCE2GgXHB8tRko",
            "pass": "x",
            "rig-id": "test",
            "nicehash": false,
            "keepalive": true,
            "variant": -1,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "threads": [
        {
            "index": 0,
            "intensity": 480,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 8,
            "comp_mode": false,
            "affine_to_cpu": false
        },
        {
            "index": 0,
            "intensity": 480,
            "worksize": 8,
            "strided_index": 2,
            "mem_chunk": 2,
            "unroll": 8,
            "comp_mode": false,
            "affine_to_cpu": false
        }
    ],
    "user-agent": null,
    "syslog": false,
    "watch": true
}
```

Adding --pass="x" doesnt help too as I thought this might be the problem as xmrig-amd config had it and xmrig didnt. It didnt change anything sadly

## SChernykh | 2022-12-18T09:26:56+00:00
It looks like you downloaded the static build of xmrig (`xmrig-6.18.1-linux-static-x64.tar.gz`), this version only supports CPU, which is why it says `unrecognized option: opencl`. I've checked your command line and it works for me. If you really want to mine RandomX with your GPU and not CPU, download `xmrig-6.18.1-linux-x64.tar.gz`

## ghost | 2022-12-18T14:04:46+00:00
Thank you it works @SChernykh 

# Action History
- Created by: ghost | 2022-12-13T04:46:39+00:00
- Closed at: 2022-12-18T14:04:46+00:00
