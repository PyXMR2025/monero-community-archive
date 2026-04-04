---
title: 'Monero Tech Meeting #118 - Monday, 2025-04-28, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1194
author: rbrunner7
assignees: []
labels: []
created_at: '2025-04-25T15:17:55+00:00'
updated_at: '2025-04-28T19:16:44+00:00'
type: issue
status: closed
closed_at: '2025-04-28T19:16:42+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1190).

# Discussion History
## rbrunner7 | 2025-04-28T19:16:42+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1194
<j​berman> *waves*
<s​needlewoods> Hey
<r​brunner7> Alright, what is there to report from last week?
<r​brunner7> Inspired by last week's MRL meeting I started to study the daemon's peer selection and management code, but I don't know yet whether I will reach a point where I will be able to code a new algorithm
<jeffro256> +1
<sneedlewoods> +1
<jberman> +1
<syntheticbird> +1
<rucknium> +1
<j​effro256> Howdy
<s​needlewoods> finally managed to make a PR to [monero](https://github.com/monero-project/monero/pull/9915) and [monero-gui](https://github.com/monero-project/monero-gui/pull/4437)
<jeffro256> +1
<jberman> +1
<r​brunner7> Wow, nice
<r​brunner7> Let the reviews flow :)
<j​effro256> Did code cleanup , bug fixes, and supporting of multiple txs for the Carrot+FCMP CLI `transfer` command : https://github.com/seraphis-migration/monero/pull/32
<s​needlewoods> I plan to do some reviews next, before I start with the next step of my CCS proposal: "replace wallet2 with the Wallet API in simplewallet"
<r​brunner7> I could advertise the Wallet API a bit some day last week, maybe you saw
<r​brunner7> Linked to your PR
<j​berman> Spent a good portion of last week hardening an algorithm to calculate weight for FCMP++'s membership proofs, aiming to share details on it today, and rest of this week working with jeffro to get all the outstanding PR's ready to go
<s​needlewoods> yes, thank you for that :)
<r​brunner7> I can't remember exactly, do we already have our famous loose consensus how many inputs, and how many outputs we will allow for FCMP++ transactions? What did you actually code now, jeffro256 ?
<j​effro256> I'd have to go dig up reasoning for it, but the limit we've settled on at the moment 8/8
<r​brunner7> Nice how you have a tester now with "ComputerPony"
<j​effro256> Yeah its really really nice
<j​berman> Original gist: https://gist.github.com/kayabaNerve/dbbadf1f2b0f4e04732fc5ac559745b7
<jeffro256> +1
<j​effro256> Still trying to figure out the top block mismatch bug
<r​brunner7> Yeah, the proposal in that gist is indeed 8/8
<r​brunner7> I guess soon things will be stable enough to allow more people to start with testing
<r​ucknium> Many community people are unhappy with `MAX_INPUTS = 8`.
<r​brunner7> Sure, understandable
<r​ucknium> The last time this was discussed, people at the meeting wanted to wait until we have the optimized code for benchmarking.
<r​brunner7> Soon it will at least be possible to play around with the count and try higher limits with some reasonable code
<s​yntheticbird> I may ask a stupid question but afaik MAX_INPUTS  = 8 limit is because of performance requirement. But I also hear that the FCMP++ library is a constant-time implementation, which make sense for construction. Surely a var time one could be used for verification?
<s​yntheticbird> i have the assumption that var time is faster than constant time
<j​effro256> SyntheticBird:   Yes we discussed this for the FCMP crypto competition , but its a huge maintainability burden
<syntheticbird> +1
<jberman> +1
<j​berman> I'd say we can re-look at the limit with hardened figures, especially after the optimization contest. Recent tests took my solid ryzen 175ms to verify a membership proof with 8 inputs. That's a long time to get a node doing work
<r​brunner7> So a block with 100 txs or so could take up to 20 seconds to verify?
<r​ucknium> IIRC, a node already takes over 1000ms to verify a 143-input RingCT tx, which are allowed on mainnet now.
<r​ucknium> IIRC, jeffro256  had the comparison benchmarks
<s​yntheticbird> Surely tx verification is batch
<r​brunner7> Yes, but it's not that easy to produce such txs ...
<s​yntheticbird> or is that only possible with Curve forests?
<r​brunner7> (143 input txs)
<j​berman> No, I'd have to re-look at batch verification figures, it scales logarithmically not linearly
<r​brunner7> Ah, I see.
<j​berman> Allowing 1s verification on a single tx today doesn't sound great to me either. Especially while nodes hold a lock doing that verification
<j​berman> Though the latter could be dealt with
<jeffro256> +1
<j​effro256> They don't have to hold a lock depending on the design. You could simply copy the root while holding the lock , then verify against that local variable
<syntheticbird> +1
<r​brunner7> Maybe some determined and adventurous soul will put up a competing stress net with higher limits to prove a point :)
<r​brunner7> Alright. jberman , you wanted to give some details about tx weight calculation?
<j​berman> Unfortunately I have a bit more fine-tuning on it, but I can share general goals of the approach
<j​berman> I think a core property we want to maintain for the weight calculation is let's say you want to spend N outputs. There shouldn't be incentive to spend those N outputs across multiple txs, compared to spending them in 1 tx
<j​effro256> One 16-member CLSAG takes 4ms to verify on my machine , which doesn't include the balance check, fetching ring member data, or BP+ verification,  so 1 second total for a 143 input CLSAG tx sounds within the right ballpark
<rucknium> +1
<r​brunner7> As long as N <= 8, right
<j​berman> Right (or whatever the max is)
<j​effro256> I would disagree IF verifying a 2-in tx  plus 1-in tx was all-told cheaper than a single 3-in
<r​brunner7> Isn't that a bit improbable?
<r​ucknium> AFAIK, the function of FCMP verification time is roughly affine in the number of inputs. A fixed cost is paid regardless of the number of inputs, then the cost per input is linear:
<r​ucknium> `f(x) = alpha + beta * x`.
<r​ucknium> But I don't know how batch verification would change things. But batch verification may not be very relevant for txs in the txpool. Maybe only on initial sync
<j​berman> In my tests, verifying 2-in and 1-in is actually slightly faster than a 3-in, but there are a couple more things to consider here:
<j​berman> 1) This creates at least 2 more outputs that would be spent later on and cannot be pruned
<j​berman> 2) Taking size into consideration, the byte size of 2-in + 1-in is significantly larger than 3-in (something like 1.8x larger, have to double check)
<jeffro256> +1
<j​effro256> Not really, Bulletproof-based proofs' verification time is linear to the next highest power of 2 statements that the proof is proving. For example, for our BP+ range proofs, verifying a 3-out is just as expensive as a 4-out. So breaking up a 3-out TX into a 2-out and 1-out reduces total verification time for the range proofs.
<r​brunner7> Interesting
<j​effro256> But FCMPs are a bit more complicated because of the number of layers variable, so they don't necessarily act this way
<j​effro256> The number of "statements" for a FCMP is a weird function of the tree depth and input count
<r​brunner7> So good that soon we will be able to play around with such txs
<j​effro256> You can play around sending XMR right now with: https://github.com/seraphis-migration/monero/pull/32
<j​berman> Because of these 2 points, which I believe should both hold for all input combinations, I think it's reasonable to maintain the property that there shouldn't be incentive to spend the same number of outputs (<= max allowed) across multiple txs, compared to spending them in 1 tx
<r​brunner7> Of course I did not yet look deeper into this, but right now I tend to agree: Filling the blockchain quite a bit faster for a small performance gain does not sound very attractive IMHO
<r​brunner7> Given that the txs will be a lot larger anyway, right?
<j​berman> right
<r​brunner7> @jeffro: So current state of the FCMP++ staging repo plus PR 32 enables tests?
<j​effro256> What kind of tests do you want to do ?
<r​brunner7> I mean, that will give a working system?
<r​brunner7> So I can transact, and try 1 input, 2 input, and so on
<j​effro256> Yup!
<j​effro256> The CLI  transfer command doesn't explicitly allow you to do input selection , but if you wanted to try 3 input time, you could send 3 outputs to account 1 and set your sending account as 1
<r​brunner7> Maybe I will be crazy enough to try :)
<r​ucknium> This property doesn't conflict with the suggestion that all txs with the same in/out permutation with the same fee priority level (1-4) should cost the same, right?
<j​effro256> I don't recommend connecting it to mainnet though lol
<r​brunner7> Is that even technically possible? Don't think so
<j​berman> Rucknium: as in all txs with 1-in/2-out and fee priority level 1 should all cost the same (assuming same tx extra also)?
<j​effro256> If you edit your hard fork table , you can do anything you want. You'll probably get kicked by your peers though
<j​berman> (as one example)
<r​brunner7> I see
<r​ucknium> Yes. And you don't necessarily have to have valid arithmetic properties. Let me try to explain
<r​ucknium> You can still maintain the "cost the same" requirement even if a 4in/4out does not cost double the fee as a 2in/2out
<j​effro256> The fee also depends on the "dynamic fee base estimate" returned by the daemon which IIRC is a function of the mempool state, so probably not
<r​ucknium> Isn't it a function of recent median block size?
<j​effro256> Looking now...
<r​ucknium> IIRC, the txpool state affects whether an "automatic" fee gets bumped from the cheapest level to the next-cheapest (fixed during the suspected spam attack).
<j​berman> Just focusing in on membership proof weight for a second: any call to the weight calculation will be the same for a given number of inputs
<jeffro256> +1
<r​ucknium> And I think only the most-expensive level is affected by recent median block size. IIRC, it is affected because the most-expensive level is supposed to "pay for itself" by expanding the short-term block limit when the block subsidy is sacrificed
<j​berman> And the property is strictly focused on the membership proof weight
<j​effro256> Yes you're right
<r​brunner7> So, overall, will it probably play out correctly?
<j​effro256> To expand on this: the entire tx weight is a function of only three numbers: number of inputs, number of outputs, and tx_extra size
<j​effro256> (Proposed for FCMP++, not at the moment)
<j​berman> And the membership proof is by far the largest component of that weight calculation
<jeffro256> +1
<r​brunner7> Simply because of its size in bytes?
<j​berman> If going off just byte size alone even, yes, and this weight calculation is *also* going to take in verification time
<j​berman> similar to how BP's does it
<j​berman> It's ~5kb for a 1-in membership proof, the SAL proof and BP+ are something around ~1kb I believe (have to double check) and then the rest of the tx is going to be a lot less than that
<r​ucknium> Let `f`, `g`, and `h` be some functions transforming the number of inputs, number of outputs, and tx_extra size. Then, the transaction weight does _not_ necessarily have to be of the form `w(in, out, tx_extra) = f(in) + g(out) + h(tx_extra)`. This would give more flexibility to make sure that the new weight calculation has "the property that there shouldn't be incentive to spend the same number of outputs (<= max allowed) across multiple txs, compared to spending them in 1 tx".
<r​ucknium> I am just saying you can think outside the box if needed
<j​berman> I see, true and agree
<r​ucknium> While still maintaining the same property of same fee for the same in/out/tx_extra arguments.
<r​brunner7> Ok, I learned, and refreshed, a lot during this meeting. Do we have anything important left to mention for today?
<r​brunner7> Does not look like it. Thanks everybody for attending, read you again next week!
<s​needlewoods> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2025-04-25T15:17:55+00:00
- Closed at: 2025-04-28T19:16:42+00:00
