---
title: Monero Research Lab Meeting - Wed 27 November 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1116
author: Rucknium
assignees: []
labels: []
created_at: '2024-11-27T16:29:26+00:00'
updated_at: '2024-12-10T20:42:29+00:00'
type: issue
status: closed
closed_at: '2024-12-10T20:42:28+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

4. [Carrot audit](https://github.com/cypherstack/carrot-audit/releases/download/final/Carrot-final.pdf).

5. Proposed Cypher Stack review of ["On the Use of Logarithmic Derivatives in Eagen’s Proof of Sums of Points"](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449#note_27273).

6. [Discussion: preventing P2P proxy nodes](https://github.com/monero-project/research-lab/issues/126).

7. Making transaction weight a function of number of inputs, outputs, and `tx_extra` length instead of number of bytes.

8. [FCMP++ tx size and compute cost](https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898) and [MAX_INPUTS/MAX_OUTPUTS](https://github.com/monero-project/research-lab/issues/100#issuecomment-2433524326). [On MAX_INPUTS and MAX_OUTPUTS](https://gist.github.com/kayabaNerve/dbbadf1f2b0f4e04732fc5ac559745b7). [Monero FCMP MAX_INPUTS/MAX_OUTPUTS empirical analysis](https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6).

9. Any other business

10. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1112

# Discussion History
## Rucknium | 2024-12-03T21:16:12+00:00
Logs:

> __< k​ayabanerve:matrix.org >__ I just got the quote from Cypher Stack for 70 XMR to review the latest work output by Veridise. I support that and jberman has also signed off.     

> __< k​ayabanerve:matrix.org >__ I've also requested the next quote from Veridise for the final step of work regarding divisors and will go from there on that. The last discussion to further contract Veridise noted we were splitting the remaining work into two segments and only approving the first segment at the time.     

> __< s​gp_:monero.social >__ Certainly interesting that the review is twice as much as the work output itself     

> __< r​ucknium:monero.social >__ Do you want me to put that on today's MRL agenda?     

> __< a​rticmine:monero.social >__ I will not be able to attend the MRL meeting today. Sorry.     

> __< a​rticmine:monero.social >__ I am currently working on the scaling document.      

> __< a​rticmine:monero.social >__ It will be based on the max 8 inputs and outputs, min 1 input and min 2 outputs specifications.     

> __< o​frnxmr:monero.social >__ I don't want to ddos mrl meeting, but i want to clarify that feel we could do with a MAX_OUTPUTS of 2 and fix inputs to 2, 16*, 64* (* = debatable. But 8 is too low for a max)     

> __< a​rticmine:monero.social >__ With respect to wallet maintenance I am strongly advocating for 100% clawback on the non power of 2 inputs and outputs. So 3 will have the same weight as 4 and 5, 6 and 7 will have the same weight as 8. This is applies independently to both inputs and outputs     

> __< a​rticmine:monero.social >__ This breaks FCMP++, since we cannot have dummy inputs. I will also break scaling     

> __< a​rticmine:monero.social >__ It will break scaling because of the very large transaction weights     

> __< a​rticmine:monero.social >__ My proposal of 100% clawbacks will provide a powerful economic incentive for ongoing wallet maintenance to mitigate the impact of the max 8 inputs and outputs.     

> __< k​ayabanerve:matrix.org >__ sgp_: The person who prior did the review left, so we have a bit of a loss in continuity unfortunately. I feel that's reflected in pricing.     

> __< k​ayabanerve:matrix.org >__ Rucknium: Yes, though it is last minute, sorry.     

> __< r​ucknium:monero.social >__ MRL meeting in this room in one and a half hours.     

> __< o​frnxmr:monero.social >__ So inputs are 1-8? (1-2-3-4-5-6-7-8 are all options?)     

> __< o​frnxmr:monero.social >__ What are the weights in layman's terms? I really don't understand how a 2/2 would compare to a 64/2 or an 8/8     

> __< sech1 >__ https://gist.github.com/kayabaNerve/dbbadf1f2b0f4e04732fc5ac559745b7 says "15 ms" per one input. I assume it's the reference implementation and it's not the fastest possible.     

> __< k​ayabanerve:matrix.org >__ sech1: Give me an optimized Helios/Selene and we ideally save ~50%.     

> __< sech1 >__ I can do it (no jokes). I need to see the reference code, estimate what can be improved and allocate my time to do it.     

> __< k​ayabanerve:matrix.org >__ sech1 https://github.com/kayabaNerve/fcmp-plus-plus/tree/develop/crypto/helioselene     

> __< k​ayabanerve:matrix.org >__ It's replacing the generic arithmetic with a tailored implementation. The Crandall primes have a fast reduction we don't use at all.     

> __< k​ayabanerve:matrix.org >__ I'm pretty sure the non-platforn-specific field arithmetic in Ed25519 is roughly twice as fast though I'd have to redo my benchmarks to double check. It may be the entire lib is roughly so fast and part of that would be the Twisted Edwards curve formulas.     

> __< k​ayabanerve:matrix.org >__ There also may be some room to reduce the amount of allocations we do. If you want to get cursed and optimize to the limit, we generate the matrices per-proof. While the matrices do change with every proof, a large portion of them are consistent. I believe a single set of matrices cloned, then selectively populated with the variables, would also be faster. It's just a lot messier <clipped message     

> __< k​ayabanerve:matrix.org >__ and difficult to audit so it doesn't have my endorsement for the reference implementation.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1116     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< s​yntheticbird:monero.social >__ hi     

> __< j​berman:matrix.org >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< r​ucknium:monero.social >__ me: Researching a response to a HackerOne vulnerability report. Updated my "Monero FCMP MAX_INPUTS/MAX_OUTPUTS empirical analysis" to include a MAX_INPUTS = 128 analysis and *fixed a mistake in the computation* therein: https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6     

> __< r​ucknium:monero.social >__ I add these two papers to moneroresearch.info in the FCMP subcategory: https://moneroresearch.info/index.php?action=list_LISTSOMERESOURCES_CORE&method=subcategoryProcess&id=1     

> __< r​ucknium:monero.social >__ Slaughter, F., Goodell, B., & Salazar, R. (2024). "An Audit of the FCMP++ Addressing Protocol: CARROT."     

> __< r​ucknium:monero.social >__ Bassa, A. (2024). "On the Use of Logarithmic Derivatives in Eagen’s Proof of Sums of Points."     

> __< k​ayabanerve:matrix.org >__ Finishing my work on the FCMP libs and trying to make clear the bounds we face.     

> __< j​berman:matrix.org >__ Me: continuing locally building the FCMP++ tree on wallet sync, it's nearing completion (most recently got initial tests passing syncing a wallet from arbitrary height n on wallet restore)     

> __< r​ucknium:monero.social >__ 3) CARROT audit/review: https://github.com/cypherstack/carrot-audit/releases/download/final/Carrot-final.pdf     

> __< r​ucknium:monero.social >__ jeffro256: Do you have comments and/or summary of this?     

> __< r​ucknium:monero.social >__ Maybe jeffro isn't available this meeting. In that case, I think we can defer discussion of this item until next week.     

> __< r​ucknium:monero.social >__ 4) Proposed Cypher Stack review of "On the Use of Logarithmic Derivatives in Eagen’s Proof of Sums of Points". https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449#note_27273     

> __< r​ucknium:monero.social >__ kayabanerve: Do you want to start with this item?     

> __< k​ayabanerve:matrix.org >__ Sure     

> __< a​ck-j:matrix.org >__ Hi     

> __< k​ayabanerve:matrix.org >__ There's not much to say beyond my messages prior to this meeting. It's review of the latest work output by Veridise. The review was prior done by Aaron Feickert @ Cypher Stack and is now being proposed to be done by F. Slaughter @ Cypher Stack, under the purview of Brandon Goodell @ Cypher Stack.     

> __< k​ayabanerve:matrix.org >__ The rate quoted is 70 XMR. Considering review of this will require familiarization with the prior associated work, I find that acceptable.     

> __< s​yntheticbird:monero.social >__ Me: Late update on the FCMP++ crate integration I haven't found the time to continue looking into it in the prior weeks and my schedule is still too tied in the future. I'm sorry but if someone want to take over the branch he is more than welcome.     

> __< r​ucknium:monero.social >__ Anything noteworthy in the new Veridise document?     

> __< k​ayabanerve:matrix.org >__ Proven security of the technique as we apply it, though the security of our application is the next (and final) step of work on this topic and is still being quoted.     

> __< k​ayabanerve:matrix.org >__ This follows from the prior MRL meeting which contracted this work output. We decided to split the quote due to ongoing discussions over this latter part.     

> __< 0​xfffc:monero.social >__ ( my apologies everyone. I am on the road. So I am not going to be able to be online. My update is mostly PRs I have submitted past week. Fixing few minor issues. For next week I will spend most of my time on a optimization that I think will benefit monero-wallet-rpc ).     

> __< r​ucknium:monero.social >__ What is the reason for reviewing this part now, compared to waiting until we have a larger whole to review all at once?     

> __< k​ayabanerve:matrix.org >__ Pipelining?     

> __< k​ayabanerve:matrix.org >__ This lets Cypher Stack use availability now on this, where that availability may otherwise be wasted.     

> __< k​ayabanerve:matrix.org >__ It also reduces the latency for the full review.     

> __< r​ucknium:monero.social >__ You said previously that getting new reviewers up to speed on the Veridise work will take time. I just don't want to have to get someone else up to speed for a second time.     

> __< k​ayabanerve:matrix.org >__ It also enables finding errors in the current work product before moving on to the next work product. I am proposing running the two simultaneously, so I want to trade that benefit for overall efficiency, but finding errors midway through the next work product is still better than finding errors after the next work product.     

> __< r​ucknium:monero.social >__ If you think scheduling is better this way, that's fine. I just wanted to bring it up     

> __< r​ucknium:monero.social >__ Can we get more opinions on this proposed expenditure? In this channel before the meeting kayabaNerve said     

> __< r​ucknium:monero.social >__ > I just got the quote from Cypher Stack for 70 XMR to review the latest work output by Veridise. I support that and jberman has also signed off.     

> __< k​ayabanerve:matrix.org >__ Heard. I've not been happy with how this academic research has gone overall personally. I think we've always tried to make the best decision at each turn, and the academia itself is resolving as necessary/desired, but there's been much more paperwork (and costs) than desired/expected. That just still leaves me to try and make the best decision here, which IMO, is reviewing this now.     

> __< v​tnerd:monero.social >__ Hi     

> __< rbrunner >__ Well, sounds just like living on the bleeding edge to me :)     

> __< rbrunner >__ Other people drive ambitious projects like this one right into the abyss     

> __< s​gp_:monero.social >__ I just got a quote on the Veridise DLOG soundness proof, if we want to discuss that as well     

> __< r​ucknium:monero.social >__ I don't really want to to to get MRL approval at this meeting because this was proposed publicly less than 24 hours ago. And previously I had suggested and kayabaNerve agreed that expenditure proposals should get a few days of MRL and community review. But I am willing to be convinced on this I guess.     

> __< r​ucknium:monero.social >__ sgp_: Ok. Give a summary     

> __< s​gp_:monero.social >__ kayabanerve: please confirm you're ok sharing this as well or if we need to have them fix something first. It's literally hot off the presses     

> __< r​ucknium:monero.social >__ And for the Cypher Stack review, is there a write-up on the exact scope of the review?     

> __< j​berman:monero.social >__ I +1 moving forward with CS on review for kayaba's reasons     

> __< s​gp_:monero.social >__ I understand the extra review time to get caught up on the context, but I hope any further review (after being caught up) is more competitive     

> __< j​berman:monero.social >__ Though it's worth nothing just reached out to another solid candidate we're waiting to hear back from. If that also doesn't work out, CS is a solid option     

> __< k​ayabanerve:matrix.org >__ To be rude to Rucknium, I just received another quote and approval from jberman on it if we can discuss it today.     

> __< k​ayabanerve:matrix.org >__ sgp_: Stop front-running me D:     

> __< r​ucknium:monero.social >__ Like I said, I prefer to have more time to digest these quotes, so it is OK to bring them up now at this meeting to "start the timer".     

> __< r​ucknium:monero.social >__ I would also prefer to have something written down in something more formal than a Matrix/IRC message     

> __< r​ucknium:monero.social >__ When you can get such a thing written down     

> __< r​ucknium:monero.social >__ So there are no misunderstandings about scope later     

> __< k​ayabanerve:matrix.org >__ First, clarifying re: jberman: Someone potentially reached to volunteer their time in review. They were contacted specifically on this topic. I don't personally expect that to work out. I'd like to get the Cypher Stack quote approved regardless. We can leave it open in that either the CS quote goes through or the volunteer (at a cost of $0, so not needing MRL approval) will occur.<clipped message     

> __< k​ayabanerve:matrix.org >__  I'll defer further commentary back to jberman.     

> __< k​ayabanerve:matrix.org >__ Re: the newly received quote, it's 10-12.5k USD from Veridise for the resulting interactive protocol, the soundness proof, and finally verifying the specified R1CS matches. That follows the scope of work prior split off from the quote at the time we came to consensus on the prior quote.     

> __< k​ayabanerve:matrix.org >__ Since it resolves the issues present in the quote when we split it off (allowing us to further discuss it and come to this quote), I find it amenable.     

> __< k​ayabanerve:matrix.org >__ jberman also signified their approval.     

> __< k​ayabanerve:matrix.org >__ Rucknium: I fully understand if this is too messy to discuss today and you want to kick this Veridise quote to next week.     

> __< rbrunner >__ So many things going on, one would almost want something like a flow diagram     

> __< s​yntheticbird:monero.social >__ Github project maybe?     

> __< k​ayabanerve:matrix.org >__ I mean, I'd prefer to keep the train moving, but I personally think this is quite messy to propose mid-meeting and absolutely won't contest kicking this to next meeting.     

> __< s​gp_:monero.social >__ Fwiw MAGIC doesn't need a decision on the money today, I can sign with the hope of the money coming through as long as there's loose consensus it's a good idea     

> __< r​ucknium:monero.social >__ Let's document the quotes in Gists or something. And that will make the mental flow chart easier     

> __< s​gp_:monero.social >__ Waiting on the review for potentially free seems appropriate to me IMHO. At least a week or so     

> __< s​gp_:monero.social >__ Unless there's a pressing blocker I'm missing     

> __< k​ayabanerve:matrix.org >__ I also won't contest kicking Cypher Stack's review to the next meeting, especially given the commentary on a potential volunteer jberman brought up. I am not hopeful re: said volunteer but I acknowledge if this now exceeds the complexity allowed for time of prior awareness.     

> __< k​ayabanerve:matrix.org >__ sgp_: If we have consensus, we have consensus and MAGIC will be promised the funds. If we don't have consensus, we don't have consensus, and if MAGIC funds this it's entirely on them.     

> __< k​ayabanerve:matrix.org >__ I am not asking MAGIC to attempt to estimate loose consensus day and start making agreements.     

> __< r​ucknium:monero.social >__ I'd suggest documenting the quotes in Gists or something. Please post links in this channel when you do. And we can discuss and hopefully approve a decision path next meeting.     

> __< s​yntheticbird:monero.social >__ I know my talk don't have much value but with this many important items in the list maybe placing another meeting mid-week would be preferable     

> __< s​yntheticbird:monero.social >__ There is always a few items that needs to be kicked at each meeting     

> __< r​ucknium:monero.social >__ Maybe, if it keeps up like this. This is unusually busy and we have had meetings earlier this year that were pretty light     

> __< rbrunner >__ I think we must be near "peak FCMP++ reviews frenzy" and things quickly will get better     

> __< r​ucknium:monero.social >__ People can of course discuss these things between meetings in this channel     

> __< s​gp_:monero.social >__ I know MAGIC isn't promised the funds but I'm still happy to move forward immediately so there isn't a delay on the most important next piece of research, even if this channel might not approve it or need more time     

> __< r​ucknium:monero.social >__ And we have the highly anticipated MAX_INPUTS/MAX_OUTPUTS discussion still on this meeting's agenda     

> __< j​berman:monero.social >__ RE: Cypher Stack approval for review of Veridise work. I think this is a fairly clear solid route to take and it would be nice to arrive at loose conensus that would be the case today (just assuming the volunteer does not pan out)     

> __< r​ucknium:monero.social >__ Let me ask rbrunner: Do you prefer that the Cypher Stack review of the Veridise document be approved today (after less than 24 hours notice) or to defer to next week's meeting?     

> __< rbrunner >__ I would say next week's meeting would be slightly better. Too many balls up in the air right now.     

> __< r​ucknium:monero.social >__ Ok. It will go on next meeting's agenda. Thanks all. Sorry for the delay, but speed is the enemy of democracy, etc.     

> __< r​ucknium:monero.social >__ 5) Discussion: preventing P2P proxy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< c​haser:monero.social >__ can't we just form consensus between meetings if that would speed up the process?     

