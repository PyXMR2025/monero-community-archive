---
title: '[Feature Request]  Add support for ''Cryptonight_Turtle'' for upcoming TRTL
  fork'
source_url: https://github.com/xmrig/xmrig/issues/904
author: lost-bro
assignees: []
labels:
- enhancement
- algo
created_at: '2019-01-10T23:50:16+00:00'
updated_at: '2019-02-22T10:35:40+00:00'
type: issue
status: closed
closed_at: '2019-02-22T10:35:40+00:00'
---

# Original Description
Sorry for the bother, just wanted to verify if we can expect an updated release of XMRIG compatible  with the upcoming TRTL coin fork in 21 days.
Thanks in advance

# Discussion History
## xmrig | 2019-01-11T07:40:46+00:00
Please provide information/announce about these changes.
Thank you.

## lost-bro | 2019-01-11T20:00:27+00:00
Block Major version 5 is planned to activate CryptoNight Turtle v2.
The move to variant 2 will help strengthen TurtleCoin’s ASIC/FPGA resistance. 
https://blog.turtlecoin.lol/archives/proof-of-work-algorithm-change/
We’re confident that we have the core code ready for the soft fork to CN Turtle tentatively scheduled for block 1,200,000.m
Next Network Upgrade In (est.)	20d 15h 48m 30s  (February 1st, 2019)

https://explorer.turtlecoin.lol/

## lost-bro | 2019-01-11T20:07:47+00:00
Just wanted to comment the STAK has already released his "crytponight_turtle" variant, but I would prefer to use XMRIG for auto-algo switching purposes.
Thanks


## fexra | 2019-01-11T20:20:38+00:00
https://github.com/turtlecoin/trtlrig

## brandonlehmann | 2019-01-11T20:21:34+00:00
https://github.com/turtlecoin/turtlecoin/issues/674

Release candidate for the fork is pending. Will complete and release any day now. 

## xmrig | 2019-01-12T04:34:07+00:00
@brandonlehmann As I understand new algorithm is cn/2 with different scratchpad size and iterations? or miner need support for all 12 algorithms, this part is unclear in blog. In any case test pool required and pull request is preferred even if it partially done.

@fexra this fork not contain any related changes.
@lost-bro `crytponight_turtle` is just alias to `crytponight-lite` variant `1`, currently also no support for upcoming fork.

## davehlong | 2019-01-12T05:27:53+00:00
@xmrrig - you are correct, new algo is cn/2 with changes to scratchpad and iterations. @brandonlehmann  and I have already implemented here https://github.com/plenteum/xmrig/commit/16a60cf59b7ba43aef1332b624cedbb03bc7d5f3, but it's hashing Much slower on my PC than the hash rates I am getting with the same changes added to xmr-stak. I think there is an issue with memory allocation, but have not had much chance to look into it yet.

For test pool you can use: 197.81.192.74:3333, this is a PLE testnet pool but is running CN TUrtle (Lite) same as Turtlecoin.

