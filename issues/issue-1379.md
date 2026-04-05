---
title: Memory usage of new version
source_url: https://github.com/xmrig/xmrig/issues/1379
author: worm001
assignees: []
labels:
- question
created_at: '2019-12-04T04:00:55+00:00'
updated_at: '2019-12-21T20:03:23+00:00'
type: issue
status: closed
closed_at: '2019-12-21T20:03:22+00:00'
---

# Original Description
The memory usage of the new version is at least 2G. There is no command line or parameter to control when viewing official documents? Can't those like us who want to use computers and mine by the way?

# Discussion History
## dpsec | 2019-12-04T08:45:33+00:00
Hello, I need the same option. I've been searching to limit the memory for a process on Windows and I ended up SetProcessWorkingSetSize feature but I couldn't figure out how to implement it. If anybody has C++ knowledge maybe can help. 

Here is the full guide: [SetProcessWorkingSetSize](https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setprocessworkingsetsize?redirectedfrom=MSDN)

In theory, we can limit the working set for this specific process and force xmrig to use whatever we put there. Of course it will effect the mining performance but at least we can use the computer while mining without stopping the process. 

## dpsec | 2019-12-04T12:21:38+00:00
I just upgraded to the new version 5.1.1.0. It seems memory is ok (265MB used) with one of my computers which is **i7-6700** CPU but my other 2 computers which are **i7-3770** CPU still uses 2G ram. Is the fix by CPU model or am I missing something else?

## xmrig | 2019-12-04T12:44:42+00:00
https://github.com/xmrig/xmrig/issues/1318#issuecomment-559676080 but please note `light` mode is very slow, algorithm designed to use 2 GB.
Thank you.

## dpsec | 2019-12-04T13:12:57+00:00
Yes it's slow with the light mode **320 H/s** vs **2,032 H/s** with i7-3770 CPU. 

I don't know... I think in this case the best option to schedule of replacement config.json on certain times with cron. Light mode can be used certain peek hours but when the computer is idle, it's needed to be switched to auto to get the best performance.

## xmrig | 2019-12-04T13:15:13+00:00
Mode can't be changed by config replacement, only full miner restart.

## dpsec | 2019-12-04T13:23:56+00:00
I understand, thank you @xmrig for the hint. I was still wondering why i7-6700 CPU still uses around 256MB ram but get almost similar amount of hashrate with the one uses 2G ram. The only difference is the CPU model i7-6700 vs i7-3770. Do you have any idea?

## xmrig | 2019-12-04T13:28:12+00:00
Please show log from miner start till CPU threads started.
Thank you.

## worm001 | 2019-12-04T13:47:55+00:00
 light mode？ How can I call it on the command line? Only upgrade to 5.1.1?

## dpsec | 2019-12-04T13:49:21+00:00
Please find the logs attached.

i7-3770 memory is only 8MB used
i7-6700 memory is 2GB used

Similar hashrate. The only difference is the OS. i7-3770 is Windows 10, i7-6700 is Windows 7 but almost the same hashrate.

[i7-3770_memory-8MB_used.txt](https://github.com/xmrig/xmrig/files/3922107/i7-3770_memory-8MB_used.txt)

[i7-6700_memory-2GB_used.txt](https://github.com/xmrig/xmrig/files/3922108/i7-6700_memory-2GB_used.txt)



## dpsec | 2019-12-04T13:50:53+00:00
> light mode？ How can I call it on the command line? Only upgrade to 5.1.1?

Yes only 5.1.1 upgrade has it. Check below mode option.

    "autosave": true,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "mode": "auto",  // --> instead of auto, make it light
        "numa": true
    },

## worm001 | 2019-12-04T13:51:30+00:00
> Please find the logs attached.
> 
> i7-3770 memory is only 8MB used
> i7-6700 memory is 2GB used
> 
> Similar hashrate. The only difference is the OS. i7-3770 is Windows 10, i7-6700 is Windows 7 but almost the same hashrate.
> 
> [i7-3770_memory-8MB_used.txt](https://github.com/xmrig/xmrig/files/3922107/i7-3770_memory-8MB_used.txt)
> 
> [i7-6700_memory-2GB_used.txt](https://github.com/xmrig/xmrig/files/3922108/i7-6700_memory-2GB_used.txt)

The memory usage you see in task manager of win7 and win10 is not real. You need to see it in resource monitor.

## worm001 | 2019-12-04T13:53:01+00:00
> Please find the logs attached.
> 
> i7-3770 memory is only 8MB used
> i7-6700 memory is 2GB used
> 
> Similar hashrate. The only difference is the OS. i7-3770 is Windows 10, i7-6700 is Windows 7 but almost the same hashrate.
> 
> [i7-3770_memory-8MB_used.txt](https://github.com/xmrig/xmrig/files/3922107/i7-3770_memory-8MB_used.txt)
> 
> [i7-6700_memory-2GB_used.txt](https://github.com/xmrig/xmrig/files/3922108/i7-6700_memory-2GB_used.txt)

The memory usage you see in task manager of win7 and win10 is not real. You need to see it in resource monitor.

## xmrig | 2019-12-04T13:53:16+00:00
Both version use 2336 MB, but Windows Task Manager not show huge pages memory and you have enough memory for fast mode.
Thank you.

## aa-delite | 2019-12-05T12:41:44+00:00
I've noticed that my machines (ryzen) with ~2GB xmrig usage in task manager mining nothing with NULL hashrate and just swapping to disk.

## berezinevgeniy | 2019-12-05T16:12:26+00:00
> Both version use 2336 MB, but Windows Task Manager not show huge pages memory and you have enough memory for fast mode.
> Thank you.

Hello. Do yo know, how to monitor huge pages on windows 2008? I have 32GB of ram with over 25Gb free. But xmrig often start with 89% or 11% of memory allocation randomx threads. Restart helps, but this is not good decision. Can i find problem with any apps?

# Action History
- Created by: worm001 | 2019-12-04T04:00:55+00:00
- Closed at: 2019-12-21T20:03:22+00:00
