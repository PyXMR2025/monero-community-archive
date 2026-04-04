---
title: Monero Research Lab Meeting - Wed 26 November 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1303
author: Rucknium
assignees: []
labels: []
created_at: '2025-11-25T23:27:59+00:00'
updated_at: '2025-12-06T16:44:50+00:00'
type: issue
status: closed
closed_at: '2025-12-06T16:44:50+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [BulletStar (more efficient membership and range proofs)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626).

4. P2Pool consolidation fees after FCMP hard fork. [Coinbase Consolidation Tx Type](https://github.com/monero-project/research-lab/issues/108).

5. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-11.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44).

6. [FCMP alpha stressnet](https://monero.town/post/6763165).

7. Post-FCMP scaling concepts.

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1299 

# Discussion History
## preland | 2025-11-26T05:15:14+00:00
If time permits, I’d like to discuss some of the scaling avenues I’ve been looking into at the end of the meeting

## Rucknium | 2025-11-26T14:22:02+00:00
@preland : Yes. What do you want me to call the agenda item?

## preland | 2025-11-26T15:41:21+00:00
Something along the lines of "post-FCMP scaling concepts"

## janowitz | 2025-11-28T12:50:57+00:00
Unfortunately I couldn't attend. Could somebody please post a log? monerologs.net doesn't update any more.

## Rucknium | 2025-11-28T20:46:32+00:00
@janowitz . https://libera.monerologs.net/monero-research-lab/20251126 is working again. I'll post the log in a minute.

## Rucknium | 2025-11-28T20:47:03+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1303     

> __< rucknium >__ 1. Greetings     

> __< emsczkp:matrix.org >__ Hi     

> __< gingeropolous >__ hi     

> __< jberman >__ waves     

> __< ack-j:matrix.org >__ Hi     

> __< preland >__ Hi     

> __< vtnerd >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Investigating medium- and long-term selfish mining countermeasures again. Looking at FCMP hard fork scaling parameters.     

> __< gingeropolous >__ me: spinning up my scrap heap for fcmp stressnet testing. Hit a wall with monerosim re: mining shim, going to revert back to less perfect block controller     

> __< emsczkp:matrix.org >__ wrote the ccs proposal "Bulletstar", renamed in Bulletproofs*     

> __< jberman >__ me: FCMP++ alpha stressnet I shared a custom build that includes changes slated for v1.5 alpha stressnet to address OOM's, received a couple reports from people using that build I want to continue investigating (new sync issues), planning to put out a new CCS proposal soon     

> __< preland >__ Continuing i2p bounty work, and personal research into more radical/general scalability paths.     

> __< vtnerd >__ me: squashing a few things (bugs) in lws, adding a get_info (get_version) endpoint to lws, and working on lwsf lookahead (still a slight mess)     

> __(removed)__     

> __(removed)__     

> __(removed)__     

> __(removed)__     

> __(removed)__     

> __< plowsof >__ redacted      

> __< rucknium >__ (minimum power level to send messages here temporarily raised to 10)     

> __< rucknium >__ (Ping me in #monero-research-lounge:monero.social  if you need your power level raised.)     

> __< rucknium >__ 3. BulletStar (more efficient membership and range proofs) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626).     

> __< emsczkp:matrix.org >__ Here I am, I'm the author of this CCS, thank you for this space     

> __< rucknium >__ emsczkp:matrix.org: Thanks for joining the meeting.     

> __< articmine >__ Hi     

> __< rucknium >__ emsczkp:matrix.org: Would the proposed changes to the FCMP cryptography require a hard fork?     

> __< ack-j:matrix.org >__ emsczkp:matrix.org: How does bulketproof* compare to your previous work on constant time range proofs?     

> __< ack-j:matrix.org >__ https://moneroresearch.info/178     

> __< rucknium >__ Do most of the efficiency gains occur with multi-input txs? How much benefit would single-input txs see?     

> __< emsczkp:matrix.org >__ rucknium: No, the proposal is an improvement to the zkp proofs mechanisms behind FCMP      

> __< emsczkp:matrix.org >__ ack-j:matrix.org: this is related to the question of if the Halo's modified IPA is compatible with that of BP in order to do accumulation, and the answer is no ... this research was trying to explore that direction     

> __< ack-j:matrix.org >__ s/time/size/     

> __< rucknium >__ So the planned FCMP hard fork could occur, then BulletStar added afterward without a hard fork?     

> __< sgp_ >__ Thank you for making the proposal     

> __< jberman >__ i.e. no modifications to the membership proof and range proofs used in FCMP++ txs would be needed, and the folding scheme would simply fold the existing proofs?     

> __< emsczkp:matrix.org >__ rucknium: there is an asymptotic gain with folding as long as your computations grow, in single-input txs you should not see that      

> __< emsczkp:matrix.org >__ jberman: We have to operate inside the underlying GBP proof and I would expect some modifications     

> __< rucknium >__ According to my calculations (2019-2024), 54 percent of txs are single-input: https://gist.github.com/Rucknium/d2c02f51a2d9f103a28caa8f51be7dbf/     

> __< preland >__ Interesting to see than only around 7% have more than 2     

> __< jberman >__ as I understand it, a folding scheme would enable accumulating many single-input txs into a single proof. So it's not as though there would be no benefits for single-input txs in aggregate IIUC     

> __< jberman >__ I think emsczkp:matrix.org was saying that standalone multi-input txs could benefit from a folding scheme too (if you're verifying a single 128-input proof e.g.)     

> __< jberman >__ is that accurate?     

> __< emsczkp:matrix.org >__ yes jberman, thank you for clarification. Multiple single-input txs can be aggregated and with folding we may enable an efficient proof batching     

> __< jeffro256 >__ Howdy. Sorry I'm late. I'm working on organizing an audit for the carrot_core library and trying to pin down a draft for a potential PQ turnstile design     

> __< jberman >__ basically this would complete this issue: https://github.com/monero-project/research-lab/issues/110     

> __< jberman >__ emsczkp:matrix.org: although slightly different in that we may not be able to accumualte the existing proofs     

> __< rucknium >__ How would this work in practice? Users send txs to miners and the miners create an aggregated proof, then post the aggregated proof to the blockchain and throw away the individual proofs?     

> __< jberman >__ not being able to accumulate the existing FCMP++ proofs is ok imo, this research direction is imo a critical avenue for a more scalable protocol nonetheless     

> __< rucknium >__ Will this be quantum-resistant?     

> __< jberman >__ rucknium: IIUC sounds like something like that would be possible. I imagine there would still likely be some archive nodes saving all individual proofs like kayabanerve:matrix.org  mentioned in that issue     

> __< jeffro256 >__ rucknium: You couldn't discard individual proofs w/o a hard fork, but perhaps a new node could skip downloading those individual proofs and just download/verify the aggregate proof      

> __< datahoarder >__ jberman: pruned txs by default :), full node vs archival node time?     

> __< rucknium >__ New nodes could do full chain verification without the individual proofs, right? Otherwise, it's not much better than simple pruning like we already have.     

> __< emsczkp:matrix.org >__ rucknium: no, the folding security will rely on the underlying standard assumptions of GBP. But there are interesting research proposal moving towards PQ safe folding     

> __< rucknium >__ kayabanerve:matrix.org suggested a moratorium on Monero cryptography research that is not quantum resistant. I don't necessarily share that view, but he did suggest that.     

> __< sgp_ >__ I tend to prioritize PQ safe as well     

> __< jberman >__ I think it would be a nice added bonus to consider PQ in this proposal     

> __< jberman >__ But considering this is an independent researcher aiming to take ownership of this specific research direction in parallel, I don't think it would make a lot of sense to block it     

> __< preland >__ What would be the implications of shifting to PQ in terms of difficulty/clarity of implementation? I wouldn't want PQ to derail the whole thing     

> __< sgp_ >__ Yeah I definitely don't want to block it. It is a reasonable enough direction as-is. But practically, PQ safe is more important than efficiency with the existing assumptions, imho     

> __< emsczkp:matrix.org >__ preland: First you need a PQ safe GBP, then if you want folding is another question. From my knowledge there is only one proposal doing recursive proofs in PQ settings     

> __< rucknium >__ We need to move on to the next agenda item. Any more quick comments or questions for now? It will come back as an agenda item next week.     

> __< jberman >__ I'm a strong +1, grateful for the submission emsczkp:matrix.org !     

> __< rucknium >__ emsczkp:matrix.org: IMHO, it would be good to add to the proposal a description in even simpler language of the likely benefits for Monero.     

> __< emsczkp:matrix.org >__ ok, thank you     

> __< rucknium >__ Thank you very much for your work on this, emsczkp:matrix.org     

> __< rucknium >__ I had to raise your power level, hooftly:matrix.org .     

> __< rucknium >__ We had spam earlier.     

> __< emsczkp:matrix.org >__ thank you again, see you next week     

> __< rucknium >__ 4. P2Pool consolidation fees after FCMP hard fork. Coinbase Consolidation Tx Type (https://github.com/monero-project/research-lab/issues/108).     

> __< hooftly:matrix.org >__ Ah I figured something happend     

> __< rucknium >__ Any more discussion on P2Pool coinbase output consolidation for now?     

> __< DataHoarder >__ No updates from last week. I need to start making a flow diagram to present here.     

> __< rucknium >__ Thanks.     

> __< rucknium >__ 5. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-11.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44).     

> __< DataHoarder >__ However, it'd depend on 1-in zero fee txs (in-pool) with fallback normal txs (with fees) for no multisig agreement. I think this topic can sit on the sidelines until above flow is ready.     

> __< rucknium >__ Let me ask if "delayed" fast scaling would be acceptable. Slow scaling parameters in effect for let's say 2 years after the hard fork, then the fast-scaling parameters in effect after that.     

> __< articmine >__ I am going to cut to the chase  here     

> __< rucknium >__ This would provoide time to make the node code more efficient and some more technological progress in storage and CPUs     

> __< articmine >__ What I see is that stressnet has uncovered serious vulnerabilities that requires time and resources to fix     

> __< articmine >__ Many of the devs feel overwhelmed by the task at hand.      

> __< datahoarder >__ rucknium: akin to ethereum's difficulty bomb, other way around? and worst case - the fast scaling can be soft forked if the code is not ready     

> __< articmine >__ Fast scaling cannot be soft forked     

> __< jberman >__ I see where you're headed with this articmine:monero.social , false statements so far     

> __< articmine >__ What false statements      

> __< jeffro256 >__ articmine: I think datahoarder:monero.social is saying that with the "delayed" scaling, you can soft fork away the fast scaling before it takes effect     

> __< jberman >__ articmine: No one feels overwhelmed for starters. We are making progress     

> __< datahoarder >__ articmine: I mean "limited", not added in. If fast scaling is seen as still bad then, it can be "patched"     

> __< articmine >__ jberman: I know you are     

> __< articmine >__ But are the timelines reasonable?     

> __< jberman >__ What timelines? The prior timeline estimates?     

> __< preland >__ articmine: To make sure we are all on the same page, what is the current timeline, as I've heard it thrown around a ton, but nothing from core or anyone in the know     

> __< rucknium >__ IMHO, the poor performance of the node was already revealed during last year's mainnet spam and the first stressnet last year.  It is only now that more dev effort has been applied to the problems.     

> __< articmine >__ My point is that when is being proposed is to throttle scaling in an attempt to mitigate code vulnerabilities      

> __< jeffro256 >__ It's been a while since (IMO since the divisors kink) we've had a real aligning about timelines     

> __< preland >__ I think the last estimate I heard was Q1 '26, which seems too early     

> __< jberman >__ articmine: Ack, heard on this point     

> __< rucknium >__ How important is it to discuss timelines now?     

> __< jeffro256 >__ I want to get a code audit for the carrot_core lib ASAP. FCMP++ Rust code already has most of the reviews it needs AFAIK. Then I think the FCMP++ integration code on the daemon side would be worth auditing. That can be done in parallel of carrot_core.  We could modify hard fork table then?      

> __< jeffro256 >__ Then HF activation is 6 months after that release      

> __< sgp_ >__ jeffro256:monero.social let me know if you want help for the carrot_core audit(s)     

> __< ofrnxmr >__ dont we hard fork testnet first, potentially stagenet as well to give some time for ecosystem to update     

> __< ofrnxmr >__ arbitrary, but i dont think it has to be 6 months in advance     

> __< jeffro256 >__ Yeah, that's fair. Testnet and stagenet don't need a 6month lead time tho     

> __< articmine >__ I mean if my proposal with a 500000 byte minimum penalty free zone is not enough to address the vulnerability concerns then we have some very serious issues that have nothing to with scaling      

> __< jberman >__ personally I'd like to complete the alpha stressnet (reach a point where alpha stressnet is running smooth under reasonable conditions), ideally within the next 4 weeks. and then reopen a conversation on target dates     

> __< jeffro256 >__ That's fair, and can also be done in parallel to integration / crypto audits      

> __< rucknium >__ Even with node code with zero inefficient "overhead", the proposed FCMP allowed block sizes would stress hardware. With 16MB blocks, which are allowed with quick scaling in articmine:monero.social 's proposal AFAIK, you can get 2466 1in/2out txs into a block, which would require 93 seconds on a single thread to verify. Accord [... too long, see https://mrelay.p2pool.observer/e/v7eH18wKbFd4dkxM ]     

> __< jeffro256 >__ AFAICT, the remaining changes to be made to the stressnet wouldn't involve much FCMP++/Carrot crypto-specific changes      

> __< rucknium >__ If an adversary tries to pack blocks, they can slow down verification further by selecting slow tx types.     

> __< ofrnxmr >__ aside from the dropping connections, i think its running pretty well. Would like to see how mobile wallets fare with the tx volume. Dont want a zcash situation where wallets cant keep up     

> __< jberman >__ rucknium: that proposal doesn't limit to 16mb blocks     

> __< sgp_ >__ I'm more concerned with the max block sizes (and permitted growth) than the initial penalty free zone     

> __< jeffro256 >__ ofrnxmr: Wallets really shouldn't be affected much if you assume daemons are working okay since they deal in pruned transactions, not full transactions      

> __< DataHoarder >__ also saw last week, that a 128-in FCMP++ input is already larger than the block weight at minimum, which prevents these from being included unless block is grown (I guess if they pay more fees it could be worth it?)      

> __< ofrnxmr >__ DataHoarder: I think this is due to incorrrecrly reported weight     

> __< articmine >__ Then use the current scaling parameters with a 500000 byte penalty free zone and see what you get.     

> __< articmine >__ It is far easier to test the stressnet with the current parameters than with my proposal that delays the scaling by over 2 months      

> __< ofrnxmr >__ tx reports 132kb, but weight 700kb     

> __< DataHoarder >__ yeah, then we have "Revisit FCMP++ transaction weight function" as part of this topic :) (which afaik agreement was byte size = weight?)     

