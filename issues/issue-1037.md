---
title: Monero Research Lab Meeting - Wed 10 July 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1037
author: Rucknium
assignees: []
labels: []
created_at: '2024-07-09T21:56:41+00:00'
updated_at: '2024-07-22T20:05:15+00:00'
type: issue
status: closed
closed_at: '2024-07-22T20:05:15+00:00'
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

5. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

6. Uniformity of Monero's hash-to-point function.

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1034 

# Discussion History
## Rucknium | 2024-07-16T20:59:44+00:00
Log:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1037     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< jberman >__ *waves*     

> __< v​tnerd:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< 0​xfffc:monero.social >__ (1) Fixed a bug, (2) working on start up speed up: https://github.com/0xFFFC0000/monero/pull/26     

> __< r​ucknium:monero.social >__ me: Helping with stressnet. Reading papers about gossip networks and analyzing the Monero p2p transaction gossip messages.     

> __< j​effro256:monero.social >__ howdy     

> __< jberman >__ me: completed first pass at growing and trimming the tree (db and tests implemented, tests passing)     

> __< v​tnerd:monero.social >__ Not much to report, between work contracts atm     

> __< j​effro256:monero.social >__ me: Jamtis-RCT. Specifically, the conversion functions between X25519 and ed25519 points for legacy address support. If anyone knows a way to find the ed25519 (x, y) values from X25519's x value without doing explicitly finding the y value for X25519 by performing a square root op, please let me know     

> __< s​gp_:monero.social >__ Hello     

> __< r​ucknium:monero.social >__ 3) Stress testing monerod https://github.com/monero-project/monero/issues/9348     

> __< jberman >__ ("the tree" = fcmp curve trees merkle tree     

> __< r​ucknium:monero.social >__ I think we found another problem that could prevent block sync. Sometimes a valid block can be placed on the `m_invalid_blocks` list. It looks like a node can get on a short alt chain. Then it marks one of the main chain's blocks as invalid. Because the block is "invalid", it stops syncing to the main chain and bans nodes that send the "invalid" block.     

> __< r​ucknium:monero.social >__ I guess that nodes are applying the alt chain's rules for validity to the main chain, and think it's invalid. Probably it has something to do with the 100 block median block size, the penalty area, and how much miners can pay themselves. Maybe miners pay themselves too much on the main chain's block when the alt chain's rules are applied.     

> __< r​ucknium:monero.social >__ The nodes can start syncing again if they shut down and restart or if the node operator inputs `flush_cache bad-blocks` into the monerod console.     

> __< r​ucknium:monero.social >__ In the incident that I analyzed closely, the alt chain was 2 blocks long     

> __< r​ucknium:monero.social >__ I guess the problem is the block size computation because AFAIK this type of thing doesn't happen on the mainnet, but mainnet usually doesn't increase the 100-block median block size.     

> __< r​ucknium:monero.social >__ AFAIK, there is no plan yet to try to debug this     

> __< r​ucknium:monero.social >__ This week I started spamming 144in/2out txs to see if the out-of-memory issue that some people saw on mainnet would happen. I've seen a modest increase in RAM usage, but nothing that would cause a major problem. Most nodes on stressnet have 30 connections or fewer, so the OOM issue may be due to number of connections more than how many inputs txs have     

> __< r​ucknium:monero.social >__ But the CPU usage of nodes has increased because verifying inputs requires more CPU per byte of data than verifying outputs.     

> __< r​ucknium:monero.social >__ A low-end node (4GB RAM, 2 CPU threads) took 30 seconds per block recently to catch back up with chain tip with 4MB blocks mostly filled with 144in/2out txs.     

> __< r​ucknium:monero.social >__ Any more comments on stressnet?     

> __< jberman >__ sounds like a nice list of daemon issues has formed for would-be takers to pursue further     

> __< r​ucknium:monero.social >__ Here's the relevant part of the log file when the nodes fail to sync, by the way:     

> __< r​ucknium:monero.social >__ D [<IP>:<PORT> INC] first block hash <f6a9bcee7e02c2aa0da480de70f0d1369bda37d6aaab48a5cb55880a9101f192>, last <b7dfc5fbe7570a7cb61e0f9db175a235ee2b83e286c983f3d973435c1dcd27c7>     

> __< r​ucknium:monero.social >__ D block <f6a9bcee7e02c2aa0da480de70f0d1369bda37d6aaab48a5cb55880a9101f192> found in main chain     

> __< r​ucknium:monero.social >__ D block <33a5c86ea4a291ddf810df8620784ec8c9fea4014280a0d14f4bb6f6e0c17348> found in alternative chains     

> __< r​ucknium:monero.social >__ D block <4a76385a6ddb03134ce72d88c8e08c26737f43a5fb88ca2f278ef067e39fbaf2> found in m_invalid_blocks     

> __< r​ucknium:monero.social >__ E [<IP>:<PORT> INC] Block is invalid or known without known type, dropping connection     

> __< r​ucknium:monero.social >__ 4) Potential measures against a black marble attack. https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ I don't have much to report on this issue today except I found a paper that proposes an alternative to Dandelion++:     

