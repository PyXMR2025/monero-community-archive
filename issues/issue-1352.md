---
title: Speed n/a on AMD, rx/0 algo
source_url: https://github.com/xmrig/xmrig/issues/1352
author: MrXtar
assignees: []
labels:
- opencl
- randomx
created_at: '2019-12-01T10:17:50+00:00'
updated_at: '2021-04-12T15:13:17+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:13:17+00:00'
---

# Original Description
Why no speed on rx/0 algo? Win 8, xmrig-5.1.0-gcc-win64

What can i do? 

![image](https://user-images.githubusercontent.com/19951620/69912624-e8875d00-143c-11ea-9278-298f76da9029.png)


# Discussion History
## hawk-eye77 | 2019-12-01T18:22:47+00:00
Got the same on All my r280X 3gb.... Don't know what to do...

## hawk-eye77 | 2019-12-01T18:25:48+00:00
By the way, network hashrate doubled after the fork. So many CPU miners working worldwide?

## komatom | 2019-12-01T22:31:47+00:00
Try set dataset_host to true in the config file, section for the threads of rx/0 algo.

## lss4 | 2019-12-03T07:29:46+00:00
I'm having issues with Navi (RX 5700 XT). The ocl thread compiles, but it seems stuck, with no hashrate and can't even be stopped after exiting xmrig (when exiting xmrig the ocl thread don't appear to stop), you can forcefully exit xmrig by typing Ctrl-C many times, but the GPU utilization will remain 100% until reboot.

Not sure if kernels were relevant as this is observed on 5.4.1 kernel (on Manjaro Testing). Back then with 5.3.12 kernel and with cn/r algo, it took quite a while for the ocl thread to actually start working, and once it started working, it didn't take long to stop the thread when exiting.

## ajtetreault | 2019-12-03T23:12:22+00:00
I'm having the same issue with RX 580s and a Vega 56.  The CPU is hashing but nothing from the AMD cards.  I've updated to the latest AMD drive to no avail.  Similar issue with shutting down.  Ctrl-c will stop CPU mining but then just hangs and I need to kill xmrig from Task Manager.

## lss4 | 2019-12-04T00:02:58+00:00
> Ctrl-c will stop CPU mining but then just hangs and I need to kill xmrig from Task Manager.

After force-killing xmrig, does video card usage return to normal for you?

In my case with Navi, even after force-killing xmrig the video card stays 100% loaded until reboot.

## ajtetreault | 2019-12-05T03:33:13+00:00

> After force-killing xmrig, does video card usage return to normal for you?
> 
> In my case with Navi, even after force-killing xmrig the video card stays 100% loaded until reboot.

The video cards GPUs are never loaded at all.  They are at 0% from start to finish.

## ajtetreault | 2019-12-05T04:18:08+00:00
Hi,

I think I'm just doing something dumb and missing or have a wrong setting.  The CPU is mining, but not the AMD GPUs.  The shows everything is there, but it's kind of like they are just all paused.  I've even tried just pressing 'r' to resume but to no avail.  The initial log is attached.
[log.txt](https://github.com/xmrig/xmrig/files/3925079/log.txt)


## aa-delite | 2019-12-05T12:53:20+00:00
I have null hashrate on ryzen 2200G using 5.1.1. It does not crash, but mining nothing with null hashrate, using much RAM and swapping to disk.
Can't fix it on that machine. Most my PCs works well, even ryzen 1xxx series.

## aa-delite | 2019-12-06T00:13:01+00:00
Do you see 100% huge pages (green) or red?
allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT
Check it when just starting mining.

## dedizones | 2019-12-12T09:40:59+00:00
I have same problem, AMD 280X =>n/a | n hashrate

when I look at the startup the card reloads well, then suddenly its crash as the settings were reset => wattman notification :"Default Radeon WattMan Settings Have been Restored due to...."
so I don't know if it's the XMRIG version, I'm in the latest version, AMD driver I tested all of them for 1 year: D without result, in short if anyone has a solution
I now end up with unused GPUs

# Action History
- Created by: MrXtar | 2019-12-01T10:17:50+00:00
- Closed at: 2021-04-12T15:13:17+00:00
