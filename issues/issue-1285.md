---
title: 'Monero Tech Meeting #143 - Monday, 2025-10-27, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1285
author: rbrunner7
assignees: []
labels: []
created_at: '2025-10-24T15:18:48+00:00'
updated_at: '2025-10-27T18:19:30+00:00'
type: issue
status: closed
closed_at: '2025-10-27T18:19:30+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1282).


# Discussion History
## rbrunner7 | 2025-10-27T18:19:30+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1285
<jberman> waves
<rbrunner7> Hmm, will be a short meeting if only the two of us are here :)
<needlewoods> hey
<rbrunner7> Alright, never mind, on to the reports from last week!
<sneedlewoods> worked on TODOs and fixing bugs, mostly related to transfer/sweep and sign/submit with raw_monero_tx and unsigned_monero_tx
<jberman> stressnet bug investigating, PR wrangling, and finally reviewed p2p ssl
<rbrunner7> Is that one of vtnerd's PRs that are waiting for quite a while already?
<rbrunner7> The P2P SSL
<j​berman> yep
<j​berman> https://github.com/monero-project/monero/pull/8996
<r​brunner7> Ok. 2023, lol. But well, if it moves, that's nice.
<r​brunner7> By the way, don't remember, will stressnet have to fork again to a new blockchain in the future, possibly with some changes like the final fee formula?
<r​brunner7> Or one or the other Carrot tweak
<j​berman> I penciled in a plan where we just save those tasks for a beta stressnet, so the beta stressnet would be a new fork from current testnet again (and will have 0 relation to the current alpha stressnet)
<j​berman> but in theory, if those tasks were to be done as part of alpha stressnet, yes it would be another hard fork. It wouldn't make sense to do that though since it would introduce unnecssary forking logic
<r​brunner7> Yeah, sure. Not worth the hassle, just wipe everything and fork again from some particular testnet height.
<r​brunner7> It seems like we are through already with reports. No wonder, everything running smoothly I guess :) Something more to discuss today?
<s​needlewoods> Nothing from me
<r​brunner7> Anyway, the room is always open. Thanks everybody for attending, read you again next week!
<s​needlewoods> thank you & cu
````


# Action History
- Created by: rbrunner7 | 2025-10-24T15:18:48+00:00
- Closed at: 2025-10-27T18:19:30+00:00
