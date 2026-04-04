---
title: 'Monero Tech Meeting #160 - Monday, 2026-03-09, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1350
author: rbrunner7
assignees: []
labels: []
created_at: '2026-03-06T13:52:33+00:00'
updated_at: '2026-03-09T20:49:44+00:00'
type: issue
status: closed
closed_at: '2026-03-09T20:49:44+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1347).


# Discussion History
## rbrunner7 | 2026-03-09T20:49:44+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1350
<jeffro256> Howdy
<vtnerd> Hi
<jpk68> Hello
<jberman> waves
<sneedlewoods> Hello
<j​effro256> Seems like we lost a contributor just a few moments ago
<r​brunner7> Nice round today. So what are the reports from last week?
<r​brunner7> jeffro256: Yeah, looks like it.
<UkoeHB> Hi
<r​brunner7> UkoeHB: Welcome back :)
<j​effro256> Hi koe!
<v​tnerd> Tracked down the tx-notify issues on both stressnet and mainline. Upcoming work is to update the lws+lwsf patches to the new changes in fcmp++-stage
<s​needlewoods> According to my investigation, out of the 53 [wallet rpc error codes](https://github.com/monero-project/monero/blob/master/src/wallet/wallet_rpc_server_error_codes.h), only 14 of them need to be handled/propagated by the Wallet API
<jeffro256> +1
<j​effro256> Me: Rebased fcmp++-stage against master to prepare for beta stressnet: https://github.com/seraphis-migration/monero/tree/fcmp%2B%2B-stage-new-3-7-2026. Writing stressnet-specific PRs (stressnet window size change, RPC config changes, etc) locally against it, also to prep for beta. Beefing up testing for hot/cold wallet PR.
<r​brunner7> SNeedlewoods: Sounds like good news for the approach
<j​berman> Had some discussion with koe re: integration audit plans (excited to have koe back!!), koe proposed combining phases 1 & 2 together since phase 1 is a fairly small amount of work. I'm currently preparing the PR's for phase 2 right now, and aiming to complete that today & begin audit comms tomorrow
<sneedlewoods> +1
<UkoeHB> Me: rereading ztm2, reviewed the current state of fcmp++ with jberman’s help
<sneedlewoods> +1
<s​needlewoods> I still didn't do your proposal justice, went with my `exception_ptr` idea so far, but I'm planning to answer on the issue you created once I get my notes done
<r​brunner7> More eyes on FCMP++ are certainly very welcome
<UkoeHB> Planning to read the carrot paper and review the carrot_core PR so it is closer to mergeable when audits are done. Then try to figure out multisig
<UkoeHB> What are the review/audit intentions for carrot_core?
<j​effro256> Cypherstack audited carrot_core recently: https://github.com/cypherstack/carrot_core-audit/
<UkoeHB> Thanks, missed that one. Are there any other carrot-related audits?
<j​effro256> Not at the moment, but it would probably be worth auditing some of the transaction construction code in carrot_impl at some point
<UkoeHB> Ok. Do you think it would still be worthwhile for me to review carrot_core? I will at the very least do a partial review to understand the code.
<j​berman> There were these as well: https://github.com/jeffro256/carrot/tree/master/audits
<r​brunner7> Maybe that answer about review will get answered in a bit.
<r​brunner7> If we are through otherwise with the reports, I have something coming out of my journey into Polyseed that I would like to put on the table.
<r​brunner7> It started with this comment from Tevador: https://github.com/tevador/polyseed/issues/13#issuecomment-4007864335
<r​brunner7> It seems that there is an important difference between now and Carrot, that the main "secret" is a point on the one hand, and just 256 bits (a scalar?) on the other hand
<r​brunner7> And that this will have consequences about handling of seeds, and the need or not to reduce
<j​effro256> Ah yes ^ the spec reviews too
<j​effro256> koe: yeah if you are going to be looking over the code anyways, it would appreciate any feedback on it!
<r​brunner7> I worry that this has the potential to cause trouble with no end when restoring from seed, because the code may do either a reduce too much, or miss one
<UkoeHB> jeffro256: ok
<j​berman> > I would advise against supporting legacy seeds with new wallet types unless we think it's OK to require users to manually input their hierarchy type (legacy/Carrot/Jamtis) when restoring a wallet
<j​berman> I have thoughts on this comment by tevador. First off, even if we didn't support legacy seeds with new wallet types, there has to be a way to differentiate if a user is restoring a legacy wallet or a Carrot wallet into perpetuity
<j​berman> I think using a feature bit may make sense for Carrot
<jbabb> +1
<r​brunner7> Yes, that's a slightly different question
<j​berman> Second off, I'm in favor of continuing support for the legacy seed type primarily so that people who don't want to use the new view balance key have the option to not use it
<jbabb> +1
<j​effro256> I've been thinking about this, and I'm getting closer to saying that it doesn't really matter for security, since the original entropy is only 128 bits. Reducing probably doesn't affect the security a non-negligible amount since the scalar space is ~232 bits, so even though the reduction "removes" ~4 bits, the probability that many 32 bit secrets, generated by 128 seeds, reduce to<clipped 
<j​effro256>  the same scalar is pretty small
<j​effro256> But plz take it with a grain of salt, I'm just spit balling
<r​brunner7> Do people see the potential for confusion, wrong wallet restores, etc, that I see?
<jbabb> +1
<j​effro256> I could definitely see a possibility for some implementation weirdness
<r​brunner7> If you have to decide whether to reduce or not, and the correctness of the info given about the type of seed decides whether the restore succeeds, that's pretty fragile IMHO
<j​effro256> It does, although it would be nice to have a seamless upgrade with the same seed phrase. Although that may make the people against OVKs uncomfortable
<j​berman> If we have a way to differentiate legacy and Carrot seeds (which I think we will need no matter what), then I think Carrot wallets always XOR'ing when a passphrase is provided makes sense (i.e. the mechanism for Carrot seed restore when passphrase is provided is the same even regardless of whether or not an encrypted feature bit set. the benefit of the encrypted feature bit is tha<clipped me
<j​berman> t if it's set, then wallets should require a passphrase input)
<r​brunner7> Hmm, we have several things inter-relate with each other here.
<r​brunner7> That's again a potential pittfall, if we suddenly have *two* methods how to apply seed offsets, and wallets can disagree which to apply
<r​brunner7> I have a concrete proposal for discussion: To become less fragile, let's "sacrifice" 4 bits of Carrot master secrets by reducing them as if they were points, and then continue to use subtracting seed offsets for *all* types of secrets/keys
<j​berman> I don't see how to achieve a seamless upgrade with the same seed phrase
<j​babb> the people uncomfortable with OVKs can just not use them
<UkoeHB> rbrunner: points use 256 bits, scalars are 253 bits
<j​effro256> New addresses replace old addresses in UI, the generate-addres tier works for new addresses, old addresses still work though, if funds are all held in new addresses, then OVKs can be used
<j​effro256> They don't seem to understand that ;)
<r​brunner7> UkoeHB: Now I am pretty confused
<r​brunner7> Maybe I am just using terminology wrong
<r​brunner7> "Reduce" leaves a smaller number, right?
<j​berman> hmm, I don't know if I'd call this seamless. For one, wallets will still need to scan both for legacy and new, no? For two, I'd argue replacing addresses in the UI is a pretty major UX change
<jbabb> +1
<UkoeHB> A point is two coordinates, a single coordinate is 255 bits and the second coordinate is signified by a sign bit.
<UkoeHB> So both require reduction
<j​effro256> You can share the private view-incoming key if you know that you're using an old Polyseed
<r​brunner7> Is at least my assumption correct that if we just go ahead and reduce Carrot master secrets we lose 4 bits? Which we may deem acceptable in the interest of making things less brittle
<j​effro256> Replacing the addresses being a big UX change is fair. For someone who doesn't expect it, but memorizes the characters in their addresses, that could be scary
<r​brunner7> Looks like there are at least 3 important issues to discuss surrounding Carrot keys ...
<j​effro256> You don't even lose 4 AFAICT since the original entropy is 128 bits, much less that the total scalar space of 232 bits
<j​berman> The default user isn't sharing private view keys with anyone, and I'm saying seems the local wallet would have ~2x'd scanning work
<jbabb> +1
<r​brunner7> With Polyseed only, right? Legacy seeds can produce the full 256 bits
<j​babb> I had assumed that we'd basically add scanning of carrot addresses alongside the legacy scanning but had hoped we could just cleanly adopt and move to carrot at hf.  but that won't be happening, will it?
<j​babb> that is, we will be scanning legacy and carrot post-hf?
<r​brunner7> Oh, so it's 256-232=24 bits we are talking about?
<j​effro256> Think of it like this, if the seed phrase was only 10 bits (1024 possible combos), then reducing would like almost certainly have 0 effect on the number of possible secret keys, since the probability of 2 of the 1024 32-bit secrets reducing to the same scalar is near 0
<j​effro256> Yes, legacy would have a reduction of ~4 bits, which still means they beat Polyseed by about 104 bits :)
<UkoeHB> 232? Now I’m the one confused lol
<j​effro256> I'm saying that the wallet would automatically share the private view-incoming key with the 2 key hierarchies, so the scanning work stays the same
<r​brunner7> So there is not much to worry about losing bits, essentially, and we can discuss trade-offs. Like the somewhat illogical step of reducing something that does not need reducing, technically.
<j​effro256> Sorry, 252
<rbrunner7> +1
<j​berman> Ahhh, I follow
<UkoeHB> jeffro256: 253, no? Unless I wrote it wrong in ztm2
<j​effro256> So legacy beats Polyseed by 124, excuse me. The point is that the reduction doesn't really matter for security I believe
<j​effro256> Uhhhh you're probably right, I'm going off of memory rn
<j​effro256> Whatever size l is
<r​brunner7> I think we would really profit if we don't let full 256 bit numbers occur anywhere, at any time, if it is about the "master secret". Easy to check, easy to handle, hard to produce bugs and wrong restores etc.
<j​effro256> It's 252 plus change
<r​brunner7> Yeah, it's not about "full" bits :)
<UkoeHB> If the entropy is ~128 bits, then reducing an expanded 256 bits to 253 will lose half the reduced bits, so ~2 bits.
<j​berman> Ok I concede on the point of scanning not needing to be ~2x'd if legacy seeds were upgraded to Carrot seeds
<r​brunner7> By the way, subtracting instead of XOR also for Carrot has the small advantage that really paranoid people can subtract more than once
<r​brunner7> And produce progressively more filled families of decoy wallets
<r​brunner7> (But only with legacy seeds maybe?)
<j​berman> The UX challenge of having both legacy addresses and Carrot addresses from one seed seems tricky still in my view
<r​brunner7> Yeah, that could cause confusion on a whole new level
<r​brunner7> I am not sure the trade-offs are good for such combined wallets
<j​babb> in an ideal world at hf we could just by convention move to carrot addressing and so by convention be able to not have to scan legacy past that point
<r​brunner7> Even if possible in theory
<j​babb> unfortunately wallets are going to need additional controls
<j​berman> I wouldn't necessarily call this a real advantage. You can hash a passphrase as many times as you want too and derive n seeds from a ciphertext that way
<UkoeHB> jbabb: existing addresses posted in the wild need to remain functional
<j​berman> > existing addresses posted in the wild need to remain functional
<j​berman> ya this is a critical aim with the hf
<j​babb> very true, it's nonsensical really to suggest we'll be able to stop scanning legacy
<j​babb> some wallets will choose to only use legacy, some will move to carrot, some will support both
<r​brunner7> But still we don't have to support "mixed wallets", with two sets of keys, right?
<r​brunner7> It's all already complicated enough, if you ask me.
<sneedlewoods> +1
<UkoeHB> Monero has a history of only supporting old stuff to the extent of backwards compatibility, but not to the extent of full ongoing support.
<j​babb> practically, yes
<UkoeHB> So never producing new legacy addresses seems appropriate.
<r​brunner7> It took only one tiny feature bit ("Encrypted?") and different wallets doing different things with it to create a mess with Polyseed
<r​brunner7> We have wallets failing to restore an encrypted Polyseed silently, without any warning.
<UkoeHB> Old seeds will always scan both legacy and carrot, new seeds only scan carrot, and the core wallet UI only presents new carrot addresses (but tx history and address balances include legacy).
<j​babb> +1
<j​berman> I think it will raise the controversial elements of the hf (specifically the ovk) a significant degree by not supporting the creation of legacy seeds after the hf in core software. I'm also fairly certain wallets in the ecosystem emerge that support new legacy seeds
<r​brunner7> Agree.
<r​brunner7> Basically impossible to prevent.
<j​babb> a monero-wallet-cli flag to enable legacy seeds/addresses would suffice
<r​brunner7> We also have hardware now that produces Monero keys and addresses, I believe
<r​brunner7> I am more thinking about smartphone wallet apps, that are in competition regarding supporting features.
<r​brunner7> The more, the better sometimes.
<j​effro256> I'm somewhat fine not supporting the new key hierarchy in Polyseed, forcing the user to move over to a new seed phrase to get the new features. However, I'm much more worried about hardware wallets. Ideally, a HW user should NOT need to change their seed phrase to use new feature s
<j​berman> I think supporting both legacy + carrot addresses from 1 seed will carry a load of complexity wallets will need to deal with, both from a UI perspective and internal code
<UkoeHB> jbabb: instead of a flag, the cli wallet API could include ‘new legacy_address’ in addition to ‘new address’ creating carrot addrs.
<r​brunner7> Again, agree. I personally would like to just shoot that down :)
<r​brunner7> (to jberman )
<UkoeHB> And new legacy_address would error for new seeds
<j​babb> UkoeHB: +1.  rbrunner7, this and anything accessible via wallet2 will suffice for Cake and Stack at least, which both use wallet2 via MrCyjaneK's monero_c project (which he's updating for stressnet with Cake too btw)
<j​babb> it shouldn't be monero-project/monero's job to maintain support for every experimental wallet's format, but vice versa: imo it's all the other wallets' job to reproduce monero-wallet-cli behavior, not the other way round
<j​effro256> Do you plan to tell HW users that they simply don't get the new features because of the complexity for us?
<j​babb> if polyseed even "officially" adopted in "core" software?  is in in-scope yet?
<j​babb> is*, sorry.
<j​pk68:matrix.org> UkoeHB: Why make legacy_address error? I have no problem with Carrot or anything, just wondering
<j​effro256> FWIW, a lot of code in the Carrot integration was written in mind to support hybrid key hierarchies
<j​babb> is polyseed even "officially" adopted in "core" software?  is it "in-scope" yet?*
<UkoeHB> jpk68: because new seeds would only be expected to scan with the carrot method
<UkoeHB> An expectation required for cross-wallet compatibility
<j​berman> I think that's completely fine yes. It's also not just the complexity, it's also the controversy surrounding the ovk. I think it's 100% reasonable to say if you want an ovk, create a new wallet and transfer funds to it
<r​brunner7> "Do you plan to tell HW users that they simply don't get the new features " That's formulated a bit harshly, no? They are one new address generation and sweep away from the new features
<j​pk68:matrix.org> UkoeHB: Fair point
<j​effro256> Is it reasonable to tell HW users to change seed phrase when A) people hold BTC, ETH, LTC, DASH, etc other coins on their wallet, and B) it defeats the entire point of a HW to be messing with seed phrases?
<r​brunner7> I can only repeat that we managed to produce a fine mess with something as simple as a Polyseed feature bit, because of different wallet implementations. Aren't people here as pessimistic as I am regarding possible trouble? :)
<j​babb> rbrunner7: is that all of our jobs to clean up and support going forward, though?
<j​effro256> They're aren't one sweep away if A) they hold other coins, or B) if they plan to support old addresses they have posted elsewhere
<UkoeHB> jberman: can you elaborate why old seed wallets defaulting to making new carrot addrs would be problematic? (with the caveat of a minimal API to generate legacy addresses)
<j​berman> They created a seed without the ovk in the first place, I think if they don't want the ovk, they'd would be ok with not having it, and if they want the ovk, they'd be ok with taking an extra step
<r​brunner7> jeffro256: The HW could produce a new Carrot secret from the one master HW multi-coin secret?
<r​brunner7> Treating Carrot basically like a new coin
<j​effro256> rbrunner7: exactly
<r​brunner7> Thus I don't see the problem...?
<j​berman> @UkoeHB: if a user already sees address X in their wallet, and then stops seeing that address, and/or the UI is telling them "use Y address instead", I think that is a confusing pain point to illustrate cleanly to users
<j​effro256> Sorry, the new coin part seems like unnecessary cruft, but otherwise, yes
<r​brunner7> Anyway, seems to me we have so many complex open issues that we most probably won't reach our famous "loose consensus" about any of them today
<j​berman> Or are you saying, if UI has already displayed X addresses, don't change anything with X addresses, and just show new Carrot addresses when creating new addresses going forward
<UkoeHB> Yes only make new addresses as carrot.
<r​brunner7> We had x people freaking out because one HW wallet did not support the display of integrated addresses, remember?
<UkoeHB> Displaying wallet history has to continue displaying legacy addrs.
<j​effro256> The device can still inform users of a change TBF. It can either be a bit stored in persistent storage on-device, or the hot wallet can call some endpoint if the HW device is old, but the wallet cache stores that the user hasn't accepted the dialouge yet
<j​effro256> That's just a straight up bug in the Ledger wallet, not a conscious design decision. I don't see how that's relevant
<UkoeHB> The cli can display a warning/notice message when ‘address’ returns a legacy addr for old seeds. To inform the user that carrot is available. And maybe add a cli command to switch ‘address’ display to carrot (saved in wallet data, has to be re-set on restore).
<j​berman> @UkoeHB: continuing to display already displayed legacy addresses is better than what I originally thought. Imo it's still a bit of a gross thing to fully deal with if all wallets don't already converge on exactly what they display to users
<r​brunner7> jeffro256:  It's not technically relevant, but it illustrates how users react if they don't understand something. Like addresses that seem to change at a given point in time, if I understand the proposal correctly
<UkoeHB> jberman: a bit of grossness seems inevitable. One big point of carrot over jamtis was ~seem less transition of existing seeds, no?
<jbabb> +1
<j​berman> The next tricky aspect to manage is storing both already displayed suabaddress index maps of legacy and carrot, and correctly only using Carrot addresses on new. The latter will also require a synced wallet to handle properly
<j​berman> The biggest point as I understood it was backwards compatibility so legacy seeds still received major new benefits of Janus protection, forward secrecy, etc.
<j​effro256> Fair enough. But the Leger integrated address issue is where the users are absolutely correct in that is a bug, there's not necessarily confusion there AFAICT. The only "confusion" is the fact that sending to an integrated address on a Ledger simply isn't verifiable
<j​berman> And that legacy was indistinguishable from Carrot on chain
<r​brunner7> I respect jeffro256 's dedicated efforts to support "hybrid" wallets with 2 sets of keys, but really ... do you think that complex address display trick described here will *ever* really work reliably over the whole wallet app ecosystem?
<j​effro256> UkoeHB: okay there's 2 components. There's CARROT, which is the addressing protocol, i.e. how to send XMR from sender to receiver, and how to send XMR to self. Then there's the new key hierarchy, which is recommended in the CARROT spec. No one needs to do anything whatsoever to use CARROT. In fact, CARROT is being used actively on the Alpha Stressnet right now. We're talking about<clipped 
<j​effro256>  how to introduce the new key hierarchy
<UkoeHB> Ah, fair. And legacy addrs continuing to work. But I think it’s unreasonable to say carrot requires full wallet replacement just because of UX awkwardness. Anyone with serious wallet security will have a big pain replacing their seeds (eg people storing in lock boxes, hardware wallets, etc).
<j​babb> well we have to have two sets of keys anyways, it's about how to present them
<j​babb> we can't control wallets that want to keep presenting only legacy. "monero-wallet-cli-classic"
<j​babb> we have to have two sets of keys for legacy seeds*
<j​babb> for pre-existing wallets, that's a given
<r​brunner7> Yes, but you don't have to "switch" anything with address display if we don't support hybrid wallets, if I think about it correctly.
<r​brunner7> And *that's* were it seems I and jberman see a big tangle of complexity
<j​berman> There could be a way to create a Carrot-maxxed wallet from an existing master bip39 seed with a UI toggle
<r​brunner7> How about one person saying "I sent you the XMR, to this address" and the other person says "What? I cannot see such an address at all"?
<UkoeHB> rbrunner7: you have to switch either way, it just depends where the switch occurs.
<UkoeHB> The cli has to support both UIs.
<r​brunner7> Ah, no that particular example won't happen if the wallet app works correctly
<UkoeHB> Either separate UI or merged.
<r​brunner7> Not sure what you mean with "separate UI". The addresses have the same format?
<r​brunner7> Display of secrets differs of course
<j​babb> the cli will have to present whether an address is legacy or carrot
<r​brunner7> Really?
<j​babb> ha, maybe not, actually.
<r​brunner7> It must be able to tell you what kind of wallet you have, yes. But addresses?
<j​effro256> For the basic user, I'd imagine that they don't really care which address is of which type
<jbabb> +1
<UkoeHB> It would be useful to describe each of the two ‘solutions’ in detail (CLI modifications, UX flows) so they can be compared fully. New GitHub issue?
<r​brunner7> UkoeHB: Sounds like an idea.
<j​berman> +1
<r​brunner7> Now we just need a volunteer to write that ..
<j​babb> ha, maybe not, actually.  edit: definitely not, sorry.  I was considering a merged UI but that also wouldn't be required.
<UkoeHB> rbrunner7: I can do it
<j​berman> fwiw, the Carrot spec even says section 2.2 is for New wallets only "Existing Monero wallets will not inherit these features, unfortunately" .. it would definitely be a deviation from the info out now that existing wallets will gain the new feature set
<jbabb> +1
<r​brunner7> Splendid, UkoeHB!
<r​brunner7> Might help you to get into Carrot, in fact
<j​berman> (and that all wallets would have ovk's after the fork)
<r​brunner7> Well, you could make it an extra step "Create a hybrid wallet", no?
<j​effro256> I can also write up a more detailed version of what I've been trying to describe since I've been the one harping on it. Then we can compare / improve both
<r​brunner7> Even better. After all, much is at stake here.
<j​effro256> I guess it depends on what your definition of a wallet is, but yeah I can see why that would be confusing
<r​brunner7> Not only technically, but also regarding UX, that much should be clear now
<j​berman> Another annoying UX quirk is that the ovk doesn't even capture all of your txs because you can have mixed legacy txs
<j​berman> so it would be a watered down addition of the feature set
<j​effro256> Maybe could be worded as "*Without deriving new material*, existing Monero wallets will not ..."
<r​brunner7> Hmm, is that correct? That sounds bad, the OVK failing with hybrid wallets
<j​effro256> Yes, until you spend the funds sitting in legacy addresses
<r​brunner7> Coin control to the rescue, for everybody :)
<r​brunner7> Ok. That might be our longest meeting ever :) I think despite much left to discuss, and even more to finally decide, we can close the meeting proper, and continue to discuss during the week, or at the next meeting at the latest.
<r​brunner7> Thanks everybody for attending, read you again next week!
<r​brunner7> Interesting times indeed
<sneedlewoods> +1
<s​needlewoods> thanks everyone, cu
<j​pk68:matrix.org> :)
````


# Action History
- Created by: rbrunner7 | 2026-03-06T13:52:33+00:00
- Closed at: 2026-03-09T20:49:44+00:00
