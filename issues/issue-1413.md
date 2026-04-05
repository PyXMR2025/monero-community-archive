---
title: Disabling Hardware Prefetch in BIOS question
source_url: https://github.com/xmrig/xmrig/issues/1413
author: setuidroot
assignees: []
labels: []
created_at: '2019-12-13T19:47:50+00:00'
updated_at: '2020-02-02T16:15:55+00:00'
type: issue
status: closed
closed_at: '2020-01-02T13:44:55+00:00'
---

# Original Description
I have some HP Proliant DL385 G7 servers (they are dual socket AMD Opteron 6276.)

The AMD Opteron 6276's are 2.3 GHz 16 "core" (8 modules of 2 shared resource cores) / 16 thread CPUs with 16MB of L2 and 16MB L3 cache.  Each CPU has 2 NUMA nodes and four memory channels (total 4 NUMA nodes per server.)

Anyways... I went to disable prefetching in the BIOS and I didn't know which ones to disable 🤔 there are 5 different options:

````
Hardware prefetch training on software prefetch
DRAM Prefetch on CPU Request
DRAM Prefetch on I/O Request
CPU Core Hardware Prefetcher
CPU Cache Stride Prefetcher
````
I'm also not sure if it's better to have "Node Interleaving" (or "channel interleaving" for that matter) enabled or disabled.

I have always had node interleaving disabled and channel interleaving enabled.  My systems only have 8 DIMM sticks (4 per CPU, one in each memory channel) some of my servers have 8 1GB RAM sticks (8GB total) and others have 8 2GB RAM sticks (16GB total.)  Obviously I prefer the 16GB configurations because I can run 4 RandomX datasets (one for each NUMA node.)  But the 8GB servers I run with either 2 datasets (one per socket) or some I just have NUMA disabled and it runs with 1 dataset for the whole server (but that server has a bad memory channel on one of the CPUs.)

Anyways, I tried disabling all 5 of the above listed BIOS prefetch options and it lowered my hashrate, so I tried it now with both of the DRAM Prefetch options enabled again.  The hashrate is about the same, still lower than before I messed with it.  Here is a picture of the BIOS options:

![Screenshot_20191213-132911](https://user-images.githubusercontent.com/32213080/70827035-00040580-1dae-11ea-915e-753f95909e75.png)

Any recommendations on which I should disable and which I should leave enabled?  @SChernykh ?

I read where it says: 
````
"Always disable Hardware Prefetcher and Adjacent Cache Line Prefetch in BIOS to get the optimal performance." 
````

But my AMD Opteron (HP Proliant) BIOS isn't so simple 😕

I appreciate any suggestions.  I guess I'll just try any/all combinations of these options, but it takes forever for these servers to post 🙄



# Discussion History
## SChernykh | 2019-12-13T20:02:20+00:00
Hardware prefetcher and stride prefetcher can be disabled, but DRAM prefetch on CPU request needs to be left enabled.

## setuidroot | 2020-01-02T13:44:55+00:00
Just as an update: I got best hashrate with these 3 settings disabled:
````
Hardware prefetch training on software prefetch
CPU Core Hardware Prefetcher
CPU Cache Stride Prefetcher
````

And these two left enabled:
````
DRAM Prefetch on CPU Request
DRAM Prefetch on I/O Request
````

The difference is very small.  Overall disabling all 3 gave me about 35-40 H/s faster (on RX/0.)  Total hashrate with two AMD 6276 CPUs is currently ~4940 H/s.

My advice is don't buy these Opterons for mining unless you have free power.  At ~115 watts per CPU... it's losing money even at my low energy cost.  But it's winter time lol.

Also, I got a more pronounced hashrate boost by switching from Ubuntu 18.04 LTS to Lubuntu 19.10.  The lighter desktop environment helps undoubtedly (but I disable the DE service anyways.)  I think the newer 5.3.0 Linux Kernel helps and works better with the default GCC 9.2.1.  There's also entropy helping randomness systemd service on default Lubuntu 19.10 called "Haveged" ... I think that might explain the hashrate boost from Ubuntu 18.04 (but maybe not.)  

Ubuntu 18.04: 4772 H/s
Lubuntu 19.10: 4940 H/s

Both of those are with the 3 BIOS prefetch options disabled.  I recommend the upgrade (no stability issues at all.)


I've got a few more potential hashrate boosters for Linux users... if they pan out I'll make PRs and/or post help how-to guides.

I'm closing this anyways.  Thank you SChernykh for the nudge in the right direction.  Keep up the awesome work xmrig dev guys! 

## Imperium20 | 2020-02-02T16:15:54+00:00
Have you tried with TurionPowerControl -psmax 1 ?

I guess that Hardware prefetch training on software prefetch should remain enabled as well.

# Action History
- Created by: setuidroot | 2019-12-13T19:47:50+00:00
- Closed at: 2020-01-02T13:44:55+00:00
