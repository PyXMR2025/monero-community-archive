---
title: Monero Research Lab Meeting - Wed 17 July 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1041
author: Rucknium
assignees: []
labels: []
created_at: '2024-07-16T21:02:03+00:00'
updated_at: '2024-07-26T16:42:36+00:00'
type: issue
status: closed
closed_at: '2024-07-26T16:42:36+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

5. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). Brandon Goodell has submitted a quote for doing review of the GBP security proofs: https://repo.getmonero.org/-/project/54/uploads/e370fc495ccf32276aa40d2858366607/monero-gbp.pdf

6. Uniformity of Monero's hash-to-point function.

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1037 

# Discussion History
## Rucknium | 2024-07-22T20:04:49+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1041     

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< jberman >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< jberman >__ me: working on the migration of existing cryptonote outputs into the curve trees merkle tree so they can be used in fcmp's     

> __< v​tnerd:monero.social >__ Finally reviewing jeffro256 pr that really needs shipping     

> __< r​ucknium:monero.social >__ me: Helping with stressnet. Researching the fluff phase of the Dandelion++ protocol.     

> __< j​effro256:monero.social >__ me: Jamtis-RCT testing     

> __< 0​xfffc:monero.social >__ Basically did spend most of my time debugging this: https://github.com/spackle-xmr/monero/pull/13     

> __< 0​xfffc:monero.social >__ There is one simple issue (by nature) that stuck. I have to disconnect the node before going to validation. But the core object doesn’t have any access to t_protocol_handler. So I am trying to find a way to fix this issue. Otherwise the PR is ready.      

> __< 0​xfffc:monero.social >__ I am going to decide to add it as a flag (—sync-then-verify) or propose it as default way of monerod start up.     

> __< r​ucknium:monero.social >__ 3) Stress testing monerod https://github.com/monero-project/monero/issues/9348     

> __< r​ucknium:monero.social >__ I tried jeffro256 's "Blockchain: fix temp fails causing alt blocks to be permanently invalid" https://github.com/monero-project/monero/pull/9395 . I didn't see any of the patched nodes get stuck because of incorrectly marking blocks as invalid. Two of my nodes that didn't have the patch got stuck.     

> __< j​effro256:monero.social >__ Nice. Thanks for testing!     

> __< r​ucknium:monero.social >__ Stressnet is back to a lower tx volume, which makes the original bug harder to reproduce. Eventually the stressnet tx volume will rise back to the 3+MB block size where the issue was triggered a lot     

> __< r​ucknium:monero.social >__ No more comments on stressnet? Moving on:     

> __< r​ucknium:monero.social >__ 4) Potential measures against a black marble attack. https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ I have been looking at the fluff phase of the Dandelion++ protocol. In "Fix embargo timeout in dandelion++" https://github.com/monero-project/monero/pull/9295 vtnerd notes that Monero's D++ implementation sets the time between fluffing to a Poisson-distributed random timer. The D++ paper assumed that the fluff phase would use BTC's diffusion protocol that used an exponential distribution.     

> __< r​ucknium:monero.social >__ In 2022 BTC Core developers changed the name of the random timer from Poisson to exponential because the name was misleading: "Rename and move PoissonNextSend functions" https://github.com/bitcoin/bitcoin/pull/24021     

> __< r​ucknium:monero.social >__ Why it's confusing:     

> __< j​effro256:monero.social >__ Ahh that would explain why vtnerd used a Poisson dist     

> __< r​ucknium:monero.social >__ A random variable may be a _Poisson process_ if the arrival times between the values have an exponential distribution. The distribution of the number of arrivals in a fixed time period, e.g. one hour, is a Poisson distribution.     

> __< r​ucknium:monero.social >__ I don't know for sure what, if any, the privacy impact of this discrepancy may be (positive or negative).     

> __< r​ucknium:monero.social >__ Remember that this is the fluffing phase, which provides low privacy anyway     

