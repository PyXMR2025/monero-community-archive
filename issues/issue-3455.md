---
title: IO awareness for the smart mining
source_url: https://github.com/monero-project/monero/issues/3455
author: beenotung
assignees: []
labels: []
created_at: '2018-03-20T23:32:41+00:00'
updated_at: '2018-08-15T12:54:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently the smart mining mode auto adjust the CPU load, providing mining experience without much impact on the system, so the user can still use the system for their work and use idle CPU resources to do the mining.

However, on Linux, when the IO is under heavy load, the whole system will freeze. This is lead by the design of the linux kernel (heard BSD don't have this issue).
From my observation, heavy IO loading occurs when verifying a number of new blocks (let's say I have not turn is computer on for a few days, or when block(s) regression happens).

I suggest the smart mining to not just auto adjust based on the CPU loading, but also auto adjust based on the overall IO loading.

# Discussion History
## glv2 | 2018-03-21T08:47:20+00:00
I think the system freeze under heavy IO load is not related to smart mining. It will probably also happen when synchronizing many blocks even if mining is not activated.

If it is not already the case on your system, you could try using the *deadline* IO scheduler in the Linux kernel (using the ```elevator=deadline``` option in the kernel boot line), this should reduce the freezes under heavy IO load.


## moneromooo-monero | 2018-03-21T11:29:11+00:00
Smart mining should indeed be turned off when syncing. This is done automatically in the sync code, at fairly low level, so Cryptonight does not run concurrently for both mining and block verification. Since this is fairly low level, it'll turn on and off quickly when needed, and so may well report to be on when you check.
Mining itself does not use more than negligible I/O, it's all CPU stuff.
There's one thing which can happen though:after a new block is added, when mining's enabled again, a new block template will be generated. This can be heavy if your txpool is large, and is pointless in this case since other blocks will get added soon. This should be changed if it does this (not 100% sure but I think it does).


## beenotung | 2018-03-22T03:18:20+00:00
@glv2 yes, it happens when not mining. I can see my CPU and RAM utility rate low on multi-core system with plenty memory from `htop`. But I see 99.99% IO usage from `iotop`

## beenotung | 2018-03-22T03:21:16+00:00
So my request may be 'smart mining' similiar feature for block sync. (Smart sync or Smart verify?)

## moneromooo-monero | 2018-08-15T12:54:40+00:00
You can use --max-concurrency N to set the max number of worker threads used in heavy workloads such as syncing.


# Action History
- Created by: beenotung | 2018-03-20T23:32:41+00:00
