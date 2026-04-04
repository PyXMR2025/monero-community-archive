---
title: Monero Research Lab Meeting - Wed 25 June 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1226
author: Rucknium
assignees: []
labels: []
created_at: '2025-06-24T22:08:57+00:00'
updated_at: '2025-07-06T14:45:52+00:00'
type: issue
status: closed
closed_at: '2025-07-06T14:45:52+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3.  [SLVer Bullet: Straight Line Verification for Bulletproofs](https://github.com/cypherstack/silver-bullet).  [Cypher Stack review of divisors for FCMP](https://github.com/cypherstack/divisor_deep_dive).

4. [MoneroKon 2025 recap](https://www.monerokon.org/).

5. [Spy nodes](https://github.com/monero-project/research-lab/issues/126).

6.  CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).

7. Peer Scoring Metrics.

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1223 

# Discussion History
## Rucknium | 2025-06-27T21:52:06+00:00
Logs

> __< 0​xfffc:monero.social >__ My sincere apologies. I have been relocating to a new city. It took few days and I will not be 100 percent available for few more days.     

> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1226     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< b​oog900:monero.social >__ hi     

> __< a​ntilt:we2.ee >__ seas     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Working on data collection on reachable nodes and a web app to display the data: https://github.com/Rucknium/xmrnetscan . "Participated" in MoneroKon.     

> __< j​berman:monero.social >__ me: fixed ofrnxmr 's reported bug on the fcmp++-stage branch (credit to ofrn for solid testing and maintaining a reproducible setup, making it easy to track down and fix), worked on reducing data stored per output in the fcmp++ curve tree, PR review / PR touchups     

> __< r​ucknium:monero.social >__ 3) SLVer Bullet: Straight Line Verification for Bulletproofs. Cypher Stack review of divisors for FCMP. https://github.com/cypherstack/silver-bullet  https://github.com/cypherstack/divisor_deep_dive     

> __< r​ucknium:monero.social >__ Last I remember hearing, kayabanerve  was going to look closely at SLVR Bullet for its suitability for FCMP and see if improvements could be made.     

> __< a​rticmine:monero.social >__ Sorry I am late     

> __< j​berman:monero.social >__ (I'm not aware of an update on SLVer)     

> __< j​berman:monero.social >__ AFAIK this is the latest still     

> __< j​berman:monero.social >__ Actually to be more precise, that this is the latest (that kayaba is going to implement the changes)     

> __< j​berman:monero.social >__ Link for IRC folk: https://libera.monerologs.net/monero-research-lab/20250619#c535414-c535418     

> __< a​rticmine:monero.social >__ Voice message.ogg     

> __< r​ucknium:monero.social >__ Any updates that Cypher Stack wants to share on this? If not, we can move to the next item.     

> __< r​ucknium:monero.social >__ 4) MoneroKon 2025 recap. https://www.monerokon.org/  https://cfp.twed.org/mk5/schedule/     

> __< r​ucknium:monero.social >__ Interesting talks that will be posted in about two weeks:     

> __< r​ucknium:monero.social >__ Talk by ArticMine on FCMP++ fees     

> __< r​ucknium:monero.social >__ Talk by jeffro256 on changes to the block format with FCMP that could help enable Simple Payment Verification (SPV) wallet software     

> __< r​ucknium:monero.social >__ Talk by afungible about his mainnet experiment in August 2022 of a minor stress test of the network.     

> __< r​ucknium:monero.social >__ Talk by Yu Gao about the topology of the Monero network (i.e. inferring the connections between nodes)     

> __< r​ucknium:monero.social >__ Talk by hbs that shared new software to improve Monero<>Ethereum atomic swaps     

> __< r​ucknium:monero.social >__ Talk by CJ and Sean Coughlin on an in-progress implementation of payment channels on Monero (Grease)     

> __< r​ucknium:monero.social >__ Talk by Alan Szepieniec on post-quantum anonymous transactions without signatures     

> __< r​ucknium:monero.social >__ Talk by Aaron Feickert (sarang) about temporary mnemonic  seeds for risky situations like border crossings     

> __< r​ucknium:monero.social >__ The MoneroKon organizers will scrub the live records of any privacy problems, then post     

> __< r​ucknium:monero.social >__ But there were four pre-recorded talks that were posted immediately.     

> __< rbrunner >__ Can't somebody fast-track that Grease talk? :)     