> __< r​ucknium:monero.social >__ IMHO it would be good to decide on some actions. I think MRL should release a suggestion on Monero communication channels (Matrix/IRC, GitHub, monero.town, Reddit, Twitter, etc., maybe not necessarily the website blog) for node operators to run the IP address blocklist. Maybe some people can PGP-sign a hash of the blocklist.     

> __< r​ucknium:monero.social >__ Then the second step could be for myself and possibly boog900 (and anyone else who wants to do so like vtnerd) to research the pros and cons of having an ASmap-like criteria for `monerod` establishing peer connections: https://github.com/monero-project/monero/pull/7935     

> __< r​ucknium:monero.social >__ I could start on step 2 in 1 -2 months probably.     

> __< k​ayabanerve:matrix.org >__ ACK with frustration the first quote isn't being decided on this meeting but also understanding.     

> __< r​ucknium:monero.social >__ chaser: Maybe, but I don't know what form that would take.     

> __< s​yntheticbird:monero.social >__ Official communication would probably be the most effective solution in short-term, I don't see any reason not to do so now that the consensus has been reached on the seriousness of this network issue     

> __< rbrunner >__ Wow, the linked ASmap related PR waits since 2021?     

> __< o​frnxmr:monero.social >__ Wouldn't asmap allow a large actor to: own multiple proxies on each provider, starving honest nodes of connections to other honest nodes?     

