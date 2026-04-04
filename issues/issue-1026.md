---
title: 'Seraphis wallet workgroup meeting #75 - Monday, 2024-06-24, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1026
author: rbrunner7
assignees: []
labels: []
created_at: '2024-06-21T11:47:46+00:00'
updated_at: '2024-06-24T19:10:58+00:00'
type: issue
status: closed
closed_at: '2024-06-24T19:10:57+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/1023

# Discussion History
## rbrunner7 | 2024-06-24T19:10:57+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1026
<j​effro256> howdy!
<jberman> *waves*
<s​needlewoods> hey
<tobtoht_> hi
<r​brunner7> I had a little chat with dangerousfreedom . He is busy, but will probably have time to Monero work in about two weeks.
<r​brunner7> What is there to report from last week?
<s​needlewoods> from me: minor fixes on organize functions PR after reviews from 0xfffc and rbrunner
<s​needlewoods> And have no code to show, but started this table https://paste.debian.net/1321359/ (it's markdown, copy and paste here to preview: https://markdownlivepreview.com/) to make it easier to see what's already there (and where it's located) and to make it easier to discuss what we actually want/need.
<s​needlewoods> Not sure this table is needed for every function, but I assume it would be helpful for e.g. all the transfer/sweep stuff. At least for my smol brain it is hard to remember/comprehend all the overloading and all different names and places.
<tobtoht_> Comments on wallet_api plans: I support the approach outlined in #64. It is sensible we keep the API intact that most wallets rely on (or at least try to minimize breakage, provide a migration guide for developers if necessary).
<tobtoht_> With regard to Feather: I'm nearly positive I will attempt to 'roll my own' API on top of the seraphis libraries, even if it means slashing most functionality and slowly rebuilding to feature parity. Since I control the downstream, I can just keep iterating without having to worry about stability guarantees.
<tobtoht_> wallet2_api.h is not very well-thought-out and it too should perish. I don't want to deal with its string-ified cruft again or extend it. However, regardless of whether a new shiny API comes into existence we need to keep it for now to ensure a relatively smooth transition for most wallets.
<jberman> me: I realized an issue in my grow_tree impl for fcmp's, went back to the drawing board on it and have a clean design I'm working on finalizing now. I'm planning to document a clean specification for the final impl also
<tobtoht_> CLI and RPC are our problem to deal with. Feather is going to do it's own thing. That leaves us with woodser's libraries. I would like to hear their thoughts too. To my knowledge there are no other (open source) wallets/libraries that use wallet2 directly.
<jberman> Also pushing some bite-sized scanner PR's to the monero repo today
<s​needlewoods> thanks for chiming in tobtoht
<j​effro256> If you can quickly describe the issue with the grow tree impl, I'd like to know just out of curiosity
<w​oodser> my libraries only do what wallet rpc can do, so they can be updated if wallet rpc is updated
<j​effro256> By stringified cruft, you mean like passing the addresses and multisig blobs, etc right?
<tobtoht_> Yes, instead exposing something like a MoneroAddress class
<r​brunner7> "wallet2_api.h is not very well-thought-out and it too should perish" That's a pretty hard statement, surprises me a bit. You think many people know but took it nevertheless because it was the only thin available?
<j​effro256> me: worked on Jamtis library legacy address integration, and I *think* I found a way to fix temporary subaddress lookahead issues, but it remains to be seen
<r​brunner7> jeffro256: Where do you integrate, into the Seraphis library?
<r​brunner7> Ah, no, you integrate old addresses into your new library, right?
<j​effro256> Well legacy addresses will continue to be supported alongside Jamtis addresses, but the way derivations will be done is different (outlined in the Jamtis-RCT proposal).
<j​effro256> So the crypto adjacent code is a bit different, and there's also the way it fits into the new Jamtis library. We already have code in the Seraphis library to scan legacy addresses on the legacy protocol, but not to scan legacy addresses on the Jamtis protocol
<r​brunner7> This all gets a bit confusing ...
<r​brunner7> But I think I understand
<r​brunner7> I think to continue to support old addresses is a quite big experiment with an unknown result. We will see, and probably never know whether a hard could have been better after all.
<jberman> "If you can quickly describe the issue with the grow tree impl" -> Assume the tree is structured like `leaves -> layer 0 -> layer 1 -> root`. Let's say the last leaf chunk is NOT full, and the last chunk in layer 1 is also NOT full. You add 1 leaf to the tree. When you update the last hash in layer 1, you need the old value of the last hash in
<jberman> layer 0. I had prior thought I accounted for this case, but was missing it under some circumstances when the tree is depth >3
<r​brunner7> *a hard cut
<j​effro256> For example, with the new onetime address composition that comes with the FCMP-RCT consensus update, tevador showed how we can achieve conditional quantum forward secrecy without regenerating old addresses
<j​effro256> That isn't possible if you don't change the derivations while constructing/scanning
<j​effro256> Thanks jberman, that's interesting. Thinking about how all the leaves are being updated and combining that with unlock times makes my head spin ;)
<r​brunner7> By the way, would you agree that the "plan" is, or still is, to have "our" new wallet ready for the FCMP hardfork? Or, the other way round, the plan is not to hardfork to FCMP with `wallet2` still playing the main role?
<r​brunner7> Which would give us maybe 1 year to get all the pieces into place?
<r​brunner7> Which is not that much of time for such a project
<s​needlewoods> I think one year should be enough if we're talking about "our" wallet still using `wallet2`, if you mean "our" wallet without `wallet2` then I think we need more manpower.
<r​brunner7> Yes, I mean the latter, more or less.
<j​effro256> What we should aim for at a minimum is implementing the scanning code required for FCMP-RCT in a *good* way, completely outside of `wallet2`. That way we can integrate that code into `wallet2` neatly and then reuse it later in a "better" integration
<r​brunner7> Maybe "manpower" depends on the point in time jberman could be available for wallet work proper, and not only things directly related to FCMP
<jberman> Correction to my description of the issue in grow_tree: if the leaf layer last chunk IS full, layer 0 last chunk IS full, layer 1 last chunk is NOT full, then we grow the tree by 1 leaf. In this case when updating the root, we need to use the prior value of the last hash in layer 1 to update the root. For all other layers, we don't need the prior
<jberman> values of last hashes and can simply append to those layers. That was the edge case I prior missed
<r​brunner7> jeffro256: That's quite a small minimum, if you ask me ...
<jberman> I'll be back for full manpower on wallet work in ~4 months
<r​brunner7> It also might give us some psychological boost, some target to work towards, some motivation, IMHO.
<j​effro256> rbrunner7: Well we're going to have to write FCMP-RCT wallet-side code anyways. Might as well write it well in a way that is reusable and not bound to wallet2. Ostensibly, good modular code can be reused in many different integrations, even messes like `wallet2`
<s​needlewoods> Hope I'm not interrupting, but it would be great to get feedback/confirmation on the following questions/statements (regarding the table I posted in the beginning of the meeting):
<s​needlewoods> - Currently it is not possible to create a new non-deterministic wallet from the wallet API or wallet RPC, but it is possible in wallet2 and simplewallet. Do we want to add the functionality to API and/or RPC?
<s​needlewoods> - Not sure about the HW wallet functions, the names range between "recover", "create", "new_wallet" and "restore", but they all call `restore()` in `wallet2.cpp` which has a comment that states: "Creates a wallet from a device". And it seems creating a HW wallet from RPC is not supported.
<j​effro256> If we don't do it that way, then we're going to have to rewrite it later
<s​needlewoods> Documenting is still WIP for "Open Wallet", "Close Wallet" and "Store Wallet", so you can ignore those for now.
<s​needlewoods> And disclaimer, I don't claim this table to be complete or correct, because I tried to find a middle-line between accuracy and speed.
<r​brunner7> What I am especially afraid of that we paint ourselves into a corner where substantial expansions in the spaghetti tangle that is wallet2 code are necessary
<r​brunner7> SNeedlewoods: My take would be to take *everything* in, as long as the amount of work does not go through the roof, which it probably won't. Less chances anybody runs into problems, and less chance for some opposition.
<r​brunner7> And yeah, good naming is surprisingly difficult. At least you are free to choose if it's new stuff.
<j​effro256> SNeedlewoods: I don't think we should expose non-determinstic wallet generation yet unless specifically requested for by downstream devs or users (YAGNI)
<r​brunner7> I beg to differ. Some user may need it in many years time. If it's not in the Wallet API, we have to remove that feature from the CLI wallet, and then where would that person go to?
<jberman> it would be necessary to do that to get the CLI wallet to interface through the wallet API, and not directly with wallet2 (step 2: https://github.com/seraphis-migration/wallet3/issues/64#issue-2253543928)
<r​brunner7> For me, restoring, seed, keys, are holy.
<j​effro256> Fair enough since it's been a feature exposed historically
<jberman> I would still advocate for keeping that as a step 2, and getting rid of the wallet2 dependency in the wallet API as step 1
<s​needlewoods> Just to be clear for restoring a non-deterministic wallet there is a function already `recoverFromKeysWithPassword`
<r​brunner7> It's a bit more work, but if you just take *everything* and *all* you spare yourself a *lot* of agonizing whether to take or drop something :)
<r​brunner7> Ah, you wrote it that way, a *new* such wallet. Little misunderstanding. No, that really isn't needed anymore. If somebody wants that, they have to code it themselves, period.
<jberman> (also thank you tobtoht_ for your thoughts, I was pretty much nodding to all of that)
<r​brunner7> As long as it's possible to restore, all is well.
<s​needlewoods> jberman, for me it's unclear which way to go, I just try to follow suggestions, the "get rid of the wallet2 dependency in API" was the route I was going first, then rbrunner suggested that should be step 2 (hope I'm not misrepresenting!?), so I'm going a little back and forth
<r​brunner7> I think we have consensus, but are producing some misunderstandings right now.
<s​needlewoods> Or I'm not sure if rbunner said that should be step 2, but step 1 should be to figure out what is missing in the API first to be more precise
<r​brunner7> I really don't think you are on some "wrong" track, I can't imagine what that would be :) Don't worry.
<r​brunner7> That Markdown you gave us, that's part of that analysis "What is still missing in the Wallet API that programs like the CLI wallet, the RPC server, and third-party stull may need", correct?
<s​needlewoods> Indeed
<r​brunner7> I wonder how much will be missing in the end, just curious. It's bigger than I expected, that API, noticed while reviewing. Pretty "exotic" stuff is already there.
<s​needlewoods> I'm bad at giving estimates, so I won't try
<r​brunner7> Alright, anything more to discuss in this very meeting?
<s​needlewoods> Something less important, but still would be great to get feedback on this: Should we add "block separator" comments in e.g. one before all `public` functions, one before all `static` functions, etc.? Which one do you prefer, or do you suggest something else?
<s​needlewoods> (you can `grep`/`ctrl-f` for "// TODO : block seperator" (yeah I noticed it should be sepArator not sepErator) in this commit to see where I considered adding those comments: https://github.com/monero-project/monero/commit/19e90c1376a37f029a0afed4d99644528a12a12f)
<s​needlewoods> sorry in advance for incoming spam:
<s​needlewoods> 1. single line:
<s​needlewoods> `//-------------------------------------------------------------------------------------------------------------------`
<s​needlewoods> 2. keyword, e.g.:
<s​needlewoods> // Static functions
<s​needlewoods> 3. single line with keyword, e.g.:
<s​needlewoods> `//--------------------------------------------- Static functions ---------------------------------------------------`
<s​needlewoods> 4. keyword within lines, e.g.:
<s​needlewoods> ```
<s​needlewoods> //-------------------------------------------------------------------------------------------------------------------
<s​needlewoods> // Static functions
<s​needlewoods> //-------------------------------------------------------------------------------------------------------------------
<rbrunner7> I would say 4. There will be much more comment than before, so I think a single like is not visible enough.
<rbrunner7> Did you check how koe "did it" in his Seraphis library?
<SNeedlewoods@sneedlewoods> it is single line between every function, double line before static functions, but no special "blocks" iirc
<rbrunner7> Maybe it would be good to see a proposal in the form of an actual file, when you reach that point.
>SNeedlewoods@sneedlewoods> alright, nothing more from me then
<jeffro256> Seraphis does something similar to 2
<rbrunner7> Ok, let's close this meeting. Thanks for attending, read you again next week.
<SNeedlewoods@sneedlewoods> good meeting, thanks everyone and cu
````


# Action History
- Created by: rbrunner7 | 2024-06-21T11:47:46+00:00
- Closed at: 2024-06-24T19:10:57+00:00
