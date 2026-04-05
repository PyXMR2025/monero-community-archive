---
title: killed immediately
source_url: https://github.com/xmrig/xmrig/issues/2993
author: bitmastercoin
assignees: []
labels:
- question
created_at: '2022-03-25T18:11:54+00:00'
updated_at: '2022-04-03T07:44:50+00:00'
type: issue
status: closed
closed_at: '2022-04-03T07:42:48+00:00'
---

# Original Description

root@mint:/home/mint/xmrig/build# ./xmrig
 * ABOUT        XMRig/6.16.4 gcc/9.4.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   disabled
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU X5550 @ 2.67GHz (1) 64-bit -AES
                L2:1.0 MB L3:8.0 MB 4C/4T NUMA:1
 * MEMORY       3.7/3.8 GB (96%)
                CPU0 DIMM1: 1 GB DDR3 @ 1333 MHz M391B2873DZ1-CH9
                CPU0 DIMM2: 1 GB DDR3 @ 1333 MHz 9905432-008.A00LF
                CPU0 DIMM3: 1 GB DDR3 @ 1333 MHz M391B2873DZ1-CH9
                CPU0 DIMM4: 1 GB DDR3 @ 1333 MHz M391B2873DZ1-CH9
                CPU0 DIMM5: 2 GB DDR3 @ 1333 MHz OCZ3V1333LV2G_SYX2
                CPU1 DIMM1: 2 GB DDR3 @ 1333 MHz KP223C-ELD
                CPU1 DIMM2: 2 GB DDR3 @ 1333 MHz KP223C-ELD
                CPU1 DIMM3: 2 GB DDR3 @ 1333 MHz KP223C-ELD
                CPU1 DIMM4: 2 GB DDR3 @ 1333 MHz KP223C-ELD
                CPU1 DIMM5: 4 GB DDR3 @ 1600 MHz F3-17000CL11-4GBSR
                CPU1 DIMM6: 2 GB DDR3 @ 1333 MHz OCZ3V1333LV2G_SYX2
                SYSTEM ROM: 0 GB Flash @ 0 MHz SYSTEM ROM
 * MOTHERBOARD  Hewlett-Packard - 0AECh
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      rx.unmineable.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled (failed to load OpenCL runtime)
 * CUDA         disabled
[2022-03-25 18:11:13.018]  net      use pool rx.unmineable.com:3333  139.59.164.251
[2022-03-25 18:11:13.019]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2587532 (2 tx)
[2022-03-25 18:11:13.019]  cpu      use argon2 implementation SSSE3
[2022-03-25 18:11:14.219]  randomx  init dataset algo rx/0 (4 threads) seed e4d555e6b077f469...
[2022-03-25 18:11:14.220]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
Killed




# Discussion History
## Spudz76 | 2022-03-25T21:18:08+00:00
You need to balance the RAM between the CPUs more evenly, and ideally have the same size/speed/model in every slot.

CPU0 has 6GB and CPU1 has 12GB

Mismatched sizes will probably break multi-channeling.

Weird the system total is only 4GB since you have 18GB...

## rlabrach | 2022-03-29T14:12:04+00:00
Hello,
i have same issue on MacBook Air M1 : 

Last login: Tue Mar 29 15:50:03 on ttys000
/Applications/xmrig-6.16.4/xmrig ; exit;
renaud.labracherie@FRNUM-MC823-RL ~ % /Applications/xmrig-6.16.4/xmrig ; exit;
zsh: killed     /Applications/xmrig-6.16.4/xmrig

Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.

[Opération terminée]



## xmrig | 2022-04-03T07:42:48+00:00
This is some kind of virtual machine with limited memory `MEMORY 3.7/3.8 GB (96%)`.

## xmrig | 2022-04-03T07:44:50+00:00
#2986

# Action History
- Created by: bitmastercoin | 2022-03-25T18:11:54+00:00
- Closed at: 2022-04-03T07:42:48+00:00