> __< jberman >__ feel free to correct this math articmine:monero.social, but if I'm calculating correctly the latest proposal allows blocks to grow to 611mb within 1 year 1000*(2^(365/100,000/720/2)     

> __< articmine >__ sgp_: The lot term has va very negative impact on blockchain surveillance     

> __< articmine >__ Long term      

> __< articmine >__ I understand that.     

> __< articmine >__ This is a totally different and very serious issue      

> __< jeffro256 >__ ofrnxmr: block size is limited by tx weight, not tx byte size. So it would be limited under the current stressnet weight rules, but that is being changed for the next iteration of the stressnet     

> __< articmine >__ My proposal can destroy blockchain surveillance      

> __< jeffro256 >__ https://github.com/seraphis-migration/monero/pull/232     

> __< jeffro256 >__ Under this PR, its weight is approximately equal to its byte size      

> __< ofrnxmr >__ jeffro256: Right, when i say incorrectly reported weight, i mean that the "weight roughly = to byte size" isnt in yet     

> __< rucknium >__ jberman: jberman:monero.social: Is it 16MB blocks in the short term (100,000 blocks median)?     

> __< jberman >__ articmine: 611mb blocks would destroy Monero     

> __< ofrnxmr >__ jberman: 100.01mb blocks would destroy monero :P     