> __< r​ucknium:monero.social >__ I could try to guess the impact. The best comparison I have is in Fanti and Viswanath (2017) "Anonymity Properties of the Bitcoin P2P Network" https://arxiv.org/abs/1703.08761     

> __< r​ucknium:monero.social >__ Fanti is also the lead author of the D++ paper.     

> __< j​effro256:monero.social >__ I don't know much about the technical details of D++. Is the embargo timeout the delay from when you receive a fluffed tx to when you rebroadcast it?     

> __< r​ucknium:monero.social >__ Fanti and Viswanath (2017) analyze both the diffusion protocol (which has an exponentially-distributed timer) and "trickle", which was the pre-2015 BTC tx propagation protocol.     

> __< b​oog900:monero.social >__ IMO we should move to the exponential distribution, however I don't think we have actually found the cause of nodes OOMs yet, right?      

> __< b​oog900:monero.social >__ If the cause is the fluff queue, using the exponential distribution could make the problem worse as connections could go a lot longer without fluffing     

> __< r​ucknium:monero.social >__ AFAIK, the "Embargo" in PR #9295 was the "last defense" against a black hole attack when a defective node didn't send during the stem phase     

> __< v​tnerd:monero.social >__ no embargo timeout starts when you receive a stem tx.     

> __< v​tnerd:monero.social >__ Each stem node chooses a unique timeout randomly     

> __< r​ucknium:monero.social >__ boog900: Something I noticed: for a given mean (i.e. given rate lambda), an exponential distribution has a much higher variance than a poisson distribution. That could support your point     

> __< v​tnerd:monero.social >__ Ideally you cannot determine the order in the stem based on how the embargos timeout     

> __< j​effro256:monero.social >__ Ah I see, thanks. Does the originating node have an embargo timeout, or does it just try stem again after a certain time period in the current impl?  I cam imagine a scenario om which the first node of the stem drops the tx, and then it nevers gets broadcasted     

> __< r​ucknium:monero.social >__ BTC's pre-2015 trickle protocol randomly ordered a node's peers and then sent them with a 200ms delay one after the other. This is not the same as a Poisson distribution, but maybe we could get a rough idea of the privacy of the Poisson-distributed timer if we think that its privacy is somewhere between diffusion (true exponential) and trickle.     

> __< v​tnerd:monero.social >__ The originating node also has a timeout, due to the problem you identified     

> __< r​ucknium:monero.social >__ On a realistic simulation of the BTC network graph (Figure 8 of Fanti and Viswanath (2017)), the probability of correctly guessing the true originating node was 30% for diffusion and 60% for trickle when the adversary had one connection to each honest node.     

> __< r​ucknium:monero.social >__ ^ That's without any type of D++ stem protocol     

> __< r​ucknium:monero.social >__ Fanti and Viswanath (2017) didn't think diffusion with exponential delays was very good, anyway. That's why they (with others) wrote the D++ paper.     

> __< r​ucknium:monero.social >__ But in a practical attack scenario diffusion worked better than trickle at defense     

> __< r​ucknium:monero.social >__ By the way, I'm only looking at their results for the first-seen estimator instead of the graph-centrality-based estimators. The latter can be more powerful, but AFAIK we believe that it is not feasible to estimate Monero's p2p network graph after this patch: "p2p: add a reference to Cao, Tong et al. for the last_seen changes" https://github.com/monero-project/monero/pull/5682     

> __< r​ucknium:monero.social >__ That's as far as I've gotten. It may be difficult to directly compute the probability of detection for the diffusion protocol when the timer is Poisson-distributed. Fanti and Viswanath (2017) complain about it a little even when it is the easier exponential distribution. (AFAIK, the computation is much easier with exponential because it is memoryless. Many of the terms in the formulas simplify.)     

> __< r​ucknium:monero.social >__ My guess: It would be better to use the exponential distribution from the original diffusion protocol, but I cannot be 100% sure about it at this time.     

> __< r​ucknium:monero.social >__ Anything more on this agenda item?     