> __< r​ucknium:monero.social >__ ofrnxmr: My research would investigate that question.     

> __< rbrunner >__ The way forward sketched by Rucknium sounds good to me. I thing without going into something like an "emergency mode" we don't have good alternatives anyway. Which is no problem IMHO.     

> __< s​yntheticbird:monero.social >__ no there are more honest subnets than bad ones     

> __< r​ucknium:monero.social >__ Basically, would an adversary gain an advantage in the status quo compared to more ASN diversity.     

> __< c​haser:monero.social >__ I was thinking of something along the lines of the majority of the relevant (per competence) people signing off on it. I understand that's a loose definition, and that it may be difficult to reach everyone outside meeting hours (in which case it would be just carried over to the meeting). just an idea.     

> __< r​ucknium:monero.social >__ It depends on the empirical distribution of honest nodes with respect to ASNs, which I have some preliminary results on     

> __< o​frnxmr:monero.social >__ For home networks, but not for vps. Asmap makes vps a more attractive attack point imo     

> __< r​ucknium:monero.social >__ OK I will write up a proposed communication plan on the blocklist for next meeting     

> __< r​ucknium:monero.social >__ 6) Making transaction weight a function of number of inputs, outputs, and `tx_extra` length instead of number of bytes.     

> __< rbrunner >__ ofnrxmr: I think we mostly agree that this needs very careful research before any action     

