---
title: 'Monero Tech Meeting #172 - Monday, 2026-06-01, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1397
author: rbrunner7
assignees: []
labels: []
created_at: '2026-05-29T05:23:19+00:00'
updated_at: '2026-06-01T18:39:23+00:00'
type: issue
status: closed
closed_at: '2026-06-01T18:39:23+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1394).


# Discussion History
## rbrunner7 | 2026-06-01T18:39:23+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1397
<jpk68> Hello
<jberman> waves
<sneedlewoods> Hey
<vtnerd> hi
<rbrunner7> Alright. Let's start with the reports from last week. I continued with Polyseed, where work to implement it in the Wallet RPC Server was quite a bit more than anticipated. But nearing completion now.
<sneedlewoods> still restore height on wallet creation in the GUI and updated wallet-rpc with rebasing and minor fixes https://github.com/monero-project/monero/compare/master...SNeedlewoods:seraphis_wallet:x_remove_wallet2_from_rpc
<jpk68> Made some small progress on I2P SAM integration, made a bunch of random patches/fixes, worked with sneedle on adding a --wallet-dir option to simplewallet
<jpk68> Looks like I also successfully CBOR-pilled vtnerd ;)
<rbrunner7> What is "CBOR"?
<jpk68> It's a binary serialization format, used in RPC as an alternative to JSON
<rbrunner7> You mean it gets investigated as viable or not now?
<jberman> FCMP++ integration audit remediation tasks (can see latest PR's here: https://github.com/j-berman/monero/pulls ), stressnet monitoring
<jpk68> @rbrunner7: https://github.com/monero-project/monero/pull/10659
<jpk68> It looks like the plan was originally to use MsgPack, but I made the case to use CBOR instead and it looks like that's what's happening now :)
<rbrunner7> Ah, there was a need for something there for quite some time already?
<jpk68> +1
<rbrunner7> What's the main driver there?
<jpk68> I should probably let vtnerd answer this
<rbrunner7> I ask because I was wondering that if bytes transferred should happen the main driver, whether it would be possible to simply use HTTP traffic compression ...
<rbrunner7> (An idea from some bombastic new wallet announcement recently, which is maybe not even dumb)
<jpk68> I'm not too sure whether that would be viable, but generally, JSON will be a lot slower/larger than binary serialization
<rbrunner7> Yeah, but very zip-friendly maybe
<jpk68> CBOR is somewhat widely-adopted and is nicely standardized
<rbrunner7> Just brainstorming, @vtnerd:monero.social is the comms guru :)
<jpk68> +1
<jpk68> It's also worth noting that kayabaNerve was also in support of CBOR, it was by no means my doing alone
<jpk68> He would (obviously) know better than me
<rbrunner7> I see.
<rbrunner7> If we are complete with the reports, I did some brainstorming about the FCMP++ release process that I want to share.
<rbrunner7> Do I get that right: The plan so far for that monumental FCMP++ plus Carrot hardfork release is to give it the new main release number 19, and fork the release branch from master?
<selsta> the current plan is to have a v0.19.0.0 release early, without any HF
<selsta> this gives us time to test the new guix build system in the wild
<rbrunner7> What will that be based on?
<selsta> master
<selsta> and then have a v0.20 or maybe even v1 (doesn't matter) with FCMP++
<rbrunner7> Ah, ok, then other people had the same idea that crossed my mind, and I can already rest my case :)
<rbrunner7> I was thinking about all those things that accumulated on master during literally years the release branch is separate already, and possible problems if that goes live all at once together with all the really new stuff
<selsta> v0.19 can also contain the Polyseed changes if they are ready
<rbrunner7> About what time horizon do we talk here, give or take?
<selsta> 2-3 months
<rbrunner7> That could work if I hurry a bit
<selsta> I don't know what the current plan is for FCMP++, but I assume it will need at least another 6 months?
<selsta> see also https://github.com/monero-project/monero/issues/10682
<jberman> Hopefully not, and we're currently building on top of master
<selsta> but would that be an issue for v0.19 release?
<jberman> nope, v0.20 or v1 would be fine and relatively seamless
<rbrunner7> Throwing about bootstrapping should really simplify many things
<rbrunner7> No wonder the AIs byte :)
<rbrunner7> By the way, that would be Polyseed in the CLI wallet and RPC server - no GUI wallet yet, didn't even start to look into that
<rbrunner7> But I guess that could become a relatively painless update along the way without much fuss
<sneedlewoods> sorry for much typing, I don't have that much to say :D
<sneedlewoods> I imagine v19 on master will also simplify many things 
<rbrunner7> No problem :) Do we have to discuss something else still today?
<vtnerd> Perf. Numbers are in pr. Zmq-pub uses json which is inefficient in size and time, especially given the amount of crypto binary blogs that have to be transferred > <@rbrunner7> What's the main driver there?
<vtnerd> *blobs
<rbrunner7> Thanks for the hint, vtnerd, didn't scroll down enough to see them. So JSON is also less efficient to generate in the first time?
<rbrunner7> Alright, let me close the meeting proper, room stays open of course ... thanks for attending everybody, read you again next week!
<jpk68> +1
<sneedlewoods> thanks everyone
````


# Action History
- Created by: rbrunner7 | 2026-05-29T05:23:19+00:00
- Closed at: 2026-06-01T18:39:23+00:00
