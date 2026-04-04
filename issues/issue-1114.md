---
title: 'Monero Tech Meeting #96 - Monday, 2024-11-25, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1114
author: rbrunner7
assignees: []
labels: []
created_at: '2024-11-22T18:21:25+00:00'
updated_at: '2024-11-25T19:10:59+00:00'
type: issue
status: closed
closed_at: '2024-11-25T19:10:59+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1110).


# Discussion History
## rbrunner7 | 2024-11-25T19:10:59+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1114
<s​needlewoods> hi
<j​berman> *waves*
<j​effro256> Howdy
<r​brunner7> Welcome back from Mexico :)
<r​brunner7> I hope "back to coding" so there is something to report already :)
<r​brunner7> So, what happened last week for you?
<s​needlewoods> Added callback functions [here](https://github.com/monero-project/monero/pull/9464/commits/85d3200831781fe873ee5bef6d9122c02745fc1e), I think the methods in "wallet2_api.h" maybe should not be pure abstract functions, but will hopefully figure that out with tests.
<s​needlewoods> and here is the interface for `setDaemon()` I'm about to implement next https://github.com/monero-project/monero/pull/9464/commits/c4488ab10790316eacce6f059cc0721a0f7a2c62
<j​berman> me: continued making progress on starting tree sync from arbitrary restore height. Nothing significant to report. Working on db, RPC (/getblocks.bin), wallet2, and tree sync module changes
<s​needlewoods> I'm about to implement next, if nothing speaks against it*
<r​brunner7> Has quite a number of parameters, that call
<s​needlewoods> I looked into how wallet_rpc handles the ssl_options, that's where those parameters come from, but not sure if that's the way
<r​brunner7> Yeah, I think there is probably a good reason and good use case for each of the parameters
* DataHoarder has quit (Ping timeout: 248 seconds)
* DataHoarder (~DataHoard@user/meow/DataHoarder) has joined
<s​needlewoods> Only alternative I saw was including "net_ssl.h" for `epee::net_utils::ssl_options_t` into "wallet2_api.h", but we want only standard headers there.
<jeffro256> +1
<r​brunner7> Probably, yes.
<r​brunner7> jberman: Just curious, how far away are you from syncing "true" FCMP++ transactions from the blockchain through the daemon?
<j​effro256> @jberman I posted this comment https://gist.github.com/kayabaNerve/dbbadf1f2b0f4e04732fc5ac559745b7?permalink_comment_id=5299298#gistcomment-5299298 yesterday on kayaba's FCMP post. Definitely not asking for this now, but is this approach correct/feasible?
<j​effro256> Btw, I've just been working on Carrot HW device handling code this week
<j​berman> I'd guess once I finish wallet sync (ETA 3 weeks), another 1-2 months to wire up prove/verify/consensus changes
<r​brunner7> Ok, thanks.
<r​brunner7> I am starting to think about a good point to reach out to people who "do their own crypto" and ask how they see FCMP++
<r​brunner7> Like MyMonero, or that Dart library that was recently announced
<r​brunner7> Seems a bit early still then
<r​brunner7> Well, of course the carrots are also part of the mix
<k​ayabanerve> jeffro256: it's irrelevant.
<k​ayabanerve> We'd only need it if the tree was within reorg depth.
<k​ayabanerve> Yes, that solves the penalty cost of the tree reorg'ing, but we're still left with all the existing reasons for the 10-block lock.
<j​berman> The other (probably main) issue with reorgs is that it invalidates an FCMP++ that references a tree root that's reorged out, so it's not just nodes that have to switch over to the correct chain that the 10 block lock affects
<k​ayabanerve> We don't need that complexity for something which should never get hit (and it shouldn't thanks to the 10-block lock)
<k​ayabanerve> So you did nullify the tree perf impact I raised (with complexity) but that still leaves the contagion issues currently justifying the lock.
<j​effro256> The contagion issue is opt-in though, the constructor gets to choose how far back they reference the tree root. Cue uniformity issues, but....
<r​brunner7> You mean, in simple terms, for all reorgs < 10 blocks there is no tree performance problem even with simple, straight-forward code?
<k​ayabanerve> That actually has massive issues as I've prior discussed
<k​ayabanerve> Please don't make me write a new post on that :( I spent 4h on the one for MAX_INPUTS for all the noisy people who didn't follow the meetings :(((
<r​brunner7> Well, having things nicely in one place instead of strewn over several meeting logs certainly is something ...?
<k​ayabanerve> In theory, it's not as bad. You don't actually have to reorg the tree until you hit 10 blocks. You just have to disavow certain roots *if you reorganized onto a shorter chain* until the chain is long enough those roots are 10 blocks old again.
<k​ayabanerve> But any reorg less than 10 blocks won't affect the tree state at the current block number compared to where it was on the reorged from blockchain
<k​ayabanerve> rbrunner7: You are welcome to write the next one ;)
<r​brunner7> I did things like that, e.g. about Jamtis addresses, but now this stuff all goes seriously over my head.
<j​berman> How might the PoS finality layer look @kayabanerve ? PoS layer grows the tree in shorter intervals, PoW miners aggregate the txs into the chain and respect txs with tree root refs that aren't necessarily at PoW consensus block level?
<j​effro256> Yeah, you would just need to rollback if you *added* another block on top of that rollback that was different than what you had after it
<k​ayabanerve> No?
<k​ayabanerve> You need to reorg the queue, not the tree itself.
<k​ayabanerve> We only accumulate whatever is 10 blocks old.
<j​effro256> I'm assuming we're in a scenario where we support 1-block-lock default
<k​ayabanerve> As long as the 10-block-old block, at time of reorg from, is still on the reorged to chain, the current tree root on reorged from will appear on reorged to.
<k​ayabanerve> Oh, so we're assuming the insane, icic
<jeffro256> +1
<k​ayabanerve> :p
<k​ayabanerve> Jokes aside, if we had a 1-block lock, then yeah, any reorg would invalidate the current tree root assuming we actually moved to another chain.
<j​effro256> Yes, I was just commenting that a shallow tree invalidation doesn't have to impose any computational requirement besides DB read/writes if we do it right
<k​ayabanerve> If we introduce the complexity of state diffs/a versioned cache OR we keep the entire recent tree in a DB TXN and solely commit the part older than 10 blocks (regardless of the current lock setting)
<k​ayabanerve> That last one just means on reboot, nodes rebuild the tree data for the last 10 blocks
<j​effro256> I know it's a joke, but it might not be so insane given that A) FCMP largely mitigates decoy elimination attacks from reorgs B) it is being proposed that max tx input counts are being reduced and C) shallow reorg performance hits can be mitigated
<r​brunner7> Ah, something that I understand, "complexity". Please no :)
<sneedlewoods> +1
<jeffro256> +1
<k​ayabanerve> jeffro256: The invalidation of my newly noted commentary on tree perf, which can be worked around with more intelligent tree management, still leaves all existing issues.
<j​effro256> The complexity for value here is pretty low IMO. We only keep a tuple of (total_output_count, right_tree_edge) for 10 blocks in the past
<j​effro256> It's notably simpler than an actual tree trim
<k​ayabanerve> That only discards this one reason which I'm fine discarding.
<r​brunner7> I guess we can change such tree adjustment algorithms pretty easily between the hardfork to FCMP++ and the next one, or even earlier?
<k​ayabanerve> That still leaves us with all the other issues.
<r​brunner7> Thus no hurry, in a way
<k​ayabanerve> This is all an impl detail rbrunner until we actually discuss changing the lock.
<jeffro256> +1
<r​brunner7> Which maybe we shouldn't, with so much to worry already on the way to FCMP++?
<j​berman> FWIW, trimming the tree isn't such a computationally burdensome op relative to growing. With grow you have to hash potentially multiple chunks of leaves and layers above. With trim, you only do a smaller hash op on the last chunk in each layer
<k​ayabanerve> Or at all? It forces everyone to redo their TXs on even a 1-block reorg (if discussing removal).
<j​effro256> All the other issues are opt-in by wallets who should decide their own risk profile
<k​ayabanerve> jeffro claims it's opt-in. It's not really.
<k​ayabanerve> jeffro256: You should reasonably assume every wallet will immediately enable this to resolve user complaints of the 10-block lock.
<k​ayabanerve> And users cannot be assumed to have an educated opinion on this setting.
<rbrunner7> +1
<k​ayabanerve> Anyone who does have an educated opinion and chooses to re-enable the lock per their preference will immediately be segmented into a new privacy pool.
<k​ayabanerve> If wallets try to be clever and most recent tree for outputs which need it, stable tree for outputs which can use stable, we're just reintroducing the idea that we should have dedicated TXs for the most recent 10 blocks.
<k​ayabanerve> Opt-in TXs with a contagion risk in their own explicit privacy pool.
<k​ayabanerve> We effectively shot down that idea.
<k​ayabanerve> Removing the 10-block lock implicitly has the same effect.
<k​ayabanerve> It also makes us vulnerable as hell to DoSs by anyone who decides to on purposely do 1-block reorgs just to force users to redo their interactions. Yes, users can 'opt-out', effectively splitting the privacy pool of users, but I'm not looking forward to those user complaints and that being the new UX scapegoat.
<k​ayabanerve> Not to mention 1-block reorgs may be sufficiently cheap this entire feature can be nullified in practice and then we're just left with the hell of it. I'd have to re-visit Rucknium's analysis and see how often they naturally occur.
<o​frnxmr> 1 block reorgs happen multiple times per week
<k​ayabanerve> And then wallets can choose a 5-block lock as their safety window? But then it's uniformity issues + effectively just a lock reduction when we also effectively shot down *that* idea a few weeks ago.
<r​brunner7> Yeah, Rucknium 's analysis was quite a bit depressing how cheap it would be to buy / rent hashpower and force us into 3 block, 4 block, 5 block reorgs ...
<o​frnxmr> not tooo many, and it depends on your node config
<o​frnxmr> Nodes with more connections typically reorg more than those with less
<k​ayabanerve> Add a finality layer or suck it up. Don't remove the lock D: 
<k​ayabanerve> ^ that's my stance on it all
<r​brunner7> But anyway, I am a bit surprised that anybody would be ready to put the lock question on top of a veritable mountain of work for implementing FCMP++
<j​berman> @kayabanerve ^ how would that finality layer look?
<k​ayabanerve> Oh, sorry, I missed that
<k​ayabanerve> PoS validators run a BFT algorithm to finalize block proposals. PoW blocks are now solely proposals.
<k​ayabanerve> Nodes only build on top of the finalized blocks.
<r​brunner7> What means *PoS* here? I am lacking context
<k​ayabanerve> Stake
<r​brunner7> Is this a thought experiment?
<k​ayabanerve> I sketched a system where the most recent PoW miners earn points in an opt-in second layer but the security on it was hell.
<k​ayabanerve> It's not a discussion I see viable given the Monero community but it is the actual solution to the 10-block lock.
<ofrnxmr> +1
<k​ayabanerve> I always bring it up so more people are willing to listen/ack it as a possible solution so that someday it may be a viable discussion.
<r​brunner7> That sounds like a dangerous statement :)
<ofrnxmr> +1
<k​ayabanerve> I did not find this even secure enough to open the issue discussing the concept.
<k​ayabanerve> Rbrunner7: Feel free to make today the day it's discussed
<j​effro256> I think it's not unreasonable to teach users "the use of this setting will often cause transaction failures. Don't use this if you aren't willing to resign the transaction".
<j​effro256> > Anyone who does have an educated opinion and chooses to re-enable the lock per their preference will immediately be segmented into a new privacy pool.
<j​effro256> There are ways to mitigate this, the choice doesn't necessarily have to be 1 OR 10 for all transactions that one user does. Any single user might do some 1 block old txs and some 10 block old txs. A wallet can also randomly choose something between 1-10 or whatever scheme you'd like to come up with. So I wouldn't necessarily call it different privacy pools because there will be la<clipped mess
<j​effro256> rge overlap. But also, it's a user's choice to opt-in into this separate privacy pool anyways.
<j​effro256> > But anyway, I am a bit surprised that anybody would be ready to put the lock question on top of a veritable mountain of work for implementing FCMP++
<j​effro256> To be clear, I'm not advocating for a reduction/removal now, but I am always looking for pathways to remove the lock, as I have seen it impact real-world payments.
<k​ayabanerve> But unless you want to do so, I stand by my dismissal of it as a discussion viable to have for today :p
<r​brunner7> Better not. I think what we don't need are people getting false hopes from skimming the meeting log, maybe with even less understanding of complexities than myself
<k​ayabanerve> jeffro256: that's just reinventing the decoy selection algorithm with more steps
<j​effro256> Also I just wanted to pushback on the point that allowing a 1-block-lock would *necessarily* cause slowdowns for shallow reorgs
<k​ayabanerve> :p
<k​ayabanerve> Monero: finally removes the DSA
<k​ayabanerve> jeffro256: but what if we added a DSA
<r​brunner7> DSA?
<j​effro256> decoy selection algo
<k​ayabanerve> Decoy selection algorithm
<r​brunner7> Ah, of course
<k​ayabanerve> jeffro256 is right we technically can remove the lock, say HF, make it the wild west
<k​ayabanerve> But the DSA always had fundamental issues and I'm trying to point out this will also have a ton of issues for privacy
<k​ayabanerve> We shouldn't re-enable chain analysis in this way and give Rucknium a new TX property to track
<j​effro256> Secretly I want job security for Rucknium.....
<k​ayabanerve> (limited chain analysis ofc, the wallet used by the user most likely)
<r​brunner7> That mystical second layer would run with decoys? I am just guessing now :)
<k​ayabanerve> Wait that's a good argument jeffro
<k​ayabanerve> I'm convinced /s
<j​berman> I generally agree with kayaba that the ideal direction should be toward maximizing uniformity to maximize privacy and also agree this proposal runs counter to that
<k​ayabanerve> No, rbrunner7, sorry, two separate discussions
<k​ayabanerve> Removing the 10-block lock to 'solve' it effectively restores DSA-level bs.
<r​brunner7> Ok
<j​berman> I'm curious to hear more on the hypothetical PoS system design
<j​effro256> But only for people who opt-in ...... ;)
<k​ayabanerve> Just as now you select decoys in ring signatures, removing the lock has you select which tree to use with whatever algorithm and privacy impacts.
<k​ayabanerve> It in practice would reveal what user group you belong to.
<j​berman> I'm wondering if there is a way to design a PoS validation layer such that the security of the system is still completely dependent on PoW, but PoS can help establish a "secure enough" way to do faster txs and that's it. aka still always enable fallback to PoW
<j​berman> In that way PoS wouldn't be used for finality as I understand it, but would be used to establish a baseline level of security users are content to rely on to spend faster than 10 blocks
<k​ayabanerve> Which may be as fine-grained as using specific atomic swap software or as widely-grained as 'n00b'.
<k​ayabanerve> The proper solution to the 10-block lock isn't to remove it. It's to alternatively solve the issues it solves.
<k​ayabanerve> My only answer for that is a PoS finality layer.
<r​brunner7> Does sound very interesting - as a long-term goal, I would assume
<k​ayabanerve> jberman: My opt-in sketch didn't achieve meaningful security, but it was only active so long as validators were online and a majority of hashpower. If that property failed, it deactivated.
<k​ayabanerve> The issue is it just allows exchanges to faster handle TXs. Having it remove the lock would require tightly coupling it and not being opt-in.
<k​ayabanerve> Some designs still be able to fallback on PoW and the existing 10-block lock?
<r​brunner7> I guess it's also possible one day somebody comes up with a novel and very, very good solution for that problem
<k​ayabanerve> But that'll really complicate the security analysis.
<k​ayabanerve> Also, awarding stake to miners has unclear practice w.r.t. p2pool
<k​ayabanerve> I have no idea how p2pool would vote in the finality layer.
<k​ayabanerve> And having prior mined blocks doesn't equal weight in the game so that screws over the security analysis. You'd have to hold the block reward hostage or note that historic miners can just equivocate and partition the network at no cost
<k​ayabanerve> It's a very long discussion with a lot of rabbit holes :/
<r​brunner7> Ok, we are nearing the full hour. Is there anything else we need to touch in this meeting?
<j​berman> Ya, generally agree it's hard to see introducing PoS as an actually viable option, but it's an interesting thought experiment
<r​brunner7> Doesn't look like it. Allow me to close the meeting, of course continue discussions, thanks for attending, read you again next week!
<k​ayabanerve> And that's why I haven't spent 4 hours writing a post on it :D
<s​needlewoods> thanks everyone, cu
<r​brunner7> We need a secretary for you, kayabanerve
<k​ayabanerve> I nominate jeffro256
<r​brunner7> You do know that documentation is underrated, right? :)
<k​ayabanerve> Just already know everything /s
````


# Action History
- Created by: rbrunner7 | 2024-11-22T18:21:25+00:00
- Closed at: 2024-11-25T19:10:59+00:00
