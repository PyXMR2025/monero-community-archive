---
title: Help best configuration
source_url: https://github.com/xmrig/xmrig/issues/2132
author: gorunks2001
assignees: []
labels:
- question
created_at: '2021-02-26T07:23:13+00:00'
updated_at: '2021-04-12T14:10:19+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:10:19+00:00'
---

# Original Description
Hi, we have 3 machines with 2x Xeon E5-2640 v2 @ 2ghz 64bit
L2 0.5MB  L3 40MB
256gb ram each

We have 3 virtual machines Linux Ubuntu, one for each machine

Could you help us for the best setting for mining?

actually we use this string:
sudo ./xmrig/build/xmrig -o pool.minexmr.com:443 -u OurWallet -k --hugepage-size=1000000 --cpu-no-yield --tls --rig-id Ale1

thanks


# Discussion History
## gorunks2001 | 2021-02-26T13:28:03+00:00
we just installed ubuntu in the phisical machine... but when we start xmrig it use only 16 threads instead 32.  and have an hashrate of 5000

how we can increase it?

thanks


## SChernykh | 2021-02-26T13:36:16+00:00
> only 16 threads instead 32

This is correct for this CPU. Your hashrate is also correct, see benchmark for a single CPU system: https://xmrig.com/benchmark/3rNuVu

## gorunks2001 | 2021-02-26T13:38:11+00:00
> > only 16 threads instead 32
> 
> This is correct for this CPU. Your hashrate is also correct, see benchmark for a single CPU system: https://xmrig.com/benchmark/3rNuVu

thanks for the answer, is there a way for use all the 32 threads?

thanks


## SChernykh | 2021-02-26T13:52:37+00:00
Yes, but 32 threads will be slower. Add `-t 32` to the command line.

## gorunks2001 | 2021-02-26T13:53:56+00:00
oh ok, so in 5300 is the max hash for this machine .
thanks

# Action History
- Created by: gorunks2001 | 2021-02-26T07:23:13+00:00
- Closed at: 2021-04-12T14:10:19+00:00
