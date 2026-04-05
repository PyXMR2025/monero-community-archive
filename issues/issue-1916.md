---
title: Illegal Instruction crash with randomx on Arm
source_url: https://github.com/xmrig/xmrig/issues/1916
author: turtleminor13
assignees: []
labels:
- arm
created_at: '2020-10-26T06:24:52+00:00'
updated_at: '2021-04-12T14:43:58+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:43:57+00:00'
---

# Original Description
**Describe the bug**
On Arm, randomx algos crash at initialization with Illegal Instruction.  Frequently (not always) crashes with rx/0, and with rx/wow always crashes.

**To Reproduce**
Run randomx algo on Arm cpu, using Xmrig v6.4.0, or earlier v6.x versions.

**Expected behavior**
No crash

**Required data**
Observed on Jetson TX2 with 8gb ram running ubuntu 18.04.5, and also Rock Pi 4 with 4gb ram running Armbian.

**Additional context**
Screenshots from Jetson TX2
![image](https://user-images.githubusercontent.com/49797136/97139700-4b9a7600-1718-11eb-95e6-1ed8cb3deee5.png)
![image](https://user-images.githubusercontent.com/49797136/97140149-3ffb7f00-1719-11eb-89ea-710774b67af7.png)



# Discussion History
## Saikatsaha1996 | 2020-10-26T08:00:20+00:00
> **Describe the bug**
> On Arm, randomx algos crash at initialization with Illegal Instruction.  Frequently (not always) crashes with rx/0, and with rx/wow always crashes.
> 
> **To Reproduce**
> Run randomx algo on Arm cpu, using Xmrig v6.4.0, or earlier v6.x versions.
> 
> **Expected behavior**
> No crash
> 
> **Required data**
> Observed on Jetson TX2 with 8gb ram running ubuntu 18.04.5, and also Odroid N2 with 4gb ram running Armbian.
> 
> **Additional context**
> Screenshots from Jetson TX2
> ![image](https://user-images.githubusercontent.com/49797136/97139700-4b9a7600-1718-11eb-95e6-1ed8cb3deee5.png)
> ![image](https://user-images.githubusercontent.com/49797136/97140149-3ffb7f00-1719-11eb-89ea-710774b67af7.png)
> 
> 

What is your hash rate?
And how you enable your huge page 100% can you please tell me?

## SChernykh | 2020-10-26T08:39:20+00:00
@turtleminor13 Can you run it with gdb: `gdb ./xmrig` and do `layout asm` command when it crashes? It will show what instruction is "illegal".

## turtleminor13 | 2020-10-26T16:33:24+00:00
@SChernykh  "Reading symbols from ./xmrig...(no debugging symbols found)...done."  Does it need to be recompiled for debug symbols?  What are steps?
![image](https://user-images.githubusercontent.com/49797136/97200159-1587e100-176e-11eb-8887-550a6a22a9c4.png)


## SChernykh | 2020-10-26T16:43:36+00:00
Type `run` there and press enter. When it crashes, type `layout asm` and it'll show you where it crashed.

## turtleminor13 | 2020-10-26T18:25:35+00:00
Thanks, here's the result for rx/wow:

turtlejas@tx2:~/mining/xmrig640/build$ gdb ./xmrig
GNU gdb (Ubuntu 8.1-0ubuntu3.2) 8.1.0.20180409-git
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "aarch64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./xmrig...(no debugging symbols found)...done.
(gdb) run --bench=1M -a rx/wow
Starting program: /home/turtlejas/mining/xmrig640/build/xmrig --bench=1M -a rx/wow
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
 * ABOUT        XMRig/6.4.0 gcc/7.5.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Cortex-A57 (2) x64 AES
                L2:2.0 MB L3:0.0 MB 6C/6T NUMA:1
 * MEMORY       4.0/7.7 GB (53%)
 * DONATE       0%
 * POOL #1      benchmark algo rx/wow
 * COMMANDS     hashrate, pause, resume, results, connection
[New Thread 0x7fb5a301d0 (LWP 14890)]
 * OPENCL       disabled
 * CUDA         disabled
[2020-10-26 11:21:17.915]  bench    start benchmark hashes 1M algo rx/wow print_time 60s
[2020-10-26 11:21:17.915]  cpu      use argon2 implementation default
[2020-10-26 11:21:17.915]  randomx  init dataset algo rx/wow (6 threads) seed 0000000000000000...
[2020-10-26 11:21:18.267]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (351 ms)
[New Thread 0x7fb522f1d0 (LWP 14891)]
[New Thread 0x7fb4a2e1d0 (LWP 14892)]
[New Thread 0x7faffff1d0 (LWP 14893)]
[New Thread 0x7faf7fe1d0 (LWP 14894)]
[New Thread 0x7faeffd1d0 (LWP 14895)]
[New Thread 0x7fae7fc1d0 (LWP 14896)]
[Thread 0x7faeffd1d0 (LWP 14895) exited]
[Thread 0x7fb522f1d0 (LWP 14891) exited]
[Thread 0x7faffff1d0 (LWP 14893) exited]
[Thread 0x7faf7fe1d0 (LWP 14894) exited]
[Thread 0x7fb4a2e1d0 (LWP 14892) exited]
[2020-10-26 11:21:37.873]  randomx  dataset ready (19607 ms)
[2020-10-26 11:21:37.873]  cpu      use profile  rx/wow  (6 threads) scratchpad 1024 KB
[Thread 0x7fae7fc1d0 (LWP 14896) exited]
[New Thread 0x7fae7fc1d0 (LWP 14897)]
[New Thread 0x7faeffd1d0 (LWP 14898)]
[New Thread 0x7faf7fe1d0 (LWP 14899)]
[New Thread 0x7faffff1d0 (LWP 14900)]
[New Thread 0x7fb522f1d0 (LWP 14901)]
[New Thread 0x7fb482e1d0 (LWP 14902)]

Thread 10 "xmrig" received signal SIGILL, Illegal instruction.
[Switching to Thread 0x7faeffd1d0 (LWP 14898)]
0x0000007faddfc000 in ?? ()
(gdb) layout asm
   ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  >│0x7faddfc000    sub    sp, sp, #0xc0                                                                                                                       │
   │0x7faddfc004    stp    x16, x17, [sp]                                                                                                                      │
   │0x7faddfc008    stp    x18, x19, [sp, #16]                                                                                                                 │
   │0x7faddfc00c    stp    x20, x21, [sp, #32]                                                                                                                 │
   │0x7faddfc010    stp    x22, x23, [sp, #48]                                                                                                                 │
   │0x7faddfc014    stp    x24, x25, [sp, #64]                                                                                                                 │
   │0x7faddfc018    stp    x26, x27, [sp, #80]                                                                                                                 │
   │0x7faddfc01c    stp    x28, x29, [sp, #96]                                                                                                                 │
   │0x7faddfc020    stp    x8, x30, [sp, #112]                                                                                                                 │
   │0x7faddfc024    stp    d8, d9, [sp, #128]                                                                                                                  │
   │0x7faddfc028    stp    d10, d11, [sp, #144]                                                                                                                │
   │0x7faddfc02c    stp    d12, d13, [sp, #160]                                                                                                                │
   │0x7faddfc030    stp    d14, d15, [sp, #176]                                                                                                                │
   │0x7faddfc034    mov    x4, xzr                                                                                                                             │
   │0x7faddfc038    mov    x5, xzr                                                                                                                             │
   │0x7faddfc03c    mov    x6, xzr                                                                                                                             │
   │0x7faddfc040    mov    x7, xzr                                                                                                                             │
   │0x7faddfc044    mov    x12, xzr                                                                                                                            │
   │0x7faddfc048    mov    x13, xzr                                                                                                                            │
   │0x7faddfc04c    mov    x14, xzr                                                                                                                            │
   │0x7faddfc050    mov    x15, xzr                                                                                                                            │
   │0x7faddfc054    ldp    x9, x1, [x1]                                                                                                                        │
   │0x7faddfc058    mov    x10, x9                                                                                                                             │
   │0x7faddfc05c    ldp    q24, q25, [x0, #192]                                                                                                                │
   │0x7faddfc060    ldp    q26, q27, [x0, #224]                                                                                                                │
   │0x7faddfc064    mov    x16, #0xffffffffffffff          // #72057594037927935                                                                               │
   │0x7faddfc068    mov    v29.d[0], x16                                                                                                                       │
   │0x7faddfc06c    mov    v29.d[1], x16                                                                                                                       │
   │0x7faddfc070    ldr    q30, [x0, #64]                                                                                                                      │
   │0x7faddfc074    mov    x16, #0x80f0000000000000        // #-9155818042444218368                                                                            │
   │0x7faddfc078    mov    v31.d[0], x16                                                                                                                       │
   │0x7faddfc07c    mov    v31.d[1], x16                                                                                                                       │
   │0x7faddfc080    mrs    x8, fpcr                                                                                                                            │
   │0x7faddfc084    rbit   x8, x8                                                                                                                              │
   │0x7faddfc088    str    x0, [sp, #-16]!                                                                                                                     │
   │0x7faddfc08c    ldr    x0, 0x7fade001e4                                                                                                                    │
   └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
multi-thre Thread 0x7faeffd1d0 In:                                                                                                       L??   PC: 0x7faddfc000
(gdb)


## turtleminor13 | 2020-10-26T18:29:17+00:00
Result for rx/0:

turtlejas@tx2:~/mining/xmrig640/build$ gdb ./xmrig
GNU gdb (Ubuntu 8.1-0ubuntu3.2) 8.1.0.20180409-git
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "aarch64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./xmrig...(no debugging symbols found)...done.
(gdb) run
Starting program: /home/turtlejas/mining/xmrig640/build/xmrig
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
 * ABOUT        XMRig/6.4.0 gcc/7.5.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Cortex-A57 (2) x64 AES
                L2:2.0 MB L3:0.0 MB 6C/6T NUMA:1
 * MEMORY       4.0/7.7 GB (53%)
 * DONATE       1%
 * POOL #1      gulf.moneroocean.stream:10008 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[New Thread 0x7fb5a301d0 (LWP 14915)]
 * OPENCL       disabled
 * CUDA         disabled
[New Thread 0x7fb522f1d0 (LWP 14916)]
[New Thread 0x7fb4a2e1d0 (LWP 14917)]
[New Thread 0x7fb422d1d0 (LWP 14918)]
[New Thread 0x7fb3a2c1d0 (LWP 14919)]
[2020-10-26 11:26:38.107]  net      use pool gulf.moneroocean.stream:10008  54.188.223.206
[2020-10-26 11:26:38.108]  net      new job from gulf.moneroocean.stream:10008 diff 8000 algo rx/0 height 2216908
[2020-10-26 11:26:38.108]  cpu      use argon2 implementation default
[2020-10-26 11:26:38.108]  randomx  init dataset algo rx/0 (6 threads) seed c6b33164bdcdc962...
[2020-10-26 11:26:38.457]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (350 ms)
[New Thread 0x7fb31bc1d0 (LWP 14920)]
[New Thread 0x7fb29bb1d0 (LWP 14921)]
[New Thread 0x7fb21ba1d0 (LWP 14922)]
[New Thread 0x7fb19b91d0 (LWP 14923)]
[New Thread 0x7fb11b81d0 (LWP 14924)]
[New Thread 0x7fb09b71d0 (LWP 14925)]
[Thread 0x7fb21ba1d0 (LWP 14922) exited]
[Thread 0x7fb29bb1d0 (LWP 14921) exited]
[Thread 0x7fb31bc1d0 (LWP 14920) exited]
[Thread 0x7fb11b81d0 (LWP 14924) exited]
[Thread 0x7fb19b91d0 (LWP 14923) exited]
[2020-10-26 11:26:57.756]  randomx  dataset ready (19299 ms)
[2020-10-26 11:26:57.756]  cpu      use profile  rx  (6 threads) scratchpad 2048 KB
[Thread 0x7fb09b71d0 (LWP 14925) exited]
[New Thread 0x7fb09b71d0 (LWP 14926)]

Thread 13 "xmrig" received signal SIGILL, Illegal instruction.
[Switching to Thread 0x7fb09b71d0 (LWP 14926)]
0x0000007fb31a8080 in ?? ()
(gdb) layout asm
   ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  >│0x7fb31a8080    mrs    x8, fpcr                                                                                                                            │
   │0x7fb31a8084    rbit   x8, x8                                                                                                                              │
   │0x7fb31a8088    str    x0, [sp, #-16]!                                                                                                                     │
   │0x7fb31a808c    ldr    x0, 0x7fb31ac1e4                                                                                                                    │
   │0x7fb31a8090    ldr    x11, 0x7fb31ac1ec                                                                                                                   │
   │0x7fb31a8094    ldr    x20, 0x7fb31ac1f4                                                                                                                   │
   │0x7fb31a8098    ldr    x21, 0x7fb31ac1fc                                                                                                                   │
   │0x7fb31a809c    ldr    x22, 0x7fb31ac204                                                                                                                   │
   │0x7fb31a80a0    ldr    x23, 0x7fb31ac20c                                                                                                                   │
   │0x7fb31a80a4    ldr    x24, 0x7fb31ac214                                                                                                                   │
   │0x7fb31a80a8    ldr    x25, 0x7fb31ac21c                                                                                                                   │
   │0x7fb31a80ac    ldr    x26, 0x7fb31ac224                                                                                                                   │
   │0x7fb31a80b0    ldr    x27, 0x7fb31ac22c                                                                                                                   │
   │0x7fb31a80b4    ldr    x28, 0x7fb31ac234                                                                                                                   │
   │0x7fb31a80b8    ldr    x29, 0x7fb31ac23c                                                                                                                   │
   │0x7fb31a80bc    ldr    x30, 0x7fb31ac244                                                                                                                   │
   │0x7fb31a80c0    ldr    q0, 0x7fb31ac24c                                                                                                                    │
   │0x7fb31a80c4    ldr    q1, 0x7fb31ac25c                                                                                                                    │
   │0x7fb31a80c8    ldr    q2, 0x7fb31ac26c                                                                                                                    │
   │0x7fb31a80cc    ldr    q3, 0x7fb31ac27c                                                                                                                    │
   │0x7fb31a80d0    ldr    q4, 0x7fb31ac28c                                                                                                                    │
   │0x7fb31a80d4    ldr    q5, 0x7fb31ac29c                                                                                                                    │
   │0x7fb31a80d8    ldr    q6, 0x7fb31ac2ac                                                                                                                    │
   │0x7fb31a80dc    ldr    q7, 0x7fb31ac2bc                                                                                                                    │
   │0x7fb31a80e0    ldr    q8, 0x7fb31ac2cc                                                                                                                    │
   │0x7fb31a80e4    ldr    q9, 0x7fb31ac2dc                                                                                                                    │
   │0x7fb31a80e8    ldr    q10, 0x7fb31ac2ec                                                                                                                   │
   │0x7fb31a80ec    ldr    q11, 0x7fb31ac2fc                                                                                                                   │
   │0x7fb31a80f0    ldr    q12, 0x7fb31ac30c                                                                                                                   │
   │0x7fb31a80f4    ldr    q13, 0x7fb31ac31c                                                                                                                   │
   │0x7fb31a80f8    ldr    q14, 0x7fb31ac32c                                                                                                                   │
   │0x7fb31a80fc    ldr    q15, 0x7fb31ac33c                                                                                                                   │
   │0x7fb31a8100    lsr    x18, x10, #32                                                                                                                       │
   │0x7fb31a8104    and    w16, w10, #0x1fffc0                                                                                                                 │
   │0x7fb31a8108    and    w17, w18, #0x1fffc0                                                                                                                 │
   │0x7fb31a810c    add    x16, x16, x2                                                                                                                        │
   └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
multi-thre Thread 0x7fb09b71d0 In:                                                                                                       L??   PC: 0x7fb31a8080


(gdb)


## SChernykh | 2020-10-26T18:49:45+00:00
All I can see is that it's pointing at legit ARMv8-a instructions, so it's most likely a problem with caching - xmrig uses GCC's `__builtin___clear_cache()` to make sure CPU sees new generated code every time. Try newer version of GCC, maybe your version doesn't implement it correctly.

## jfikar | 2020-10-27T14:24:32+00:00
It works for me on ARM64 with gcc-8.3.0, completed the new `--benchmark=1M` as well as `--benchmark=1M -a rx/wow`

## turtleminor13 | 2020-11-09T04:08:42+00:00
@SChernykh  - Thanks for fixing gcc 9 compile with v6.5.1, when I tried it last week and failed, I thought I had something wrong with my gcc setup.  Anyway I have compiled with gcc 9 and still getting the illegal instruction crash.  I have noticed that my Odroid N2 has not crashed since moving up to v6.4, where it had crashes with earlier versions of xmrig.  Maybe this is unique to the Nvidia cpu in the Jetson TX2?  

Here is the GDB output now:

turtlejas@tx2:~/mining/xmrig651/build$ gdb ./xmrig
GNU gdb (Ubuntu 8.2-0ubuntu1~18.04) 8.2
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "aarch64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./xmrig...(no debugging symbols found)...done.
(gdb) run
Starting program: /home/turtlejas/mining/xmrig651/build/xmrig
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
 * ABOUT        XMRig/6.5.1 gcc/9.3.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A57 (2) x64 AES
                L2:2.0 MB L3:0.0 MB 6C/6T NUMA:1
 * MEMORY       3.7/7.7 GB (49%)
 * DONATE       1%
 * POOL #1      gulf.moneroocean.stream:10002 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[New Thread 0x7fb59e11d0 (LWP 23108)]
[New Thread 0x7fb51e01d0 (LWP 23109)]
[New Thread 0x7fb49df1d0 (LWP 23110)]
[New Thread 0x7fb41de1d0 (LWP 23111)]
[New Thread 0x7fb39dd1d0 (LWP 23112)]
[2020-11-08 20:00:58.471]  net      use pool gulf.moneroocean.stream:10002  54.188.223.206
[2020-11-08 20:00:58.471]  net      new job from gulf.moneroocean.stream:10002 diff 2000 algo rx/0 height 2226506
[2020-11-08 20:00:58.471]  cpu      use argon2 implementation default
[2020-11-08 20:00:58.471]  randomx  init dataset algo rx/0 (6 threads) seed b7ada94788aadd1f...
[2020-11-08 20:00:58.811]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (339 ms)
[New Thread 0x7fb316d1d0 (LWP 23113)]
[New Thread 0x7fb296c1d0 (LWP 23114)]
[New Thread 0x7fb216b1d0 (LWP 23115)]
[New Thread 0x7fb196a1d0 (LWP 23116)]
[New Thread 0x7fb11691d0 (LWP 23117)]
[New Thread 0x7fb09681d0 (LWP 23118)]
[Thread 0x7fb11691d0 (LWP 23117) exited]
[Thread 0x7fb316d1d0 (LWP 23113) exited]
[Thread 0x7fb296c1d0 (LWP 23114) exited]
[Thread 0x7fb09681d0 (LWP 23118) exited]
[Thread 0x7fb216b1d0 (LWP 23115) exited]
[2020-11-08 20:01:18.423]  randomx  dataset ready (19612 ms)
[2020-11-08 20:01:18.423]  cpu      use profile  rx  (6 threads) scratchpad 2048 KB
[Thread 0x7fb196a1d0 (LWP 23116) exited]
[New Thread 0x7fb09681d0 (LWP 23119)]
[New Thread 0x7fb11691d0 (LWP 23120)]

Thread 14 "xmrig" received signal SIGILL, Illegal instruction.
[Switching to Thread 0x7fb11691d0 (LWP 23120)]
0x0000007fb3144040 in ?? ()
(gdb) layout asm
   ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  >│0x7fb3144040    mov    x7, xzr                                                                                                    │
   │0x7fb3144044    mov    x12, xzr                                                                                                   │
   │0x7fb3144048    mov    x13, xzr                                                                                                   │
   │0x7fb314404c    mov    x14, xzr                                                                                                   │
   │0x7fb3144050    mov    x15, xzr                                                                                                   │
   │0x7fb3144054    ldp    x9, x1, [x1]                                                                                               │
   │0x7fb3144058    mov    x10, x9                                                                                                    │
   │0x7fb314405c    ldp    q24, q25, [x0, #192]                                                                                       │
   │0x7fb3144060    ldp    q26, q27, [x0, #224]                                                                                       │
   │0x7fb3144064    mov    x16, #0xffffffffffffff          // #72057594037927935                                                      │
   │0x7fb3144068    mov    v29.d[0], x16                                                                                              │
   │0x7fb314406c    mov    v29.d[1], x16                                                                                              │
   │0x7fb3144070    ldr    q30, [x0, #64]                                                                                             │
   │0x7fb3144074    mov    x16, #0x80f0000000000000        // #-9155818042444218368                                                   │
   │0x7fb3144078    mov    v31.d[0], x16                                                                                              │
   │0x7fb314407c    mov    v31.d[1], x16                                                                                              │
   │0x7fb3144080    mrs    x8, fpcr                                                                                                   │
   │0x7fb3144084    rbit   x8, x8                                                                                                     │
   │0x7fb3144088    str    x0, [sp, #-16]!                                                                                            │
   │0x7fb314408c    ldr    x0, 0x7fb31481e4                                                                                           │
   │0x7fb3144090    ldr    x11, 0x7fb31481ec                                                                                          │
   │0x7fb3144094    ldr    x20, 0x7fb31481f4                                                                                          │
   │0x7fb3144098    ldr    x21, 0x7fb31481fc                                                                                          │
   │0x7fb314409c    ldr    x22, 0x7fb3148204                                                                                          │
   │0x7fb31440a0    ldr    x23, 0x7fb314820c                                                                                          │
   │0x7fb31440a4    ldr    x24, 0x7fb3148214                                                                                          │
   │0x7fb31440a8    ldr    x25, 0x7fb314821c                                                                                          │
   │0x7fb31440ac    ldr    x26, 0x7fb3148224                                                                                          │
   │0x7fb31440b0    ldr    x27, 0x7fb314822c                                                                                          │
   │0x7fb31440b4    ldr    x28, 0x7fb3148234                                                                                          │
   │0x7fb31440b8    ldr    x29, 0x7fb314823c                                                                                          │
   │0x7fb31440bc    ldr    x30, 0x7fb3148244                                                                                          │
   │0x7fb31440c0    ldr    q0, 0x7fb314824c                                                                                           │
   │0x7fb31440c4    ldr    q1, 0x7fb314825c                                                                                           │
   │0x7fb31440c8    ldr    q2, 0x7fb314826c                                                                                           │
   │0x7fb31440cc    ldr    q3, 0x7fb314827c                                                                                           │
   └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
multi-thre Thread 0x7fb11691d0 In:                                                                              L??   PC: 0x7fb3144040
(gdb) Quit


## jfikar | 2020-11-10T09:57:33+00:00
The Jetson TX2 has a Tegra X2 SoC with 2 (big?) Denver 2 cores and 4 (little?) Cortex-A57 cores. Maybe you can try to run just on Denver or just on A57 to see, where the problem is.

Also [I can share](http://ge.tt/50wVBk83) my binary compiled by gcc-8.3.0, if it helps.

## turtleminor13 | 2020-11-13T09:19:07+00:00
Nice idea jfikar.  I set my Jetson TX2 to only run on the A57 cores with "rx": [0, 3, 4, 5], in the config and still got an illegal instruction crash.
I have also done further testing on my Rock Pi 4 with an RK3399 cpu and also getting an illegal instruction crash.  So my current experience is that xmrig v6.4 or v6.5.1 crashes at RandomX startup intermittently (not always) on my Jetson TX2 and Rock Pi 4, but not seeing crashes on my Odroid N2 (with Amlogic S922X cpu).

Here is GDB output from my Rock Pi 4:

turtlejas@rockpi-4a:~/mining/xmrig651/build$ gdb ./xmrig
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "aarch64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./xmrig...(no debugging symbols found)...done.
(gdb) run
Starting program: /home/turtlejas/mining/xmrig651/build/xmrig
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
 * ABOUT        XMRig/6.5.1 gcc/8.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          ARM Cortex-A53 (2) x64 AES
                L2:0.0 MB L3:0.0 MB 6C/6T NUMA:1
 * MEMORY       2.7/3.7 GB (73%)
 * DONATE       1%
 * POOL #1      gulf.moneroocean.stream:10002 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[New Thread 0xfffff5dff1d0 (LWP 2181)]
 * OPENCL       disabled
[New Thread 0xfffff55fe1d0 (LWP 2182)]
[New Thread 0xfffff4dfd1d0 (LWP 2183)]
[New Thread 0xfffff45fc1d0 (LWP 2184)]
[New Thread 0xfffff3dfb1d0 (LWP 2185)]
[2020-11-13 00:55:19.469]  net      use pool gulf.moneroocean.stream:10002  54.188.223.206
[2020-11-13 00:55:19.470]  net      new job from gulf.moneroocean.stream:10002 diff 2000 algo rx/0 height 2229586
[2020-11-13 00:55:19.470]  cpu      use argon2 implementation default
[2020-11-13 00:55:19.470]  randomx  init dataset algo rx/0 (6 threads) seed 1d725bf87a3f3a26...
[2020-11-13 00:55:20.175]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (704 ms)
[New Thread 0xfffff35c01d0 (LWP 2187)]
[New Thread 0xfffff2dbf1d0 (LWP 2188)]
[New Thread 0xfffff25be1d0 (LWP 2189)]
[New Thread 0xfffff1dbd1d0 (LWP 2190)]
[New Thread 0xfffff15bc1d0 (LWP 2191)]
[New Thread 0xfffff0dbb1d0 (LWP 2192)]
[Thread 0xfffff1dbd1d0 (LWP 2190) exited]
[Thread 0xfffff15bc1d0 (LWP 2191) exited]
[Thread 0xfffff2dbf1d0 (LWP 2188) exited]
[Thread 0xfffff25be1d0 (LWP 2189) exited]
[Thread 0xfffff0dbb1d0 (LWP 2192) exited]
[2020-11-13 00:55:44.505]  randomx  dataset ready (24329 ms)
[2020-11-13 00:55:44.505]  cpu      use profile  rx  (6 threads) scratchpad 2048 KB
[Thread 0xfffff35c01d0 (LWP 2187) exited]
[New Thread 0xfffff0dbb1d0 (LWP 2193)]
[New Thread 0xfffff15bc1d0 (LWP 2194)]
[New Thread 0xfffff1dbd1d0 (LWP 2195)]
[New Thread 0xfffff25be1d0 (LWP 2196)]
[New Thread 0xfffff31ff1d0 (LWP 2197)]
[New Thread 0xffff51fff1d0 (LWP 2198)]
[2020-11-13 00:55:44.617]  cpu      READY threads 6/6 (6) huge pages 100% 6/6 memory 12288 KB (111 ms)

Thread 18 "xmrig" received signal SIGILL, Illegal instruction.
[Switching to Thread 0xffff51fff1d0 (LWP 2198)]
0x0000fffff35473c0 in ?? ()
(gdb) layout asm
   lqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqk
  >x0xfffff35473c0  eor    v19.16b, v19.16b, v23.16b                                                                                                                x
   x0xfffff35473c4  stp    q16, q17, [x16]                                                                                                                          x
   x0xfffff35473c8  stp    q18, q19, [x16, #32]                                                                                                                     x
   x0xfffff35473cc  subs   x3, x3, #0x1                                                                                                                             x
   x0xfffff35473d0  b.ne   0xfffff3543100  // b.any                                                                                                                 x
   x0xfffff35473d4  ldr    x0, [sp], #16                                                                                                                            x
   x0xfffff35473d8  stp    x4, x5, [x0]                                                                                                                             x
   x0xfffff35473dc  stp    x6, x7, [x0, #16]                                                                                                                        x
   x0xfffff35473e0  stp    x12, x13, [x0, #32]                                                                                                                      x
   x0xfffff35473e4  stp    x14, x15, [x0, #48]                                                                                                                      x
   x0xfffff35473e8  stp    q16, q17, [x0, #64]                                                                                                                      x
   x0xfffff35473ec  stp    q18, q19, [x0, #96]                                                                                                                      x
   x0xfffff35473f0  stp    q20, q21, [x0, #128]                                                                                                                     x
   x0xfffff35473f4  stp    q22, q23, [x0, #160]                                                                                                                     x
   x0xfffff35473f8  ldp    x16, x17, [sp]                                                                                                                           x
   x0xfffff35473fc  ldp    x18, x19, [sp, #16]                                                                                                                      x
   x0xfffff3547400  ldp    x20, x21, [sp, #32]                                                                                                                      x
   x0xfffff3547404  ldp    x22, x23, [sp, #48]                                                                                                                      x
   x0xfffff3547408  ldp    x24, x25, [sp, #64]                                                                                                                      x
   x0xfffff354740c  ldp    x26, x27, [sp, #80]                                                                                                                      x
   x0xfffff3547410  ldp    x28, x29, [sp, #96]                                                                                                                      x
   x0xfffff3547414  ldp    x8, x30, [sp, #112]                                                                                                                      x
   x0xfffff3547418  ldp    d8, d9, [sp, #128]                                                                                                                       x
   x0xfffff354741c  ldp    d10, d11, [sp, #144]                                                                                                                     x
   x0xfffff3547420  ldp    d12, d13, [sp, #160]                                                                                                                     x
   x0xfffff3547424  ldp    d14, d15, [sp, #176]                                                                                                                     x
   x0xfffff3547428  add    sp, sp, #0xc0                                                                                                                            x
   x0xfffff354742c  ret                                                                                                                                             x
   x0xfffff3547430  sub    sp, sp, #0x60                                                                                                                            x
   x0xfffff3547434  stp    x0, x1, [sp, #64]                                                                                                                        x
   x0xfffff3547438  stp    x2, x30, [sp, #80]                                                                                                                       x
   x0xfffff354743c  eor    x9, x9, x18                                                                                                                              x
   x0xfffff3547440  ror    x9, x9, #32                                                                                                                              x
   x0xfffff3547444  mov    x0, x1                                                                                                                                   x
   x0xfffff3547448  mov    x1, sp                                                                                                                                   x
   x0xfffff354744c  and    w2, w9, #0x1                                                                                                                             x
   mqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqj
multi-thre Thread 0xffff51fff1 In:                                                   


## ElectroFlux-SS | 2020-11-22T20:46:13+00:00
Is your "hw-aes" set to true in your config.json?
If so, try setting this to false or null to see problem is resolved.

## turtleminor13 | 2020-11-29T19:08:26+00:00
I did have "hw-aes": true in my config, and changing it to false does stop the illegal instruction issue on randomx.  But then performance suffers (no surprise).  For example, cn-heavy/xhv is less than half the hash rate, compared to hw-aes:true.  

@ElectroFlux-SS - Is there a known issue with ARM hw-aes?  I haven't seen an issue with it on the CN algos, just now with randomx.

## jfikar | 2020-12-02T08:09:11+00:00
@turtleminor13 that's interesting. Have you tried my compiled binary? I suspect compilation problems.

I don't have Jetson TX2 nor RK3399, but I ordered the latter. Waiting for the delivery.

## ElectroFlux-SS | 2020-12-02T14:07:33+00:00
There must be some relationship between ARM, HW-AES being on and this illegal instruction now 

I'm not sure sure if it was known, acknowledged, or corrected by the authors, but I noticed this myself when I started with this combination and v6.3.5 and above and back in mid-October 2020 for me. 

## xmrig | 2020-12-02T14:52:39+00:00
Major ARM related changes in v6.3:
* v6.3.0 I don't think it related but... https://github.com/xmrig/xmrig/pull/1771
* v6.3.2 Auto-config use thread affinity, earlier versions don't use it.


## turtleminor13 | 2020-12-03T03:10:49+00:00
@ElectroFlux-SS  thanks for confirming that you are also experiencing this issue, now I know I'm not alone.  What specific Arm cpu do you have?

## ElectroFlux-SS | 2020-12-03T04:37:55+00:00
I was getting the same issue with the Cortex-A53 (Pi3B+) as well as the Cortex-A72 (Pi4B+).

After reading the last post I just tried recompiled with v6.2.3 and also went back to v5.5.0, but still had same error with "hw-aes": true in the config (using the Cortex-A72 with 8GB of RAM).

## xmrig | 2020-12-03T05:10:50+00:00
@ElectroFlux-SS Raspberry PI (all models) does not support hardware AES.

## ElectroFlux-SS | 2020-12-03T05:37:54+00:00
Thanks xmrig - That's why I run with hw-aes = false; LOL

But it looks like other ARM processors like the Cortex-A57 on the ROCK boards have similar results.  I had a ROCK RK board with the A57 a few months ago (running Armbian also) and had the same issues/errors with the hw-aes on. 

## Kaal1990 | 2021-01-10T09:27:27+00:00
Hey, 

i try yesterday to run a Miner too on my raspberry Pi 4 4GB.

But every time i try to run the rx/0 algo, the miner crash whit Illegal Instruction. (Same as above)
I try to disable AES in the config, but that doesnt help.

While make, i get a "Error" message, but dont know if it is a error or just a information:

> [ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
> /home/pi/xmrig/src/crypto/randomx/aes_hash.cpp: In lambda function:
> /home/pi/xmrig/src/crypto/randomx/aes_hash.cpp:396:62: warning: comparison of integer expressions of different signedness: ‘uint64_t’ {aka ‘long unsigned int’} and ‘const int’ [-Wsign-compare]
>            } while (xmrig::Chrono::highResolutionMSecs() - t1 < test_length_ms);
>                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~
> 

I install the Miner like this way

>  sudo apt-get install -y raspbian-nspawn-64
>  ds64-shell
>  sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
>  git clone https://github.com/xmrig/xmrig.git
>  cd xmrig
>  mkdir build
>  cd build
>  cmake ..
>  make

I try to use a newer compiler (10.1.0) too but it doenst help.

Hope that anybody can help me :)

## BoneGoat | 2021-02-01T13:51:04+00:00
v6.2.3 works on RockPi4 while v6.8.0 crashes with Illegal instruction. Will test other versions in between to try and pinpoint where it breaks.

 * ABOUT        XMRig/6.2.3 gcc/8.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARMv8 (2) x64 AES
                L2:0.0 MB L3:0.0 MB 6C/6T NUMA:1
 * MEMORY       2.6/3.7 GB (70%)
 * DONATE       100%
 * POOL #1      solo-xmr.2miners.com:4444 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-02-01 14:40:22.849]  net      use pool solo-xmr.2miners.com:4444  51.89.96.41
[2021-02-01 14:40:22.849]  net      new job from solo-xmr.2miners.com:4444 diff 240009 algo rx/0 height 2287332
[2021-02-01 14:40:22.849]  cpu      use argon2 implementation default
[2021-02-01 14:40:22.850]  randomx  init dataset algo rx/0 (6 threads) seed d432f49920515087...
[2021-02-01 14:40:23.696]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (846 ms)
[2021-02-01 14:40:52.380]  randomx  dataset ready (28684 ms)
[2021-02-01 14:40:52.380]  cpu      use profile  rx  (6 threads) scratchpad 2048 KB
[2021-02-01 14:40:52.484]  cpu      READY threads 6/6 (6) huge pages 100% 6/6 memory 12288 KB (104 ms)
[2021-02-01 14:41:52.449]  miner    speed 10s/60s/15m 157.9 125.2 n/a H/s max 161.6 H/s

## SChernykh | 2021-02-01T16:10:42+00:00
https://github.com/xmrig/xmrig/pull/2075 should fix it

## BoneGoat | 2021-02-01T18:35:58+00:00
Nope, sorry. I merged your PR before compiling of course. Still on RockPi4.

[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
 * ABOUT        XMRig/6.8.1-dev gcc/8.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A53 (2) 64-bit AES
                L2:0.0 MB L3:0.0 MB 6C/6T NUMA:1
 * MEMORY       3.0/3.7 GB (81%)
 * DONATE       100%
 * POOL #1      solo-xmr.2miners.com:4444 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
[New Thread 0x7fb5a371d0 (LWP 3663)]
 * OPENCL       disabled
 * CUDA         disabled
[New Thread 0x7fb52361d0 (LWP 3664)]
[New Thread 0x7fb4a351d0 (LWP 3665)]
[New Thread 0x7fb42341d0 (LWP 3666)]
[New Thread 0x7fb3a331d0 (LWP 3667)]
[2021-02-01 19:28:31.213]  net      use pool solo-xmr.2miners.com:4444  51.89.96.41
[2021-02-01 19:28:31.214]  net      new job from solo-xmr.2miners.com:4444 diff 240009 algo rx/0 height 2287473
[2021-02-01 19:28:31.214]  cpu      use argon2 implementation default
[2021-02-01 19:28:31.214]  randomx  init dataset algo rx/0 (6 threads) seed d432f49920515087...
[2021-02-01 19:28:32.063]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (848 ms)
[New Thread 0x7fb31801d0 (LWP 3668)]
[New Thread 0x7fb297f1d0 (LWP 3669)]
[New Thread 0x7fb217e1d0 (LWP 3670)]
[New Thread 0x7fb197d1d0 (LWP 3671)]
[New Thread 0x7fb117c1d0 (LWP 3672)]
[New Thread 0x7fb097b1d0 (LWP 3673)]
[Thread 0x7fb31801d0 (LWP 3668) exited]
[Thread 0x7fb297f1d0 (LWP 3669) exited]
[Thread 0x7fb097b1d0 (LWP 3673) exited]
[Thread 0x7fb217e1d0 (LWP 3670) exited]
[Thread 0x7fb117c1d0 (LWP 3672) exited]
[2021-02-01 19:28:59.034]  randomx  dataset ready (26972 ms)
[Thread 0x7fb197d1d0 (LWP 3671) exited]
[New Thread 0x7fb097b1d0 (LWP 3674)]
[New Thread 0x7fb117c1d0 (LWP 3675)]
[New Thread 0x7fb197d1d0 (LWP 3676)]
[New Thread 0x7fb217e1d0 (LWP 3677)]
[New Thread 0x7fb2f801d0 (LWP 3678)]
[New Thread 0x7f9bfff1d0 (LWP 3679)]
[2021-02-01 19:28:59.066]  cpu      READY threads 6/6 (6) huge pages 100% 6/6 memory 12288 KB (31 ms)

Thread 17 "xmrig" received signal SIGILL, Illegal instruction.
[Switching to Thread 0x7fb2f801d0 (LWP 3678)]
0x0000007f9b5ff000 in ?? ()



0x7f9b5ff000    sub    sp, sp, #0xc0                                                                                                                                                                   │
   │0x7f9b5ff004    stp    x16, x17, [sp]                                                                                                                                                                  │
   │0x7f9b5ff008    stp    x18, x19, [sp, #16]                                                                                                                                                             │
   │0x7f9b5ff00c    stp    x20, x21, [sp, #32]                                                                                                                                                             │
   │0x7f9b5ff010    stp    x22, x23, [sp, #48]                                                                                                                                                             │
   │0x7f9b5ff014    stp    x24, x25, [sp, #64]                                                                                                                                                             │
   │0x7f9b5ff018    stp    x26, x27, [sp, #80]                                                                                                                                                             │
   │0x7f9b5ff01c    stp    x28, x29, [sp, #96]                                                                                                                                                             │
   │0x7f9b5ff020    stp    x8, x30, [sp, #112]                                                                                                                                                             │
   │0x7f9b5ff024    stp    d8, d9, [sp, #128]                                                                                                                                                              │
   │0x7f9b5ff028    stp    d10, d11, [sp, #144]                                                                                                                                                            │
   │0x7f9b5ff02c    stp    d12, d13, [sp, #160]                                                                                                                                                            │
   │0x7f9b5ff030    stp    d14, d15, [sp, #176]                                                                                                                                                            │
   │0x7f9b5ff034    mov    x4, xzr                                                                                                                                                                         │
   │0x7f9b5ff038    mov    x5, xzr                                                                                                                                                                         │
   │0x7f9b5ff03c    mov    x6, xzr                                                                                                                                                                         │
   │0x7f9b5ff040    mov    x7, xzr                                                                                                                                                                         │
   │0x7f9b5ff044    mov    x12, xzr                                                                                                                                                                        │
   │0x7f9b5ff048    mov    x13, xzr                                                                                                                                                                        │
   │0x7f9b5ff04c    mov    x14, xzr                                                                                                                                                                        │
   │0x7f9b5ff050    mov    x15, xzr                                                                                                                                                                        │
   │0x7f9b5ff054    ldp    x9, x1, [x1]                                                                                                                                                                    │
   │0x7f9b5ff058    mov    x10, x9                                                                                                                                                                         │
   │0x7f9b5ff05c    ldp    q24, q25, [x0, #192]                                                                                                                                                            │
   │0x7f9b5ff060    ldp    q26, q27, [x0, #224]                                                                                                                                                            │
   │0x7f9b5ff064    mov    x16, #0xffffffffffffff          // #72057594037927935                                                                                                                           │
   │0x7f9b5ff068    mov    v29.d[0], x16                                                                                                                                                                   │
   │0x7f9b5ff06c    mov    v29.d[1], x16                                                                                                                                                                   │
   │0x7f9b5ff070    ldr    q30, [x0, #64]                                                                                                                                                                  │
   │0x7f9b5ff074    mov    x16, #0x80f0000000000000        // #-9155818042444218368                                                                                                                        │
   │0x7f9b5ff078    mov    v31.d[0], x16
0x7f9b5ff07c    mov    v31.d[1], x16                                                                                                                                                                   │
   │0x7f9b5ff080    mrs    x8, fpcr                                                                                                                                                                        │
   │0x7f9b5ff084    rbit   x8, x8                                                                                                                                                                          │
   │0x7f9b5ff088    str    x0, [sp, #-16]!                                                                                                                                                                 │
   │0x7f9b5ff08c    ldr    x0, 0x7f9b6031e4                                                                                                                                                                │
   │0x7f9b5ff090    ldr    x11, 0x7f9b6031ec                                                                                                                                                               │
   │0x7f9b5ff094    ldr    x20, 0x7f9b6031f4                                                                                                                                                               │
   │0x7f9b5ff098    ldr    x21, 0x7f9b6031fc                                                                                                                                                               │
   │0x7f9b5ff09c    ldr    x22, 0x7f9b603204                                                                                                                                                               │
   │0x7f9b5ff0a0    ldr    x23, 0x7f9b60320c                                                                                                                                                               │
   │0x7f9b5ff0a4    ldr    x24, 0x7f9b603214                                                                                                                                                               │
   │0x7f9b5ff0a8    ldr    x25, 0x7f9b60321c                                                                                                                                                               │
   │0x7f9b5ff0ac    ldr    x26, 0x7f9b603224                                                                                                                                                               │
   │0x7f9b5ff0b0    ldr    x27, 0x7f9b60322c                                                                                                                                                               │
   │0x7f9b5ff0b4    ldr    x28, 0x7f9b603234                                                                                                                                                               │
   │0x7f9b5ff0b8    ldr    x29, 0x7f9b60323c                                                                                                                                                               │
   │0x7f9b5ff0bc    ldr    x30, 0x7f9b603244                                                                                                                                                               │
   │0x7f9b5ff0c0    ldr    q0, 0x7f9b60324c                                                                                                                                                                │
   │0x7f9b5ff0c4    ldr    q1, 0x7f9b60325c                                                                                                                                                                │
   │0x7f9b5ff0c8    ldr    q2, 0x7f9b60326c                                                                                                                                                                │
   │0x7f9b5ff0cc    ldr    q3, 0x7f9b60327c                                                                                                                                                                │
   │0x7f9b5ff0d0    ldr    q4, 0x7f9b60328c                                                                                                                                                                │
   │0x7f9b5ff0d4    ldr    q5, 0x7f9b60329c                                                                                                                                                                │
   │0x7f9b5ff0d8    ldr    q6, 0x7f9b6032ac                                                                                                                                                                │
   │0x7f9b5ff0dc    ldr    q7, 0x7f9b6032bc                                                                                                                                                                │
   │0x7f9b5ff0e0    ldr    q8, 0x7f9b6032cc                                                                                                                                                                │
   │0x7f9b5ff0e4    ldr    q9, 0x7f9b6032dc                                                                                                                                                                │
   │0x7f9b5ff0e8    ldr    q10, 0x7f9b6032ec                                                                                                                                                               │
   │0x7f9b5ff0ec    ldr    q11, 0x7f9b6032fc                                                                                                                                                               │
   │0x7f9b5ff0f0    ldr    q12, 0x7f9b60330c

## SChernykh | 2021-02-01T18:38:50+00:00
Are you sure you merged it and recompiled everything? It fixed the crashes completely on my phone and it was an obvious bug in the code.

## SChernykh | 2021-02-01T18:40:40+00:00
I take that back, just tested it again and it crashed. Interesting.

## SChernykh | 2021-02-01T18:43:22+00:00
It crashes in ~3 out of 4 cases when I launch it, but when it starts without crash, it keeps mining. @BoneGoat Can you test and confirm?

## BoneGoat | 2021-02-01T18:43:34+00:00
Yup, I can get it to run maybe once in 20 tries. It's... interesting...

## SChernykh | 2021-02-01T18:46:42+00:00
It's definitely related to instruction cache flushing because illegal instruction error means CPU tried to execute some garbage, but debugger shows valid instruction. I'll keep looking into it.

## BoneGoat | 2021-02-01T18:57:55+00:00
OK, great! On my end, v6.4.0 works and v6.5.0 does not.

## SChernykh | 2021-02-01T21:58:54+00:00
Fixed with #2077 

## BoneGoat | 2021-02-02T07:01:35+00:00
Confirmed working on RockPi4. Great work!

# Action History
- Created by: turtleminor13 | 2020-10-26T06:24:52+00:00
- Closed at: 2021-04-12T14:43:57+00:00
