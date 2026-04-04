---
title: 'Seraphis wallet workgroup meeting #57 - Monday, 2024-02-12, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/967
author: rbrunner7
assignees: []
labels: []
created_at: '2024-02-09T18:57:55+00:00'
updated_at: '2024-02-12T19:06:28+00:00'
type: issue
status: closed
closed_at: '2024-02-12T19:06:28+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/964

# Discussion History
## rbrunner7 | 2024-02-12T19:06:28+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/967
<j​effro256> Howdy
<s​needlewoods_xmr> hello
<d​angerousfreedom> Hello
<r​brunner7> Alright, any reports from last week?
<j​effro256> I started working on the new transaction variant. If any of y'all wanted some clarification on my proposed design, I'd like to answer questions
<s​needlewoods_xmr> from me nothing noteworthy
<g​hostway> Hi, nothing from me. If anyone needs something I'd love to help, but will be available after this Sunday
<d​angerousfreedom> Nice! I started looking at the database files. My only experience with databases is using Django for some web applications. I guess the principles are the same for all databases, right? You define the db tables and then you insert the entries, right?
<d​angerousfreedom> I think would be nice to draft how you see the integration of this Variant
<j​effro256> Yeah in our LMDB setup, the transactions are serialized into blobs and accessible by a "transaction index" which is a deterministic ordering based on where they appear in the chain. So the DB table where you actually get the blobs from is a map of tx_index -> tx_blob
<j​effro256> When I'm writing the new tx classes, they can deserialize directly from v1 and v2 formats
<d​angerousfreedom> Do you know already what we need to modify in the database for the Seraphis txs?
<j​effro256> So no modifications to the blobs would be necessary, i.e. there's no "conversion" step
<d​angerousfreedom> We dont need to add any fields in the db scheme?
<j​effro256> Honestly, in terms of the actual database LMDB structure, basically nothing, since the LMDB structure is tx-format agnostic. However, we do need to update the generalized interface `BlockchainDB` to include fetching and sending transactions which aren't `cryptonote::transaction`
<d​angerousfreedom> I see. Nice! Seems much better than I thought then
<r​brunner7> With Seraphis, is there still a single enormous list of transactions, i.e. they don't form 2 pools, coinbase and others?
<j​effro256> What do you mean by "form 2 pools"?
<r​brunner7> I think some designs to avoid coinbase transactions in normal rings for our *current* setup would need two such separate pools.
<r​brunner7> Some thoughts like that were done when it looked as if p2pool transactions would overrun everything ...
<j​effro256> Ohhhh... yeah a wrote a PR that let wallet2 do non-coinbase or coinbase-only decoy selections. The difference I made to the database was that there was two cumulative RingCT output numbers stored per block instead of one. If you picked an output between these two numbers it was a coinbase output, otherwise it was a non-coinbase. So it didn't need a change to the way that transacti<clipped mess
<j​effro256> ons were stored, just the cumulative RingCT dist info
<r​brunner7> But it does not look like this will actually go into production with the next pre-Seraphis hardfork, right? And with the much larger rings the subject is probably pretty much off the table anyway.
<j​effro256> Probably not, it didn't get much traction
<r​brunner7> Ok
<r​ucknium> FWIW, I support implementing the change in the next hard fork.
<r​brunner7> I have a question about your new transaction class. It's a detail, but I wonder.
<r​brunner7> That `CryptonoteTxV2` that's a *new* class, right? A redesign of `cryptonote::transaction` with unnecessary and duplicated fields eliminated.
<j​effro256> Yes
<r​brunner7> So its binary serialization will of course also differ considerably from how that old class now serializes.
<j​effro256> No its binary serialization will be the exact same
<r​brunner7> Ah, ok, that's the point that I did not get.
<j​effro256> For example, a v2 transaction does not serialize the `signatures` field, so I don't have to store it, but I get to keep backwards-compatibility with the old format
<r​brunner7> Wouldn't smaller binary blobs result that would read a bit faster if you introduced a new store format, with its own version number, and use the version numbers 2 only for *reading* the old format?
<j​effro256> Depends if you can actually serialize the same information with fewer bytes. But I don't see the point in creating a new format if we're not going to hardfork it in before Seraphis
<d​angerousfreedom> @jeffro: Do you think you could create a unit_test using a DB object storing/reading all the different transactions when you create this variant?
<j​effro256> Yes, of course. I will definitely test that it correctly reads existing v1/v2 tx format AND serializes to the same blob
<r​brunner7> Ok, yes, that's a solid advantage if you could run our new software in parallel to the old one. Good argument.
<d​angerousfreedom> Great! Then it should be easy to apply to a local testnet, right?
<j​effro256> Yes, the end goal will be to hopefully use the new tx variant directly from existing LMDB instances
<r​brunner7> If you can get your new class defined, implemented, and serializing and deserializing correctly, basically as I see it only one question is left: Will it be realistic to adjust the whole codebase to it, from a point of view of effort needed? Do you have already any gut feelings or even educated guesses there?
<j​effro256> Trying to make a testnet eventually
<r​brunner7> I worry a bit, frankly, but maybe that's our fate to go through with that
<j​effro256> We will already have to adjust everything if we stuff that info into `cryptonote::transaction` because now we have to handle the possibility of Seraphis fields inside the transaction. However, now we explicitly handle it instead of possibly missing it
<r​brunner7> Merging in substantial changes from master could probably become quite a chore after we switched and changed e.g. each and every access to some `cryptonote::transaction` class field
<j​effro256> Also, we can create a method which converts `CryptonoteTxV1/2` into `cryptonote::transaction` to verify that to save typing
<r​brunner7> "to save typing" I don't understand. Can you elaborate?
<j​effro256> Yes, with new PR #9135, all we have to do in terms of tx verification to make it functional is move `Blockchain::check_tx_inputs()` into a function and then basically everything else is business logic
<j​effro256> What I meant by "saving typing" is reducing trivial review work and code changes
<r​brunner7> I still don't get what you mean, but never mind, I think if you can present the design of the new class things should become clear.
<j​effro256> What I'm saying is that we will have to do a ton of re-writing anyways to support new transactions anyways. Basically everywhere we handle transactions, we would have to specify version rules and tx semantics rules, etc. With the new tx variant, we would have to update more function declarations etc, but the most difficult and meaningful review work will largely be the same
<r​brunner7> E.g. getting the id of a tx must be one of the most frequent operations. How will that look with the new variant class? A function call instead of a field access and thus a trivial change?
<s​needlewoods_xmr> just out of curiosity, will monero-project/monero in any time get merged into UKoeHB/monero or seraphis-migration/monero?
<s​needlewoods_xmr> I imagine if the repos only get 'synced' when seraphis is ready to get merged into monero-project/monero, that could lead to many git conflicts?
<j​effro256> Well you're technically not supposed to access that field directly anyways, because sometimes it might not be set, so the codebase was using a function anyways
<j​effro256> But I was wanted to create a cache wrapper around the tx variant once things really got started
<r​brunner7> It's already a function call? Maybe I did not code too long already :)
<j​effro256> SNeedlewoods: Ukoe just merged master back into seraphis_lib last week
<r​brunner7> Is that merge through now? Could I try to merge that result into our repository already?
<s​needlewoods_xmr> ah thanks, I didn't notice
<j​effro256> There's still an issue with IIRC android builds that keeps it from compiling
<r​brunner7> Alright. Any prediction whether that merge will run into special difficulties?
<r​brunner7> So I know what I might have to face ...
<r​brunner7> git and I are sometimes friends, sometimes not so much :)
<j​effro256> I'm not sure... I started working off of it clean but there's already changes in the seraphis_wallet branch so it might be messier
<r​brunner7> Ok. Please give me a ping when I could start trying, so I can play around with a local repository clone to see.
<r​brunner7> Or maybe playing would be possible already, with only small changes left
<j​effro256> I would wait until the android compile problem is fixed IMO
<r​brunner7> I see, no problem.
<r​brunner7> So, what's the opinion of the room? Do you see anything that still speaks against jeffro256 mooving full steam ahead towards a proof of concept for that class?
<r​brunner7> I myself think that's ok.
<d​angerousfreedom> By all means, please :)
<s​needlewoods_xmr> I'm excited to see the result
<r​brunner7> That in any case. I just hope fellow Monero devs won't swear for years to come about today's decision, in the style of "How could they" :)
<r​brunner7> On the other hand, they swear anyway, no?
<j​effro256> lol right
<d​angerousfreedom> This looks the best way. I dont see better alternative either. And not a better person too :p
<j​effro256> aw thanks :)
<r​brunner7> We will see probably later whether any work can shared here. Maybe adjusting parts of the codebase could be done by other people helping jeffro256 .
<d​angerousfreedom> Yeah, I'm interested in learning. I will definitely review his code as soon as he has something.
<s​needlewoods_xmr> just as a disclaimer, I'll be pretty busy until mid/end of March, but if anyone wants to review https://github.com/seraphis-migration/monero/pull/16 I try my best to quickly respond (before I forget everything)
<r​brunner7> So, anything else still do discuss for today?
<d​angerousfreedom> I will continue working on the opening of wallet3. I believe I made some progress with the keys handling but there are a lot of things to discuss there. I'm trying to document everything. I will make an issue with the design decisions that I made. The plan is to integrate the EnoteStore next (have it serialized, used for mock transactions and create some necessary functions for th<clipped 
<d​angerousfreedom> at). General advises are very welcome. I believe it is better to write a lot of documentation and agree on things now than to go just coding a lot of things. I will also have time again to participate Wednesdays on the MRL meetings :p
<j​effro256> Thanks for working on that sneedlewoods
<r​brunner7> dangerousfreedom: Please do share early. Will try my best to look at anything and comment
<j​effro256> Also I'm excited to see what you get done with wallet initialization dangerousfreedom
<d​angerousfreedom> Ok. Thanks.
<j​effro256> That documentation is on the seraphis migration wiki right ?
<r​brunner7> Would probably be a good place, in any case. SNeedlewoods also put their additions there.
<d​angerousfreedom> Yeah, here: https://github.com/seraphis-migration/strategy/wiki/Seraphis-Documentation
<r​brunner7> Ah, something already there. Even better.
<d​angerousfreedom> Dont know if it is the best place since anyone can modify and delete everything apparently :p
<r​brunner7> Well, it's a git repository, restore should be reasonably simple. And can somebody not member of the org change?
<r​brunner7> Maybe have to check.
<d​angerousfreedom> Oh okay, there are revisions :p
<r​brunner7> Alright, the hour is full, and by gosh we don't want to hold jeffro up from coding. Thanks for attending everybody, read you again next week.
<j​effro256> Thanks everyone!
<s​needlewoods_xmr> thank you all
````


# Action History
- Created by: rbrunner7 | 2024-02-09T18:57:55+00:00
- Closed at: 2024-02-12T19:06:28+00:00
