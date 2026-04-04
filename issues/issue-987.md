---
title: 'Seraphis wallet workgroup meeting #65 - Monday, 2024-04-08, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/987
author: rbrunner7
assignees: []
labels: []
created_at: '2024-04-05T14:58:52+00:00'
updated_at: '2024-04-09T04:26:20+00:00'
type: issue
status: closed
closed_at: '2024-04-09T04:26:19+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/985

# Discussion History
## rbrunner7 | 2024-04-09T04:26:19+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/987
<SNeedlewoods> hey
<r​brunner7> Matrix / matrix.org problems persist. Thus please beware.
<o​ne-horse-wagon> Hello
<jberman> hello
<d​angerousfreedom> Nah, that should work for all systems. I messed something that works only for me probably. SNeedlewoods  also tested and worked. I will try a few things here and let you know.
<r​brunner7> Thanks, dangerousfreedom
<d​angerousfreedom> Hi :)
<r​brunner7> Do we also have jeffro256 around? Maybe after some gentle ping :)
<r​brunner7> So what is there to report from the week that passed?
<SNeedlewoods> yes wallet3_transfer_demo2 worked for me on linux mint 21.2
<r​brunner7> I didn't do much, just belatedly trying to compile danger's wallet demo, which seems to have a problem on my system
<SNeedlewoods> fixed all failing tests and feel stupid because it took so long, but I'm glad I solved it on my own lol
<jberman> woot, congrats
<r​brunner7> Nice. Doing it yourself probably has the best learning effect :)
<SNeedlewoods> there is still one TODO left https://github.com/UkoeHB/monero/pull/40/files#diff-26e5d9b89856333eb9c4e55b0c4a24341d7a41528c56d1de4502d5e323f7d38bR103, koe suggested to pipe the tx era, but I don't know from where (only found `TxEraSp`)
<r​brunner7> If hard-earned
<SNeedlewoods> my first idea to just compare current block index with hard-coded block height from RingCT hardfork doesn't work (see linked TODO) and this method would also mess with the tests
<SNeedlewoods> so before I start to introduce even more code I'd like to hear your feedback
<d​angerousfreedom> Nice! What was it? Did you push the updates? I spent half a day last week trying to solve and could not find the problem :p
<jberman> me: async scanner is now ready for review (link: https://github.com/UkoeHB/monero/pull/23), finishing up benchmarks atm
<SNeedlewoods> df you can see in this commit https://github.com/UkoeHB/monero/pull/40/commits/09972fc8516286fbbd07d1e71aad55420bbe2f0a that I unwrapped to `LegacyContextualEnoteRecordV1` where I actually should unwrap to V2
<r​brunner7> I guess that's quite a tough piece of code for review?
<r​brunner7> (that async scanner)
<SNeedlewoods> I "reviewed" the first three commits of the async scanner, will take a while until done
<r​brunner7> SNeedlewoods: And nowhere was anything where the compiler didn't like what you did? Sounds somehow surprising.
<jberman> the first 11 commits are fairly tame. The 12th commit that intros the actual async scanner is probably the most difficult to review
<d​angerousfreedom> From my side, I was trying to figure out what we can do to get as fast as possible to regtest. I guess it would be possible to play with the rpc client/server and add some methods to the lmdb database so we can store blocks with seraphis txs.
<r​brunner7> Can you please quickly explain what exactly you mean with "regtest"? I somehow can't get a handle on this.
<SNeedlewoods> (not seraphis related) I also reviewed https://github.com/monero-project/monero/pull/9151 thanks to rbrunner for the bump it now has 4 reviews
<SNeedlewoods> and did my first PR to monero-project/monero
<r​brunner7> I guess to much of this the answer is "introduce the new transaction class", no?
<r​brunner7> From there much should automatically just work in the daemon, I would suspect
<SNeedlewoods> "And nowhere was anything where the compiler didn't like what you did? Sounds somehow surprising." it's quite possible I missed some warnings
<d​angerousfreedom> Well, I believe we have a basic code to transfer enotes between wallets but I'm using a MockLedger. The idea is to save these txs into the lmdb database (from which I can also get legacy enotes) and play transfer any enote between the wallets.
<d​angerousfreedom> I dont know yet exactly it should be done but I know things could be fairly easily serialized and stored in the db (which I was imagining to be much more difficult).
<d​angerousfreedom> Yes, I believe the best would be to create some kind of transaction class that handles both
<r​brunner7> I think jeffro256 worked already towards that to quite some degree
<d​angerousfreedom> Yes, jeffro256 would do a lot of the hard work :p
<r​brunner7> Alright then :)
<r​brunner7> Decided, next meeting point ...
<d​angerousfreedom> Well, I believe we have a basic code to transfer enotes between wallets but I'm using a MockLedger. The idea is to save these txs into the lmdb database (from which I can also get legacy enotes) and transfer any enote between the wallets.
<d​angerousfreedom> I dont know yet exactly how it should be done but I know things could be fairly easily serialized and stored in the db (which I was imagining to be much more difficult).
<jberman> If I had a vote on this, I'd vote try to shoot for the wallet2 replacement first before Seraphis regtest, but the regtest is work that has to be done eventually too
<jberman> The daemon eventually has to recognize, verify, store, and serve Seraphis txs. Agree a new transaction class would do heavy lifting for that, but not the only piece there
<jberman> I will also add: over the medium term, I'm leaning toward switching personal coding focus to kayabaNerve's proposal for FCMP's
<r​brunner7> Say again how you people arrive at the term "regtest". I think I am missing something trivial.
<r​brunner7> What is "reg" standing for?
<d​angerousfreedom> https://monero.stackexchange.com/questions/13668/what-is-regtest
<r​brunner7> Ah, ok, I see.
<d​angerousfreedom> Basically what jberman is doing by testing the scanner. Mining blocks to a specific wallet in a regtest (local) network.
<jberman> I think what I will try to do over the next week is dig deeper into the task of replacing wallet2 with the Seraphis lib enote store, and reusing the CLI/RPC/wallet API
<jberman> Hopefully I can make headway that makes it clearer how that can be moved forward with by others too while I'm focused on FCMP's
<r​brunner7> If nobody has any pressing general subject to discuss today, I would like to learn about the sentiment, and the plans of the attending people regarding their future engagement in the light of the arrival of FCMP implementation work.
<r​brunner7> jberman already kind of announced, not very surprisingly, that he will lean soon towards that work instead of Seraphis work.
<jberman> I'll still do PR review over here and participate in discussions / meetings
<d​angerousfreedom> I first need to understand it. I would love to do so and to contribute but I cant in the short term. I fully support its development. Luckly everything can be done in parallel.
<r​brunner7> So for you this may develop into some "Odysseus an the sirens" situation? I am convinced that FCMPs can be a very fascinating subject, and the work to bring them to Monero very interesting
<SNeedlewoods> I plan to mainly contribute to seraphis and maybe get more into monero, so far this takes up all my capacities and I don't know much about FCMPs and nothing about rust, therefore no intentions to switch for now
<r​brunner7> Anyway, I myself will probably try to continue with my role as "project manager" here. Somebody has to do it, even if in terms of work hours it's quite modest so far. This might chance if things progress of course, which I hope they will still do.
<r​brunner7> *change
<r​brunner7> Maybe jeffro256 will chime in later with a short statement. I somehow hope that we won't "lose him to FCMPs" ...
<r​brunner7> But of course things are very much in flux. Pretty much nothing ins guaranteed.
<d​angerousfreedom> Anyway, FCMP is just one part of the transaction... we are proposing, with jamtis and seraphis, to change everything. So, of course our work has to be done.
<r​brunner7> For example I wonder how it will turn out if "we" turn the wallet upside down by giving `wallet2.h` a new underpinning, and the FCMP people likewise need larger modifications there.
<d​angerousfreedom> Impossible in the long term
<r​brunner7> Maybe it's too early to have answers here.
<r​brunner7> Yes, in the long term everything coverges into a single wallet code of course. I was thinking about the way there.
<r​brunner7> I guess we will see early enough. Also depends on the speed the two groups will move forward.
<d​angerousfreedom> Yes. I hope the theoretical stuff will be layed down soon so kayaba and jberman wont build FCMP on something dubious
<o​ne-horse-wagon> Are there enough people immediately available to  effectively code FCMP?
<r​brunner7> Well, kayabanerve is a true workhorse. I don't know whether that guy has to sleep at all. Together with jberman you probably have already quite some implementation team.
<r​brunner7> Much is coded already anyway in the core of it, if I understood correctly.
<r​brunner7> This still may take some wind out of our sails here at the Seraphis team, as the saying goes
<r​brunner7> Although it seems it won't be too bad, from the statements we had here today
<d​angerousfreedom> I like your comparisons with sailing
<r​brunner7> Yeah, sometimes it's about sentiment and motivation, things that nerds may forget a bit too easily
<d​angerousfreedom> rbrunner7: I will pm you so we can try to solve your compilation problem so you can hopefully give me some feedback later :p
<r​brunner7> Alright, no stress :)
<r​brunner7> Anything left for today's meeting?
<jberman> with tevador also seemingly keen to help with performant lower level arithmetic for FCMP's as well, I'm feeling optimistic about having the people needed for implementation myself included
<d​angerousfreedom> Not from me. I will keep cleaning up things in the wallet demo and thinking about the next tasks.
<r​brunner7> Does not look like it then. Thanks everybody for attending, read you again next week!
<d​angerousfreedom> Thanks rbrunner7
<o​ne-horse-wagon> Thank you.
<SNeedlewoods> from me neither, will try to continue with reviews
<SNeedlewoods> thanks everyone
<jberman> thanks all
````

# Action History
- Created by: rbrunner7 | 2024-04-05T14:58:52+00:00
- Closed at: 2024-04-09T04:26:19+00:00
