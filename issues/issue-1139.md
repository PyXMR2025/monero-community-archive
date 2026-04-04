---
title: 'Monero Tech Meeting #103 - Monday, 2025-01-13, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1139
author: rbrunner7
assignees: []
labels: []
created_at: '2025-01-10T14:51:02+00:00'
updated_at: '2025-01-13T18:53:38+00:00'
type: issue
status: closed
closed_at: '2025-01-13T18:53:37+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1135).

# Discussion History
## rbrunner7 | 2025-01-13T18:53:38+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1139
<j​effro256> Howdy
<j​berman> *waves*
<s​yntheticbird> hi guys
<s​needlewoods> hey
<r​brunner7> Monero seems to pick up steam in the new year :) What can you report from past week?
<s​needlewoods> Didn't remove the "WIP" tag from the Wallet API PR yet, because I haven't figured out why the ci fails at unit test `node_server.race_condition`, but I guess I could try to force push and hope it disappears.
<s​needlewoods> Though I began to look into and work on my list and made a first PR in that regard.
<r​brunner7> Did you already ask selsta whether that is something that fails from time to time anyway, for mysterious reasons? I think there have been such things in the past. Maybe you are innocent.
<selsta> yes, that fails from time to time
<s​needlewoods> Haven't asked yet, in the past I often assumed something failing in the ci wasn't my fault, when later it turned out to indeed was my fault lol
<selsta> rerunning should fix it
<s​needlewoods> good to know, thanks
<j​effro256> I finished all not-integration-related end-to-end testing of the Carrot addressing protocol all the way from sender payment proposals -> output set finalization -> basic fee proposals -> enote creation -> `cryptonote::transaction` -> serialization -> deserialization -> scanning -> spend opening on the receiver side. Also I finished integrating the fast X25519 key exchange into Carrot, so scanning should take ~37% less CPU time now.
<jberman> +1
<rottenwheel> +1
<sneedlewoods> +1
<r​brunner7> Is that over all scanning, meaning it's about a third faster, or only for some important parts of the scanning code?
<j​effro256> It doesn't affect download/RPC speed, but everything after that
<r​brunner7> Ah, I see, of course. Still impressing.
<j​berman> me: set up FCMP++ prove over the FFI using all C++ components from the input side, I have an error in verify that I'm still investigating
<jeffro256> +1
<rottenwheel> +1
<r​brunner7> Also sounds like nice progress
<r​brunner7> I guess that "FFI" stuff does not eat too much performance all on its own? Crossing the Rust-C++-boundary is reasonably fast?
<j​berman> as far as I can tell yes. The massively significant computational work is in crypto ops
<r​brunner7> On the C++ side then?
<r​brunner7> Will be very interesting to see where we finally land with the behaviour of the fully working, live system using FCMP++
<j​berman> C++ side is handling torsion check / torsion clear which is significant, rust side is handling FCMP++ arithmetic which is significant
<r​brunner7> By the way, do you see a need for a separate repo like we had it for the Seraphis work, or will you two coordinate things between you "on the fly"? That didn't get very far anyway, that separate repo ...
<r​brunner7> With "two" I mean jberman and jeffro256
<j​berman> jeffro256: have you been able to spend much time looking at the FCMP++ PR? I haven't yet gotten to Carrot PR review and don't really have an opinion on best coordination route yet
<r​brunner7> Sounds to me like it's a bit early to say. Surely no problem as long as nobody runs into problems with their work.
<r​brunner7> Alright. Do we have something to discuss beyond these reports?
<j​effro256> I've combed through it a bit. I think I'll merge in the RCT type code changes at first, just enough to use it as a scanning flag. I think the end flow should look a little something like: Carrot code creates pruned `cryptonote::transaction` and finished BP+s, then FCMP++ code signs, then wallet fetched tree root and completes membership proofs, all in a sequential pipeline
<j​effro256> I'm going to make a flow chart today to try to coordinate how new transaction construction pipeline should look like
<j​effro256> There's a ton of improvements we can make, especially if the transaction weight is going to be a function of the in/out *counts*, and not the bytesize of the finished transaction
<r​brunner7> SyntheticBird: I think your Saturday question about " has the GPU acceleration been discussed" is still unanswered. I didn't see anything discussed in this regard. Seems to me that's not on top of anybody's mind right now.
<syntheticbird> +1
<j​berman> sounds like a solid plan to me, thank you jeffro256
<r​brunner7> I guess that would anyway be firmly past FCMP++ hardfork, right?
<j​effro256> The current input selection -> finished transaction construction logic in `wallet2` is horrific, in no small part to the fact that the tx fee depends upon minute details of the on-chain tx serialization format, which in turn depends on the fee chosen
<j​berman> If we do end up swapping out wallet2's tx construction logic, we're probably going to add another 1k - 3k lines of code at least, so it's worth being cognizant of that we are already looking at thousands of lines of new code
<r​brunner7> Does that transaction weight question / apporach change need further discussion, maybe in the MRL meeting frame, until it can be decided? If yes, maybe that should get some priority soon?
<j​effro256> Yeah we have to weigh the pro/cons of trying to stuff separate membership proving/fee logic and a new addressing protocol into this part of `wallet2` versus replacing it
<j​berman> (AFAIK no one is looking at GPU acceleration at this time)
<j​effro256> If we replace it, it might end up being many more lines of code nominally, but be a hell of a lot simpler for a human to review
<r​brunner7> Well, probably still not that many humans around who will be capable to really review that ...
<j​effro256> Don't forget that if we integrate transaction construction logic directly into `wallet2`, we have to duplicate it in like three different spots for sweep single, sweep all, etc
<r​brunner7> Maybe you did not hack hard enough mentally when you arrived at this need? :)
<j​effro256> Yes the weight question shold be discussed again. Kayaba also sorted out all of the performance regressions I noted earlier, so the max input/output count discussion is ripe again since we have actual numbers now
<r​brunner7> Ok
<r​brunner7> What's the current plan how long, during the hardfork phase, it will be possible to build and submit "old" transactions? Maybe if that's a longer phase of say several weeks, there would be a need to even support two fee calculation approaches?
<j​effro256> Yes during the transition, we will need to support old fee calculation for pre-FCMP++ transactions, and new fee calculation for post-FCMP++ transactions
<r​brunner7> Sounds a bit tricky
<j​effro256> We should keep the crusty old logic around for making pre-FCMP++ transactions, but I don't think we should try to integrated FCMP++ signing and Carrot protocol into that old code
<j​berman> fwiw updated wallets shouldn't submit the pre-FCMP++ txs during this period even if consensus allows it. the idea behind the grace period last hf was to allow txs constructed right before the first hf and in the pool to remain in the pool and be mined
<r​brunner7> If I remember correctly we had some ideas for a longer "grace period" for Seraphis and Jamtis, possibly weeks. But that would have been a much more radical hardfork, with the address format change.
<r​brunner7> Maybe for FCMP++ we can muddle through with the usual day, or two.
<j​effro256> I think it'll depend on whether or not the ecosystem is read
<j​effro256> ready
<r​brunner7> Ok, I expect that things will clear up considerably soon in these regards, with the growing code
<r​brunner7> You would think that if the ecosystem is not ready the whole hardfork will get postponed
<j​effro256> Because it should be relatively seamless from a user perspective, this update still requires a decent amount of dev work depending on how your wallet is written
<j​berman> well either way, I don't see why an updated wallet would want to submit pre-FCMP++ txs during this period
<j​effro256> Yes, *updated*
<j​effro256> I agree with you on that
<j​berman> so why keep the old logic around in this path?
<r​brunner7> I don't see the need either
<j​effro256> We need it, at least initially, if the wallet software is updated because the HF, otherwise it won't be able to create transactions
<j​effro256> We could remove it after the HF though
<r​brunner7> Ah, yes
<j​berman> ya fair enough, dumb q
<j​effro256> *before the HF
<r​brunner7> Too bad ...
<j​effro256> Lol not a dumb question, it's tricky to keep track all of the moving parts and their different version
<j​effro256> At different points in time
<r​brunner7> We lost pooled transactions once during a hardfork, even, if I remember correctly, because of a very tricky problem nobody saw before. That stuff is *hard*
<s​needlewoods> it's the first hf I witness, very exciting
<syntheticbird> +1
<jeffro256> +1
<r​brunner7> We will all blame you then if something goes wrong, haha
<r​brunner7> Alright, I think we can close the meeting here. Thanks for attending, read you again next week!
<s​needlewoods> thanks everyone, cu
<s​yntheticbird> thanks delicious meeting as always
````


# Action History
- Created by: rbrunner7 | 2025-01-10T14:51:02+00:00
- Closed at: 2025-01-13T18:53:37+00:00
