---
title: Transaction fee is too low for v4 transactions on private stagenet node
source_url: https://github.com/monero-project/monero/issues/5255
author: moneroexamples
assignees: []
labels: []
created_at: '2019-03-08T08:24:50+00:00'
updated_at: '2019-03-09T08:57:51+00:00'
type: issue
status: closed
closed_at: '2019-03-09T08:57:51+00:00'
---

# Original Description
Running private nodes allows for creation of old type transactions for development and testing of ,e.g.,   light or mobile wallets. Without them, its not possible to test how these wallets treat coinbase and regular txs from 2014 to 2017, unless someone has real access to such txs.  

With current `release-v0.13` I can create and spend transactions from v1-v3 (i.e., pre-RingCT) txs and v5 and up on my private stagenet node. When v4 is comes into effect, can't make any txs, due to fee being to low. 

This seems to be limited only to v4 txs (first time when RingCT was enabled).

```
2019-03-08 08:02:41.618 [RPC1]  DEBUG   blockchain  src/cryptonote_core/blockchain.cpp:2984 lo 0.006995216240, qlo 0.006995220000, mask 10000
2019-03-08 08:02:41.618 [RPC1]  DEBUG   blockchain  src/cryptonote_core/blockchain.cpp:3028 Using 0.006995220000/kB fee
2019-03-08 08:02:41.618 [RPC1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3037 transaction fee is not enough: 0.066000000000, minimum fee: 0.230842260000
2019-03-08 08:02:41.618 [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:140   PERF        0      add_tx
2019-03-08 08:02:41.619 [RPC1]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:960 Transaction verification failed: <b49921a634107314fee1fc9c3a90da283cc6a67d00cf6f02c4d8f73140a63d0e>
2019-03-08 08:02:41.619 [RPC1]  WARN    daemon.rpc  src/rpc/core_rpc_server.cpp:721 [on_send_raw_tx]: tx verification failed: fee too low
2019-03-08 08:02:41.619 [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:140   PERF       28    on_send_raw_tx
```


# Discussion History
## moneromooo-monero | 2019-03-08T10:19:15+00:00
When you say v4 txes, you mean a tx according to the v4 fork rules, right ? We only have v1 ans v2 txes so far.

## moneromooo-monero | 2019-03-08T12:10:02+00:00
If you run an old wallet,  it should work. I have had no qualms about keeping the wallet non compatible with old forks, since there was no point to it. If you want to send old txes, then you should checkout an old wallet revision if the current one does not work well. Alternatively, if the change to allow this is unobtrusive, then it can also be merged.


## moneroexamples | 2019-03-08T22:26:05+00:00
> you mean a tx according to the v4 fork rules, right ? 

Yes. I imagine it is not a priority to be backward compatible with previous forks, thus I was very positively surprised to see that using `release-v0.13` one can spin up private nodes for all other past forks and make txs using the rules from these forks. Well, everything except v4 fork rules due to low fees.

Backward compatibility with previous forks is very useful for testing and development. For example, I can spin up private node and fast-mine to v2 fork rules from 2016. Make some wallets there, get coinbase txs and make regular txs resulting in v2 hard fork outputs. Then I fast-mine in minutes to v11 hard fork, and check how the new rules of v11 work with v2 outputs. And this can be done for all past forks, except v4, using `release-v0.13` software on a same blockchain, unlike when you would use old wallets.

I try to check why v4 fee is too small. I think its something easy, probably wrong rules are selected when calculating fee. 

 




## moneromooo-monero | 2019-03-08T22:56:21+00:00
There is a fair chance than the wallet does not even bother checking rules for this.

## moneroexamples | 2019-03-08T23:30:51+00:00
It works with v5 which is also RingCT. V5 is "Adjusted minimum blocksize and fee algorithm" according to https://github.com/monero-project/monero#scheduled-software-upgrades . So maybe current wallet is trying to use v5 fee algorithm for v4? 

## moneroexamples | 2019-03-09T08:57:51+00:00
I found that there is about 720 block delay when v4 hard fork fee rules kick in. So once this threshold is passed, you can create v4 transactions.

So everything seems fine now. Thanks for feedback.


# Action History
- Created by: moneroexamples | 2019-03-08T08:24:50+00:00
- Closed at: 2019-03-09T08:57:51+00:00