> __< r​ucknium:monero.social >__ Luke Szramowski - Full-Chain Membership Proofs (FCMP++) Divisors: The Inside Scoop  https://youtube.com/watch?v=6kQYqaKgupQ     

> __< r​ucknium:monero.social >__ Justin Ehrenhofer - Overview of the Last Year of Audits, Reviews, and Proofs https://youtube.com/watch?v=Fo1uxIETpOI     

> __< r​ucknium:monero.social >__ Rucknium & Boog900: Defeating Spy Nodes on the Monero Network: https://vimeo.com/1095371245 https://youtube.com/watch?v=k7LBKOn81rc     

> __< r​ucknium:monero.social >__ Rucknium: OSPEAD: Optimal Ring Signatures: https://vimeo.com/1094758696 https://youtube.com/watch?v=F7hNOQVp88A     

> __< r​ucknium:monero.social >__ sarang posted his slides here: https://github.com/AaronFeickert/monkon2025     

> __< r​ucknium:monero.social >__ Slides for my presentations + Boog900 are here: https://github.com/Rucknium/presentations     

> __< r​ucknium:monero.social >__ IIRC, the presenters of the Grease talk said that they were more interested in one-ro-one applications of Grease than creating a whole network like Lightning.     

> __< r​ucknium:monero.social >__ one-to-one*     

> __< r​ucknium:monero.social >__ Which is something that I liked hearing.     

> __< r​ucknium:monero.social >__ afungible's talk helped answer a question that I thought I already had the answer to: why did tx volume spike right before the August 2022 hard fork?     

> __< r​ucknium:monero.social >__ I thought it was MineXMR, a mining pool, shutting down and sending the last of its payments. That was a logical explanation, to me. But, something less logical happened.     

> __< a​rticmine:monero.social >__ The failings of LN can for the most part be traced back to a broken layer 1.      

> __< a​rticmine:monero.social >__ Grease on Monero would not have this issue.     

> __< r​ucknium:monero.social >__ For example, I think that Grease could be used with something like XMRChat. A user may not want to wait 20 minutes, on average, between comments to livestreamers!     

> __< r​ucknium:monero.social >__ More comments about things that happened at MoneroKon?     

> __< j​berman:monero.social >__ Sounds like it was a great conference. Looking forward to watching these     

> __< r​ucknium:monero.social >__ 5) Spy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< r​ucknium:monero.social >__ Last week, jhendrix  released research about the network-level privacy issues on the Zano network, which is a CryptoNote-based protocol like Monero. Onion hidden service link accessible with Tor Browser: http://g7cpug4k6ydyq5dlxrji35xnfq5n5rba3n7holux4tmdsm42ju543tad.onion/     

> __< r​ucknium:monero.social >__ It seems that the combination of not having Dandelion++ and having around 40 reachable nodes can reduce privacy a lot.     

> __< r​ucknium:monero.social >__ IMHO, one clever thing about this research is that it could infer the amount of staked coins in Zano's hybrid proof-of-stake/proof-of-work protocol because you can figure out how many blocks each IP address mines.     

> __< rbrunner >__ Yes, that's cool, and unexpected     

> __< r​ucknium:monero.social >__ Despite the fact that Zano has the Zarcanum protocol to "hide" the amount that you are staking on the blockchain, which koe helped with IIRC     

> __< r​ucknium:monero.social >__ jhendrix had previously examined the Monero network, released findings, and discussed them here a few months ago: http://maldomapyy5d5wn7l36mkragw3nk2fgab6tycbjlpsruch7kdninhhid.onion/     

> __< r​ucknium:monero.social >__ Monero has spy nodes on its network, but it has Dandelion++, thousands of nodes, and does not use proof-of-stake     

> __< r​ucknium:monero.social >__ I would not be surprised if jhendrix  releases finds about a third coin's network soon.     

> __< a​ntilt:we2.ee >__ ... and also a vulnerability - core stakers are ~8 nodes with known IP addresses     

> __< r​ucknium:monero.social >__ The Zano team released a response to the research: https://blog.zano.org/team-response-to-zano-network-analysis-report/     

> __< a​ntilt:we2.ee >__ on the other hand staking 51% secures the net     

> __< a​ntilt:we2.ee >__ ... call it centralized.     

