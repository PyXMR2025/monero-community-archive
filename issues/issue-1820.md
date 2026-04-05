---
title: Unstable hashrate on coffe lake cpu from run-to-run.
source_url: https://github.com/xmrig/xmrig/issues/1820
author: Moris-D
assignees: []
labels: []
created_at: '2020-08-31T13:32:53+00:00'
updated_at: '2021-04-12T14:50:22+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:50:22+00:00'
---

# Original Description
Unstable hashrate on coffee lake cpu from run-to-run (random-x).
Hello! 
When i run random-x algo on my core i5 or core i7 CPU coffee lake (U0 stepping) its gives me the different hashes (1900-3000 h/s on 9400F). I have to start the miner up to 5-6 times before i get the max hashes.

It's a quite easy to see this bug. Please check this. I hope this will be fix in the new version.

CPU I5 9400F/i7 8700 (U0)

OS Win 8/win 10 1709

xmrig version 5.1.0-6.3.1



# Discussion History
## Lonnegan | 2020-09-03T09:00:59+00:00
Has never been different with Coffee Lake. No idea why, but as I used an i7-8700 in early 2018 to mine Monero (Cryptonite at that time) I had the same problem with several different mining software. So it's not an issue with xmrig. Sometimes I had 350 H/s, then 270 H/s, then 420 H/s. Had to restart the miner several times to reach the "correct" hashrate. Perhaps an issue with data prefetching or something like that?

Never had such a problem with Haswell.

## Moris-D | 2020-09-05T13:14:52+00:00
I thought, maybe xmrig dev can give the answer. What is this? Software bug, or core design bug (coffee lake U0)? I just wanted to draw atention to the problem. Is it so hard to resolve that?

## SChernykh | 2020-09-07T07:49:02+00:00
Please check that huge pages are allocated 100% when xmrig starts. It can also be some other software running and taking CPU. I have never seen this problem on Pentium G5400 which is also Coffee Lake.

## Moris-D | 2020-09-07T13:50:50+00:00
> Please check that huge pages are allocated 100% when xmrig starts. It can also be some other software running and taking CPU. I have never seen this problem on Pentium G5400 which is also Coffee Lake.

Ofcourse huge pages are enabled and works (100% allocated). There are no other tasks in the windows task manager that use the cpu. I'm not the only one who sees this bug ;).
I saw this on two different system Core i5 9400F+b365 mobo/I7 8700+b360 mobo, Win 8/Win 10 1709. I tried all the settings in the config-file related to the cpu. Not one helped.
How many threads are you using? Can you try it on a coffe lake cpu which has more cores 6 or 8?
Can i attach some log-file? How can i create it?

## SChernykh | 2020-09-07T14:08:40+00:00
Can you post a screenshot of miner window when hashrate is low and normal (press `h` before making screenshot)? I don't have other Coffee Lake CPU to test.

## Moris-D | 2020-09-07T18:30:24+00:00
> Can you post a screenshot of miner window when hashrate is low and normal (press `h` before making screenshot)? I don't have other Coffee Lake CPU to test.

ok. everytime i run xmrig it gives me one of three different hashes (different, but each time one of these three) ~1900h/s, ~2450h/s or ~3000. And here they are:
1900 - https://ibb.co/ypVBdPX
2400 - https://ibb.co/9pJs1cr
3000 - https://ibb.co/V99BV8C
 

## SChernykh | 2020-09-07T18:39:16+00:00
- Try to set `"yield":false,` in config and if it doesn't help, change `"rx":[2,3,4,5],` to `"rx":[-1,-1,-1,-1],`
- Check what speed CPU is running at when hashrate is low and high

## Moris-D | 2020-09-07T18:51:23+00:00
> * Try to set `"yield":false,` in config and if it doesn't help, change `"rx":[2,3,4,5],` to `"rx":[-1,-1,-1,-1],`
> * Check what speed CPU is running at when hashrate is low and high

I tried to change "yield" option and cpu affinity (no affinity -1 -1 -1 -1). The CPU Frequency is fixed (all cores 3900Mhz) and doesn't drop.

## Lonnegan | 2020-09-07T23:48:38+00:00
As I've said already: the problem is years old and not miner related. I saw this with an i7-8700 system in early 2018 with different mining software. So I think it's not fair to report this as a bug in xmrig. I fear that it's a problem in Coffee Lake's prefetch mechanisms.

Only thing I haven't tried at that time: please deactivate SMT/HTT in BIOS/UEFI and try again. May be it's a locking issue in Intel's SMT implementation "HyperThreading". But I don't think so, because I didn't have that problem with Sandy Bridge, Ivy Bridge and Haswell, which had SMT/HTT, as well.

## SChernykh | 2020-09-08T07:58:05+00:00
@Moris-D I have no explanation yet for this issue, but I want you to try mining with only 1 thread and see if you get different hashrate each time.

## Moris-D | 2020-09-08T12:26:30+00:00
> As I've said already: the problem is years old and not miner related. I saw this with an i7-8700 system in early 2018 with different mining software. So I think it's not fair to report this as a bug in xmrig. I fear that it's a problem in Coffee Lake's prefetch mechanisms.

I agree. But maybe the xmrig dev will be the first who can solve this problem? :) If it possible. So bug report always makes sense.

# Action History
- Created by: Moris-D | 2020-08-31T13:32:53+00:00
- Closed at: 2021-04-12T14:50:22+00:00