sample config file for testnet pool:
[config.txt](https://github.com/xmrig/xmrig/files/2751741/config.txt)



## lost-bro | 2019-01-12T17:04:00+00:00
![cn-trtl](https://user-images.githubusercontent.com/37913805/51076075-8b828d00-1659-11e9-8a25-eefbcb5324ac.png)
"Cryptonight_Turtle" (Variant_2) is the algo name used in the *TRTL-forked* version (for NEW TRTL algo of upcoming fork) of XMRIG.  Please see Screen shot from *TRTL-forked* version of XMRIG attached.

"Cryptonight_Turtle" (Variant_2) is NOT the same as "crytponight-lite variant 1".

The requested modifications to XMRIG do NOT require support for all 12 listed algos.  
The 12 listed algos are compatible w/TRTL blockchain, but are NOT implemented simultaneously.  
Thanks

## brandonlehmann | 2019-01-19T23:08:07+00:00
@xmrig  For reference, xmrigCC has support for the algo via https://github.com/Bendr0id/xmrigCC/commit/4c995ea44357aa5bfec0d38dda8356dbb6fe0c0e

I've also submitted a PR on xmr-stak via https://github.com/fireice-uk/xmr-stak/pull/2178 including test pool data

I'll see if we're able to apply the update to xmrig and open a PR; however, if we can't, your assistance is appreciated :)


## xmrig | 2019-01-20T07:58:09+00:00
I saw, due date for this issue is 23rd I will be unavailable after this date for about a week, some things eg ASM patching already prepared.

Smooth algorithm changing while fork will not possible, because memory requirements changed, also it means block version after fork doesn't mater for miner.
Thank you.

## YetAnotherRussian | 2019-01-22T08:29:02+00:00
@xmrig @SChernykh Please note that xmrig-CC implementation possibly got an asm-side issue for Ryzen - asm=off is faster than any other asm setting on Ryzen (this is cn-turtle ONLY issue). On any other CPUs (Bulldozer, Intel) asm usage gives some speed improvement. Maybe CPU family arch issue (memory bottlenecks or something), but if that is true then some algo-dependent switch is needed for Ryzen.

Huge pages count and scratchpad rounding (for cli output) is also broken there (xmrig-CC).

## SChernykh | 2019-01-22T09:09:03+00:00
Interesting. Smaller memory access time may mean different asm code is optimal, I can check it this week.

## xmrig | 2019-01-22T10:44:01+00:00
@YetAnotherRussian  Please provide details, CPU, config, hashrate, etc.
@Bendr0id

## SChernykh | 2019-01-22T11:50:08+00:00
I couldn't get better hashrate than with 2 single threads per core (asm=ryzen) no matter what I tried. asm=ryzen is 10% faster than asm=off on Ryzen 5 2600.

## YetAnotherRussian | 2019-01-22T13:04:21+00:00
Ryzen7 2700X stock, no overclock (mem 2666MHz dual-channel 2x16Gb 2rank plates), Win10

Best performance with:
"algo": "cryptonight-ultralite",
"aesni": 0,  
"threads": 32, 
"multihash-factor": 1,
"multihash-thread-mask" : null, 
"pow-variant" : "turtle",  
"asm-optimization" : "off", 
"background": false,
"cpu-affinity": null,
"cpu-priority": null,
"max-cpu-usage": 100, 

Total: 14250 h/s

If "asm-optimization" is set to "auto" or "ryzen" => 13200 h/s

Totals tolerance: ~100h/s

## xmrig | 2019-01-23T08:09:40+00:00
It might be xmrig-CC only related issue, I get exactly same hashrate (about 14250) on Ryzen7 2700X with same hardware config, only difference is Ubuntu 18.04 and asm `bulldozer`. Asm `ryzen` is slowest (about 13600).

Pure C++ version always slower, only about 10000 H/s.

## Bendr0id | 2019-01-23T09:19:55+00:00
Here are my results with XMRigCC 1.8.10. 
Ubuntu is for me on Ryzen always slower than MVC version on Windows. For Intel i can't see a difference.

Tests are performed under Windows 10. 

Configuration | Ryzen 1600 3.8GHz | Ryzen 2600 3.85GHz | Ryzen 2700 4.1GHz
-- | -- | -- | --
threads:12 , ASM: Ryzen , hf:1 | 9,560 h/s | 10,065 h/s | 11,003 h/s
threads:16 , ASM: Ryzen , hf:1 | 9,542 h/s | 10,022 h/s | 14,041 h/s
threads:24 , ASM: Ryzen , hf:1 | 9,521 h/s | 10,035 h/s | 14,010 h/s
threads:32 , ASM: Ryzen , hf:1 | 9,532 h/s | 10,060 h/s | 14,009 h/s
threads:12 , ASM: off , hf:1 | 8,861 h/s | 9420 h/s | 10,068 h/s

Hashfactor 2, was always slower.

So i can't reproduce it either.




## xmrig | 2019-01-23T13:43:51+00:00
v2.10.0 released
https://github.com/xmrig/xmrig/releases/tag/v2.10.0
https://github.com/xmrig/xmrig-amd/releases/tag/v2.10.0
https://github.com/xmrig/xmrig-nvidia/releases/tag/v2.10.0
https://github.com/xmrig/xmrig-proxy/releases/tag/v2.10.0

New algorithm name is `cn-pico/trtl`, alternative names `cryptonight-turtle`, `cn-trtl`, `cryptonight-ultralite`, `cn-ultralite`, `cryptonight_turtle` also supported.

## brandonlehmann | 2019-01-23T14:10:51+00:00
Thanks! @xmrig 

## lost-bro | 2019-01-23T17:36:04+00:00
@xmrig , Much appreciated


## asylum119 | 2019-01-25T19:24:27+00:00
All I get with the latest compile using config.json is "no valid algorithm specified. Exiting" 

Loading via command gives a no config.json file or directory error because the algo is not recognised.

xmrig-amd works fine.

## snipeTR | 2019-01-25T19:42:25+00:00
Please paste json to code

## asylum119 | 2019-01-25T19:51:20+00:00
After having no luck with the aliases on command I tried the config.json already posted ^. Again algo was not recognised



## asylum119 | 2019-01-25T21:00:10+00:00
Might have been a compile issue, I recompiled and all is good. 

## browolf | 2019-01-25T22:04:36+00:00
I had  "no valid configuration found" until I realized variant needs to be "-1"  




# Action History
- Created by: lost-bro | 2019-01-10T23:50:16+00:00
- Closed at: 2019-02-22T10:35:40+00:00
