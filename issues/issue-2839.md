---
title: 5950X lower hash on virtual threads
source_url: https://github.com/xmrig/xmrig/issues/2839
author: toy1111
assignees: []
labels: []
created_at: '2021-12-27T00:33:24+00:00'
updated_at: '2021-12-29T06:46:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I've been using xmrig for sometime with mostly 3800XT and 3900XT rigs and the per thread hashrates are usually the same on all threads. But with a 5950X I just got I'm seeing the core/virtual threads differ.
Not sure if this is expected and I can't seem to find anyone else discussing such behavior so I'm asking. 

Using same mobo/memory and xmrig settings with 3800XT or 3900XT then switching to 5950X and basically only changing the cpu affinity threads to use 32 plus I add another pair of ram modules.

Below is relevant part of my config.json file and below that is the output from API monitoring rig that shows consistent hash and lower hash for the core/thread pairs. 

Is it expected with 5950X to have lower hash virtual threads vs the core thread?

(note: no change with xmrig 6.15.0 and [-1,....] for the all the cpu affinity threads)

---------
config.json:
"randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
"cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
---------
API /1/summary

 "version": "6.16.2",
    "kind": "miner",
    "ua": "XMRig/6.16.2 (Windows NT 10.0; Win64; x64) libuv/1.42.0 msvc/2019",
    "cpu": {
        "brand": "AMD Ryzen 9 5950X 16-Core Processor",
        "family": 25,
        "model": 33,
        "stepping": 0,
        "proc_info": 10620688,
        "aes": true,
        "avx2": true,
        "x64": true,
        "64_bit": true,
        "l2": 8388608,
        "l3": 67108864,
        "cores": 16,
        "threads": 32,
        "packages": 1,
        "nodes": 1,
        "backend": "hwloc/2.5.0",
        "msr": "ryzen_19h",
        "assembly": "ryzen",
        "arch": "x86_64",
        "flags": ["aes", "vaes", "avx", "avx2", "bmi2", "osxsave", "pdpe1gb", "sse2", "ssse3", "sse4.1", "popcnt", "cat_l3"]
    },
    "donate_level": 1,
    "paused": false,
    "hashrate": {
        "total": [17411.5, 17412.19, 17409.76],
        "highest": 17464.97,
        "threads": [
            [580.25, 580.42, 579.92],
            [508.65, 508.83, 508.48],
            [585.05, 584.88, 584.69],
            [511.88, 512.34, 512.13],
            [579.52, 579.34, 579.25],
            [507.71, 507.76, 507.7],
            [578.9, 579.02, 579.0],
            [508.02, 507.78, 507.87],
            [579.52, 579.58, 579.28],
            [508.02, 508.15, 507.9],
            [583.69, 583.62, 583.38],
            [510.94, 511.57, 511.42],
            [579.32, 578.82, 578.84],
            [507.4, 507.31, 507.47],
            [578.59, 578.77, 578.8],
            [507.92, 508.11, 508.19],
            [578.69, 578.59, 578.4],
            [508.13, 507.93, 507.85],
            [580.36, 580.1, 580.11],
            [508.96, 508.78, 508.79],
            [578.06, 578.17, 578.3],
            [508.02, 508.08, 507.9],
            [578.17, 578.13, 578.05],
            [507.5, 507.31, 507.48],
            [577.86, 578.22, 578.2],
            [507.29, 507.66, 507.68],
            [578.9, 578.34, 578.46],
            [507.71, 507.71, 507.67],
            [581.09, 580.92, 580.85],
            [510.11, 510.16, 510.11],
            [577.54, 578.03, 577.9],
            [507.6, 507.61, 507.54]
        ]
    },
    "hugepages": true



# Discussion History
## SChernykh | 2021-12-27T08:28:05+00:00
No, this is not normal. Check that nothing else is using CPU, go through [the tuning guide](https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/)

## toy1111 | 2021-12-27T16:00:50+00:00
Thank you for letting me know this isn't expected. I will go through the guide again but I thought its pretty well tuned. In testing If I swap out the 5950X for a 3900XT all of the threads hash as expected (about 610hs for all 24 threads). Also in the config if I reduce the threads from 32 to say 30 or 24 there isn't any change in the thread/virtual thread hash rates - which would make me think there isn't anything else using the CPU. Really perplexed by this....



## Lonnegan | 2021-12-28T00:22:57+00:00
Is that Windows 11 or 10? The term "Windows NT 10.0" unfortunately doesn't tell us, since Win 10 and 11 both are internally called NT 10.0 

