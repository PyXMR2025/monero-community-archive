---
title: 'Monero Tech Meeting #122 - Monday, 2025-05-26, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1210
author: rbrunner7
assignees: []
labels: []
created_at: '2025-05-23T17:19:56+00:00'
updated_at: '2025-05-26T18:23:14+00:00'
type: issue
status: closed
closed_at: '2025-05-26T18:23:13+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1206).


# Discussion History
## rbrunner7 | 2025-05-26T18:23:13+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1210
<s​needlewoods> hi
<j​berman> *waves*
<j​effro256> Howdy
<r​brunner7> Alright, on to the reports about last week
<s​needlewoods> made `--generate-from-[view-key/spend-key/keys]` work, also started facing more complex stuff like e.g. how to handle `tools::wallet_keys_unlocker` in `SCOPED_WALLET_UNLOCK_ON_BAD_PASSWORD` [src](https://github.com/monero-project/monero/blob/125622d5bdc42cf552be5c25009bd9ab52c0a7ca/src/simplewallet/simplewallet.cpp#L116-L120)
<j​berman> implemented FCMP++ scan_tx & an RPC endpoint to fetch paths in the tree by output ID: https://github.com/seraphis-migration/monero/pull/49
<jeffro256> +1
<j​berman> and now working on making sure all tests passing. Once that's complete I'm going to draft a checklist for implemented features / TODO's for remaining FCMP++ / Carrot tasks
<r​brunner7> Seems you also found some "long-hanging fruit" how to improve good old wallet2 sync speed, at least under some constellations
<r​brunner7> with PR #9936
<j​berman> yep that was a good push from jeffro to kick that off
<j​effro256> I'm still working on hot/cold wallet flow for Carrot
<j​berman> I'm not sure what issue MrCyjaneK is running into in 9936 though, have asked plows to see if they can repro too
<r​brunner7> What you did way back for Seraphis scanning had a totally different management for threads, right?
<j​berman> Yep the Seraphis async scanner didn't have this issue, and has additional optimizations compared to wallet2 (faster downloading and better CPU utilization)
<j​berman> It was using koe's threadpool implementation
<r​brunner7> Ok. By the way, maybe asked before, but I forgot the answer: How well will FCMP++ transactions prune? Will we have similar blockchain savings as today?
<j​effro256> Lol thanks for the credit but that was all jberman
<j​berman> all in all pretty much the same maybe even slightly better because key_offsets are empty, though Carrot outs have a little more data
<j​berman> well there is also the tree
<j​berman> I'd say comparable
<r​brunner7> Good to hear. Maybe pruning will become even more important, with the blockchain growing quite a bit faster probably with FCMP++
<j​effro256> We save at least 16 bytes per input, keep an additional 18 per output
<r​brunner7> But a 5 kB unpruned transaction will still be 2 kB or so after pruning?
<r​brunner7> Give or take
<j​effro256> Should be significantly smaller than 2kb
<r​brunner7> That would of course be very nice
<j​effro256> The reason the chain is ~30% of the size of the real chain is that the node keeps 1/8 full blocks as well as all the normal cache tables
<r​brunner7> Maybe some patience is needed until we hold actual numbers after implementing. But for now, if somebody asks, e.g. on Reddit, we can say that pruning has a future with FCMP++ as well
<j​berman> the huge FCMP++ proofs can be pruned
<j​effro256> So a pruned tx will be <10% of a full tx, but the pruned node database might still be ~30% the size of a full node
<r​brunner7> Yeah, because so much different stuff is in there, now with extra added "tree" or however that's called :)
<r​brunner7> Alright. Do we have something in particular to discuss today beside reports?
<r​brunner7> Seems pretty smooth sailing on the implementation front, in comparison with the bumpy Divisor road ...
<r​brunner7> Maybe we will hear more in the coming MRL meeting, might get interesting
<r​brunner7> Alright, looks like we can close for today. Thanks everybody for attending, read you again next week!
<s​needlewoods> thank you
````


# Action History
- Created by: rbrunner7 | 2025-05-23T17:19:56+00:00
- Closed at: 2025-05-26T18:23:13+00:00
