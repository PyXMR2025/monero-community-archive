---
title: Closing after few minutes mining. v5.1.0
source_url: https://github.com/xmrig/xmrig/issues/1374
author: FabioFrmg
assignees: []
labels:
- bug
created_at: '2019-12-03T14:44:47+00:00'
updated_at: '2020-06-02T14:35:39+00:00'
type: issue
status: closed
closed_at: '2020-06-02T14:35:39+00:00'
---

# Original Description
Hi,
I'm having problems running XMRIG V5.1.0 cpu mining now with RandomX.
I ran tests on 5 different computers with different processors and noticed that on most of machines, after a few minutes running XMRIG it simply shutdown by itself and stops running.
No overclock or other tunning, just default settings. 
Temperatures are checked and still ok.
I tried several different options including disabling NUMA, changing from fast to light mode or disable running in backgroud without any success. 
I have Ryzen 5, Ryzen 7 and Intel Core I5 processors in my machines. 
Running in Windows 10 64 bits. 
Most of computers have 8GB DDR3 or DDR4 RAM. 
By the way, i have the same issue when i use GPU mining with Nvidia Geforce 1060.
Everything appears ok looking at hashrates and jobs but near 10 minutes mining the process xmrig.exe just close and i need to restart it.
Any ideas?
Thanks for now

# Discussion History
## SChernykh | 2019-12-03T15:00:48+00:00
Some Ryzen processors are known to have this issue, it can be fixed by disabling "Opcache" option in BIOS

## monero101 | 2019-12-03T15:21:40+00:00
Are the previous versions of xmrig affected by this too ?

## FabioFrmg | 2019-12-03T15:25:59+00:00
> Are the previous versions of xmrig affected by this too ?

No. ;)

## FabioFrmg | 2019-12-03T15:26:37+00:00
> Opcache

Ok, i will try. But what about with GPU mining?

## SChernykh | 2019-12-03T15:27:17+00:00
If v5.0.1 worked fine for you and v5.1.0 has this problem then v5.1.1 should hopefully fix it because it brings back some code which was removed.

## monero101 | 2019-12-03T15:30:34+00:00
> If v5.0.1 worked fine for you and v5.1.0 has this problem then v5.1.1 should hopefully fix it because it brings back some code which was removed.

Do we need to use the yield option in v5.1.1 ?

## FabioFrmg | 2019-12-03T15:30:42+00:00
> If v5.0.1 worked fine for you and v5.1.0 has this problem then v5.1.1 should hopefully fix it because it brings back some code which was removed.

Ok, thanks for help =D
Waiting a new version. 

## xmrig | 2019-12-04T03:44:45+00:00
`yield` now used by default again, this is already in code, v5.1.1 will be released today.
Thank you.

## xmrig | 2019-12-04T10:40:24+00:00
v5.1.1 released https://github.com/xmrig/xmrig/releases/tag/v5.1.1 no changes in config file required, please confirm is this issue fixed or not.
Thank you.

## FabioFrmg | 2019-12-04T17:44:43+00:00
> v5.1.1 released https://github.com/xmrig/xmrig/releases/tag/v5.1.1 no changes in config file required, please confirm is this issue fixed or not.
> Thank you.