> __< articmine >__ How?     

> __< jberman >__ ofrnxmr: lol     

> __< jberman >__ articmine: you would need a data center to run a full node     

> __< jeffro256 >__ articmine: Nodes would not be able to sync / propagate faster than blocks are created. Storage requirements may become infeasible for particpants      

> __< preland >__ jeffro256: "storage is free"     

> __< preland >__ yeah, 611mb blocks would be an issue imo     

> __< ofrnxmr >__ even storage r/w speeds would be crippled by receiving a 600mb block     

> __< sgp_ >__ I think we should join together and submit a counterproposal. It's fine my initial idea isn't getting traction, but we should have another actual option that's considered good by multiple people instead of talking in circles on this one imho     

> __< articmine >__ sgp_: I will be blunt. Conflict of interest     

> __< jeffro256 >__ What is the conflict of interest of discussing new scaling ideas?     

> __< rucknium >__ sgp_:monero.social: I don't know why you decided to start a blockchain surveillance firm. Baffling decision that will follow you forever.     

> __< ArticMine >__ https://www.naxo.com/faqs     

> __< preland >__ rucknium: have to second this lol; fireice_uk keeps giving me grief in the buttcoin discord server because of it xD     

> __< ArticMine >__ Blockchain survelliance simple does ntot scale     

> __< jberman >__ I think there is some general agreement short-term / medium-term larger blocks is ok, and general agreement besides articmine:monero.social that consensus allowing blocks in the hundreds of mb's within 1 year is not (ignoring the 100mb serialization limit)     

> __< jberman >__ packet size limit*     

> __< ArticMine >__ It is at least apparent conflict of interest as defined by the government of canada     

> __< jberman >__ unless other people think blocks in the hundreds of mb's is ok?     

> __< boog900 >__ ArticMine: We cant attract users by promising privacy if we get enough users.     

> __< ArticMine >__ This is totaly separate from the issue of whethre Monero can handel certain trasnaction rates     

> __< boog900 >__ Why not just used one of the many other coins and just try get their coin more users      

> __< preland >__ jberman: I'd say this is a fair summary, though if anyone disagrees they should state it, because as it stands it'll be hard for anyone in the future to look back at this and come to a better conclusion     

> __< ofrnxmr >__ I havr a 1tb data limit on my vps and my home network     

> __< articmine >__ We need t make the necessary changes to allow Monero to be used     

> __< rucknium >__ Is there a workable compromise to have hard fork scaling rules to allow fast scaling, but soft-fork rules has slow scaling? So the soft fork can be lifted or relaxed when it makes sense to do so?     

> __< articmine >__ If a 100x increase in usage breaks Monero we have some very serious problems      

> __< boog900 >__ Removing soft fork rules is a HF AFAIK      

> __< articmine >__ boog900: I have to agree with this     

> __< datahoarder >__ rucknium: it can be a continuous function (up to some sanity limits) that can be slowed/stopped via soft fork, but that way it's always "improving" faster at a defined rate, not specifically linear     

