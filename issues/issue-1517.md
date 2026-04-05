---
title: Access Violation errors
source_url: https://github.com/xmrig/xmrig/issues/1517
author: charminULTRA
assignees: []
labels: []
created_at: '2020-01-25T19:16:00+00:00'
updated_at: '2020-01-27T02:38:53+00:00'
type: issue
status: closed
closed_at: '2020-01-27T02:38:53+00:00'
---

# Original Description
Hi - I'm getting access violation errors, does anyone know what this is and why so I can fix it? Happens right after XMRig is started. After this it crashes.

"[2020-01-25 14:12:47.242]  rx   dataset ready (3289 ms)
[2020-01-25 14:12:47.243]  cpu  use profile  rx  (8 threads) scratchpad 2048 KB
[2020-01-25 14:12:47.455]  cpu  READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (213 ms)
[2020-01-25 14:13:09.274] [THREAD 13912] Access violation at 0x000001BFAB5050A7: write at address 0x000001C047099201
[2020-01-25 14:13:47.404] speed 10s/60s/15m 4033.2 n/a n/a H/s max 4450.1 H/s
[2020-01-25 14:14:15.814] [THREAD 13912] Access violation at 0x00007FF617693242: write at address 0x0000000000134900"

# Discussion History
## 2010phenix | 2020-01-25T22:59:23+00:00
man, need some more than just error address...
what version you use, on what system, how much RAM you have and etc....

## charminULTRA | 2020-01-26T17:12:08+00:00
> man, need some more than just error address...
> what version you use, on what system, how much RAM you have and etc....

Sorry about that:

XMRig Version 5.5.1 within a root folder (C:/FOLDER)
AMD Ryzen 5 (Zen1) system with 16GB RAM - No OCing
Windows 10

Attached is my actual log from [XMRig.]([url](url
[xmrig.log](https://github.com/xmrig/xmrig/files/4113785/xmrig.log)

I'm running the CLI daemon on the Monerod side. 

## charminULTRA | 2020-01-26T17:52:33+00:00
[config.txt](https://github.com/xmrig/xmrig/files/4113907/config.txt)

Here's the config file I'm using

## 2010phenix | 2020-01-26T23:50:54+00:00
you have AMD Ryzen 5 1600X, thay have problem...
Is 3-5 issues about CPU and few answer how to fix, us remember need disabling "opcache" in BIOS

in issues search write "Ryzen 5" and try few solution....

## charminULTRA | 2020-01-27T02:38:53+00:00
> you have AMD Ryzen 5 1600X, thay have problem...
> Is 3-5 issues about CPU and few answer how to fix, us remember need disabling "opcache" in BIOS
> 
> in issues search write "Ryzen 5" and try few solution....

That was it, thanks!


# Action History
- Created by: charminULTRA | 2020-01-25T19:16:00+00:00
- Closed at: 2020-01-27T02:38:53+00:00
