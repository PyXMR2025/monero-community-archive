---
title: 'Seraphis wallet workgroup meeting #63 - Monday, 2024-03-25, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/982
author: rbrunner7
assignees: []
labels: []
created_at: '2024-03-22T18:27:49+00:00'
updated_at: '2024-03-25T18:35:11+00:00'
type: issue
status: closed
closed_at: '2024-03-25T18:35:10+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/980

# Discussion History
## rbrunner7 | 2024-03-25T18:35:10+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/982
<r​brunner7> Can you please add "reading" to your hello
<r​brunner7> so I know who can read me and who probably not
<d​angerousfreedom> Hello. I can read you now :)
<j​berman> *waves*
<r​brunner7> jberman: Can you read me?
<SNeedlewoods> hey, I joined IRC so hopefully see the best of both worlds
<s​needlewoods_xmr> hey
<r​brunner7> Perfect, SNeedlewoods . That probably works.
<SNeedlewoods> rbrunner your message didn't come through to matrix side
<jeffro256> Howdy
<s​needlewoods_xmr> jberman can you join irc? message from rbrunner does not show here
<jeffro256> I'm joining from IRC since monero.social -> matrix.org Matrix messages don't work 
* jberman (~jberman@2001:41d0:a:2aab::1) has joined
<r​brunner7> jeffro256: Do you see what I write as "rbrunner7" on Matrix?
<jberman> *waves from irc*
<jberman> I don't, I only see sneedlewood's message
<rbrunner> jeffro256: Do you see what I write as "rbrunner7" on Matrix?
<d​angerousfreedom> I only changed the server to monero.social and now I can see the messages
<j​effro256> rbrunner7: yes, but i'm on the monero.social server
<rbrunner> So maybe better I also use IRC for today?
<rbrunner> Alright, seems more or less ok then to start.
<rbrunner> What is there to report from last week?
<d​angerousfreedom> This week I could advance in putting everything together (EnoteStore, TxHistory, KeyContainer) and created a demonstrator of a wallet. The goal was to make a few transactions between two wallets, retrieve the proper balance, show the enotes and make knowledge proofs on them. Here it is:
<jeffro256> Holy moly that's awesome !
<d​angerousfreedom> I would like to kindly ask your feedback about the way things are going. I believe this could really look like a version0_pre_alpha_proto seraphis wallet :p
<jeffro256> How were transactions transmitted?
<system> file Screencast from 25.03.2024 18:21:17.webm too big to download (17663360 > allowed size: 1000000)
<d​angerousfreedom> Screencast from 25.03.2024 18:21:17.webm
<SNeedlewoods> I got feedback from koe and jberman and worked on https://github.com/UkoeHB/monero/pull/40
<SNeedlewoods> but currently my local branch is quite messy and I introduced bugs I need to fix, can still push if someone wants to see?
<d​angerousfreedom> Of course there are really a lot of things to do like:
<d​angerousfreedom> - Use the proper KeyContainer. Right now I'm using the previous version of seraphis and waiting for ghostway  KeyContainer.
<d​angerousfreedom> - Update everything (address scheme, knowledge proofs, etc) with the jamtis updates proposed by jeffro256 
<d​angerousfreedom> - Use a real ledger instead of the `MockLedgerContext`. Some comments here:
<d​angerousfreedom>     - Right now I'm de/serializing the MockLedgerContext to have a local permanent storage. This is not optimal, it is buggy now but it allows to test many wallet functions. (Thanks to Koe and his modular library design).
<d​angerousfreedom>     - Only the storage of seraphis enotes is working now. I will try to fix the serialization for the legacy ones next and try to incorporate the legacy scanner from jberman
<jberman> Update: the async wallet scanner is now backwards compatible with today's node versions, scanning perf is on par with wallet2 today when pointing to a current node (the async scanner's significant speed-up requires the daemon to update). I'm currently wrapping up the PR with final touches, cleaning up class structure/naming/commit history etc.
<jberman> Shooting for ready-for-review this week
<SNeedlewoods> before that I started this https://github.com/UkoeHB/monero/compare/seraphis_lib...SNeedlewoods:seraphis_wallet:x_identify_edge_cases
<d​angerousfreedom> I'm serializing the MockLedgerContext and loading/saving it everytime I open/close a wallet
<rbrunner> ghostway announced shortly before the meeting started that they will make a PR tomorrow.
<d​angerousfreedom> There are really a lot of clean-ups and more comments to make but I think it would be better to have your feedback on it first. Even in a high level. You can play with the wallet (open many wallets and transfer enotes between them). -> https://github.com/DangerousFreedom1984/seraphis_lib/commit/9340e037e763cc69619d3a27883327e2bf060437
<d​angerousfreedom> Just compile and run ./monero-wallet3
<rbrunner> Great, dangerousfreedom!
<rbrunner> A lot of things finally start to drop into place
<rbrunner> My little contribution was yet another rebase of our "seraphis_wallet" branch to koe's latest "seraphis_lib"
<rbrunner> I know and understand now the necessary trick, as explained patiently by jeffro256
<SNeedlewoods> dangerousfreedom I'll try to check  your monero-wallet3 out soon
<rbrunner> jberman: I think everybody is also looking forward to your PR. Another big piece.
<rbrunner> Will this a lib PR, a wallet PR, or a two-part PR?
<rbrunner> *Will this be
<d​angerousfreedom> Thanks! I will look at your PR soon also since my serialization is not working for legacy yet and it might be better to even go to a real ledger and then I would need to use your PR with jberman's scanner. I will think about it this week.
<jeffro256> Me: https://github.com/UkoeHB/monero/pull/31, https://github.com/UkoeHB/monero/pull/34, and https://github.com/UkoeHB/monero/pull/38 were merged into seraphis_lib. I'm working on a PR which will switch the way we index legacy enotes to match how we currently index enotes (amount, global index), so that we can have CLSAG rings in seraphis transactions w/o re-indexing the database 
<rbrunner> Sounds a bit like magic ...
<rbrunner> Ah, no, just a switch back to the "old" system?
<jeffro256> yes
<jeffro256> So heads up @dangerousfreeedom, the internal structure of MockLedgerContext will change with this PR I'm working on, and thus the serialization code will have to update 
<rbrunner> jberman, do you copy, this was a question meant for you: Will this a lib PR, a wallet PR, or a two-part PR?
<jberman> rbrunner I'm going to divide up the commits as cleanly as possible including small commits to the daemon RPC today, and then from there I think it'll be easier to see what should be PR'd where and at what time etc. Probably will be a number of small PR's
<rbrunner> Just making sure that we all are on the same boat regarding PRs
<d​angerousfreedom> Yeah, everything is changing everytime haha. But hopefully we will start having an idea about the core of the wallet
<rbrunner> Thanks, jberman, sounds good
<jberman> jeffro256 have you seen this PR from SNeedlewoods that introduces an `enote_same_amount_index` ? https://github.com/UkoeHB/monero/pull/40
<jberman> *enote_same_amount_ledger_index
<rbrunner> Does this solve the same problem?
<rbrunner> Or is this an addition?
<jberman> It would enable indexing by amount + global index, same as today
<jeffro256> No IIUC, they should work together. That PR is for adding contextual information to legacy enote records, while the PR I'm working on changes the `LegacyRingSignatureV4` to include an enote amount for indexing the input members 
<rbrunner> I guess jeffro256 will sort it out :)
<jberman> gotcha
<jberman> noice
<rbrunner> Alright. Do we have any separate subject to discuss today? Anybody want to bring up some general things?
<rbrunner> Nice that my incremental pool update code now becomes useful, "thanks" to the spam wave. Now we "only" have to get everybody to update
<d​angerousfreedom> Haha thanks :p
<jberman> +1
<jeffro256> yeah that's great that incremental pool updating was implemented and tested before it was really really needed 
<jeffro256> Usually not how the dev cycle goes here ;)
<rbrunner> Well, I did not have spam waves on my mind ...
<rbrunner> Ok, if nothing else I think we can close for today. Thanks everybody for the fantastic news regarding progress, and your attendance. Read you next week.
<jeffro256> Unrelated, and not to be selfish, but https://github.com/UkoeHB/monero/pull/26 still needs review, and it will affect most wallet-related things downstream. If anyone is brave enough to help review, Koe and I would greatly appreciate it 
<jeffro256> But yes thank you everyone! Things are speeding up which is nice to see 
<jberman> on my list :)
<rbrunner> Good luck, I hope you find a reviewer. That won't be me, however, that's definitely beyond my reach
````


# Action History
- Created by: rbrunner7 | 2024-03-22T18:27:49+00:00
- Closed at: 2024-03-25T18:35:10+00:00