> __< rucknium >__ Why would that be true? Miners just agree "after this block, the rules are relaxed"?     

> __< ofrnxmr >__ rucknium: some miners will reject the blocks     

> __< datahoarder >__ rucknium: someone could have not upgraded. suddenly, chain split     

> __< ofrnxmr >__ Some nodes*     

> __< articmine >__ In Bitcoin they tried this and it failed in 2013     

> __< preland >__ rucknium: I like this idea on a basic level; the hardfork adds the switch, and soft forks are used to turn it from one to the other, though I agree that it isn't without critique     

> __< boog900 >__ A soft fork is making rules tighter hard fork is making them looser     

> __< datahoarder >__ you can always make things stricter, not broader, with softforks.     

> __< articmine >__ boog900: It can work. We have to be very careful     

> __< articmine >__ I must say that I am glad my hard line on scaling is exposing some serious problems      

> __< rucknium >__ IIRC, Bitcoin Unlimited has this idea to let the bitcoin block size be unlimited, but allow miners to agree on a (short-term) limit. And miners would want that since propagation delays would increase their blocks' risk of being orphaned.     

> __< jeffro256 >__ If we assume that we must hard fork in the future for either A) PQ crypto, or B) recursive ZK proofs, C) out-of-band proving (e.g. sheilded CSV), D) plain old FCMP efficiency improvements, or E) something else, we will have another opportunity in the future to adjust scaling parameters in the scaling-maximization direction kno [... too long, see https://mrelay.p2pool.observer/e/xrfU18wKaVY2X3ZL ]     

> __< jeffro256 >__ I'm not convinved that increasing scaling parameters is do or not right now when there are popular proposals for much more radical changes in the future     

> __< datahoarder >__ jeffro256: that ossification/untenable part is maybe why having a future date where it becomes enabled by default (unless something is done) might work to get things moving     

> __< jeffro256 >__ Yeah, I don't dislike that idea      

> __< boog900 >__ the difficulty bomb 2     

> __< datahoarder >__ boog900: "past us build a bomb so we don't procrastinate now"     

> __< jberman >__ I'm not a proponent of disparate scaling algos / a future bomb     

> __< rucknium >__ Here is info on the Bitcoin Unlimited Excessive Block Size config parameter: https://medium.com/peter_r/the-excessive-block-gate-how-a-bitcoin-unlimited-node-deals-with-large-blocks-22a4a5c322d4     

> __< articmine >__ I mean a soft fork cap on the block size cout be overridden by a 51% of the hashrate     

> __< datahoarder >__ yeah, maybe difficulty bomb is a bad example, but something reasonable that all agree on ~2 years or whatever is set (and is not catastrophic)     

> __< ofrnxmr >__ rucknium: I think the fluffy block fix, fixes the broadcast delay     

> __< jeffro256 >__ articmine: Not really, unless you want 49% of the Monero ecosystem to split      

> __< sgp_ >__ The problem is that the proposal allows catastrophic things. That's the core problem     

> __< boog900 >__ yeah I would be ok with a future block size bomb, although I see most likely outcome that it is just delayed and we stick with the more security focused scaling algo     

> __< datahoarder >__ ofrnxmr: with large tx pools that are segregated (not everyone has all txs) you still end up with large transfer of txs to get blocks accepted     

> __< jberman >__ (I have to step away in 7 mins unfortunately)     

> __< jeffro256 >__ In reality, even with a soft fork, you need a supermajority to not cause catastrophic damage to the economy built around your network. You want opposing the soft fork to be so disastrous that no one does it      

> __< ofrnxmr >__ But what if you're qubic and want to do it for fun?     

> __< articmine >__ With all due respect the danger of ossification is real     

> __< preland >__ ofrnxmr: beat me to it lol     

> __< datahoarder >__ jeffro256: reverse block size scaling? where blocks become smaller until it's catastrophic even without 100x growth     

> __< articmine >__ Remember what Satoshi said in 2010     

> __< articmine >__ I mean we can leave the parameters as they are      

> __< boog900 >__ I think you are the only one that thinks current scaling is anywhere close to safe      

> __< rucknium >__ boog900: Is this true? Anyone want to say that current scaling is anywhere close to safe?     

> __< preland >__ rucknium: Define safe in this context     

> __< datahoarder >__ ofrnxmr: the only reason qubic didn't do it with their tx spamming on the side was they had their own dumb technical limitation to 896 byte block header size, so they could only attach like ~20 txs per block tops     

> __< jeffro256 >__ I like the current scaling TBF      

> __< boog900 >__ preland: allows us to react fast enough to someone producing max size blocks to prevent nodes falling out of consensus      

> __< rucknium >__ preland:monero.social: You can define it as you like. Qualify your statement.     

> __< ofrnxmr >__ jeffro256: Getting to 40mb in under 48hrs? Without max fees?     

> __< ofrnxmr >__ I think the current scaling shouldnt allow such growth speeds with just lvl 3 fees. Its almost free     

> __< datahoarder >__ is it capped to max size blocks? or is it unbounded? if it can reach 100 MB net. limit within one or two weeks, that's catastrophic. Just one or two MRL meetings to talk!     

> __< jeffro256 >__ boog900: I think that it does do a decent job at it. Yes, you can spam, but you have to stay very very consistent and continually burn XMR to increase block size     

> __< jberman >__ I intend to make a more detailed comment responding to articmine:monero.social 's latest comment, but here are some things to think about in the mean time:     

> __< boog900 >__ jeffro256: You just need mining power     

> __< jberman >__ * The most significant parameter in the proposal/algo is the long term median max growth rate of 2x     

> __< jberman >__ * This value is what determines how large blocks can grow to over the long term     

> __< ofrnxmr >__ jeffro256: you dont have to spend very much, and if you control a mining pool, you can earn your losses back by forcing othera to outbid you     

> __< jberman >__ * Reducing that back to 1.7x and keeping everything else the same, max block size w/in 1 year = 260mb     

> __< rucknium >__ IMHO, it doesn't make sense to have scaling that would require "manual" intervention. Just set the scaling parameters correctly from the start.     

> __< jberman >__ * Reducing back to 1.4x and keeping everything else the same, 94mb     

> __< jeffro256 >__ boog900: Okay fair, but you're still paying an XMR opportunity cost      

> __< boog900 >__ you can pad blocks with useless data to make them huge, and or you can set txs to 0 fee       

> __< jberman >__ The current scaling algo in consensus today allows for blocks to grow to 244mb     

> __< datahoarder >__ ofrnxmr: and IF selfish, can attempt to remove light blocks     

> __< ofrnxmr >__ I have 200xmr on stressnet and can get blocks to 14mb in 720 blocks and atill have ~200xmr     

> __< articmine >__ We must not rely on a future hard fork      

> __< boog900 >__ jeffro256: we have seen an entity recently reduce their XMR reward just for some advertising      

> __< boog900 >__ what about an entity who wants us dead?     

> __< jeffro256 >__ jberman: what causes the 244mb cap?     

> __< ofrnxmr >__ opportunity cost like $1500     

> __< jberman >__ jeffro256: check this spreadsheet for the calculations: https://github.com/monero-project/research-lab/issues/70#issuecomment-1027806393     

> __< jberman >__ that shows which params affect the calculation     

> __< preland >__ ofrnxmr: what if we publically offered like $30 in xmr to an individual who could increase the stressnet blocksize the most     

> __< boog900 >__ jeffro256: 2 days of mining is 864 XMR      

> __< spackle >__ Another thing that would have serious impact would be extending the long term median window.     

> __< jeffro256 >__ boog900: An entity who wanted to cripple Monero would probably go for a 0-tx block strategy IMHO. It's more resource-efficient      

> __< datahoarder >__ preland: this was being talked about in #monero-research-lounge:monero.social :)     

> __< jberman >__ spackle: that's true     

> __< boog900 >__ jeffro256: that would only pause us, nodes falling out of consensus allows double spends      

> __< ofrnxmr >__ jeffro256: 0tx 51% attack is harder than havinf 51/100 blocks at max size til you pass setialization or packet limits     

> __< jberman >__ extending the long term median window actually has a very significant impact     

> __< ofrnxmr >__ At which point the chain is cooked     

> __< jeffro256 >__ boog900: Fair      

> __< preland >__ jberman: Probably a dumb question, but how long would it take roundabouts for the size to drop back down to a sane level after reaching the 244 peak     

> __< ofrnxmr >__ ofrnxmr: And this only takes like 2, maybe 3 days?     

> __< ofrnxmr >__ preland: Short term = 51 blocks     

> __< boog900 >__ current mainent would last way less than 2 days     

> __< datahoarder >__ jberman: Existing miners can pad blocks right now up to that size for "free", fill the rest with legit txs, without getting into penalty zone (point being to always be at the limit of penalty zone), and extend the median free     

> __< preland >__ ofrnxmr: oh right     

> __< jberman >__ have to step away, sorry :/     

> __< rucknium >__ We are almost at 2 hours. IMHO, discussion participants need to see if a compromise is possible and what that compromise would look like. Be creative. If a compromise can't be reached, then that's unfortunate, but sometimes it's like that.     

> __< articmine >__ I was also called out     

> __< gingeropolous >__ i think extending the long term median window should be investigated     

> __< gingeropolous >__ this forces the market, or the attacker, to really justify the blocksize increase     

> __< articmine >__ A couple of things     

> __< articmine >__ 1) If the spam is not maintained the short term median resets at 50 blocks.     