> __< r​ucknium:monero.social >__ kayabaNerve wrote up some more formal proposal on this here: https://gist.github.com/kayabaNerve/dbbadf1f2b0f4e04732fc5ac559745b7#on-fee-calculation     

> __< r​ucknium:monero.social >__ My question on this is how exactly do the confidential transactions arithmetic match up with the implicit fee rate.     

> __< o​frnxmr:monero.social >__ I agree, as long as the tx sizes per input/output are relatively static.     

> __< r​ucknium:monero.social >__ In bitcoin and its cousins, the fee is fully implicit: the fee is just the difference of the sum of outputs and inputs. But Monero does it explicitly since the sum of inputs and outputs isn't explicit due to CT     

> __< r​ucknium:monero.social >__ By implicit/explicit I mean there is a field (or isn't) in the actual transaction data     

> __< r​ucknium:monero.social >__ Ok we are beyond the hour and still have the MAX_INPUTS/MAX_OUTPUTS item. We can move on to that since there was a lot of interest in it     

> __< r​ucknium:monero.social >__ 7) FCMP++ tx size and compute cost and MAX_INPUTS/MAX_OUTPUTS. On MAX_INPUTS and MAX_OUTPUTS. Monero FCMP MAX_INPUTS/MAX_OUTPUTS empirical analysis.     

