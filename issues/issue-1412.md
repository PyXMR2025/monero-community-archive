---
title: 'Monero Tech Meeting #175 - Monday, 2026-06-29, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1412
author: rbrunner7
assignees: []
labels: []
created_at: '2026-06-29T10:08:04+00:00'
updated_at: '2026-06-29T18:34:49+00:00'
type: issue
status: closed
closed_at: '2026-06-29T18:34:49+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1408).


# Discussion History
## rbrunner7 | 2026-06-29T18:34:49+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1412
<sneedlewoods> Hi
<jberman> waves
<jpk68> Hello
<selsta> hi
<rbrunner7> So, what are the reports from last week?
<rbrunner7> I could make an update for my Polyseed PR. Most things are now either addressed, or waiting for some clarifications and/or opinions from reviewers.
<sneedlewoods> Made a PR for the wallet-rpc https://github.com/monero-project/monero/pull/10819
<plowsof> +1
<rbrunner7> +1
<jpk68> +1
<sneedlewoods> Started reviewing the Polyseed PR by rbrunner7
<sneedlewoods> Preparing a new CCS proposal and planning to include potentially work on restore height issues, would like to hear if anyone has any thoughts on this?
<sneedlewoods> (besides: a) work on Wallet API, walllet-cli and wallet-rpc review comments and b) do reviews / help out where I can)
<sneedlewoods> so the proposed tasks currently look like this:
<sneedlewoods> - By now I have a [couple big PRs](https://github.com/monero-project/monero/pulls/SNeedlewoods) pending for which I plan to address review comments ASAP. To name the most important ones:
<sneedlewoods>   1. Add functions to Wallet API [#9464](https://github.com/monero-project/monero/pull/9464)
<sneedlewoods>   2. Remove cached password from Wallet API [#10232](https://github.com/monero-project/monero/pull/10232)
<sneedlewoods>   3. Both based on 1. and 2.
<sneedlewoods>      a) Replace `wallet2` with Wallet API in `monero-wallet-cli` [#10233](https://github.com/monero-project/monero/pull/10233)
<sneedlewoods>      b) Replace `wallet2` with Wallet API in `monero-wallet-rpc` [#10819](https://github.com/monero-project/monero/pull/10819)
<sneedlewoods> - There are some issues related to restore height I could eventually address (and partially already started investigating or working on):
<sneedlewoods>   - Get actual block height on wallet creation from daemon and only rely on estimated restore height when offline.
<sneedlewoods>   - Figure out if it's worth to improve the "get restore height by restore date" when offline behavior, this could be beneficial for wallets created with Polyseed (which stores the birthdate).
<sneedlewoods> - Try to help where I can, e.g. PR reviews, issues on Github or discovered during other work, requests/suggestions from other devs.
<sneedlewoods> Last meeting jeffro256 said that ideally all the Wallet API changes could make it into v0.19, for that I would need to rebase the API/CLI/RPC changes onto the polyseed PR AFAICT, do you think that is also a task worth to add to the CCS proposal?
<jpk68> Finished the first milestone of my CCS for I2P work, having to do with the core daemon implementation
<plowsof> +1
<rbrunner7> +1
<sneedlewoods> +1
<rbrunner7> Nice milestone again, @sneedlewoods !
<selsta> One thing that I just remembered, wallet_api apparently has some bugs with refresh thread https://github.com/oxen-io/oxen-core/pull/1466
<selsta> this should be investigated and fixed on our side before we switch all wallets to it.
<sneedlewoods> +1
me: finished reviewing @jeffro256:monero.social 's mega hot-cold PR for FCMP++/Carrot, believe we *now* solved @rucknium:monero.social  sporadic double spend issue and will finalize an upstream PR for that today ( https://github.com/seraphis-migration/monero/issues/365#issuecomment-4811722029 ), and I'm going to have all upstream PR's from the FCMP++ integration phase 1 prepared for merge today (was waiting on Trail of Bits finalized published report, but they're still in a final "tech" editing phase and I think it should be fine to move forward before they finish)<rbrunner7> Good find. Maybe we corrected already on our side some time in the 5 years since then
<rbrunner7> (to selsta)
<selsta> I don't think this ever got fixed on our side.
<jberman> selsta: fwiw the new FCMP++ changes introduce a new refresh lock internally to wallet2
<jpk68> jberman: Out of curiosity, does the 6x faster zero commit speed up anything besides FCMP++ crypto? As in, would it provide any speed improvement currently
<jberman> @jberman: though it shouldn't hurt to fix the API's lock handling also
<rbrunner7> Making sure @sneedlewoods is not running out of work anytime soon :)
<jberman> @jpk68: yes, that function is currently used at consensus for coinbase outputs and for pre-RCT outputs. It's not a major bottleneck in current syncing, but it would marginally help syncing
<jpk68> +1
<rbrunner7> What is a "zero commit"?
<jpk68> I have the same question :D
<DataHoarder> a commitment to the amount of 0, using Mask as `
<DataHoarder> as 1*
<rbrunner7> Some "no money out of thin air" thing then?
<DataHoarder> mask scalar = 1, amount = 0 which as jberman is used in special cases like coinbase
<jberman> when an output has a transparent amount, you calculate its commitment as amount * H (H is a generator specific to Monero)
<DataHoarder> which has public amounts
<jberman> it's necessary so that transparent amount outputs can be used as inputs in future txs enabling you to construct a tx where sum of inputs == sum of outputs while still blinding amounts
<jberman> it becomes more relevant in FCMP++ because all outputs' commitments are stored in the curve tree, which both the daemon and wallet build
<jberman> so speeding this up has a more tangible impact on both wallet and daemon sync speed with FCMP++
<rbrunner7> Next step up will be curve forest .. you read it here first ...
<rbrunner7> Ok, ok, interesting reports. Do we have to discuss something beyond those today?
<selsta> I can only advertise again that we need reviews for v0.18.5.1 https://github.com/monero-project/monero/issues/10545
<selsta> all have at least one review but need a second before merge
<rbrunner7> Will try to have a look, now with my PR update out of the door
<jberman> can review those 2 by tomorrow as well
<jberman> those 3*
<rbrunner7> You will probably overtake me then :)
<rbrunner7> Alright, looks like we are through. Thanks everybody for attending, read you again in 1 week!
<jpk68> +1
<sneedlewoods> Thanks everyone
````


# Action History
- Created by: rbrunner7 | 2026-06-29T10:08:04+00:00
- Closed at: 2026-06-29T18:34:49+00:00
