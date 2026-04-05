---
title: 4x xeon e7 8870 with xmrig
source_url: https://github.com/xmrig/xmrig/issues/1009
author: DalDal78
assignees: []
labels:
- bug
- NUMA
created_at: '2019-04-04T19:36:23+00:00'
updated_at: '2019-08-02T11:55:41+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:55:41+00:00'
---

# Original Description
Im using a pre compiled xmrig on windows server 2016 with 4x xeon e7 8870s. Xmrig is only detecting 2 of the cpus and only using two of the cpus regardless of how many threads I set and affine. 

# Discussion History
## Spudz76 | 2019-04-20T06:43:35+00:00
Windows doesn't treat systems with over 64 cpus properly.
Either disable HT (so visible cores is 40) or complain to microsoft for designing their multi-processor subsystems like a toddler.

Basically to support their broken view of multiple cpus there is a whole bunch of dumb code needed to jump into the other "processor group".

No idea why they can't handle a single processor group once core count is above 64.  You also can't quite affine things the same, when grouping decides to ruin the topology.

Sometimes windows will decide to ruin the topology even before you hit 64 total, depending on "M$ LOGIC" thus who knows when.

## Spudz76 | 2019-04-20T06:47:55+00:00
They put their affinity into a 64-bit field, thus the 64 limit (one or zero for each cpu in the group, run out of binary bits and you have to go new CPU-group and then make GROUP+affinity calls (and try to keep the topology straight).  Thus no miner apps ever bothered.  Also people don't tend to have $40K servers for jacking around on so the 64 limit basically hurts five people ever.

## Spudz76 | 2019-04-20T06:52:18+00:00
The HT trick probably won't work either they tend to detect that HT-capable and "might" get turned on later so it predicts (pre-dicks?) the topology to reserve space for the full 80.  Thus it will break into more than one group and partition the cpus into 2x2 again anyway even though actual current total is under 64.

That's part of the "M$ LOGIC" and there seem to be some more rules but its all basically undocumented.  Other than, you have to make all sorts of extra code to deal with multiple cpu groups and even then it's pretty suck.

## qutimqqcom | 2019-05-12T19:47:45+00:00
hi
im use  E7- 8830,  new  version 2141  dont work in double threads mode, 
av = 2,  take  x2  memory, but  H\S  like  av=0,   algo  CNR
previos  version 2.13  work good  ,   algo  CN8


how  to  use  advanced threads mode   ?

## DalDal78 | 2019-05-14T22:43:21+00:00
im probley not much help but i just install ubuntu so i dont have to deal
with all that.

On Sun, 12 May 2019 at 15:47, qutimqqcom <notifications@github.com> wrote:

> hi
> im use E7- 8830, new version 2141 dont work in double threads mode,
> av = 2, take x2 memory, but H\S like av=0, algo CNR
> previos version 2.13 work good , algo CN8
>
> how to use advanced threads mode ?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1009#issuecomment-491623659>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AKLJXZJN7Q6R2UU3LY7E4PLPVBX63ANCNFSM4HDWHBIA>
> .
>


## xmrig | 2019-08-02T11:55:23+00:00
#1077

# Action History
- Created by: DalDal78 | 2019-04-04T19:36:23+00:00
- Closed at: 2019-08-02T11:55:41+00:00
