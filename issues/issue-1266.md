---
title: Xmrig with dual Epyc 32core not possible ? Segmentation fault
source_url: https://github.com/xmrig/xmrig/issues/1266
author: theshadowpeople
assignees: []
labels:
- bug
- opcache
created_at: '2019-11-06T18:10:32+00:00'
updated_at: '2020-06-02T14:35:21+00:00'
type: issue
status: closed
closed_at: '2020-06-02T14:35:21+00:00'
---

# Original Description
I want to test my server with xmrig / RandomX but it fails.
![xmrig](https://user-images.githubusercontent.com/57456171/68324954-c19d6b80-00c8-11ea-9611-9aee27f227c9.png)

here is the topology

[topology.txt](https://github.com/xmrig/xmrig/files/3816067/topology.txt)

Does anyone have an idea why it doesn´t work?

With my dual Opteron 2x12core it works without any problems.

# Discussion History
## theshadowpeople | 2019-11-07T14:10:58+00:00
Now i have install Ubuntu Mate 18.04.03 LTS and it doesn't work too.
![pic](https://user-images.githubusercontent.com/57456171/68395819-c87fb900-0170-11ea-9b4c-13cfe445e2aa.png)

lshw File
[hardware.txt](https://github.com/xmrig/xmrig/files/3820099/hardware.txt)



## ari2asem | 2019-11-08T11:06:48+00:00
probably because it is ES cpu?

try another pool..
look ar reddit -->> moneromining -->> supportxmr testnet pool for more info

i am running dual socket epyc 7551 (retail, not ES) without problems

## theshadowpeople | 2019-11-08T18:26:34+00:00
Another Pool doesn't work too .... Maybe XMRIG don't like my engineering sample
Which mainboard do you have ?
With Ubuntu i get the massage "Speicherzugriffsfehler" i think the english translation is "segmentatio fault" but i have test my rams with memtest without any errors .....


## ari2asem | 2019-11-08T18:49:57+00:00
i have h11dsi, rev 1.0. ddr4-2666 MHz ecc-reg 10*  8gb RAM. w;ndows 10 v1903, 64 bit....try windows version xmrig msvc...maybe that should work....
yet another question...in general, is your system stable?? can you stress test your system (or cpu only) to exclude your cpu (or system) is having another problems except xmrig?

i  sorry, i dont use Linix at all

## theshadowpeople | 2019-11-08T22:16:30+00:00
yes my system are stable (tested with prime95) 
in Ubuntu Syslog i get this massage "kernel: [ 2220.824402] traps: xmrig[10126] general protection fault ip:7f2eb6379ac2 sp:7f2e9f7fddb0 error:0"

## ari2asem | 2019-11-09T08:25:17+00:00
can you try precompiled binaries of xmrig-msvc version on windows 10?

## theshadowpeople | 2019-11-09T19:43:40+00:00
I already tested and it doesn't work too. :( 

## ari2asem | 2019-11-09T20:03:10+00:00
can you try randomx benchmark tool? also available on github...and try also without large pages, so disable large pages....otherwise, mistery. probably becaus of ES

## pawelantczak | 2019-11-11T19:28:38+00:00
@theshadowpeople did you try with benchmark tool from RandomX github page?

## theshadowpeople | 2019-11-12T07:58:27+00:00
![xmrig3](https://user-images.githubusercontent.com/57456171/68652659-3ee23980-052a-11ea-9e4a-7740095843f6.png)
If i start RandomX benchmark v.1.1.1 with --nonces 5000 i get an result but if i start with --nonces 50000 that i get the same like xmrig .... nothing

## ari2asem | 2019-11-12T14:20:36+00:00
you need new cpu

## theshadowpeople | 2019-11-12T20:34:26+00:00
I can not explain it.... everything else is perfect .... Memtest86x, prime95 all benchmarks run without errors and normal score.
Is there any way to find out what exactly causes the crash?

## lss4 | 2019-11-17T01:17:55+00:00
Not sure about you CPU. I'm having this issue about 2 weeks ago on latest Manjaro Testing.

I've a 7551 and mine doesn't look like an engineering sample. It happened since kernel 5.4-rc6, before this everything was okay. Since this kernel onwards, xmrig would segfault after mining for about an hour.

I'm currently mining on 5.3 kernel (5.3.11) and I'm able to mine for at least 10 hours without a single segfault so far, with v4.5.0-beta.

EDIT: Just tested OpenCL appears to work with Navi (using v5.0.0) but very unstable.

EDIT 2: It's very likely that something in the 5.4-rc6/5.4-rc7 kernels that caused the segfault. I mined for more than 20 consecutive hours with 5.3.11 kernel without any issue. The EPYC never had any issue with mining ever since I got it.

EDIT 3: Since the transition to RandomX I haven't encountered a single segfault, with latest xmrig releases and kernels.

## SChernykh | 2019-11-25T16:30:53+00:00
@theshadowpeople Can you try to compile and test https://github.com/SChernykh/xmrig/tree/ryzen-fix ?

## xmrig | 2019-12-01T22:41:07+00:00
Disabling opcache in BIOS should fix the issue, not sure it possible on server motherboard, but please try https://github.com/xmrig/xmrig/pull/1348#issuecomment-560122919

## theshadowpeople | 2019-12-02T02:27:54+00:00
For me it doesn't work but the H11DSI has the option only with MOD BIOS and i am not sure if this option work correct.

## xmrig | 2019-12-22T19:32:18+00:00
Try recent version with `"wrmsr": ["0xc0011020:0x0", "0xc0011021:0x60", "0xc0011022:0x510000", "0xc001102b:0x1808cc16"]` more details about MSR https://xmrig.com/docs/miner/randomx-optimization-guide/msr
Thank you.

## SChernykh | 2019-12-30T10:18:21+00:00
@theshadowpeople XMRig 5.5.0 has a workaround for 1st gen Ryzen/Threadripper/EPYC crashes, you should be able to mine even with enabled Opcache.

# Action History
- Created by: theshadowpeople | 2019-11-06T18:10:32+00:00
- Closed at: 2020-06-02T14:35:21+00:00
