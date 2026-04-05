---
title: 'warning: "can''t bind memory" seems to be OS-related.'
source_url: https://github.com/xmrig/xmrig/issues/2482
author: xq0404
assignees: []
labels: []
created_at: '2021-07-11T04:04:09+00:00'
updated_at: '2022-06-10T23:15:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There is warning: "can't bind memory" under Fedora and Ubuntu, but no problem occurs under Windows 10. So this problem seems to be OS-related. 

 msr      register values for "ryzen_17h" preset have been set successfully (4 ms)
[2021-07-10 22:01:35.357]  randomx  init datasets algo rx/0 (64 threads) seed 36e5ffbb4d64a1f3...
[2021-07-10 22:01:35.657]  randomx  #0 allocated 2080 MB huge pages 100% (300 ms)
[2021-07-10 22:01:35.954]  randomx  #2 allocated 2080 MB huge pages 100% (596 ms)
[2021-07-10 22:01:35.995]  randomx  #0 allocated  256 MB huge pages 100% +JIT (41 ms)
[2021-07-10 22:01:35.995]  randomx  -- allocated 4416 MB huge pages 100% 2208/2208 (637 ms)
[2021-07-10 22:01:37.738]  randomx  #0 dataset ready (1743 ms)
[2021-07-10 22:01:38.202]  randomx  #2 dataset ready (464 ms)
[2021-07-10 22:01:38.202]  cpu      use profile  rx  (32 threads) scratchpad 2048 KB
[2021-07-10 22:01:38.204] CPU #32 warning: "can't bind memory"
[2021-07-10 22:01:38.204] CPU #34 warning: "can't bind memory"
[2021-07-10 22:01:38.204] CPU #36 warning: "can't bind memory"
[2021-07-10 22:01:38.204] CPU #38 warning: "can't bind memory"
[2021-07-10 22:01:38.204] CPU #40 warning: "can't bind memory"
[2021-07-10 22:01:38.204] CPU #42 warning: "can't bind memory"
[2021-07-10 22:01:38.204] CPU #44 warning: "can't bind memory"
[2021-07-10 22:01:38.204] CPU #46 warning: "can't bind memory"
[2021-07-10 22:01:38.204] CPU #50 warning: "can't bind memory"
[2021-07-10 22:01:38.204] CPU #52 warning: "can't bind memory"
[2021-07-10 22:01:38.205] CPU #48 warning: "can't bind memory"
[2021-07-10 22:01:38.205] CPU #54 warning: "can't bind memory"
[2021-07-10 22:01:38.205] CPU #58 warning: "can't bind memory"
[2021-07-10 22:01:38.205] CPU #56 warning: "can't bind memory"
[2021-07-10 22:01:38.205] CPU #62 warning: "can't bind memory"
[2021-07-10 22:01:38.205] CPU #60 warning: "can't bind memory"
[2021-07-10 22:01:38.227]  cpu      READY threads 32/32 (32) huge pages 100% 32/32 memory 65536 KB (25 ms)
[2021-07-10 22:01:52.037]  cpu      accepted (1/0) diff 480045 (574 ms)

 - OS: Ubuntu ubuntu-20.04.2.0-desktop-amd64, Fedora-Workstation-Live-x86_64-34-1.2
CPU: AMD 2990WX




