---
title: verify code for randomx (rx/0)
source_url: https://github.com/xmrig/xmrig/issues/1298
author: amitceder
assignees: []
labels:
- question
- wontfix
created_at: '2019-11-17T17:36:58+00:00'
updated_at: '2019-11-19T11:35:58+00:00'
type: issue
status: closed
closed_at: '2019-11-19T11:35:58+00:00'
---

# Original Description
Hi,
in the latest version 15.0 of xmrig - the source don't containt a verify code similar to the one of the other algos - as CN/R.
Can you share a verify code for that please?

thanks
Amit.

# Discussion History
## amitceder | 2019-11-18T17:37:46+00:00
excuse me - I mean version 5.0.0.
Is there a verify ("stand alone") version for random X (without connecting to the pool, just run a kind of "self test")

## Spudz76 | 2019-11-18T19:44:10+00:00
You can use the speed testing mode of [meta-miner](https://github.com/MoneroOcean/meta-miner) to feed a test job to any miner without a pool.  Set perf items in its mm.json to 0 and it will speed test.

## amitceder | 2019-11-19T08:58:28+00:00
I think I wasn't very clear - I don't mean a kind of a testbench to check my machine abilities in general.
What I meant was - to run RandomX miner code in a "verify"/"verify2" manner (as mentioned in the code on CpuWorker.cpp.

## SChernykh | 2019-11-19T10:31:11+00:00
Verification would require creating and initializing 2 GB dataset, this is just too slow. It's not there because of this.

## xmrig | 2019-11-19T10:31:34+00:00
This code not included, main reason is verification time, dataset initialization is slow process it can take few seconds and use all CPU cores, for verification need initialize dataset twice, one time for test seed and one time for user seed (provided by pool) also it increase complexity of code, miner can use multiple datasets (with NUMA hardware).

It can't be done on miner startup too, because mining starts only after job received.
Thank you.

## amitceder | 2019-11-19T10:43:46+00:00
understood - but still - for simulation and self-test reasons - assuming for example the data-set large DDR memory is all zeros, and then run the VM for one cycle - as was done with cn/r (variant 4) and cn/2 (variant 2) - can a code like that be added please? 

## xmrig | 2019-11-19T11:00:28+00:00
I might add in future API method to calculate hashes with any input data and any supported algorithm, sometimes it may useful for test purposes, but it low priority task and no ETA right now.
Thank you.


## amitceder | 2019-11-19T11:35:56+00:00
Thanks a lot anyway.

# Action History
- Created by: amitceder | 2019-11-17T17:36:58+00:00
- Closed at: 2019-11-19T11:35:58+00:00
