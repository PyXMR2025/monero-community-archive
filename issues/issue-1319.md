---
title: 'Monero Tech Meeting #152 - Monday, 2026-01-05, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1319
author: rbrunner7
assignees: []
labels: []
created_at: '2026-01-02T15:15:28+00:00'
updated_at: '2026-01-05T19:08:58+00:00'
type: issue
status: closed
closed_at: '2026-01-05T19:08:58+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1315).


# Discussion History
## rbrunner7 | 2026-01-05T19:08:58+00:00
````
<r​brunner7> Meeting time. Hello! monero-project/meta #1319
<j​berman> *waves*
<s​needlewoods> hello and happy new year
<r​brunner7> Good, some people are still here, not everybody exit-scammed with the turn of the year :)
<r​brunner7> Likewise, happy new year
<j​berman> happy new year :)
<j​babb:cypherstack.com> Happy new year all
<r​brunner7> Let's start already with the reports. I could finish a first review of SNeedlewoods 's magnum opus, moving the CLI wallet to the Wallet API: monero-project/monero #10233
<jeffro256> +1
<r​brunner7> Overall, looks pretty good, I would say
<j​effro256> Howdy
<v​tnerd> hi
<j​effro256> Happy New Year!
<s​needlewoods> thanks to rbrunner and vtnerd I have lots of valuable review comments to work on
<s​needlewoods> currently focusing on vtnerds review of #9464 / #10232
<j​berman> thank you guys for reviewing
<j​effro256> Thanks for taking on that first review
<r​brunner7> Fun fact: With that merged, git blame will say for more than half of all CLI wallet code that it's from sneedlewoods :)
<sneedlewoods> +1
<j​berman> me: completed changes to tx relay v2 (0xFFFC0000/monero #62) and ofrnxmr has been testing. The only thing noted there so far is a potential issue with "refill" logic (refilling the pool on restart), but I don't believe that's an issue with txs relay v2, so that seems to be holding up well
<j​berman> I then dug into a segfault seraphis-migration/monero #258 and have narrowed in on what looks like a likely cause. It seems to be an upstream issue to me and unrelated to FCMP++
<ofrnxmr> +1
<r​brunner7> Any more reports?
<j​effro256> Me: I'm thinking about breaking the `wallet2` reserve proof API and I wanted to bring up the idea here.
<r​brunner7> You mean introduce a breaking change how that works?
<v​tnerd> I got lwsf to construct fcmp++ txes with a custom ZMQ function in monerod
<jberman> +1
<jeffro256> +1
<j​effro256> The reason is that the reserve proof API in `wallet2` is sort of broken right now in that it doesn't do a good job at checking non-collusion across entities, even though the crypto code itself tries to check this. The fundamental reason why it is broken is because it A) takes 1 proof at a time, B) uses current chain state to "pin" Monero addresses to one-time address, and C) doesn't check chain state differences across reserve proofs
<v​tnerd> *custom rpc method. That rpc method is going to be tweaked such that it only accepts the new global output indexes
<r​brunner7> Sounds like a nice milestone reached, vtnerd
<v​tnerd> yes, hopefully the lwsf based wallets will not be left behind (couldn’t resist)
<sneedlewoods> +1
<jeffro256> +1
<r​brunner7> Lol
<r​brunner7> jeffro256: I am afraid I don't yet understand the fundamentals here. What entities are you speaking of that may collude? Isn't a reserve proof something for just a single wallet, and that's it?
<j​effro256> This leads to a scenario where entities A and B are trying to prove reserves, and are supposed to be separate. Entity V is validating reserves. Entity A could make a reserve proof, Entity V could validate the proof with `wallet2::check_reserve_proof()`, Entity A could then send XMR to entity B, Entity B could make a reserve proof with shared funds, then Entity V could validate B's proof with `waller2::check_reserve_proof()` . It would look like A and B hold reserves separately, but in reality, they are "double dipping"
<j​effro256> Nice!
<o​frnxmr> Yeah, seems to be working well enough
<r​brunner7> Hmm. Doesn't sending *any* funds *after* a reserve proof make that proof moot already? ELI5 :)
<k​ayabanerve:trix.org> waves
<j​effro256> What needs to be done is that `wallet2` must understand that reserve proofs need to be validated in some sort of explicit shared context, or the `wallet2` must pin some blockchain state (e.g. lowest used block hash) between validations of reserve proofs
<j​effro256> Yes, exactly, but the API doesn't really have a way to handle this.
<j​effro256> Which mais why I think it merits breaking it
<k​ayabanerve> I've reported some issues with wallet2 to jeffro256, specifically around size limits on transactions and the methodology of construction. Some of it is stupidly over-complicated (add a payment ID if it's not a blood moon, unless the user is a virgin in the eyes of Cthulhu), and some of it could be argued fingerprints in edge cases.
<k​ayabanerve> While _some_ of these should disappear with CARROT, I think there may be a couple explicit lines of code which need to be whacked for this to properly move forward.
<r​brunner7> There is nothing like a "timestamp" in that proof? Like "done at this and this state of the blockchain, and/or the wallet"?
<s​needlewoods> breaking something that's broken to fix it sounds good to me
<k​ayabanerve> Also, isn't multisig TX construction completely independent, having been rebuilt by koe? That implies the two have fingerprints due to the absurd amount of bug-for-bug compatibility you'd need. Very silly, very messy. Thankfully, that's under an experimental flag.
<k​ayabanerve> I think I can give you an address that Monero will send to, but won't realize is an address when determining how many people were sent to, with weird as hell effects from there.
<r​brunner7> You should trademark that expression, "bug-for-bug compatibility"
<k​ayabanerve> Nothing breaking, just very stupid edge cases.
<r​ucknium> Would it make sense to discuss implementing another reserve proof?, e.g. Thakore, V., & Vijayakumaran, S. (2025). MProve-Nova: A Privacy-Preserving Proof of Reserves Protocol for Monero. Proceedings on Privacy Enhancing Technologies, 2025(2), 582–606. moneroresearch.info/266
<r​ucknium> Or the one before that
<k​ayabanerve> It's the same issues discussed with Bitcoin, lacking a formal spec, as the code is the spec. I think one of their opcodes immediately begins by throwing away the first value.
<k​ayabanerve> Not because that's reasonable. They just loaded the first argument twice in their evaluator, from a stack, so the top of the stack gets yeeted.
<r​brunner7> Seems to be a constant: "There is always a paper" :)
<k​ayabanerve> every observable effect of a system, even if unintentional, will become someone's requirement for the behavior of the system
<j​effro256> The reserve specifies references to one-time addresses, and its associated Monero receive addresses and key images. The verifier then deferences these one-time addresses, does the Monero address -> one-time address derivation, validates the one-time address -> key image association, then checks that the key images are not yet spent. There's no "timestamp" in the proof per se. You could calculate the block index when the reserve proof stops being valid by the first occurrence of a key image on-chain in the given set inside the reserve proof. However, the daemon doesn't store when key images first appeared in the chain, so you'd have to do a full-chain scan for key images to find this block index, unfortunately
<r​ucknium> Regular MProve moneroresearch.info/256 and MProve+ exist too moneroresearch.info/35
<r​ucknium> rbrunner7: So it's actually three papers :P
<r​brunner7> Ok ok
<j​effro256> Disclaimer: I wrote a new type of reserve proofs which use FCMP++ to get full-chain privacy ;)
<rucknium> +1
<j​effro256> That would also cause a breaking of the API
<r​ucknium> The only instance of a Monero reserve proof I have seen was a wrapped coin implementation IIRC.
<r​brunner7> Just curious: Do such proofs play a large role "out there in the wild"? Or would we at least very much make them more popular, and more widely used?
<r​brunner7> *like to make them more popular
<r​ucknium> IIRC, Thakore & Vijayakumaran (2025) uses an auxiliary Merkle tree to get "full privacy" with RingCT.
<r​brunner7> So the 3 proofs in the 3 papers may not translate cleanly to FCMP++?
<k​ayabanerve> xkcd.com/1172 as my final comment on wallet2 bs as reported on above :p
<jeffro256> +1
<j​effro256> They're in `wallet2` right now, but they have 0 sender privacy, 0 receive privacy, and 0 amount privacy. And the API is broken like I mentioned
<k​ayabanerve> jeffro256: The FCMP codebase is obviously internally modular, so you should be able to run with it :)
<r​brunner7> kayabanerve: That's a good XKCD. Classic
<r​brunner7> Isn't "amount privacy" a bit difficult with a proof of reserves?
<r​brunner7> Or do you mean that not only the sum, but the individual enotes become known?
<k​ayabanerve> The idea is you prove reserves equal to or in excess of, without revealing the exact outputs.
<jeffro256> +1
<k​ayabanerve> So it's, on a naïve level, a batch FCMP + Proof of Ownership that _doesn't_ reveal the key images (but does assert they're distinct and unspent within the current blockchain), plus a final proof over the sum of their value.
<r​brunner7> I think the proof string contains a version, so we could continue to support the old proofs after introducing any new one, and nobody will be left out in the cold?
<r​brunner7> But hey, do they work with FCMP++ at all, as they are now, or are we *forced* to move?
<j​effro256> The way I currently have written the new ones reveals the key image , just not the input output pubkey -> key image associations
<j​effro256> For simplicity and so that provers don't have to remake reserve proofs every block
<j​effro256> Validating would work , but only on pre-FCMP++ outputs
<j​effro256> So yeah we are effectively forced to update anyways
<j​effro256> But the wallet2 API itself would also have to change
<r​brunner7> Well, if our hands are forced, that's just living with and developping for a currency that moves forward with a high speed
<r​brunner7> Did you already actually implement your new proof, jeffro256?
<j​effro256> Cryptographically, yes. Haven't integrated it yet b/c of the API issue
<j​berman> personally I think reserve proofs are a pretty niche feature / not many wallets support it AFAIK, and so breaking the API for an improved reserve proof with FCMP++/Carrot is a fairly reasonable / sane decision
<j​berman> considering the break is isolated to just the reserve proof API
<r​brunner7> I tend to agree
<k​ayabanerve> jeffro256: Why do you hate privacy and why do you want to break a critical part of the Monero ecosystem, with 0-5 users?
<jeffro256> +1
<k​ayabanerve> Your solution should either be perfectly private, and post-quantum, and backwards-compatible, or I don't actually think you support Monero
<r​brunner7> Suuure
<k​ayabanerve> /s :p
<k​ayabanerve> It sounds like the reserve proof should be _versioned_ but yes, new protocol, new proof, and the rest sounds straightforward from there.
<jberman> +1
<k​ayabanerve> I don't support publishing key images (by far), but that's the hardest problem _and_ it's fine in a post-FCMP++ world.
<j​effro256> sorry my bad i will also integrate a proof of liabilities protocol next week
<r​brunner7> We seem to have now:
<r​brunner7> static constexpr char header_v1[] = "ReserveProofV1";
<r​brunner7> static constexpr char header_v2[] = "ReserveProofV2"; // assumes same length as header_v1
<k​ayabanerve> Prove reserves, provw liabilities, why don't you prove you're not a federal agent? Huh? Huh???
<jeffro256> +1
<k​ayabanerve> /s :p I'll stop, my actual comment is above, thank you jeffro256: for all your hard work on this transition and a proper future
<r​brunner7> If not FEDs, certainly Mossad. I learned that today on Reddit.
<r​brunner7> So it seems we have loose consensus that a breaking wallet2 API change has merit, and is acceptable.
<j​effro256> Yeah I'm not sure how we would do this. I know how to do exclusion proof by revealing the value (or at least a range that the value could be in), but not how to do exclusion proofs using FCMPs on a value which you don't reveal, and on which there must also be some sort of composition proof
<r​brunner7> For reserve proofs.
<r​brunner7> Alright. Some additional topic that we have to discuss today? We are nearing the full hour, for once :)
<r​brunner7> Doesn't look like it. Nice meeting, good start into the new year. Thanks everybody for attending, read you again in 1 week!
<sneedlewoods> +1
<j​effro256> Yeah spend proofs, tx proofs, and output decoding are pretty much unaffected and have a direct Carrot/FCMP++ analogues
<j​effro256> Thanks everyone!
<s​needlewoods> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2026-01-02T15:15:28+00:00
- Closed at: 2026-01-05T19:08:58+00:00