> __< r​ucknium:monero.social >__ They said that they had tried broadcasting all txs over Tor earlier, but that method was unreliable. I didn't know that, but it's consistent with the position that boog900  and I had about Tor/I2P-only in our MoneroKon talk about spy nodes: Tor/I2P is too unreliable to use as default for all users.     

> __< a​ntilt:we2.ee >__ remote nodes need to be reachable as tor hidden service. Such a mix is fine.     

> __< rbrunner >__ That response sounds a bit like an attempt of damage control to me.     

> __< r​ucknium:monero.social >__ I don't agree with their claim that Dandelion++ doesn't help much. It's not perfect, but even Chainalysis in their leaked video said that Monero network surveillance became much more difficult after D++ was deployed.     

> __< rbrunner >__ Even if it's not great. "It's not perfect therefore not worth doing" is a well-known intelectual fallacy     

> __< r​ucknium:monero.social >__ And they suggest that users concerned about privacy can choose to connect only to "trusted" nodes. IMHO, a trusted node soon becomes a targeted node. And taking that stance isn't very decentralized.     

> __< a​rticmine:monero.social >__ The Chainalysis blockchain surveillance video actually indirectly made a case for the use of VPNs to defeat spy nodes in Monero     

> __< a​rticmine:monero.social >__ If they detected a VPN they gave up surveillance of the wallet     

> __< r​ucknium:monero.social >__ Like I said in my update, I am working on a data pipeline and webapp data visualizer to collect daily data about reachable Monero nodes. This could potentially detect if new spy nodes with patched code appear suddenly. I will also collect informative data such as the share of pruned node, which nodes have RPC available, which nodes appear to be using ban lists, etc.: https://githu<clipped message     

> __< r​ucknium:monero.social >__ b.com/Rucknium/xmrnetscan     

> __< r​ucknium:monero.social >__ I may have something to show by next meeting.     

> __< r​ucknium:monero.social >__ This uses the network scanner written by boog900 , using cuprate technology, as its core.     

> __< b​oog900:monero.social >__ their video was just a show. In reality you can still link txs together if they come from the same IP, even if you can't find the real source.     

> __< b​oog900:monero.social >__ specifically the part about tracking the person was just a show.     

> __< r​ucknium:monero.social >__ rbrunner's subnet deduplication PR to reduce spy node threat is available for review: https://github.com/monero-project/monero/pull/9939     

> __< r​ucknium:monero.social >__ 6) CCS proposal: Monero Network Simulation Tool. https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589     

> __< a​ntilt:we2.ee >__ #9939 is paramount and not too risky to release IMHO.     

> __< r​ucknium:monero.social >__ I tried to contact the developer of EthShadow to get their opinion on implementing Shadow for Monero: https://github.com/ethereum/ethshadow/issues/25     

> __< r​ucknium:monero.social >__ No response yet. Making a GitHub issue maybe it's the best way to contact someone, but their personal website is a dead link and I cannot find any other contact info.     

> __< a​ntilt:we2.ee >__ would't this be a job for ginger ?     

> __< a​rticmine:monero.social >__ Of course one can link TXs to the same IP, but the whole point of blockchain surveillance is to accuse a person of a crime and then sell the accusation to law enforcement for profit.     

> __< r​ucknium:monero.social >__ Well, I said I would do it last meeting, so I did do it.     

> __< r​ucknium:monero.social >__ 7) Peer Scoring Metrics.     

> __< b​oog900:monero.social >__ knowing txs are linked can be very useful if you know something about one of those txs, i.e sent to an exchange or whatever.     

> __< b​oog900:monero.social >__ or even just analyzing ring members, knowing some ring members came from the same source.     

> __< a​rticmine:monero.social >__ In my view the real value of Monero's privacy technologies including Dandelion and FCMP++ lies in removing even the illusion of surveillance. This is critical to protect the innocent from false accusations. This being  said we must keep in mind that from a technical perspective blockchain surveillance remains highly unreliable even on so-called surveillance coins.     

> __< r​ucknium:monero.social >__ Any discussion on peer scoring metrics?     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< a​rticmine:monero.social >__ Thanks     

> __< a​ntilt:we2.ee >__ de-doubling (#9939) is a pre-requisite to taking further action imho. (strengthening anchor nodes, for example)     

> __< a​ntilt:we2.ee >__ de-doubling may be a scoring spectrum - rather than on/off   

# Action History
- Created by: Rucknium | 2025-06-24T22:08:57+00:00
- Closed at: 2025-07-06T14:45:52+00:00
