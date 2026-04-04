---
title: 'Seraphis wallet workgroup meeting #51 - Monday, 2024-01-01, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/950
author: rbrunner7
assignees: []
labels: []
created_at: '2023-12-29T20:33:02+00:00'
updated_at: '2024-01-01T19:05:12+00:00'
type: issue
status: closed
closed_at: '2024-01-01T19:05:12+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/945

# Discussion History
## rbrunner7 | 2024-01-01T19:05:12+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/950
<g​hostway> Hello
<s​needlewoods_xmr> hey and happy new year
<g​hostway> Indeed :)
<r​brunner7> Right :)
<j​effro256> Howdy
<plowsof> hi all 
<r​brunner7> Anything to report, from last year still?
<r​brunner7> The CCS came back to live. And everything funded so far.
<g​hostway> If no one has any tasks, I'll try and resolve stuff in curve trees 
<g​hostway> But probably I need to get the key container merged already
<s​needlewoods_xmr> made a little progress on https://github.com/seraphis-migration/monero/pull/16
<r​brunner7> ghostway: I think that the container needs some work still, right?
<g​hostway> I don't remember, but some stuff needs to be talked about too
<g​hostway> Are separate serialization structs necessary? Is the security adequate?
<s​needlewoods_xmr> but still stuck on finding the right place from where to fetch enote_same_amount_ledger_index
<g​hostway> Is all information required to try and help in the issue?
<g​hostway> If you have any conclusions or anything
<g​hostway> I think it'd be helpful to write here, maybe
<j​berman> I've got spotty connection at the moment, but small update: found a minor issue in polyseed basically the same as the one I recently posted with classic seeds: https://github.com/tevador/polyseed/issues/11
<j​effro256> I wanted to talk about the enote store: serialization: I think we should avoid the pattern of serialization that we were using before with wallet2 where we serialize the entire thing as one huge chunk since that is human noticably slow. The enote store will likely be the majority of the data that we store so I think its worth looking st real database solutions (namely LMDB)
<r​brunner7> Yes, maybe it would be helpful that you "think aload" here, ghostway , so we can finally settle things over the next days
<r​brunner7> Well, I once constructed a wallet with several thousands of inputs, to check whether things become too slow, and I didn't notice.
<r​brunner7> I am not sure where you saw something "human noticably slow", or whether that really was the pure write or load time.
<j​effro256> At least for me, on my piece of crap laptop, my wallet cache is 25 MB and it takes about half a second to write it to disk
<r​brunner7> I also wrote this early issue: https://github.com/seraphis-migration/wallet3/issues/11
<j​effro256> But especially if we're going to support find-received/assist-filter wallets at a personal level, we'll be storing ~1% of all the block chain data in the wallet cache. That will be super noticeable when storing
<r​brunner7> From a certain point on, surely?
<j​effro256> I'm glad you made an issue for that though , I'll look at it
<r​brunner7> Not much there, except a place for discussion ...
<j​effro256> Yes from the point of wallet creation
<r​brunner7> What bugs me to quite some degree about that "wallet cache with LMDB" is the jump up in complexity to handle the stuff.
<r​brunner7> Very simple code, or almost no code, gets replaced by database handling code.
<r​brunner7> That, for 90% of all wallets that will exist, will be overkill.
<r​brunner7> Maybe we should check whether we can safely defer that question into the future, hopefully by showing that the changes will be pretty local for that switch, and implement more fundamental things first?
<r​brunner7> I mean, still tremendous insecurity about the wallet "API", as an example.
<r​brunner7> I.e. how will the Seraphis wallet present itself to wallet app devs?
<r​brunner7> I would rather like to put some efforts in there, and leave that "LMDB wallet cache" question be for the time.
<r​brunner7> Ah, I completely overlooked this: https://github.com/seraphis-migration/wallet3/issues/4
<j​effro256> jberman: could a solution to the polyseed problem be that the generator code checks beforehand if the language is ambiguous and tries again if it is ? The probability of getting the same ambiguous language for each word in the seed is incredibly small, yeah? If its small, it shouldn't reduce entropy very much
<r​brunner7> When I wrote that issue, I was under the impression that the Seraphis library does, and the wallet will, access enotes and collections of enotes all over the place. If *all* of that should get forced to become method calls somehow so that we can go into a LMDB file, I think that has the potential to become quite complicated and tedious.
<r​brunner7> I mean, you wouldn't have all the enotes in RAM at the same time anymore, right?
<r​brunner7> Maybe we could restrict special things, like your mentioned " find-received/assist-filter ", to a LMDB file?
<j​effro256> Depends on the OS's caching, but LMDB was designed with file caching in mind and does a pretty good job at it
<r​brunner7> I don't worry about speed, mostly, but on a pretty tedious programming style that you could get forced into.
<j​effro256> But now we would have 2 enote stores, doing the same thing, but one's just as complicated as the thing we were trying to avoid
<j​effro256> A good real world example would be to look at `monerod`. Monerod does a ton of random reads on at least 100x more data than we'd be doing, and the caching is good enough that it isn't ground to a halt every time we need to validate a tx
<r​brunner7> Yeah, but aren't the "patterns of access" to enotes in the Seraphis wallet and library about 10 times more diverse and numerous?
<r​brunner7> Again, I don't worry about speed here, mostly.
<r​brunner7> Basically: Are devs happy if you take away trivial std::vector with foreach and index access and force *everything* through method calls?
<r​brunner7> Not sure I manage to bring my worries accross sucessfully ...
<r​brunner7> Or you will just overload the operators to prevent that?
<j​effro256> No I get what you're saying. `BlockchainLMDB` already has generalized for-each-like APIs for different things so that shouldn't be too hard IMO
<j​effro256> LMDB makes it easy to do for-each loops. You could then just use a callback in enote store and then you can write simple processors without having to worry about how the data is stored
<j​effro256> Even if we store things in RAM, that's honestly a cleaner design that handing over a vector (which might later be a list or deque, etc)
<r​brunner7> Anyway, if you look deeper into this up to a state where we can make a good informed decision, nothing to say against that IMHO. I was just hoping that somebody would try to "architect" the structure of the whole wallet, deciding the classes, the API, and other rather important things first ...
<r​brunner7> With you as currently the prime candidate for that "somoebody" :)
<j​effro256> I bring it up now because dangerousfreedom is currently working on it and I wanted to put my opinion in before he puts more work into it
<r​brunner7> Yes. Maybe I am mistaken, but I had the impression that serializing in the "conventional way" should not be too much work, and should not result on too much code. So even if we go down the LMDB route, not too much is lost. And we can get a wallet prototype running soon, even if only a very preliminary one of course.
<r​brunner7> That's only me, but I see possibly wasting some time here as a much smaller problem than not having a clue yet how the whole wallet will look ...
<j​effro256> Fair enough
<r​brunner7> SNeedlewoods: Any comments? Maybe you can still see things more from the outside, and give some valuable opinion how our discussion sounds?
<t​obtoht> Does LMDB support transparent data encryption or will cache contents no longer be encrypted?
<r​brunner7> I dimly remember some info from @hyc that he would have something ready if needed, but don't ask me about details.
<r​brunner7> Regarding encryption
<t​obtoht> Thanks
<s​needlewoods_xmr> unfortunately I can't really contribute to the discussion, because my understanding isn't broad enough
<r​brunner7> Alright
<r​brunner7> Anyway, often such decisions of general development direction are the hardest to take
<r​brunner7> I have seen cases in my dayjob where we really had to start to implement and just see how it went to get things to clear
<r​brunner7> Anything else for today's meeting?
<s​needlewoods_xmr> a general question about std::map, in https://github.com/seraphis-migration/monero/blob/seraphis_wallet/src/seraphis_mocks/mock_ledger_context.cpp#L457 (a map with a rather complicated structure https://github.com/seraphis-migration/monero/blob/seraphis_wallet/src/seraphis_mocks/mock_ledger_context.h#L323) what happens to the map in that line `m_blocks_of_legacy_tx_output_contents<clipped 
<s​needlewoods_xmr> [new_index];`? Will it just add the new_index with an empty (inner) map?
<r​brunner7> That definition looks pretty wild
<j​effro256> If the key doesn't already exist, then the map will create an empty map as the value. If it already exists, it does nothing
<s​needlewoods_xmr> and iirc somewhere I read that devs at this stage should leave mock code behind and instead implement production code
<s​needlewoods_xmr> but currently almost all rabbit holes I go down end in mocks
<r​brunner7> Well, as long as there is no real blockchain access there, everything has to go through that "mock ledger", right?
<j​effro256> https://en.cppreference.com/w/cpp/container/map/operator_at
<s​needlewoods_xmr> thanks jeffro
<s​needlewoods_xmr> I thought maybe there is already a place for legacy blockchain scanning!?
<r​brunner7> Yeah, jberman is working on that, but did not yet realase something merge-able
<s​needlewoods_xmr> okay, will have to wait on his input then ... in the meantime I will try to expand the documentation I started
<r​brunner7> Alright, the hour is full, so let's close this first meeting in 2024. Many more to come, read you again next week! Thanks everybody for attending.
<s​needlewoods_xmr> thanks rbrunner7 , cu all
<j​effro256> Thanks everyone
````


# Action History
- Created by: rbrunner7 | 2023-12-29T20:33:02+00:00
- Closed at: 2024-01-01T19:05:12+00:00
