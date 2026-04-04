---
title: 'Monero Tech Meeting #149 - Monday, 2025-12-08, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1308
author: rbrunner7
assignees: []
labels: []
created_at: '2025-12-05T13:30:33+00:00'
updated_at: '2025-12-08T18:25:00+00:00'
type: issue
status: closed
closed_at: '2025-12-08T18:24:59+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1304).


# Discussion History
## rbrunner7 | 2025-12-08T18:24:59+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1308
<s​needlewoods> hi
<j​effro256> Howdy
<j​berman> *waves*
<r​brunner7> Ok, the regulars are here, thus we can move to the reports from last week
<s​needlewoods> some more fixes, one of the bigger issues that got fixed: `show_transfers` now does show incoming pool txs, but outgoing pending txs still not showing up
<s​needlewoods> ready to push, but I'm a little hesitant, because of all the GitHub spam it creates
<s​needlewoods> and started planning what to do next, I think it's a good idea to continue with replacing wallet2 by the Wallet API in monero-wallet-rpc, because now I'm still relatively familiar with the Wallet API. If you guys have no objections, I'd write a CCS proposal for that, starting in January.
<r​brunner7> Yes, I think that's the next logical step, monero-wallet-rpc
<jeffro256> +1
<jberman> +1
<j​berman> Identified and patched issues causing broken and unreliable sync when the pool exceeds the max weight allowed, I'm catching up on people's comments in the stressnet channel now, and planning to work on unexpected slow sync, runaway span OOM's, and tx relay v2 this week / whatever issues people highlight in the stressnet channel
<r​brunner7> Stressnet causing some stress for you fixing bugs :)
<j​berman> It's been solid, I'm glad, this one was a lingering bug in FCMP++ integration code that I'm happy is now fixed: https://github.com/seraphis-migration/monero/pull/251
<sneedlewoods> +1
<j​effro256> Implemented PQ changes to carrot_core, communicating with potential code auditors, and working on updating the benchmark suite. Might take a serious stab at transaction proofs next week
<r​brunner7> By the way, just curious, where do the block sizes top out currently on stressnet? 10 MB or so?
<s​needlewoods> v1.5 is supposed to be the last version for this stressnet run? There you made quite a few improvements since 1.4v fwiw
<r​ucknium> 18MB now. A few blocks up to 30MB. However, the actual bytes is not equal to tx weight. I don't know the error factor.
<jeffro256> +1
<j​berman> I recall seeing ofrnxmr mention 19+ MB blocks (although that's not actual MB, just weight, since weight on alpha stressnet is actually much larger than byte size). ofrnxmr / Rucknium  may know definitively current peak
<ofrnxmr> +1
<j​berman> Thank you Rucknium
<r​brunner7> Impressive
<j​berman> that's the hope, but we'll see how it goes
<sneedlewoods> +1
<j​berman> haven't released v1.5 yet, people have been testing a pre-release for v1.5
<r​ucknium> https://matrix.monero.social/_matrix/media/v1/download/monero.social/QEeyVrGkBYxuaKQuyLMnrYSG
<r​ucknium> ^ Last week of block weights
<r​ucknium> From https://stressnetnode1.moneronet.info/
<j​effro256> Nice graph, thank you
<r​brunner7> How long like that until you pass mainnet blockchain filesize :) Hyc confirmed today on Reddit that LMDB per se works without problems with terabyte sized files, so nothing to fear.
<r​ucknium> Almost 95GB unpruned now. Added 30GB in last week because we turned up the spam volume.
<r​brunner7> Ok, so our streak with impressive progress, at least as I see it, every week continues. Anything special to discuss today?
<r​brunner7> Does anybody happen to know where we stand with DNS checkpoints? With Qubic almost gone, awfully quiet on that front.
<r​brunner7> Almost gone as a clear and present danger, I mean
<j​effro256> I think it's kinda stagnant at the moment, ofrn mentoned something about how there's a bug in the handling of it, but I haven't looked into that
<s​needlewoods> my last information was 0xfffc was investigating, but not sure
<r​brunner7> Would be a bit sad to not walk the last few meters after quite some journey, no?
<j​effro256> nice
<r​brunner7> Ok, looks like we are through for today. Thanks everybody for attending, read you again next week!
<s​needlewoods> thanks everyone, cu
<plowsof> for pools' hashrate check https://blocks.p2pool.observer/pools by DataHoarder 
<o​frnxmr> Yeah, a checkpointed block is orphaned before the checkpoint us received -> receive checkpoint -> node rolls back to _before_ the checkpoint -> node refuses to reorg onto the checkpointed chain, because its orphaned + node cannot add blocks to the chain, because they dont match the checkpoint = node stuck
````


# Action History
- Created by: rbrunner7 | 2025-12-05T13:30:33+00:00
- Closed at: 2025-12-08T18:24:59+00:00