> __< ofrnxmr >__ gingeropolous: How does this do anything to stop the short term 50mb blocks?     

> __< articmine >__ 2) The rate of growth and decline of the long term median is the same      

> __< articmine >__ The whole idea behind the long term t was to kill the spam. This is why a ZCash like spam attack I Monero does not work      

> __< articmine >__ So we limit the growth of the short term median to 16x and the block size also to 16x of the long term median      

> __< articmine >__ This t what my proposal does      

> __< gingeropolous >__ and what do those numbers give us in worse case scenario. 100MB blocks in 2 days? 100MB blocks in 1 year?     

> __< articmine >__ Now that the conflict of interest has been exposed, maybe calmer heads will prevail and we can work on consensus      

> __< rucknium >__ 6. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< ofrnxmr >__ 1.5 hitting some small delays due to nodes dropping all connections     

> __< ofrnxmr >__ If note, there were also 2 or 3 reports from people on 1.4 also dropping connections, and some "invalid block" logs. So maybe coincidence?     

> __< jeffro256 >__ Are you running v1.5?     

> __< ofrnxmr >__ I am     

> __< ofrnxmr >__ No issues on my end     

> __< DataHoarder >__ ofrnxmr: if "invalid block" logs are around that specific invalid miner tx, that's an old issue     

> __< ofrnxmr >__ I dont think it was that one     

> __< gingeropolous >__ yeah i got a node fully syncd on 1.5     

> __< jeffro256 >__ Yes, there's still the issues of connections dropping     

> __< jeffro256 >__ Probably a better long term approach for debugging would be to have the nodes send a reason for dropping beforehand     

> __< rucknium >__ Opt-in and/or stressnet/testnet only? Could a mainnet adversary find that info useful?     

> __< ofrnxmr >__ Otherwise, things seem to be pretty smooth. I have some 0 value amounts in wallet (probably result of sweeps) that i think might be slowing down wallet sync.     

> __< ofrnxmr >__ rucknium: The reasons for dropping connections are usually logged on lvl 2 aiui     

> __< DataHoarder >__ rucknium: it could be used to detect versions, if behavior changes, or find details about the "internal" state to find propagation     

> __< DataHoarder >__ if you mean giving the reason to other peers     

> __< jeffro256 >__ rucknium: Yeah def opt-in only. Since we use TCP connections, sending a message and then verifying it reached the destination requires communication from the other end which is a DoS vector.      

> __< DataHoarder >__ +1 for it being opt-in, though. that way operators can choose     

> __< ofrnxmr >__ https://matrix.to/#/!sgiUzbrYPvMAvwQKTG:monero.social/$D1N9WP_TIfgtrYVGN---YXQeobf_ZcFP7asXRiZ9cYA?via=monero.social&via=matrix.org&via=nope.chat datahoarder - different block     

> __< DataHoarder >__ (also, it should be not be freeform, or it may be abused to display messages on other nodes with high loglevel.)     

> __< DataHoarder >__ not as bad as this, but similar https://github.com/spesmilo/electrum/issues/4968     

> __< rucknium >__ Anything more on stressnet?     

> __< rucknium >__ 7. Post-FCMP scaling concepts.     

> __< preland >__ (copy paste inbound)     

> __< preland >__ Thank you. There are two ideas that I have been looking into in terms of scalability. The first is a more ambitious “federation”-style approach to scalability.     