> __< r​ucknium:monero.social >__ https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898     

> __< r​ucknium:monero.social >__ https://github.com/monero-project/research-lab/issues/100#issuecomment-2433524326     

> __< r​ucknium:monero.social >__ https://gist.github.com/kayabaNerve/dbbadf1f2b0f4e04732fc5ac559745b7     

> __< r​ucknium:monero.social >__ https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6     

> __< r​ucknium:monero.social >__ Yes, there are four links associated with this item     

> __< k​ayabanerve:matrix.org >__ Sorry, I had connectivity issues the past few minutes.     

> __< r​ucknium:monero.social >__ IMHO, it may make sense to wait until there are actual CPU benchmarks for tx verification for these txs types before really getting into the discussion to make a decision. Consistent with what sech1 has said.     

> __< k​ayabanerve:matrix.org >__ Re: topic 6, fee discretization, ArticMine already proposed an exact clawback to use.     

> __< k​ayabanerve:matrix.org >__ On topic 7, my cited GH comment is deprecated by my long-form write-up. My Python estimator is deprecated by the actual Rust code which does now 100% accurately perform the size estimation (but is less accessible to work with).     

> __< rbrunner >__ I think we can indeed wait for hard numbers from actual benchmarks because technically the decisions do not seem to have too many consequences and interdependencies     