> __< r​ucknium:monero.social >__ 5) Research Pre-Seraphis Full-Chain Membership Proofs. Brandon Goodell has submitted a quote for doing review of the GBP security proofs: https://repo.getmonero.org/-/project/54/uploads/e370fc495ccf32276aa40d2858366607/monero-gbp.pdf     

> __< r​ucknium:monero.social >__ kayabanerve , kayabanerve     

> __< k​ayabanerve:monero.social >__ Above quote is above, I believe we should move forward.     

> __< k​ayabanerve:monero.social >__ > Their estimate is less than Cypher Stack's quote for the Bulletproofs++ review (my closest comparable, though they're not really the same). Since the hours should be budgeting for the worst case, I personally endorse it     

> __< r​ucknium:monero.social >__ I read it. It looks good to me.     

> __< rbrunner >__ He does not mention payment in XMR?     

> __< rbrunner >__ Not sure that means much ...     

> __< r​ucknium:monero.social >__ I noticed that, too. How is he going to be paid?     

> __< rbrunner >__ But yeah, having him working again for Monero would certainly be nice     

> __< k​ayabanerve:monero.social >__ They did assume a stablecoin 🤔 Sorry, I didn't think much of that. I'll confirm XMR is viable, else we can ping sgp to see if MAGIC makes sense, so long as we do want to move forward.     

> __< k​ayabanerve:monero.social >__ *they didn't explicitly state an option, leaving the examples as stablecoins.     

> __< j​effro256:monero.social >__ I agree. Brandon accepting XMR would be preferable, especially for the stated rate     

> __< j​effro256:monero.social >__ I guess the other approach to reviewing GBPs would be to have him not look at the security proofs and instead writing his own proofs, seeing if he reaches the same conclusion. What would be the upsides/downsides of this approach?     

> __< k​ayabanerve:monero.social >__ That was considered. aaron:cypherstack.com spoke against the idea unless an independent methodology was used.     

> __< j​effro256:monero.social >__ Brandon has probably already looked at the paper I assume, which would bias his thought process     

> __< k​ayabanerve:monero.social >__ Since practically, proofs will be derived from the existing BP AC proof, we won't actually get such a methodology.     

> __< k​ayabanerve:monero.social >__ Reviewing the currently stated proofs should be less work and still cause proper evaluation.     

> __< k​ayabanerve:monero.social >__ Are there objections to moving forward and working out XMR/MAGIC after the meeting *if there's not objections to the quote itself*? Or is the financial aspect something considered critical to work out prior to general consensus?     

> __< a​aron:cypherstack.com >__ Just saw the mention, so I haven't checked the backlog...     

> __< a​aron:cypherstack.com >__ The GBP work makes changes to the protocol as well, which any independent proof would need to account for     

> __< a​aron:cypherstack.com >__ But yes, in this case I think a more efficient and useful approach would be to have a qualified reviewer conduct a review of Cypher Stack's modified protocol and security proof     

> __< j​berman:monero.social >__ the approach and price point of Brandon's proposal LGTM, agree XMR is preferable, and I'm fine with MAGIC as a backup for the stablecoin route     

> __< rbrunner >__ I also think payment will work out somehow, so no objection from me to move right after it does     

> __< j​effro256:monero.social >__ Speaking of audits, I wanted to throw the idea up of auditing the addressing protocol for legacy Cryptonote addresses as detailed in the Jamtis-RCT document, so that we can use this protocol as soon as FCMPs hit (to leverage forward secrecy and so that there isn't a fingerprinting problem when we switch to Jamtis-RCT)     

> __< r​ucknium:monero.social >__ IMHO, there is rough consensus in favor of https://repo.getmonero.org/-/project/54/uploads/e370fc495ccf32276aa40d2858366607/monero-gbp.pdf     

> __< r​ucknium:monero.social >__ We can end the meeting here.   

# Action History
- Created by: Rucknium | 2024-07-16T21:02:03+00:00
- Closed at: 2024-07-26T16:42:36+00:00
