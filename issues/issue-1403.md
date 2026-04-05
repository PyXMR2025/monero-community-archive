---
title: XMRig 5.2.x Release notes
source_url: https://github.com/xmrig/xmrig/issues/1403
author: xmrig
assignees: []
labels:
- META
created_at: '2019-12-11T08:24:20+00:00'
updated_at: '2019-12-21T19:46:26+00:00'
type: issue
status: closed
closed_at: '2019-12-21T19:46:26+00:00'
---

# Original Description
**This release brings support for Linux to the next level:**
1. 1GB huge pages.
2. Automatic (with root privileges) huge pages configuration both for regular 2MB and new 1GB pages.
3. Automatic (with root privileges) Intel prefetchers configuration via MSR.

1GB huge pages disabled by default, please check new documentation https://xmrig.com/docs/miner/randomx-optimization-guide

Also Ryzen CPUs hashrate improvements and other bug fixes.

https://github.com/xmrig/xmrig/releases/tag/v5.2.1


# Discussion History
## FabioFrmg | 2019-12-11T13:09:58+00:00
Ok, new test here with a AMD Ryzen 2700 + 16GB DDR4 + Asus Prime B450M + Windows 10 PRO 64 bits lastest build with all patches and "opcache" disabled in Bios. 
Using default clocks, default timings, good power supply and temps is ok. 
The segmentation fault still happening. 
XmRig closes without error after a few time mining. 

## setuidroot | 2019-12-11T15:16:49+00:00
> Ok, new test here with a AMD Ryzen 2700 + 16GB DDR4 + Asus Prime B450M + Windows 10 PRO 64 bits lastest build with all patches and "opcache" disabled in Bios.
> Using default clocks, default timings, good power supply and temps is ok.
> The segmentation fault still happening.
> XmRig closes without error after a few time mining.

@FabioFrmg what does your config.json file look like?  Can you upload a copy of your config.json file (XMR addresses, etc redacted) and also can you get and post a screenshot (or copy and paste the terminal/"command prompt" window text output) when the miner is first starting to run?

I want to know what the miner says when it's first run (a screenshot would be great) as I'm curious what it shows your CPU to be and what it shows it's cache sizes to be.  It's possible that the CPU info given from hwloc is incorrect and due to that your config.json file's autoconfiguration could be incorrect which could cause it to crash.

I'm assuming you're mining CPU only (no OpenCL or CUDA) because if you're using GPUs that opens up a whole new world of potential issues that could cause seg faults.