> __< rbrunner >__ (With emphasis on *technically* of course)     

> __< k​ayabanerve:matrix.org >__ It's only the 1-input case I've extensively benchmarked. Additional inputs should be largely linear if we aren't discussing batch verification (such as upon mempool acceptance). 2-inputs double the base cost, and while they don't double the amount of commitments, those are a fraction compared to the base cost.     

> __< k​ayabanerve:matrix.org >__ But ACK to providing more benchmarks. What exact FCMP params would people like to see?     

> __< s​yntheticbird:monero.social >__ just to have a rough idea do you know what amount of commitment would represent the computation of one input ?     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: What?     

> __< rbrunner >__ Discussions seem to oscillate between max inputs of 4 versus max inputs of 8, right? So at least those two :)     

> __< s​yntheticbird:monero.social >__ > while they don't double the amount of commitments, those are a fraction compared to the base cost.     

> __< s​yntheticbird:monero.social >__ what fraction exactly (if known) ?     

> __< k​ayabanerve:matrix.org >__ I'd refer you to the Python estimation code.     

> __< k​ayabanerve:matrix.org >__ rbrunner: My advocacy is 8 for MAX_INPUTS at this time. I'm unsure anyone is advocating for 4. I've seen complaints 8 is too low but without associated recommendations.     

> __< k​ayabanerve:matrix.org >__ (other than 8 is too low. My guess is the recommendation is anywhere from 16 to 120)     

> __< k​ayabanerve:matrix.org >__ I don't believe anyone has called out reducing MAX_OUTPUTS to 8 though.     

> __< rbrunner >__ Just to be sure, next sensible step is 16, not 12 or even 10, for technical reasons?     

> __< rbrunner >__ (For max inputs)     

> __< s​yntheticbird:monero.social >__ 120 isn't a power of two afaik     

> __< rbrunner >__ Not even if you squint?     

> __< c​haser:monero.social >__ if the end goal is max 4/4, there will need to be a reduction anyway at a later fork. so, while max 4/8 sounds attractive, it's not necessary to achieve it with this fork.     

> __< k​ayabanerve:matrix.org >__ The MAX_* values should be powers of two rbrunner     

> __< rbrunner >__ Thanks, thought so     

> __< rbrunner >__ Quite some step from 8 to 16 then     

> __< k​ayabanerve:matrix.org >__ chaser: These changes aren't being made for uniformity.     

> __< c​haser:monero.social >__ kayabanerve I know, but they still lead to a lower number of tx shapes, which does increase uniformity.     

> __< rbrunner >__ I tend to agree that a limit of 8 is a software problem for people with consolidation needs of large numbers of enotes, not a protocol problem     

