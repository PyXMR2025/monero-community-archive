---
title: Segmentation Fault in fillAes1Rx4 while running on x86
source_url: https://github.com/xmrig/xmrig/issues/1867
author: playern1
assignees: []
labels:
- bug
created_at: '2020-10-05T16:17:45+00:00'
updated_at: '2021-04-12T14:47:24+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:47:24+00:00'
---

# Original Description
xmrig was built on "Linux ubuntu 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:01:15 UTC 2019 i686 i686 i686 GNU/Linux" successfully according to instructions from https://xmrig.com/docs/miner/build/ubuntu section "Advanced build"

After running the binary I get Segmentation Fault in fillAes1Rx4 immediately

$ file ./xmrig32
./xmrig32: ELF 32-bit LSB executable, Intel 80386, version 1 (GNU/Linux), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32

$ gdb ./xmrig32
(gdb) r
Starting program: xmrig32

ABOUT XMRig/6.3.5 gcc/5.4.0
LIBS libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
HUGE PAGES supported
1GB PAGES unavailable
CPU Intel(R) Xeon(R) CPU E5-2650L v4 @ 1.70GHz (1) -x64 AES
L2:0.2 MB L3:35.0 MB 1C/1T NUMA:1
MEMORY 0.8/1.0 GB (79%)
DONATE 1%
POOL #1 pool.minexmr.com:443 algo auto
COMMANDS hashrate, pause, resume, results, connection
[New Thread 0xf7d8cb40 (LWP 16518)]
OPENCL disabled
CUDA disabled
[New Thread 0xf758bb40 (LWP 16519)]
[New Thread 0xf6d8ab40 (LWP 16520)]
[New Thread 0xf6589b40 (LWP 16521)]
[New Thread 0xf5d88b40 (LWP 16522)]
[2020-10-05 17:58:26.029] net use pool pool.minexmr.com:443 TLSv1.3 88.99.193.240
[2020-10-05 17:58:26.030] net new job from pool.minexmr.com:443 diff 175004 algo rx/0 height 2201739
[2020-10-05 17:58:26.030] cpu use argon2 implementation default
[2020-10-05 17:58:26.030] randomx init dataset algo rx/0 (1 threads) seed aeb044aa31eab166...
[2020-10-05 17:58:26.030] randomx not enough memory for RandomX dataset
[2020-10-05 17:58:26.037] randomx failed to allocate RandomX dataset, switching to slow mode (7 ms)
[2020-10-05 17:58:29.636] randomx dataset ready (3597 ms)
[2020-10-05 17:58:29.641] cpu use profile rx (1 thread) scratchpad 2048 KB
[New Thread 0xe51feb40 (LWP 16523)]
[2020-10-05 17:58:29.660] cpu READY threads 1/1 (1) huge pages 100% 1/1 memory 2048 KB (19 ms)
Thread 7 "xmrig32" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0xe51feb40 (LWP 16523)]
0x08324d80 in void fillAes1Rx4<0>(void*, unsigned int, void*) ()
(gdb) bt
#0 0x08324d80 in void fillAes1Rx4<0>(void*, unsigned int, void*) ()
#1 0x083325dc in randomx::VmBase<0>::initScratchpad(void*) ()
#2 0x081c0599 in xmrig::CpuWorker<1u>::start() ()
#3 0x081b05e8 in xmrig::Workersxmrig::CpuLaunchData::onReady(void*) ()
#4 0x0858d4de in ?? ()
#5 0xf7fad26a in start_thread (arg=0xe51feb40) at pthread_create.c:333
#6 0xf7e7550e in clone () from /lib32/libc.so.6
(gdb) c
Continuing.
[Thread 0xe51feb40 (LWP 16523) exited]
[Thread 0xf5d88b40 (LWP 16522) exited]
[Thread 0xf6589b40 (LWP 16521) exited]
[Thread 0xf6d8ab40 (LWP 16520) exited]
[Thread 0xf758bb40 (LWP 16519) exited]
[Thread 0xf7d8e700 (LWP 16514) exited]

Program terminated with signal SIGSEGV, Segmentation fault.

# Discussion History
# Action History
- Created by: playern1 | 2020-10-05T16:17:45+00:00
- Closed at: 2021-04-12T14:47:24+00:00
