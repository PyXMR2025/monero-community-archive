---
title: Add ability to sweep a wallet's balance
source_url: https://github.com/monero-project/monero/issues/668
author: fluffypony
assignees: []
labels:
- enhancement
created_at: '2016-02-15T08:30:39+00:00'
updated_at: '2016-09-05T19:00:02+00:00'
type: issue
status: closed
closed_at: '2016-07-07T20:03:41+00:00'
---

# Original Description
Currently it's extremely difficult to sweep a wallet due to the fee only being able to be computed when the transaction is built, so it becomes a bit of trial-and-error. We should add a command that lets you sweep the balance of a wallet to a destination, and it takes care of splitting / fees / etc.

This may be a little complex due to the inability to chain Monero transactions (ie. you have to wait for change to "clear" before you can send the next transaction), so any split should be exact and shouldn't be reliant on change.


# Discussion History
## moneromooo-monero | 2016-04-02T14:27:54+00:00
Such a command would have to spend two different types of txes: one with mixin 0 for unmixable things, and one with mixin 2 for the rest. sweep_unmixable should not create change, the other should be some variation on transfer_new to avoid creating change in split txes.


## moneromooo-monero | 2016-04-19T20:24:25+00:00
Done in https://github.com/monero-project/bitmonero/pull/815, though that only does a single (possibly split) tx. The user can sweep_unmixable first if needed.


## fluffypony | 2016-07-07T20:03:41+00:00
Fixed


## greatwolf | 2016-08-31T00:53:01+00:00
Just to clarify, can `sweep_unmixable` be use to consolidate dust transactions? For example, early implementations of node-cryptonote-pool used by many mining pools use to send a lot of dust payout transactions frequently until they finally fixed it. Can mined dust amounts from that period be consolidated with `sweep_unmixable`? Any caveats and consequences to be aware of when doing this?


## fluffypony | 2016-09-05T19:00:02+00:00
@greatwolf `sweep_unmixable` only works for old dust amounts that aren't quantised, eg. an output of 0.003279123. It won't help for very small quantised amounts, eg. an output of 0.000000003 XMR.


# Action History
- Created by: fluffypony | 2016-02-15T08:30:39+00:00
- Closed at: 2016-07-07T20:03:41+00:00