# Discussion History
## xq0404 | 2021-07-11T04:15:47+00:00
The following is what has happened under Windows 10.  Everything seems quite normal.
![normal win10](https://user-images.githubusercontent.com/20359673/125182562-a1c92e00-e241-11eb-986e-fe05b0882308.JPG)


## Lonnegan | 2021-07-12T09:07:49+00:00
You seem to use xmrig in a Virtual Machine. Just with Windows 10 (for testing) or as well with Linux? Perhaps that's why the system can't bind the threads because of the virtualization layer between mining software and hardware!

## xq0404 | 2021-07-13T16:03:27+00:00
> 
> 
> You seem to use xmrig in a Virtual Machine. Just with Windows 10 (for testing) or as well with Linux? Perhaps that's why the system can't bind the threads because of the virtualization layer between mining software and hardware!

No, I just had  Linux (Fedora and Ubuntu) OS booted up on a live installation USB stick, and tested. I did not install Linux on a hard disk drive.  So it's not in a Virtual Machine environment.

## Lonnegan | 2021-07-15T05:56:15+00:00
> No, I just had Linux (Fedora and Ubuntu) OS booted up on a live installation USB stick, and tested. I did not install Linux on a hard disk drive. So it's not in a Virtual Machine environment.

But xmrig recognized your system as a VM. Look at the output line 5 


## Spudz76 | 2021-07-15T08:49:31+00:00
Is the hwloc version the same between the two?

## xq0404 | 2021-07-17T14:42:41+00:00
> 
> 
> Is the hwloc version the same between the two?

For Portable Hardware Locality, I guess yes as both are booted up on the same hardware. 

## xq0404 | 2021-07-17T14:44:29+00:00
> 
> 
> > No, I just had Linux (Fedora and Ubuntu) OS booted up on a live installation USB stick, and tested. I did not install Linux on a hard disk drive. So it's not in a Virtual Machine environment.
> 
> But xmrig recognized your system as a VM. Look at the output line 5

I had Hyper-V enabled under Windows 10, which nominally also runs as a virtual machine, but xmrig has direct access to all hardware.  

## xq0404 | 2021-07-17T16:28:19+00:00
This is what has happend under pop-os:
 
root@pop-os:/home/pop-os# '/home/pop-os/Downloads/xmrig-6.13.1/xmrig' 
 * ABOUT        XMRig/6.13.1 gcc/9.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen Threadripper 2990WX 32-Core Processor (1) 64-bit AES
                L2:16.0 MB L3:64.0 MB 32C/64T NUMA:4
 * MEMORY       4.7/31.3 GB (15%)
                DIMM 0: <empty>
                DIMM_A1: 8 GB DDR4 @ 2933 MHz KHX3200C18D4/8G     
                DIMM 0: <empty>
                DIMM_B1: 8 GB DDR4 @ 2933 MHz KHX3200C18D4/8G     
                DIMM 0: <empty>
                DIMM_C1: 8 GB DDR4 @ 2933 MHz KHX3200C18D4/8G     
                DIMM 0: <empty>
                DIMM_D1: 8 GB DDR4 @ 2933 MHz KHX3200C18D4/8G     
MOTHERBOARD  Gigabyte Technology Co., Ltd. - X399 AORUS PRO-CF


## xq0404 | 2021-07-19T02:49:09+00:00
Instead of booting up a live USB stick, I just installed a Ubuntu OS on a 64 USB flash drive. The same "can't bind memory" occurred. 

## xq0404 | 2021-07-19T04:36:06+00:00
By the way, I have experimented with Hyper-V both enabled and disabled under Windows 10,  and XMRig has always been running properly without any bug prompts. 

## Spudz76 | 2021-07-19T18:14:34+00:00
Probably needs all 8 sticks or not all nodes get their own RAM, which will anger hwloc pinning cores to RAM they don't have.

## Lonnegan | 2021-07-20T05:58:35+00:00
@Spudz76 Threadripper 2990WX has only 4 DRAM channels, not 8. That's the difference to the EPYCs of the same generation. 2 of the 4 dies on the package don't have their own memory controller. Perhaps that's the cause of the issue. But then, all 1st gen Threadrippers would have this problem!

## xq0404 | 2021-07-20T12:37:16+00:00
> 
> 
> @Spudz76 Threadripper 2990WX has only 4 DRAM channels, not 8. That's the difference to the EPYCs of the same generation. 2 of the 4 dies on the package don't have their own memory controller. Perhaps that's the cause of the issue. But then, all 1st gen Threadrippers would have this problem!

You are right. This is a bug for the Linux version of XMRig.  So I appeal for the developers to correct this problem, even if only for 2990WX and other 1st gen Threadrippers. 

## Spudz76 | 2021-07-20T19:31:00+00:00
What does your `hwloc-ls` look like?

## xq0404 | 2021-07-21T00:45:30+00:00
> hwloc-ls

* LIBS   libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1

## Spudz76 | 2021-07-21T14:56:41+00:00
hwloc-ls is a command.  Mostly looking for the NUMANode entries.

```
root@some-rig:~# hwloc-ls | grep NUMANode
    NUMANode L#0 (P#0 24GB)
    NUMANode L#1 (P#1 24GB)
```

## ThrudTheBarbarian | 2021-07-29T02:48:30+00:00
I'm getting the same thing with a 2990WX. 

```
root@xanadu:/xmrig-6.13.1# ./xmrig -o us-west.minexmr.com:443 -k --tls --rig-id Xanadu --randomx-1gb-pages
 * ABOUT        XMRig/6.13.1 gcc/9.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen Threadripper 2990WX 32-Core Processor (1) 64-bit AES
                L2:16.0 MB L3:64.0 MB 32C/64T NUMA:4
 * MEMORY       99.9/125.8 GB (79%)
                DIMM_A0: 16 GB DDR4 @ 2133 MHz F4-2800C15-16GVR
                DIMM_A1: 16 GB DDR4 @ 2133 MHz F4-2800C15-16GVR
                DIMM_B0: 16 GB DDR4 @ 2133 MHz F4-2666C15-16GVR
                DIMM_B1: 16 GB DDR4 @ 2133 MHz F4-2666C15-16GVR
                DIMM_C0: 16 GB DDR4 @ 2133 MHz F4-2800C15-16GVR
                DIMM_C1: 16 GB DDR4 @ 2133 MHz F4-2666C15-16GVR
                DIMM_D0: 16 GB DDR4 @ 2133 MHz F4-2800C15-16GVR
                DIMM_D1: 16 GB DDR4 @ 2133 MHz F4-2666C15-16GVR
 * MOTHERBOARD  ASRock - X399 Professional Gaming
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      us-west.minexmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-07-28 18:32:44.735]  net      use pool us-west.minexmr.com:443 TLSv1.3 51.81.151.235
[2021-07-28 18:32:44.735]  net      fingerprint (SHA-256): "f8cb85d6dc856748d376b48e6b87f90900b3f683fe505ef59de570296761d14b"
[2021-07-28 18:32:44.735]  net      new job from us-west.minexmr.com:443 diff 175004 algo rx/0 height 2415047
[2021-07-28 18:32:44.735]  cpu      use argon2 implementation AVX2
[2021-07-28 18:32:44.742]  msr      register values for "ryzen_17h" preset have been set successfully (7 ms)
[2021-07-28 18:32:44.742]  randomx  init datasets algo rx/0 (64 threads) seed 7a73dd52a187a51a...
[2021-07-28 18:32:45.366]  randomx  failed to allocate RandomX dataset using 1GB pages
[2021-07-28 18:32:45.366]  randomx  #0 allocated 2080 MB huge pages 100% (623 ms)
[2021-07-28 18:32:45.366]  randomx  failed to allocate RandomX dataset using 1GB pages
[2021-07-28 18:32:45.366]  randomx  #2 allocated 2080 MB huge pages 100% (623 ms)
[2021-07-28 18:32:45.401]  randomx  #0 allocated  256 MB huge pages 100% +JIT (36 ms)
[2021-07-28 18:32:45.401]  randomx  -- allocated 4416 MB huge pages 100% 2208/2208 (659 ms)
[2021-07-28 18:32:47.126]  randomx  #0 dataset ready (1724 ms)
[2021-07-28 18:32:47.366]  randomx  #2 dataset ready (240 ms)
[2021-07-28 18:32:47.366]  cpu      use profile  rx  (32 threads) scratchpad 2048 KB
[2021-07-28 18:32:47.368] CPU #16 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #17 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #18 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #19 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #20 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #21 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #22 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #23 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #24 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #25 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #26 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #27 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #28 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #29 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #30 warning: "can't bind memory"
[2021-07-28 18:32:47.368] CPU #31 warning: "can't bind memory"
```

My hwloc-ls looks like:
```
@xanadu:~$ hwloc-ls  | grep NUMANode
    NUMANode L#0 (P#0 63GB)
    NUMANode L#1 (P#2 63GB)
```

It's clearly not loading the machine down because I can see the temp's running at ~50% of what they run at when I'm really pushing it, and the CPU's are only being half-used:
![Screen Shot 2021-07-28 at 7 50 41 PM](https://user-images.githubusercontent.com/22286193/127424103-d42ee1e2-1bdd-4c39-9d3d-176ad252206c.png)

It may be that the two non-memory-channel dies can't be used, I don't know, but I *thought* they would transparently push requests through the other two dies which *do* have memory channels...

Kind of weird that a 128GB machine can't allocate 1GB pages, as well, but mine not to wonder why :)

## colinxs | 2021-08-18T12:37:48+00:00
finally found someone else having this issue, unfortunately it appears there's no resolution other than "download more ram" :).

Would setting the topology/thread affinities to ignore nodes with attached memory work as a stopgap?

## ThrudTheBarbarian | 2021-08-18T14:22:52+00:00
I gave up :( 

## NVMDSTEVil | 2022-06-05T04:24:45+00:00
bump, issue still exists in 6.17.0

2990wx, 8x8GB

## Spudz76 | 2022-06-05T08:25:02+00:00
I did begin seeing can't bind errors on Intel systems but killing it and running again it just works.

## xq0404 | 2022-06-06T01:20:32+00:00
> I did begin seeing can't bind errors on Intel systems but killing it and running again it just works.

So it's likely an OS-related bug.

## Spudz76 | 2022-06-06T08:07:16+00:00
Yes or hwloc newer than 2.4.x or something (not sure if 2.3.x->2.4.x deps version bump was about when it began)

Things definitely need 2.x.x or GhostRider breaks, so maybe even 2.1.x or 2.2.x would work better.

## Spudz76 | 2022-06-09T08:19:04+00:00
Added some better failure messaging since the call could fail in a few ways.  The hwloc object lookup works but then the actual binding fails.  It actually did it for me the second time I restarted it, luck?  As usual a third relaunch it worked fine like the first.

```
[2022-06-09 01:14:09.558]  randomx  #1 skipped (can't bind memory: cpu->membind() failed)
```

## lexo-mfleuti | 2022-06-10T16:23:04+00:00
I fiddled with this now for several hours and the solution is most probably not software related. I documented it here:
https://www.lexo.ch/blog/2022/06/solved-xmrig-cpu-xx-warning-cant-bind-memory-xmrig-does-not-run-on-all-cpu-cores/

Hope this helps!

## Spudz76 | 2022-06-10T21:18:46+00:00
@lexo-mfleuti Thanks for that, all very true and could be the issue for some here.  However the other half of the issue happens regardless of physical memory locations (one of my systems has every slot full, still occasionally fails but works the next run).

## NVMDSTEVil | 2022-06-10T23:06:48+00:00
@lexo-mfleuti WX series Threadrippers have 2 CCD/CCX's not connected directly to memory, they must cross through other CCD/CCX's before they can be seen by the memory controller,

I think the problem is that for some of us XMRIG is miss-identifying useable CPU cores due to this.  The memory latency is higher due to the way the CPU's are made but the cores are still useable.

This increased memory latency might be why XMRIG can be re-started and the next time it works fine for some.

As a side-note, I have been able to replicate a similar issue using CPUMiner for Raptoreum.  Sometimes when I perform a tune_config it will disable half the true cores and performance will reflect that (~2.5-3.3Kh average 24 hours).  With a "good" tune that all the cores stayed enabled the performance is approximately what it should be (5Kh average over last 6 days).  The old Threadripper 1950x I had did 2.6-2.7Kh average per 24 hours so this is probably fairly close to correct.

BTW I run with SMT disabled and memory in Channel interleave mode to force NUMA nodes to enable and optimize memory access latency as best as possible.  I have 8x8GB dual rank Samsung E-Die, so my slots and ranks are literally full, lol.  Something of note is that running the infinity fabric faster (3200mhz vs 3000/2400/etc) or using Channel/auto interleave mode might have an affect on XMRIG for others who cant get it to bind the memory at all.  I have done extensive testing for the interleave modes on CPUMiner for RTM and only Channel mode is able to perform well, even if I managed to get a "clean" tune on any other mode.

I just checked, hwloc 2.1.0 dfsg4 on my Mint box

![image](https://user-images.githubusercontent.com/95266968/173160846-976e22f1-4c20-49c6-a88d-97b5ad2cb05e.png)


# Action History
- Created by: xq0404 | 2021-07-11T04:04:09+00:00
