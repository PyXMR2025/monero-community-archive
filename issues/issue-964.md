---
title: 'Seraphis wallet workgroup meeting #56 - Monday, 2024-02-05, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/964
author: rbrunner7
assignees: []
labels: []
created_at: '2024-02-02T16:36:04+00:00'
updated_at: '2024-02-05T18:44:27+00:00'
type: issue
status: closed
closed_at: '2024-02-05T18:44:27+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/960

# Discussion History
## rbrunner7 | 2024-02-05T18:44:27+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/964
<d​angerousfreedom> Hello
<s​needlewoods_xmr> hey
<r​brunner7> We had a full week of "quiet" in our room. But now the let's start with the reports :)
<d​angerousfreedom> This week, I continued working on the opening of the wallet. I have a working prototype that do the following: load wallet keys (either seraphis or legacy) or create a new wallet, convert to seraphis if necessary, show the wallet-tier (Master, ViewAll, ViewReceived, FindReceived, AddrGen), save and quit wallet. I have also started using the mock transactions to play with enotes using 
<d​angerousfreedom> ithe same wallet. Though the ability to read/store things on a database (blockchain) is missing. Before the end of the week, I will document everything I did so far and post a demonstrator here showing how this prototype is working. I will also ask for your advices to know how we can proceed.
<s​needlewoods_xmr> +1
<r​brunner7> dangerousfreedom: Sounds good. Does this include serialization of the enote store? I lost a bit track how far along that piece is.
<d​angerousfreedom> I did not really start playing with enotes yet. Just the Key Container.
<d​angerousfreedom> So, I'm just storing the wallet keys file
<s​needlewoods_xmr> sadly I didn't achieve much, was too busy with rl stuff
<s​needlewoods_xmr> just from a quick look at the seraphis tests, it looks like we only use `tx_extra_additional_pub_key` there and no `tx_extra_pub_key"
<r​brunner7> I see. Did we say that you will probably implement that serialization?
<d​angerousfreedom> The cache file (with the Enote Store) will be done next
<r​brunner7> Splendid!
<r​brunner7> SNeedlewoods: Yeah, real life happens :)
<d​angerousfreedom> rbrunner7: I think the serialization of the Enote Store is basically done or has very few things to do
<d​angerousfreedom> I will look into that next
<r​brunner7> Ok
<d​angerousfreedom> I'm focusing on the Key Container now
<d​angerousfreedom> I believe if we (I) spend the next weeks focusing on properly opening the wallet with the keys management then it will be already something.
<s​needlewoods_xmr> if anyone can give input on `tx_extra`, that would be appreciated, otherwise will try to figure out more from reading the code
<r​brunner7> You mean how that works with Seraphis?
<d​angerousfreedom> Sorry, I didnt get your question SNeedlewoods , what is that?
<r​brunner7> I would be surprised if already somebody looked at that closely. Why do you mention `tx_extra`, out of all things?
<s​needlewoods_xmr> yes, why do the tests only use `tx_extra_additional_pub_keys`?
<s​needlewoods_xmr> https://github.com/UkoeHB/monero/issues/27
<r​brunner7> I would guess that's only pre-Seraphis?
<s​needlewoods_xmr> I was trying to get into thiis issue
<r​brunner7> That ugly hack to store regular, bog-standard tx parts in `tx_extra`
<r​brunner7> Maybe because of some hardfork "politics" or time conflicts
<s​needlewoods_xmr> I ran `./unit_tests --gtest_filter="seraphis*"` and set a breakpoint here https://github.com/UkoeHB/monero/blob/bcae39d2624ecec946f5875e6323ec5a6ba8b115/src/seraphis_core/legacy_core_utils.cpp#L389 but it never hit that point
<r​brunner7> Did you make sure that subaddresses are involved?
<r​brunner7> Maybe a dumb question ...
<s​needlewoods_xmr> some tests involve subaddresses, pretty sure
<r​brunner7> Then I am already out :)
<d​angerousfreedom> Oh I didnt look into that. But that is surely necessary for the enote_scanner to work.
<d​angerousfreedom> I dont know how to answer now. I would have to get into the code too. If you struggle this week, I can try to look next week.
<d​angerousfreedom> You want to identify the cases where it is failing?
<d​angerousfreedom> when*
<s​needlewoods_xmr> I'll look deeper into it and notify you here if I'm still having problems
<dangerousfreedom> +1
<d​angerousfreedom> You will find out :)
<r​brunner7> Alright. More things to discuss today?
<d​angerousfreedom> Not from me
<d​angerousfreedom> Oh maybe one thing
<d​angerousfreedom> The only-view wallet in legacy has no convertion to seraphis, right?
<d​angerousfreedom> If someone has a view-only wallet, he cant do anything with it when seraphis only protocol is enabled, right? That was my understanding from reading the jamtis spec
<r​brunner7> Sorry, no idea. Maybe it's not possible to derive some keys then, without the spend key and only the view key?
<r​brunner7> Is the case mentioned in the spec?
<d​angerousfreedom> I didnt find.
<r​brunner7> But you derived it from the way the keys are calculated?
<d​angerousfreedom> We can only derive a seraphis wallet from the private spend-key
<d​angerousfreedom> Yes
<r​brunner7> That's .... surprising, in a way.
<d​angerousfreedom> According to the spec I hope
<r​brunner7> Or maybe not. Why should it be possible to derive further Jamtis keys from a pre-Jamtis view key?
<r​brunner7> So a view-only wallet capable to scan the whole blockchain would need *two* "view keys"?
<d​angerousfreedom> Yes, I think it should be like it is. Just wanted to confirm
<d​angerousfreedom> In seraphis you only need the view_balance key
<d​angerousfreedom> Which is not the same as the legacy view_only
<r​brunner7> Well, my gut feeling is a quite weak confirmation
<r​brunner7> Yes, but I guess you can't scan pre-Seraphis tx with that Jamtis view_balance key? Hence the need for a wallet with two view-style keys?
<d​angerousfreedom> Yes
<d​angerousfreedom> If you have legacy enotes, you need legacy keys
<d​angerousfreedom> But you can have a seraphis wallet (seraphis enotes) with legacy keys
<r​brunner7> Ok. So no automatism, but with proper tools it would be possible to add the Jamtis view_balance key to the legacy view key to get a fully working view-only wallet
<r​brunner7> To an already *existing* view-only wallet I mean
<UkoeHB> The library is designed to be correct but I did not unit test every single possible code path, especially for legacy stuff.
<d​angerousfreedom> I think it will be impossible to get the correct amounts if you have a seraphis_wallet derived from a legacy wallet
<r​brunner7> Unless you add the view_balance key I would guess
<d​angerousfreedom> That would not work for your previous legacy enotes
<r​brunner7> Er, yes, of course, that's why I say everything works out as soon as the wallet gets hold of *both* view-style keys, old and new :)
<r​brunner7> And whether you can add the Jamtis view_balance key after migrating the wallet is merely a question of wallet functionality and commands
<d​angerousfreedom> Yes, okay, from the moment it is not possible anymore to make legacy transactions then having both keys should be enough, right
<r​brunner7> *wallet app functionaliy
<r​brunner7> Ok, so that's one of the many things to keep in mind for new wallet apps and questions of migrating
<r​brunner7> Interesting
<r​brunner7> Anything else?
<r​brunner7> So let's close this meeting, thanks everybody for attending, read you next week!
<d​angerousfreedom> Thank you rbrunner7
<s​needlewoods_xmr> thank you, bye
````


# Action History
- Created by: rbrunner7 | 2024-02-02T16:36:04+00:00
- Closed at: 2024-02-05T18:44:27+00:00