Also worth noting that Windows does **not** (and probably never will) support 1GB hugepages (it rarely works well with regular 2MB hugepages, but that is 100% a Windows problem, no fault of xmrig... nothing the devs can do about Window's poor RAM memory management; I'm actually impressed they got largepages working at all in Windows 10... I couldn't even figure out how to enable it manually lol.)

Bottom line here is that Windows <s>sucks.</s> isn't the best option.  If this is a dedicated mining rig you shouldn't be running Windows on it [some AMD GPUs (like the RX 550) are an exception due to AMD's subpar drivers, specifically their Linux drivers... but NVIDIA has good Linux drivers.)  A CPU miner will always run better on Linux (IMHO and assuming proper configuration) due to many things (no forced updates that break things, better RAM memory management and control, etc.)  I don't mean to preach (well, maybe a little... gotta spread the word lol) but if this is a dedicated mining rig (or you have no direct reason to use Windows that can't be done on Ubuntu with wine or Windows 10 inside a VirtualBox VM on Linux) then you should really make the switch IMHO.  Especially since xmrig has plans to add autoconfiguration of 1GB hugepages for Linux (something that isn't possible on Windows.)  But I digress... I'm only trying to be helpful, your OS is your OS.

If you can post the screenshot and config.json file, I will take a look at it and offer a possible fix for your miner on Windows.

## 2010phenix | 2019-12-11T15:25:49+00:00
@xmrig, testing now 5.2.0 on Win7 x64 ... I think some big mess with threads detection or ....
reproduce:
1.
**command line start** (--algo rx/0  --randomx-no-numa)
 * ABOUT        XMRig/5.2.0 gcc/9.2.0
 * LIBS         libuv/1.34.0 hwloc/2.1.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz (1) x64 AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       3.9/16.0 GB (24%)
 * ASSEMBLY     auto:intel
 * OPENCL       disabled
 * CUDA         disabled
[2019-12-11 18:04:22.074]  rx   init dataset algo rx/0 (4 threads) seed 3250d2a2
1f1cefef...
[2019-12-11 18:04:22.317]  rx   allocated 2336 MB (2080+256) huge pages 100% 116
8/1168 +JIT (242 ms)
[2019-12-11 18:04:31.192]  rx   dataset ready (8875 ms)
[2019-12-11 18:04:31.192]  cpu  use profile  rx  (3 threads) scratchpad 2048 KB
[2019-12-11 18:04:31.253]  cpu  READY **threads 3/3** (3) huge pages 100% 3/3 memory
 6144 KB (60 ms)
===========
2.
**start default** xmrig with almost default json
>         "init": -1,
>         "mode": "fast",
>         "1gb-pages": false,
>         "wrmsr": 6,
>         "numa": false

 * ABOUT        XMRig/5.2.0 gcc/9.2.0
 * LIBS         libuv/1.34.0 hwloc/2.1.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz (1) x64 AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       3.9/16.0 GB (25%)
 * ASSEMBLY     auto:intel
 * OPENCL       disabled
 * CUDA         disabled
[2019-12-11 18:23:23.940]  rx   init dataset algo rx/0 (4 threads) seed 3250d2a2
1f1cefef...
[2019-12-11 18:23:24.189]  rx   allocated 2336 MB (2080+256) huge pages 89% 1040
/1168 +JIT (248 ms)
[2019-12-11 18:23:32.368]  rx   dataset ready (8178 ms)
[2019-12-11 18:23:32.368]  cpu  use profile  rx  (1 thread) scratchpad 2048 KB
[2019-12-11 18:23:32.371]  cpu  READY **threads 1/1** (1) huge pages 100% 1/1 memory
 2048 KB (3 ms)

## xmrig | 2019-12-11T15:44:09+00:00
@2010phenix please show full command line and full config (except wallet addresses).
Thank you.

## 2010phenix | 2019-12-11T16:26:31+00:00
@xmrig 

> {
>     "api": {
>         "id": null,
>         "worker-id": null
>     },
>     "http": {
>         "enabled": false,
>         "host": "127.0.0.1",
>         "port": 0,
>         "access-token": null,
>         "restricted": true
>     },
>     "autosave": true,
>     "background": false,
>     "colors": false,
>     "randomx": {
>         "init": -1,
>         "mode": "fast",
>         "1gb-pages": false,
>         "wrmsr": 6,
>         "numa": false
>     },
>     "cpu": {
>         "enabled": true,
>         "huge-pages": true,
>         "hw-aes": null,
>         "priority": null,
>         "memory-pool": false,
>         "yield": true,
>         "asm": true,
>         "argon2-impl": null,
>         "argon2": [0],
>         "cn": [
>             [1, 0]
>         ],
>         "cn-heavy": [
>             [1, 0]
>         ],
>         "cn-lite": [
>             [1, 0]
>         ],
>         "cn-pico": [
>             [2, 0]
>         ],
>         "cn/gpu": [0],
>         "rx": [0],
>         "rx/wow": [0],
>         "cn/0": false,
>         "cn-lite/0": false,
>         "rx/arq": "rx/wow"
>     },
>     "opencl": {
>         "enabled": false,
>         "cache": true,
>         "loader": null,
>         "platform": "AMD",
>         "cn/0": false,
>         "cn-lite/0": false
>     },
>     "cuda": {
>         "enabled": false,
>         "loader": null,
>         "nvml": true,
>         "cn/0": false,
>         "cn-lite/0": false
>     },
>     "donate-level": 1,
>     "donate-over-proxy": 1,
>     "log-file": null,
>     "pools": [
>         {
>             "algo": null,
>             "coin": "monero",
>             "pass": "x",
>             "rig-id": null,
>             "nicehash": false,
>             "keepalive": false,
>             "enabled": true,
>             "tls": false,
>             "tls-fingerprint": null,
>             "daemon": false,
>             "self-select": null
>         }
>     ],
>     "print-time": 60,
>     "health-print-time": 60,
>     "retries": 5,
>     "retry-pause": 5,
>     "syslog": false,
>     "user-agent": null,
>     "watch": false
> }

and

> xmrig-notls1.exe --algo rx/0  --randomx-no-numa --no-color -o **IP** -u **WALLET**

PS if add -t 2 miner correct start with 2 threads 

## sectorKS | 2019-12-11T21:17:01+00:00
Hello,

I just compiled 5.2.0 on debian but I can't get 1GB pages working on linux. Normal huge pages work fine.

 * ABOUT        XMRig/5.2.0 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz (8) x64 AES
                L2:2.0 MB L3:160.0 MB 8C/8T NUMA:1
 * MEMORY       4.2/5.8 GB (72%)
 * ASSEMBLY     auto:intel

[2019-12-11 22:04:10.263]  rx   init dataset algo rx/0 (8 threads) seed ed5d070fac5138ce...
[2019-12-11 22:04:10.643]  rx   failed to allocate RandomX dataset using 1GB pages
[2019-12-11 22:04:10.688]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (425 ms)
[2019-12-11 22:04:14.837]  rx   dataset ready (4149 ms)
[2019-12-11 22:04:14.837]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2019-12-11 22:04:14.982]  cpu  READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (145 ms)

Any idea why or how to debug this?

My config, I run as root from cmd just ./xmrig

    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": true,
        "wrmsr": 6,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": false,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 4,
    "donate-over-proxy": 1,
    "log-file": "log.txt",
    "pools": [
        {
            "algo": null,
            "coin": null,
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
    "print-time": 300,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true




## x151973 | 2019-12-12T01:16:23+00:00
> 
> 
> > Ok, new test here with a AMD Ryzen 2700 + 16GB DDR4 + Asus Prime B450M + Windows 10 PRO 64 bits lastest build with all patches and "opcache" disabled in Bios.
> > Using default clocks, default timings, good power supply and temps is ok.
> > The segmentation fault still happening.
> > XmRig closes without error after a few time mining.
> 
> @FabioFrmg what does your config.json file look like? Can you upload a copy of your config.json file (XMR addresses, etc redacted) and also can you get and post a screenshot (or copy and paste the terminal/"command prompt" window text output) when the miner is first starting to run?
> 
> I want to know what the miner says when it's first run (a screenshot would be great) as I'm curious what it shows your CPU to be and what it shows it's cache sizes to be. It's possible that the CPU info given from hwloc is incorrect and due to that your config.json file's autoconfiguration could be incorrect which could cause it to crash.
> 
> I'm assuming you're mining CPU only (no OpenCL or CUDA) because if you're using GPUs that opens up a whole new world of potential issues that could cause seg faults.
> 
> Also worth noting that Windows does **not** (and probably never will) support 1GB hugepages (it rarely works well with regular 2MB hugepages, but that is 100% a Windows problem, no fault of xmrig... nothing the devs can do about Window's poor RAM memory management; I'm actually impressed they got largepages working at all in Windows 10... I couldn't even figure out how to enable it manually lol.)
> 
> Bottom line here is that Windows sucks. isn't the best option. If this is a dedicated mining rig you shouldn't be running Windows on it [some AMD GPUs (like the RX 550) are an exception due to AMD's subpar drivers, specifically their Linux drivers... but NVIDIA has good Linux drivers.) A CPU miner will always run better on Linux (IMHO and assuming proper configuration) due to many things (no forced updates that break things, better RAM memory management and control, etc.) I don't mean to preach (well, maybe a little... gotta spread the word lol) but if this is a dedicated mining rig (or you have no direct reason to use Windows that can't be done on Ubuntu with wine or Windows 10 inside a VirtualBox VM on Linux) then you should really make the switch IMHO. Especially since xmrig has plans to add autoconfiguration of 1GB hugepages for Linux (something that isn't possible on Windows.) But I digress... I'm only trying to be helpful, your OS is your OS.
> 
> If you can post the screenshot and config.json file, I will take a look at it and offer a possible fix for your miner on Windows.

Hi, is there any physical examples the hashrate Linux vs Windows on rx cpu mining using xmrig? how is difference look like, 120% or more?

## reeyon | 2019-12-12T02:33:41+00:00
@sectorKS are you running on VM? I'm having the same issue.

## xmrig | 2019-12-12T05:40:31+00:00
@2010phenix `"rx": [0],` this part of config define use 1 thread with affinity to first core, config was copied from another PC? try remove this line or whole `cpu` object.
Thank you.

## xmrig | 2019-12-12T05:43:52+00:00
@sectorKS You use virtual machine (wrong CPU count and cache size) it may not available even if CPU support it, or maybe (unlikely) reboot helps.
Thank you.

## Arkad19 | 2019-12-12T05:52:32+00:00

Hey. Does it support mining SFX coins?

## sectorKS | 2019-12-12T07:46:52+00:00
Yes this is a WM. Can you please advise what is exactly wrong with CPU count and cache size? 

I have 8 of processors (0...7, posting just first one), info from /proc/cpuinfo

processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 63
model name      : Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz
stepping        : 2
microcode       : 0x36
cpu MHz         : 2394.231
cache size      : 20480 KB
physical id     : 0
siblings        : 1
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 15
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts nopl xtopology tsc_reliable nonstop_tsc cpuid aper
fmperf pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm cpuid_fault epb pti fsgsbase smep cqm_llc cqm_occup_llc dtherm ida arat pln pts
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
bogomips        : 4788.46
clflush size    : 64
cache_alignment : 64
address sizes   : 40 bits physical, 48 bits virtual
power management:

I have another AMD host running VM and have same issue there.

 * ABOUT        XMRig/5.2.0 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Opteron(tm) Processor 6128 (4) x64 -AES
                L2:4.0 MB L3:40.0 MB 8C/8T NUMA:1
 * MEMORY       3.0/3.9 GB (77%)
 * ASSEMBLY     auto:none
 * OPENCL       disabled
 * CUDA         disabled

[2019-12-12 08:39:57.977]  rx   init dataset algo rx/0 (8 threads) seed ed5d070fac5138ce...
[2019-12-12 08:39:59.174]  rx   failed to allocate RandomX dataset using 1GB pages
[2019-12-12 08:39:59.373]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (1396 ms)
[2019-12-12 08:40:09.151]  rx   dataset ready (9778 ms)
[2019-12-12 08:40:09.151]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2019-12-12 08:40:09.298]  cpu  READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (147 ms)


## xmrig | 2019-12-12T08:03:23+00:00
I don't think 1GB is available in VM without special care on host system. https://stackoverflow.com/questions/44379170/hugepagesize-is-not-increasing-to-1g-in-vm

Your hypervisor report to guest OS you have 8 physical CPUs (packages) each with single core, it not a issue if you use manual configuration, but auto configuration may fail because CPU topology information wrong.

## 2010phenix | 2019-12-12T13:27:53+00:00
> @2010phenix `"rx": [0],` this part of config define use 1 thread with affinity to first core, config was copied from another PC? try remove this line or whole `cpu` object.
> Thank you.

khx, no just unpack xmrig-5.2.0-gcc-win64.zip and on first run make this config .... 
yes, "rx": [0] is a 1 thread... but even not look on this, miner autoconfig build, strange.....

PS another clean unpack zip, try and yes, now correct build         "rx": [0, 1, 2],


## reeyon | 2019-12-13T03:30:00+00:00
I have followed this article to enabling [HugePages ](https://docs.vmware.com/en/VMware-vCloud-NFV-OpenStack-Edition/3.0/vmwa-vcloud-nfv30-performance-tunning/GUID-1F05987F-012B-4BC4-9015-CDE3C991C68C.html)for VM guest. 
But somehow, it still unable to allocate RX dataset using 1GB pages during launch.

``` 
* ABOUT        XMRig/5.2.0 gcc/7.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz (2) x64 AES
                L2:0.5 MB L3:30.0 MB 12C/12T NUMA:2
 * MEMORY       7.7/11.7 GB (66%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      1.1.1.1:3344 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2019-12-13 11:18:24.677]  net  use pool 1.1.1.1:3344  1.1.1.1
[2019-12-13 11:18:24.677]  net  new job from 1.1.1.1:3344 diff 30000 algo rx/loki height 422998
[2019-12-13 11:18:24.679]  rx   init datasets algo rx/loki (12 threads) seed 57605565760671d4...
[2019-12-13 11:18:25.989]  rx   #0 allocated 3072 MB huge pages 100% (1310 ms)
[2019-12-13 11:18:25.990]  rx   failed to allocate RandomX dataset using 1GB pages
[2019-12-13 11:18:25.990]  rx   #1 allocated 2080 MB huge pages 100% (1311 ms)
[2019-12-13 11:18:25.990]  rx   -- allocated 5152 MB huge pages 100% 1043/1043 (1312 ms)
[2019-12-13 11:18:30.672]  rx   #0 dataset ready (4681 ms)
[2019-12-13 11:18:31.035]  rx   #1 dataset ready (363 ms)
[2019-12-13 11:18:31.035]  cpu  use profile  rx  (12 threads) scratchpad 2048 KB
[2019-12-13 11:18:31.258]  cpu  READY threads 12/12 (12) huge pages 100% 12/12 memory 24576 KB (222 ms)
```
My server has 2 NUMA nodes. My `vm.nr_hugepages` is `2336`. It seems like it was able to enable 1G page on node1, but not the node0. 





## SChernykh | 2019-12-13T09:28:15+00:00
@reeyon you don't need to have 2336 hugepages if you use 1GB pages. You only need 3x1GB pages per NUMA node + 1x2MB page per mining thread. Also try to run xmrig with sudo, it'll allocate hugepages itself.

## setuidroot | 2019-12-13T18:41:27+00:00
> I have followed this article to enabling [HugePages ](https://docs.vmware.com/en/VMware-vCloud-NFV-OpenStack-Edition/3.0/vmwa-vcloud-nfv30-performance-tunning/GUID-1F05987F-012B-4BC4-9015-CDE3C991C68C.html)for VM guest.
> But somehow, it still unable to allocate RX dataset using 1GB pages during launch.
> 
> ```
> * ABOUT        XMRig/5.2.0 gcc/7.4.0
>  * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
>  * HUGE PAGES   supported
>  * 1GB PAGES    supported
>  * CPU          Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz (2) x64 AES
>                 L2:0.5 MB L3:30.0 MB 12C/12T NUMA:2
>  * MEMORY       7.7/11.7 GB (66%)
>  * DONATE       5%
>  * ASSEMBLY     auto:intel
>  * POOL #1      1.1.1.1:3344 algo auto
>  * COMMANDS     hashrate, pause, resume
>  * OPENCL       disabled
>  * CUDA         disabled
> [2019-12-13 11:18:24.677]  net  use pool 1.1.1.1:3344  1.1.1.1
> [2019-12-13 11:18:24.677]  net  new job from 1.1.1.1:3344 diff 30000 algo rx/loki height 422998
> [2019-12-13 11:18:24.679]  rx   init datasets algo rx/loki (12 threads) seed 57605565760671d4...
> [2019-12-13 11:18:25.989]  rx   #0 allocated 3072 MB huge pages 100% (1310 ms)
> [2019-12-13 11:18:25.990]  rx   failed to allocate RandomX dataset using 1GB pages
> [2019-12-13 11:18:25.990]  rx   #1 allocated 2080 MB huge pages 100% (1311 ms)
> [2019-12-13 11:18:25.990]  rx   -- allocated 5152 MB huge pages 100% 1043/1043 (1312 ms)
> [2019-12-13 11:18:30.672]  rx   #0 dataset ready (4681 ms)
> [2019-12-13 11:18:31.035]  rx   #1 dataset ready (363 ms)
> [2019-12-13 11:18:31.035]  cpu  use profile  rx  (12 threads) scratchpad 2048 KB
> [2019-12-13 11:18:31.258]  cpu  READY threads 12/12 (12) huge pages 100% 12/12 memory 24576 KB (222 ms)
> ```
> 
> My server has 2 NUMA nodes. My `vm.nr_hugepages` is `2336`. It seems like it was able to enable 1G page on node1, but not the node0.

Enable 1GB hugepages for the second NUMA node like this:

````
sudo echo "3" >> /sys/devices/system/node/node*/hugepages/*1048*/nr_hugepages
````

The above command will actually enable 3 1GB hugepages for both NUMA nodes (total 6GB of RAM used.)

See my comment to issue #1411 for a full explanation, but you already have 1GB hugepages working, you just need to allocate 3 pages to the other NUMA node is all.

## setuidroot | 2019-12-13T19:09:12+00:00
@x151973 
> Hi, is there any physical examples the hashrate Linux vs Windows on rx cpu mining using xmrig? how is difference look like, 120% or more?

No, Linux is definitely not 120% better hashrate than windows.  Actually the hashrates are generally pretty similar in my experience (limited with Windows) but Linux has many more options and capabilities to improve the hashrate, where nothing ever seems to work right in Windows (if it even has the functionality at all.)  Plus Linux memory is more stable (less fragmentation) so you don't get hashrate drops after running for awhile like you do in Windows.  Just the fact Windows forces sh*tty updates down your throat that break functionality should be enough to make you not want to use it (never mind the fact that the whole Windows OS is spyware for American intelligence agencies.)  Oh and Windows isn't even free 😓 (not that anybody would actually pay the $100+ for a license that you don't even need to run Windows) but how much slapping in the face by Windows must people incur before they stand up for themselves?  The Windows monopoly will continue on as long as people are sheep.  I don't understand why people accept this especially since their are thousands of Linux distros that offer a better (or at least equal to Windows) operating system all for **free** and they respect your privacy (they are open source such that you can vet the code yourself.)  You could even build your very own Linux distro and make it just how you want it... granted a lot of learning is required to get into modifying and building the Linux kernel, but all the free information to learn how to do so is out on the internet.

Anyways... enough ranting.  I'd say I get ~3-4% better hashrate on Linux than I did on Windows (but I've done many optimizations with Linux.)  Stock, I'd say Windows and Linux perform close to equal for xmrig CPU mining.  But in Windows hashrate goes down a lot as the memory fragments and it loses it's hugepages; that never happens in Linux... plus I've had Windows CPU mining it crashes randomly (updates and are all disabled and Microsoft server IPs are blocked) but it still freezes and crashes... I've **never** had linux crash while CPU mining (I even had one server that had been mining non-stop for ~6 months, then a coin fork forced me to stop and compile a new miner and it continued with an uptime for almost a year.)

## xmrig | 2019-12-14T08:10:42+00:00
v5.2.1 release notes https://www.reddit.com/r/MoneroMining/comments/eah5db/xmrig_521_added_automatic_msr_mod_for_ryzen_cpus/

## miki-bgd-011 | 2019-12-14T11:00:53+00:00
I can't set 1gb pages to true in config file while it works fine when activating via command line with --randomx-1gb-pages.


    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "1gb-pages": true,   
        "hw-aes": true, 

## randomXguy | 2019-12-14T16:14:11+00:00
Hello
Is there something about threadrippers second gen in this releases, some confugurations? I have couple of amd 2990wx and I'm getting 14000H/s(4x8gb rigs)-18000H/s(4x16gb rigs). I think this is little, because 3900x gives that much with 12core/24threads . Here is my configuration: 


{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "0.0.0.0",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "wrmsr": 6,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18],
            [1, 20],
            [1, 22],
            [1, 24],
            [1, 26],
            [1, 28],
            [1, 30],
            [1, 32],
            [1, 34],
            [1, 36],
            [1, 38],
            [1, 40],
            [1, 42],
            [1, 44],
            [1, 46],
            [1, 48],
            [1, 50],
            [1, 52],
            [1, 54],
            [1, 56],
            [1, 58],
            [1, 60],
            [1, 62]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 8],
            [1, 10],
            [1, 16],
            [1, 18],
            [1, 24],
            [1, 26],
            [1, 32],
            [1, 34],
            [1, 40],
            [1, 42],
            [1, 48],
            [1, 50],
            [1, 56],
            [1, 58]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27],
            [1, 28],
            [1, 29],
            [1, 30],
            [1, 31],
            [1, 32],
            [1, 33],
            [1, 34],
            [1, 35],
            [1, 36],
            [1, 37],
            [1, 38],
            [1, 39],
            [1, 40],
            [1, 41],
            [1, 42],
            [1, 43],
            [1, 44],
            [1, 45],
            [1, 46],
            [1, 47],
            [1, 48],
            [1, 49],
            [1, 50],
            [1, 51],
            [1, 52],
            [1, 53],
            [1, 54],
            [1, 55],
            [1, 56],
            [1, 57],
            [1, 58],
            [1, 59],
            [1, 60],
            [1, 61],
            [1, 62],
            [1, 63]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27],
            [2, 28],
            [2, 29],
            [2, 30],
            [2, 31],
            [2, 32],
            [2, 33],
            [2, 34],
            [2, 35],
            [2, 36],
            [2, 37],
            [2, 38],
            [2, 39],
            [2, 40],
            [2, 41],
            [2, 42],
            [2, 43],
            [2, 44],
            [2, 45],
            [2, 46],
            [2, 47],
            [2, 48],
            [2, 49],
            [2, 50],
            [2, 51],
            [2, 52],
            [2, 53],
            [2, 54],
            [2, 55],
            [2, 56],
            [2, 57],
            [2, 58],
            [2, 59],
            [2, 60],
            [2, 61],
            [2, 62],
            [2, 63]
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 2,
    "donate-over-proxy": 0,
    "log-file": false,
    "pools": [
        {
            "algo": null,
            "coin": "monero",
            "url": "pool.supportxmr.com:3333",
            "user": "xxxxxxxxxxxxxxxxxxx",
            "pass": "sl15",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 50,
    "retry-pause": 50,
    "syslog": false,
    "user-agent": null,
    "watch": true
}

## jdmpro | 2019-12-14T23:01:09+00:00
5.2.1 is way slower then the previous 

## sectorKS | 2019-12-17T22:32:07+00:00
Hi all, 

I was able to get this working on linux VM. I found out that what you really need is 6GB RAM even if you have just 1 NUMA. No need to setup anything special on esxi hypervisor. I was not able to get it working with 4 or 5GB. Still got "failed to allocate RandomX dataset using 1GB pages". I have only 1 NUMA node and expected this to work with 4GB of RAM.

One WM on another host I had to put 8GB as I was not able to get it working with 6GB.

This works (6GB RAM)

```
 * ABOUT        XMRig/5.3.0 gcc/8.3.0
 * LIBS         libuv/1.24.1 hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz (1) x64 AES
                L2:0.2 MB L3:20.0 MB 8C/8T NUMA:1
 * MEMORY       0.3/5.8 GB (5%)
 * ASSEMBLY     auto:intel
[2019-12-17 21:03:31.460]  msr  register values for Intel has been set successfully (31 ms)
[2019-12-17 21:03:31.460]  rx   init dataset algo rx/0 (8 threads) seed ...
[2019-12-17 21:03:32.115]  rx   allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (654 ms)
[2019-12-17 21:03:36.235]  rx   dataset ready (4121 ms)
[2019-12-17 21:03:36.235]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2019-12-17 21:03:36.383]  cpu  READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (147 ms)
```
 
This does not (5GB RAM)

```
 * ABOUT        XMRig/5.3.0 gcc/8.3.0
 * LIBS         libuv/1.24.1 hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz (1) x64 AES
                L2:0.2 MB L3:20.0 MB 8C/8T NUMA:1
 * MEMORY       0.2/4.8 GB (5%)
 * ASSEMBLY     auto:intel
[2019-12-17 21:39:02.795]  msr  register values for Intel has been set successfully (22 ms)
[2019-12-17 21:39:02.795]  rx   init dataset algo rx/0 (8 threads) seed ...
[2019-12-17 21:39:03.733]  rx   failed to allocate RandomX dataset using 1GB pages
[2019-12-17 21:39:03.842]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (1046 ms)
[2019-12-17 21:39:07.990]  rx   dataset ready (4147 ms)
[2019-12-17 21:39:07.990]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2019-12-17 21:39:08.137]  cpu  READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (147 ms)
```

Some more details I found out. If you do this after reboot, before xmrig run:

```
cat /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
0
cat /sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages
0
```

after xmrig is run (6 GB RAM)

```
cat /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
8
cat /sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages
3
```

If your RAM size on VM is insufficient to have 3 huge pages (1GB) and you try this

`echo "3" > /sys/devices/system/node/node0/hugepages/hugepages-1048576kB/nr_hugepages`

It will not work and "3" will not be there when you "cat" nr_hugepages after.

I have debian buster (4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u2) and xmrig 5.3.0

I however get very little difference using 1GB pages (on VM and physical machine). Less than 0.5% hashrate increase.

One note: you can remove vm.nr_hugepages config from /etc/sysctl.conf as xmrig does this auto now. 



# Action History
- Created by: xmrig | 2019-12-11T08:24:20+00:00
- Closed at: 2019-12-21T19:46:26+00:00
