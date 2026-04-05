---
title: SegFault after accepting first block
source_url: https://github.com/xmrig/xmrig/issues/696
author: ghost
assignees: []
labels: []
created_at: '2018-06-18T02:47:40+00:00'
updated_at: '2018-11-05T06:59:00+00:00'
type: issue
status: closed
closed_at: '2018-11-05T06:59:00+00:00'
---

# Original Description
Hi,

I was able to successfully compile on a i686 with no severe errors. When I run ./xmrig --help it shows the help and exits.

However when I run it and connect to a pool, it seems to connect, accept a share, and then die immediately:
`root@ps0:~/MINERS/xmrig# ./xmrig -a cryptonight -o 192.168.1.2:3333 -O 486hiBt6zu5fJ9RvuHapFnJHPZ4zqtAChYvmVrs4NiLM1fonXAyHcwPhhqaZZwkTfXGNqwbKaLWag8uVBbGAwuMCKEEDDpg:ps0
 * VERSIONS     XMRig/2.6.3 libuv/1.9.0 gcc/4.9.2
 * CPU          Mobile Genuine Intel(R) processor       1100MHz (1) -x64 -AES-NI
 * CPU L2/L3    1.0 MB/0.0 MB
 * THREADS      1, cryptonight, av=0, donate=1%
 * POOL #1      192.168.1.2:3333 variant 1
 * COMMANDS     hashrate, pause, resume
[2018-06-17 22:41:38] use pool 192.168.1.2:3333 192.168.1.2
[2018-06-17 22:41:38] new job from 192.168.1.2:3333 diff 666 algo cn/1
[2018-06-17 22:41:39] READY (CPU) threads 1(1) huge pages 1/1 100% memory 2.0 MB
Segmentation fault`

There are only two suspicions I have...

1) It says L3 cache is 0MB and I wonder if this is why? Does it require at least some space in L3 as well?
2) Maybe something with the algorithm is causing it to segfault.

`Linux ps0 3.16.0-5-586 #1 Debian 3.16.51-3+deb8u1 (2018-01-08) i686 GNU/Linux`

`xmrig: ELF 32-bit LSB executable, Intel 80386, version 1 (GNU/Linux), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=b7636c964f192a10c3fff0fbefca162b90a3a5a6, stripped`

Does anyone have any idea why it segfaults after accepting its first block?

Thanks for your help :)

# Discussion History
## ghost | 2018-06-18T05:25:51+00:00
So I fixed it...

For the record, I was running Debian Jessie on those servers, so I upgraded, then changed sources.list to stretch and upgraded the system. After upgrade the package compiled and ran no problems!

Might I suggest fixing this jessie-and-backwards compatability issue for ARM and those older machines that can't run the latest Debian?

This ticket will be left open until response, feel free to respond and close. Thanks

## xmrig | 2018-06-18T06:27:19+00:00
1. Detected cache size only used to determine how many threads should run in automatic mode.
2. Without call stack hard to say what was happen.

## ghost | 2018-06-24T01:02:45+00:00
I actually found out some of the servers still do this... 

I did some researching and it turns out these machines are i586 (I think) and there is an issue where some of them have the CMOV instruction set, and some do not. My suspicion is these do not have CMOV so I have to somehow override the CMAKE instructions to force the compiler to use the right instruction set to compile.

Apparently it is a known issue with compiling anything on the machines without this instruction set. Unless the author of a program makes a fix/workaround in the CMAKE files, it will never be fixed because of the age of the architecture.

Once I figure out the fix I will notify you of the fix :)

## xmrig | 2018-06-25T10:16:20+00:00
If miner somehow use instruction not supported by host CPU error should looks like: `Illegal instruction (core dumped) `.

## ghost | 2018-06-26T13:49:02+00:00
I manually set the threads to 1, so that can't be the problem...

GDB info:
> root@ps3:~/MINERS/xmrig# gdb ./xmrig
> GNU gdb (Debian 7.12-6) 7.12.0.20161007-git
> Copyright (C) 2016 Free Software Foundation, Inc.
> License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
> This is free software: you are free to change and redistribute it.
> There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
> and "show warranty" for details.
> This GDB was configured as "i686-linux-gnu".
> Type "show configuration" for configuration details.
> For bug reporting instructions, please see:
> <http://www.gnu.org/software/gdb/bugs/>.
> Find the GDB manual and other documentation resources online at:
> <http://www.gnu.org/software/gdb/documentation/>.
> For help, type "help".
> Type "apropos word" to search for commands related to "word"...
> Reading symbols from ./xmrig...(no debugging symbols found)...done.
> (gdb) r
> Starting program: /root/MINERS/xmrig/xmrig 
> [Thread debugging using libthread_db enabled]
> Using host libthread_db library "/lib/i386-linux-gnu/libthread_db.so.1".
> 
> Program received signal SIGILL, Illegal instruction.
> 0x0052a59f in cpuid_identify_intel ()
> (gdb) bt
> #0  0x0052a59f in cpuid_identify_intel ()
> #1  0x00528fd4 in cpu_ident_internal ()
> #2  0x00528ff8 in cpu_identify ()
> #3  0x004fa82b in Cpu::initCommon() ()
> #4  0x004fa544 in Cpu::init() ()
> #5  0x0048c73b in xmrig::Controller::init(int, char**) ()
> #6  0x00460e2b in App::App(int, char**) ()
> #7  0x0045f474 in main ()
> (gdb) x/i 0x0052a59f
> => 0x52a59f <cpuid_identify_intel+1500>:	movq   %xmm2,0x4(%eax)
> (gdb) quit
> A debugging session is active.
> 
> 	Inferior 1 [process 3742] will be killed.
> 
> Quit anyway? (y or n) y
> 

Not sure if the movq is related to SSE... The PC reports:

> root@ps3:~/MINERS/xmrig# cat /proc/cpuinfo 
> processor	: 0
> vendor_id	: GenuineIntel
> cpu family	: 6
> model		: 11
> model name	: Mobile Intel(R) Celeron(TM) CPU          650MHz
> stepping	: 4
> cpu MHz		: 650.003
> cache size	: 256 KB
> physical id	: 0
> siblings	: 1
> core id		: 0
> cpu cores	: 1
> apicid		: 0
> initial apicid	: 0
> fdiv_bug	: no
> f00f_bug	: no
> coma_bug	: no
> fpu		: yes
> fpu_exception	: yes
> cpuid level	: 2
> wp		: yes
> flags		: fpu vme de pse tsc msr pae mce cx8 sep mtrr pge mca cmov pse36 mmx fxsr sse eagerfpu
> bugs		: cpu_meltdown spectre_v1 spectre_v2
> bogomips	: 1300.00
> clflush size	: 32
> cache_alignment	: 32
> address sizes	: 36 bits physical, 32 bits virtual
> power management:

So I apparantly do have SSE and I think movq is SSE instruction but I tried disabling it with -mno-sse but that does not work either

Any idea now why it crashes?

## xmrig | 2018-06-26T14:39:51+00:00
Mining code require SSE2, movq with xmm registers also require SSE2. Possible remove any SSE/SSE2 dependecies, but it require to rewrite mining code and other code like `cpuid_identify_intel`.
Thank you.

# Action History
- Created by: ghost | 2018-06-18T02:47:40+00:00
- Closed at: 2018-11-05T06:59:00+00:00
