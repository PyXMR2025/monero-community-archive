---
title: 'Seraphis wallet workgroup meeting #66 - Monday, 2024-04-15, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/990
author: rbrunner7
assignees: []
labels: []
created_at: '2024-04-12T16:38:48+00:00'
updated_at: '2024-04-15T19:25:45+00:00'
type: issue
status: closed
closed_at: '2024-04-15T19:25:45+00:00'
---

# Original Description
On Monday, November 14 2022, we started with regular weekly meetings of the Seraphis wallet workgroup, and all interested parties from the community that want to join. Time is 18:00 UTC on each Monday. "Location" is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting here: https://github.com/monero-project/meta/issues/987

# Discussion History
## rbrunner7 | 2024-04-15T19:25:45+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/990
<SNeedlewoods> hello there
<d​angerousfreedom> Hello
<jberman> howdy
<r​brunner7> Same possible problem with people on matrix.org still applies, as far as I know
<k​ayabanerve> waves
<s​yntheticbird> I confirm. Messages are delayed on matrix.org side
<r​brunner7> Ok. What are the reports from last week?
<SNeedlewoods> Made another PR https://github.com/UkoeHB/monero/pull/43 and have relatively high hopes it's already ready for review.
<jeffro256> +1
<jeffro256> Kayabanerve: In your proposal, you say that "Seraphis offers much more efficient FCMPs". Is this because a) we assume we do a "pure" curve cycle (perhaps tevone instead of helios/selene), b) our first
<k​ayabanerve> It's due to doing less DLog proofs and having a better cycle.
<SNeedlewoods> I haven't done anything on the `LegacyEnoteOriginContext` PR, because of jeffro's comment from last Tuesday, AFAIU it may become obsolete, which even though I spent a lot of time on it, I'd support just treating `enote_ledger_index` more flexible, if that reduces the 1500 lines of code I added. But I have to admit, I'm still bad at visualizing all the consequences without having it in code form t
<r​brunner7> SNeedlewoods: Looks like a lot of code, that new PR #43
<jberman> me: finished up benchmarks on the async scanner thanks to gingeropolous (I observed 50-60% faster scanning pointing to ginger's remote node over clearnet), going to explore replacing wallet2 this week and do PR review
<dangerousfreedom> +1
<SNeedlewoods> +1
<SNeedlewoods> I also got a little deeper into the async scanner, especially functional tests. Even though I think I won't be able to do a full review, from what I've seen so far it's well organized, written and thought through.
<d​angerousfreedom> I started the review of jberman's scanner and started figuring out what we can do to write seraphis txs/enotes on the lmdb with jeffro. He will lead the way there and I will try to help. Maybe we can discuss it today. I also started to write a book about Money, Monero and privacy. Hopefully I will finish and publish someday :p
<SNeedlewoods> rbrunner that's mostly tests
<r​brunner7> Ah, ok
<r​brunner7> dangerousfreedom: A book, really? Wow.
<r​brunner7> I hope you know what you are getting yourself into :)
<d​angerousfreedom> Haha yeah, I took some time out of coding to look at the big picture this week and thought that it would be a nice idea haha I have no experience with that though. Lets see :p
<SNeedlewoods> interested to see that book, not that I don't have enough reading to do already
<r​brunner7> jeffro256 seems to be active also on the theory side ...
<j​effro256> I've been reviewing kayabanerve 's FCMP+SA+L proposal and just trying to weight different engineering costs/benefits against Seraphis
<k​ayabanerve> @jeffro256 and I talked and ended up with a question to ask. What would everyone here personally estimate the academic leg work, and PR to merge Seraphis into Monero, be ready by? Koe, prior, in an estimate I don't want to solely rely on, said 3-5y.
<k​ayabanerve> @jberman had a distinct estimate if they'd like to repeat it (I'd have to pull up what it was)
<jberman> Seraphis with FCMP's 3y, without 2y
<k​ayabanerve> And then @jeffro256 their own, so I'd personally like to evaluate this.
<d​angerousfreedom> SNeedlewoods: Looks nice. I will look it deeper this week.
<sneedlewoods> +1
<r​brunner7> jberman's estimate of 2 years and 3 years respectively until the "hot" hardfork to the new tech sounds reasonable to me as well.
<r​brunner7> Maybe 1 year more is a bit much if much prior work went into current tech plus FCMP first
<j​effro256> As I've told kayabanerve , I am personally of the opinion that it won't take 3 years (obv up for debate). I also don't think we can do FCMPs in any form whatsoever within 1 year, simply because infra inside Monero core is hellish. For example, updating a RW-lock within the blockchain code is taking months of review
<d​angerousfreedom> I think we can be on testnet by the end of the year. Then one more year testing and trying to let no wallet behind :p
<k​ayabanerve> That's why I asked for time to PR, not time till activation.
<r​brunner7> But well, where do you see the importance of such estimates?
<r​brunner7> I am a bit suspicious there.
<j​effro256> The importance of these estimates determine whether or not the community wants to go for the quick and dirty FCMP upgrade on RingCT right now, or wait until Seraphis to do it
<r​brunner7> Well, that's more of a psychological question. My interpretation was, yes of course people want FCMPs *as fast as possible* because they worry
<k​ayabanerve> For every year estimated, I plan to curse the community with one more year of drama over irrelevant bs
<jeffro256> +1
<rbrunner7> +1
<k​ayabanerve> :p No, it's as jeffro said.
<k​ayabanerve> My proposal for RingCT + FCMPs only makes practical sense if they lead Seraphis by 6m+.
<r​brunner7> I think it's quite dangerous to rely on estimates for pretty much everything, much less important decisions, IMHO. They are just too bad for that.
<k​ayabanerve> Accordingly, we need an estimate if both time till Seraphis and time till FCMPs, and to confirm the delta.
<k​ayabanerve> I'd also note my dropping RingCT+FCMPs would be for Seraphis+FCMPs. The fact those have an extra year estimated further cements my personal opinion :/
<j​effro256> And I fundamentally disagree with this stance, since I *don't* think FCMPs are the most important upgrade for the future of Monero, but that's subjective
<r​brunner7> The MRL meeting was "fire and flame" for FCMPs *right* now, no?
<k​ayabanerve> Yes and then @jeffro256 tanked my CCS D:
<jberman> fwiw I'd argue updating the RW-lock is significantly more complex than the daemon-side infra code for FCMP's (ignoring the crypto)
<r​brunner7> Huh? Tanked your CCS?
<jberman> The RW-lock is a significant change to the internals of the daemon, but the code for FCMP's can be mainly additional and distinct call paths that still leans on most of the existing internal infra
<k​ayabanerve> (they didn't attend the MRL meeting and then said during CCS review the timeline wasn't justified :p )
<r​brunner7> Yeah, that particular timeline of events was a bit unfortunate ...
<j​effro256> Yeah that's on me. I regret missing that MRL
<k​ayabanerve> It's a fair comment that the timeline must be justified. Because jeffro has reopened this discussion, I'm here to re-have this discussion. Multiple people respect jeffro256's opinion and want it discussed.
<k​ayabanerve> I wanted this CCS due to personally believing it'd be more expedient. Jeffro256 is correct we need to actually largely agree it is. If everyone else was satisfied at MRL, and jeffro is now satisfied, that may be everyone.
<r​brunner7> Well, we probably have quite a different "group dynamic" here, in contrast to the broad MRL meeting, being focussed on Seraphis and Jamtis
<k​ayabanerve> Hence me asking everyone's opinion on Seraphis timelines. I have no interest in further drawing it out.
<j​effro256> And to be fair, I'm not against *most* of the CCS if it's true as kayabanerve said that most of the work carries over to Seraphis, I just haven't been convinced yet that the move to FCMPs on RingCT is the best move for the network at the moment
<d​angerousfreedom> But anyway kayabanerve , is there any big difference implementing FCMP into serpahis or the current monero code? I guess the real bulk of the work is on doing the job properly in C++, right? Integration would be the easiest part I guess
<k​ayabanerve> Apologies if I already have drawn it out too much.
<k​ayabanerve> We can shift this to the next MRL.
<k​ayabanerve> I'll also note while Seraphis is the clean, functional design, Seraphis with Grootle brings neither FCMPs nor F-S. I care about both, and I'll settle for one ASAP. RingCT + FCMPs is the former ASAP.
<r​brunner7> Well, if I could freely wish, I would do Seraphis plus FCMPs *together*, but I go with consensus without complaining too loudly.
<j​effro256> I asked this question because it we *DON'T* switch to a pure curve cycle with Seraphis, and stick with using the helios/selene tower cycle, how much efficiency will we lose in the long run?
<k​ayabanerve> The tree, if properly coded, would carry.
<k​ayabanerve> The GBP/divisor/gadgets carry.
<k​ayabanerve> The first layer of the circuit, and the curves used, would be different. If RingCT+FCMPs is performant enough with tevador's recent creation, we may? Not need to move curves with Seraphis. That needs more R to evaluate, and real world inspection.
<k​ayabanerve> Doing FCMPs first effectively forces Seraphis+FCMPs IMO. I don't see how we justify a downgrade.
<r​brunner7> > That needs more R to evaluate, and real world inspection.
<r​brunner7> Sounds like a reason to wait with final decisions?
<j​effro256> B/c if we can do mixed pre-Seraphis and Seraphis reference sets, and use helios/selene for some perf loss at the privacy gain of no hard enote migration, I think we should do that mainly for the privacy concerns. But also, it *would* make dev time shorter
<k​ayabanerve> I'd agree it'd be optimal to do them together and first. Seraphis has become the larger bottleneck.
<k​ayabanerve> *Once I impl and testnet RingCT FCMPs is when we'd have the info need to eval that*
<k​ayabanerve> We can't say if Helios/Selene remove the need (and make solely preferable) to curve cycle with Seraphis until we have implementations of them and the proofs actually being benched.
<r​brunner7> My take would be to *not* put FCMPs first into current Monero, for what it's worth.
<kaybaynerve> > jeffro256: B/c if we can do mixed pre-Seraphis and Seraphis reference sets, and use helios/selene for some perf loss at the privacy gain of no hard enote migration, I think we should do that mainly for the privacy concerns ...
<k​ayabanerve> It, honestly, has super weird effects. It may have no impact at all, other than being less preferable, or it could screw over some future designs.
<r​brunner7> But that was a decidedly minority opinion at least in that fateful MRL meeting
<j​effro256> jberman: If it's not too much trouble, would you mind roughly explaining the 3year with FCMP timelime estimate?
<kayabanerve> > rbrunner7: My take would be to not put FCMPs first into current Monero, for what it's worth.
<k​ayabanerve> Even if FCMPs were ready a year before Seraphis?
<d​angerousfreedom> What do you mean by 'the curves would be different' under the current monero code or seraphis?
<r​brunner7> They probably won't be if we put most of dev capacity into Seraphis and Jamtis, with jberman also working on that more or less fulltime ...
<r​brunner7> But maybe that opinion is unfouned
<r​brunner7> *unfounded
<r​brunner7> if most work carries over anyway, as you seem to assume
<k​ayabanerve> Helios/Selene, if implemented and evaluated, may be performant enough they remove the justification to move curves.
<k​ayabanerve> I don't know. We haven't implemented them because we only would if RingCT+FCMPs.
<j​effro256> jberman: responding to the rw lock comment, I disagree. Even without crypto code, the FCMP code must add tables to LMDB, functions to fetch that data, logic to add/pop data w/ blocks, tx validation logic in `Blockchain`, RPC code in `core_rpc_server`, logic in `wallet2` to fetch paths, code in `cryptonote_basic` to construct these proofs, etc. The RW lock simply replaces the epee <clipped mess
<j​effro256> critical section with extra semantics that need to be verified
<kayabanerve> > rbrunner: if most work carries over anyway, as you seem to assume
<k​ayabanerve> Probably 80%.
<k​ayabanerve> Probable ixnay on Helios/Selene, GSPs (paper linked above), and the first layer (composition of gadgets we'd reuse).
<k​ayabanerve> Though Seraphis should independently use a GSP for the composition AFAICT. They can open the enote and prove the linking tag a bit more efficient than current, and are already proven.
<k​ayabanerve> But that's a minor improvement which doesn't need to be insisted upon.
<jberman> I think FCMP's can be coded within 6 months (FCMP's slot in pretty neatly into Seraphis). Academic theory work can happen in parallel within the 6mo - 1y. Review/auditing I think could be completed in the 4-6mo after coding is done 
<r​brunner7> slot into *Seraphis* you mean, right?
<r​brunner7> For the 6 months I mean
<k​ayabanerve> j-berman: We could probably start auditing GBPs within a month of starting the schedule I laid out.
<k​ayabanerve> Both the theory and audits are parallelized.
<jberman> ya that's explaining my 3y FCMP estimate with Seraphis (2y for Seraphis + 6mo for coding + 6mo for review/audit = 3y)
<jberman> ok I'm referring to 6mo for review/audit of the final implementation
<r​brunner7> I think there would be quite some parallelization potential there, to bring it down a bit, maybe half a year
<r​brunner7> Ah, ok, final "total" audit
<jberman> "the FCMP code must add tables to LMDB, functions to fetch that data, logic to add/pop data w/ blocks, tx validation logic in `Blockchain`, RPC code in `core_rpc_server`, logic in `wallet2` to fetch paths, code in `cryptonote_basic` to construct these proofs" I still think the infra is mostly reusable here, except maybe the fetching paths part
<r​brunner7> I still see something like a catch-22, at least to some degree: If we go with FCMPs for current Monero tech, it will arrive quite a bit faster than Seraphis, but at least in part just *because* it's done first.
<r​brunner7> Or, if everybody would shoot at Seraphis and FCMPs as fast as possible, mostly everything could arrive at the same time
<k​ayabanerve> If it makes you feel better, I am the sole dev on FCMPs as cryptography and I won't work on Seraphis regardless <3
<r​brunner7> Oh, I feel pretty good, no problem :)
<k​ayabanerve> (I say that to tease, but truly, integrating Seraphis into Monero isn't my skill set nor interest)
<xFFFC0000> ( late to the meeting, reading what have been discussed so far ) 
<r​brunner7> I mean FCMPs really fast also has solid advantages
<jberman> personally I'm of the view that FCMP's should be top priority and I still think it's fine if we have parallel development tracks on this front
<k​ayabanerve> So my work on FCMPs isn't taking from Seraphis.
<k​ayabanerve> It's my proposed theft of jberman which somewhat does (swaths of reuse).
<k​ayabanerve> Distinctly, does anyone else have other topics? If so, we should table the rest of this topic till the next MRL IMO. I do not want to control this talk.
<r​brunner7> Yeah, my darkest fear - losing almost the whole crew to a FCMPs now craze - did not materialize
<d​angerousfreedom> Wouldnt it be safer then to explore this option anyway? If we dont need to introduce a new curve to the Monero codebase, that would be better and easier to integrate, right? How hard would it be to change curves if we find something better later?
<jeffro256> > rbrunner7: Or, if everybody would shoot at Seraphis and FCMPs as fast as possible, mostly everything could arrive at the same time
<j​effro256> This is kind of the point that I've been trying to get across. Seraphis integration has not had the resources allocated to it that the FCMP on RingCT proposal has, so it sort of (in my opinion) misdirects where we should be putting in capital. If we want FCMPs faster AND we assume we want Seraphis, then we should be merging these efforts to get it done together. Because if Seraphi<clipped mess
<j​effro256> s integration had the same manpower, it might be moving faster, if that makes sense
<k​ayabanerve> It'd take months and would still add two curves. It just doesn't remove Ed25519 from the active protocol.
<j​effro256> (If we don't assume that we want Seraphis, then that's an entire other story)
<k​ayabanerve> It's less work now for more trouble later. That more trouble is just either 0.1, near 0, or 100, quite fucked.
<r​brunner7> The whole situation is as clear as mud right now, IMHO. We would do well by letting things develop for some time, and come back to the discussion again, more than once if needed
<o​ne-horse-wagon> Could Koe be enticed to help out on Seraphis full time?
<jberman> "the FCMP code must add tables to LMDB, functions to fetch that data, logic to add/pop data w/ blocks, tx validation logic in `Blockchain`, RPC code in `core_rpc_server`, logic in `wallet2` to fetch paths, code in `cryptonote_basic` to construct these proofs" I think we should be able to at least agree that most of this code should absolutely be
<jberman> reusable for Seraphis + FCMP's, except obviously the wallet2 part
<k​ayabanerve> There has been no resources to RingCT+FCMPs, or as I have taken to calling it, RingCT/FCMPs, where FCMPs are one part of a complete privacy protocol.
<k​ayabanerve> There has been proposed resource allocation.
<d​angerousfreedom> I see more advantages with Seraphis and Jamtis than with FCMP also. Having view-keys that shows the correct balance, easier multi-sig and tx chaining are much more desired features for me than FCMP IMO.
<k​ayabanerve> I have not taken any resources towards this. I have put in a few days of thoughts. I have taken a few meetings. I have made two CCSs.
<k​ayabanerve> Squashing my CCSs does not free a developer team for Seraphis. The currenf Seraphis development would continue.
<k​ayabanerve> My CCS do not explicitly take from Seraphis development. Practically, they step on Seraphis's toes and take jberman.
<k​ayabanerve> To argue we could do Seraphis on the FCMP timeline if RingCT+FCMPs is dropped is to argue... jberman hasn't been working on Seraphis and now would? I guess?
<j​effro256> Right, I meant the future resources you proposed to be allocated to that goal of RingCT/FCMPs. Seraphis integration has *not* had those resources. People want Seraphis to happen faster. So it makes sense to me if people a) want Seraphis, b) want FCMPs, c) Seraphis integration isn't happening fast enough for their liking, d) have the resources to make extensive protocol changes/R&D<clipped mess
<j​effro256>  happen right now, then -> they should allocate those resources to Seraphis integration
<kayabanerve> > dangerousfreedom@dangerousfreedom: I see more advantages with Seraphis and Jamtis than with FCMP also. Having view-keys that shows the correct balance, easier multi-sig and tx chaining are much more desired features for me than FCMP IMO.
<k​ayabanerve> ... bad time to say FCMPs+RingCT technically does all of those?
<k​ayabanerve> It's feature complete with Seraphis except forward secrecy.
<k​ayabanerve> Very fair clarification @jeffro256.
<k​ayabanerve> I'm not convinced F-S is impossible but it's annoying af and likely can't be done anywhere near as nicely as Seraphis. I'e dropped it for now.
<d​angerousfreedom> How you see the correct balance with your view key without Jamtis?
<j​effro256> Well you would need Jamtis on RingCT
<r​brunner7> Yeah, that's a whole new wildcard that you throw into the right, that maybe, just maybe, we have a better Seraphis than Seraphis, in a way
<k​ayabanerve> It enables redefining the output key so that key images are a private key, not the private key. Read the gist.
<k​ayabanerve> No, same addresses.
<k​ayabanerve> *same address protocol, not same addresses. Wallets would make new ones indistinguishable.
<j​effro256> sorry ur right
<kayabanerve> > rbrunner7: Yeah, that's a whole new wildcard that you throw into the right, that maybe, just maybe, we have a better Seraphis than Seraphis, in a way
<k​ayabanerve> No. It's not. It doesn't have F-S.
<j​effro256> You still need Jamtis for other features
<k​ayabanerve> Jamtis for Janus and view tag key.
<j​effro256> and no subaddress lookahead
<j​effro256> IIRC
<k​ayabanerve> Yep
<j​effro256> and curve25519 DH
<r​brunner7> If we have such a hard time to decide between two possible ways forward, maybe not the best idea to come up with a third, unless that pure *genius*
<k​ayabanerve> If F-S is solved, maybe. I wrote a Pythom script with a DLog oracle and showed for a random output, you can extract solutions for everything except the last variable which only has a single valid opening (the actual output) :/
<dangerousfreedom> > kayabanerve: *same address protocol, not same addresses. Wallets would make new ones indistinguishable.
<d​angerousfreedom> Well, I'm interested now. Show me the derivation path to see my full balance only with my view-key using the current protocol or with your proposed changes.
<d​angerousfreedom> :)
<r​brunner7> I said it before, those cryptographers are very dangerous, they come up with new stuff at rates that are simply too fast
<k​ayabanerve> Tbf, if F-S was cracked, it'd be Seraphis without the new pool, without forcing new addresses, and incrementally mergeable.
<k​ayabanerve> FCMPs
<k​ayabanerve> Then same address protocol, yet generating with OVKs and F-S
<k​ayabanerve> Then a new address protocol if still desired
<k​ayabanerve> Then a new TX version to eliminate TX extra, etc
<k​ayabanerve> But F-S wasn't cracked and I am not actively working on it. Seraphis clearly has F-S. Since F-S is a requirement, we should drop this for now, as tevador said.
<r​brunner7> Who made that wonderful example with the interstellar ship that never starts?
<k​ayabanerve> dangerousfreedom: Read the gist :p
<jberman> @dangerousfreedom: https://gist.github.com/kayabaNerve/0e1f7719e5797c826b87249f21ab6f86?permalink_comment_id=5014753#gistcomment-5014753
<k​ayabanerve> Regardless of any of the three paths, FCMPs are desired. The current CCSs have ~80% overlap regardless. It sounds like we agree they could be a year faster.
<k​ayabanerve> That leaves the discussion should I purge that 20% and should Seraphis get in on this. That requires a plan for Seraphis to so scale.
<k​ayabanerve> I do not claim to be able to postulate that plan. I'd defer to rbrunner, the effective expert here, and jeffro256, who asked that question in the first place.
<r​brunner7> If it really is a realistic scenario that we only "lose" jberman  to FCMPs, that does not sound too bad indeed.
<k​ayabanerve> I don't believe that we can throw money at Seraphis. It sounds like a developer manpower issue, and developers can't immediately integrate :/
<r​brunner7> Hard to say what happens if work turns out to be significantly bigger or difficult than estimated however ...
<k​ayabanerve> That's what the third CCS is for, the cloning vats.
<jeffro256> +1
<k​ayabanerve> (overlaps with Seraphis)
<r​brunner7> Yes, of course you can't conjure up manpower. But as I said, it has a psychological component, that manpower could, in theory, get "sucked" into FCMPs
<r​brunner7> Does not look like that, mostly, right now
<kayabanerve> +1
<d​angerousfreedom> Damn! You guys are fast! I missed two weeks of discussions and everything changed :p
<d​angerousfreedom> I will try to catch up.
<r​brunner7> There, I said it. They never sleep, those cryptographers.
<r​brunner7> Well, we are nearing the hour mark, and I don't think that *this* particular discussion will lead to any hard decisions anyway. It was of course very useful nevertheless, at least IMHO.
<r​brunner7> Can people agree with letting things stand where they are right now, and close this meeting? Things will then continue maybe in 2 days already
<r​brunner7> In the MRL meeting
<k​ayabanerve> Sorry for so aggressively side tracking. It does sound like there's a bit more clarity/consensus.
<SNeedlewoods> thanks everyone, appreciate the discussion and big brain power that goes into this
<r​brunner7> For me really nothing to be sorry about. If we don't reach a solid consensus, we will probably run into serious trouble sooner or later
<jberman> I'm good with closing the meeting, thanks :)
<r​brunner7> Thanks for attending, interesting times indeed. Read you again here in 1 week.
<j​effro256> Thanks all !
````


# Action History
- Created by: rbrunner7 | 2024-04-12T16:38:48+00:00
- Closed at: 2024-04-15T19:25:45+00:00
