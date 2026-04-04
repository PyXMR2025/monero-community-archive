---
title: 'Seraphis wallet workgroup meeting #62 - Monday, 2024-03-18, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/980
author: rbrunner7
assignees: []
labels: []
created_at: '2024-03-15T16:27:58+00:00'
updated_at: '2024-03-18T19:23:13+00:00'
type: issue
status: closed
closed_at: '2024-03-18T19:23:12+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/977

# Discussion History
## rbrunner7 | 2024-03-18T19:20:49+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/980
<j​effro256> Howdy
<j​berman> howdy
<d​angerousfreedom> No pre-meeting message and no greetings from rbrunner7 . I hope he is fine :)
<d​angerousfreedom> Hello
<r​brunner7> Well, then maybe something is not ok with Matrix?
<s​needlewoods_xmr> hey
<r​brunner7> Alright. What are the reports from past week?
<r​brunner7> I tried to update our branch, as can be seen in the backlog. I think I know now how to do it. Thanks, jeffro256
<j​berman> guess it's us 3 :)
<moneromooo> I see rbrunner7's lines fwiw. Get on IRC ?
<s​needlewoods_xmr> I don't think rbrunner forgot about the meeting, because we talked about the meeting earlier
<d​angerousfreedom> Ok, from my side: this week I have been unifying my code to present a coherent work. Next week I will probably have something to show and I will be studying the possible modifications on the knowledge proofs with jeffro's changes.
<rbrunner> Can everybody by chance read me if I write on IRC?
<s​needlewoods_xmr> I had a look at #31 & #34 from jeffro, maybe could review #31, but I'm not sure my understanding is good enough to be of much value.
<j​berman> Update: I rebased and resolved merge conflicts on background sync PR 8619, that should be ready to go.
<j​berman> Seraphis lib async scanner: I pushed a functional test framework for Seraphis wallet lib -> live RPC daemon (and wallet2 -> RPC daemon) interactions: https://github.com/UkoeHB/monero/pull/23/files/aff28f13ec95fddeb7f47e1300db31bc34886137..1893f649cb40360f89c498ef233179e7d45b2f2f
<j​berman> I think this test framework can come in handy as the Seraphis lib is built up and used in a full-fledged wallet (can use this framework to test migrating from a wallet2 instance -> Seraphis lib wallet then transacting w/seraphis lib, or populating a wallet2 instance from the Seraphis lib enote store and sending valid txs pre-Seraphis fork, or to eventually test the complete end-to<clipped message>
<j​berman> -end Seraphis lib -> live daemon flow, etc.).
<j​berman> It's divided into 3 commits. Commit 1: a helper simple daemon RPC client. Commit 2: sets up the wallet2 <> live RPC daemon test framework not using anything from Seraphis lib. Commit 3: adds tests for Seraphis lib async scanner <> live RPC daemon
<j​berman> I can PR Commits 1 and 2 to the Monero repo whenever (i.e. today), and then Commit 3 builds on top of that framework to test the async scanner in the Seraphis lib
<j​berman> This week/next I'm hoping to finish review on jeffro256  's 9135 PR to write txs to disk once instead of twice on sync, review SNeedlewoods' PR for LegacyEnoteOriginContext, make the async scanner backwards compatible with existing daemons, and clean it up so it's ready for review.
<s​needlewoods_xmr> And I did some more research for this issue https://github.com/UkoeHB/monero/issues/27 and will probably have something to work with/ask questions about soon.
<0​xfffc> (I am following the discussion. But don’t have anything to share in this meeting)
<d​angerousfreedom> SNeedlewoods: the main goal of your PR is to make jberman 's scanner compatible for all the Monero versions?
<s​needlewoods_xmr> But first I'd like to get input on how to proceed with my first PR in regards to this comment from rbrunner https://github.com/seraphis-migration/monero/pull/16#issuecomment-2002391965
<s​needlewoods_xmr> Do all the changes belong to the `seraphis_lib` branch in `UkoeHB/monero`? Then I would close the PR, rebase it locally and make a new PR to that branch!?
<s​needlewoods_xmr> Or do some of the changes actually belong to the `seraphis_wallet` branch and the PR needs to get split up?
<j​berman> that PR is necessary in order for the Seraphis wallet lib scanner to be able to scan enough data to be able to construct a pre-RCT ring on today's daemon version
<d​angerousfreedom> Awesome jberman !
<r​brunner7> Can everybody who can read this please give me a quick "thumbs up" or feedback?
<jeffro256> +1
<j​effro256> SNeedlewoods: it just adds the legacy enote context struct and utils yeah? Then you can probably rebase then PR to ukoes repo
<d​angerousfreedom> Yes! I think it would be better to PR into koe's seraphis_lib
<s​needlewoods_xmr> thanks jberman, you can explain it better than I could
<rbrunner> Can everybody who can read this please give me a quick "thumbs up" or feedback?
<d​angerousfreedom> https://github.com/UkoeHB/monero/tree/seraphis_lib
<s​needlewoods_xmr> I first started development on the `seraphis_lib` but iirc someone told me to move to `seraphis_wallet` but I don't remember the reasoning
<r​brunner7> It's a conspiracy against me as the moderator of this meeting :)
<j​effro256> rbrunner7: I can read both lol
<j​effro256> I think it's fine where it is honestly
<r​brunner7> I wanted to discuss this repo and PR question, and have a strong opinion that everything that modifies Seraphis lib code should go to koe's branch
<j​effro256> That's fair
<r​brunner7> But well ... maybe copy that over, jeffro256 , for the others to read lol
<d​angerousfreedom> Well, if nobody has other things to share then I guess this is it
<j​effro256> dangerousfreedom: that PR for direct serialization will be PRed in a couple hours
<j​berman> I got nothin else, excited for that test framework too :)
<j​effro256> Sorry I didn't get to it earlier its just I did a lot of traveling
<j​effro256> Rbrunner7 said: "I wanted to discuss this repo and PR question, and have a strong opinion that everything that modifies Seraphis lib code should go to koe's branch"
<d​angerousfreedom> Next week I'm planning to show a demonstrator of opening a wallet, making a mock transaction, visualizing enotes and making some knowledge proof. So the goal would be to use these three components EnoteStore, KeyContainer and TxHistory. This could open discussions about the (modular) wallet design. Next I will definitely try to understand more about the daemon and the node connection.
<rbrunner> That Matrix is not in the mood to forward what I write with Matrix user "rbrunner7" is one thing, but that people can't read "rbrunner" from IRC either is pretty strange
<s​needlewoods_xmr> that sounds promising
<j​berman> I forgot, I actually was hoping to also discuss progression toward a release of a usable wallet lib so devs could start using the updated lib
<r​ucknium> rbrunner: I can see your messages from IRC and Matrix both.
<d​angerousfreedom> Which wallet lib? For wallet2?
<j​berman> to replace wallet2
<r​ucknium> jeffro and I are both on the monero.social Matrix servers. Maybe that has something to do with it.
<d​angerousfreedom> How would that be different from jeffro's api of wallet2 ?
<d​angerousfreedom> (if we can call it an api)
<r​brunner7> Rucknium: Thanks for the feedback, could be, yes.
<j​effro256> The wallet2_basic API only has loading and storing capabilities RN. we need to add tx construction to it
<j​berman> hmm can you link me what you're referring to?
<j​berman> and/or expand on that? iirc jeffro mentioned interest in designing an API, but nothing concrete settled yet there
<d​angerousfreedom> https://github.com/jeffro256/monero/tree/wallet2_conv
<j​berman> oh gotcha, ya
<d​angerousfreedom> I think he tried to PR
<d​angerousfreedom> https://github.com/monero-project/monero/pull/8923
<d​angerousfreedom> I thought it was already on monero
<d​angerousfreedom> Apparently not
<j​effro256> Here it is merged in seraphis_wallet: https://github.com/seraphis-migration/monero/tree/seraphis_wallet/src/wallet/wallet2_basic
<r​brunner7> That's pretty dumb, to be be mere spectator on "my" meeting :)
<j​effro256> IIRC wallet2_conv is a little outdated
<j​berman> I was more so hoping to discuss path toward getting a lib into wallet devs' hands that's using the Seraphis lib. that PR is one element of that path, since we'll need to migrate from a wallet2 instance -> Seraphis lib-backed instance of a wallet
<j​berman> that PR got merged over here looks like: https://github.com/seraphis-migration/monero/pull/4
<j​effro256> Are you saying getting the API design done before the implementation for wallet3 ?
<d​angerousfreedom> Oh yes, into our project.
<d​angerousfreedom> I think this is very useful (at least for me). Do you have any case in mind where it fails you?
<d​angerousfreedom> Do you need something extra from wallet2?
<j​berman> have you started using that to populate an enote store?
<d​angerousfreedom> I tried to use that for the legacy knowledge proofs
<d​angerousfreedom> But I have to revisit again, it may not be the way we want to do it
<d​angerousfreedom> So, no.
<j​berman> I haven't given it a good look, I don't have an opinion on it from that end
<r​brunner7> Trying a last time, from the Linux Element app instead of the web app in Chrome. Can anybody not with monero.social as their homeserver read this?
<j​berman> I'm thinking would be nice to start thinking through / planning using that wallet2 converter, the async scanner, and the enote store to get a Seraphis-lib backed sdk into wallet dev's hands
<d​angerousfreedom> Yes! I think one needs only to put all the pieces together. You and jeffro already did the bulky work
<j​berman> I think once the scanner is out the door + SNeedlewoods PR is done, we can move toward the goal of constructing legacy txs pre-fork
<j​berman> and populating an enote store from a wallet2 instance
<d​angerousfreedom> Yeah, maybe SNeedlewoods would like to that ? So it would give a real meaning to his work on the Legacy Enotes. Could be very interesting
<d​angerousfreedom> Yeah, maybe SNeedlewoods would like to do that ? So it would give a real meaning to his work on the Legacy Enotes. Could be very interesting
<j​effro256> Same thing: can anyone read my messages ?
<s​needlewoods_xmr> I should probably stick to things that don't need to be delivered fast, because I'm very slow
<moneromooo> jeffro256: I can, fwiw.
<r​brunner7> Somehow I hope not, lol, because otherwise I start to feel targeted :)
<d​angerousfreedom> I think it would be great to learn about all the other components. You can always ask for help too
<j​berman> I think we've got a bit of time until this current slate of work is in ready-state (legacy enote PR + the scanner) and next tasks are ready. but I generally wanted to get thoughts forming on path toward shipping a usable lib using these components
<r​brunner7> Does anybody who can read me happen to know who babysits the monero.social Matrix server?
<d​angerousfreedom> My opinion is that the more tools we have the better. It cant go wrong now. I think it would be useful for many applications and tests also.
<j​berman> We'll need a way to:
<j​berman> A) populate a Seraphis lib-backed instance from an existing wallet2 instance
<j​berman> B) construct legacy txs (by populating a wallet2 instance from a Seraphis-lib backed instance, then constructing a tx with wallet2)
<j​berman> Once those are done, we can then move on toward ensuring the Seraphis-lib backed wallet supports the features that wallet devs will want, then ship a lib that wallet devs can start using today
<s​needlewoods_xmr> alright, I'll have a look and put some thoughts to it
<moneromooo> r​brunner7: I think sgp might be involved, but I'm really not sure.
<r​ucknium> rbrunner7: IIRC it's Dan Miller
<d​angerousfreedom> Why is B) necessary ?
<j​berman> because we want to ship the Seraphis lib before the Seraphis fork, and so wallets will still need a way to construct legacy txs. The approach to use a wallet2 instance that's populated in-memory on demand seemed a fairly sane approach to me: https://github.com/seraphis-migration/wallet3/issues/48
<d​angerousfreedom> I see, this path looks safer indeed
<UkoeHB> I have been struggling to find space for pending PR reviews (which require all my brain power). Hopefully later this week, but we all know how much timeline promises go.
<UkoeHB> how my*
<r​brunner7> Thanks, UkoeHB, for the info. I hope we will manage to make it known to all people, not just the people on the monero.social Matrix server
<j​berman> SNeedlewoods: if you do start looking into this soon (which it's fine if you focus on other stuff for now like those edge cases I think), I think the test framework I just pushed for the async scanner would also come in handy to mess around with. It can be useful to see what it's like to use the wallet2 instance to construct txs, and start getting a sense for routes to make wallet<clipped message>
<j​berman> 2 <> Seraphis lib play nice
<s​needlewoods_xmr> yeah I took a lot of notes from what you guys mentioned here and will do my homework
<j​berman> awesome, approaching the end of the hour now
<d​angerousfreedom> Thanks for the discussion guys
<s​needlewoods_xmr> thank you guys, until next week
````


## rbrunner7 | 2024-03-18T19:23:12+00:00
FYI, for the unlikely case it should ever become important: Probably because of problems with the monero.social Matrix server, rbrunner7, jeffro256, and Rucknium could read each other, but other people could see none of their messages. jberman, dangerousfreem and sneedlewoods basically had the meeting for themselves.

# Action History
- Created by: rbrunner7 | 2024-03-15T16:27:58+00:00
- Closed at: 2024-03-18T19:23:12+00:00
