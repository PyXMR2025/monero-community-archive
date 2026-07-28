---
title: 'Monero Tech Meeting #179 - Monday, 2026-07-27, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1430
author: rbrunner7
assignees: []
labels: []
created_at: '2026-07-24T18:22:28+00:00'
updated_at: '2026-07-27T19:12:03+00:00'
type: issue
status: closed
closed_at: '2026-07-27T19:12:03+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1427).


# Discussion History
## rbrunner7 | 2026-07-27T19:12:03+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1430
<sneedlewoods> hey
<jeffro256> Howy 
<jeffro256> Howdy
<rbrunner7> Another summer time meeting :)
<jpk68> Hello
<syntheticbird> Hello
<rbrunner7> Alright, what is there to report from last week?
<jberman> waves
<sneedlewoods> reviews, addressing review comments, rebasing and solving merge conflicts
<rbrunner7> I can still do one or the other improvement of my Polyseed PR because I still receive review comments. Nice to see how many people engage!
<jeffro256> me: finishing up on mx25519 PRs (thanks tevador for reviewing!). Waiting on https://github.com/monero-oxide/monero-oxide/pull/188 for https://github.com/monero-project/monero/pull/10963. Reviewing j-berman's FCMP++ PRs, made a Gannt chart for FCMP++/Carrot work
<jpk68> Me: work on I2P integration, GUI testing for Qt6 migration, and fixing some issues with hardware wallets. I also submitted another CCS proposal for general development, and took a slight detour to fix a few dozen memory safety issues in i2pd :)
<rbrunner7> i2pd, that's one of the open source server projectes then?
<jeffro256> me: also reworked carrot_core to use the new unclamped API and crypto::x25519 wrapper 
<jberman> No significant update on my end, continuing upstream FCMP++ PR's. Have been a bit busy with personal stuff lately, will be back 100% Thursday
<jpk68> @rbrunner7: Yes, a C++ implementation of the I2P daemon.
<rbrunner7> I wonder how Monero will fare with a good implementation. Seems always a bit below a critical mass so far to me ...
<jeffro256> Rebased Ukoe's carrot_impl review PR, will submit comments to that soon, then will implement review feedback, then peel and rework carrot_impl for recent carrot_core changes 
<rbrunner7> @jeffro256:monero.social: Will you proudly present you chart / timeline in the MRL meeting?
<jeffro256> Yes, I can do that 
<rbrunner7> My last main change to the Polyseed PR, by the way, was respecting custom restore heights even with Polyseeds. A discussion convinced me that this should be ok.
<selsta> Cake Wallet is having issues with transactions not getting relayed. I looked a bit into it and so far wasn't able to figure out why. We did not have any relevant changes on the daemon side in a while.
<jeffro256> Maybe a targeted attack?
<selsta> They asked if it's a network issue but I haven't seen evidence for that so far.
<selsta> No logs unfortunaterly.
<jpk68> Do any other wallets have reports of the same issue?
<rbrunner7> You mean the transactions go from the wallets on the smartphones to their Monero daemons and then get stuck there?
<selsta> It's not clear, it looks like the node has no knowledge of the tx, or it's still in the phase where the daemon acts like it doesn't know about it.
<jeffro256> So the tx never shows up locally? 
<jeffro256> Hmmm then it feels like an application issue ngl 
<plowsof> could be related? https://github.com/monero-project/monero/pull/9295
<jberman> Fwiw Rucknium's similar issue stems from a restricted RPC, if it was unrestricted the wallet would detect the tx. So I think unrelated in case that's a thought here
<rbrunner7> Maybe they didn't change something on the side of their app, but some Android update does not play nice anymore with their software?
<plowsof> a feather wallet user reported one of my nodes dropped a tx, but feather has multi tx broadcast so it was fine. and a 2nd person told me about a similar tx - the node had not seen their txid, with no double spends or failures seen, odd 
<jeffro256> Wasn't there a few recent change which hid RPC information from restricted clients? Maybe they pulled in those commits, and expected the data and timing to remain the same 
<selsta> We did have this person who reported a similar issue but was using old software, and they did not have a publicly exposed node: https://github.com/monero-project/monero/issues/10923
<jpk68> I think we'll just be stumbling around in the dark without more info about this
<selsta> if there was a network wide attack we would get more reports from users that don't use Cake Wallet like exchanges
<selsta> yes, without logs we won't be able to figure this out
<rbrunner7> Well, depending on what you want to achieve, just attacking the Cake Wallet nodes is already enough
<rbrunner7> But I speculate that would be a kind of attack that is not publicly known until now?
<jpk68> Doesn't Cake Wallet (have the option to) use nodes besides their own?
<sneedlewoods> yep
<jpk68> +1
<rbrunner7> But many people may not know that
<UkoeHB> me: multisig update is ready, waiting on hotcold stuff being merged before I can PR
<jberman> +1
<jeffro256> +1
<sneedlewoods> +1
<jpk68> +1
<rbrunner7> That's nice. So multisig is saved for the time being!
<rbrunner7> Still experimental (tm) :)
<UkoeHB> It's going to need thorough use-testing @rbrunner7
<rbrunner7> I see ...
<jeffro256> UkoeHB: I just rebased the carrot_impl review PR, I will try to merge that ASAP pending feedback on the PR
<jberman> Trail of Bits publicly shared their audit of the FCMP++ integration Phase 1 here: https://github.com/trailofbits/publications/blob/master/reviews/2026-07-magicgrants-monerofcmp++crypto-securityreview.pdf
<jpk68> +1
<jeffro256> +1
<jbabb> +1
<UkoeHB> Also I should probably see if the python tests still run...
<UkoeHB> jeffro256: ty I reset the branch
<jeffro256> +1
<jberman> I'll update all the places that publicly reference that audit with that link when I get the chance
<rbrunner7> @jberman:monero.social: How bad is it?
<jberman> The audit? It was all informational issues. The audit went well
<rbrunner7> Good.
<jberman> It's been complete for a while and we've had the content from the audit for a while, but we've been waiting on them to have it publish-ready
<jberman> So we've known the informational issues and their rationalethey identified for a while
<rbrunner7> Ok. As it looks we are through with the reports, the obligatory question: Anything to discuss today beyond those?
<jeffro256> I wanted to discuss something before the MRL meeting regarding planning for FCMP++: should we wait 6 months after the beginning of the code freeze, or 6 months after the end of the code freeze to activate the HF? The former would move the schedue for v17 activation by 4 weeks.  Sech1 already gave his feedback (thank you):
<jeffro256> > wait period is there to let users update their nodes, miners, and maybe some custom code. Mostly the miners and custom code - nodes can be updated much quicker. So 6 months after the code is finalized (except for bugfixes)
<jeffro256> *move up
<rbrunner7> Not sure I understand. What is "the end of the code freeze"?
<jeffro256> 4 weeks after the merge of the HF table update, and thus the merge of the first commit that is "FCMP++ ready"
<jeffro256> or FCMP++ enabled, rather 
<jeffro256> The beginning of the code freeze the moment that me merge in said change 
<rbrunner7> Hmm. Still not sure about the difference of the two options on the table, sorry
<tevador> AFAIK there has never been a wait period of 6 months before HF. However, if we want to do it, it should be 6 months from the first production release, IMO.
<jeffro256> Then follow-up: would the first production release be prepared ASAP after the HF activation merge? 
<jpk68> This is probably a dumb question, but why?
<tevador> To clarify: I have the same opinion as sech1
<sech1> The whole 6 months numbers came from me IIRC :D
<rbrunner7> Isn't a sensible definition of "code freeze" the point in time where we "freeze" the release branch and only do the absolutely necessary changes?
<sech1> It was related to miners updating their XMRig
<sech1> But since XMRig is already 4 months in, it's mostly out of the picture now
<jeffro256> @rbrunner7: Yes. TBC, I have 2 different code freeze planned in the schedule: a code freeze for all consensus and p2p, then a later freeze for wallet features 
<rbrunner7> Ah, that's the bit I was missing, two freezes
<DataHoarder> sech1: afaik other randomx features like commitments are still not in xmrig yet?
<jeffro256> Because IMO waiting for multisig, hot/cold, HW, knowledge proofs, all sync_tx features, etc is not a good idea 
<jeffro256> @rbrunner7: Well the 2nd freeze isn't relevant for this specific planning question 
<sech1> XMRig supports commitments for RandomX v2
<DataHoarder> or well, they are implicit in a way, just one extra step in the pipeline
<sech1> In Stratum protocol
<rbrunner7> Just when I thought I understand :(
<sneedlewoods> +1
<sech1> Pools don't (yet)
<tevador> 6 months from the commit when the first HF-ready monerod binary can be built
<sech1> But pools can be updated faster
<jeffro256> So if we wait 6 months after first production release, where do we place the first production release in relation to the first HF-enabled merge?
<DataHoarder> then all good. I guess that would need to be updated for mining directly against monerod rpc using the new block format that includes commitment 
<sech1> "the first HF-ready" means it already has the hardfork height hardcoded
<jeffro256> tevador: So *don
<jeffro256> So don't wait on the first production release then?
<jeffro256> sech1: Yes
<sech1> Monero solo mining is not supported in XMRig yet, but it's a much smaller chunk of the network hashrate
<sech1> *solo mining for v2
<tevador> If the first release need all wallet features then no, don't wait
<DataHoarder> sech1: then that's all good for miners/randomx, and other stuff can update faster
<sech1> https://github.com/xmrig/xmrig/blob/master/src/backend/cpu/CpuWorker.cpp#L321-L326
<rbrunner7> If we can say with good conscience "Ok, we are pretty much finished, from now on only urgent fixes, a.k.a. code freeze" won't this be more or less the point where we can risk a first public release? Or do you see there the question of how much wait time?
<jeffro256> Okay, can we agree on the following plan?. Event A) HF-enabled merge is merged into master. Event B) First prodution release. Event C) Month-long first consensus/p2p code freeze. Event D) 6-month v17 wait period. Event B depends on A, Event C depends on A, Event D depends on A, and not C nor B
<sech1> code freeze and the first public release must still be separated by a few weeks to test it and fix the most severe bugs
<rbrunner7> But we can also agree that wide testing only starts with B)?
<jeffro256> This plan may mean that there is less than 6 months of wait between Event B and Event D, depending on long it takes us to prepare/publish the first production release 
<rbrunner7> And you guesstimate right now that between A) and B) we will have about 1 month?
<jeffro256> Not necearrily, it could be one day. 
<tevador> I think anything more than 2 months between B and D would be sufficient.
<jeffro256> Unless we want to make event B depend on event C
<rbrunner7> No, I mean, what is realistic. Releases to take their time.
<sech1> btw first production release also means testnet forks to fcmp++
<jeffro256> It totally depends on how fast it gets pushed out, with the current plan 
<sech1> and everyone tests their stuff on testnet
<sech1> pools, miners, exchanges etc
<sech1> 6-month wait period can start right at B)
<jeffro256> Yeah, rbrunner7 makes a good point for putting out the first point release as soon as possible: the quicker it is out, the faster we get real user testing 
<rbrunner7> sech1: I understand jeffro wants the 6 months start at A)
<sech1> maybe this: "fisrt release -> a couple weeks wait -> testnet fork -> 6 months wait -> mainnet fork"?
<sech1> well, testnet fork can be tied to A)
<sech1> just it will make harder for people to test the actual fork sequence without the released binaries
<rbrunner7> I think so as well. Anybody bold enough to use testnet deserve what they get :)
<jeffro256> sech1: I think that having the 6 month wait start after testnet/stagenet activation is a bit too conservative for more taste, I would prefer the activation is sooner than that
<jeffro256> It's not like no one is testing until the offical testnet activation date 
<jeffro256> We've had a stressnet live since October 
<sech1> 6 months is not a sacred number, it can be shorter - given that XMRig miners are mostly updated already
<sech1> I still need to prepare P2Pool for FCMP++, but I guesstimate it will not take more than 1 month
<tevador> Remember that all transactions before FCMP activation will be eventually deanonymized, which is a good argument not to delay the fork unnecessarily.
<jeffro256> +1
<rbrunner7> At least this discussion shows that some good labels for all the points in time that are important will be very useful for a good discussion ...
<sech1> https://github.com/xmrig/xmrig/releases/tag/v6.26.0 - release on Mar 28th, so starting from October XMRig is out of the equation - I assume that most miners will be updated by then
<rbrunner7> What I wonder a bit: Point A), the day when jeffro, jberman and others proudly declare "FCMP++ coding is done, heureka", that day alone has not much meaning. It only gets meaning through testing, IMHO.
<jeffro256> sech1: would you find it acceptable to activate 6 months after HF-enabled merge on master, assuming that the first production release was prepped ASAP after that point, and the announcement was widely disseminated?
<DataHoarder> I have been testing go-p2pool in stressnet, "as is", most of the work was bringing in the Carrot derivations (and keeping up with changes), so P2Pool should indeed be fairly easy (ofc P2Pool is in C)
<sech1> jeffro256 yes
<sech1> in fact, it can be even shorter than 6 months
<jeffro256> @rbrunner7: I agree, although, we have been testing, debugging, and reviewing each other's work for well over a year FWIW 
<sech1> but not too much shorter
<sech1> less than 4 months will be too tight
<jeffro256> Does that sound good tevador?>
<tevador> I'm OK with that
<rbrunner7> But aren't some pretty big puzzle parts like the "work for submitting big transactions" still missing?
<jeffro256> PoWER? Yes, that's a fair point. That hasn't undergone much review, and isn't currently implemented 
<rbrunner7> (Out of the loop, admittedly.)
<jeffro256> Or rather, there's a PR for it by hinto, but it has yet to be integrated and throughly tested 
<rbrunner7> But yeah, fair point, extensive stressnet runs do mean something of course
<sech1> There are also coins merge mining with Monero (Tari on mainnet now, DarkFi on testnet) - they will need to synchronize their forks too, not sure how capable they are and it's secondary to Monero's schedule
<rbrunner7> Maybe they need the push of an announced hardfork date :)
<jeffro256> Surely 6 months is enough time to update to RandomX v2 + commitments, plus the field changes to the block content hash? 
<sech1> I vaguely remember that I helped Tari to untangle Monero block template construction/verification, and FCMP++/Carrot changes it quite a bit, so I'll have to help them again
<jeffro256> +1
<sech1> DarkFi guys seem to be much more capable
<rbrunner7> Did some Tari devs already leave, taking "low-level knowledge" with them?
<sech1> yes
<jeffro256> sech1: I guess that they now have to use Carrot 
<jeffro256> Tari is almost all Rust, correct? I do have a Carrot library which they could use 
<sech1> yes, Tari is all Rust
<sech1> DarkFi too
<boog900> Tari uses monero-rs
<boog900> which probably wont last post FCMP 
<jeffro256> Speaking of my Carrot-rs library, would that be a good candidate to be maintained by monero-oxide? 
<jeffro256> Or should I maintain it in a personal repo?
<boog900> I think so, but I can only speak for me 
<rbrunner7> Usually the more "official", the better for the long-term future of something, if you ask me
<DataHoarder> jeffro256: maybe moved in-tree as a crate into monero-oxide?
<jeffro256> It already pulls in a monero-oxide dependency for definitions of H and T 
<jeffro256> If that would be better for the long-term health of the ecosystem, I'll make a PR to merge it into monero-oxide
<boog900> +1
<jeffro256> Gotta update a couple things first though because of all the recent upstream tweaks to FCMP++ 
<DataHoarder> would https://github.com/jeffro256/carrot be moved to be along where carrot-rs ends up at?
<rbrunner7> For what it's worth, I currently tend to agree to a "6 months after A)" schedule. Such a schedule would be a success anyway, compared with earlier hardforks.
<jeffro256> +1
<rbrunner7> Alright, I guess discussion will continue in the MRL meeting, if @jeffro256:monero.social brings up the point there.
<jeffro256> I'm gonna keep that one ;)
<jeffro256> The spec is relevant to other impls beside the Rust impl anyways
<boog900> +1
<rbrunner7> It looks like we reached a good point to close. Thanks everybody for attending, read you again in 1 week!
<sneedlewoods> thanks everybody, cu
<tevador> @jeffro256 Opinions about this PR? https://github.com/tevador/mx25519/pull/19
<jpk68> Thanks!
````

# Action History
- Created by: rbrunner7 | 2026-07-24T18:22:28+00:00
- Closed at: 2026-07-27T19:12:03+00:00