Thanks for update. 
But bad news. The issue was not fixed. =(
I sended attached my log file. 

[log.txt](https://github.com/xmrig/xmrig/files/3923228/log.txt)

Command Line: 
`xmrig.exe -o xmr-us-east1.nanopool.org:14444 -u mywallet.myworker -p 12345 -t 6 -k --cpu-no-yield --randomx-no-numa --coin monero -S -l log.txt`

Log File: 

```
* ABOUT        XMRig/5.1.1 MSVC/2017
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   permission granted
 * CPU          AMD Ryzen 5 1400 Quad-Core Processor (1) x64 AES
                L2:2.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       3.5/7.9 GB (44%)
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmr-us-east1.nanopool.org:14444 coin monero
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2019-12-04 14:23:03.697]  net  use pool xmr-us-east1.nanopool.org:14444  192.99.69.170
[2019-12-04 14:23:03.699]  net  new job from xmr-us-east1.nanopool.org:14444 diff 480045 algo rx/0 height 1981616
[2019-12-04 14:23:03.699]  rx   init dataset algo rx/0 (8 threads) seed 435333dc1dc4a930...
[2019-12-04 14:23:04.092]  rx   allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (392 ms)
[2019-12-04 14:23:08.258]  net  new job from xmr-us-east1.nanopool.org:14444 diff 480045 algo rx/0 height 1981616
[2019-12-04 14:23:09.575]  rx   dataset ready (5483 ms)
[2019-12-04 14:23:09.576]  cpu  use profile  *  (6 threads) scratchpad 2048 KB
[2019-12-04 14:23:10.202]  cpu  READY threads 6/6 (6) huge pages 100% 6/6 memory 12288 KB (626 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |       -1 |     n/a |     n/a |     n/a |
|        1 |       -1 |     n/a |     n/a |     n/a |
|        2 |       -1 |     n/a |     n/a |     n/a |
|        3 |       -1 |     n/a |     n/a |     n/a |
|        4 |       -1 |     n/a |     n/a |     n/a |
|        5 |       -1 |     n/a |     n/a |     n/a |
|        - |        - |     n/a |     n/a |     n/a |
[2019-12-04 14:23:13.939] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-12-04 14:24:08.973]  net  new job from xmr-us-east1.nanopool.org:14444 diff 480045 algo rx/0 height 1981616
[2019-12-04 14:24:09.592] speed 10s/60s/15m 705.0 n/a n/a H/s max 720.9 H/s
[2019-12-04 14:25:09.096]  net  new job from xmr-us-east1.nanopool.org:14444 diff 480045 algo rx/0 height 1981616
[2019-12-04 14:25:09.633] speed 10s/60s/15m 727.5 693.5 n/a H/s max 728.5 H/s
[2019-12-04 14:25:46.052]  net  new job from xmr-us-east1.nanopool.org:14444 diff 480045 algo rx/0 height 1981617
[2019-12-04 14:25:48.258]  net  new job from xmr-us-east1.nanopool.org:14444 diff 480045 algo rx/0 height 1981618
[2019-12-04 14:26:09.648] speed 10s/60s/15m 704.1 710.4 n/a H/s max 728.5 H/s
[2019-12-04 14:26:16.278]  net  new job from xmr-us-east1.nanopool.org:14444 diff 480045 algo rx/0 height 1981619
[2019-12-04 14:27:09.711] speed 10s/60s/15m 727.9 696.6 n/a H/s max 730.1 H/s
[2019-12-04 14:27:16.518]  net  new job from xmr-us-east1.nanopool.org:14444 diff 480045 algo rx/0 height 1981619


```

## SChernykh | 2019-12-04T17:51:09+00:00
Did you try to disable "Opcache" in BIOS?

## FabioFrmg | 2019-12-04T17:55:12+00:00
> Did you try to disable "Opcache" in BIOS?

There's no option to disable Opcache in Bios. 

Bios locked by Dell for Gamer Inspiron 5675

Any other possibility?

## SChernykh | 2019-12-04T18:06:47+00:00
Then you can only make a .bat file to auto-restart xmrig when it crashes (as a workaround), this is hardware bug in some 1st gen Ryzens. Some people reported that after 10-20 crashes it starts mining just fine.

## pinnarandolf | 2019-12-04T20:20:34+00:00
I noticed that it closes when minimized.
It says open if the window is normal sized and hidden by another window (maximized browser for example)
Ryzen 1800X, Windows 10
Edit: Can confirm, the behaviour started with 5.1.0

## FabioFrmg | 2019-12-05T11:03:19+00:00
> I noticed that it closes when minimized.
> It says open if the window is normal sized and hidden by another window (maximized browser for example)
> Ryzen 1800X, Windows 10
> Edit: Can confirm, the behaviour started with 5.1.0

Wow same here. It's strange but if Xmrig windows is maximized the process don't close. Only when minimized or in background. 
Maybe a bug with -B --background?
I have noticed that some other generations of AMD Ryzen have same issue. 


## FabioFrmg | 2019-12-05T11:08:21+00:00
> Then you can only make a .bat file to auto-restart xmrig when it crashes (as a workaround), this is hardware bug in some 1st gen Ryzens. Some people reported that after 10-20 crashes it starts mining just fine.

Could you show an .bat example? 
I tryed by different ways without sucess using task scheduler in Windows. =( 
The best way that i have found is create a xmrig.exe as a system service, but the program was not compiled for this use. 
Is possible to convert xmrig to be compatiple with windows system service and set auto restart feature when it close? 

## aa-delite | 2019-12-05T12:51:17+00:00
I have null hashrate on ryzen 2200G using 5.1.1. It does not crash, but mining nothing with null hashrate, using much RAM and intensive swapping to disk.
There is no opcache option there. 

I see you also have null hashrate. Do you see 100% huge pages?
allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT



## FabioFrmg | 2019-12-06T05:36:55+00:00
> see you also have null hashrate. Do you see 100% huge pages?
> allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT

I have hashrate and pool is reporting sucessfull hashrate too:
"speed 10s/60s/15m 705.0 n/a n/a H/s max 720.9 H/s"
But still closing... =(
This is why I am questioning about an option to auto restart the process infinitely. 
Maybe a xmrig windows service process compatible is the way to go. 
Or maybe we will have an external way to handle with opcache. 
Many people in world uses Ryzens. I can't believe that opcache will be a forever limitation.


## SChernykh | 2019-12-06T06:34:43+00:00
You can create a .bat file which restarts XMRig in a loop. Opcache is a problem only for a portion of 1st gen Ryzens that were produced before May 2017, it's not a problem for all Ryzens.

## FabioFrmg | 2019-12-06T12:33:44+00:00
> You can create a .bat file which restarts XMRig in a loop. Opcache is a problem only for a portion of 1st gen Ryzens that were produced before May 2017, it's not a problem for all Ryzens.

New tests here and i think that the problem is not opcache. 
I have Ryzens 2700, 1400, 1700 (after this date) and all of AMDs stops mining. 
There's no specific time, but in sure, all of them stops mining after some of time.
Intel Core I3 (gen4 and gen7), Core I5 (Gen8), are the only that not stop mining. 


## carlosmonaco | 2019-12-07T16:50:36+00:00
Same here 3900x , random stop with no error ( 60°C , 4000 MHz , 1,25V)

## valdirSalgueiro | 2019-12-08T11:12:37+00:00
Having the same problem. After some hours it just stops... No errors on console either.

## carlosmonaco | 2019-12-11T10:19:25+00:00
Same problem with new version 5.2

# Action History
- Created by: FabioFrmg | 2019-12-03T14:44:47+00:00
- Closed at: 2020-06-02T14:35:39+00:00