> __< preland >__ This would have the blockchain and network autonomously split into smaller sub-networks once a certain threshold has been met. The result would be an effectively infinitely scalable network. The main challenges I’ve found would be ensuring that two sub-networks can trivially prove that each other have been following proper p [... too long, see https://mrelay.p2pool.observer/e/yJrq2MwKYlUtNm5R ]     

> __< preland >__ I’ll continue looking into that, but for now I’m mainly focused on the other idea I’ve been looking into, which is adopting a quorum consensus model similar to how Qubic’s operates (with significant modifications made to its implementation). This would allow for transaction scaling to be increased to an incredib[... more lines follow, see https://mrelay.p2pool.observer/e/yJrq2MwKYlUtNm5R ]     

> __< rucknium >__ Is the first one similar to sharding?     

> __< preland >__ Yes     

> __< datahoarder >__ preland: Note Qubic's model depend on a centralized arbitrator to kick computors out, which they have done a few times and one last week. No specific reason is needed, but they claim to have found collusion     

> __< datahoarder >__ The comparison with their model is maybe not desired, as it's, mainly centralized across several layers     

> __< preland >__ datahoarder: Correct; this is one (of many) things that have been switched out     

> __< preland >__ datahoarder: It's what inspired my initial look into it, which is why I mention it, even if it isn't entirely deserved tbh     

> __< datahoarder >__ preland: They'll use any mention for marketing :)     

> __< datahoarder >__ On that topic, they recently changed how all of that works regarding txs, and changed how fast they tick, and changed it back again, and later changed how txs work again.     

> __< ofrnxmr >__ Isnt the former similar to how pruning currently works     

> __< ofrnxmr >__ Except, instead of infinite, there are 8 different shards (stripes)     

> __< rucknium >__ A pruned 1in/2out FCMP tx is about the size of a 1in/2out bitcoin tx, FWIW. Learn to love pruning.     

> __< preland >__ ofrnxmr: not exactly; each subnetwork would be a distinct network in and of itself, and the networks would be able to interact with each other through some sort of transfering     

> __< preland >__ the main upside to it wouldn't be in storage per se, but in tps scaling     

> __< rucknium >__ Or don't. You don't have to love pruning if you don't want to. But it's very useful  (and the default when you launch a Monero node from the GUI wallet now).     

> __< datahoarder >__ if I understand, to "prune" a subnetwork you'd have to aggregate its state in a proof -> to then join the others and "close" aka prune it?     

> __< preland >__ datahoarder: From what I've seen so far that seems to be the case     

> __< datahoarder >__ all that would be left of that subnetwork would be that proof, which participants can create new transactions against     

> __< datahoarder >__ in (again Qubic) case their "pruning" is due to being a balance based system. So they just aggregate current state, delete everything else, and also, delete some inactive (but with active dust) and zero-balance accounts     

> __< rucknium >__ https://mrelay.p2pool.observer/m/monero.social/FpALSKRIlOlUVUhFgNWuHkRi.ods (carrot_fcmp_pruned_tx_size.ods)     

> __< rucknium >__ ^ Pruned FCMP tx size table, created by jeffro256:monero.social  🧡     

> __< datahoarder >__ this is how they claim to be "more private than Monero", too bad anyone can just archive the network :). How does this work for an UTXO based system, without clear spend tied to each UTXO? Using an accumulator (a-la UTREEXO?)     

> __< preland >__ datahoarder: The equivalent pruning would be using zk rollups     

> __< rucknium >__ It was posted in the #no-wallet-left-behind:monero.social  room: https://matrix.to/#/!PAAeACCTzofUENRcqJ:monero.social/$1QQzyPyFKw0XrNZH3p0t-a4Wgxi4EhstRKq3ir6tJqw?via=monero.social&via=matrix.org&via=tchncs.de     

> __< preland >__ As you pointed out, the comparison to Qubic is not exactly an apt one admittedly; there are a number of attributes and "quirks" in Qubic that cannot be tolerated whatsoever in Monero, and a number of features that just don't make sense (like UPoW)     

> __< articmine >__ I have to leave bow     

> __< datahoarder >__ the lack of decoy indices adds up, it's just a list of key images -> outputs! > <rucknium> A pruned 1in/2out FCMP tx is about the size of a 1in/2out bitcoin tx, FWIW. Learn to love pruning.     

> __< datahoarder >__ on that topic, would it make sense to have a V3 tx format, that removes the need to serialize inputs with empty vectors of offsets / input type / amount?     

> __< rucknium >__ If you are curious about how many pruned nodes you have to have to make sure you have all 8 slices/stripes, I have the numbers and formula in Appendix B here: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-optimal-fee-ring-size.pdf      

> __< rucknium >__ Code: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/code/pruning-slices-collectors-problem.R     

> __< jberman >__ I think it's possibly unrelated to anything in v1.5. I have complete logs of the issue on my end and a first look looks like an issue that triggers when the pool actually does exceed the max weight > <ofrnxmr> If note, there were also 2 or 3 reports from people on 1.4 also dropping connections, and some "invalid block" logs. So maybe coincidence?     

> __< jberman >__ I haven't had the chance to dig yet     

> __< datahoarder >__ the overhead for FCMP++ of "unused" data per input is 1 byte for type, 1 byte for amount, 1 byte for len of offsets. so 19 total, 15% overhead per input. ofc, pruned.     

> __< ofrnxmr >__ jberman: I pinned a log from 1.4 release with similar issue     

> __< ofrnxmr >__ jberman: Yeah. The pool was > 600mb , filled with 128 input txs that couldnt be mined     

> __< preland >__ I am going to continue looking into this further, as I think that this would be an interesting path for Monero to take once FCMP++ has been implemented and related issues have been addresssed. I'll plan on continuing my work and progress in the https://github.com/preland/xmr-republic-docs repository; if there are any issues of [... too long, see https://mrelay.p2pool.observer/e/j4qz2cwKbmU4N01N ]     

> __< rucknium >__ Thanks everyone. We can end the meeting here.     

> __< ofrnxmr >__ ofrn questions:     

> __< ofrnxmr >__ 1. Randomx v2 <- are we hoping to ship this with fcmp hf?     

> __< ofrnxmr >__ 2. Should we increase the default txpool limit by 4x? Also, are we sure eviction works properly? Are txs added back when the txs are re-received from peers?     

> __< ofrnxmr >__ 3. Is 72hrs a sane expiry for valid txs?     

> __< preland >__ Thank you     

> __< datahoarder >__ ofrnxmr: 1. AFAIK the commitment part is done, but not a change in parameters to tweak towards modern hardware     

> __< ofrnxmr >__ But is this on the todo for fcmp hf? Or not planned? Should it be?     

> __< datahoarder >__ proposal for v17 https://github.com/monero-project/monero/pull/10038 and https://github.com/monero-project/monero/issues/8827 which is listed under https://github.com/seraphis-migration/monero/issues/53 "RandomX commitments w/double hashing" under "Daemon features"     

> __< datahoarder >__ that might be nice to see on beta stressnet :)     

