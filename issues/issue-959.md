---
title: Monero Research Lab Meeting - Wed 24 January 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/959
author: Rucknium
assignees: []
labels: []
created_at: '2024-01-24T16:59:30+00:00'
updated_at: '2024-01-31T17:03:01+00:00'
type: issue
status: closed
closed_at: '2024-01-31T17:03:01+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: How to confirm security of Monero's multisignature protocol? Do we need mathematical security proofs, and can we get them? Info:
- [Brandon Goodell and Sarang Noether (2018) "Thring Signatures and their Applications to Spender-Ambiguous Digital Currencies"](https://www.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf)
- [Monero multi-signature patch review by Inference](https://community.rino.io/rino-multisig-pr8194-audit-20220627.pdf)
- [Rust alternative implementation](https://github.com/serai-dex/serai/blob/develop/coins/monero/src/wallet/send/multisig.rs) by @kayabaNerve

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#957 

# Discussion History
## plowsof | 2024-01-25T11:45:45+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting in this room in one hour.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/959     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< vtnerd >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: OSPEAD. I originally set an internal deadline of January 31, but it is best to inform everyone in the project of internal deadlines 😅. isthmus is working on getting me some additional data. Also, I killed one of the Monero Research Computing Server's computers. Or, you cannot prove anything, but I was at the scene of the crime.     

> __< r​ucknium:monero.social >__ ("Why am I getting all these segfaults?") gingeropolous got it back running quickly.     

> __< vtnerd >__ me : still working on pow difficulty tracking in LWS - still not certain whether its worth hacking LWS to get crude pow verification     

> __< rbrunner >__ If your part of OSPEAD work is finished, does this need a next step of "coding" it? And if yes, is that much work still?     

> __< rbrunner >__ (Maybe I asked that before, but must be quite some time ago ...)     

> __< r​ucknium:monero.social >__ You mean the edits to wallet2? AFAIK, only a few lines need to be changed. Maybe someone will need to implement an unusual parametric distribution if an unusual one is the one that fits best.     

> __< rbrunner >__ Ok. Sounds good.     

> __< r​ucknium:monero.social >__ Taking pains, I have mirrored what wallet2 does. That means that the probability distribution is not modeled as time-since-block, but as output index.     

> __< r​ucknium:monero.social >__ I have mirrored wallet's calculation of the flow of outputs per second. (seconds per output, actually.)     

> __< r​ucknium:monero.social >__ And the unspendable outputs because of lock time (most relevant for coinbase outputs with 60 block lock instead of 10 block lock     

> __< r​ucknium:monero.social >__ So this is supposed to be a drop-in replacement for what wallet2 does now.     

> __< r​ucknium:monero.social >__ But that brings me to a question that I have wondered about: Will there be a hard fork this calendar year?     

> __< rbrunner >__ No idea. It must be a long time already ago that I read anybody writing something about a possible hardfork.     

> __< r​ucknium:monero.social >__ isthmus and I discussed implementation of the new decoy selection algorithm. We could try to compute the privacy impact of introducing a new DSA without a hard fork. But isthmus thinks the research time for that isn't work it. And it will be hard to forecast certain important variables.     

> __< rbrunner >__ But you completing your work might provide a push. And I think some nice RandomX changes are waiting.     

> __< r​ucknium:monero.social >__ So probably we would wait for the next hard fork so all wallet2-based wallets have the same DSA instead of a slow adoption.     

> __< r​ucknium:monero.social >__ Yes, I think the possible changes are to PoW and Bulletproofs++     

> __< rbrunner >__ Yeah, those as well.     

> __< r​ucknium:monero.social >__ AFAIK, the coding changes to PoW are complete.     

> __< rbrunner >__ Think so as well     

> __< r​ucknium:monero.social >__ The soundness of BP++ is still being researched by CypherStack.     

> __< rbrunner >__ We could also pair the hardfork with a push to a broader introduction of Polyseed, although of course technically not related. But if you update anyway ...     

> __< r​ucknium:monero.social >__ The University of Zurich research group has applied to MAGIC for funding their idea to replicate the BTC transaction graph with Monero's ring signatures to analyze EAE-like attacks. We talked about that a few months ago here IIRC. Any further thoughts?     

> __< rbrunner >__ Nope. Would they need a large sum?     

> __< r​ucknium:monero.social >__ They are requesting about 24,000 USD. It is one post-doc, one PhD student, and one professor supervising.     

> __< r​ucknium:monero.social >__ From the Blockchain & Distributed Ledger Technologies Group at UZH     

> __< rbrunner >__ Hard to say whether that would find funding, but maybe worth a try?     

> __< rbrunner >__ Although it does not look too good with exchanges and Monero nowadays, so that EAE problem may become smaller over time ...     

> __< r​ucknium:monero.social >__ Yes, that is an interesting development. The group plans to use data on who owns the BTC addresses like exchanges, etc., to get a realistic picture of how successful EAE-like attacks would be.     

> __< r​ucknium:monero.social >__ vtnerd: Question about Dandelion++. If a node operator has no incoming connections, do all txs submitted to that node from wallets immediately enter the fluff phase? I assume that they do because the node's outgoing connections would know that a stem-phase tx actually originates with that node because they have no incoming connections that could be stem phase.     

> __< r​ucknium:monero.social >__ But, for example, Serai or a DEX that functions in a similar way would sort of have a EAE problem since the incoming and outgoing txs would be known to the Serai validators IIRC.     

> __< vtnerd >__ thats a good question, and I don't remember off-hand, let me check     

> __< g​hostway:matrix.org >__ I'm reading and trying to process GBPs and reading kayabanerve's code     

> __< r​ucknium:monero.social >__ Thanks :)     

> __< g​hostway:matrix.org >__ If anyone cares :)     

> __< r​ucknium:monero.social >__ ghostway: Good. Anything you want to share about it?     

> __< vtnerd >__ it prints this error message : 'Unable to send transaction(s) via Dandelion++ stem' and then initiates a fluff     

> __< r​ucknium:monero.social >__ vtnerd: Thank you!     

> __< vtnerd >__ and its the opposite, its no outgoing connections     

> __< r​ucknium:monero.social >__ Oh. Then it still sends stem phase txs without any incoming connections?     

> __< r​ucknium:monero.social >__ AFAIK, this "attack" would require the adversary to be a little active since the adversary would have to check if the node was accepting incoming connections to conclude that any seen stem txs originated with the node.     

> __< r​ucknium:monero.social >__ I'm not certain if immediate-fluff or stem phase is better or worse for privacy in this case.     

> __< r​ucknium:monero.social >__ The outgoing connections are chosen by the node, so in theory they are supposed to be "friendlier" than an incoming connection that could be from anyone. AFAIK.     

> __< vtnerd >__ yes, stem phase uses outgoing connections     

> __< vtnerd >__ that comes straight from the paper     

> __< r​ucknium:monero.social >__ Right. I mean that if an operator of node `A` does not open ports and the node's outgoing connections know that the ports are not open by probing them, then the nodes on the outgoing connections know that node `A` will have no stem phase txs except for the ones that originate from itself.     

> __< r​ucknium:monero.social >__ By deduction.     

> __< r​ucknium:monero.social >__ So those nodes would know for sure that the stem phase txs belong to wallets that submitted txs to node `A`.     

> __< r​ucknium:monero.social >__ But maybe if the txs were in fluff mode they would not know for sure because a fluff phase may have been sent to node `A` by one of its other outgoing connections.     

> __< vtnerd >__ I'm not following. the node would still have stem-phase because it has outgoing links?     

> __< r​ucknium:monero.social >__ My question is if the txs that are submitted to node `A` by wallets are set to be stem phase when they are first relayed to the outgoing connections. In the case that node `A` has no incoming connections.     

> __< r​ucknium:monero.social >__ Normally, all txs submitted to a node will be relayed to another node in stem mode (except maybe if they are in that 20% in the epoch that has its mode switched to "always fluff").     

> __< vtnerd >__ yes, if there are no incoming connections, it should still use stem mode on the outgoing links     

> __< r​ucknium:monero.social >__ The only way that a node will relay a tx in stem mode is if (1) it received the tx in stem mode from another node that is an incoming connection _or_  (2) if the tx was submitted directly to that node by a wallet. Right?     

> __< r​ucknium:monero.social >__ So if a node has ports closed, then possibility (1) is eliminated and (2) remains. Nodes connected by outgoing connections could check if node `A` has its ports closed.     

> __< r​ucknium:monero.social >__ Anyway, a small network privacy issue for node operators who have their ports closed or who reject incoming connections.     

> __< r​ucknium:monero.social >__ Anything more to discuss?     

> __< vtnerd >__ ok, yes, that is a privacy leak that I dont recall being discussed     

> __< vtnerd >__ a tx could also come inbound via tor, but if they have tor inbound enabled they likely have tcp inbound enabled     

> __< r​ucknium:monero.social >__ Maybe that could be analyzed using some of the nice formulas from the D++ paper. Or from the other paper with python simulation     

> __< r​ucknium:monero.social >__ Sharma, P. K., Gosain, D., & Diaz, C. 2022. On the anonymity of peer-to-peer network anonymity schemes used by cryptocurrencies.     

> __< r​ucknium:monero.social >__ I downloaded the Python simulation months ago and it seemed to work.     

> __< r​ucknium:monero.social >__ We can end the meeting here.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2024-01-24T16:59:30+00:00
- Closed at: 2024-01-31T17:03:01+00:00