> __< k​ayabanerve:matrix.org >__ 2, 4, 8, 16, 32, 64 are all a reduction to MAX_INPUTS in effect and powers of two. I think even 16 is too much. I can have 1, 2, 4, 8, 16 benched to provide the data on that though.     

> __< k​ayabanerve:matrix.org >__ 32, 64, by estimate, would be half a second and one second. Unless 16 surprises me by shattering my expectations, I'd argue those clearly unviable and not worth the time to collect data on.     

> __< k​ayabanerve:matrix.org >__ We can phrase it as benchmarking until proof time exceeds some threshold though. Let me know the threshold.     

> __< rbrunner >__ Aren't 32 and 64 hardly viable on the grounds of transaction sizes anyway?     

> __< k​ayabanerve:matrix.org >__ We currently support ~120. With a single aggregate FCMP, I'm pretty sure we'd be able to support 64 with current TX size limits.     

> __< k​ayabanerve:matrix.org >__ I think we can even support 128. The issue is solely the verification time.     

> __< k​ayabanerve:matrix.org >__ I did prior calculate the numbers on this, I'm just on my phone and can't pull them up now, sorry.     

> __< s​yntheticbird:monero.social >__ blame the phone for being ergonomic enough for maths     

> __< s​yntheticbird:monero.social >__ for not being*     

> __< k​ayabanerve:matrix.org >__ It doesn't let me run my rust tests :(     

> __< s​yntheticbird:monero.social >__ 😭,     

> __< k​ayabanerve:matrix.org >__ Anyone, for what verification time threshold to run until?     

> __< c​haser:monero.social >__ could be fit to the current protocol's times     

> __< c​haser:monero.social >__ *fitted     

> __< s​yntheticbird:monero.social >__ could it be possible? I thought it would be significantly higher than current RingCT.     

> __< c​haser:monero.social >__ it may be, I am not sure of the current verification time per output     

> __< k​ayabanerve:matrix.org >__ We can fit it to the current time for whatever the maximum amount of CLSAGs is.     

> __< k​ayabanerve:matrix.org >__ cc jberman jeffro256 can one of you get me that number?     

> __< j​berman:monero.social >__ Time to verify a 16 member CLSAG with max number of inputs?     

> __< k​ayabanerve:matrix.org >__ Yes     

> __< sech1 >__ I didn't have chance to reply about code optimizations until now, but what I can basically do is to polish an existing implementation and make it much faster. I'm good at it. As for the optimal implementation in terms of algorithms, that will require a much bigger effort from me, so better if kayaba prepares a reference with algorithms already     

> __< sech1 >__ being optimal     

> __< k​ayabanerve:matrix.org >__ Please and thank you     

> __< k​ayabanerve:matrix.org >__ It's really just the time for one CLSAG scaled jberman     

> __< c​haser:monero.social >__ I found a chart in the Seraphis paper that says 8 ms for 16 in     

> __< k​ayabanerve:matrix.org >__ sech1: If I knew how to do this, I would've budgeted for it.     

> __< c​haser:monero.social >__ wait, no. that's 16 ring size     

> __< k​ayabanerve:matrix.org >__ Implementing tailored prime field arithmetic isn't in my repertoire sech1. It's why I used a generic bigint library. The point is to replace that with our own arithmetic, optimized add/reduce/mul algorithms, etc.     

> __< sech1 >__ k​ayabanerve but you already mentioned some algorithmic optimizations which are possible     

> __< sech1 >__ ah, I understand     

> __< k​ayabanerve:matrix.org >__ The optimized algorithms depend on the primes we chose. Nicely, we only use 255 bits, not 256.     

> __< k​ayabanerve:matrix.org >__ So that will enable certain algorithms which require access to that high bit. We don't need to allocate an extra byte for overflow.     

> __< k​ayabanerve:matrix.org >__ But which algorithms? No clue. Not my field. I only know we chose a Crandall prime because it has a fast reduction algorithm.     

> __< s​yntheticbird:monero.social >__ I think we can pardon you for not being knowledgeable on something at this point.     

> __< j​berman:monero.social >__ Yea this has good benchmarks figures here: https://github.com/monero-project/research-lab/issues/91     