> __< r​ucknium:monero.social >__ Franzoni, F., & Daza, V. (2022). Clover: An anonymous transaction relay protocol for the bitcoin p2p network.  https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=222     

> __< r​ucknium:monero.social >__ I just skimmed the paper. It claims that Clover is as good as D++, simpler, and works well for nodes that have no incoming connections (i.e. its ports are closed).     

> __< j​effro256:monero.social >__ Hmmmm that's a really interesting issue. I wonder what the value of even having a running "invalid blocks" list is, realistically. Obviously it would speed up failing known repeated bad blocks for honest peers, but the PoW check should be the very very first check performed on block data. This will mathematically limit the number of non-trivial bad blocks that can exist. An unhone<clipped messag     

> __< j​effro256:monero.social >__ st peer, however, can send any number of garbage blocks that don't pass PoW verification.     

> __< r​ucknium:monero.social >__ The last part is interesting. A few months ago we discussed a potential issue with D++ when nodes have no incoming connections. D++ treats incoming and outgoing connections differently for its graph theory to work.     

> __< r​ucknium:monero.social >__ jeffro256: In the log files I found an error message about the "invalid" block pointing to this line of code: https://github.com/monero-project/monero/blob/master/src/cryptonote_core/blockchain.cpp#L1217     

> __< r​ucknium:monero.social >__ Right above that is a comment: "FIXME: Why do we keep invalid blocks around?  Possibly in case we hear about them again so we can immediately dismiss them, but needs some looking into."     

> __< rbrunner >__ Waiting for a fix for 4 years :)     

> __< r​ucknium:monero.social >__ I've only skimmed the Clover paper. The D++ paper looks at a lot of different threat models. It is a dense paper. On a skim, the Clover paper looks like it analyzes fewer threat models. Anyway, I will keep the paper and come back to it later.     

> __< rbrunner >__ Ah, now, that remark is 9 years old.     

> __< r​ucknium:monero.social >__ My naive view is to try to fix the miscalculation of the block validity first.     

> __< r​ucknium:monero.social >__ 5) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< r​ucknium:monero.social >__ kayabanerve, kayabanerve     

> __< r​ucknium:monero.social >__ By the way, I've listed "Uniformity of Monero's hash-to-point function" as a separate agenda item. (It's next on the list.)     

> __< k​ayabanerve:monero.social >__ I have no updates on either.     

> __< k​ayabanerve:monero.social >__ But thank you :)     

> __< r​ucknium:monero.social >__ I skimmed a few related papers on the hash-to-point function. One of them proves that a different hash-to-point function is approximately uniformly distributed. I wonder: would it be useful to do some preliminary statistical tests of the uniformity of Monero's function? If it fails one or more tests, that's a good reason for a researcher to look at its potential biasedness more formally.     

> __< r​ucknium:monero.social >__ Diehard-like tests.     

> __< r​ucknium:monero.social >__ kayabanerve: What do you think? ^     

> __< k​ayabanerve:monero.social >__ I'm honestly unsure the methodology for testing. If you have learned it and want to, I'd be happy to comment as I can, but my expertise on the subject only went as far as to know to hire someone to ensure we're not messing up :p     

> __< r​ucknium:monero.social >__ AFAIK, what I would need would be a large number of the points to test if they are uniformly distributed or (even better) an easy-to-use function that I could use to generate points at will.     

> __< r​ucknium:monero.social >__ I would have to look into this more, but that's what I think would be required.     

> __< r​ucknium:monero.social >__ And then I would have to understand elliptic curves a little if the test is actually uniformity on the curve instead of just uniformity on the set of integers     

> __< j​effro256:monero.social >__ Rucknium: you probably know this already, but it's important to note that a random ed25519/X25519 public key (and therefore key images) as we serialize them will NOT look like a uniform random string since not all (X, Y) combos are valid. And of those (X, Y) combos, we only really use 1/8 of them (the one's without cofactor)     

> __< r​ucknium:monero.social >__ If it doesn't fail any tests, that doesn't necessarily mean that it's unbiased. But if it does fail tests, then that could make a researcher more interested in it.     

> __< k​ayabanerve:matrix.org >__ There's a C++ and a Rust impl     

