---
title: Bus error on armv7 device
source_url: https://github.com/xmrig/xmrig/issues/1537
author: DoBi
assignees: []
labels: []
created_at: '2020-02-05T12:34:26+00:00'
updated_at: '2020-04-12T17:22:46+00:00'
type: issue
status: closed
closed_at: '2020-04-12T17:22:46+00:00'
---

# Original Description
**Describe the bug**
I want to use xmrig on a BananaPi M2U Berry. I compiled it there and started it afterwards but it stops every time after receiving a job from the pool. I've tried different algorithms: cn/half, cn/r, rx/0 and others, but every time it is crashed.

**To Reproduce**
Start xmrig and receive a job from the pool

**Expected behavior**
After receiving the job, xmrig should start mining instead of crashing

**Required data**
 - Miner log: 
```
 * ABOUT        XMRig/5.5.3 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARMv7 (1) -x64 -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       0.9/1.0 GB (96%)
 * DONATE       5%
 * POOL #1      stratum+tcp://gulf.moneroocean.stream:80 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2020-02-05 13:30:33.775]  net  use pool gulf.moneroocean.stream:80  116.203.73.240
[2020-02-05 13:30:33.776]  net  new job from gulf.moneroocean.stream:80 diff 118 algo cn/half height 897886
[2020-02-05 13:30:33.776]  cpu  use profile  cn  (4 threads) scratchpad 2048 KB
Bus error
```
 - Config file or command line (without wallets): 
`xmrig -o stratum+tcp://gulf.moneroocean.stream:80 -u <...> -p "<..>~cn/half"`
 - OS: Linux Armbian Buster (based on Debian)
 - gdb log:
```
Thread 7 "xmrig" received signal SIGBUS, Bus error.
[Switching to Thread 0xb41ff450 (LWP 20429)]
0x005ffdae in xmrig::CpuWorker<1u>::CpuWorker (this=0xb38005b8, id=0, data=...)
    at /home/dominik/xmrig/src/backend/cpu/CpuWorker.cpp:64
64	    m_ctx()
(gdb) bt
#0  0x005ffdae in xmrig::CpuWorker<1u>::CpuWorker (this=0xb38005b8, id=0, 
    data=...) at /home/dominik/xmrig/src/backend/cpu/CpuWorker.cpp:64
#1  0x005f60de in xmrig::Workers<xmrig::CpuLaunchData>::create (
    handle=0x8db370) at /home/dominik/xmrig/src/backend/common/Workers.cpp:194
#2  0x005f67ce in xmrig::Workers<xmrig::CpuLaunchData>::onReady (arg=0x8db370)
    at /home/dominik/xmrig/src/backend/common/Workers.cpp:167
#3  0x005f8f10 in std::__invoke_impl<void, void (*)(void*), xmrig::Thread<xmrig::CpuLaunchData>*> (
    __f=@0x8f0880: 0x5f67bd <xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*)>, __args#0=@0x8f087c: 0x8db370) at /usr/include/c++/8/bits/invoke.h:60
#4  0x005f8504 in std::__invoke<void (*)(void*), xmrig::Thread<xmrig::CpuLaunchData>*> (
    __fn=@0x8f0880: 0x5f67bd <xmrig::Workers<xmrig::CpuLaunchData>::onReady(void*)>, __args#0=@0x8f087c: 0x8db370) at /usr/include/c++/8/bits/invoke.h:95
#5  0x005fafc0 in std::thread::_Invoker<std::tuple<void (*)(void*), xmrig::Thread<xmrig::CpuLaunchData>*> >::_M_invoke<0u, 1u> (this=0x8f087c)
    at /usr/include/c++/8/thread:244
#6  0x005faf08 in std::thread::_Invoker<std::tuple<void (*)(void*), xmrig::Thread<xmrig::CpuLaunchData>*> >::operator() (this=0x8f087c)
    at /usr/include/c++/8/thread:253
#7  0x005faec4 in std::thread::_State_impl<std::thread::_Invoker<std::tuple<void (*)(void*), xmrig::Thread<xmrig::CpuLaunchData>*> > >::_M_run (this=0x8f0878)
    at /usr/include/c++/8/thread:196
```
 - `cat /proc/cpuinfo`:
```
processor	: 0
model name	: ARMv7 Processor rev 5 (v7l)
BogoMIPS	: 48.00
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 5

processor	: 1
model name	: ARMv7 Processor rev 5 (v7l)
BogoMIPS	: 48.00
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 5

processor	: 2
model name	: ARMv7 Processor rev 5 (v7l)
BogoMIPS	: 48.00
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 5

processor	: 3
model name	: ARMv7 Processor rev 5 (v7l)
BogoMIPS	: 48.00
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xc07
CPU revision	: 5

Hardware	: Allwinner sun8i Family
Revision	: 0000
Serial		: 165541532b7ec45a
```

**Additional context**
I updated the Armbian version of the BananaPi to Buster yesterday. Before the update xmrig works fine, but now the error appears. So there are no hardware changes since then.

# Discussion History
## SChernykh | 2020-02-05T15:41:50+00:00
`* MEMORY       0.9/1.0 GB (96%)`
You don't have enough free memory

## DoBi | 2020-02-05T16:05:43+00:00
> `* MEMORY 0.9/1.0 GB (96%)`
> You don't have enough free memory

Thats what I also thought, but why did it worked on the same hardware a day before? There was not more memory.. And why is the swap memory not included? I've 2GB of swap active.

## Spudz76 | 2020-03-23T06:34:03+00:00
mining won't use swap, scratchpads are locked into memory unswappable
maybe setting sysctl `vm.swappiness` to something high will shove more OS into swap for you
but lots of OS doesn't want to be swapped out or is in use too often

No idea how it ever worked unless some other process was using less before, or you had less threads and autoconf turned them back up

## DoBi | 2020-04-12T17:22:46+00:00
Thank you for your explanation @Spudz76.

I reinstalled the current version of armbian today and everything works fine again. So I don't know, what was the problem, but it is fixed now.

# Action History
- Created by: DoBi | 2020-02-05T12:34:26+00:00
- Closed at: 2020-04-12T17:22:46+00:00
