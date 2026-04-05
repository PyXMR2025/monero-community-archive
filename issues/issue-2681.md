---
title: MSR Mod Failed to Apply
source_url: https://github.com/xmrig/xmrig/issues/2681
author: goodkarma07
assignees: []
labels: []
created_at: '2021-11-10T23:53:41+00:00'
updated_at: '2022-03-17T10:27:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Not sure why MSR mod won't apply, I am doing this as admin

![image](https://user-images.githubusercontent.com/73962646/141212140-cbd2525c-b246-41a0-841e-09d114dfaf82.png)


# Discussion History
## Lonnegan | 2021-11-11T00:04:13+00:00
The xmrig version 6.8.1 you are using is older than your Intel Tiger Lake-H CPU! Please try the latest version 6.15.3 of xmrig!

## MRvykyng | 2021-11-13T22:06:12+00:00

C:\Windows\system32>cd C:\Users\Asus\Desktop\xmrig-6.15.3\

C:\Users\Asus\Desktop\xmrig-6.15.3>xmrig.exe -o rx-us.unmineable.com:3333 -u SHIB:0x9BF2f541311b6dB2c0B78afc40666a56a48fc293.ASUS#e4xd-wmzl -p x
 * ABOUT        XMRig/6.15.3 gcc/10.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Pentium(R) Silver N5030 CPU @ 1.10GHz (1) 64-bit AES
                L2:4.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       2.5/3.8 GB (66%)
                A1_DIMM0: 4 GB DDR4 @ 2400 MHz 4ATF1264HZ-2G6E1
                A1_DIMM1: <empty>
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - E410MA
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      rx-us.unmineable.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-13 13:58:40.828]  net      use pool rx-us.unmineable.com:3333  138.68.148.132
[2021-11-13 13:58:40.828]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492693 (64 tx)
[2021-11-13 13:58:40.828]  cpu      use argon2 implementation SSSE3
[2021-11-13 13:58:40.875]  msr      cannot set MSR 0x000001a4 to 0x000000000000000f
[2021-11-13 13:58:40.922]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-11-13 13:58:40.922]  randomx  init dataset algo rx/0 (4 threads) seed 3185acac234a171b...
[2021-11-13 13:58:41.281]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492693 (64 tx)
[2021-11-13 13:58:41.313]  randomx  allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (400 ms)
[2021-11-13 13:58:56.385]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492693 (64 tx)
[2021-11-13 13:58:58.150]  randomx  dataset ready (16824 ms)
[2021-11-13 13:58:58.150]  cpu      use profile  rx  (2 threads) scratchpad 2048 KB
[2021-11-13 13:58:58.181]  cpu      READY threads 2/2 (2) huge pages 100% 2/2 memory 4096 KB (29 ms)
[2021-11-13 13:59:11.349]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492693 (64 tx)
[2021-11-13 13:59:26.311]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492693 (64 tx)
[2021-11-13 13:59:31.432]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492693 (99 tx)
[2021-11-13 13:59:41.422]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492693 (99 tx)
[2021-11-13 13:59:44.639]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492694 (84 tx)
[2021-11-13 13:59:52.006]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492695 (1 tx)
[2021-11-13 13:59:56.265]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492695 (1 tx)
[2021-11-13 13:59:59.608]  miner    speed 10s/60s/15m 1.03 n/a n/a H/s max 1.13 H/s
[2021-11-13 14:00:11.276]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492695 (1 tx)
[2021-11-13 14:00:50.788]  cpu      accepted (1/0) diff 100001 (239 ms)
[2021-11-13 14:00:56.342]  net      new job from rx-us.unmineable.com:3333 diff 100001 algo rx/0 height 2492695 (1 tx)
[2021-11-13 14:01:00.886]  miner    speed 10s/60s/15m 311.4 122.9 n/a H/s max 311.4 H/s


Unable to initiate MSR Mod
Secure Boot Disabled
Not sure what i'm missing,so I am hopeful I can get some help from my log
Thanx in Advance for your time/help

## SChernykh | 2021-11-13T22:11:28+00:00
```
CPU Intel(R) Pentium(R) Silver N5030 CPU @ 1.10GHz (1) 64-bit AES
L2:4.0 MB L3:0.0 MB 4C/4T NUMA:1
```
This CPU doesn't support MSR mod. It's a low-power Intel Atom CPU, not a desktop CPU.

## MRvykyng | 2021-11-13T22:18:58+00:00
Thank you SChernykh for your swift reply.
Thought I had bad configurations, but obviously not
I will stop playing with my settings, reboot my puter, and let xmrig churn away
Thanx Again-Cheers!!!!

## ghost | 2021-11-17T01:06:48+00:00
I have the same problem and nobody seems to know what the problem is? then it must be a bug?

## Spudz76 | 2021-11-17T16:23:14+00:00
Well if you have the WinRing service exists error then you need to uninstall whatever it says it found (in the original screenshot, it was NiceHashMiner that was in the way).

Some clashing WinRing providers still work (the one with OpenHardwareMonitor) but not all of them.

## Rgreenfield86 | 2022-03-17T10:27:43+00:00
How do i apply MSR mod for the Tiger lake U ?

# Action History
- Created by: goodkarma07 | 2021-11-10T23:53:41+00:00