> __< k​ayabanerve:matrix.org >__ They explicitly shouldn't be uniform over the byte array.     

> __< k​ayabanerve:matrix.org >__ Presumably, the field element should be     

> __< b​oog900:monero.social >__ the original CryptoNote whitepaper claims the hash to point function, as used for original ring signatures, does not need to be perfect: `None of the proofs demands Hp to be an ideal cryptographic hash function. It’s main purpose is to get a pseudo-random base     

> __< b​oog900:monero.social >__ for image key I = xHp(xG) in some determined way.`     

> __< b​oog900:monero.social >__ do our other usages?     

> __< k​ayabanerve:matrix.org >__ The original proof's implementation does allow forgeries of you can predict the HtP IIRC.     

> __< k​ayabanerve:matrix.org >__ ... if you can control its output to a solved for point?     

> __< k​ayabanerve:matrix.org >__ I'm unsure how to phrase it. I don't think that's the risk, due to it using keccak to start, and I wouldn't be surprised if it's fine if it offers a notably reduced bit count than desirable for a hash fn of its length.     

> __< k​ayabanerve:matrix.org >__ But I wouldn't take that informal comment at face value.     

> __< r​ucknium:monero.social >__ Any other comments on this or agenda items?     

> __< j​effro256:monero.social >__ I believe I know of a way that that a valid block could be added to the invalid blocks list. In `Blockchain::switch_to_alternative_blockchain`, if `handle_block_to_main_chain` returns `false` for any reason, we add the alt block and its children to the invalid blocks list. However, `handle_block_to_main_chain` can fail for temporary non-deterministic reasons, one of them being tha<clipped messag     

> __< j​effro256:monero.social >__ t the transactions of that block are not found inside of the mempool. This might have happened during the stressnet because the mempool got full. So if the node attempts reorging from a worse alt chain to the main chain, but a transaction is missing, the main chain block permanently gets added to the invalid blocks list     

> __< j​effro256:monero.social >__ I haven't confirmed it yet, so take it with a grain of salt, but that's maybe a possibility     

> __< r​ucknium:monero.social >__ "one of them being that the transactions of that block are not found inside of the mempool" If that's true, that is a strange design decision.     

> __< r​ucknium:monero.social >__ Transaction propagation on stressnet is not perfect.     

> __< j​effro256:monero.social >__ Well the node inherently can't determine the validity of a block if it doesn't have each tx on hand     

> __< r​ucknium:monero.social >__ Doesn't the fluffy block protocol ask nodes for "missing" txs from the node that sent the block?     

> __< r​ucknium:monero.social >__ There are log messages about requesting the missing txs     

> __< j​effro256:monero.social >__ Yes, usually     

> __< r​ucknium:monero.social >__ I mean, not necessarily in this specific bug, but one of the log categories will give you that log message sometimes     

> __< r​ucknium:monero.social >__ Maybe the sending node doesn't have the tx in its txpool either?     

> __< r​ucknium:monero.social >__ But it would have it in its blockchain     

> __< j​effro256:monero.social >__ But if a block gets added as an alt block, and the txs were ALREADY in the pool, then the txs aren't forced to stay in the pool like they are with a normal fluffy block directly to the main chain.     

> __< r​ucknium:monero.social >__ We can end the meeting here. And continue the debugging discussion after the meeting     

> __< j​effro256:monero.social >__ So this sequence of events could happen: 1) TX T gets propagated, 2) alt block B1 gets added as alt block, 3) full mempool causes TX T to get pushed out 4) alt block B2 has B1 as previous block and gets added as an alt block 5) we attempt to reorg to block B2 6) TX T is not present 7) blocks B1 and B2 get added as invalid blocks permanently     

> __< j​effro256:monero.social >__ (B1 contains TX T btw)     

> __< r​ucknium:monero.social >__ I think this was happening even when the tx pool wasn't full by the way.     

> __< j​effro256:monero.social >__ Would you be able to send me the full log please? I would like to see which reason is logged as the initial failure for `handle_block_to_main_chain`     

> __< r​ucknium:monero.social >__ Yes. When the bug occurred I just had log level 0. But the bug seems to happen about once every 3 days per node. Is there a log level I should set on nodes to get more info?     

> __< j​effro256:monero.social >__ 3 days is actually the interval after which old txs are dropped from the mempool. That might have something to do with it     

> __< j​effro256:monero.social >__ For logging consensus verification errors, you can use log category "verify" and on ERROR level  

# Action History
- Created by: Rucknium | 2024-07-09T21:56:41+00:00
- Closed at: 2024-07-22T20:05:15+00:00
