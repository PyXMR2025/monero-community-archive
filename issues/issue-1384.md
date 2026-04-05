---
title: Ryzen 3600 XMRIG crashes after a few seconds
source_url: https://github.com/xmrig/xmrig/issues/1384
author: kike818
assignees: []
labels:
- stability
created_at: '2019-12-05T03:52:26+00:00'
updated_at: '2020-08-31T05:48:46+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:48:46+00:00'
---

# Original Description
Hi Guys,

I am using xmrig v5.1.1, The miner crashes after a few seconds of mining.
Had same issue with version V5.1.0 and V5.0.1 
Large pages are enabled and virtual memory is at 8gb min 24gb Max

PC is the following
Ryzen 3600
Asus X470 mini itx
16GB or 3000Mhz memory
GTX 1070 Ti

![Capture](https://user-images.githubusercontent.com/47010842/70202789-94e07200-16cf-11ea-9247-b31a1b846d1a.PNG)




# Discussion History
## xmrig | 2019-12-05T04:27:53+00:00
It might be general stability issue especially if v5.0.1 affected too, please check your CPU temperatures, remove overclocking, increase memory timings, try move memory sticks to place recomented by motherboard manual, for example from A1 B1 to A2 B2.
Thank you.

## FabioFrmg | 2019-12-05T11:22:35+00:00
Something happened after change for RandomX algo specialy with AMD Ryzens. 
Im not mining from 30/11.
Many computers in my farm have the same issue here. 
xmrig.exe process autoclose after a little time of mining 
No matter if you use default system settings without overclock and good temps.

## aa-delite | 2019-12-05T12:35:06+00:00
It's ryzen segmentation fault issue. They think it only affects ryzen 1xxx series, but it's not. There are problems on different ryzen machines, segfault or null hashrate.
If you can find "opcache" in BIOS, you're lucky. You can disable it and everything will be ok. There is no another solution for today. You can also install latest amd chipset drivers and reboot few times. Sometimes it works for a while till next boot.

## list1999 | 2019-12-05T18:26:30+00:00
The system on Ryzen 1600 xmrig 5.1 disabling "opcache" in BIOS did not help me, but xmrig 5.1.1 works for 12 hours so far.

## FabioFrmg | 2019-12-05T23:26:33+00:00
> Sometimes it works for a while till next boot.
Why not make xmrig.exe compatible as windows service? 
In this way will be possible to set autorestart process forever. 



## xmrig | 2020-08-31T05:48:46+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: kike818 | 2019-12-05T03:52:26+00:00
- Closed at: 2020-08-31T05:48:46+00:00
