---
title: 'how to config '
source_url: https://github.com/xmrig/xmrig/issues/73
author: hoangcao243
assignees: []
labels:
- NUMA
created_at: '2017-08-29T05:13:27+00:00'
updated_at: '2017-11-27T19:37:54+00:00'
type: issue
status: closed
closed_at: '2017-09-03T03:16:12+00:00'
---

# Original Description
Hello everybody,

I'm brand new to this so please educate me.
I've been trying to read all the issue and download hwloc and have result below.

I have dell r410 with 2 cpus xeon x5650 6 cores 12 threads each cpu, 12 cores, 24 threads total (well i believe it's one main board however running hwloc it shows 2 nodes).

I have set the affinity to 0xFFFFFFFFFFFF
When I have threads at 24, cpu loads fully at 100% but the hs drops from 400 to 80.
seems like when i set threads at 12 i get the best results.
Running 1 instance with 12 threads i get 460hs, however cpus lload maybe at 79-80%
 Running 2 instances i get one at 460 and other at around 150 and now cpus load fully at 100% 

![node](https://user-images.githubusercontent.com/29996277/29805237-5399b56e-8c3d-11e7-8a2d-693a97df09db.PNG)
![thread](https://user-images.githubusercontent.com/29996277/29805247-6ced59da-8c3d-11e7-9b64-59ac0ad14483.PNG)

Should I change anything in order to run 1 instance and get max hs?
thank you


# Discussion History
## xmrig | 2017-08-29T16:21:17+00:00
Related issue #57 currently work with NUMA with single instance not supported.
You need run 2 instances and pin it to each node.
Thank you.

## hoangcao243 | 2017-08-29T23:32:22+00:00
thank you very much for your prompt reply.
Does that mean i just need to add the line "start/node 1" in the start.cmd file ?
I do not need to configure the file config.json correct? 

## xmrig | 2017-08-29T23:46:15+00:00
That right `start /node 0`, `start /node 1`. Also 6 threads per CPU/Node is optimal, because of 12 MB L3 cache, each thread required 2 MB cache for optimal performance, more threads less hashrate. So 12 threads is optimal anyway, just need separate it.

## hoangcao243 | 2017-08-30T00:20:59+00:00
Thank you for your very quick reply.
Please educate me, i don't seem to make it run when added start /node 0, start /node 1 in the .cmd file
i have my file like this

-p x --threads=12 start /node 0 start /node 1 --av=1--no-huge-pages --max-cpu-usage=100 --cpu-affinity 0xFFFFFFFFFFFF

![cmd](https://user-images.githubusercontent.com/29996277/29849850-6a2a6cd2-8cde-11e7-83dc-8da9bee56f16.PNG)


## xmrig | 2017-08-30T00:31:39+00:00
Something like:
```
start /node 0 xmrig.exe --threads=6
start /node 1 xmrig.exe --threads=6
```
Check first without `--cpu-affinity`.

## hoangcao243 | 2017-08-30T00:47:42+00:00
I just tried both times with and without affinity. Both time gave me same result about 480 total for 2 cmd.
However the cpus only load at about 56%. 
If i change the thread up to 12. The cpus will load at 100% but hs drops to 160hs total for 2 cmd?
Maybe there is something else I should do?

![mining](https://user-images.githubusercontent.com/29996277/29850388-267be7d2-8ce2-11e7-9972-aed7f86d974a.PNG)



## xmrig | 2017-08-30T00:57:14+00:00
12 threads and about 50% visible CPU load it's ok, no need more, because cache 100% used. 480H/s is good result for these CPUs too.

You can try `--cpu-affinity=0x555` for both cmd or `--cpu-affinity=0x555` for first and `--cpu-affinity=555000` for second. Both 6 threads (12 total).

## hoangcao243 | 2017-08-30T01:16:11+00:00
Thank you.
I did not know as long as cache 100% used it's max out. I thought cpu has to be 100% too lol. 

I tried with affinity 0x555 and 555000 both time gave me lower number like 350 total.

So in order to mine monero, please educate me which part of the Cpu  is the most important ? L2 cache ?  

## xmrig | 2017-08-30T01:27:12+00:00
L3 cache size most important on most CPUs, each thread require 2MB fast memory, of Monero scratchpad not fit into cache, CPU waiting for slow RAM, it looks like 100% load, but it just waste performance.

On some CPUs important is L2 + L3 (AMD FX Series) on these CPUs can load all threads to 100%.
On most desktop and old Xeons like yours, 100% **visible** load is useless.

Primary factor is cache size, threads not important to much.

## hoangcao243 | 2017-08-30T01:40:37+00:00
Thank you very much for your great support 👍

## hoangcao243 | 2017-08-30T02:17:08+00:00
By the way do you have any idea how the E7 4870 will performe? It has 10 cores, 2.4ghz and 30Mb L3. 
Seems like people are getting like 350hs per cpu.

Whereas the amd 6276 has 16mb but people can get 450 with it?



## xmrig | 2017-08-30T03:02:55+00:00
E7 4870 should give much more, 350 looks very low.

Opteron 6276 tricky processor, it pair of FX CPUs and it has 32 MB cache (16 MB L2 + 16 MB L3)

## hoangcao243 | 2017-08-30T03:11:00+00:00
Thank you again for the info. I'm very surprised when i see that number too. Maybe that cpu has 10 cores and 20 threads each so the user was not able to configure it correctly (usually they come with 4 nodes system).

Assuming same price per cpu, which one would you choose to go with? 4870 or 6276?
Thanks for a lot of valuable info.

## xmrig | 2017-08-30T03:24:36+00:00
Hard question)
6276 legendary for Monero, it always on high demand, but very tricky 2 NUMA nodes per single CPU, so I choice it only because of this. If not thinking about mining I prefer Intel, classical architecture etc

## hoangcao243 | 2017-08-30T03:30:28+00:00
Thank you very much. 

## hoangcao243 | 2017-08-30T15:02:57+00:00
Hey man, one question just pop up in my mind. Now at my work we have a blade server and we could mix amd blade with xeon cpu blade. How would i go to configure the thing? Better to keep it simple with one type of cpu blade?

## xmrig | 2017-09-03T03:16:12+00:00
Move all NUMA related issues to #86

## jdevsan | 2017-11-27T19:37:54+00:00
Hi i was trying to configure my xmrig in a vps  with ubuntu and i buy like 12 cores and only i get 2 on xmrig! what it is? the more high hash rate i get when i put 2 threads 

# Action History
- Created by: hoangcao243 | 2017-08-29T05:13:27+00:00
- Closed at: 2017-09-03T03:16:12+00:00
