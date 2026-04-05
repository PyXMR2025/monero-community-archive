---
title: System Hang Lock Crash on v5.x+ with Ryzen 5 2600X
source_url: https://github.com/xmrig/xmrig/issues/1462
author: BradT7
assignees: []
labels:
- stability
created_at: '2019-12-23T20:00:15+00:00'
updated_at: '2020-08-31T05:48:40+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:48:40+00:00'
---

# Original Description
**Describe the bug**
System locks up, disk usage goes to 100% in task manager (Samsung Evo SSD) with no matching app, xmrig looses connection to pool and stops mining due to system hard lock. I can move mouse, but unable to click anything. Forced to reboot machine.

**To Reproduce**
Run any xmrig v5.0.1 to v5.4 with 8 threads for 1-10 minutes, gets especially worse after version 5.1.1
I can delay the hard locks to every few hours if dropping down to 6 threads using v5.1.1+.
I'm only able to run stable with 5.0.1 using 6 threads.
I was using 8 threads on all 4.x versions with no issues. Only became an issue running 8 threads after v5.x

**Expected behavior**
Run 8 threads without crashing and get around 4700 h/s.

Compared to 6 threads getting around 4500 h/s on v5.4.
Or around 4200 h/s on 6 threads with v5.0.1 on stable setup.
(only got around 4200+ with 8 threads on v4.x)

**Required data**
```
 * ABOUT        XMRig/5.4.0 MSVC/2019
 * LIBS         libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 5 2600X Six-Core Processor (1) x64 AES
                L2:3.0 MB L3:16.0 MB 6C/12T NUMA:1
 * MEMORY       5.0/15.9 GB (31%)
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmr-us-east1.nanopool.org:14433 coin monero
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2019-12-23 14:30:22.500]  net  use pool xmr-us-east1.nanopool.org:14433 TLSv1.2 142.44.243.6
[2019-12-23 14:30:22.502]  net  fingerprint (SHA-256): "..."
[2019-12-23 14:30:22.502]  net  new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 1995373
[2019-12-23 14:30:22.528]  msr  register values for "ryzen" preset has been set successfully (26 ms)
[2019-12-23 14:30:22.528]  rx   init dataset algo rx/0 (12 threads) seed 8fd8d3ee74547743...
[2019-12-23 14:30:22.539]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (11 ms)
[2019-12-23 14:30:25.706]  rx   dataset ready (3167 ms)
[2019-12-23 14:30:25.706]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2019-12-23 14:30:25.925]  cpu  READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (218 ms)
[2019-12-23 14:30:26.635]  cpu  accepted (1/0) diff 480045 (135 ms)
[2019-12-23 14:30:27.785]  net  new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 1995374
[2019-12-23 14:31:26.006] speed 10s/60s/15m 4317.8 n/a n/a H/s max 4689.2 H/s
```
 
```
{
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
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 1],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 7]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 6],
            [1, 8]
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
            [1, 11]
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
            [2, 11]
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "rx": [0, 2, 4, 1, 6, 8, 10, 7],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
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
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "monero",
            "url": "xmr-us-east1.nanopool.org:14433",
            "user": "",
            "pass": "x",
            "rig-id": "",
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "verbose": 0,
    "watch": true
```
OS: Windows 1909

**Additional context**
Issue happens with or without msr enabled (when running as admin)
Running 2600X at 3.6GHz
Tested multiple bios settings on ASUS PRIME B450M-A same issue (BIOS is up to date).
Tried lowering the CPU clock speed and lowering the RAM speed from the default DCOP Corsair 
2933MHz settings, but still get system freezes.
Currently running default BIOS settings with default DCOP memory at 2933MHz and timings.
Additional system hardware includes a 450 watt Antec PSU and Nvidia 710 GT (for general video out, and not used for gaming or mining)



