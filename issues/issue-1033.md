---
title: can add support for mipsel cpu?
source_url: https://github.com/xmrig/xmrig/issues/1033
author: 77pippofranco
assignees: []
labels:
- wontfix
created_at: '2019-06-12T16:22:01+00:00'
updated_at: '2021-01-04T21:53:15+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:41:32+00:00'
---

# Original Description
what think about BCM7346B2 cpu ?

cat /proc/cpuinfo 
system type             : BCM7346B2 STB platform
machine                 : Unknown
processor               : 0
cpu model               : Broadcom BMIPS5000 V1.1  FPU V0.1
BogoMIPS                : 733.18
cpu MHz                 : 1104.006
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 64
extra interrupt vector  : yes
hardware watchpoint     : no
isa                     : mips1 mips2 mips32r1
ASEs implemented        :
shadow register sets    : 1
kscratch registers      : 0
package                 : 0
core                    : 0
VCED exceptions         : not available
VCEI exceptions         : not available

processor               : 1
cpu model               : Broadcom BMIPS5000 V1.1  FPU V0.1
BogoMIPS                : 552.96
cpu MHz                 : 1104.006
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 64
extra interrupt vector  : yes
hardware watchpoint     : no
isa                     : mips1 mips2 mips32r1
ASEs implemented        :
shadow register sets    : 1
kscratch registers      : 0
package                 : 0
core                    : 0
VCED exceptions         : not available
VCEI exceptions         : not available

i have try to build in debian quemu vmlinux-4.9.0-4-4kc-malta without success.. can help me? thx

# Discussion History
## Spudz76 | 2019-06-15T16:51:49+00:00
You would have to disable all ASM and remove all incompatible optimizations (`-maes` and friends)
And even then it might not work, but if it does... you could be looking at a very maximum hashrate of 1.2H/s, probably worse.

In other words, no, not worth it, MIPS32 does not have the accels needed for present-day algos, and even worse is 32-bit.  Minimum 'embedded' type CPU is generally some form of ARM with Neon extensions.  Also fast local memory (cpu cache) is where the action happens, if it has to go out to external memory the hashrate is destroyed (part of ASIC resistance).  These have no cache and their memory is slow.

Designed for running large case/switch or if/then/else trees, but not really for "thinking" or "maths" besides arithmetic.  Less a CPU than a Logic Unit (one tiny step above a microcontroller).

## seisdr | 2021-01-04T21:53:15+00:00
I want to do it though
nanostation has no enough storage for qemu and xmrig so I want static xmrig for mipsel 

# Action History
- Created by: 77pippofranco | 2019-06-12T16:22:01+00:00
- Closed at: 2019-08-02T11:41:32+00:00
