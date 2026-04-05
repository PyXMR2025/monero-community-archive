---
title: 2 x Xeon E5 2620 V3 - 270h/s? How to setup second CPU?
source_url: https://github.com/xmrig/xmrig/issues/1854
author: K-morpse
assignees: []
labels: []
created_at: '2020-09-26T20:00:13+00:00'
updated_at: '2020-10-01T15:25:06+00:00'
type: issue
status: closed
closed_at: '2020-10-01T15:25:06+00:00'
---

# Original Description
Hi everyone!

I got 2 x  HP Z640 with  Xeon 2620 v3 (6C/12T 15Mb L3) yesterday and i want them to work on XHV but i can't find proper desription how to setup XMrig. I was looking for it for hours now and i'm just keep circulation between the same links without any succes. So i downloaded the latest XMrig I tried it and the result was 150h/s. It might be because of the missing adjustment of the CPU-s. When i start the miner its shows only 1 NUMA node which i guess should be more due i have 2 CPU each PC. 
If someone would help me to set i would be greatfull.


# Discussion History
## K-morpse | 2020-09-27T12:41:50+00:00
So now its working with apr.: 300hs/s on XHV and see the second NUMA node when the Xmrig starts, but when i'm checking the taskmanager i see only one CPU is working with full load, the other is around 4%. How can i start the other CPU aswell? Thanks

## Lonnegan | 2020-09-28T21:57:47+00:00
Hi,

you shouldn't mine Haven (XHV) with your Xeon CPU. Haven is a GPU algo. Radeon Vega 56/64 hashes around 1500-1800 H/s.

XHV is a Cryptonight Heavy derivate, which means, you need plenty of cache if you want to mine via CPU; 4 MB last level cache for each thread! Your Xeon 2620-v3 has only 15 MB L3 cache, which means, xmrig can only start 3 threads per CPU without flooding the cache (or 12 and flooding it as much as it can LOL). EVEN THE AMD EPYC 7601, which has 64 MB L3 cache and as a modern 32c/64t CPU has higher IPC only reaches about 900 H/s.

I'd mine Wownero with your CPU. That should load the ressources of your CPU in the best way :)

## agentpatience | 2020-09-29T00:58:11+00:00
I’m not mining haven?!

Sent from my iPhone

> On Sep 28, 2020, at 5:58 PM, Lonnegan <notifications@github.com> wrote:
> 
> ﻿
> Hi,
> 
> you shouldn't mine Haven (XHV) with your Xeon CPU. Haven is a GPU algo. Radeon Vega 56/64 hashes around 1500-1800 H/s.
> 
> XHV is a Cryptonight Heavy derivate, which means, you need plenty of cache if you want to mine via CPU; 4 MB last level cache for each thread! Your Xeon 2620-v3 has only 15 MB L3 cache, which means, xmrig can only start 3 threads per CPU without flooding the cache (or 12 and flooding it as much as it can LOL). EVEN THE AMD EPYC 7601, which has 64 MB L3 cache and as a modern 32c/64t CPU has higher IPC only reaches about 900 H/s.
> 
> I'd mine Wownero with your CPU. That should load the ressources of your CPU in the best way :)
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub, or unsubscribe.


## Lonnegan | 2020-09-29T05:24:45+00:00
"i want them to work on XHV ", you said in the first post?! XHV is Haven!

## K-morpse | 2020-09-29T05:28:13+00:00
Easy lads, i am the idiot who's mining xhv on CPU :D

## K-morpse | 2020-09-29T05:30:01+00:00
> "i want them to work on XHV ", you said in the first post?! XHV is Haven!

Thanks for the advice btw. I'm gonna try wowmonero this afternoon. What miner would be ok for me?

## Lonnegan | 2020-09-30T14:49:34+00:00
> I'm gonna try wowmonero this afternoon. What miner would be ok for me?

xmrig? ;)



## K-morpse | 2020-10-01T15:20:53+00:00
> > I'm gonna try wowmonero this afternoon. What miner would be ok for me?
> 
> xmrig? ;)

It doesn't really wanna work with xmrig, but xmstak doin apr. 5-6khs/s on 83% load of the CPUs. Now i have to find a reliable wallet.

# Action History
- Created by: K-morpse | 2020-09-26T20:00:13+00:00
- Closed at: 2020-10-01T15:25:06+00:00