## toy1111 | 2021-12-28T04:45:22+00:00
The OS is Win Server 2022 and I also used Win Server 2019 - both gave same results where the virtual thread is consistently lower. I don't see this on these same rigs with the 3800XT and 3900XT processors. I also tested a completely different mobo though both are ASUS B450 type with latest BIOS but again same lower hash on the virtual thread with the 5950X. 





## steba000 | 2021-12-28T09:06:15+00:00
you can try changing the cpu affinity. HWinfo reports the Core Performance Order.
In my case the order is: "1, 2, 5, 4, 8, 3, 7, 12, 15, 14, 6, 10, 9, 16, 11, 13" and the cpu affinity reflects this order: first all the phisical cores and then the virtual cores

## toy1111 | 2021-12-28T17:04:58+00:00
I have tried the [-1,-1,-1,....] for all 32 threads and tried using only some of the threads (30 or less). In both cases It still has the virtual cores hashing about 70hs lower. With Ryzen I've not seen any core ordering that isn't 1,2/3,4/5,6/.,..., but I know with Intel CPUs this isn't the case. Either way its still being consistently low on the virtual thread. I'm still trying different things like changing the OS. Anyone's thoughts are appreciated.

## toy1111 | 2021-12-28T19:21:47+00:00
Appears the issue is with Windows Server 2019/2022. Keeping all the same but booting from a drive with fresh install of Win10 21H1 all threads are hashing as expected (below). But I don't see this with the 3800XT (16 threads) or 3900XT (24 threads) processors - wonder if the 5000 series are not fully working on Win Server?

 "hashrate": {
        "total": [18620.33, 18596.01, null],
        "highest": 18621.0,
        "threads": [
            [579.4, 578.68, null],
            [581.69, 581.13, null],
            [583.54, 582.84, null],
            [583.32, 582.04, null],
            [584.73, 584.15, null],
            [585.17, 584.54, null],
            [585.71, 585.23, null],
            [585.17, 584.69, null],
            [581.36, 578.71, null],
            [582.56, 579.79, null],
            [582.23, 581.13, null],
            [582.99, 581.07, null],
            [582.45, 581.67, null],
            [582.99, 582.2, null],
            [580.49, 579.64, null],
            [580.16, 579.6, null],
            [581.03, 581.05, null],
            [581.47, 581.12, null],
            [583.32, 582.9, null],
            [583.1, 582.8, null],
            [580.38, 579.65, null],
            [579.94, 579.84, null],
            [583.54, 583.36, null],
            [583.32, 583.17, null],
            [579.73, 579.37, null],
            [580.38, 579.85, null],
            [578.64, 578.05, null],
            [578.86, 578.32, null],
            [577.77, 576.82, null],
            [580.71, 579.87, null],
            [582.12, 581.54, null],
            [581.9, 581.03, null]
        ]
    },

## SChernykh | 2021-12-28T19:29:17+00:00
Maybe it has something to do with virtualization or core isolation/memory integrity settings.

## toy1111 | 2021-12-28T21:37:16+00:00
Not sure exactly where to look for these possible settings but I made some changes though hashrate still low on the virtual threads in Win Server. Defender is uninstalled and here are the rig's reported Security:Secured-Core settings,

Hypervisor Enforced Code Integrity (HVCI) - Not configured
Boot DMA Protection - Not supported
System Guard - Not configured
Secure Boot - Not configured
Virtualization-based Security (VBS) - Not configured
Trusted Platform Module 2.0 (TPM 2.0) - Not supported

In SystemInfo this is reported:

VM Monitor Mode Extensions: Yes
Virtualization Enabled In Firmware: Yes (In BIOS this is CPU SVM Mode and is off by default, I enabled but no change to hashrate)
Second Level Address Translation: Yes
Data Execution Prevention Available: Yes


## Lonnegan | 2021-12-29T06:46:40+00:00
Windows Server 2019 is based on the Windows 10 1809 core, while Windows Server 2022 is based on Windows 10 21H2. Therefore, they should behave similarly in principle.

One difference is that Windows 10 is set to prioritize foreground programs by default, while Windows Server prioritizes background services. Perhaps this has an effect on the scheduler.

And whether Windows Server also uses things like core prioritization and CPPC2, I don't know. However, Zen 2 already supports CPPC2, so it can't be because of that alone that the problem only occurs with your Zen 3. Anyway, a strange case!

# Action History
- Created by: toy1111 | 2021-12-27T00:33:24+00:00
