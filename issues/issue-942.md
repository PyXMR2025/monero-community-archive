---
title: 'Seraphis wallet workgroup meeting #49 - Monday, 2023-12-11, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/942
author: rbrunner7
assignees: []
labels: []
created_at: '2023-12-08T18:47:40+00:00'
updated_at: '2023-12-11T19:15:46+00:00'
type: issue
status: closed
closed_at: '2023-12-11T19:15:46+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/939

# Discussion History
## rbrunner7 | 2023-12-11T19:15:46+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/942
<s​needlewoods_xmr> heyho
<j​berman> Waves
<r​brunner7> So, any reports from last week? I did not have much to do, I just merged a little PR from ghostway , the encrypted files class
<h​into.janaiyo> hello
<s​needlewoods_xmr> just added another commit https://github.com/seraphis-migration/monero/pull/16
<s​needlewoods_xmr> but tests still fail at the same place, so will look further into that
<r​brunner7> Glancing over the code you wrote for that PR I think you have already learned quite something about the Seraphis library, in a relatively short time frame.
<j​berman> Worked on monero-serai and made some progress in discussions on formalization of Seraphis (nothing to report yet on this front, but hopefully should have something this week). Will finish up the bulk of monero-serai work remaining this week, then move back over to Seraphis wallet work next week. I have a new CCS proposal drafted
<s​needlewoods_xmr> but I have to do baby steps, otherwise I get easily lost in the codebase
<r​brunner7> jberman: Do you already know what you will go into next regarding wallet work?
<r​brunner7> SNeedlewoods: Even baby steps accumulate if you just do enough of them :)
<j​berman> rbrunner7: complete this PR https://github.com/UkoeHB/monero/pull/23
<j​berman> after that, probably help move forward the enote store, and then I'm thinking starting to glue the wallet API to the Seraphis wallet lib
<r​brunner7> jeffro256 wrote something here yesterday about some Janus attack and address index generators. Does that tell anybody anything? Is this something to worry about?
<r​brunner7> > glue the wallet API
<r​brunner7> Well, which API?
<g​hostway> Hello, pushed some fixes to my pr
<g​hostway> Oh, its been merged? Cool
<r​brunner7> Indeed :)
<g​hostway> Anyone got any cool new ideas for wallet/innovative work?
<s​needlewoods_xmr> just saw jeffro commented on his PR that he added a test for janus attack https://github.com/UkoeHB/monero/pull/26
<r​brunner7> Ah, I see: "Will push fix soon..."
<j​berman> ya looks like he's working through it still and that it only applies to his changes. it will be something to think deeper about in reviewing his changes, looks like
<j​berman> I'm thinking maybe `wallet/api/wallet.h` + `wallet/api/wallet_manager.h`? Underlying goal being how to glue the CLI/RPC/GUI wallets to the new wallet lib, and so that seems a good catch-all spot to start with
<j​berman> or start exploring
<j​effro256> Howdy
<r​brunner7> Well, when I still was hoping for taking part in designing and implementing, I had the intention to design a new wallet API from the ground up. Nothing existing that I looked at really convinced me, I have to say.
<r​brunner7> And yes, of course with a new API there is much to adjust. But there is much to adjust anyway because of Seraphis and Jamtis I suspect.
<j​effro256> I think wallet RPC should remain mostly intact , which shouldn't necessarily be too hard
<j​berman> writing a new API seems a reasonable path to me too. I think avoiding rewriting the CLI and RPC wallets from the ground up would be nice
<j​effro256> Also wallet/API could be mostly doable
<r​brunner7> RPC should learn more than 1 wallet open at the same time, surely? Just for one thing.
<r​brunner7> I have to look back in the meeting logs, I think we already discussed various such points "in the early times" i.e. a bit less than a year ago
<j​effro256> Yes this is true
<j​berman> we did, I don't recall where it settled firmly
<j​effro256> Although specifying an API for more than 1 open wallet at a time can be done in a backwards compatible manner
<j​berman> at this stage I generally feel this is a nice-to-have
<r​brunner7> Well, how many tools using the RPC interface did you already build? :) I am running 3 different instances of the RPC server for my techwallet, and for each of them I open and close wallets on the fly as needed. As elegant as an overweight elefant.
<r​brunner7> But yeah, maybe a bit special as a use case ...
<j​berman> I mean I think it's an important nice-to-have. theoretically someone could spin up an external wrapper tool that manages multiple RPC wallet processes
<r​brunner7> Ok.
<r​ucknium> You hit the RAM limit quickly if you do that. monero-wallet-rpc takes a lot of RAM.
<r​ucknium> However, I don't want any Seraphis dev's job to get harder 😅
<j​berman> guessing that's when syncing multiple wallets, all from an early start point. each request for blocks is 100mb
<r​ucknium> I think it takes lots of RAM just from existing
<r​ucknium> monero-wallet-rpc is a major pain point for application developers. It also has problems when connecting to a remote monerod.
<r​ucknium> If an application developer wants to develop anything custodial, even a custodial view key, then the one-wallet restriction is a pain point.
<r​brunner7> It's also simply an outdated API design nowadays, I would say
<r​brunner7> Imagine a web browser without tabs :)
<h​into.janaiyo> sounds like seraphis could benefit from more developers - especially optimization stuff like this
<h​into.janaiyo> i think i know a guy
<r​brunner7> I think this all also depends on our capacity. If we don't get additional dev capacity we may be forced to aim low
<r​brunner7> hinto: By all means tell them to have a look at what we do!
<h​into.janaiyo> (guy == me)
<j​berman> if anyone wanted to take on the task of a new multi-wallet RPC interface (just the interface), I don't think Seraphis is a blocker on that
<r​brunner7> Ah, ok :) You mean possible follow-up work after you get bored with Cuprate, or you finish that whole thing
<r​brunner7> Or do I confuse you now with somebody else?
<h​into.janaiyo> cuprate is still up in the air - not really enough community/dev push for it so i think it'll be indefinitely blocked
<r​ucknium> For example this: "5. Allow a different Monero wallet per store, not only 1 wallet per server" https://bounties.monero.social/posts/88/3-500m-btcpay-server-additional-optimizations
<h​into.janaiyo> although i don't think any questions would be raised if i "worked on seraphis"
<r​brunner7> jberman: I am a bit skeptical, but never had a close look. You may well be right
<r​ucknium> ^ There is probably no good way to do this simple thing without a complicated and failure-prone cycling through wallets in the background
<r​brunner7> @hinto: You mean your CCS proposal won't get the necessary support to get merge? I am a bit confused
<j​berman> I'm thinking the Seraphis lib could be built up to meet that interface
<j​berman> it's modular enough as is that I think it's doable
<h​into.janaiyo> rbrunner7: quite possibly yes
<r​brunner7> jberman: Do we mean the same? I meant that already know it's reasonably possible to work on a new RPC interface
<r​brunner7> That I doubt a bit, but may be wrong
<j​berman> why do you doubt that?
<r​brunner7> I imagined to come up with a wallet API, and then the RPC API would essentially be **the same**, just over RPC
<r​brunner7> If the interface is good, that should be possible, one would think
<r​brunner7> Or, the other way round, why the heck would there be different interfaces?
<j​berman> ah I see where you're coming from there
<j​effro256> So do you already have an API design written down ?
<j​berman> I don't think Seraphis is a blocker on the design of that interface
<r​brunner7> No. Did not get as far as actually designing anything
<r​brunner7> I definitely have to read some early logs. They may become important soon.
<r​brunner7> ghostway's question about possible follow-up work for them went under a bit in the various discussions. If somebody has a good idea for a component to tackle, preferably not too big I guess, please write it down here anytime.
<r​brunner7> Did I actually discuss a little class to manage options with somebody here? Because that's also needed sooner or later. Not very sexy, not very challenging, but somebody will have to write it sooner or later
<r​brunner7> I mean wallet options
<j​effro256> What kind of options ?
<r​brunner7> All the various things that now are direct members of the wallet2 class. We should unite them in a nice class, with each option checked whether still relevant now and under Seraphis + Jamtis
<j​berman> like all these? https://github.com/monero-project/monero/blob/ac02af92867590ca80b2779a7bbeafa99ff94dcb/src/simplewallet/simplewallet.cpp#L3168
<r​brunner7> Yeah, those more or less directly translate into things to set in a `wallet2` object
<j​effro256> All of those options can be read using the wallet2_basic lib
<r​brunner7> Yes, we got migration already covered, which is nice. I am talking about how the *new* Seraphis wallet will handle options. In the interest of better modularization, with a separate options class
<j​berman> that sounds like a good idea to me
<j​effro256> Ah okay yeah that's good
<j​effro256> Yeah a lot of the options are obsolete but it'd be good to go thru and see which ones translate well
<r​brunner7> It's possible that I discussed this already with ghostway or dangerousfreedom . Man, I get old.
<r​brunner7> Yes, and adding comments. Lots of comments :)
<j​effro256> Honestly yeah it could be a good learning exercise and would add value to the codebase if people went thru and added comments to undocumented parts of the code
<j​berman> it gets a little tricky separating stateful options that are saved to the wallet (like `inactivity_lock_timeout`), and runtime config options (like --trusted-daemon), but I think collecting all options into a separate class, separating them cleanly, is a good task
<r​brunner7> Alright. I think we rarely discussed so many different points in a single meeting, and we are approaching the full hour. Anything important left to say for this meeting here?
<s​needlewoods_xmr> options task sounds interesting, would look into that if I didn't have something already
<j​berman> to wrap up the discusison from earlier on a new interface, it would be nice to start putting "pen to paper" on the design of such an interface if someone wanted to take that on
<r​brunner7> Sure. Maybe a warning that this may be quite challenging work. Maybe does not look like it first, but well ...
<j​berman> I bet woodser would be a very solid point of contact and reference on that as well. see this: https://moneroecosystem.org/monero-java/monero-spec.pdf
<r​brunner7> Yes. I studied that to quite some degree early on. And there you also see that you *can* do it quite differently
<h​into.janaiyo> jberman: is separating the interface/functions from internal details like thread+async a value in seraphis?
<h​into.janaiyo> or should these be made in such a way they can be called from any context
<j​effro256> Wdym called from any context ?
<h​into.janaiyo> i guess a practical example would be generic functions with no assumptions executed by the caller vs functions that spawn a bunch of stuff to do work
<j​berman> I don't think we have a definitive answer to that question yet. in the scanner for example, I tried to separate the networking implementation from the interface so that the caller can bring their own network client, but the scanner's main value-add is its speed which comes from its multithreaded implementation
<j​berman> the "async scanner" I'm working on
<j​berman> @spirobel voiced strong thoughts on this here: https://github.com/seraphis-migration/strategy/issues/1
<r​brunner7> Oh yeah, that issue
<h​into.janaiyo> yeah separating is definitely harder - i meant mostly about the new rpc api
<h​into.janaiyo> stuff like caller calls rpc api x32 or x32 threads are spawned and returns result
<j​berman> in order to realize maximum performance, then the RPC would probably have to internally be capable of multithreaded execution
<r​brunner7> Allow me to declare the official meeting over, have to go. Please do continue with the discussion of course. Thanks for attending everybody, interesting meeting.
<s​needlewoods_xmr> good meeting, thanks everyone
````



# Action History
- Created by: rbrunner7 | 2023-12-08T18:47:40+00:00
- Closed at: 2023-12-11T19:15:46+00:00