# Discussion History
## BradT7 | 2019-12-24T16:35:17+00:00
Some updates:
Confirmed system lock using only 6 threads on version 5.4, took only about 10-15 minutes. (Previous versions would usually run longer on 6 threads.)
Tested with a different 500W PSU, same issue.
Tested with Samsung SSD Rapid Mode off, same issue.
Here's a picture of the error, after the system locks up, xmrig still posts messages but stops mining, I'm unable to close any windows or open anything new as system is frozen, only mouse and windows can be moved. You can see the Disk showing at a 100% too.
![IMG_20191224_094402646_MP](https://user-images.githubusercontent.com/35740466/71418304-d3ff4480-2637-11ea-97a3-23ec81611d3a.jpg)

Any tips on additional troubleshooting would be appreciated.
I'm not really sure about the mechanics of what xmrig is really dependent on, but I'd be willing to try some more BIOS tweaks. I'm just not sure what to target, or what might be pushing the hardware over the edge to freeze like this when compared to previous versions like the 5.0.1 which runs stable on 6 threads (but not 8 threads, it will freeze after a day or two).


## xmrig | 2019-12-26T18:13:56+00:00
Disk used by something else, it's zero for miner process, use sorting by disk usage.
Thank you.

## kio3i0j9024vkoenio | 2019-12-29T15:50:45+00:00
Verify that you are not having any memory errors by running Memtest86 for at least the default four loops.

https://www.memtest86.com

If any errors show you need to fix them (increase voltage, change timings, replace them, etc) because memory errors will cause symptoms like what you are describing.

Example: I ordered a set of :

G.SKILL Ripjaws V Series 16GB (2 x 8GB) 288-Pin DDR4 SDRAM DDR4 3600 (PC4 28800) Desktop Memory Model F4-3600C16D-16GVKC

These sticks would produce a few errors in Test 8 and 9 of memtest86. These are on the QVL list for the motherboard (which had the latest BIOS) and were running in XMP mode at the stated 1.35 volts. Bumping the voltage to 1.4 volts did not fix the problem. So I returned the defective memory for a refund.

![Bad Memory](https://user-images.githubusercontent.com/35711866/71559180-caebea00-2a20-11ea-98bc-0f03fc12b241.JPG)

 

## BradT7 | 2019-12-30T21:00:05+00:00
**I'VE FIXED IT!** At least to my liking. Not sure if a fix can be built into xmrig for future updates, or if it's purely a CPU/MoBo/RAM issue/limitation, but I'm running stable with this setting Disabled in the BIOS. 
**AMD CBS > AMD Core Performance Boost > Disabled**
Thanks to a search result for Under-clocking the [Asus Prime B450M-A ](https://rog.asus.com/forum/showthread.php?108616-How-to-underclock-my-CPU-Ryzen-5-2600x-in-Asus-Prime-B450M-A)

Even though I had all my BIOS settings set to Auto (except for the fixed default XMP/DCOP RAM settings) with the Boost enabled by default it was still auto setting my CPU clock to around 3.9 GHz (as seen in Asus utility screenshot above) even when I manually set it to 3.6 GHz for testing it would still boost the CPU under load (I think the max boost is 4.1 GHz or 4.2 GHz for the Ryzen CPUs)

I'm currently running with AMD Core Performance Boost Disabled and 2600X CPU clock speed manually set to the default 3.6 GHz 
I'm now getting around 4500 h/s with 8 threads and around 4300 h/s with 6 threads.
With 8 threads I'm only running an average auto voltage of 1.122V for CPU and temp of 60C with the stock CPU fan at 1500 RPM, not bad at all!

If I bump up the CPU clocks as little as 3.65 GHz to 3.9 GHz, I get instability again. I notice the CPU voltage goes from the average 1.122V for 3.6 GHz to average 1.275V and 68C when 3.65 GHz, 3.7 GHz, 3.75 GHz doesn't matter, and not much improvement in the hashrate either, only at 3.8 GHz and 3.9 GHz can I reach 4700 h/s with hard locks.

So it's AMD Core Performance Boost and the CPU being pushed past the stock clock speed of 3.6 GHz that's causing the instability with the hardware being pushed too hard beyond the limits of the CPU, MoBo or RAM. I'll have to play around with the voltages more later I guess and take some more BIOS settings off of Auto, but not sure if it's worth the headache for an extra 200 h/s. 

I'll run with 8 threads for the next few days and report back if any additional hard locks on v5.4 and then test with v5.5 after that. Hopefully this helps anyone else that might be having similar issues. Also anyone who has any additional BIOS advice would be appreciated, not extremely savvy in the area of manually looking for and configuring settings.

## BradT7 | 2019-12-30T21:36:41+00:00
I forgot to mention I did test the memory with that tool, and it all came back okay, so it seems like if I do have an issue it's with the CPU or Motherboard, just not sure how to confirm if there is an issue and which one it is. I guess XMRig makes for a good stress tester XD

## SChernykh | 2019-12-31T09:19:20+00:00
I think the real issue here is not AMD Core Performance Boost but the general instability at higher clock speeds.

## BradT7 | 2019-12-31T16:59:33+00:00
I agree, issue does not appear to be related to xmrig software, but limitations of mid-range hardware.
I was stable all night at 3.6 GHz and Auto Voltage running around 1.122V.
At least all this was not in vain, I've been manually tweaking just the CPU core and voltage and found what looks to be some excellent settings, with AMD Core Performance Boost still disabled for now.
I've increased the CPU to 3.9 GHz and increased the stock voltage of 1.1875V +0.0375V to 1.225V
(Previously increasing the CPU to just 3.65 GHz the Auto Voltage was jumping to 1.275V and locking)
I'm now getting an average of 4750 h/s with 8 threads a CPU temp of around 65C and stock fan around 2000 rpm
I know all these details are not really applicable to xmrig, but hopefully they can help others that might be having similar freezing issues.
It might have just been an Auto Voltage issue all along with AMD Core Performance Boost enabled, but I'll keep it disabled for now and test this setup for a couple days before possibly enabling again.

## kio3i0j9024vkoenio | 2019-12-31T17:25:27+00:00
It may be that your 2600X needs extra voltage to run at the higher speeds because of the silicon lottery.

On my 2700X I am running stable @ 3.9 GHz with 1.175 Vcore (-100mv Vcore reduction set in BIOS) at 65c and default auto fan speed. 

6028 H/s on RX/0

## xmrig | 2020-08-31T05:48:40+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: BradT7 | 2019-12-23T20:00:15+00:00
- Closed at: 2020-08-31T05:48:40+00:00
