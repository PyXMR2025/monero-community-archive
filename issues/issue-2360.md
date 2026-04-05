---
title: Low hash rates on FreeBSD, probably because registry values are not being set
source_url: https://github.com/xmrig/xmrig/issues/2360
author: gkroon
assignees: []
labels: []
created_at: '2021-05-09T12:33:03+00:00'
updated_at: '2021-05-09T19:00:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Registry values aren't being set on FreeBSD, and manually overriding with `cpucontrol(8)` also doesn't seem to work. I suspect that is why my hash rate is so low on FreeBSD.

**To Reproduce**

My OS, and how I ran XMRig.

```
# uname -v
FreeBSD 12.2-RELEASE-p6 f2858df162b(HEAD) TRUENAS
# ./xmrig -a rx/0 -o monero.herominers.com:10191 -u MY_ADDRESS -k --tls -p MY_WORKER
 * ABOUT        XMRig/6.12.1 clang/10.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 9 3950X 16-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       13.1/31.9 GB (41%)
                DIMM 0: <empty>
                DIMM_A1: 16 GB DDR4 @ 3200 MHz CMK32GX4M2B3200C16  
                DIMM 0: <empty>
                DIMM_B1: 16 GB DDR4 @ 3200 MHz CMK32GX4M2B3200C16  
 * MOTHERBOARD  Micro-Star International Co., Ltd - B450 TOMAHAWK MAX (MS-7C02)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      monero.herominers.com:10191 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-05-09 14:08:11.599]  net      use pool monero.herominers.com:10191 TLSv1.2 157.90.94.153
[2021-05-09 14:08:11.599]  net      fingerprint (SHA-256): "81a2c88ddfd210295be5bdf5907041eff023982194374daed21f246213cbf667"
[2021-05-09 14:08:11.599]  net      new job from monero.herominers.com:10191 diff 120001 algo rx/0 height 2357129
[2021-05-09 14:08:11.599]  cpu      use argon2 implementation AVX2
[2021-05-09 14:08:11.599]  randomx  init dataset algo rx/0 (32 threads) seed 93374bbc2ac22459...
[2021-05-09 14:08:11.847]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (248 ms)
[2021-05-09 14:08:13.345]  randomx  dataset ready (1499 ms)
[2021-05-09 14:08:13.345]  cpu      use profile  rx  (32 threads) scratchpad 2048 KB
[2021-05-09 14:08:13.360]  cpu      READY threads 32/32 (32) huge pages 100% 32/32 memory 65536 KB (15 ms)
[2021-05-09 14:08:33.302]  cpu      accepted (1/0) diff 120001 (60 ms)
[2021-05-09 14:08:33.578]  cpu      accepted (2/0) diff 120001 (47 ms)
[2021-05-09 14:08:41.236]  cpu      accepted (3/0) diff 120001 (67 ms)
[2021-05-09 14:08:45.074]  cpu      accepted (4/0) diff 120001 (94 ms)
[2021-05-09 14:09:17.607]  miner    speed 10s/60s/15m 7905.6 7935.6 n/a H/s max 8006.1 H/s
```

I also tried to play around with overriding the registries manually:

```
#!/bin/sh

for x in /dev/cpuctl*; do
    cpucontrol -m 0xc0011020=0 "$x"
    cpucontrol -m 0xc0011021=0x40 "$x"
    cpucontrol -m 0xc0011022=0x1510000 "$x"
    cpucontrol -m 0xc001102b=0x2000cc16 "$x"
done
```

But that didn't have any effect when restarting XMRig.

**Expected behavior**
I would expect a much higher hash rate (17000 H/s on Linux, which does detect and applies the ryzen_17h preset automatically).

**Additional context**
In the above example, I downloaded and ran the pre-compiled binary from https://github.com/xmrig/xmrig/releases/download/v6.12.1/xmrig-6.12.1-freebsd-static-x64.tar.gz. I normally run the latest version in FreeBSD (currently version 6.11.0), inside a jail. Neither seem to provide the hash rate I should be getting.

# Discussion History
## NoResponse13 | 2021-05-09T18:36:17+00:00
show please `ls /dev/cpuctl*`

## gkroon | 2021-05-09T18:46:38+00:00
> show please `ls /dev/cpuctl*`

```
# ls -1 /dev/cpuctl*
/dev/cpuctl0
/dev/cpuctl1
/dev/cpuctl10
/dev/cpuctl11
/dev/cpuctl12
/dev/cpuctl13
/dev/cpuctl14
/dev/cpuctl15
/dev/cpuctl16
/dev/cpuctl17
/dev/cpuctl18
/dev/cpuctl19
/dev/cpuctl2
/dev/cpuctl20
/dev/cpuctl21
/dev/cpuctl22
/dev/cpuctl23
/dev/cpuctl24
/dev/cpuctl25
/dev/cpuctl26
/dev/cpuctl27
/dev/cpuctl28
/dev/cpuctl29
/dev/cpuctl3
/dev/cpuctl30
/dev/cpuctl31
/dev/cpuctl4
/dev/cpuctl5
/dev/cpuctl6
/dev/cpuctl7
/dev/cpuctl8
/dev/cpuctl9
```

## NoResponse13 | 2021-05-09T19:00:35+00:00
thought that the kernel module was not loaded 

# Action History
- Created by: gkroon | 2021-05-09T12:33:03+00:00
