---
title: 'Seraphis wallet workgroup meeting #67 - Monday, 2024-04-22, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/993
author: rbrunner7
assignees: []
labels: []
created_at: '2024-04-19T15:00:14+00:00'
updated_at: '2024-04-22T19:26:42+00:00'
type: issue
status: closed
closed_at: '2024-04-22T19:26:41+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/990

# Discussion History
## rbrunner7 | 2024-04-22T19:26:41+00:00
````
<jberman> The analogy of current wallet API to "horse" and a new wallet API to "car" is not accurate
<jberman> A new wallet API would be very nice, but moving forwards more efficiently and pragmatically toward the actual upgrades that take Monero from horse to car (FCMP's / Seraphis / Jamtis) would be nicer
<jberman> Plus, deprecating wallet2 is analogous to a major engine upgrade. If we successfully swap out the scanner cleanly, again, that's in the thousands of "engine" lines upgraded. No reason to downplay this
<jberman> we've rewritten a scanner from scratch. And I'm now proposing swap it into the current wallet API. OBVIOUSLY that would demonstrate the scanner can be swapped into a different wallet API in the future...
<jberman> I disagree with the framing that we can't possibly upgrade the API in the future. This sequence of steps would show we absolutely can thanks to how this from-scratch wallet lib is written
<jberman> FWIW I do *also* personally think monero-serai is probably a better base to look to in order to design a new wallet API from scratch in the short-to-medium term, since it has no baggage to serve such a wide set of features already
<jberman> No reason that it should take 5 years for a functional wallet API built around monero-serai to develop, unless demand for such an API is lackluster
<jberman> I'm also not opposed to anyone who wants to work on a new wallet API today, I'd happily review designs
<jberman> But I personally don't think that's the most efficient route to taking Monero from horse to car today
<jberman> We have mountains of work to do to get the existing core feature set of CLI/GUI/RPC wallets functional with the Seraphis lib
<jberman> "improving the existing one is just as much work as starting from scratch" -> it isn't. Starting a new wallet API from scratch is at least 2-3x the work
<r​brunner7> I think I will take this into the meeting log, although you posted before the meeting, strictly speaking, jberman
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/993
<o​ne-horse-wagon> Hello.
<s​needlewoods> hey
<jberman> *waves*
<plowsof> Hi
<d​angerousfreedom> Hello
<j​effro256> howdy
<s​gp_> Hello
<r​brunner7> Alright. Any reports from last week?
<s​needlewoods> fixed some things after jberman's review and squashed https://github.com/UkoeHB/monero/pull/43
<d​angerousfreedom> First, thank you for the donations. So my next milestone will be to present a demonstrator of a basic wallet using real data from the blockchain. I wont be able to achieve it without jeffro's help I guess though. I do agree with jberman's approach of inserting his scanner incrementally and I will continue with my approach of coming up with a demonstrator for wallet3 using a PoC `CLI`. I believe I can also write an interface that this PoC CLI would use, like wallet2_api.h. This would be very useful in the future and to discuss the wallet on something concrete. What do you think?
<jeffro256> +1
<s​needlewoods> apart from that I've been trying to follow the wallet/api discussions
<jberman> me: mostly PR review (reviewed jeffros' PR for legacy indexing + PR to reduce tx writes on sync from 2 to 1, sneedlewood's^ PR on edge cases, vtnerd's p2p encryption), and design discussion 
<xFFFC0000> hello
<r​brunner7> dangerousfreedom: We will come to interfaces today later, for sure.
<j​effro256> Most reviewing kayaba's FCMP+SA+L proposal. My opinion is starting to shift towards going with the forward-secret variant of the FCMP-RCT proposal instead of Seraphis, because of 1 major reason: we get to do membership proofs over all enotes types, including previous RingCT, pre-RingCT, and FCMP-RCT, at once inside a single proof, which means we don't restart our sender anon pool
<j​effro256> I think I figured out a way to do this in Seraphis, but it's pretty inefficient to basically have 2 linking tags composition proofs per input
<r​brunner7> Ok. Today is a good day to speak about jberman 's proposal regarding our wallet API. For the record, as already mentioned yesterday, that's this here: https://github.com/monero-project/meta/issues/993
<r​brunner7> I think over the last few days we had already statements from most involved people that are for this proposal. I don't think I heard a single dissenting voice. Only ramblings from this old boomer here about missed chances :)
<dangerousfreedom> > jeffro256: My opinion is starting to shift towards going with the forward-secret variant of the FCMP-RCT proposal instead of Seraphis, ...
<d​angerousfreedom> I dont fully understand what you mean by that. You think we should totally forget about Seraphis?
<r​brunner7> Ah, you bite.
<r​brunner7> Whatever we decide on the FCMP front eventually, we will still need a wallet API. So that's probably much more immediate as a subject.
<r​brunner7> Even if we can get a majority for something as drastic as throwing away Seraphis altogether.
<j​effro256> Is this the link that was supposed to be shared ?
<r​brunner7> Ah, no, my bad: https://github.com/seraphis-migration/wallet3/issues/64
<r​brunner7> Sorry :(
<sneedlewoods> +1
<d​angerousfreedom> I'm trying to understand FCMP but it has been hard to understand all concepts.
<r​brunner7> "all concepts" is probably a bit much
<d​angerousfreedom> Looks like only kayaba understands it haha
<d​angerousfreedom> I think I now understand curve cycles :p
<d​angerousfreedom> But there is no place with a nice explanation of the Generalized Bulletproofs. I guess it is only on kayaba's head
<jeffro256> > dangerousfreedom: I dont fully understand what you mean by that. You think we should totally forget about Seraphis?
<j​effro256> I think we should keep the legacy code in the seraphis library for sure since its 10x cleaner and note modular than what we currently have
<dangerousfreedom> +1
<r​brunner7> Anyway, can we go on record with a decision to indeed choose `wallet_api` as the API for the new wallet and discuss the way forward already today?
<r​brunner7> By the way, although we are not the *full* Monero dev community, I think we *can* decide that. Everybody who is even a bit interested should know that we intend to take away `wallet2.h`, so something has to give.
<j​effro256> I'm good with that; we would need to refactor the CLI and RPC wallet sooner rather than later
<UkoeHB> Abandon Seraphis? Seriously?
<d​angerousfreedom> I'm not of that opinion.
<d​angerousfreedom> Koe created something that works now. FCMP is just a promise.
<d​angerousfreedom> Which by the way works very nicely
<r​brunner7> We will have a stern word with jeffro256 for sure :) But well, one thing after the other. We can open a lot of things to work on, for many people, if we manage to go forward quickly on that API front
<r​brunner7> And that's a good thing however which way, no?
<jberman> yes
<r​brunner7> Are people ok to talk about the details of implementation? I guess so.
<d​angerousfreedom> Yes
<j​effro256> yes
<r​brunner7> Do I see that correctly, one of the very first thing would be to make the current API complete, so that nothing at all from `wallet2.h` would strictly be needed anymore, even for something as feature-rich like the CLI wallet or the RPC server?
<r​brunner7> Going carefully through `wallet2.h`, and the *wallet_api*, compare and complete?
<r​brunner7> Thinking about it, we could do that even on current Monero master, out of all repos!
<r​brunner7> Nobody will get harmed if we just extend the wallet API
<UkoeHB> I did not get a clear answer. Who is proposing to abandon Seraphis?
<s​needlewoods> not me
<r​brunner7> jeffro256 mentioned something like that, on 20:09: "My opinion is starting to shift towards going with the forward-secret variant of the FCMP-RCT proposal instead of Seraphis"
<r​brunner7> That bombshell may derail our meeting a bit ...
<dangerousfreedom> > rbrunner7: Going carefully through wallet2.h, and the wallet_api, compare and complete?
<d​angerousfreedom> I dont understand what is the point you are making. The idea is to get rid of wallet2, right? Why you want to reimplement that on the wallet2_api ?
<r​brunner7> First, we need a really feature-complete API. And I think implement that using `wallet2` should turn out to be quite simple, so we could that pretty easily, and then really test whether it's possible to put the CLI wallet on that, if we wanted.
<r​brunner7> Only strictly in a first, transitory phase, of course.
<d​angerousfreedom> Okay so you are basically proposing a wallet2 clean-up? No new features, just more modular, readable and documented? Something like that?
<jeffro256> > UkoeHB: Abandon Seraphis? Seriously?
<j​effro256> I think it's way too early to say that all the cryptography will shake out in FCMP-RCT's favor in time before Seraphis. I still am *extremely* doubtful about the proposed 12 month timeline for FCMP-RCT; I think it'll take around twice that long in a good case. There's one main way that FCMP-RCT edges out Seraphis (for me personally): we get to have membership proofs of enotes of a<clipped mess
<j​effro256> ll mixed types (pre-RingCT, RingCT, FCMP-RCT) in one proof, which means that we don't have to start the anon pool over again. Otherwise, FCMP-RCT apparently has feature parity. If we ever change linking tag formats with Seraphis, AFAIK, we will either 1) have to restart the sender anon pool  [i.e. what is currently done in seraphis_lib] or 2) keep 2 composition proofs for the different types of linking tags inside each input proof
<r​brunner7> If we get that into master, wallet apps could start to transition already *today*, imagine that
<r​brunner7> jeffro256: That *dream* so far of FCMP plus this plus that *may* have feature parity with Seraphis. Or so.
<jberman> the wallet2_api.h feels like a misnamed filename. I also consider that part of the wallet API personally and it sits pretty high above wallet2 in abstraction that makes sense to reuse as well
<r​brunner7> Yeah, it would be nice to have better naming there. Also "wallet API" is pretty easy to misunderstand.
<UkoeHB> jeffro256: Seraphis has quite a lot of benefit to just throw away, not to mention FCMP on RCT will be much less efficient than on squashed enotes. Not sure how we got from kayabanerve insisting on Seraphis over completely different curves in the name of efficiency, to FCMP-RCT which is probably 3-6x less efficient.
<r​brunner7> Seems to me a quite accute attack of "Gras is greener over there" fever, to put it bluntly
<j​effro256> Because the API isn't *that* bad, it's just a mess of >14K lines of spaghetti code underneath that is hard to maintain and debug  etc etc. Replacing the internals and keeping the API in one form or another will allow much better downstream dev with best practices for newcomers into the space, while not breaking existing projects too badly
<r​brunner7> I think the misunderstanding was that I proposed to implement the newly completed wallet API "plus" using wallet2 code only as a first temporary and intermediate step. Test the interface, so to say.
<r​brunner7> Not something more.
<d​angerousfreedom> Yes, I see the usefulness of that. I just dont understand how it contributes to the 'new wallet' whatever it is.
<r​brunner7> Not yet. But if we can so easily, say, *validate* the new API, that must be good thing.
<d​angerousfreedom> Okay, I see.
<r​brunner7> And as I said, whoever wants, can start to switch to that API and throw out any direct wallet2 stuff *now*
<s​needlewoods> Not sure if the following is something that's important for this decision/discussion, but from my (still noobish) POV, there is already very useful and (relatively) easy to understand information to get into how seraphis works. FCMPs on the other hand fwiw seem to be more complicated, even for way more experienced cryptographers, which I assume can make it harder in the future to attract new devs.
<jeffro256> > UkoeHB: jeffro256: Seraphis has quite a lot of benefit to just throw away, not to mention FCMP on RCT will be much less efficient than ...
<j​effro256> This is why I've been working this week on the math to try to add the mixed membership reference sets into Seraphis, and see if we can get the best of both worlds, eventually weening ourselves off of the old key image format for most txs for the best efficiency with squashed enotes and smaller layers, but not having to bootstrap an anon pool completely from scratch
<j​effro256> If it turns out to be feasible, it would be cool to go that route
<j​effro256> That's completely hypothetical right now though
<d​angerousfreedom> Agree. My perception is that only kayaba and tevador (from the public people) understand what FCMP+SA+L mean. Even reviewing everything would take lots of time.
<r​brunner7> Is it really that important to have a very large tx set immediately?
<j​effro256> This is very true
<r​brunner7> I think realistically FCMPs will come, one way or another, and soon or soonish. The rest is probably "details" :)
<r​brunner7> Anyway, if nobody really says my assumption of a need to make the wallet API feature-complete so no more technical need for direct wallet2 references: Any takers for that particular work?
<r​ucknium> rbrunner7: I have this question, too. Transactions turn over very quickly. It depends what you might mean by the anon set, but in terms of volume of txs, you have over 50% of txs spending enotes less than a week old. I wonder if the anon set benefit is a code technical debt benefit or software architectural one or something like that.
<r​brunner7> *my assumption ... is wrong
<j​effro256> Realistically, if we started Seraphis v1 protocol with FCMPs, I really don't think that it would matter *that* much, but that's just an informal thought. It's a good question for our resident statistician ;)
<j​effro256> jinx
<r​brunner7> Yeah, don't let those run out of work, lol
<r​ucknium> This is can be a question about which types of users should be given more weight in these decisions. Fast spending or slow spending ones. If all txs are given equal weight, then the fast spending users are given more weight.
<dangerousfreedom> > rbrunner7: Any takers for that particular work?
<d​angerousfreedom> I can help for sure. We need a bit more clarity and consensus about the way we are going though.
<r​brunner7> That's the spirit, dangerousfreedom
<r​brunner7> Sure the devil will be in the details, but overall seems a nice starting work
<j​effro256> Assuming we have FCMPs on Seraphis, if a really slow spender got back online in say like 5 years and wanted to spend their pre-RingCT enote, they could churn to themselves once and then have the sender anon set of the last few years of Seraphis tx volume
<rucknium> +1
<j​effro256> With the only thing maybe giving away their spend is timing analysis
<UkoeHB> jeffro256: I would recommend the following:
<UkoeHB> - Adapt Grootle proofs to legacy enotes using kayabanerve's technique for blinding the Hp() points. This can be rolled out in a hardfork within 1 - 1.5yr, and gives probably 5x reference set size.
<UkoeHB> - Work on FCMP for seraphis squashed enotes over ed25519. Give up on moving to new curves.
<UkoeHB> - Roll out seraphis with either Grootle, or FCMP depending how far along they are.
<UkoeHB> - Hard-fork seraphis to start using FCMP if they aren't ready for initial release.
<r​brunner7> I feel jeffro256's fever retreat a bit :)
<j​effro256> That honestly sounds like a really good plan
<jberman> sounds fine to me too
<r​ucknium> Let me explain more about my point: Say that there are two users. The fast spender spends once per day. The slow spender spends once per week. In a seven day period, seven txs from the fast spender will appear on the blockchain. One will appear from the slow spender. If equal weight is given to all txs, the fast spender is given 7x the weight of the slow spender.
<r​brunner7> UkoeHB, are these new thoughts, and alternatives not yet discussed, or was this particular course of action discussed already somewhere?
<UkoeHB> rbrunner: This is a new plan I just came up with.
<r​brunner7> Ah, ok!
<r​brunner7> But well, even more variants and possible courses of action to discuss :) Interesting times, Chinese proverb, or so
<d​angerousfreedom> Every week new plans to take over the world :p
<j​effro256> I think this is kind of inevitable since we can't tell on-chain if its 10 guys spending 1x per day or 1 guy spending 10x per day.
<UkoeHB> If you follow that plan, step 1 means:
<UkoeHB> - Figure out the crypto theory to verify it makes sense.
<UkoeHB> - Update the Grootle proof to allow multiple parallel key sets.
<UkoeHB> - Get binned ref sets working for legacy.
<UkoeHB> - <insert typical hard fork stuff>
<UkoeHB> Also
<UkoeHB> - implement the new ownership proof
<UkoeHB> - audit the proofs and implementations
<j​effro256> Another course of action for Seraphis we could take to make the transition smoother, and remove one con vs FCMP-RCT, is to support old cryptonote addresses, which is technically possible to do with today's version of Seraphis AFAIK. It doesn't have all the same forward secrecy properties of Jamtis, but we wouldn't have to require all wallets regenerate their keys *now*
<j​effro256> (assuming no curve switch)
<UkoeHB> The grootle security proof is already done, it just needs slight adaptation for parallel keys.
<j​effro256> wdym by "parallel keys"?
<UkoeHB> Parallel key sets: K, KI, C
<UkoeHB> I mean: K, Hp(K), C
<j​effro256> ahh since it's not squashed like in Seraphis?
<UkoeHB> Yes, did you read https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86 ?
<r​ucknium> jeffro256: Yes. Anyway, I discuss the slow/fast spender problem more starting on line 325 page 11 of https://github.com/Rucknium/OSPEAD/blob/main/OSPEAD-Fully-Specified-Estimation-Plan-PUBLIC.pdf
<r​brunner7> Amazing how the possibilities seem to fan out constantly ...
<j​effro256> yes i've been reading that gist a lot that last 2 weeks. I'll admit I don't understand how the correspondence  for the "parallel" keys are done, was wondering that earlier
<j​effro256> i.e. idk how the set membership correspondence is proved to be the same for the key, commitment, and image generator at the same time
<j​effro256> but that might be off-topic for now...
<r​brunner7> Alright, anything immediate to discuss still for this very meeting? Discussions can of course continue freely.
<UkoeHB> You provide blinded versions of each key, then in the membership proof show they match with a member at a specific index. The grootle proof is designed to all parallel layers 'sign' at the same index.
<UkoeHB> so all*
<s​needlewoods> The feature complete api sounds like a good idea to me, dangerousfreedom let me know if I can help with that.
<dangerousfreedom> +1
<s​needlewoods> Nothing else from my side, thanks for the meeting everyone
<r​brunner7> SNeedlewoods: I was also thinking that may result in a nice teamwork for the two of your, if both want, of course.
<j​effro256> I think tobtoht mentioned that the wallet_api might have to be fleshed out for some lesser-used features to capture the complete functionality of `wallet2`
<j​effro256> Would be a great exercise to move CLI/RPC to wallet_api now
<r​brunner7> jeffro256: Exactly :) I was writing a lot of that while your mind was set on FCMPs for most of the meeting.
<s​needlewoods> I'd love to help
<r​brunner7> Now we are finally in the same boat regarding that.
<j​effro256> koe: very interesting. I might DM you later about this haha
<UkoeHB> It may not be as simple as I described, since you need to prove the relation between `rK` and `(1/r)Hp(K)`. But anyway, it seems plausible and worth exploring.
<r​brunner7> Alright, we are past the hour, let me close the meeting. Thanks everybody for attending, this gets more interesting by the week.
<j​effro256> thanks rbrunner. sorry for derailing, i'll still be around to talk
<tobtoht_> jeffro256: "I think tobtoht mentioned" <- I can upstream code to add coin control / other misc. features to wallet_api, but have mostly moved away from it in Feather now to get access to internal types instead of having to go through a string-ified abstraction layer every time. I think rewriting simplewallet to not use cryptonote/wallet2.h types is
<tobtoht_> going to be a lot of work, but I suppose there is no way around it.
<j​effro256> Btw rucknium thank you for that link
<rucknium> +1
<r​brunner7> jeffro256: No problem.
<r​brunner7> I am grateful that we are able to continue to discuss even "wild" ideas in a pretty civilized manner
````

# Action History
- Created by: rbrunner7 | 2024-04-19T15:00:14+00:00
- Closed at: 2024-04-22T19:26:41+00:00
