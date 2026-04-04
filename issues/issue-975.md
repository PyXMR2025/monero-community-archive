---
title: 'Seraphis wallet workgroup meeting #60 - Monday, 2024-03-04, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/975
author: rbrunner7
assignees: []
labels: []
created_at: '2024-03-01T06:36:36+00:00'
updated_at: '2024-03-04T19:10:35+00:00'
type: issue
status: closed
closed_at: '2024-03-04T19:10:34+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/972

# Discussion History
## rbrunner7 | 2024-03-04T19:10:34+00:00
````
<g​hostway> Hello, meeting time(?)!
<j​berman> hello!
<j​effro256> Howdy
<r​brunner7> Yes, yes, I am late a bit today :)
<d​angerousfreedom> Hello
<j​effro256> @UkoeHB thanks
<g​hostway> 30 seconds late!
<j​effro256> Unforgivable
<g​hostway> Indeed
<r​brunner7> https://github.com/monero-project/meta/issues/975
<r​brunner7> So I nice round of people today.
<r​brunner7> So we can already move to the reports.
<g​hostway> Update from me:
<g​hostway> Talked with dangerousfreedom about the new keys, and we both got to the conclusion (I think) it would be nice to make the key container opaque to the keys themselves. We also thought the meeting should touch on this
<j​berman> Update: started back up on the async scanner. One problem I had with the scanner was that sync progress would update in huge chunks but very intermittently, so it felt like the scanner is sitting doing nothing for a while before progressing a huge amount, making scanning feel slow even though it's significantly faster than the current wallet2 scanner. I found a simple way to make <clipped message>
<j​berman> sync progress feedback smooth and near-instant: reduce the size of each request for blocks.
<j​berman> I found that even on a decently high latency connection, when setting the max request size of 20 blocks, feedback was instant and continuous, and total time to sync was unaffected. It would be nice to benchmark on more connections at some point.
<j​berman> I'm currently working on core tests that scan every type of legacy tx. Next will be integration tests for using the async scanner to scan legacy sends and receives.
<d​angerousfreedom> I basically updated the address_utils [PR](https://github.com/seraphis-migration/monero/pull/17), read more about the new modifications introduced by jeffro with the 4th key and studied a bit more about the serialization. Is this [new scheme](https://github.com/seraphis-migration/strategy/wiki/Key-Container#wallet-tiers-and-keys-hierarchy) correct? If so, I will try to see with gh<clipped 
<d​angerousfreedom> ostway  what needs to be done so we can have a final PR for the key_container and jamtis_keys. Unfortunately, this is only what my 20h/week allowed me to do, if I could be sponsored full-time for a year, I would quit my job, buy a sailboat with big and fat monero sails and dedicate full time to monero :p
<g​hostway> Lol
<r​brunner7> So your bit-fiddling discussed in last week's meeting was successful, basically?
<g​hostway> Sounds great
<j​effro256> me: editing transaction format of `SpTxSquashedV1` to remove non-serialized / non-transcripted fields, working on new tx variant, working to add support for legacy validation into sp lib: https://github.com/UkoeHB/monero/pull/34 and https://github.com/UkoeHB/monero/pull/37
<d​angerousfreedom> Btw, great job jberman on the FCMP! Looks like we have something touchable now! I couldnt see it yet but I will try as soon as I have more time! Looks amazing!
<j​berman> thank you :D it's a bit rough at the moment, but I think touchable too
<g​hostway> Yea I have it on my to-read list
<g​hostway> Anything to do there?
<j​berman> sprinkled some TODO's around the code, here are a few: https://github.com/j-berman/monero/commit/6602377e05c134d2b96236663112477a799d62e6
<ghostway> +1
<j​effro256> Good work @jberman. Are you still of the opinion that we should switch curves now ?
<j​effro256> (even if not implementingh FCMPs at next fork)
<r​brunner7> jeffro256: "add support for legacy validation into sp lib" That sounds a bit surprising. Is there validation missing there?
<d​angerousfreedom> After trying to shift everything by one bit and getting crazy, I thought that the best idea would be to pick the last bits and fill it in the remaining bits of the X25519 keys. I will update it soon with the 4th key but it seems an easy and good idea to me.
<j​effro256> So far seraphis lib doesn't touch non seraphis txs
<j​effro256> It understands CLSAG sigs as inputs, but not validating the old txs itself
<r​brunner7> Ah, I see.
<d​angerousfreedom> Would have been much easier if C++ had pointers on bits. But I dont think it is possible, is it?
<g​hostway> Depends on what you wanna do
<g​hostway> std::bitset, _BitInt in c23 etc
<j​effro256> You could write a type that opaquely acts like this with C++ operator overloading, but natively, no machines that I know of support it
<g​hostway> And... Shifting
<j​berman> my opinion is probably leaning closer toward supporting FCMPs for Seraphis v1 fork at this point honestly, but if not, then ya switching curves would avoid needing to change addresses again for reasonably efficient FCMP's
<r​brunner7> By all means, don't blow up that thing too much, for me stuffing bits in somewhere ad hoc is bad enough already :)
<g​hostway> kayabanerve: how's your GBP journey going?
<r​brunner7> jberman: Are we nearing the point where some good estimates about speed and transaction / enote size will become possible?
<g​hostway> enote size has been calculated by kayabanerve, no?
<j​effro256> Really? That's surprising but good to hear. From a pure code readability perspective, if we were to start refactoring seraphis lib now, what should we name the types for points and scalars for the two different curves?
<g​hostway> The Pasta curves library calls them Fp and Fq
<r​brunner7> jeffro256 already nearly on the run with that ball ...
<d​angerousfreedom> Yeah, I'm sure there are many ways of achieving it but this was the one with less operations that I found.
<g​hostway> I don't think it's that bad
<j​effro256> enote size should be about the same IIUC
<g​hostway> I remembered it being slightly less, somehow
<j​berman> enote size is unaffected, but proof size is affected. I'm forgetting final size estimate, will get back to that or kayaba will jump in
<g​hostway> Yea yea
<j​effro256> Well IIRC curve size is smaller by a few bits but IDK if that translates into actual serialized smaller size
<g​hostway> Not really
<g​hostway> You'd have to manage a byte at least :)
<j​berman> there's also the tree which would be composed of the existing squashed enotes, which I believe is just an additional ~`log(# of enotes)` bytes
<g​hostway> Right, sorry
<r​brunner7> I guess if we switch curves, or even go full FCMP already with the initial hardfork, there will be quite some work for the Seraphis library, but "our" wallet work won't be terribly changed?
<j​effro256> Yeah probably not
<g​hostway> Not much, a few types I imagine...
<j​effro256> The Jamtis changes are a much bigger issue for downstream
<j​effro256> Mainly the key container PR and addressing PR currently open
<j​berman> kayaba gave verification time estimates at monerokon, but with the changes toward GBP's, and with some more optimization work on the table, that will take some time to get to finalized
<ghostway> +1
<r​brunner7> Hope is to get faster than those estimates?
<j​berman> yep
<d​angerousfreedom> Yeah, there is a lot going on on the seraphis level still... it makes it harder to build a wallet with things moving that much and so fast :p
<d​angerousfreedom> What is the state of the seraphis_lib with jefrro's review?
<d​angerousfreedom> Would the FCMP change the jamtis specs somehow?
<j​berman> ignoring all changes needed for switching curves, the changes to existing Seraphis lib are pretty minimal, which you can get a feel for here: https://github.com/j-berman/monero/commit/46c5801128b4af1aba597e299029818eef0a81b5
<dangerousfreedom> +1
<jeffro256> +1
<rbrunner7> +1
<j​effro256> How come input image proofs are the same even though we are switching commitments? In other words, how are Pederson commitments transitioned?
<j​effro256> Oh or are they not, but we're not using squashed enote model anymore and Pederson commitments stay on ed25519?
<d​angerousfreedom> Very nice! What I need to do to run an unit_test of a tx using the V2 Membershipproofs ?
<r​brunner7> Those FCMP really are the shiniest tool in the collection we currently have, the lure is tremendous :)
<j​berman> we wouldn't need to switch commitments nor would pedersen commitments be affected at all if we were sticking with ed25519. AFAIU (and kayabanerve can correct here) with the switch to a curve cycle, we would need a migration tx that switches existing commitments over to the new curve. then once transitioned, it would just be a matter of new types basically
<j​berman> we'd use COPZ for that migration, which I didn't get into with that code
<r​brunner7> For us mere mortals, COPZ translates to ...
<g​hostway> https://github.com/kayabaNerve/full-chain-membership-proofs/blob/c649dcad6646bc66f788526dbd164ab8e35f01ad/crypto/copz-dleq/README.md?plain=1#L1
<j​berman> ^
<r​brunner7> Thanks!
<d​angerousfreedom> Other than that... I hope koe and jeffro can reach an agreement about the serialization of the seraphis lib soon. IMO the macros introduced by jeffro to directly serialize any seraphis/jamtis struct and class without the need to define a new `ser_*` is a big gain in readability, compactness and cleanness. Behind the curtains, it would be doing the same thing, right? Basically usin<clipped 
<d​angerousfreedom> g boost for the de/serialization so the output with or without jeffro's modifications should be the same, right?
<j​berman> the unit tests I set up there currently hang cuz some of the lower level crypto ops for the ed25519 > bulletproof25519 tower are unimplemented, BUT if you wanted to run it anyway and see it in action, can pull this branch:  https://github.com/j-berman/monero/commits/fcmp
<dangerousfreedom> +1
<r​brunner7> I think it's not boost, it's the epee proprietary stuff, but the question stays the same
<j​berman> tobtoht: also helped out with getting the rust to build in one pass (with a single `make` at the root of the monero repo) with this commit which you can cherry-pick: https://github.com/tobtoht/monero/pull/2/commits/4b84006e0c2954dec8068285ad70844efb9628a5
<g​hostway> Can you link to a paper detailing what are towers and/or their implementation?
<j​berman> I'll get that commit up in that branch in a sec
<j​effro256> Yes they do the same thing at the end of the day, but removing fields from the transaction that aren't serialized or transcribed in TXIDs could lead to fewer subtle bugs IMO
<r​brunner7> Maybe we will have some complicated cases where a `ser_` class will be the way to go nevertheless, but that would not make everything else useless
<j​berman> https://github.com/j-berman/full-chain-membership-proofs/tree/cpp-compat-ed25519/crypto/bulletproof25519
<g​hostway> Thanks!
<g​hostway> Hmm, are you doing that-very-inefficient-thing-that-the-cycles-are-trying-to-avoid?
<g​hostway> What's the difference
<g​hostway> ?
<j​effro256> So if we skipped right to the pasta curves, this would look like using CLSAGs on existing ed25519 inputs, then creating a new commitment, one for each input, then doing a COPZ proof from the psudo output commitment to the new pasta input commitment?
<d​angerousfreedom> How is that possible? Once you define what is being serialized then how is it different from using `ser_`... ?
<j​berman> (keep in mind I'm not planning to do much further with the ed25519 > bulletproof25519 tower, it's mostly there as a shoe-in to show how FCMP's could work with the Seraphis lib)
<j​berman> yes AFAIU
<j​effro256> Oh I updated that PR to include more things than just the serialization updates.... maybe I should break it into 2 PRs
<d​angerousfreedom> Ok
<r​brunner7> By the way, we have somebody that submitted a CCS proposal for a "new" wallet, where I voted for the author to at least have a look at what we do with Jamtis and Seraphis wallet-wise: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/437
<r​brunner7> Not sure how successful I was
<r​brunner7> And well, we don't have any API to show yet, admittedly ...
<j​effro256> Thanks I was thinking the same thing lol. Can't tell anyone what to do but we can use all the help we can get with the new seraphis wallet
<dangerousfreedom> +1
<r​brunner7> With all the balls that jeffro256 has in the air I am a bit skeptic that much time is left right now for API design, but time will come, I hope :)
<r​brunner7> Ok, we have touched a ton of interesting things already, but is there something still left noteworthy for today?
<r​brunner7> We have to leave something for next week otherwise we will just hang around with nothing to say :)
<jeffro256> +1
<g​hostway> Lol
<d​angerousfreedom> Can someone confirm that [this](https://github.com/seraphis-migration/strategy/wiki/Key-Container#wallet-tiers-and-keys-hierarchy) logic is correct and hopefully the final version of the keys hierarchy?
<j​berman> pinging kayabanerve  on this too, but AFAIU, there is an extra step in the tower that adds significant cost that a curve cycle avoids (kayaba can add more color on this, I'm not sure where exactly in the code that is), and by not going with a curve cycle, we lose out on the potential long-term gains described here: https://gist.github.com/kayabaNerve/97441ad851dc6e4d2a0b699f58a004f2
<r​brunner7> Alright, do continue to discuss, but I think we can close the official meeting, thanks everybody for attending, read you again next week!
<d​angerousfreedom> Thanks everyone
<j​effro256> `s_ga` is derived from `d_vr`, not `d_fa`? (Also we changed notation in the codebase a bit: we use `d_` prefix instead of `xk_` prefix for X25519 keys)
<j​effro256> Thanks everyone!
<j​effro256> `s_ga` is derived from `d_vr`, not `d_fa`. (Also we changed notation in the codebase a bit: we use `d_` prefix instead of `xk_` prefix for X25519 keys)
<g​hostway> Thanks!
<d​angerousfreedom> Yes, I'm aware of that. I just want to code the logic of the wallet tier. So I would do the corresponding ifs to get the proper tier. Would that be correct?
<j​effro256> Oh well you could have a combo of filter-assist and generate-address tiers if both were non-zero
````


# Action History
- Created by: rbrunner7 | 2024-03-01T06:36:36+00:00
- Closed at: 2024-03-04T19:10:34+00:00
