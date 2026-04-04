---
title: Monero Research Lab Meeting - Wed 10 December 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1310
author: Rucknium
assignees: []
labels: []
created_at: '2025-12-09T22:47:32+00:00'
updated_at: '2025-12-23T21:12:27+00:00'
type: issue
status: closed
closed_at: '2025-12-23T21:12:27+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Bulletproofs* (more efficient membership and range proofs)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626).

4. [Spy nodes](https://github.com/monero-project/meta/issues/1124).

5. New papers: [Lee, S., & Kim, H. (2025). Inside Qubic's Selfish Mining Campaign on Monero: Evidence, Tactics, and Limits.](https://moneroresearch.info/293) & [Venturi, A., Jerico-Yoldi, I., Zola, F., & Orduna, R. (2025). ART: A Graph-based Framework for Investigating Illicit Activity in Monero via Address-Ring-Transaction Structures.](https://moneroresearch.info/292)

6. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-12-01.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44).

7. [Proposal: Limit blocks to 32 MB, regardless of context](https://github.com/monero-project/research-lab/issues/154).

8. [FCMP alpha stressnet](https://monero.town/post/6763165).

9. Post-FCMP scaling concepts.

10. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1307 

# Discussion History
## Rucknium | 2025-12-12T00:19:55+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1310     

> __< rucknium >__ 1. Greetings     

> __< tevador >__ Hi     

> __< articmine >__ Hi      

> __< datahoarder >__ Hello world.     

> __< boog900 >__ hi     

> __< jeffro256 >__ Howdy     

> __< emsczkp:matrix.org >__ Hello     

> __< jberman >__ waves     

> __< vtnerd >__ Hi     

> __< ArticMine >__ Hi from IRC     

> __< ammortel >__ Hello      

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< tevador >__ Revisiting PQ encryption (#151).     

> __< ArticMine >__ I have reviewing the various scaling proposals     

> __< datahoarder >__ Implemented Carrot PQ derivation changes and PQ Turnstile test on my libraries, and tested convergence. Stressnet testing, launched https://stressnet.p2pool.observer/ (for as long as stressnet monerod survives). Analyzing long term Qubic log artifacts, it's ~800 GiB of compressed event logs.     

> __< rucknium >__ me: Working on analysing selfish mining with Markov Decision Process (MDP). Getting stressnet more stressed. Updated https://moneroresearch.info to the latest version of WIKINDX, with some help from plowsof:matrix.org .     

> __< jeffro256 >__ Me: Added PQ changes to spec, working on knowledge proof integration into wallet2, communicating with potential code auditors for carrot_core, reviewed some seraphis-migration PRs     

> __< jberman >__ Identified and patched issues causing broken and unreliable sync when the pool exceeds the max weight allowed, currently investigating unexpectedly slow multithreaded FCMP++ verification     

> __< vtnerd >__ Me: working on boost::beast transition in lwsf for websocket support. Otherwise bug fixes in lws+lwsf infrastructure      

> __< rucknium >__ 3. Bulletproofs* (more efficient membership and range proofs) (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626).     

> __< rucknium >__ This CCS proposal has now moved to Funding Required.     

> __< emsczkp:matrix.org >__ Hi, I’m the proposer of the Bulletproofs* research. Thank you all.     

> __< emsczkp:matrix.org >__ No additional comments beyond the previous meeting. I just wanted to let the community know that this proposal has been merged. I’m truly happy about this and I look forward to seeing it funded:     

> __< emsczkp:matrix.org >__ https://ccs.getmonero.org/proposals/emsczkp-research-folding-gbp.html     

> __< rucknium >__ More discussion of Bulletproofs*?     

> __< tevador >__ jeffro256: where can I find the PQ changes to carrot?     

> __< datahoarder >__ tevador: https://gist.github.com/jeffro256/146bfd5306ea3a8a2a0ea4d660cd2243     

> __< datahoarder >__ https://github.com/jeffro256/carrot/pull/6     

> __< jeffro256 >__ https://github.com/jeffro256/carrot/pull/6     

> __< datahoarder >__ https://github.com/seraphis-migration/monero/pull/250 for C++ code port     

> __< jeffro256 >__ jinx     

> __< jeffro256 >__ Thanks, DataHoarder     

> __< tevador >__ Thanks     

> __< rucknium >__ 4. Spy nodes (https://github.com/monero-project/meta/issues/1124).     

> __< rucknium >__ I noticed yesterday that the spy nodes on the LionLink Autonomous System Number (ASN) had disappeared from my scanner: https://moneronet.info/     

> __< rucknium >__ I think that the spy node on DigitalOcean and Hetzner are still there. About a month ago they started "hiding" themselves by not responding with the spy node fingerprint.     

> __< rucknium >__ But boog900:monero.social  may have more info     

> __< jeffro256 >__ tevador: Changes in #6 may (needs reviewing) allow a PQ switch-style migration which securely 1) opens amounts to existing amount commitments, and 2) opens key images to existing output pubkeys. The signer should be able to make a Schorr signature against their prove-spend key, univariate over the T generator, which is A) hi [... too long, see https://mrelay.p2pool.observer/e/mfeFltEKTm9ZR1hL ]     

> __< boog900 >__ I think they have just switched to these IP ranges:      

> __< boog900 >__ ```     

> __< boog900 >__ 45.13.179.0/24     

> __< boog900 >__ 82.26.133.0/24[... more lines follow, see https://mrelay.p2pool.observer/e/yZ2IltEKRlcxaTdF ]     

> __< jeffro256 >__ It destroys spend privacy for the migrated enotes, but should leave the history of the rest of the wallet hidden     

> __< boog900 >__ boog900: This is more IPs than they had before as well btw     

> __< jeffro256 >__ But they showed up with the spy fingerprint on the new range?     

> __< rucknium >__ By "just switched" we mean "switched in the last 24 hours and the scanner should display the info when it updates the data for today."     

> __< boog900 >__ jeffro256: Yep     

> __< boog900 >__ Those ranges are on a different ASN that got registered a few weeks after I found the spy nodes last year      

> __< jeffro256 >__ hmmm, does anyone have any hypothesis why they would have shown up non-fingerprinting on the old range, but fingerprinting on the new range?     

> __< rucknium >__ IMHO, it's strange that the DigitalOcean & Hetzner spy nodes fixed their spy fingerprint, but these "new" nodes coming online today did not.     

> __< rucknium >__ Two entities using the same software. One entity fixed their software.     

> __< rucknium >__ One hypothesis ^     

> __< jeffro256 >__ You think perhaps someone is selling this spy node software commercially?     

> __< rucknium >__ Maybe monitor the situation for a week and then update the official MRL ban list with the new IP ranges and announce it.     

> __< ArticMine >__ They are as part of BS     

> __< jeffro256 >__ Maybe they had an automatic deploy script, but forgot to update the deploy script      

> __< rucknium >__ jeffro256:monero.social: I don't know how plausible it is, but it's a possibility that came to my mind.     

> __< ArticMine >__ BS does not have to work, to make money. The illusion of surveillance is enough     

> __< boog900 >__ The 2 proxies always behaved a bit differently, I suggested that they might just be trying to stop us from finding their other nodes.     

> __< boog900 >__ If they keep the big subnets as obvious proxies, then they might have thought we are less likely to look for difference in behavior and find their other nodes.     

> __< rucknium >__ By the way, the second chart on moneronet.info, "Estimated number of honest nodes with ban lists enabled", increased the number of nodes with "DNS ban list enabled", but those are probably false positives.     

> __< boog900 >__ They can't really keep them hidden anyway, 2000 nodes going offline then 2000 nodes going online is pretty obvious     

> __< rucknium >__ Since no nodes on the DNS ban list are on the network anymore, all nodes don't have them in their peer lists anymore. The data in the chart is an inference, not direct measurement, based on whether nodes share banlisted peers when they perform a Levin handshake.     

> __< rucknium >__ boog900:monero.social: It's obvious when it's being monitored daily 😇     

> __< selsta >__ can someone make a fresh list for the DNS ban list that fits into DNS?     

> __< boog900 >__ https://github.com/Boog900/monero-ban-list/pull/10     

> __< rucknium >__ selsta: I suggested it here a while ago, but now the ranges should be changed to reflect the new spy ranges: https://github.com/monero-project/meta/issues/1242     

> __< boog900 >__ boog900: That's the update to my list     

> __< jeffro256 >__ Maybe we invest in a compact binary format for specifying the DNS ban list?     

> __< datahoarder >__ Binary ranges ought to work :)     

> __< datahoarder >__ Or require TCP for dns which should already be a thing with the long existing dns checkpoints     

> __< jeffro256 >__ rucknium: We could drop the old spy node ranges, which should free up a lot of space, but it would be a sneaky trick if they switched back. I guess it's faster to update a DNS record than to re-acquire a block of IPs for hosting.     

> __< rucknium >__ More honest nodes are using the DNS ban list than the MRL ban list. 55 percent versus 8 percent. Changing the DNS ban list could have a big effect.     

> __< selsta >__ ok, once https://github.com/Boog900/monero-ban-list/pull/10 is merged I'll ask mooo to update the DNS list, at least as many as fit     

> __< selsta >__ if they switch back we can update it again     

> __< jeffro256 >__ rucknium: So you're saying add it to the FCMP++ hard fork.......     

> __< datahoarder >__ There's automatic range merging plus a binary format for this would help sizes. What are the current sizes and intended target?     

> __< rucknium >__ Anyway, node operators should continue to be encouraged to update to the latest version of monerod, which has the subnet deduplication countermeasure against this type of adversary.     

> __< rucknium >__ Subnet deduplication PR by rbrunner7:monero.social  , reviewed by jeffro256:monero.social , vtnerd:monero.social , and myself: https://github.com/monero-project/monero/pull/9939     

> __< rucknium >__ More on spy nodes at this time?     

> __< rucknium >__ 5. New papers: Lee, S., & Kim, H. (2025). Inside Qubic's Selfish Mining Campaign on Monero: Evidence, Tactics, and Limits. (https://moneroresearch.info/293) & Venturi, A., Jerico-Yoldi, I., Zola, F., & Orduna, R. (2025). ART: A Graph-based Framework for Investigating Illicit Activity in Monero via Address-Ring-Transaction Structures. (https://moneroresearch.info/292)     

> __< rucknium >__ There are two new papers about Monero. I read both of them.     

> __< rucknium >__ I liked the Qubic paper. I don't agree with every methodological decision, but they did a good job in a short period of time IMHO.     

> __< rucknium >__ It concludes that Qubic did not achieve a 51% attack and Qubic's block-orphaning strategy was usually less profitable than if they had just mined honestly.     

> __< datahoarder >__ They used on-chain data plus tasks form Qubic. They lacked a lot of data but still aggregated them consistent to what we also found with larger set of data and internal hashrates     

> __< rucknium >__ In Section III(A), they seem to say that they assume Qubic's hashpower share is the share of main-chain blocks that they mine. This seems incorrect because it ignores orphaned blocks of honest miners and Qubic and blocks that Qubic never broadcasted to the network.     

> __< rucknium >__ datahoarder:monero.social: Do you agree that's what they did?     

> __< rucknium >__ They still have data on the orphaned blocks that propagated through the network, but they don't use it to compute "effective hashpower"     

> __< rucknium >__ AFAIK     

> __< datahoarder >__ They did gather a limited selection of orphan blocks. They describe how they gathered the data, one by querying Monero nodes for blocks and historical orphans, and second by polling one of Qubic RPC that gives the current task     

> __< datahoarder >__ The current task includes all possible Qubic block templates, so they can find orphans as well that never get published     

> __< jeffro256 >__ > <rucknium> In Section III(A), they seem to say that they assume Qubic's hashpower share is the share of main-chain blocks that they mine. This seems incorrect because it ignores orphaned blocks of honest miners and Qubic and blocks that Qubic never broadcasted to the network.     

> __< jeffro256 >__ If true, then this is the exact same misunderstanding of PoW that the Qubic founder leveraged to claim a "51%" attack, which they later retracted. As you probably know, you don't just need more than 51% of the blocks, you need 51% of the active hashpower, which is not the same thing.     

> __< datahoarder >__ But indeed, they didn't do a similar comparison of hashrates when taking into account missing data. That's the flaw I see, they lacked large sets of data for orphans or actual hashrates.     

> __< datahoarder >__ I did get a different understanding of that section, I'll re-read.     

> __< jeffro256 >__ That is a pretty big mistake for a researcher to make when selfish mining is the main topic of the paper IMO.     

> __< datahoarder >__ Yeah, that would be a major criticism as well. That's a root base that they use for assumptions later on so if that's flawed, the simulations may be too     

> __< rucknium >__ > Figure 1 shows Qubic’s mining power share in the Monero network, computed as the ratio of Qubic-attributed blocks to all main-chain blocks over weekly, daily, and hour windows. Since direct telemetry of the pool’s physical hashrate is unavailable, we rely on this ‘effective hashrate’ realized on-chain as the primary metric (α) for our selfish mining models.     

> __< rucknium >__ ^ That's the passage I'm interpreting     

> __< datahoarder >__ Their estimates found a lower efficiency than observed in the real world. This may be due to that flawed assumption (our quick checks using more complete data of orphans on both sides showed -20 to -12% efficiency loss)     

> __< datahoarder >__ rucknium: Aha! They later touch on it if I remember correctly, that they may have underestimated hashrate     

> __< jeffro256 >__ Eek, yeah if you take their word in that passage Rucknium quoted, then they messed up that calculation.     

> __< rucknium >__ Or maybe "Qubic-attributed" blocks also means Qubic's orphaned blocks. But then it doesn't make sense to not include the honest miners' orphaned blocks.     

> __< datahoarder >__ That's why they have a whole section on the observed values not matching simulations. The actual state machine for the simulation is pretty accurate to observed behavior otherwise     

> __< rucknium >__ I note that they use the original Eyal & Sirer (2013) theoretical selfish mining behavior.     

> __< rucknium >__ Later papers showed that the selfish mining behavior proposed by Eyal & Sirer (2013) was not optimal. Selfish miners could get a little more revenue by following a more complex decision rule. You find the decision rule by setting up Markov Decision Process (MDP) analysis. In MDP, you define the objective (i.e. maximize self mi [... too long, see https://mrelay.p2pool.observer/e/2t7zltEKNFhZUl9F ]     

> __< jeffro256 >__ I wonder if Qubic had many of their blocks orphaned in practice. If I had to guess, it's probably not big enough to be important     

> __< rucknium >__ The Eyal & Sirer (2013) strategy instructs the selfish miner to broadcast its block if its chain is one block ahead of the honest chain. But often Qubic would broadcast when it was two blocks ahead. The two-blocks-ahead strategy is less profitable, but less risky if Qubic's block propagation is slow.     

> __< rucknium >__ datahoarder:monero.social: Do you have something to say about jeffro256:monero.social 's guess?     

> __< datahoarder >__ jeffro256: They did, specially around the threshold levels     

> __< datahoarder >__ I have the dumps I published every week until they stopped selfish but they had quite many in the list that can be proven     

> __< jeffro256 >__ jeffro256: TBC, by orphaned, I mean Qubic's blocks which made it on the main chain of most other nodes, but then were beat out. I'm not talking about blocks in side chains which Qubic decided to abandon before they were longer than main     

> __< datahoarder >__ Aha. Most of those are 1-2 deep only     

> __< datahoarder >__ I am parsing the event logs so I'll have more info on this later     

> __< rucknium >__ jeffro256:monero.social: They plot Qubic's orphaned blocks in Fig. 1 on page 3.     

> __< jeffro256 >__ datahoarder: Are these dump from Qubic mining pool or from your node?     

> __< datahoarder >__ It's a dump of the equivalent of their inner stratum tasks and solutions - with 600M difficulty granularity     

> __< datahoarder >__ Events logged to the millisecond across several networks PoV and across Monero nodes     

> __< datahoarder >__ (And other data, Tari blocks, task server they had, it's ~800 GiB of compressed event logs)     

> __< ravfx:xmr.mx >__ I noticed the spy nodes stopped to try to connect to my node on the 6 of this month.     

> __< ravfx:xmr.mx >__ Adding the new IPs everywhere.     

> __< ravfx:xmr.mx >__ https://mrelay.p2pool.observer/m/xmr.mx/uXaEUNvsxSEQSiBksYMvRZHy.png (clipboard.png)     

> __< rucknium >__ What I'm trying to do now is 1) Fit tevador's "Share or Perish" (https://github.com/monero-project/research-lab/issues/146) suggestion into MDP and 2) Develop an alternative MDP objective that maximizes disruption instead of maximizes the adversary's revenue.     

> __< rucknium >__ Qubic wasn't trying to maximize revenue. They were interested in the propaganda value of disruption, IMHO. So we want to know how the proposed countermeasures would inhibit disruptive mining instead of just selfish mining.     

> __< datahoarder >__ If you want specific pre-parsed data around Qubic I have an aggregate list, though not posted publicly (it's incomplete, pending parsing of full logs which I can't do live, we are still gathering data). If you want this incomplete list, DM me     

> __< rucknium >__ I will probably make my Monerotopia Conference talk in February about Qubic and selfish/disruptive mining. Possibly with some collaboration.     

> __< datahoarder >__ rucknium: Indeed. There's entities extracting maximum value and entities extracting maximum damage or marketing     

> __< datahoarder >__ What about the other paper if there isn't more on Qubic?     

> __< rucknium >__ The other paper is Venturi, A., Jerico-Yoldi, I., Zola, F., & Orduna, R. (2025). ART: A Graph-based Framework for Investigating Illicit Activity in Monero via Address-Ring-Transaction Structures. (https://moneroresearch.info/292)     

> __< rucknium >__ I didn't really like this paper. It fit a machine learning model on 19 transactions from 2017 and tried to validate detection of behavioral traits in txs.     

> __< rucknium >__ In 2017, Monero didn't even require a fixed ring size, so they could use ring size as a predictor.     

> __< rucknium >__ IMHO, training ML on RingCT Monero txs is a dead end because you cannot get a valid training set.     

> __< ArticMine >__ There was a minimum ring size     

> __< rucknium >__ Even if you have info from centralized exchanges, those txs are obviously a biased sample that would not reflect general user behavior outside of interaction with a centralized exchange.     

> __< rucknium >__ Yes, minimum ring size in 2017, but AFAIK, users could select higher than the minimum if desired.     

> __< ArticMine >__ Yes they could. I used a much higher ring size in 2018 to extract the Monero Original safely.      

> __< jeffro256 >__ A minimum of two ring members causes decoy elimination cascading attacks. Was that the limit enforced in 2017, or was that already known by then and the minimum greater than 2?     

> __< ArticMine >__ The minimu as I recall was 5     

> __< rucknium >__ These two papers brings the count to 10 of Monero papers written by non-MRL affiliated researchers in 2025. Nice to have the auxiliary platoon of external researchers 😎     

> __< rucknium >__ The other 8 are     

> __< rucknium >__ Thakore, V., & Vijayakumaran, S. (2025). MProve-Nova: A Privacy-Preserving Proof of Reserves Protocol for Monero. Proceedings on Privacy Enhancing Technologies, 2025(2), 582–606. (https://moneroresearch.info/266)     

> __< rucknium >__ Yang, X., Xu, L., & Zhu, L. (2025). De-anonymizing Monero: A Maximum Weighted Matching-Based Approach. IEEE Transactions on Information Forensics and Security. (https://moneroresearch.info/260)     

> __< ArticMine >__ I used like 255 to ensure common rinngs on both chains greater than 5 for the Monero Original extration     

> __< rucknium >__ Lee, J., Choi, G., Han, J., & Park, J. (2025). Advanced Monero wallet forensics: Demystifying off-chain artifacts to trace privacy-preserving cryptocurrency transactions. Forensic Science International: Digital Investigation, 54, 301988. (https://moneroresearch.info/290)     

> __< jeffro256 >__ According to the README, there was already of minimum of 3 by 2016, which got increased to 5 in 2017.     

> __< rucknium >__ Kopyciok, Y., Victor, F., & Schmid, S. (2025). Moneros Decentralized P2P Exchanges: Functionality, Adoption, and Privacy Risks. (https://moneroresearch.info/270)     

> __< rucknium >__ Kopyciok, Y., Schmid, S., & Victor, F. (2025). Friend or Foe? Identifying Anomalous Peers in Moneros P2P Network. (https://moneroresearch.info/280)     

> __< rucknium >__ Shi, R., Peng, Z., Lan, L., Ge, Y., Liu, P., & Wang, Q., et al. 2025, February 24–28, Eclipse Attacks on Monero’s Peer-to-Peer Network. Unpublished paper presented at Network and Distributed System Security (NDSS) Symposium 2025. (https://moneroresearch.info/248)     

> __< ArticMine >__ 25*     

> __< rucknium >__ Gao, Y., Zhang, Y., Piškorec, M., & Tessone, C. J. (2025). Monero Peer-to-peer Network Topology Analysis. (https://moneroresearch.info/278)     

> __< rucknium >__ Gao, Y., Piškorec, M., Zhang, Y., Vallarano, N., & Tessone, C. J. (2025). Charting the Uncharted: The Landscape of Monero Peer-to-Peer Network. (https://moneroresearch.info/267)     

> __< rucknium >__ More discussion on these papers?     

> __< ravfx:xmr.mx >__ They also moved the tor/i2p spy nodes too     

> __< jeffro256 >__ Does the BulletCT paper count? ;)     

> __< rucknium >__ ravfx:xmr.mx: These were the spy nodes spying on the i2p and tor networks in general, right?     

> __< rucknium >__ Then, 11 😀 Wang, N., Wang, Q., Liu, D., Esgin, M. F., & Abuadbba, A. (2025). BulletCT: Towards More Scalable Ring Confidential Transactions With Transparent Setup.   https://moneroresearch.info/285     

> __< rucknium >__ 6. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-12-01.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44).     

> __< ArticMine >__ I have spent some time reviewing the various proposals. In particular boog900     

> __< ArticMine >__ the laater would make a good choice for a mature chain over 1000 transactions per second. If one tries to modify it then the maximum annual growth rate grows over 2.5%.      

> __< ravfx:xmr.mx >__ rucknium: yeah, but they have a big collection of them at LIONLINK     

> __< ravfx:xmr.mx >__ had*     

> __< ArticMine >__ This issue is that we need the ability of ML to change in order to accommodate the variability in transaction rates that has been identified in the past both in Monero and other chains including over 100x in Bitcoin and Litecoin     

> __< boog900 >__ I think my proposal is too aggressive if anything, but it is an improvement over what we have currently.      

> __< ArticMine >__ Then we hate the issue of too high an annual growth rate.      

> __< rucknium >__ boog900:monero.social: Can you post the link?     

> __< ArticMine >__ My take is that  my proposal with the Nielsen's Law caop is the way to go      

> __< boog900 >__ https://github.com/seraphis-migration/monero/issues/44#issuecomment-3617687600     

> __< ArticMine >__ We are capping the annula growth rate to below 1.389 x     

> __< ArticMine >__ There is also no need for fixed caps     

> __< ArticMine >__ and we have a predictable max block weight with time.      

> __< ArticMine >__ Like ~7 years to reach 100 MB for example     

> __< boog900 >__ 1024x max growth in a year is completely unnecessary     

> __< boog900 >__ 47x is too but it is much better      

> __< ArticMine >__ There is no max growth of 1000x in a year      

> __< sgp_ >__ Personally I'd consider a 100x capacity change in the short term to be unimportant. Without it, worst case fees go up in the short term. I don't consider this a failure. I don't see short term higher fees as a devastating failure of the goal of p2p cash     

> __< boog900 >__ ArticMine: 16x in short term 2x every ltm adjustment     

> __< ArticMine >__ I ran a bitcoin node in 2017 - 2018. Over 2 TB of data in a month     

> __< ArticMine >__ Bitcoin stly fee markes can be easily spammed     

> __< ArticMine >__ that was over a 50 Mbits DSL line     

> __< ArticMine >__ boog900 You have the cap at 1.390 ..     

> __< ArticMine >__ That is the key change     

> __< boog900 >__ articmine:monero.social: has said mine is good for a mature network, I believe my proposal also allows us to reach a mature level (according to artic) in a reasonable amount of time     

> __< boog900 >__ I SAID MAX GROWTH.      

> __< ArticMine >__ I know max growth     

> __< ArticMine >__ is way faster     

> __< ArticMine >__ but are people prepard to accept this with no caop?     

> __< ArticMine >__ Or conntroversial fied limits?     

> __< boog900 >__ Max growth in a single year makes the sanity cap meaningless as eventually it grows enough to not restrict a years worth of growth      

> __< ArticMine >__ If that is the case then the market is taking care of things     

> __< ArticMine >__ This is not a case to argue against the underlaying scaling     

> __< boog900 >__ why do we need to plan for no growth for 14 years then gigabyte blocks in 1 year?     

> __< ArticMine >__ And I mean ovr a decade of more     

> __< boog900 >__ ArticMine: it is as otherwise we are just relying on the sanity cap to keep us secure      

> __< ArticMine >__ We are not planning for no growth for 17 years     

> __< boog900 >__ another bandaid solution, just like the ones that got monerod in the state it is      

> __< ArticMine >__ we can have 1000 tpd in 14 years     

> __< ArticMine >__ tps     

> __< boog900 >__ we do not need 1024x in a single year     

> __< ArticMine >__ This is far from no growth     

> __< jberman >__ I think boog900:monero.social  raises good arguments against exponential cap, in favor of more reasonable allowed max growth params     

> __< boog900 >__ we can have a gradual increase if you believe we wont have all the growth in 1 year      

> __< sgp_ >__ Even if we allow, say, 2x growth per year max, that will still catch up to the sanity cap over time     

> __< ArticMine >__ We have an under 1.4x per cap How many time do I have to repeat this?     

> __< boog900 >__ brooooo     

> __< jeffro256 >__ Why not both? I thought that the exponential cap was an additional sanity check on the long term medium, which itself is limited by the historical block sizes.     

> __< ArticMine >__ That is what it is     

> __< jeffro256 >__ It's not like the block size is allowed to immediately jump up to sanity cap      

> __< boog900 >__ my proposal has that as optional jeffro256:monero.social, I don't think it is needed with it though     

> __< ArticMine >__ Both are integrated into my proposal     

> __< boog900 >__ the underlying scaling is slow enough without it IMO     

> __< jeffro256 >__ So why does it hurt, in your eyes? Just extra unnecessary complexity?     

> __< ArticMine >__ 2.5x is greater compunded than 1.4x     

> __< boog900 >__ jeffro256: yes      

> __< boog900 >__ ArticMine: 2.5x is literally maxing out scaling      

> __< boog900 >__ 1.4x is always increasing, no matter what     

> __< ArticMine >__ It is actually too high over time     

> __< boog900 >__ I agree     

> __< boog900 >__ ^ > <boog900> I think my proposal is too aggressive if anything, but it is an improvement over what we have currently.      

> __< jeffro256 >__ TBF, if implementeting the sanity cap as a function of the block height, it could be extremely helpful as a quick stateless pre-check     

> __< ArticMine >__ Then what is the problem with under 1.4x?     

> __< boog900 >__ we can lower it?     

> __< boog900 >__ ArticMine: BECAUSE IT INCREASES NO MATTER WHAT      

> __< ArticMine >__ We have a cap ML can stay at 2x and allow or the necessary felxibilty     

> __< boog900 >__ you have a shit scaling algo with a sanity ontop that makes it kinda ok for some years/.      

> __< ArticMine >__ It is a sanity cap     

> __< boog900 >__ why not just have a good scaling algo     

> __< ArticMine >__ It is not possible to do both     

> __< boog900 >__ it really is     

> __< ArticMine >__ You eithe lock up the short term or allow massive grwoth in the long term     

> __< boog900 >__ why do we need 1024x max growth in a year     

> __< ArticMine >__ 16*32 =512 please     

> __< boog900 >__ that is under a year 1024x is a little over a year     

> __< boog900 >__ I said this in my comment      

> __< ArticMine >__ With a 1.4 cap Please     

> __< ArticMine >__ 1.4x     

> __< boog900 >__ oh my days      

> __< boog900 >__ can we just vote?     

> __< gingeropolous >__ i think all the proposals would need to be up somewhere with things clearly laid out before a vote     

> __< kayabanerve:matrix.org >__ Should we literally just have a vote on 1.4x YoY or 1.4x prior year?     

> __< ArticMine >__ Yes 2.5x per year vs under 1.4x per year     

> __< gingeropolous >__ everythings buried in comments and threads blah blah blah     

> __< kayabanerve:matrix.org >__ Should we first agree to defer to a vote after consensus this isn't going anywhere?     

> __< rucknium >__ What would the voting process be and what would it accomplish?     

> __< boog900 >__ I really don't like how you are framing this ArticMine     

> __< boog900 >__ really disingenuous      

> __< ArticMine >__ the maximum growth     

> __< gingeropolous >__ i think our terminology is also mixed     

> __< ArticMine >__ What is wrong with thatSo we vote between my proposal and boog900s?     

> __< articmine >__ rucknium: I would like to know myself?     

> __< jberman >__ I generally agree with ginger, it's a bit hard to follow and I'm decently well versed in the scaling algo params. Where did 2.5x come from?     

> __< jeffro256 >__ Even so, 512x is too much. Assuming that only 10000 people use Monero now, a 512x growth rate means that every man, woman, and child on the planet would be migrated Monero in ~2.2 years. > <ArticMine> 16*32 =512 please     

> __< sgp_ >__ This conversation is so silly. Why can't we do something like 1.4x sanity cap which is ever increasing, but instead of allowing >100x growth in any single year based on demand, why not limit that to 2x or so max per any single year. Not 512x-ish     

> __< ArticMine >__ I have my ptoposal on github for everyone to review     

> __< boog900 >__ jberman: a ltm multiplier of 1.2 with 5 adjustments      

> __< ArticMine >__ This is getting pointless     

> __< sgp_ >__ Which goes to my point that the "feature" of >100x growth per year to accommodate demand should be an explicit non-goal > <ArticMine> This issue is that we need the ability of ML to change in order to accommodate the variability in transaction rates that has been identified in the past both in Monero and other chains including over 100x in Bitcoin and Litecoin     

> __< jbabb:cypherstack.com >__ the point is to patch the big bang block bug/attack     

> __< articmine >__ An under 1.4x per year maximum cap     

> __< articmine >__ Even this is not enough      

> __< boog900 >__ I don't see everyone coming to consensus on a single algo, a vote is just to decide the scaling algo by majority.     

> __< articmine >__ There are 2 Lagos on the table      

> __< articmine >__ algos     

> __< boog900 >__ sgp_: isn't this pretty much my proposal?      

> __< sgp_ >__ Yeah I think the thinking largely aligns     

> __< jeffro256 >__ I agree that 1.4x per year probably isn't enough if we actually expect the real long term median block size to hit this sanity cap. 1.4x growth per year means that it would take 4 decades to reach global adoption assuming 10,000 users now.  > <articmine> An under 1.4x per year maximum cap     

> __< boog900 >__ articmine: I really hate how you are just closing your ears to all arguments      

> __< gingeropolous >__ right. Lets perhaps start with terms. I think we generally agree that theres a short term median, and blocks can grow 2x the median. Then there's a long term median, and blocks currently can grow to 50x the LTM. What is that 50x factor called? These are the dynamic caps. Then we have possibly 2 additional caps coming into play [... too long, see https://mrelay.p2pool.observer/e/kNnHmNEKcHFoRTY5 ]     

> __< articmine >__ boog900: I am t     

> __< boog900 >__ like on the one hand you say mine is more aggressive on the other you say we want a more restrictive algo?     

> __< sgp_ >__ arguing "2.5x vs 1.4" is not accurate. One increases only with demand, the other increases regardless of it.  They can be combined together     

> __< sgp_ >__ which is what boog suggested     

> __< gingeropolous >__ lets seperate dynamic caps and non-dynamic caps. dynamic here is referring to chain usage. not just blockheight      

> __< sgp_ >__ growing 2.5x in any given year is plenty generous imo     

> __< boog900 >__ gingeropolous: the short term multipler is what I have been calling that 50x number, basically it means the median can rise 50x in the short term (before an adjustment of the long term median). This means we can have blocks 100x the size of the current long term median before any adjustments as blocks can be 2x the median.     

> __< articmine >__ sgp_: Yes they can. This allows the harm done by the BS companies to Monero to be baked into the consensus protocol     

> __< articmine >__ So if the suppression continues we can't recover      

> __< articmine >__ We come back to the conflict of interest      

> __< gingeropolous >__ is the main contention over the non-dynamic caps?     

> __< boog900 >__ oh my days      

> __< sgp_ >__ the fundamental thinking difference is that Artic considers high fees in the short term (if demand grows faster than block space increases) to cause the permanent failure of Monero's p2p usage. But it's simply not possible to always guarantee low fees even with aggressive scaling space afforded     

> __< articmine >__ The main contention is allowing catch up after suppression      

> __< articmine >__ So if Monero is suppressed for say a decade we can't recover      

> __< sgp_ >__ Any annual growth over 1.4 is recovering towards the sanity cap     

> __< boog900 >__ if we needed 10000x, your 1000x would also not allow us to recover.       

> __< articmine >__ The sanity cap grows during the suppression period      

> __< boog900 >__ what makes 1000x special?      

> __< articmine >__ It is not      

> __< jeffro256 >__ IMO, if implemented non-dynamic caps (e.g. the 1.4x sanity limit) should be very liberal (i.e. non-limiting) with today's conditions. They should only kick in when we predict that the hardware/bandwidth  requirements would cause severe decentralization issues. The dynamic caps should be the real bottlenecks under current and [... too long, see https://mrelay.p2pool.observer/e/2LzimNEKbTFZaDl5 ]     

> __< boog900 >__ jeffro256:monero.social: do you think my values are good, ignoring the sanity cap for now?     

> __< articmine >__ The sanity cap is not a band aid     

> __< jeffro256 >__ In my opinion, hoping that state/BS-organized suppression would heal itself if we allow more transactions on the chain is wishful thinking.  > <articmine> So if Monero is suppressed for say a decade we can't recover      

> __< gingeropolous >__ ok, so sanity cap = 1.4x thing, the neilson law thing. The hard cap is the 90MB proposed thing.      

> __< articmine >__ jeffro256: No the state suppression is overturned by the courts     

> __< articmine >__ Then Monero needs to recover     

> __< articmine >__ That is the issue      

> __< boog900 >__ FWIW you can calculate a maximum block size without an explicit sanity limit       

> __< boog900 >__ so you can get the max size of a block at a specific height     

> __< gingeropolous >__ so if the sanity cap starts at 10MB, that gives us 660k tx/day for year 1, which is about where bitcoin stands, today     

> __< jeffro256 >__ jeffro256: You can't heal price suppression except by increasing trust in your product / mission. As long as transactions are not prohibitively expensive for day-to-day use (which I don't think they would be with a 2x dynamic short-term limit), then I think allowing spam would harm trust more than the friction due to said on-chain fees.     

> __< boog900 >__ boog900: the closer you starting block the lower that number will be too.     

> __< jeffro256 >__ Yours has max dynamic growth of 2.5x? > <boog900> jeffro256:monero.social: do you think my values are good, ignoring the sanity cap for now?     

> __< jeffro256 >__ Ignoring sanity limit ofc     

> __< articmine >__ gingeropolous: Yes but if you drastically reduce the underlying scaling , then we cannot recover from state suppression     

> __< boog900 >__ jeffro256: so in the short term it allows 16x then after that every ltm adjustment is 1.2x. So in the first year 40 to 47x every year after that 2.5x     

> __< articmine >__ Bitcoin today is a disaster as peer to peer cash      

> __< jbabb:cypherstack.com >__ jeffro256: increasing trust and/or usability. enabling swaps would be a workaround     

> __< gingeropolous >__ the dynamic stuff? thats very liberal no matter how we cut it. the multiplier being 50x or 16x, it'll hit the sanity cap quickly     

> __< articmine >__ It is heavily price     

> __< articmine >__ Priced     

> __< boog900 >__ boog900: Artic is 512x to 1024x in the first year then 32 to 64x in the years after.      

> __< articmine >__ It has NOT happened in 11 years      

> __< articmine >__ With more aggressive scaling and NO sanity cap      

> __< articmine >__ We are not ZCash which was spammed to 300x in blocksize      

> __< jberman >__ boog900:monero.social: what if you brought the params down further such that yearly growth is capped at 1.4x via dynamic scaling?     

> __< articmine >__ jberman: It will not work at a     

> __< articmine >__ AKL     

> __< gingeropolous >__ well that'd be even worse for the suppression hypothesis  jberman:monero.social     

> __< boog900 >__ jberman: I would prefer it to be 2x, I think it is safe enough. What I don't like is the 16x in the short term.      

> __< boog900 >__ I would prefer that to be lower, if that could get consensus.      

> __< elongated:matrix.org >__ articmine: Not yet     

> __< jeffro256 >__ How is 2.5x max growth acquired from a 1.2x LTM increase, assuming STM is maxed out? Maybe I'll just have to do the math lol > <boog900> so in the short term it allows 16x then after that every ltm adjustment is 1.2x. So in the first year 40 to 47x every year after that 2.5x     

> __< boog900 >__ jeffro256: 1.2 ^ 5     

> __< articmine >__ 1.2^5     

> __< jeffro256 >__ jberman: You didn't ask me lol, but that's much too conservative for my taste     

> __< jeffro256 >__ articmine: Isn't LTM 100K blocks, which would mean 1.2 ^ ~2.6?     

> __< kayabanerve:matrix.org >__ I think the abundance hypothesis is put forth by agitators in an attempt to split the community and degrade the network's performance, meaning we should strike a reasonable balance (what's being labelled the 'suppression hypothesis', despite still allowing for 40% growth of use YoY) in order to ensure network quality, stabilit [... too long, see https://mrelay.p2pool.observer/e/mLWOmdEKRDRZRURf ]     

> __< tevador >__ It's 100K blocks, so it can grow every 50K blocks.     

> __< boog900 >__ boog900: if we have an adjusted ltm at 10 MB, so adoption brings us to 10 MB for a few years, then 16x means we could have 160 MB before a ltm adjustment, 1024x means 10 GB.     

> __< articmine >__ kayabanerve:matrix.org: Really     

> __< boog900 >__ wait no I said that wrong my bad     

> __< gingeropolous >__ so the hypothetical scenario is that The Law somehow abolishes blockchain surveillance companies, and then within a matter of days there are millions of txs per day on the monero blockchain (?)     

> __< boog900 >__ both proposals have 16x in the short term.      

> __< rucknium >__ articmine:monero.social: /s means that kayabanerve:matrix.org  meant the comment sarcastically.     

> __< kayabanerve:matrix.org >__ I know that isn't actually a helpful comment, but I feel obliged to point out how absurd some of this discussion had been and still is     

> __< kayabanerve:matrix.org >__ No one suggesting scaling usage 40% per year should be considered suppressive.     

> __< articmine >__ Yours has very stiff pricing with no scaling growth      

> __< tevador >__ People on matrix: please try to keep your messages <500 characters. It's very hard to read the conversation on IRC otherwise.     

> __< ofrnxmr >__ kayabanerve:matrix.org: 40% from 300kb-650kb, i would definitely consider suppressive     

> __< articmine >__ kayabanerve:matrix.org: I agree     

> __< kayabanerve:matrix.org >__ Sorry, I meant to send my messages in immediate succession but my internet had a hiccup     

> __< kayabanerve:matrix.org >__ My following messages obviously elaborate on the "/s" originally included but lacking comprehension     

> __< jeffro256 >__ I think 40% can be too conservative at today's size, but on the other hand, at a VISA level size, it would be absurd to think that we could expand 40% in one year.     

> __< kayabanerve:matrix.org >__ I meant to point out the absurdity, not leave it hanging for three minutes 😅     

> __< kayabanerve:matrix.org >__ Doesn't that simply suggest we need a larger base, as these proposals already include?     

> __< kayabanerve:matrix.org >__ My primary comment was solely 40% of the year's usage, even if not 40% of the prior year's +40%, shouldn't be considered suppressive     

> __< boog900 >__ what do we think the best path to consensus is?      

> __< sgp_ >__ jeffro256: As long as we don't start with Visa's allowance, Monero will always trail it in adjusted performance terms (assuming tech keeps getting better)     

> __< rucknium >__ jeffro256:monero.social: Isn't this the tyranny of exponential growth and a reason to not have exponential growth indefinitely?     

> __< kayabanerve:matrix.org >__ I'd advocate complete proposals, potentially independent or not, and voting     

> __< rucknium >__ I will again point to the logistic growth curve.     

> __< kayabanerve:matrix.org >__ My proposal was for an independent knob. I don't see why 1.4x usage can't be an independent knob.     

> __< jeffro256 >__ Artic, what do you think of Boog900's proposal as-is?     

> __< rucknium >__ Which is classically the theoretical curve of adoption of a new technology.     

> __< gingeropolous >__ and the proposals should have graphs. graphs!     

> __< kayabanerve:matrix.org >__ I agree independent proposals mashed together can be suboptimal, but we need at least clear, complete proposals, and the issue with proposals as large as AM's is the specific nitpicking     

> __< rucknium >__ Ah, but Arrow's Paradox ;)     

> __< kayabanerve:matrix.org >__ Hence my proposal for independently voting on static capacity and a sanity cap     

> __< ofrnxmr >__ Anyway, my vote is     

> __< ofrnxmr >__ * 40% YoY (regardless of volume). Baseline of 10mb     

> __< ofrnxmr >__ * something like 50x max growth (based on volume) in 1yr (not 1000x, not 1.5x)     

> __< ofrnxmr >__ * 90mb default max miner template (not hard cap)     

> __< tevador >__ 16x STM, 1.2x LTM and ZM = 625 000 + sanity cap starting at 10 MB seems reasonable to me.     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: we can also acknowledge impossibility and give up, so true     

> __< boog900 >__ the voting has started it seems :p     

> __< rucknium >__ I mean, Arrow's Impossibility Theorem.     

> __< jeffro256 >__ rucknium: I do like a good logistical curve. The one issue I see with this is that we have to determine an absolute top of the curve which encodes when "complete" adoption is hit.      

> __< rucknium >__ jeffro256:monero.social: I agree that is a limitation. But you could relax the ceiling with linear growth at that point or something.     

> __< tevador >__ The 40% YoY growth could be limited to ~20 years, which is enough to reach VISA-level throughput.     

> __< kayabanerve:matrix.org >__ I would like to end the McCarthyism though     

> __< gingeropolous >__ 2x STM, 50x LTM and ZM = 300 000 . These are the current params, right?     

> __< ofrnxmr >__ tevador: Depends on size of future txs. So i dont think its really necessary to cap atm.     

> __< boog900 >__ gingeropolous: 50 STM, 1.7 LTM     

> __< gingeropolous >__ ok. got it     

> __< tevador >__ Well, if PQ transactions are 1 MB, then yes, we have a problem. But that's for another time.     

> __< kayabanerve:matrix.org >__ The network isn't ossified and we can adjust the formulas for PQ TXs with the PQ fork     

> __< jberman >__ tevador: I'm ok with this as well     

> __< boog900 >__ tevador: is this 16x as is artic's 16x or my 16x (so 8)?     

> __< articmine >__ jeffro256: That was my point regarding boog900 proposal     

> __< articmine >__ One can lower the limit over say 1000 TPS     

> __< articmine >__ But now we need maximum flexibility and the possibility of growth below the  cap     

> __< articmine >__ So we should keep the 2x on ML at least until we reach 1000 TPS      

> __< jeffro256 >__ rucknium:monero.social:  That's not a bad idea. Will we be ossified by the point humanity achieves intergalatic space travel? Will cryptocurrencies be needed at that point? Probably by the time that humanity leaves Earth, if such a time comes, hopefully there is enough rough consensus on Earth to fork to support non-trivial l [... too long, see https://mrelay.p2pool.observer/e/ib3QmdEKV3VOSzk3 ]     

> __< boog900 >__ boog900: artic changed the scaling algorithm so a 8x stm before which allowed 16x max size blocks in the short term now it is the same so a 16x stm allows 16x max size      

> __< boog900 >__ it is basically a more aggressive algorithm for the same max size.     

> __< tevador >__ boog900: I'm talking about the maximum legal block size limit, so I think it's yours.     

> __< boog900 >__ nice 👍     

> __< articmine >__ A larger base opens the door to spam > <kayabanerve:matrix.org> Doesn't that simply suggest we need a larger base, as these proposals already include?     

> __< tevador >__ 625 000 * 16 = 10 MB sanity cap     

> __< gingeropolous >__ or we make the short term more flexible by allowing 4x the median 100 blocks instead of 2x     

> __< gingeropolous >__ and that would keep fees lower during these expansions     

> __< ofrnxmr >__ gingeropolous: i think its already too reactive at 100 blocks, but i digress     

> __< tevador >__ I think doubling every 100 minutes is plenty fast.     

> __< ofrnxmr >__ +1     

> __< gingeropolous >__ aye     

> __< rucknium >__ I also assume that Monero transactions are directly related to the real economy (https://en.wikipedia.org/wiki/Real_economy) instead of the financial economy. Therefore, the number of txs per person is limited since people have limited time in a day and limited demand for txs. And the number of people on the planet is leveling off.     

> __< jberman >__ Also fwiw, I generally agree a fixed cap probably is not required at conensus with sane params in the scaling algo and especially not with the 1.4x sanity cap starting at 10mb > <ofrnxmr> Anyway, my vote is     

> __< kayabanerve:matrix.org >__ jeffro256:monero.social: intergalactic p2p communication >:(     

> __< jberman >__ Once blocks start creeping up, if the node isn't re-architected in time / prepared, then there should be ample time to put a cap in place if the network would die without .. especially with the sanity cap     

> __< articmine >__ A tight base with 2x on ML is better      

> __< gingeropolous >__ well i don't have these abbreviations memorized so im out     

> __< rucknium >__ You could put a lower cap on the block templates that the monerod RPC generates. That doesn't stop a malicious miner nor miners who change the code and re-compile, but it could stop miners from mindlessly leading each other off a cliff like lemmings.     

> __< rucknium >__ p2pool has its own method, but that can be managed too.     

> __< tevador >__ Yes, a limit can be soft forked later if needed.     

> __< ofrnxmr >__ rucknium: imo this is more sane than adding a 90mb hard cap     

> __< ofrnxmr >__ Just add a 90mb default max template     

> __< ofrnxmr >__ Like btc op codes, can just change the param later (even using a runtime flag) instead of having to fork to allow the larger blocks     

> __< tevador >__ The problem is that AFAIK you need just 1 block over 100 MB to kill the network.     

> __< rucknium >__ IMHO, many miners would lead each other off a cliff irrationally. It happened to PirateChain. And Monero mining pools used to have deplayed block template updating that cost them fee revenue.     

> __< ofrnxmr >__ tevador: no, the 1 block wouldnt transmit     

> __< ofrnxmr >__ The miner would get forked off     

> __< boog900 >__ not if it is fluffy      

> __< rucknium >__ PirateChain miners causing netsplits because of excessive block verification time: https://web.archive.org/web/20230803171107/https://old.reddit.com/user/SignificantRoof5656/comments/15h9reh/pirate_chains_045_spam_attack_2_months_later/     

> __< articmine >__ And safer     

> __< jeffro256 >__ Or it would only partially transmit, depending on network conditions. This would give miners making too-big blocks a severe disadvantage.      

> __< ofrnxmr >__ boog900: in which case the network would survive, but bootstrapping wouldnt     

> __< boog900 >__ ofrnxmr: the network would split      

> __< boog900 >__ or well could split     

> __< boog900 >__ 2 or more different chains which allows double spending on each one.     

> __< tevador >__ ofrnxmr: That might not be true if we sync headers first at some point.     

> __< jberman >__ ofrnxmr: I'd call this more like "chicken running around with its head cut off"     

> __< ofrnxmr >__ Anyway, id avoid hard cap and do template max defaults. Gives us 6yrs to fix the situation properly and doesnt require a hf to deploy     

> __< rucknium >__ We can hit the next agenda item since it's being discussed already     

> __< rucknium >__ 7. Proposal: Limit blocks to 32 MB, regardless of context (https://github.com/monero-project/research-lab/issues/154).     

> __< kayabanerve:matrix.org >__ It can be broadcast bit not synced or scanned, or so     

> __< ofrnxmr >__ Repeating "Just add a 90mb default max template"     

> __< kayabanerve:matrix.org >__ Unless the sync process also separates TXs out     

> __< jeffro256 >__ NACK to 32MB non-dynamic limit, sorry Kayaba     

> __< ofrnxmr >__ kayabanerve:matrix.org:  tip, it does     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: that's now 90 MB per prior meeting,     

> __< kayabanerve:matrix.org >__ jeffro256:monero.social: ^     

> __< kayabanerve:matrix.org >__ ofrnxmr:monero.social: it needs to be at all times, not conditionally, hence the proposal on a 90 MB static limit until syncing and scanning are fixed     

> __< rucknium >__ By the way, the new network scan data is in. 1,850 "new" spy nodes on the SCNL-0001-1 ASN: https://moneronet.info/     

> __< kayabanerve:matrix.org >__ I'll withdraw my proposal if someone fixes both before the next HF. Else, 90 MB static limit with the HF is my advocacy.     

> __< boog900 >__ so close to half our network!     

> __< boog900 >__ its weird all those good nodes in their spy block      

> __< ofrnxmr >__ kayabanerve:matrix.org: A hard limit will require a hf to remove. A soft limit allows miners to produce whatever they want, and just a point release to change     

> __< jeffro256 >__ NACK to 90MB non-dynamic limit ;)     

> __< jeffro256 >__ boog900: Double crossers?     

> __< kayabanerve:matrix.org >__ I think jeffro256:monero.social: is compromised by chain analysis and wants to destabilize the network, proposal to remove from all Monero activity /s /s /s     

> __< kayabanerve:matrix.org >__ :p     

> __< boog900 >__ very funny SCNL-0001-1 was registered weeks after I found the spies last year     

> __< kayabanerve:matrix.org >__ If this isn't fixed by the HF, I don't see why we wouldn't plug the hole in this way with the next HF. I don't believe the protocol has ossified and I don't like this guillotine over our heads, with a fraying rope, even if the rope still has a year now (and will have six years under upcoming proposals)     

> __< boog900 >__ have to register a new one now!     

> __< ammortel >__ It would be more elegant not to limit anything but to improve what causes the limitation's need. If that is possible      

> __< rucknium >__ I don't know how the 90MB limit is different from the limit that mainnet nodes running 2023 software would have if there were 20 consecutive blocks of 1.5MB or larger. Fixing that limit wasn't the same as a hard fork, either: https://github.com/spackle-xmr/monero/pull/12     

> __< kayabanerve:matrix.org >__ We should have any solution ASAP IMO, and this one which _should_ never trigger and will be ready, when the necessary reworks won't be, is best IMO     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: The issue literally is some blocks can be sent that can't be naturally synced or indexed or scanned by wallets     

> __< rucknium >__ This is literally true for the current mainnet circumstances I described.     

> __< boog900 >__ tbf it is the same, its just the fix is harder      

> __< kayabanerve:matrix.org >__ Instead of having these weird edge cases needing ad-hoc patches which are fine because they simply haven't been triggered yet, my proposal is to solidify safe, deterministic rules to ensure the network functions     

> __< jberman >__ the node breaks first fwiw, wallets download pruned tx data     

> __< kayabanerve:matrix.org >__ This also is reachable by an adversary today     

> __< rucknium >__ Those of us in the stressnet trenches last year know :)     

> __< kayabanerve:matrix.org >__ jberman:monero.social: Yes and no. Yes, the pruned TXs will take longer to break, but the RPC still has some methods break at that point.     

> __< kayabanerve:matrix.org >__ Which will screw with indexers and maybe _some_ wallets.     

> __< ofrnxmr >__ rucknium: Fwiw, fcmp seems to handle 50mb batches ok     

> __< jberman >__ kayabanerve:matrix.org: ok fair enough, the RPC wallet2 uses to sync should be ok fwiw*     

> __< datahoarder >__ ofrnxmr: I added proper calculation of byte size vs weight to stressnet block explorer, to see how that differs     

> __< rucknium >__ datahoarder:monero.social: I'm getting Bad Gateway now. But thanks for that     

> __< kayabanerve:matrix.org >__ Either we hit this and the network breaks in weird and sporadic ways, or we hit this and have artificially lower capacity than the network would have _if it functioned properly at such scale_.     

> __< ofrnxmr >__ datahoarder: I think sync_info shows byte size     

> __< datahoarder >__ rucknium: Just fixed it, node crashed, OOM     

> __< datahoarder >__ https://stressnet.p2pool.observer/block/f661443cc27163de55b32c939418fbddb0f93e4f7d6575221387051456356021     

> __< kayabanerve:matrix.org >__ We can remove the limit with the functioning. tevador's table explained the theory of outcomes on this.     

> __< jberman >__ is that an OOM running the latest v1.5 pre-release as well?     

> __< datahoarder >__ ofrnxmr: you can check this on any historical block (or tx)     

> __< kayabanerve:matrix.org >__ So jeffro256:monero.social: , want to elaborate why you don't support a limit just under the existing hard limits?     

> __< datahoarder >__ jberman: yep, with the patches. but I was using computer for other things now     

> __< kayabanerve:matrix.org >__ I can't force you to agree but yes, I'd like to maintain consensus on this     

> __< kayabanerve:matrix.org >__ We did have loose consensus last meeting     

> __< datahoarder >__ We can talk about oom later keep going. Just wanted to bring up the size vs weight     

> __< tevador >__ Fixing the 100MB limit is technically a hard fork in any case.     

> __< kayabanerve:matrix.org >__ Eh. Nodes who were online at the threshold may continue indefinitely due to split syncing if blocks and TXs.     

> __< kayabanerve:matrix.org >__ It's this horrific Schrödinger's cat of liveness, functioning, and hard forks     

> __< jeffro256 >__ I would be fine with a 32MB limit on the serialized cryptonote::block itself, not the block weight. The current serialized size of cryptonote::block isn't currently limited. After the FCMP++ HF, it will be limited to one million transactions, plus a miner transaction with 10K outputs, but I think that we could do better th [... too long, see https://mrelay.p2pool.observer/e/m8O4mtEKX1ZRMy1x ]     

> __< kayabanerve:matrix.org >__ It works enough it isn't dead, but it is broken and it's no longer verifiable as it can't be synced     

> __< tevador >__ Nodes who don't upgrade may fork off, that' the definition of a hard fork.     

> __< kayabanerve:matrix.org >__ Isn't that advocating 100 GB as the hard limit jeffro256:monero.social: ?     

> __< jberman >__ I agree with tevador. It would be a point release in name only. if older nodes cannot sync, it's a fork from those nodes     

> __< kayabanerve:matrix.org >__ 1000x when the network breaks?     

> __< rucknium >__ tevador: Was this fix a hard fork? https://github.com/spackle-xmr/monero/pull/12     

> __< kayabanerve:matrix.org >__ tevador Fair     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: Probably, see how Bitcoin increased the amount of database references allowed when verifying a block and how that was a HF.     

> __< jeffro256 >__ Yes, I believe so. The limit would be a small, but useful protection against DoS attacks for block deserialization which we don't currently have.  > <kayabanerve:matrix.org> Isn't that advocating 100 GB as the hard limit jeffro256:monero.social: ?     

> __< tevador >__ Yes, increasing the limits seems like a HF to me if non upgraded nodes won't sync the larger blocks.     

> __< kayabanerve:matrix.org >__ I'm not trying to say things are bad and should be bad. I'm saying things are bad and we should acknowledge that instead of having a loaded gun sitting around     

> __< rucknium >__ Then add one to the Monero hard fork count, I suppose.     

> __< kayabanerve:matrix.org >__ We should get rid of the gun entirely with a proper sync protocol but should at least remove the round     

> __< datahoarder >__ rucknium: https://www.reddit.com/r/Monero/comments/1mvmg44/a_list_of_all_of_moneros_consensus_changes/     

> __< kayabanerve:matrix.org >__ Didn't jeffro256 HF the merkle tree three months ago?     

> __< tevador >__ Under my sanity cap, 100 GB blocks are not possible until about 2052.     

> __< kayabanerve:matrix.org >__ Or was that not merged yet?     

> __< jberman >__ Going off reddit, it seems that many in the community would prefer the guillotine over Monero that it should break if the sync protocol isn't updated, although it's been portrayed to the community as just a "fix" by articmine:monero.social     

> __< kayabanerve:matrix.org >__ There's this weird off by one for 250 GB blocks jeffro256 submitted a patch for a few months ago, which would've be/would technically cause a net split     

> __< kayabanerve:matrix.org >__ The amount of broken things sitting around is prone to a bunch of net splits and any fixes, even reasonable, can be argued hard forks.     

> __< kayabanerve:matrix.org >__ That's why I'm proposing canonicalizing current limits. To remove this bullshit.     

> __< tevador >__ I think it's reasonable to add the 90MB hard cap for now in a way that we can't forget to remove it when a future HF fixes the underlying problem.     

> __< kayabanerve:matrix.org >__ Yes, the limit is bad, but right now it's hodge podged and broken. At least I'll just be bad but functional with an explicit setting.     

> __< datahoarder >__ tevador: I suggested it explicitly only being enabled for a specific hardfork, not further ones     

> __< kayabanerve:matrix.org >__ I suggested it be enabled until removed in favor of fixed p2p, RPC, wallet sync protocols.     

> __< kayabanerve:matrix.org >__ They both declare an intended term. One forces the issue and one acknowledges the issue.     

> __< tevador >__ datahoarder: What if we need an emergency HF in the future before the issue is fixed?     

> __< rucknium >__ We are about to hit three hours of meeting. Stressnet is next.     

> __< articmine >__ Then we are back to the Bitcoin scenario. Put in a sunset block for the cap     

> __< datahoarder >__ tevador: then you explicitly need to update that parameter. which documents this being pushed     

> __< rucknium >__ Please start to wrap up the discussion for now.     

> __< datahoarder >__ it's more of fuzzy feelings, as next hardfork could just push it     

> __< kayabanerve:matrix.org >__ Yes, I'd like to not overload future HFs when this is obviously a priority     

> __< tevador >__ articmine: The sunset block is meaningless if nodes start crashing at the limit.     

> __< kayabanerve:matrix.org >__ Stressing about it doesn't actually solve it     

> __< kayabanerve:matrix.org >__ If you want to stress, you can solve it     

> __< articmine >__ My point is how long is it going to take to fix this      

> __< tevador >__ https://github.com/monero-project/research-lab/issues/154#issuecomment-3620881639     

> __< articmine >__ How many years?     

> __< kayabanerve:matrix.org >__ As is 90 MB + 10 MB a year or so. Unless the issue is fixed, allowing it to be removed, it isn't meaningful     

> __< kayabanerve:matrix.org >__ articmine:monero.social: PRs welcome     

> __< rucknium >__ Does someone want to take the initiative to recruit more senior-level developers or is the project going to continue to overwork its mainstays?     

> __< kayabanerve:matrix.org >__ It's obviously important. I'd estimate within two years, as someone who observes p2p/wallet development but doesn't participate. If you want to ensure it's done, you have to ensure that yourself. No discussion nor stress will magically translate to actual work about it.     

> __< tevador >__ If anyone has a problem with the 90MB limit, please post your arguments in #154.     

> __< kayabanerve:matrix.org >__ (Not to say we can't discuss coordination of work, ofc, cc rucknium:monero.social: who brought up bringing in more devs)     

> __< boog900 >__ tx relay v2 is a similar change to the p2p network, and that has taken a while.      

> __< rucknium >__ tevador: Good. Discussion can continue on GitHub of course.     

> __< rucknium >__ 8.  FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< rucknium >__ This week we increased the spam volume. 40GB was added in the last week and the unpruned node database is now over 100GB.     

> __< rucknium >__ https://mrelay.p2pool.observer/m/monero.social/NKqjHnLSyYCuhpLrPGsMnrUN.png (stressnet_block_weight_2025_12_10.png)     

> __< datahoarder >__ As mentioned. Deployed stressnet block explorer https://stressnet.p2pool.observer/ on clearnet. can view blocks or transactions. in a future stressnet, we could share viewkeys to identify miners/transactions. Hope it's useful, monerod willing.     

> __< rucknium >__ ^ That's the last week of stressnet block weights from https://stressnetnode1.moneronet.info/     

> __< rucknium >__ I think the short-term scaling limit has been reached, at about 18MB blocks when fees are not maxed. Up to 30MB blocks when fees are near maximum.     

> __< jeffro256 >__ boog900: To be fair, the tx relay v2 issue is much more complicated since different relay strategies affect network-level privacy and bandwidth requirements. Whereas fixing the 100MB block sync issue effectively boils down to splitting up the same message in the same order over multiple packets.      

> __< rucknium >__ IMHO, there is node instability at the 18MB block limit. A lot of orphaned blocks and foolish behavior by monerod.     

> __< ofrnxmr >__ rucknium: I think thats due to txpool     

> __< jberman >__ On network health: FCMP++-related OOM's have seemed relatively in check with the pre-release v1.5 (although Datahoarder's latest OOM is worth a look). Right now I'm focused on an interesting FCMP++ verification regression with that build, and I do want to investigate that fully before v1.5     

> __< ofrnxmr >__ I notice a lot of inconsistent txpools,which leads to new blocks being broadcast with alot of unknown txa     

> __< datahoarder >__ jberman: of note, I make heavy use of RPC for the explorer     

> __< ofrnxmr >__ example: rucknium:monero.social  your explorer showed 600mb, but my nodes showed like 50mb, 200mb, and 400mb     

> __< jberman >__ sounds like the nodes with <600mb are having issues     

> __< boog900 >__ jeffro256: Ehh tbf I thought tx relay v2 would be a pretty easy change before we started actually working on it. I think preventing any DoS while changing the whole sync and relay protocol is going to be complicated or at least take a while to review.      

> __< rucknium >__ Keeping spam tx volume consistently high is hard wen nodes are acting foolishly. So I won't keep trying there. I think good info was obtained in the last week.     

> __< jberman >__ (I agree with boog fwiw, my hunch is a new sync protocol is going to end up a more involved change)     

> __< jeffro256 >__ boog900: Hence why I'm so ready to getting header-only sync in Monero, especially DoS-resistent header-only sync with PoW commitments     

> __< jberman >__ (I guess boog didn't say that, but tha'ts myu hunch)     

> __< ofrnxmr >__ jberman: Similar problems for lower pool sizes, like spam node will have 10k txs, but explorer has only seen 5k of them     

> __< datahoarder >__ jeffro256: pow commitments on beta stressnet would be so nice to have :)     

> __< ofrnxmr >__ Also a major issue is that eventually you get a lot of "not relayed" and "failing" txs. No idea why     

> __< jeffro256 >__ datahoarder: datahoarder:monero.social: you may be interested in https://github.com/monero-project/monero/pull/10038     

> __< datahoarder >__ I already have the code in, even on my go-RandomX (which also supports V2!)     

> __< ofrnxmr >__ The tldr is that the txpool itself has issues. Fixing that should fix a lot of the alt chains, reorgs, and nodes falling behind as a result     

> __< datahoarder >__ I was looking at that but the TODO was a bit empty     

> __< rucknium >__ And nodes shouldn't check if they need to increase the LMDB size every time they receive a tx in the txpool, if that is actually what's happening.     

> __< jberman >__ ofrnxmr:monero.social: and these issues are definitively not issues helped/sovled by 252 and 254, ya?     

> __< datahoarder >__ ofrnxmr: I noticed orphan blocks dumping txs on txpool, but txpool doesn't grow, so node keeps orphan block ... but without txs to switch or broadcast it if it becomes the legit one     

> __< jeffro256 >__ #252 is huge      

> __< ofrnxmr >__ jberman: Right     

> __< datahoarder >__ which might explain the issues with orphans once txpool grows - one orphan causes a temporary split due to inability to switch back even if other grows a bit more     

> __< datahoarder >__ but one would assume then the transactions make their way over time later     

> __< jberman >__ ok, it's sounding like you guys are running into new issues where you're seeing in the logs what's happening / noticing interesting patterns. if you could write up issues for these circumstances (or add to existing ones) and include those logs, it would be helpful so we can keep track of them     

> __< rucknium >__ Anything more on stressnet?     

> __< ofrnxmr >__ jberman: rucknium asked about double spends, and noted that he had a lot of failing txs     

> __< ofrnxmr >__ I hadnt noticed failing before, but already had an issue open about not relayed     

> __< ofrnxmr >__ The other day, i noticed 1000+ failing, and ~800 not relayed     

> __< rucknium >__ Nodes thought some of my wallets were trying to double spend. rescan_spent solved it.     

> __< ofrnxmr >__ ofrnxmr: checked because (wallets were giving double spend errors)     

> __< rucknium >__ It wasn't a few outputs. AFAIK, it was almost all of the outputs that those wallets were trying to spend     

> __< ofrnxmr >__ The node didnt go over capacity on the pool - its set to 50gb max     

> __< rucknium >__ I don't know if I have the time allocation to troubleshoot every issue I hit.     

> __< rucknium >__ I mean, submit a useful bug report and help investigate     

> __< rucknium >__ I just do some percussive maintenance and move on.     

> __< jberman >__ ack on this issue, I essentially have a status report on it here: https://github.com/seraphis-migration/monero/issues/185#issuecomment-3609916734 > <rucknium> Nodes thought some of my wallets were trying to double spend. rescan_spent solved it.     

> __< rucknium >__ Keeping the spamming going, alone, takes time. I think I had about 80 wallets spamming this week.     

> __< jberman >__ ack, would probably be good to add to that issue about not relayed this new failing state > <ofrnxmr> I hadnt noticed failing before, but already had an issue open about not relayed     

> __< jberman >__ rucknium: you generally don't have to help investigate. just a quick summary of the issue and log level 2 is enough     

> __< rucknium >__ And I don't know if the issues I hit are meaningful or if it's just because I'm sending txs at a rate that no user would reasonably send them.     

> __< ofrnxmr >__ rucknium: The "not relayed" txs should probably be an easy fix     

> __< rucknium >__ jberman:monero.social: I can push logs to a viewable directory in the MRL research computing cluster. Extracting them and bringing to GitHub is annoying.     

> __< ofrnxmr >__ If you relay_tx txid, they relay. So its just monerod failing to do its job     

> __< jberman >__ rucknium: that's fine     

> __< ofrnxmr >__ ofrnxmr: The failing state though, i dont know what would cause that     

> __< jberman >__ tbh I think we'll probably want tx relay v2 in place before really digging on that one (and revert pool complement checking that I added to stressnet to reduce bandwidth)      

> __< jberman >__ (it could be the latter causing issues, I'm not sure)     

> __< jberman >__ A general update on stressnet: will just keep hammering issues as they come in, and work toward getting tx relay v2 in. Unfortunately the influx of issues (both from the integration itself and from existing quirks) is large, so it's taking time to work through it     

> __< rucknium >__ jberman:monero.social: Thank you!     

> __< rucknium >__ 9.  Post-FCMP scaling concepts.     

> __< rucknium >__ Is preland:monero.social  here?     

> __< rucknium >__ Maybe I should put this item earlier in the agenda.     

> __< rucknium >__ next time     

> __< rucknium >__ We can end the meeting here. Thank you.     



# Action History
- Created by: Rucknium | 2025-12-09T22:47:32+00:00
- Closed at: 2025-12-23T21:12:27+00:00
