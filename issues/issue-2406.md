---
title: 'Affinity settings have no effect on MacOS - update : They do but not like
  on other systems!'
source_url: https://github.com/xmrig/xmrig/issues/2406
author: XReyRobert
assignees: []
labels:
- question
created_at: '2021-05-23T12:13:42+00:00'
updated_at: '2021-10-16T01:24:17+00:00'
type: issue
status: closed
closed_at: '2021-10-15T23:00:05+00:00'
---

# Original Description
Hi all,

**Describe the bug**
Setting up CPU affinity on **XMRig/6.12.1** for **MacOS** (Big Sur 11.3.1) doesn't seem to have any effect (While being correctly reported when looking at hashrates (h)

**Expected behavior**
A clear and concise description of what you expected to happen.

Setting up **"rx": [40, 42],** I"d expect to see activity dispatched only to core 40 and 42. (On my system that would be targeting cores 10 et 12 of CPU #2)  (16 cores / 32 threads x 2) 

To make things worse it seems that there's no affinity at all (Even not CPU affinity), it means that trying to go over 20 threads I will see the performances decreasing because (I guess) threads are jumping from one cpu to another (defeating any CPU cache benefits?)

**Additional context**

|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0  |       40 |   453.9 |   456.2 |     n/a |
|        1 |       42 |   432.3 |   436.4 |     n/a |
|        - |        - |   886.1 |   892.5 |     n/a |

![Screenshot 2021-05-23 at 13 53 16](https://user-images.githubusercontent.com/38261891/119259361-3adab180-bbce-11eb-8e6f-f114f5fd1032.png)


# Discussion History
## xmrig | 2021-05-23T13:03:08+00:00
Sounds crazy, but macOS does not support affinity to specific cores, it works just like a hint for system thread scheduler, no more. https://developer.apple.com/library/archive/releasenotes/Performance/RN-AffinityAPI/index.html#//apple_ref/doc/uid/TP40006635
Thank you.


## Spudz76 | 2021-05-24T02:41:38+00:00
The XNU kernel model essentially prevents anything fun or cool.  Some stuff works as root but some is completely firewalled unless you're in the kernel.

## XReyRobert | 2021-05-25T08:42:53+00:00
Thanks for your comments. The thread affinity API apple document was an interesting read.  
So here's the result of my investigations: 

There's no way to define CPU / Core affinity using this API so using traditional "RX":[0,2,4,6 ....] xmrig setting is very bad. Instead you should use (**If you have 2 REAL CPUs**) it to define AFFINITY SETs like this: "RX":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2]
From the Apple doc :  "a set expresses an affinity with an L2 cache and the scheduler should seek to run threads in a set on processors sharing that L2 cache"

Using the parameter this way you in fact create two affinity sets that the scheduler will try to schedule at best knowing that they both share a L2 Cache on the 2 physical CPUs. There's no garanty but it works ! 

![Screenshot 2021-05-25 at 10 41 12](https://user-images.githubusercontent.com/38261891/119467554-e78b6f00-bd45-11eb-9fea-759acd7dbc08.png)

I got best result using dissymmetrical  sets WHEN set 1 is running on CPU 1 and set 2 on CPU 2. With the funny thing that there's no way to make sure that it is the case ! So you have to re-start xmrig until the allocation is right but it's not sticky and set 2 might be re-allocated to CPU 1 with terrible performance) And when it goes I go from ~9000 H/s to ~/2000 H/s. So on the long run it might be better to schedule 10-11 threads with balanced sets.

This is far from optimal and the reason why I don't get much better  H/s on my dual 2698v3 setup than on an optimized 2697v2 setup (~/5500 H/s OCed)....

But the fact there's no dual-cpu machine in the Apple range since 2012 might explain somme choices...

I might try to install a linux system to see how much I can get of this setup with proper core affinity...








## XReyRobert | 2021-05-28T09:32:21+00:00
**Update for the archives - Ignore the previous comment!** 
In fact I had some other random issues that made things unpredictable (bios or boot dependant not sure).  The same random reason was giving me issues with geekbench (1/2 score) while cinebench was running at expected speed. I suspect RAM related issue.
At the moment I disabled NUMA and isoc from bios, and I manage to reach  a steady 11.5k hrate (31 threads - 12.6k max) on dual 2698v3 which is I guess what is expected letting MacOS assign affinities with [-1,-1,-1,-1,-1 x 31]


## Spudz76 | 2021-10-16T01:24:17+00:00
That hashrate is within the top 7 [of benchmarks](https://xmrig.com/benchmark?cpu=Intel%28R%29+Xeon%28R%29+CPU+E5-2698+v3+%40+2.30GHz) so it must be pretty correct.

# Action History
- Created by: XReyRobert | 2021-05-23T12:13:42+00:00
- Closed at: 2021-10-15T23:00:05+00:00