> __< plowsof >__ thanks, i forgot to ask if https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626 would be funded with the FCMP++ research fund? kayabanerve jberman     

> __< kayabanerve:matrix.org >__ I find the work emsczkp: is proposing interesting, and the rate reasonable.     

> __< kayabanerve:matrix.org >__ It is not in scope to the existing fcmp++ research fund, thought that is handed over to the mrl upon resolution iirc.     

> __< ofrnxmr >__ datahoarder: Thats not v2 thougg     

> __< ofrnxmr >__ https://github.com/tevador/RandomX/pull/274 datahoarder     

> __< DataHoarder >__ that's what I mean, "commitment part is done, not change in parameters"     

> __< DataHoarder >__ about actual v2 parameters, poke sech1 for context :)     

> __< jeffro256 >__ Personally, I think that the commitment portion is the most important     

> __< jeffro256 >__ I am neutral to the other virtual machine changes      

> __< spackle >__ You set the default median and surge factor to limit the size of the short term blocks, and you set the long term median window to keep that limit in place for a known duration. > <ofrnxmr> How does this do anything to stop the short term 50mb blocks?     

> __< spackle >__ In combination, this establishes that no blocks larger than X MB shall be created in the next Y blocks.     

> __< spackle >__ Which is the clearest and simplest path to giving the scaling design a safety specification, at least as I see it.     

> __< spackle >__ Rather, that IS the safety specification that exists which should now be brought into alignment with the realities of the software.     

> __< articmine >__ spackle: My proposal     

> __< articmine >__ If you want to stop 50 MB short term blocks      

> __< articmine >__ How much are t willing to pay for a 50 MB block on mainnet?     

> __< spackle >__ A steady stream of 50 MB blocks will cripple the network, and should not be produced in the short term at any price IMO.     

> __< articmine >__ How much do you think it would cost to spam a 50 MB block on mainnet under my proposal at current XMR / USD rates     

> __< articmine >__ Just one block      

> __< articmine >__  ... and how long will it take?     

> __< spackle >__ I am not interested in making the price prohibitive, I am interested in prohibiting the condition entirely.     

> __< articmine >__ Price in USD or XMR     

> __< articmine >__ spackle: Then this is the wrong chain for you     

> __< articmine >__ One needs a chain with a fixed blocksize. That is not the Monero social covenant      

> __< spackle >__ You misunderstand me, nobody is discussing a long term hard limit on block size. I am discussing short term behavior and safety specification.     

> __< spackle >__ The difference we are discussing is between putting a price tag on breaking the network, and preventing the network from breaking entirely.     

> __< articmine >__ Then answer my how long question      

> __< spackle >__ That is for people to come to consensus on, not for me (or you) to dictate.     

> __< articmine >__ Define short term because      

> __< spackle >__ I see short term as the length of time it takes to adjust the long term median, currently 50000 blocks.     

> __< articmine >__ With my proposal the maximum allowable block starting at 1 MB is 16 MB     

> __< articmine >__ So problem solved      

> __< spackle >__ If there is agreement that 16 MB is the correct value. I have not yet seen that happen, and I believe we are waiting for further input from the stressnet at this time.     

> __< articmine >__ Please read my latest proposal      

> __< articmine >__ There is a lot of FUD and yes even conflict of interest      

> __< spackle >__ I have read and understand you proposal. Allow me to restate and clarify my position: The safety specification for the scaling design is that 'no blocks larger than X MB shall be created in the next Y blocks.'     

> __< spackle >__ Get agreement on the maximum size X, get agreement on the length of time Y, and the job is done.     

> __< spackle >__ *your proposal     

> __< articmine >__ X = 16 MB Y = 50000     

> __< articmine >__ Start ing blocks before the 50000 under 1 MB     

> __< spackle >__ Yes, those are the numbers you have independently chosen by yourself. My understanding is that we are waiting for further stressnet results before agreeing on these values.     

> __< articmine >__ I originally had 32 for X and later modified it to 16     

> __< spackle >__ Again, values you chose yourself without input from testing.     

> __< spackle >__ Last I heard jberman said he needed to review the 16x cap in totality with the proposal     

> __< spackle >__ I will wait for others to speak up, I am sure conversation will continue.     

> __< articmine >__ 16 had input from testing      

> __< articmine >__ As for the 1.7 growth rate for ML it was chosen at the last fork by an individual who has a conflict of interest      

> __< spackle >__ I don't think so, it was thrown out by one person as a more reasonable option than 32. I did not see hard empirical reasons or consensus backing it.     

> __< articmine >__ My original proposal at the time was 2     

> __< spackle >__ I am happy to be proven wrong, and if you would like to list the reasoning or people who had consensus on that value I think that would be helpful.     

> __< spackle >__ If that is the case, then I would like to see that discussed thoroughly at the next meeting.     

> __< articmine >__ At the time I worked on issue 70 with Koe. We came to consensus. The fee structure was based upon 2. It was at the last moment that the change was made      

> __< articmine >__ One can read all of this on issue 70      

> __< articmine >__ The fee structure is still based upon 2     

> __< spackle >__ Was any practical testing of the daemon considered in your discussions with Koe?     

> __< articmine >__ I am talking like 5 years ago      

> __< spackle >__ What I have seen from the stressnet would indicate that was not the case.     

> __< articmine >__ spackle: I agree     

> __< spackle >__ Indeed, so the scaling was set without empirical feedback. Now is the time for that to happen.     

> __< spackle >__ Right now we are waiting on feedback, as I understand things.     

> __< articmine >__ I am actually shocked as to has been revealed in the Stressnet      

> __< articmine >__ I also don't know when the fatal bugs were introduced      

> __< articmine >__ What I do know is that the scaling was way more aggressive in 2014     

> __< articmine >__ No Long term median      

> __< articmine >__ Just the short term median      

> __< spackle >__ Also way more disconnected from reality.     

