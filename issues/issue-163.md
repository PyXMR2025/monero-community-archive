---
title: AMD FX-8350 strange behavior
source_url: https://github.com/xmrig/xmrig/issues/163
author: erotavlasme
assignees: []
labels: []
created_at: '2017-10-21T19:52:11+00:00'
updated_at: '2017-11-27T00:35:20+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:35:20+00:00'
---

# Original Description
Hi,
I have an AMD FX-8350, it has 8 integer units and 4 floating point units in Clustered Multi Threading (CMT) design with 8 MB cache L2 and L3.
I tried with -av 0, -av 1 and -av 2 options. With the -av 0, xmrig autoselect av=1 mode and I have 8 threads running at 385 H/s and this is quite strange since each thread should requires 2 MB L3 cache. While with -av 2 I have 4 thread running at 230 H/s and also this is quite strange since each thread should requires 4 MB L3 cache [according to this](https://github.com/xmrig/xmrig/wiki/Threads).
This is the only CPU with such strange behaviour in terms of number of used threads and with high reduction rate between standard mode and low power mode about 230/385=41% instead of 30% as I found with other CPU.
Can you explain this behaviour? Is it better to use or not --safe option?
Thank you

# Discussion History
## xmrig | 2017-10-22T05:15:53+00:00
It expected behavior for FX CPUs. Cache hierarchy not usual there 4 L2 cache each 2 MB and one shared L3 8 MB cache, 16 MB total.

L2 cache is not equivalent to L2 cache in Intel or modern AMD CPUs, it more like L3 cache and L3 something like L4. So formula is `(L2 + L3) / 2`. Also proper affinity is much more important.
Thank you.

## brunoalexbr | 2017-11-17T02:57:26+00:00
Hello guys
I have some tips
In the XMR-STAK-CPU the Fx has a better hashrate if it puts the core 0.1 with low energy and the core 3, 5 and 7 in normal mode.
An Fx 8350 gets 430H / s under these settings. The colleague up there reported only 385H / s, why he should use either 7 threads or only 4 threads with no affinity. XMRIG does not have this definition precision in its settings, it simply applies the same algorithm to all cores  that have been defined affinity. For best performance of AMD FX low power is required at 0.1 and normal power at 3, 5 and 7 exactly in this order.
I liked XMRIG, i sue on Ryzen 7 1700, I suggest this improvement so that you can use it with FX processor. AMD Cpus are better for mining than intel cpus.

# Action History
- Created by: erotavlasme | 2017-10-21T19:52:11+00:00
- Closed at: 2017-11-27T00:35:20+00:00
