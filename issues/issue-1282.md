---
title: 'Monero Tech Meeting #142 - Monday, 2025-10-20, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1282
author: rbrunner7
assignees: []
labels: []
created_at: '2025-10-17T13:34:15+00:00'
updated_at: '2025-10-20T18:27:56+00:00'
type: issue
status: closed
closed_at: '2025-10-20T18:27:56+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1279).


# Discussion History
## rbrunner7 | 2025-10-20T18:27:56+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1282
<s​needlewoods> Hi
<j​berman> *waves*
<j​effro256> Howdy
<r​brunner7> Alright, let's start with the reports about last week
<s​needlewoods> `m_wallet` is no more, now working on `tools::wallet2`, ~25 of those are left, but they boil down to just a few TODOs (e.g. there are several calls to `tools::wallet2::parse_*_payment_id()` and `accept_loaded_tx()` functions which rely on `tools::wallet2::tx_construction_data`, need to figure out a replacement for that)
<jberman> +1
<jeffro256> +1
<s​needlewoods> I didn't come up with a satisfying solution for `--generate-from-json` [src](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/simplewallet/simplewallet.cpp#L4428), yet. It's also used by [RPC](https://github.com/monero-project/monero/blob/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/wallet/wallet_rpc_server.cpp#L4999) so I think it should be supported by the Wallet API.
<s​needlewoods> With the GUI, under some conditions I was able to get the daemon blockchain height on wallet creation, but it's fragile and it doesn't work for one of the most important cases, when someone is trying to create a new wallet for the very first time. Will do further investigation.
<r​brunner7> "m_wallet is no more" Wow!
<r​brunner7> Quite a milestome
<s​needlewoods> it felt a little unreal when it compiled
<r​brunner7> Good that you investigate that GUI wallet creation issue
<j​berman> We released v1.2 alpha stressnet, worked on another p2p change here that I ended up closing based on discussion (https://github.com/seraphis-migration/monero/pull/174), fixed a synchronization issue that was causing FCMP++ tx construction failures in the GUI (https://github.com/seraphis-migration/monero/pull/183), continuing toward 1.3 alpha stressnet, reviewed jeffro's upstream P<clipped me
<j​berman> R to cache input verification results
<r​brunner7> Is 183 a long undetected edge case present also in the current release software?
<j​effro256> Reviewing j-berman's PRs to FCMP++ and currently writing more unit tests for the mempool validation cache upstream PR
<jberman> +1
<j​berman> Yes, one reason it doesn't affect current release is because ring sigs don't work the same as the tree (ring members will be static even as you add a block to the chain, whereas the usable tree in FCMP++ advances)
<j​berman> Plus FCMP++ tx construction takes a lot longer
<r​brunner7> I see. Are there significant speedups still ahead, or do large txs just take their time with FCMP++?
<j​berman> There may be room for further multithreading, plus assembly in curve arithmetic. kayabanerve would have a better idea
<j​berman> But nothing planned at the moment
<r​brunner7> Ah, ok, so not a case where something is still waiting to to online, like some contest results
<j​berman> There's the switch to dalek ed25519 that's still pending, but aside from that, no. I don't recall how much that would be expected to affect tx construction times. The flamegraphs showed
<r​brunner7> I guess many more things are more pressing than that :) Maybe currently just makes spamming a bit harder than before.
<r​brunner7> I wonder a bit how long the fee algorithm discussion might still go forth and back in the MRL meetings. At some point in time, decisions must come, so somebody can put them into code, right?
<j​berman> Yes, I have a simplified proposal I intend to share soonish too
<sneedlewoods> +1
<r​brunner7> Maybe we will reach the long-sought "loose consensus" with that, who knows.
<r​brunner7> Looks like that's it for the reports. Anything further to discuss today?
<r​brunner7> Everybody very busy with coding anyway :)
<j​berman> Thank you for your review on 162 also :)
<r​brunner7> Welcome! Not much is left where I can still contribute something code-wise right now, frankly.
<r​brunner7> Alright, looks like we are through. Thanks everybody for attending, read you again next week!
<s​needlewoods> Thank you
````


# Action History
- Created by: rbrunner7 | 2025-10-17T13:34:15+00:00
- Closed at: 2025-10-20T18:27:56+00:00
