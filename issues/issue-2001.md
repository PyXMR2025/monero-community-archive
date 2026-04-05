---
title: msr kernel module is not available
source_url: https://github.com/xmrig/xmrig/issues/2001
author: heavyarms2112
assignees: []
labels: []
created_at: '2020-12-24T01:18:28+00:00'
updated_at: '2025-08-05T17:18:44+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:26:55+00:00'
---

# Original Description
athlon 3000g cpu on linux get the below message
msr kernel module is not available,
FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

Is this a red herring?

` * ABOUT        XMRig/6.7.0 gcc/9.3.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Athlon 3000G with Radeon Vega Graphics (1) 64-bit AES
                L2:1.0 MB L3:4.0 MB 2C/4T NUMA:1
 * MEMORY       6.0/15.6 GB (38%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.supportxmr.com:5555 algo cn/r
 * COMMANDS     hashrate, pause, resume, results, connection
[2020-12-23 20:14:31.889]  net      use pool pool.supportxmr.com:5555  104.140.244.186
[2020-12-23 20:14:31.889]  net      new job from pool.supportxmr.com:5555 diff 50000 algo rx/0 height 2258850
[2020-12-23 20:14:31.889]  cpu      use argon2 implementation AVX2
[2020-12-23 20:14:31.891]  msr      msr kernel module is not available
[2020-12-23 20:14:31.891]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2020-12-23 20:14:31.891]  randomx  init dataset algo rx/0 (4 threads) seed fd1813e59eef6d6a...
[2020-12-23 20:14:32.151]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (260 ms)
[2020-12-23 20:14:39.471]  randomx  dataset ready (7320 ms)
[2020-12-23 20:14:39.471]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2020-12-23 20:14:39.474]  cpu      READY threads 2/2 (2) huge pages 100% 2/2 memory 4096 KB (2 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |     n/a |     n/a |     n/a |
|        1 |        1 |     n/a |     n/a |     n/a |
.....
[2020-12-23 20:17:39.587]  miner    speed 10s/60s/15m 1443.9 1444.7 n/a H/s max 1446.4 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   720.5 |   720.8 |     n/a |
|        1 |        1 |   723.8 |   723.8 |     n/a |
[2020-12-23 20:18:15.154]  miner    speed 10s/60s/15m 1444.3 1444.6 n/a H/s max 1446.4 H/s
`

# Discussion History
## techroy23 | 2020-12-26T15:07:33+00:00
use sudo
eg
sudo ./xmrig

## shadragon | 2021-03-17T19:36:40+00:00
@techroy23 Thank you for your answer. 

Same issue, same fix. Cheers man. 

## heavyarms2112 | 2021-03-17T19:39:51+00:00
> use sudo
> eg
> sudo ./xmrig

no it wasn't this. I was running with sudo. the module wasn't available actually. I had to fix the unavailability with a restart.

## CaioMorato | 2021-04-20T05:47:52+00:00
Lol. it worked here for xlarig, thank you so much!



## ChandraMedhika | 2021-09-24T03:14:11+00:00
> 
> 
> use sudo
> eg
> sudo ./xmrig

Thank you for reminding

## gudata | 2022-03-24T19:12:22+00:00
What is the solution if I ran xmrig in docker container?

## heavyarms2112 | 2022-03-24T19:25:31+00:00
> What is the solution if I ran xmrig in docker container?

i don't think you can run msr tweaks in docker.

## cgumb | 2022-06-23T00:41:18+00:00
> use sudo eg sudo ./xmrig

Should we really be running xmrig as root? :/ 

## SloppyPuppy | 2023-12-09T20:36:53+00:00
> > use sudo eg sudo ./xmrig
> 
> Should we really be running xmrig as root? :/

My exact thought, I don't trust a miner to be run by the root user. And I realize its a low level tweak that requires direct kernel access, ig we have to deal with it if it's your main computer, but also you could argue it's for the best since you really shouldn't be mining on your pc (unless its in downtime), you can, but don't compromise your security.

## SChernykh | 2023-12-09T21:56:38+00:00
You can run https://github.com/xmrig/xmrig/blob/master/scripts/randomx_boost.sh with `sudo` and then run XMRig without `sudo`, and MSR will work.

## AyoubCoding21 | 2025-08-05T17:18:44+00:00
it didnt work

# Action History
- Created by: heavyarms2112 | 2020-12-24T01:18:28+00:00
- Closed at: 2021-04-12T14:26:55+00:00
