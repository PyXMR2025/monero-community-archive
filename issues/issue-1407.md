---
title: Monero Research Lab Meeting - Wed 17 Jun 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1407
author: Rucknium
assignees: []
labels: []
created_at: '2026-06-17T14:59:39+00:00'
updated_at: '2026-07-01T14:52:43+00:00'
type: issue
status: closed
closed_at: '2026-07-01T14:52:43+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Helios/Selene review.

4. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). [Jamtis](https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).  [Monero-PSK](https://gist.github.com/tevador/9169235b3c0c97e735f58a8c2ba92502).

5. [`monerosim`](https://github.com/Fountain5405/monerosim).

6. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

7. Any other business

8. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1402 

# Discussion History
## Rucknium | 2026-06-24T14:15:56+00:00
Logs

> __< gingeropolous >__ i may or may not be able to attend todays meeting. i think monerosim is on the agenda. if i can't make it i'll read the scroll and answer any questions.      

> __< rucknium >__ MRL meeting in this room in two hours.     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1407     

> __< rucknium >__ 1. Greetings     

> __< jberman >__ waves     

> __< vtnerd >__ Hi     

> __< boog900 >__ Hi     

> __< jpk68:matrix.org >__ Hello     

> __< sgp_ >__ Hello     

> __< rbrunner >__ Hello     

> __< jeffro256 >__ Howdy     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rbrunner >__ Could make my Polyseed PR: https://github.com/monero-project/monero/pull/10765     

> __< rucknium >__ me: Helping investigate bugs on stressnet. Keeping stressnet stressed with transaction spam.     

> __< tevador >__ Hi     

> __< jeffro256 >__ Me: working to implement feedback on hot/cold wallet PR, in communication with hardware wallet dev teams      

> __< jberman >__ me: solved sporadic double spends on stressnet thanks to rucknium's logs (also a mainnet issue), reviewed jeffro's upstream PR to speedup the /getblocks.bin RPC (which has been a bottleneck affecting stressnet), started reviewing jeffro's hot-cold PR, continued phase 1 audit remediation final tasks     

> __< vtnerd >__ me: updated lws fcmp++ branches, did some digging into block size limits (but still have unresolved issues), and have been working on the wallet fido2 lib     

> __< rucknium >__ 3. Helios/Selene review.     

> __< rucknium >__ Here was the discussion from last time: https://libera.monerologs.net/monero-research-lab/20260610#c683819-c683885     

> __< sgp_ >__ Hello :)     

> __< sgp_ >__ The options are unchanged from last meeting. We recommend the review for $35,000, which appears to be the best fit for expertise and budget     

> __< sgp_ >__ Support seemed to be in favor last meeting, with a desire to wait until this week to make a decision     

> __< rucknium >__ IIRC, maybe jeffro256:monero.social  wanted to look at the quotes in more detail.     

> __< rucknium >__ I mean, he had the info, but didn't have time to look at it in detail.     

> __< sgp_ >__ Yes. I am unsure if they have but I did ping him a few times this week (including yesterday)     

> __< jeffro256 >__ I did so, and agree further with the 35,000 quote      

> __< jberman >__ Also worth mentioning: one of the board members at the top candidate ($35k candidate) is also involved with a competing cryptocurrency project, but they aren't the auditor or CEO. I agree that the top candidate firm has the most relevant xp for the money     

> __< sgp_ >__ There is also one point that jberman wishes to raise for transparency's sake     

> __< rucknium >__ How many board members does the firm have?     

> __< rucknium >__ Thanks for raising this by the way     

> __< jberman >__ I can't see it affecting the audit in any way, and I'm confident in the choice of top candidate. Just figured it's worth mentioning in the interest of transparency     

> __< sgp_ >__ I believe that despite the association, this is the best pick. The auditors' skills come in part from their familiarity with doing similar curve review work for other protocols. I do not know how many board members the organization has, but the CEO and the audit staff are independent (not staff of the other crypto project org)     

> __< sgp_ >__ Therefore I consider the association irrelevant personally, but we didn't want to make it seem like we were hiding a "critical" detail     

> __< rucknium >__ More discussion on this issue?     

> __< jberman >__ probably would be good to get a signoff today if possible     

> __< rucknium >__ I think we have loose consensus in favor of the 35,000 USD equivalent quote for review of Helios/Selene.     

> __< sgp_ >__ I would appreciate assistance in receiving the funds as soon as possible so that we can lock in the contract. Thanks!     

> __< rbrunner >__ I see it in the same way, for what it's worth     

> __< rucknium >__ 4. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). Jamtis (https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).  Monero-PSK (https://gist.github.com/tevador/9169235b3c0c97e735f58a8c2ba92502).     

> __< tevador >__ No updates from me today, but I can answer questions if needed.     

> __< neptunian:unredacted.org >__ I just got here in time, haha.     

> __< neptunian:unredacted.org >__ Is there anything more to debate on Monero-PSK vs Jamtis?     

> __< neptunian:unredacted.org >__ I missed the last meeting, apologies.     

> __< tevador >__ I think we can skip Monero-PSK until spirobel produces a draft.     

> __< tevador >__ Everything that can be said without a concrete proposal has already been said.     

> __< neptunian:unredacted.org >__ tevador: Fair enough. I don't think Spirobel is currently here, so I cannot ask about PQ for Monero-PSK (namely for the DH, as the PQ properties seem to revolve mostly around symmetric encryption used.)     

> __< neptunian:unredacted.org >__ Unless, of course, you'd like to answer.     

> __< neptunian:unredacted.org >__ Regardless, I feel that Jamtis is still far more mature than Monero-PSK, leading me to consider the latter much less.     

> __< rucknium >__ tevador: I will take Monero-PSK off future agendas until further notice.     

> __< tevador >__ I think I'll be removing the instant sync protocol from Jamtis specs for reasons previously mentioned by jberman. I can hear argument for keeping it.     

> __< neptunian:unredacted.org >__ tevador: I didn't see this.     

> __< neptunian:unredacted.org >__ I'll read over it after sending this message, but I want to ask if it's stateful.     

> __< tevador >__ The main issue with the instant sync proposal is that it won't work once the wallet is ever restored from the seed.     

> __< tevador >__ neptunian: it's technically stateful but that's not an issue in practice.     

> __< neptunian:unredacted.org >__ tevador: So not as much as PSK? Cool     

> __< neptunian:unredacted.org >__ tevador: Could there be something like a bloom filter optimisation with something like in 2.2 to allow for the instant scan to be viable? It could allow for restored-seed wallets to still function.     

> __< neptunian:unredacted.org >__ neptunian:unredacted.org: Section 2.2 of the Jamtis draft*     

> __< tevador >__ No, the instant scan can never work with static addresses.     

> __< neptunian:unredacted.org >__ Understood. In that case, it seems to cripple UX from my point of view.     

> __< tevador >__ Section 2.2 is light wallet scanning, which is not "instant sync" as it still involves scanning the entire blockchain.     

> __< neptunian:unredacted.org >__ tevador: I meant as in using that light wallet server to provide some kind of compact state summary to sync the wallet.     

> __< tevador >__ That's already proposed in 2.2. I'm not sure what exactly you are proposing.     

> __< tevador >__ The LWS provides the light wallet with a list of possible owned enotes (roughly 1/256 of the blockchain)     

> __< neptunian:unredacted.org >__ Ah. I see then. I don't have any arguments for instant-sync then.     

> __< tevador >__ LWS still requires some scanning by the wallet, but just less of it.     

> __< rucknium >__ More discussion of this item?     

> __< neptunian:unredacted.org >__ rucknium: Nothing for me to add.     

> __< rucknium >__ 5. monerosim (https://github.com/Fountain5405/monerosim).     

> __< rucknium >__ Is gingeropolous:monero.social here?     

> __< rucknium >__ I lead this one then.     

> __< rucknium >__ monerosim uses the shadow software developed by Tor researchers. It runs real monerod node binaries on a local computer and simulates a network. It can be used to test node software modifications in a realistic networked environment.     

> __< rucknium >__ gingeropolous:monero.social used an LLM to do most of the coding. We allowed the LLM usage because it was conversion of existing software for a similar purpose and this software is not security-critical. I wanted to make sure that the LLM wasn't faking it somehow. I took some transaction relay analysis code that I wrote for m [... too long, see https://mrelay.p2pool.observer/e/47ewgY4LbHd2c1pq ]     

> __< rucknium >__ Here are my results: https://github.com/Fountain5405/monerosim/issues/3     

> __< rucknium >__ The transaction relay data was mostly similar to mainnet, except peer connection durations were much shorter and the transaction relay timer behavior had some sub-second discrepancies.     

> __< rucknium >__ We are trying to figure out why the peer connection durations are much shorter. The LLM "thinks" that it's because the simulated network is too uniform, especially given that all the simulated nodes are reachable. It "reasons" that the timers fire more frequently.     

> __< rucknium >__ It "says"     

> __< rucknium >__ > update_sync_search() runs on a 101-second timer (epee::math_helper::once_a_time_seconds<101>), and when all 12 outbound slots hold synced peers with fewer than 2 in state_synchronizing, it drops the last non-anchor synced out-peer to make room to search for sync candidates. In the simulator every node is always synced and ev [... too long, see https://mrelay.p2pool.observer/e/su-8gY4LRE5wUlly ]     

> __< rucknium >__ > The result in our logs: tx-carrying connections die at median 100.3 s with p25–p90 of 100.0–100.9 s — exactly one timer period. The "dropping synced peer, 0 syncing, 12 synced, 12 max out peers" line fires at 101.001 s median cadence (497 times in 16 h), each followed within 1 ms by the CLOSE of that peer.     

> __< rucknium >__ Maybe someone with peer networking knowledge may have a hypothesis.     

> __< rucknium >__ Anyway, monerosim is mostly good and it would be interesting to see other people and developers try it. You can run a small network, e.g. 30 nodes, for 72 hours on a consumer machine.     

> __< neptunian:unredacted.org >__ Perhaps you could force nodes to have a small chance for a failure rate?      

> __< rucknium >__ To get to 1,000 nodes, you need a big machine like the 256-thread 1TB RAM machine in the Monero Research Computing Complex.     

> __< neptunian:unredacted.org >__ neptunian:unredacted.org: To be clear, I have very little peer networking knowledge. It's just my best guess at something like this.     

> __< rucknium >__ I think we need to figure out how to have most nodes have closed ports. We'll need to do that anyway for a more realistic network topology.     

> __< rucknium >__ monerosim can do --hide-my-port as a startup flag for the node, but I'm not sure that has the exact same effect as closed ports.     

> __< rucknium >__ More discussion on monerosim?     

> __< rucknium >__ neptunian:unredacted.org: Neither gingeropolous:monero.social  nor I want to modify monerod more than absolutely necessary. AFAIK, it hasn't been modified at all yet. We will want to modify it later for better logs when analyzing specific phenomena.     

> __< rucknium >__ 6. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< rucknium >__ jberman:monero.social figured out this occasional bug where a wallet would forget it spent a coin. Then when it tried to spend again, it would accidentally try to double spend the same coin: https://github.com/monero-project/monero/pull/10781     

> __< jberman >__ I've got a tracking PR for beta stressnet v2.1 here: https://github.com/seraphis-migration/monero/pull/415     

> __< jberman >__ One lingering issue I think needs to be investigated fully next / soonish is occasional bans. I believe it may be an issue with tx relay v2     

> __< jberman >__ I'd also like to get the RPC speedup implemented upstream sooner rather than later, because I believe the RPC slowness may be at the root of a number of things people are seeing when the pool gets big     

> __< jberman >__ for example: https://github.com/seraphis-migration/monero/issues/414     

> __< rucknium >__ RPC speedup would be amazing :)     

> __< jberman >__ But by and large, it does seem we're moving into the territory of only pre-existing daemon issues and/or issues not directly caused by anything from FCMP++/Carrot specifically     

> __< jberman >__ So, that's good. With that v1 fiasco out of the way, and now with that double spend issue out of the way, beta seems to be chugging along nicely     

> __< rucknium >__ Things look much better. I think that things seem pretty stable at 6MB blocks. That's the long-term median max. On mainnet a determined spamming attempt would be at 6MB for 50,000 blocks before the limit raised, AFAIK.     

> __< rucknium >__ I haven't seen different-sized txpool between nodes recently. That's the only thing that still worries/annoys me. It seemed for a short while that a mining node had an empty txpool this week. Hard to know for sure.     

> __< rucknium >__ 0-conf merchant acceptance is usually considered unsafe (or unsaf er) when all nodes do not have the same txpool contents.     

> __< jberman >__ ya, that's another thing on the list to investigate fully too     

> __< rucknium >__ More discussion on stressnet?     

> __< jberman >__ nothing from me     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< ofrnxmr >__ Can just set in_peers to 0, probably > <rucknium> I think we need to figure out how to have most nodes have closed ports. We'll need to do that anyway for a more realistic network topology.     

> __< jeffro256 >__ Thanks everyone      




# Action History
- Created by: Rucknium | 2026-06-17T14:59:39+00:00
- Closed at: 2026-07-01T14:52:43+00:00
