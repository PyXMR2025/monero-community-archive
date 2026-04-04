---
title: Tx propagation sometimes failing after Dandelion++ timeout
source_url: https://github.com/monero-project/monero/issues/6929
author: selsta
assignees: []
labels: []
created_at: '2020-10-22T21:26:57+00:00'
updated_at: '2022-07-20T22:58:52+00:00'
type: issue
status: closed
closed_at: '2022-07-20T22:58:52+00:00'
---

# Original Description
I’ve read multiple reports about this issue and also encountered this myself.

Sent a transaction, it got stuck in the mempool, even after waiting 10+ minutes. In the case of Dandelion++ timeout the transaction should get propagated to all nodes, this was not the case this time. I had 64 out peers so it is unlikely that all of them dropped the transaction.

`relay_tx` did also not help in this case. I tried multiple times and also waited. Only solution was to flush_txpool and resend the transaction.

These reports have been happening since v0.17

# Discussion History
## selsta | 2020-10-22T21:28:59+00:00
@vtnerd Any idea?

## LocalMonero | 2020-10-22T21:31:12+00:00
> `relay_tx` did also not help in this case. I tried multiple times and also waited. Only solution was to flush_txpool and resend the transaction.
> 
> These reports have been happening since v0.17

We've had this happen since v0.16

## moneromooo-monero | 2020-10-22T21:36:19+00:00
When running "print_pool_sh, in monerod in such a case, what are the values of "receive_time" and "relayed" ?

What is the value of "date +%s" on the machine running monerod ?

## vtnerd | 2020-10-27T04:41:27+00:00
I'll have to look into some of the changes made since v0.16. Its likely either `tx_pool.cpp` or `levin_notify.cpp`. The latter was unit tested a bit more directly. If it happens again, try to get a printouts of the pool (with the hashes scrubbed).

## LocalMonero | 2020-10-29T17:47:02+00:00
@moneromooo-monero @vtnerd 

A couple of failed ones for you:

```
id: xxx
blob_size: 1682
weight: 2219
fee: 0.000099420000
fee/byte: 0.000000044803
receive_time: 1603953989 (10 hours ago)
relayed: 1603983131 (2 hours ago)
do_not_relay: F
kept_by_block: F
double_spend_seen: T
max_used_block_height: xxx
max_used_block_id: xxx
last_failed_height: 0
last_failed_id: 0000000000000000000000000000000000000000000000000000000000000000
```

```
id: xxx
blob_size: 1450
weight: 1450
fee: 0.000013000000
fee/byte: 0.000000008965
receive_time: 1603953990 (10 hours ago)
relayed: 1603983131 (2 hours ago)
do_not_relay: F
kept_by_block: F
double_spend_seen: F
max_used_block_height: xxx
max_used_block_id: xxx
```

`date +%s` returns `1603993759`

## vtnerd | 2020-10-30T02:36:23+00:00
@LocalMonero did you have i2p and/or tor enabled via `--tx-proxy` ?

## LocalMonero | 2020-10-30T02:38:10+00:00
@vtnerd nope.

## canlin05 | 2020-11-03T17:48:04+00:00
Any update on this?  Unable to send anything.  Have tried connecting to remote node node.xmr.to on port 18081 but all transactions are failing.

## selsta | 2020-11-03T17:50:13+00:00
@canlin05 is this with GUI? node.xmr.to should definitely work, how often did you try?

## canlin05 | 2020-11-03T17:58:26+00:00
Trying for 3rd time now ... still waiting on confirmation at 12min.  It has failed sooner in previous attempts, so hoping it goes through this time.  Though, 12min seems a long time without a confirmation (?)

## canlin05 | 2020-11-03T17:58:39+00:00
And yes, it is with GUI.

## selsta | 2020-11-03T17:59:52+00:00
You can check if your transaction is in the mempool here: https://xmrchain.net/

12 minutes without a block is nothing unusual.

## canlin05 | 2020-11-03T18:01:33+00:00
Getting some confirmations now.  Thanks for the quick replies, btw.  Should I use this remote node all the time in the future?

## selsta | 2020-11-03T18:02:27+00:00
We will release a new GUI version tomorrow that should fix simple mode again. So you can choose what you want to use.

Edit: We are still working on the release.

## Gingeropolous | 2021-03-31T03:19:10+00:00
@selsta , this issue is closed, right? 

## selsta | 2021-03-31T03:20:19+00:00
@Gingeropolous the bug was never found so I assume no

## xanoni | 2021-08-16T03:51:47+00:00
Happens quite often to me that the TX doesn't confirm after an hour or more. I haven't identified a pattern, yet.

Key config settings (see also https://github.com/monero-project/monero/issues/7863):

```
tx-proxy=i2p,127.0.0.1:4447,25
tx-proxy=tor,127.0.0.1:9050,25

anonymous-inbound=XYZ.b32.i2p:${I2P_EXT_PORT},127.0.0.1:18080,25 # `i2pd` tunnel was defined manually
anonymous-inbound=XYZ.onion:${TOR_EXT_PORT},127.0.0.1:18080,25

# settings equivalent to the below also used for RPC 
p2p-ignore-ipv4=1
p2p-use-ipv6=0
p2p-bind-ip=127.0.0.1
p2p-bind-port=18080

hide-my-port=1
public-node=0
no-igd=1
allow-local-ip=0
no-zmq=1
```

Not sure if `relay_tx` helps (last time it didn't). Seems flushing the TX and resending it has been my best bet to date.

## selsta | 2022-07-20T22:58:52+00:00
Should be solved in v0.18.0.0

# Action History
- Created by: selsta | 2020-10-22T21:26:57+00:00
- Closed at: 2022-07-20T22:58:52+00:00
