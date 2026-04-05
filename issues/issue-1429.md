---
title: Switching between coins slows the hash rate at random (using moneroocean)
source_url: https://github.com/xmrig/xmrig/issues/1429
author: 1alphabot
assignees: []
labels: []
created_at: '2019-12-16T01:32:54+00:00'
updated_at: '2021-04-12T15:09:06+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:09:06+00:00'
---

# Original Description
H/s drops from ~5000 to under 100 after random number of switches between coins on moneroocean (specifically from Monero to Loki and back and forward etc). when i say random number of changes it can go all day without a problem (with many many changes) and other times it can slow down after a couple of changes

I've tried the "memory-pool": true, option as previously suggested and that doesnt make any difference

I am using 5.1.0, ryzen 2700x, 16gb ram, win10, no gpu mining

# Discussion History
## flippp0 | 2019-12-17T20:10:07+00:00
the same (13000 to ~500) happened twice to me when my ISP dis/reconnected me resulting in a different IP. Happened mining 2 different coins on 2 different pools. No moneroocean. A (p)ause -> (r)esume fixed it. But its strange..
When reconnecting to my ISP manually (also getting a new IP) xmrig stays fine at 13000.
5.4.0-dev, Ryzen 3900x, win10, keepalive=true, tls=false

## 1alphabot | 2019-12-17T20:35:07+00:00
i've never tried a pause, resume - i just restart the miner. i guess not much difference in time but still it's a pain

## Spudz76 | 2019-12-17T23:04:34+00:00
No issues on Intel CPUs, I run many and have not seen this problem.  Voting it's a Ryzen specific thing.

## 1alphabot | 2019-12-19T23:47:38+00:00
just in case others are having the same issue (so it appears), i've changed to 5.3.0 and since then i haven't had the slow down in hash rate. it has only been 2 days though...

## 1alphabot | 2019-12-20T00:35:38+00:00
of course - spoke too soon.  still an issue with 5.3.0 on a ryzen 2600 machine

first picture shows a drop from ~4600 to 3000 for no reason (slowly increases to 3400)
second picture shows it drop from that 3400 to next to nothing (without a change of coin)
last picture shows how a pause resume brings it back up to ~4600

![1](https://user-images.githubusercontent.com/45726218/71220354-f3366300-2313-11ea-86db-eb7f8ab591af.jpg)

![1a](https://user-images.githubusercontent.com/45726218/71220452-3a245880-2314-11ea-97ca-874d7c25f005.jpg)

![2](https://user-images.githubusercontent.com/45726218/71220466-47d9de00-2314-11ea-97eb-d209448d838c.jpg)

## SChernykh | 2019-12-20T08:30:13+00:00
@1alphabot I see it's MoneroOcean pool on the screenshot. Is it stock XMRig or MoneroOcean's modded version?

## 1alphabot | 2019-12-20T23:45:16+00:00
it's the proper xmrig version

## 1alphabot | 2019-12-23T21:11:22+00:00
and so it appears to be the same as the other thread - it's slowing down without switching coins now.

also, what might be a trigger - it slows down at random, but if i use the computer it speeds back up. below is a picture from my 2700x machine

![Untitled](https://user-images.githubusercontent.com/45726218/71380779-4eba6680-261c-11ea-989d-de5b0711a50b.jpg)

## 1alphabot | 2019-12-27T04:36:38+00:00
i found something that's stopped the slow down for the past 2 days - i was running xmrig with "below normal" in the priority in the taskmanager (as I use the computers as well - they arent pure mining machines).

I have since changed that to "above normal" and I'm no longer getting the slow down....for now at least

## SChernykh | 2019-12-27T11:01:13+00:00
> i found something that's stopped the slow down for the past 2 days - i was running xmrig with "below normal" in the priority in the taskmanager (as I use the computers as well - they arent pure mining machines).
> 
> I have since changed that to "above normal" and I'm no longer getting the slow down....for now at least

If switching to "above normal" priority fixes the issue then some other process starts using CPU from time to time on your system. Higher than normal priority just helps XMRig to keep using CPU instead of that process.

## 1alphabot | 2019-12-29T02:05:20+00:00
update - another 2 days with above normal priority - no slow down of mining.

## crocket | 2021-02-18T07:25:00+00:00
Are you sure that other processes weren't competing hard with xmrig?

# Action History
- Created by: 1alphabot | 2019-12-16T01:32:54+00:00
- Closed at: 2021-04-12T15:09:06+00:00
