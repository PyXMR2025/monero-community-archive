---
title: 'Seraphis wallet workgroup meeting #6 - Monday, 2022-12-19, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/770
author: rbrunner7
assignees: []
labels: []
created_at: '2022-12-16T16:05:35+00:00'
updated_at: '2024-04-02T17:48:14+00:00'
type: issue
status: closed
closed_at: '2023-01-16T17:28:51+00:00'
---

# Original Description
On Monday, November 14, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: #765

I propose we review quickly where we stand now with Jamtis addresses, and look at the feedback received on Reddit.

Second, I think we should try to get an overview where we currently stand with the question of accounts. I hope I have time on Sunday to go through the various proposals how to handle them and have a list ready for the meeting.

# Discussion History
## rbrunner7 | 2022-12-18T19:34:37+00:00
I went through the discussions about accounts and their implementation, to get an overview of the approaches, and will deposit them here in preparation of the meeting.

@j-berman listed 3 principal approaches that came up [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4379590#gistcomment-4379590), with pro's and con's. @Tevador added later a 4th approach [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4381276#gistcomment-4381276).

1. Sub-divide the 16-byte address index in some "recommended" way
2. Let wallets manage a local list of addresses to accounts assignments
3. Add bytes to the address with the account index, at least 2 bytes, better 4
4. Encode a 4-byte account index in the output public key

2 bytes give 65536 accounts, 4 bytes a bit more that 4 billion accounts.

Approaches 1 and 2 would mean that accounts to not feature in the core protocol and "appear" only at least 1 level higher. Approaches 3 and 4 would bake accounts in the core protocol.

For 1, Tevador argued [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4384179#gistcomment-4384179) that a 4 bytes + 12 bytes split of the 16-byte address index could make sense. For 2, I brainstormed [here](https://github.com/seraphis-migration/wallet3/issues/21) how wallets could give users almost limitless freedom how to assign addresses to accounts.

## rbrunner7 | 2022-12-19T19:21:24+00:00
````
<rbrunner7[m]1> Meeting time. Hello! Who is around?
<one-horse-wagon[> Hello.
<Stnby[m]> Hey
<dangerousfreedom> Hi
<JoshBabb[m]1> Hello
<plowsof11> hi
<UkoeHB> hi
<tevador> hi
<jberman[m]> hello
<Rucknium[m]> Hi
<rbrunner7[m]1> First I want to give an overview about what happened regarding addresses in the meantime. I reported a bit in the last MRL meeting, but I can give some more details here.
<rbrunner7[m]1> I made the Reddit post that we agreed upon in the last meeting, it's here: https://old.reddit.com/r/Monero/comments/zl4615/why_seraphis_jamtis_addresses_will_be_so_awfully/
<rbrunner7[m]1> It collected 129 comments, which is not bad.
<rbrunner7[m]1> I would say comments overall were not too controversial.
<rbrunner7[m]1> I don't think there was anybody who outright attacked somehow, along the lines "200 characters? Are you crazy"?
<rbrunner7[m]1> The discussion shifted then somewhat, with about 2 other posts from other people
<rbrunner7[m]1> about the fact of hardforking itself, not merely changing addresses.
<rbrunner7[m]1> It seems for some people not yet into Monero for a long time it was news that there are regular hardforks
<rbrunner7[m]1> and hardforks that do need software adjustements.
<rbrunner7[m]1> I think the post also was the first time for a number of people that they heard in detail about Jamtis and Seraphis.
<rbrunner7[m]1> I learned that Lightning Network invoices are also very long, 190 characters upwards
<rbrunner7[m]1> which seemingly works. They also use Base32 for those, by the way.
<Rucknium[m]> IMHO, the hard work of summarizing the proposed changes for the community paid off. Good job!
<rbrunner7[m]1> Thanks. Yeah, I think overall it was a success, and I don't think we are in immediate need of a course correction from this regarding addresses especially.
<jberman[m]> +1, good post :)
<rbrunner7[m]1> So we have some ongoing and interesting work from tevador with the polynomials, fascinating stuff: https://gist.github.com/tevador/5b3fbbd0877a3412ede07263c6b2663d
<rbrunner7[m]1> For the address checksum algorithm
<rbrunner7[m]1> It seems to converge somehow towards that thing with the funny name of "U1PIRGA7"?
<tevador> my recent checksum work is summarized here: https://github.com/seraphis-migration/wallet3/issues/37
<tevador> U1PIRGA7 is the base32hex encoding of the best polynomial I found
<rbrunner7[m]1> Do you have further investigations planned, tevador, or is your search more or less complete now?
<tevador> my search is basically complete, but if someone wants to keep searching, I published all my tools
<rbrunner7[m]1> Ok, so maybe we can all agree "tentatively" on that polynomial, with the condition of course to switch should something surprising surface?
<ghostway[m]> tevador: Cool stuff. Did you search for M or did you deem it irrelevant?
<tevador> the performance of the generator I found is quite surprising, I didn't expect to find anything that can detect 5 errors at ~200 characters, os it's possible there is not much imporovement to be made
<tevador> ghostway[m]: see https://github.com/seraphis-migration/wallet3/issues/37#issuecomment-1356785119
<Rucknium[m]> If a wallet implementer makes a mistake in the checksum implementation, could a someone using that wallet lose funds by sending XMR to a "wrong" address (both sender and receiver using the faulty implementation)? Or would nodes reject those txs? 
<ghostway[m]> tevador: That's very very cool. Thanks
<rbrunner7[m]1> Well, seems to me if really only the checksum is wrong, and nobody notices, nothing bad should happen from that alone ...
<tevador> Rucknium[m]: a faulty address becomes basically a burn address
<Rucknium[m]> ok
<plowsof11> ::worried::
<tevador> if it's a valid public key that has an unknown private key
<rbrunner7[m]1> By the way, @hyc proposed Base64 as the alphabet, but as I followed the discussion of that, Base64 seems to have some drawbacks, and in any case does not lead to a breakthrough reduction in length either.
<tevador> btw the cyclic code I found works all the way to 994 characters, so it may be usable for other things such as invoices
<ghostway[m]> +1
<rbrunner7[m]1> On Reddit only very few people seemed to question the choice of the alphabet
<rbrunner7[m]1> As far as I can see right now, we don't have real questions open regarding addresses, except if we choose one the solutions for accounts that have an influence on the address.
<rbrunner7[m]1> Anybody with any further comments or questions regarding addresses?
<rbrunner7[m]1> Did the Bitcoin people simply miss this polynomial, or are the conditions slightly different?
<tevador> bitcoin uses a 6-character checksum, which is a bit weaker, but more suitable for short addresses
<rbrunner7[m]1> Interesting.
<tevador> their polynomial is "TMKLTI" and they admitted that they later found other ones that perform better
<rbrunner7[m]1> Alright, maybe we can move on to the second suject that I proposed for today, accounts.
<rbrunner7[m]1> I tried to detail here what proposal for those are currently on the table: https://github.com/monero-project/meta/issues/770#issuecomment-1356860764
<rbrunner7[m]1> I still find it a bit surprising how many discussions and how many ideas the subject of accounts has provoked
<rbrunner7[m]1> Given that while accounts certainly are useful, and people want to keep them, they are certainly not the most often used feature of Monero
<rbrunner7[m]1> And of course not all wallets by far support them
<tevador> The main question is if we want to bake accounts into the protocol.
<rbrunner7[m]1> Anyway, seems to me we are a bit stuck, with different people camping for the one of the 4 approaches, and I wonder what's a good idea to proceed and finally arrive at a decision within a reasonable timeframe.
<UkoeHB> I vote hard no
<rbrunner7[m]1> Exactly :)
<tevador> If not, then option 1 is best, otherwise option 4.
<plowsof11> accounts are an illusion for wallets to implement on the front end 
<rbrunner7[m]1> I something won if we agree that #4, "Add bytes to the address with the account index, at least 2 bytes, better 4" is more or less out of the race now?
<jberman[m]> yes 4 was definitely superior to 3. I didn't realize it was an option
<rbrunner7[m]1> Sorry, that's of course number 3, not number 4
<ghostway[m]> I'd definitely vote for 4. If I have a say in that
<tevador> I think there have been some compelling arguments to support at least 4 bytes for the account index.
<ghostway[m]> All the others just don't make much sense
<sneurlax[m]> as in, "4. Encode a 4-byte account index in the output public key", or "3. 
<sneurlax[m]> Add bytes to the address with the account index, at least 2 bytes, better 4"?
<UkoeHB> Everything I have learned after studying, designing, and implementing cryptocurrency protocols over the past 4 years tells me this kind of design change is the wrong direction.
<jberman[m]> (clarification: I didn't realize 4 was an option when I proposed 3)
<rbrunner7[m]1> I really meant 3, making the address longer still, with even 4 more bytes, that's why I thought we can at least forget that :)
<rbrunner7[m]1> I think the arguments are pretty much on the table, and the way the various involved people value / judge them, and as I said we are a bit stuck. I wonder what are possible reasonable ways to break out of that.
<rbrunner7[m]1> I don't think we can actually try out something?
<rbrunner7[m]1> Or program some simulations?
<rbrunner7[m]1> This seems to play on the field of arguments, of logic, of design, right?
<Rucknium[m]> If accounts are not part of the protocol, would we more likely see issues similar to the HD wallet derivation path issues of most other coins?
<rbrunner7[m]1> You mean multiple imcompatible systems?
<Rucknium[m]> "Wallet A handles accounts by method alpha. Wallet B does it by method beta. What happens when seed phrases are ported from Wallet A to Wallet B?"
<rbrunner7[m]1> I think nothing goes fundamentally wrong, just the accounts might not turn out the way you want it.
<rbrunner7[m]1> after restore
<plowsof11> it would be the same as refreshing a wallet with a new wallet cache no? (recipient addresses lost.. labels etc and if 2 is chosen: 'accounts' lost)
<rbrunner7[m]1> But it's about trade-offs: You can look at it and judge that this problem is to "be accepted" because a solution would be too expensive / complicated / against design principles
<rbrunner7[m]1> I think that's part of our current block: You can look at it at quite different ways
<rbrunner7[m]1> and give different weights to different aspects and arguments
<tevador> For options 4, wallets that don't support it will fail to detect payments to accounts other than the default one. So that's slightly worse than just mislabeled funds.
<rbrunner7[m]1> Nothing is really so convincing so far that it sways almost all people a certain way, as I see it
<rbrunner7[m]1> Yes, option 4 needs support for accounts at least at the lowest level of detecting enotes, even if the UI wants having nothing to do with accounts
<rbrunner7[m]1> Which is a bit unfortunate.
<rbrunner7[m]1> This plus the added complexity. And maybe some rigidity.
<rbrunner7[m]1> That's why personally I am a bit puzzled about the support for 4, but again, people and their opinions :)
<rbrunner7[m]1> And as I said, the quite big engagement that some quite "niche" theme is able to provoke.
<rbrunner7[m]1> Or am I wrong? Do we have some people here who think that accounts are very important?
<rbrunner7[m]1> (emphasis on "very", obviously)
<plowsof11> i assume those that want to have "coin control" to mitigate things
<jberman[m]> Option 4's advantages over option 1 are 1) maintains 16 bytes for the address index for robust random address generation, and 2) the user does not need to be presented with a choice on how they want their wallet to handle accounts at any stage
<Rucknium[m]> Accounts may look niche to consumers, but maybe not to merchants. You need both for an economy. (I'm not sure if protocol-level implementation is the right choice. Just saying that a small group of users can have large effect.)
<rbrunner7[m]1> Right. I have however a hunch that we may have surprises lurking that may disturb this pretty and blameless scenario.
<rbrunner7[m]1> If address generators start to play a big role
<rbrunner7[m]1> Because then somebody else can make addresses for you, with any account index they like.
<tevador> ^ That is not possible the way option 4 was proposed.
<tevador> Unless they know a private key.
<rbrunner7[m]1> Yes, and that's an important angle of this, seems that merchants and "normal" users have quite differing wishes
<rbrunner7[m]1> Yes, that "address generation key", right?
<rbrunner7[m]1> Or does option 4 kill that key?
<tevador> That is still true with option 4.
<tevador> Merchants complained about the inability to generate subaddresses without the view key. This problem is not present in jamtis.
<rbrunner7[m]1> Ok. So any good idea how to break out of our little accounts deadlock? Just wait longer seems not very clever. Giving UkoeHB some sort of veto power might not find enough support. Discussing further? Again asking the broader public, together with a good overview over the aspects of the question?
<rbrunner7[m]1> Of course we can't force something. If no good idea, we have to wait.
<rbrunner7[m]1> and see :)
<rbrunner7[m]1> Voting is also not unproblematic, surly ...
<jberman[m]> I'm not a hard yes on baking accounts into the protocol. I understand UkoeHB 's "minimize the protocol" approach. The likelihood of a future hard fork to modify the feature would probably go up, and the choice to keep it out of the protocol I think would reduce that probability
<jberman[m]> I also think it's reasonable not to bake something into the protocol that does not have strong consensus
<jberman[m]> I would be ok with moving away from option 4 so long as a hard no stands
<rbrunner7[m]1> "I also think it's reasonable not to bake something into the protocol that does not have strong consensus" That sounds quite reasonable as a general approach, no?
<one-horse-wagon[> I've been a business man all of my life.  Maybe somebody could explain to me why all of my customers should have  "separate bank accounts" for each one of them?
<rbrunner7[m]1> Because they like that, and the customer is king :)
<rbrunner7[m]1> No, seriously, it might be a bit "nice to have", but it seems it useful, and people do want to keep
<rbrunner7[m]1> that much we know from feedback, I am pretty sure
<plowsof11> humans like to compartmentalise things 
<Rucknium[m]> Maybe we can look at the XMR payment processors that exist now and see how they use (or don't use) accounts. And ask exchanges. Exchanges probably don't open source their code, so we cannot inspect it.
<rbrunner7[m]1> Just for the record, I side pretty strongly with UkoeHB in this question.
<tevador> I think the default solution should probably be not to include accounts in the protocol and have wallets handle it unless there is a strong reason to include it.
<rbrunner7[m]1> I think accounts are simply not important enough to make an already quite elaborate system more complex sitll.
<one-horse-wagon[> I have to vote with Koe on this one.  It would complicate things in major ways from an accounting point of view.
<gingeropolous> the KISS philosophy (and what i understand of unix philosophy) would be to not have accounts baked in
<one-horse-wagon[> +1
<rbrunner7[m]1> Rucknium: I think exchanges and merchants are catered already, whatever we do. They have 16 index bytes to play with in any way they want.
<dangerousfreedom> Personally I never used accounts. Subaddresses are enough for me. So I cant argue much in favor of accounts or give a strong opinion how we should implement them.
<rbrunner7[m]1> And nobody can stop them to do certain things with those 16 bytes, even if we bake accounts otherwise deeply into the protocol.
<ghostway[m]> Sure, but why would we? What are the pros? I don't see many...
<one-horse-wagon[> rbrunner7[m]1: Then any complication becomes theirs, and not Monero's.
<gingeropolous> i don't think its within scope to manage peoples money. monero is money.
<ghostway[m]> +1
<gingeropolous> as long as cleartext payment IDs are dead :)
<ghostway[m]> Imo accounts are nice as a feature that you can manage many addresses from a seed. But that's it, a wallet feature
<rbrunner7[m]1> So ... do we surprisingly have something that already approaches a loose consensus? I don't see a "strong yes" that accounts must go into the lowest level of the protocol anymore?
<jberman[m]> "do we surprisingly have something that already approaches a loose consensus?" -> I'd say so yes :)
<gingeropolous> ima make a "loose consensus" stamp
<rbrunner7[m]1> Lol. Splendid. I wish a new emoji for that.
<ghostway[m]> You can do that on Element? That's cool 
<rbrunner7[m]1> Ok, after the way this discussion went seems to me we can at least march forward as if accounts are out of the core protocol.
<ghostway[m]> +1
<one-horse-wagon[> +1
<woodser[m]1> <rbrunner7[m]1> "By the way, @hyc proposed Base64..." <- what are the drawbacks of base64, and what’s the difference in length?
<rbrunner7[m]1> Approach 4 would mean exensions in the very Seraphis library, not only the wallet, right=
<rbrunner7[m]1> I think the argument of selection by double-click came up, or the impossibility thereof. And the length merely goes down to 160 or so.
<rbrunner7[m]1> That's why I judged "no length breakthrough"
<rbrunner7[m]1> If you can handle 160, you can also handle 200, was my thought.
<rbrunner7[m]1> (answering woodser)
<ghostway[m]> rbrunner7[m]1: why? its the same address at the end, no?
<rbrunner7[m]1> I think scanning has to do something differently.
<rbrunner7[m]1> And scanning is implemented / covered already in the library, of course. 
<ghostway[m]> oh, I see
<rbrunner7[m]1> Some details from tevador here: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024?permalink_comment_id=4381276#gistcomment-4381276
<rbrunner7[m]1> Alright, seems to me we have a very nice result, and can close with the full hour.
<tevador> btw, the current specs don't contain accounts, option 4 was created in response to popular demand for accounts to be included
<rbrunner7[m]1> By the way, next Monday is second Christmas day, and many people may be away anyway. Are people ok to meet again in two weeks?
<one-horse-wagon[> Let's take a vote now whether to cancel next week.  
<one-horse-wagon[> I vote no.
<rbrunner7[m]1> "no" means "do have a meeting", right?
<one-horse-wagon[> Yes
<rbrunner7[m]1> So I vote yes, cancel
<rbrunner7[m]1> I can hold a meeting, if people like one, that's no problem.
<jberman[m]> I won't be able to make next week
<dangerousfreedom> I have to go but just wanted to share that this week I finished the [first draft](https://github.com/seraphis-migration/wallet3/issues/42) of the minimum theoretical framework for the audit proofs (thank you Koe for your promptness to review it). There is one feature more than the current transaction proofs. Today if someone wants to prove that he has a certain amount (ReserveProof), he would have to give away the key
<dangerousfreedom> image corresponding to the output. I came up with a scheme in Seraphis (a similar idea as UnspentProofs in legacy) that you can do it anonymously for a certain period of time. For example: an exchange can prove that they own a certain balance in February or so, without revealing the key image and therefore without revealing when they spend that amount (which is not possible today). I will look into implementing it in
<dangerousfreedom> the next weeks now.
<dangerousfreedom> I wont make it next Monday either.
<rbrunner7[m]1> Thanks, dangerousfreedom[m] , should have mentioned that earlier ...
<Rucknium[m]> dangerousfreedom[m]: Did you look at MProve+ (I think its name....?)
<rbrunner7[m]1> Ok, maybe we don't schedule an official meeting, but I will be around, and if people want to discuss something, or ask somehting, I am happy to serve.
<one-horse-wagon[> Good enough.
<Rucknium[m]> https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=35
<ghostway[m]> thats very interesting, and useful
<rbrunner7[m]1> Ok, many thanks to all attending, has been a pleasure. See you in the new year at the latest.
<ghostway[m]> * and useful (and makes sense)
<one-horse-wagon[> Merry Christmas and Happy New Year to one and all!
<rbrunner7[m]1> +1
````


# Action History
- Created by: rbrunner7 | 2022-12-16T16:05:35+00:00
- Closed at: 2023-01-16T17:28:51+00:00