> __< articmine >__ The long term median was introduced in 2919     

> __< articmine >__ 2019     

> __< articmine >__ Like I said I am glad we exposed the conflict of interest so we can work on this in a sensible way      

> __< articmine >__ We got a lot acct in the last meeting      

> __< articmine >__ accomplished      

> __< articmine >__ We have to get to the bottom of the bugs, t risk assist with them, how long they will take to fix, what resources are needed etc      

> __< articmine >__ We have to get to the bottom of the bugs, the risk associated with them, how long they will take to fix, what resources are needed etc.     

> __< articmine >__ Sorry I hate phones and their useless AI     

> __< articmine >__ Then we can connect with reality      

> __< articmine >__ We also given the seriousness of the situation need to make sure that the feedback is not influenced by conflicts of interest      

> __< spackle >__ My opinion is that consensus is reached when informed persons can affirmatively state:      

> __< spackle >__ 1.) YES, the network can handle a steady stream of blocks that are size X.     

> __< spackle >__ 2.) YES, we can respond, and adapt the network, to handle what may arise in the future over time Y.     

> __< spackle >__ Others have discussed longer term values, such as what the block size may become in a year. I leave it to them to make their case.     

> __< articmine >__ spackle: I agree     

> __< articmine >__ spackle: This is where the cost of spam becomes paramount     

> __< spackle >__ Then indeed we are in agreement, including that X=16MB and Y=50000 blocks are not yet settled values. I have yet to see anyone affirm those statements with those values.     

> __< articmine >__ One important aspect of testnet is that the current.  short term aggressive scaling should be used with the FCMP++  sizes and verification times.      

> __< articmine >__ Otherwise it will take months if not years to spam up the testnet, with my proposal      

> __< articmine >__ This is by design. I deliberately designed it to frustrate and increase the cost of spam     



## janowitz | 2025-11-30T10:27:44+00:00
Thank you, @Rucknium 

Unfortunately I was not able to attend the meeting, and I am aware my comment is not being considered here, but maybe someone will read this. I am one of the few being fully with ArticMine.

According to my router stats, last month I roughly received 4TB of data and sent 1TB. So receiving would be around 150 GB a day, so accordingly a block with 200 MB every 2 minutes. [Nielsens's law](https://www.nngroup.com/articles/law-of-bandwidth/) shows bandwidth is growing by 50% per year and should be roughly x50 the bandwidth of 10 years ago. The average user is streaming 4k content with up to ~50 Mbit/s and downloading a 1 GB block would take 8 seconds on a 1 Gbit/s connection under perfect circumstances.

Storage prices are as low as never before, and SSD is about 1/30 of the cost 10 years ago, most probably becoming even cheaper than traditional HDDs in the next few years https://ourworldindata.org/grapher/historical-cost-of-computer-memory-and-storage
Maybe Monero should add more than 8 "slices" for pruning nodes like 32 or 64 and allow users to choose how much they want to hold, including zero making a pruning node not a source for initial sync any more. I think the network is resilient enough at this point to do this.

The only concern I'd have is the verification, which should remain feasible to accomplish on average hardware. I don't think we should necessarily look at Raspi or low-end VPS even if we might lose some nodes. So I'd argue an average CPU with maybe 20 threads should be able to keep up syncing at any time. For mining, most rely on pools anyway, which most probably have way better hardware, and with fluffy blocks, they have only little overhead to download after a block is created. 

We shouldn't make the same mistakes as Bitcoin, when it had its momentum in adoption from large merchants like Microsoft starting to accept Bitcoin in their stores in 2014, but the blockchain became clogged, and Bitcoin has been removed again from all those. Nowadays blocks don't even get full because people have been mostly driven to custodial solutions, which can't be our goal. According to public statistics from merchants like Shopinbit or Coincards, literally nobody uses LN, and Monero is becoming dominant wherever it is accepted. Discouraging growing organic usage would be fatal for Monero.

Bitcoin became successful anyway, however not as a medium of exchange but as a projected store of value (which I doubt but doesn't matter here). Monero doesn't have this opportunity, since after delisting and more and more strict regulations, we can't rely on institutional investors or ETFs to pump the price short term. We need organic adoption, and like articmine stated, we should be prepared to scale by x100 at any time.

## MoneroArbo | 2025-12-01T11:43:16+00:00
>  So I'd argue an average CPU with maybe 20 threads should be able to keep up syncing at any time.

I don't think that's average. According to [Valve](https://store.steampowered.com/hwsurvey) the most common CPU has 6 cores / 12 threads. The percent of people with 20 threads or more is about 27%. 15% of users have 8 threads and almost 29% have 12 threads.

These numbers are probably actually higher than average since it's a survey of people who use their PC for gaming.

I've been testing FCMP on an older laptop (10th gen i5) with 8 threads (4 cores) and 10 MB blocks already can take 10-20 seconds per block to verify. A single 128 input transaction verifies in about 12 seconds.

edit: I do agree with you generally but for me the target would actually be "below average CPU" because I know a bunch of people don't have access to good hardware, or Internet for that matter, but Monero is important for them too. If the goal is peer to peer cash, accessibility is key.

## janowitz | 2025-12-01T13:49:48+00:00
> I don't think that's average. According to [Valve](https://store.steampowered.com/hwsurvey) the most common CPU has 6 cores / 12 threads. The percent of people with 20 threads or more is about 27%. 15% of users have 8 threads and almost 29% have 12 threads.

Thank you for this link, interesting data!

> I've been testing FCMP on an older laptop (10th gen i5) with 8 threads (4 cores) and 10 MB blocks already can take 10-20 seconds per block to verify. A single 128 input transaction verifies in about 12 seconds.

Okay, large input tx might become a problem at some point, since there could be ~65 tx with 150 kB size each in a 10 MB block. With 8 threads it would take around 100 seconds to verify those according to your figures on this hardware. But looking at [verification times](https://github.com/seraphis-migration/monero/issues/44#issuecomment-3150754862) with more and more inputs, it's pretty linear with the amount of inputs, however not with tx size and maybe weight should increase with every additional input not to discount malicious actors for creating tx with max amount of inputs. But it seems this has been [reverted back to byte size](https://github.com/seraphis-migration/monero/issues/44#issuecomment-3423391977).

I will join stressnet, too to test a bit for myself asap.

# Action History
- Created by: Rucknium | 2025-11-25T23:27:59+00:00
- Closed at: 2025-12-06T16:44:50+00:00
