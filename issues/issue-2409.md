---
title: the software keeps closing
source_url: https://github.com/xmrig/xmrig/issues/2409
author: Liger0
assignees: []
labels: []
created_at: '2021-05-25T19:31:51+00:00'
updated_at: '2021-05-25T20:07:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
The software keeps closing, after a bunch of minutes. No crash, no hang, straight close.
I use a ryzen 5 1600 and wanted to give it a try. I set it up to only use the CPU so I can eventually mine with the gpu at the same time on a different currency and software.
The CPU is stock, I did test both CPU and RAM and they are totally stable for hours at any stress level and software, the CPU during the mining never went above 70°C.
It's the same if I mine with gpu or not while it closes. If I GPU mine the gpu keeps going fine, without hang, crash, driver errors etc.
Other software that I use while mining also go fine.

**To Reproduce**
I just let it run for some minutes...

**Expected behavior**
It shouldn't close

**Required data**
 - Miner log as text or screenshot -> How do I make a log???
 - Config file or command line (without wallets)
[config.zip](https://github.com/xmrig/xmrig/files/6541887/config.zip)

 - OS: Windows 10
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2021-05-25T19:38:25+00:00
It's explained in **Faulty first gen Zen CPUs** section of https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide
Try to disable Opcache in BIOS.

## Liger0 | 2021-05-25T19:45:31+00:00
I'll try to find it in the bios and report back. Thank you.
Is it the problem that was in the early versions of Ryzen 5 1600? It's referred as a linux compatibility issue. I heard the first months AMD swapped them under warranty, but the later months they were fixed by factory (I'm not talking about the AF version).
In such case my cpu was produced the second half of the factoring year so it's weird.

## Liger0 | 2021-05-25T20:02:29+00:00
> 
> 
> It's explained in **Faulty first gen Zen CPUs** section of https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide
> Try to disable Opcache in BIOS.

I disabled it, now the hashrate is constant on 3000 H/s instead of the previous 15000 H/s, is it normal?

## SChernykh | 2021-05-25T20:05:01+00:00
https://xmrig.com/benchmark?cpu=AMD+Ryzen+5+1600+Six-Core+Processor
Disabled opcache reduces hashrate, but you should still get ~4000 h/s with huge pages enabled. 15000 h/s is impossible on that CPU unless you're mining some other coin.

## Liger0 | 2021-05-25T20:07:50+00:00
My bad, but it was 4500 H/s before.

# Action History
- Created by: Liger0 | 2021-05-25T19:31:51+00:00
