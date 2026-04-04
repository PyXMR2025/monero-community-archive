---
title: 'Seraphis wallet workgroup meeting #64 - Monday, 2024-04-01, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/985
author: rbrunner7
assignees: []
labels: []
created_at: '2024-03-30T17:27:15+00:00'
updated_at: '2024-04-01T19:11:52+00:00'
type: issue
status: closed
closed_at: '2024-04-01T19:11:52+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/982

# Discussion History
## rbrunner7 | 2024-04-01T19:11:52+00:00
````
<r​brunner7> Meeting time. Hello!
<SNeedlewoods> hey
<r​brunner7> https://github.com/monero-project/meta/issues/985
<d​angerousfreedom> Hello and happy Easter!
<rbrunner> Switching to IRC, as the old school tech that just works(tm). Happy Easter everybody, yeah!
<jberman> hello!
<SNeedlewoods> happy easter :)
<SNeedlewoods> I have to leave in a couple minutes, will check the log after the meeting
<rbrunner> Alright.
<rbrunner> So what is there to report? Looked like a quiet week.
<rbrunner> Nothing from my side, in any case.
<SNeedlewoods> from me nothing new since this update https://github.com/UkoeHB/monero/pull/40#pullrequestreview-1966738586
<SNeedlewoods> I'm still failing the tests
<jberman> Update: the async scanner PR code is done! It's much, much cleaner now (not perfect, but alas) and I've been testing the crap out of it with no issues yet. I also completed reviewing @jeffro256 's PR 9135 to reduce tx writes on sync from 2 to 1
<d​angerousfreedom> SNeedlewoods: I will have a look on the failing tests this week
<jberman> I'm working on squashing (+ organizing) the commits for the async scanner PR and benchmarking now, hoping to be done and mark the PR ready for review by EOD today
<jberman> I have ~13 individual commits planned. I think it will be much simpler to review the PR commit-by-commit in order, and then once I get the ok, I can PR individual commits piecemeal starting with commits to the Monero repo, then to the Seraphis lib
<jberman> 10 out of 13 commits are independent and can each be merged independently. It'll be fairly clear which ones are independent
<SNeedlewoods> nice jberman and thanks dangerousfreedom, any suggestion is appreciated
<rbrunner> jberman: Looking forward to it all!
<d​angerousfreedom> From my side, I briefly reviewed ghostway's KeyContainer and I continued working on improving the [wallet demonstrator](https://github.com/DangerousFreedom1984/seraphis_lib/tree/wallet3_transfer_demo2) to fix some issues. If you have time, I invite you again to give me your opinion about it.
<d​angerousfreedom> I also opened a new [CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/442) with the goal of moving from the mock_ledger to a regtest.
<jberman> Then was planning to move to checking over SNeedlewoods PR as well
<o​ne-horse-wagon> Hello.
<d​angerousfreedom> nice jberman
<rbrunner> dangerousfreedom: Will try to find time to look at it. I think that would be well deserved
<SNeedlewoods> the tests I did with wallet3_demo worked as expected, but haven't looked at the code yet 
<SNeedlewoods> have to go now, cu later
<d​angerousfreedom> You can compile and then run ./monero-wallet3, then 'help' and play with the creation of enotes and so on...
<j​effro256> Howdy sorry I'm late
<rbrunner> We were already close to firing you :)
<j​effro256> lol
<rbrunner> We are still in the "reports" section. Anything from your side?
<j​effro256> Working on Seraphis internals: serialization, CLSAG ref set indexing, simplifying seraphis ref set config
<rbrunner> Sounds like moving full steam ahead
<rbrunner> Looking forward to wallet PRs, if any resulting from that already. We could use a few more to show.
<rbrunner> If we are complete about the reports, I would like to make sure everybody knows that this Wednesday's meeting could get very interesting and important
<rbrunner> kayabanerve will present a new approach of "FCMPs on RingCT" - or so
<rbrunner> *MRL meeting
<rbrunner> I have left my view about such a project and "our" Seraphis and Seraphis wallet work over in the MRL channel / room
<rbrunner> from a project management point of view
<jberman> will be there
<rbrunner> For me personally the thing that is most prominent in my mind is not taking decisions based on illusions
<rbrunner> but on realistic assumptions about the trade-offs regarding timelines involved all around
<jberman> I have some probably contentious thoughts on reducing the Seraphis timeline... sticking with the current wallet API (and strictly replacing wallet2) would probably cut off 6 months to a year of development at least. I would even go so far as to suggest that sticking with the CLI/RPC/GUI wallets as is and strictly aim to swap out usage of wallet2
<jberman> This would affect the work @dangerousfreedom is currently doing
<jberman> Further, in order to speed up the timeline to deployment, I would also suggest focusing work right now on making the Seraphis lib fully functional for legacy today, swap it in and replace wallet2, get it out there so devs can start using it today and the ecosystem is then prepared for the Seraphis lib, then proceed with Seraphis-consensus work
<jberman> Then replacing the wallet API could proceed after the Seraphis fork
<j​effro256> So basically write in a drop-in replacement for wallet2 for now?
<jberman> yep
<jberman> using the new key container, enote store, async scanner, etc.
<rbrunner> Would probably need some "going into details" whether this is realistic, given the differences that you just can "magic" away between Monero now and Seraphis/Jamtis based Monero
<j​effro256> I think I can agree with that. Tbh, the API of wallet2 isn't all that bad in itself, it's just the internals are spaghetti
<j​effro256> Some details, however I think would have to be changed
<rbrunner> Well, if keeping the "not to bad" wallet2 interface makes the difference between no Seraphis and Seraphis, *realistically* ...
<j​effro256> The biggest thing that probably needs to change now in order to support a not ugly internal engine is how transfers are indexed
<jberman> Agree, I also don't think it's a simple hand-wave "everyone is prepared for Seraphis", but using the Seraphis lib for major components sooner rather than later imo is a doable goal that is a huge step forwards toward Seraphis/Jamtis
<jberman> ya agree with jeffro's assessment there as well
<rbrunner> I think nobody will stop you people investigating this scenario in earnest.
<j​effro256> Right now the API uses fixed integer indices into a vector of stored transfers in increasing scan order. That is a leaky abstraction that won't play well with the new SpEnoteStore
<jberman> yep
<rbrunner> Of course it's a pity, if you think what nice interfaces we could possibly come up out there on the green field, but alas, harsh realities
<rbrunner> I think actually starting to use the Seraphis library for something would also make "Seraphis might be 5 years out" a bit less probable
<jberman> I also think getting rid of wallet2 is a huge technical debt lift in and of itself, which is a strong win
<rbrunner> I was just thinking that a review of the whole Seraphis lib would the roll towards us ...
<rbrunner> But of course sooner or later that will have to take place
<rbrunner> So the two of you, jberman and jeffro256, will auto-organize to look at this possible scenario in detail?
<jberman> Sure
<rbrunner> Feel free to use this room for discussion, would love to be able to read along, maybe other people as well.
<rbrunner> Also from a documentation point of view of course
<rbrunner> Or with GitHub issues
<rbrunner> Alright, anything else for this meeting today?
<j​effro256> Yeah that can definitely be done
<d​angerousfreedom> I am a bit confused with your statements jberman , sometimes I have the impression that you want to make a smooth change into seraphis and keep using wallet2 and now I have the impression that you want to throw wallet2 in the garbage haha. Up to now I am only concerned in creating a useful seraphis wallet and not using wallet2 at all - while being compatible with legacy enotes. Of<clipp
<d​angerousfreedom>  course we are not there yet, but I think we are getting closer and closer.  What do you think we should do differently?
<rbrunner> It's the difference between "wallet2 the implementation" and "wallet2 the API", roughly between .cpp and .h
<rbrunner> The proposal is to throw away the .cpp *but* keep the .h as closely as possible
<rbrunner> And not come up with a brand-new wallet API, designed out there on a green field
<rbrunner> As a compromise to get Seraphis lib code into production earlier, and getting rid of wallet2 spaghetti earlier
<jberman> Understand the confusion here. Confusion is stemming from this idea here which I've mentioned I support as well: https://github.com/seraphis-migration/wallet3/issues/48
<rbrunner> It could well be that things with your code did not yet progress to a point where you had to throw away much with this approach
<jberman> My proposal right now: CLI/RPC/GUI -> wallet API (same as today) -> Seraphis lib -> wallet2 for constructing legacy txs as needed
<rbrunner> Yeah, that would mean to keep wallet2 .cpp around after all, but in a *much* reduced role, like you say, basically just for tx construction
<rbrunner> And not public anymore
<rbrunner> We would have something like wallet2.5.h or so :)
<rbrunner> wallet2.h only with modification we are forced to do
<j​effro256> Oh so you're not saying we bind to the same `tools::wallet2` API, but just the `Monero::Wallet` API? I think I was getting confused between those 2
<rbrunner> What do you mean with "Monero::Wallet"?
<tobtoht_> jberman: CLI uses wallet2 directly
<j​effro256> So does RPC IIRC
<rbrunner> Maybe you have to think a bit more in abstract ways for now
<rbrunner> Yes, if you are really talking about that strange "wallet lib", only the GUI is using that in the core Monero codebase
<j​effro256> rbrunner7: `Monero::Wallet` is the class interface in src/wallet/wallet2_api.h
<j​effro256> So the term "wallet2 API" is kind of ambiguous..
<jberman> we could reuse the wallet2_api.h, with the primary goal being to stop using wallet2.cpp logic
<rbrunner> Ah, ok. Well, if wallet2.h basically stays, I think also that API could basically stay the same
<jberman> the wallets are very tightly woven with wallet2 right now, as tobtoht_ is saying here
<jberman> I still think it would be significantly less work to de-couple from wallet2 than to rewrite the API and rewrite the wallets from scratch
<j​effro256> Keeping the `tools::wallet2` interface the same would definitely reduce downstream rewriting
<rbrunner> Did I misunderstand the proposal as well? I was understanding to primarily keep good old `wallet2.h`
<rbrunner> Only with keeping that you can basically keep the CLI wallet and the wallet RPC server
<rbrunner> Being able to keep `wallet2_api.h`also would just follow from that naturally, of course
<j​effro256> Maybe we could start rewriting RPC/CLI now to use the `Monero::Wallet` wrapper and then just re-implement `Monero::WalletImpl` for Seraphis
<rbrunner> Is that really a big win? I never really looked closely but got the impression that `wallet2_api.h` is only a pretty thin layer
<d​angerousfreedom> The seraphis lib is capable of using legacy enotes to create seraphis enotes. I would not focus on creating pure legacy enotes using the seraphis wallet. Do you mean you want to do that? During the transition period, anyone willing to use the classical wallet2 would be able to do so to create transactions normally. The verification of legacy enotes can be done using the seraphis wallet.
<rbrunner> that doesn't do a lot of "heavy liftign"
<rbrunner> That wrapper isn't even complete, no?
<tobtoht_> jeffro256: "Maybe we could start rewriting RPC/CLI now to use the `Monero::Wallet` wrapper" <- that would mean a expanding Monero::Wallet by a great deal first, it's only provides a subset of wallet2 functionality
<rbrunner> My gut feeling tells me such a rewrite would be mostly a waste of time. You can as well go "hardcore" and really keep `wallet2.h` mostly intact, IMHO
<rbrunner> That's also more "honest" in my view. We compromise, let's get over it.
<rbrunner> Don't try to put lipstick on that compromise :)
<jberman> "I would not focus on creating pure legacy enotes using the seraphis wallet. Do you mean you want to do that?" -> no, but we should have some functionality to take a Seraphis enote store, and use it to construct a legacy tx with wallet2
<rbrunner> dangerousfreedom: You might want to read (again) the linked issue of mine. I tried to detail the idea there.
<jberman> that way instead of relying on wallet2 to keep and manage state, we move toward leaning on the Seraphis lib enote store
<jberman> I don't know yet what would be the smoothest path toward deprecating which files / sections of wallet2, but the general idea is to move away from using wallet2 for state today
<rbrunner> Yeah, without using the Seraphis enote store it's not really a Seraphis lib based wallet ...
<rbrunner> Ok, we are approaching the full hour. Let's close the meeting proper. Thanks for attending everybody, has been very interesting. Read you again next week!
````


# Action History
- Created by: rbrunner7 | 2024-03-30T17:27:15+00:00
- Closed at: 2024-04-01T19:11:52+00:00