> __< k​ayabanerve:matrix.org >__ chaser: Is a single CLSAG with 16 ring members seriously 8ms per Seraphis paper?     

> __< j​berman:monero.social >__ assuming you were looking at this chart for that 8ms figure: https://user-images.githubusercontent.com/37489173/141365224-7c7e009f-60e9-4be0-a18b-05e278567bc8.png     

> __< k​ayabanerve:matrix.org >__ If so, you can craft TXs which take a second to verify rn which is cursed (though you find out if the current CLSAG is invalid on just an 8ms increment)     

> __< c​haser:monero.social >__ kayabanerve if I get it right, yeah. 14 ms raw, 8 ms in 25 batches     

> __< j​berman:monero.social >__ I think that chart is showing 4ms per CLSAG (since it's 8ms per 2-input tx)     

> __< k​ayabanerve:matrix.org >__ CLSAGs can't be batch verified except perhaps a single operation?     

> __< c​haser:monero.social >__ jberman yes, I was wrong. the chart is for 2/2's.     

> __< k​ayabanerve:matrix.org >__ The TX time != the CLSAG time     

> __< c​haser:monero.social >__ true. plot is thickening     

> __< k​ayabanerve:matrix.org >__ I believe the meeting is all but called by Rucknium? I'll be withdrawing at the hour.     

> __< c​haser:monero.social >__ is this it? https://eprint.iacr.org/archive/2019/654/1585584155.pdf#page=18 if so, then 15.9 ms     

> __< j​berman:monero.social >__ Was just about to comment the same link :)     

> __< k​ayabanerve:matrix.org >__ That's longer than an entire TX per Seraphis so it can't be 15.9 ms for a single 16-ring CLSAG. Either the software was improved or the hardware and we need to re-benchmark.     

> __< c​haser:monero.social >__ hm. the 2.1 GHz Opteron they used may not be the most up-to-date benchmarking hardware.     

> __< k​ayabanerve:matrix.org >__ I'll ask jeffro, who I'll also ask to run the benchmarks as they don't use VMs, to bench CLSAG so we have consistent reference hardware.     

> __< s​yntheticbird:monero.social >__ 2.1 GHz Opteron is lowkey the most accurate reference for an inclusive implementation for normal people phone     

> __< s​yntheticbird:monero.social >__ but i doubt people will run nodes on their phone     

> __< s​yntheticbird:monero.social >__ i mean this isn't too far fetch, its low-power yes, but not unrealistic hardware     

> __< c​haser:monero.social >__ that's good to know     

> __< c​haser:monero.social >__ is it the case that mobile wallets verify the CLSAGs only for the transactions they receive, but full nodes verifies them for all transactions?     

> __< j​berman:monero.social >__ mobile wallets don't verify CLSAGs AFAIK     

> __< j​berman:monero.social >__ and yes full nodes verify them for all txs (except for CLSAGs before the node's highest hardcoded checkpoint by default)     

> __< o​frnxmr:monero.social >__ I do     

> __< s​yntheticbird:monero.social >__ im proud of you     

> __< o​frnxmr:monero.social >__ My main node has run on my phone for maybe 3yrs now     

> __< o​frnxmr:monero.social >__ Low power, battery backup (dont worry about corruption due to power flickers)     

> __< o​frnxmr:monero.social >__ Main issue is storage. The device is 128gb and i'm running out of space fast :) (less than 1gb left atm).      

> __< o​frnxmr:monero.social >__ anyway, offtopic. Just thought that i'd mention that nodes on repurposed phones are (imo) much more economical than running a desktop or purchasing a single board device etc     

> __< k​ayabanerve:matrix.org >__ sneurlax is experimenting with building Cuprate into a phone app IIRC     

> __< midipoet >__ Is there any easy way to increase storage on phones past 128gb?     

> __< s​yntheticbird:monero.social >__ of course, with an sdcard destined to die in 6 month or a  soldering station (don't forget to bring your chinese NAND chip with you)     

> __< midipoet >__ so that's a no, then?     

> __< s​yntheticbird:monero.social >__ what does no mean?     



# Action History
- Created by: Rucknium | 2024-11-27T16:29:26+00:00
- Closed at: 2024-12-10T20:42:28+00:00
