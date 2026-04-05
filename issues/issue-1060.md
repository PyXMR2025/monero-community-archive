---
title: Thread affinity slowing down RandomWOW when using more than 1 physical cpu
source_url: https://github.com/xmrig/xmrig/issues/1060
author: hecateh
assignees: []
labels:
- NUMA
- review later
created_at: '2019-07-15T21:09:50+00:00'
updated_at: '2019-08-02T12:40:11+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:40:11+00:00'
---

# Original Description
If I run xmrig on my quad cpu (DL560 gen 8, 4x E5-4650) and it set the affinity to more than is allocated to 1 cpu, in my case 0-15 for CPU 1 the hashrate collapses for every thread added, it currently runs at around ~400h/s per thread, if I add another thread affinity >15 the new thread and one of the originals slows to ~200h/s each, if I continue this up to the third cpu the hashrate tops out at around 2000h/s in total. If I run just 1 cpu with 8 threads I can get 3000h/s. To get around it so far, I have had to start 4 instances of xmrig with 4 different configs each with their own physical CPU.

This doesn't appear to happen on my dual CPU machines but I will take a look a them soon.

# Discussion History
## xmrig | 2019-07-29T02:14:17+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

## hecateh | 2019-07-29T08:28:59+00:00
This looks to be running better, it can now start one instance and runs on all 4 cpus, thanks!

## xmrig | 2019-07-29T08:49:33+00:00
Can you run command `lstopo topo.xml` from hwloc package and share `topo.xml` somehow, it might help improve autoconfig.
Thank you.

## hecateh | 2019-07-29T11:37:57+00:00


[topo.zip](https://github.com/xmrig/xmrig/files/3441833/topo.zip)

I have attached output from 2 systems I have.

## xmrig | 2019-07-29T12:38:55+00:00
Thank you.

## hecateh | 2019-07-30T13:16:36+00:00
[topo.zip](https://github.com/xmrig/xmrig/files/3446901/topo.zip)

Just for reference, I enabled HT on one of the systems and it now has 80 threads, I was getting errors saying windows cannot reference more than 63 threads, but I was still able to assign threads corresponding to the lstopo output as below:


 ```
  "rx/wow": [
            0,2,4,6,8,10,12,14,16,18,
		   20,22,24,26,28,30,32,34,36,38,
		   64,66,68,70,72,74,76,78,80,82,
		   84,86,88,90,92,94,96,98,100,102
```

I still get the error message but it works fine.

# Action History
- Created by: hecateh | 2019-07-15T21:09:50+00:00
- Closed at: 2019-08-02T12:40:11+00:00
