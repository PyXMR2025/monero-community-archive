---
title: 5.3.0 crashing after running in administrator mode Ryzen 1700x
source_url: https://github.com/xmrig/xmrig/issues/1425
author: DCress12
assignees: []
labels:
- bug
created_at: '2019-12-15T20:14:10+00:00'
updated_at: '2019-12-30T10:17:17+00:00'
type: issue
status: closed
closed_at: '2019-12-17T22:28:20+00:00'
---

# Original Description
xmrig crashes after I right click run as administrator on xmrig.exe. It is running on Ryzen 1700x

It runs fine if a double left click to run but get the yellow warning that it needs to be run as administrator.

A have a 2nd machine running a Ryzen 3900x this is running with out a problem on 5.3.0 as administrator.

# Discussion History
## SChernykh | 2019-12-15T22:04:53+00:00
MSR mod appears to enable Opcache, so if you had it disabled in BIOS for 1700X to fix crashes, you can't use MSR mod unfortunately. Try with `"wrmsr":false` in config.json

## DCress12 | 2019-12-15T22:27:13+00:00
You are correct that I have needed to disable Opcache.

 "wrmsr":false has stopped the crash when run as administrator but it is giving me lower h/s  

## GjBrutello | 2019-12-16T00:10:18+00:00
Many old Xeon E56.. processors have about the same issue, if xmrig.exe running as Services (system account) or added to schtasks with high privileges it get crash after 2-3 min. "wrmsr":false did not help. Now need to be logged as user to work it perfectly.

## aa-delite | 2019-12-16T00:37:50+00:00
Confirmed, have also Ryzen 1700X. Opcache disabled, but 5.3.0 crashes anyway. 
Crashes with / without WinRing0x64.sys.
Crashes with Opcache enabled / disabled.
Crashes anyway.
5.1.0 works fine with Opcache disabled.

## SChernykh | 2019-12-17T06:23:21+00:00
Note that you need to reboot once you've run 5.3.0 with MSR mod enabled. Opcache stays enabled until reboot after that.

## DCress12 | 2019-12-17T08:00:06+00:00
> Note that you need to reboot once you've run 5.3.0 with MSR mod enabled. Opcache stays enabled until reboot after that.

Sorry I do not understand this. Could you reword it. Thanks. 

## SChernykh | 2019-12-17T08:09:48+00:00
If you run 5.3.0 and get crashes on 1700X, all other versions will start crashing too until you reboot.

## DCress12 | 2019-12-17T17:16:15+00:00
I can get 5.3.0 running without problems. The problem is that it will crash if I run as administrator to allow MSR write so I would like to get the write MSR registers to work. 

## SChernykh | 2019-12-17T17:27:09+00:00
Yes, I'm working on it. I just need to find out which bit in MSR registers is responsible for Opcache on/off. Can you download dev buid from here: https://download.xmrig.com/xmrig/5.4.0-dev/3cc8b19ca00191241fedfbec152df0b1c787444d/ (user: `xmrig`, password: `download`), set `"verbose":1` in config.json (at the bottom), `"url": "randomx-benchmark.xmrig.com:7777"` then run it as administrator with Opcache disabled in BIOS, then paste here full console output? Then reboot, enable Opcache in BIOS, repeat and paste full console output again? I just need to compare MSR register values with Opcache on/off.

## DCress12 | 2019-12-17T17:35:03+00:00
Will get on it tonight. Can you tell me how to do the full console output thing?

Thanks for your time :) 

## SChernykh | 2019-12-17T17:39:08+00:00
You can just make a screenshot of XMRig window, I only need to see all MSR register values on this screenshot.

## DCress12 | 2019-12-17T19:53:17+00:00
Opcache disabled

![xmrig Opcache disabled](https://user-images.githubusercontent.com/49696768/71029121-a2055400-2106-11ea-9d02-6dac5920be07.jpg)

Opcache enabled]

