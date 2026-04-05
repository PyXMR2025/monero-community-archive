---
title: xmrig not working on randomx
source_url: https://github.com/xmrig/xmrig/issues/1345
author: DCress12
assignees: []
labels:
- bug
- opcache
created_at: '2019-11-30T21:55:13+00:00'
updated_at: '2019-12-02T14:54:14+00:00'
type: issue
status: closed
closed_at: '2019-12-02T14:54:13+00:00'
---

# Original Description
xmrig was working for me until the change to randomx. Now it starts but i get press any key to continue and the program shuts down. Can any one help?
![01](https://user-images.githubusercontent.com/49696768/69906566-2644a100-13bd-11ea-82e6-24df4f2ea37a.jpg)

 

# Discussion History
## maxfreemax | 2019-11-30T22:00:01+00:00
i have the same problem. W10 /ryzen 1700X
xmrig crash few second after strat.

when i try to mine directly with monerod.exe:. it crash too.

Ryzen 1700X is not compatible with randomX?


## xmrig | 2019-11-30T22:10:16+00:00
Some people was report crashes on first generation Zen CPUs (like your 1700X), but for many others it works fine, right now is no solution for it, you can try update BIOS, remove memory overclocking.
Thank you.

## maxfreemax | 2019-11-30T23:10:57+00:00
Ok thank
but no change after update motherboard BIOS.


## maxfreemax | 2019-11-30T23:30:08+00:00
i dont understand why, but after install this:

https://www.amd.com/en/support/cpu/amd-ryzen-processors/amd-ryzen-7-desktop-processors/amd-ryzen-7-1700x

xmrig seem more stable.



## builder2020 | 2019-12-01T01:56:21+00:00
Also on Ryzen 7 1700x, and xmrig will just crash/ close down/stop working with no error/log. Issue is intermittent - sometimes it will crash out immediately before hashing, sometimes will last an hour or so or can be anything in between.  

## xmrig | 2019-12-01T02:04:03+00:00
If you can compile from source please verify #1348
Thank you.

## lsylusiyao | 2019-12-01T10:32:08+00:00
It seems that my R7 1700 has the same problem.  Just like the situation @builder2020 has, it will crash casually, from immediately to after several accepts. Also, when I tried to start xmrig in a loop in cmd, my Win10 fell into BLUESCREEN again and again. So I can only stop mining now. Is there anything I can do? Thanks

## lsylusiyao | 2019-12-01T13:57:04+00:00
Not yet, maybe I can try using WSL before using a virtual machine. But I'm very curious that why I can run the xmrig for more than 2 hours this time after I commented.🤣

## Svaag | 2019-12-01T15:49:45+00:00
As suggested by @repsac-by in #1348 I got my 1700 to stop segfaulting by disable Opcache in bios under AMD CBS/CPU Common Options on my ASRock B450M Pro4.

## xmrig | 2019-12-01T22:27:02+00:00
Disabling opcache in BIOS should fix the issue, please verify https://github.com/xmrig/xmrig/pull/1348#issuecomment-560122919

## maxfreemax | 2019-12-01T23:19:52+00:00
as suggested (proposal #1348) i have disabled opcache (auto --> disabled) on motherboard BIOS
xmrig start with no crash at the first time

thanks!


## lsylusiyao | 2019-12-02T11:26:09+00:00
I've disabled Opcache. But it still seems very strange that my Win10 goes to BLUESCREEN nearly every 1 hour. I don't know what happened even when I access to the DMP, which shows me that some part of NT kernel goes wrong. I didn't catch this when I was using xmrig 4.x to mine the old XMR. 

## DCress12 | 2019-12-02T14:51:43+00:00
Disabled opcache (auto --> disabled) has worked for me. XMRig has been running stable for 24 hours now. Thanks for help :)

# Action History
- Created by: DCress12 | 2019-11-30T21:55:13+00:00
- Closed at: 2019-12-02T14:54:13+00:00
