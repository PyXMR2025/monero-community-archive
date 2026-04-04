---
title: microlags using monerod, only on win10
source_url: https://github.com/monero-project/monero/issues/6216
author: ph0nky
assignees: []
labels: []
created_at: '2019-12-04T16:06:44+00:00'
updated_at: '2019-12-10T03:05:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am running a full node on my work PC. I mostly run debian, but have to dual boot win10 sometimes.

While I have no problems while running debian, when I boot a pretty clean win10 on the same machine, I can't run monerod in the cli without the whole os microlagging every now and then.

My machine certainly is capable concerning the Hardware.

The microlagging is so severe, that playing music laggs sporadically and the general feel and workflow is unbearable. Unfortunately, my knowledge of windows process priorization etc is pretty limited.

Any ideas on how to fix this windows specific issue?
I already tried starting monerod using --max-concurrency 2, to no avail

This is a persistent problem, I had the same issues with the 0.14.x branch (again, only on win10)

# Discussion History
## iDunk5400 | 2019-12-04T22:33:56+00:00
That sounds like a DPC latency issue, usually caused by a bad driver or system BIOS. Try using a tool like LatencyMon to find out which driver is causing high DPC latency.

## ph0nky | 2019-12-05T00:13:19+00:00
> 
> 
> That sounds like a DPC latency issue, usually caused by a bad driver or system BIOS. Try using a tool like LatencyMon to find out which driver is causing high DPC latency.

Thanks for answering, I ran LatencyMon and my DPC and ISR routines have both low values for "highest execution time".

"Highest measured interrupt to process latency" is really high though.
monerod seems to produce a lot of hard pagefaults though, maybe that's the issue? There's over 10GB of free RAM, so I don't know what's the issue.

i am using the exact same HDD on the same machine in debian to run monerod and have no issues, so I don't think it's hardware related.

## moneromooo-monero | 2019-12-05T16:14:36+00:00
The database is ~75 GB. ~25 GB even if pruned. It'll hit disk from time to time.

## ph0nky | 2019-12-06T18:00:56+00:00
> 
> 
> The database is ~75 GB. ~25 GB even if pruned. It'll hit disk from time to time.

the disc that holds the data is not the system disc. And I have no problems using the exact same disc running debian.
It has to be something windows related.

## iamamyth | 2019-12-10T03:05:48+00:00
As you're using a work machine, I wonder if it has anything to do with WMI. For example, there's this gem: https://randomascii.wordpress.com/2019/12/08/on2-again-now-in-wmi/. Also, that article provides some decent background on how to debug windows performance issues.

# Action History
- Created by: ph0nky | 2019-12-04T16:06:44+00:00