![xmrig Opcache enabled](https://user-images.githubusercontent.com/49696768/71029188-c7925d80-2106-11ea-81e0-f0083ad38525.jpg)



## xmrig | 2019-12-17T19:59:18+00:00
@DCress12 Can you make screenshot with disabled Opcache again, it looks like it not first miner run after reboot, only first run required, because MSR mod values already applied, if miner crash it not revert initial values.
Thank you.

## DCress12 | 2019-12-17T20:10:54+00:00
> @DCress12 Can you make screenshot with disabled Opcache again, it looks like it not first miner run after reboot, only first run required, because MSR mod values already applied, if miner crash it not revert initial values.
> Thank you.

To confirm you want me to disable Opcache  and run as administer? 

## xmrig | 2019-12-17T20:15:32+00:00
Yes disable Opcache, then screenshot before miner crashed, if it crashed before you make screenshot reboot and try again.
Thank you.

## DCress12 | 2019-12-17T20:24:05+00:00
![xmrig Opcache disabled 02](https://user-images.githubusercontent.com/49696768/71031374-2954c680-210b-11ea-8680-97ec68566954.jpg)


## aa-delite | 2019-12-17T20:25:23+00:00
**NOT_CLEAN_RESTART** opcache **off**
![NOT_CLEAN_RESTART_opcache_off1](https://user-images.githubusercontent.com/20845944/71031307-f293a600-2134-11ea-97bf-b6597bf80325.png)

**CLEAN_RESTART** opcache **off**
![CLEAN_RESTART_opcache_off](https://user-images.githubusercontent.com/20845944/71031326-faebe100-2134-11ea-8a4c-557a69694694.png)

**CLEAN_RESTART** opcache **ON**
![CLEAN_RESTART_opcache_on](https://user-images.githubusercontent.com/20845944/71031342-0212ef00-2135-11ea-93e1-f93b5aa9c8f2.png)

Stopped mining both opcache enabled/disabled if msr enabled.
Mining with opcache disabled, msr disabled, clean restart.



## xmrig | 2019-12-17T20:30:32+00:00
@DCress12 @aa-delite all required data received, now need some time for thinking. Thank you. 

## SChernykh | 2019-12-17T20:57:30+00:00
@DCress12 @aa-delite Can you try `"wrmsr": ["0xc0011020:0x0", "0xc0011021:0x60", "0xc0011022:0x510000", "0xc001102b:0x1808cc16"]` in config.json? It should apply MSR mod _and_ disable opcache at the same time.

## aa-delite | 2019-12-17T21:33:59+00:00
> @DCress12 @aa-delite Can you try `"wrmsr": ["0xc0011020:0x0", "0xc0011021:0x60", "0xc0011022:0x510000", "0xc001102b:0x1808cc16"]` in config.json? It should apply MSR mod _and_ disable opcache at the same time.

Sure. Should opcache be enabled or disabled in BIOS to try?

## SChernykh | 2019-12-17T21:53:05+00:00
You can try with disabled in BIOS first, just use the same dev version. You can even try with enabled opcache, it should work too because MSR mod should disable it with these register values.

## aa-delite | 2019-12-17T22:11:37+00:00
Tried that string with opcache disabled. Mining well.
![registers](https://user-images.githubusercontent.com/20845944/71038640-17dbe080-2144-11ea-89b7-b0f255a458bb.png)

![newtest](https://user-images.githubusercontent.com/20845944/71038517-d1868180-2143-11ea-92ab-298a109a54c5.jpg)


## SChernykh | 2019-12-17T22:13:20+00:00
Thanks, I think we figured it out. The fix will be in the next release.

## DCress12 | 2019-12-17T22:28:00+00:00
It has worked for me. Thanks for sorting this out :) 

## xxb | 2019-12-29T14:12:38+00:00
5.4.0 crashes anyway
I use 1700X and ASUS X370

## SChernykh | 2019-12-29T14:57:49+00:00
@xxb It's fixed in dev branch, wait for 5.5.0 release.

## SChernykh | 2019-12-30T10:17:17+00:00
@DCress12 @aa-delite XMRig 5.5.0 has a workaround for 1st gen Ryzen crashes, you should be able to mine even with enabled Opcache.

# Action History
- Created by: DCress12 | 2019-12-15T20:14:10+00:00
- Closed at: 2019-12-17T22:28:20+00:00
