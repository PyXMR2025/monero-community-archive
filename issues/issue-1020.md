---
title: Monero Research Lab Meeting - Wed 05 June 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1020
author: Rucknium
assignees: []
labels: []
created_at: '2024-06-04T21:02:55+00:00'
updated_at: '2024-06-12T23:53:57+00:00'
type: issue
status: closed
closed_at: '2024-06-12T23:53:57+00:00'
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

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1015

# Discussion History
## Rucknium | 2024-06-05T22:50:08+00:00
Logs

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< a​rticmine:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1020     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< jberman >__ hello     

> __< spackle >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< c​haser:monero.social >__ hello     

> __< v​tnerd:monero.social >__ Hi     

> __< jberman >__ me: trim_tree for the fcmp tree     

> __< r​ucknium:monero.social >__ me: Working a little more on the black marble optimal ring size and fee analysis. Helping spackle with setting up the new stressnet. Working on my MoneroKon presentation "Hard Data on Banking the Unbanked with Cryptocurrency".     

> __< a​rticmine:monero.social >__ I am finalizing the scaling changes. Will be presenting them at MoneroKon, on Friday.     

> __< b​oog900:monero.social >__ Hi     

> __< v​tnerd:monero.social >__ Me: testing the LWS remote scanning feature, which led to a few bug fixes     

> __< v​tnerd:monero.social >__ Although the bugs were unrelated to the feature, and required some backporting to release branches     

> __< 0​xfffc:monero.social >__ me: worked on few reviews here and there. Worked on a fix for duplicate transactions in fluff queue. Had no familiarity with fluff and stem, so took a long time to understand the code, and finally it is done. Initial planning with spackle and rucknium on monero stressnet and monerod torture test.     

> __< r​ucknium:monero.social >__ 3) Stress testing `monerod` https://github.com/monero-project/monero/issues/9348     

> __< spackle >__ me: running a testnet fork for stress testing     

> __< r​ucknium:monero.social >__ spackle, do you want to explain what you've been working on?     

> __< spackle >__ I've made a few attempts at stress testing monerod     

> __< spackle >__ Running a 10 node private testnet on a single machine did not stress things as desired.     

> __< spackle >__ So I have forked the testnet to create an abusable network for testing monerod.     

> __< spackle >__ The 'stressnet' is running now (https://github.com/spackle-xmr/monero)     

> __< spackle >__ The next important step is creating a release + binaries for others to run. Gitian is new to me, and I am having some difficulties with the process.     

> __< r​ucknium:monero.social >__ Recently we got the txpool to almost 200MB. More than 16 hours of backlogged txs.     

> __< spackle >__ That said, things are running fine and I have been able to see some of the limits of the daemon with some early spamming. Even with low connection counts, performance limits have been observed.     

> __< r​ucknium:monero.social >__ The monerod with the v17 hardfork for testnet self-compiles and runs fine. The harder part is trying to have a real build process for the binaries on all the operating systems so people who can't/won't compile can join the network if they want.     

> __< r​ucknium:monero.social >__ I think we saw problems with tx and block propagation already with just 6 nodes.     

> __< r​ucknium:monero.social >__ plowsof and selsta have helped with trying to troubleshoot the gitian build process :)     

> __< spackle >__ Which is much appreciated, of course.     

> __< r​ucknium:monero.social >__ I think 0xfffc  is going to help with how to measure performance precisely and try to figure out where in the code the bottlenecks are. I think what we have is a workable base.     

> __< sech1 >__ is there any write up of the problems? What was the bottleneck - CPU, memory, network, SSD?     

> __< 0​xfffc:monero.social >__ Yes. Once we got the stressnet, the other side (debugging/profiling) will be my responsibility     

> __< 0​xfffc:monero.social >__ That yes was reply to this message.     

> __< r​ucknium:monero.social >__ sech1: I think at this stage we are just experimenting and making sure that the network is running correctly and the spam script works. And figuring out the rough limits.     

> __< r​ucknium:monero.social >__ spackle's node that received the spam got to 17GB of RAM at one point. Before we had a hypothesis that maybe monerod's LMDB was loading the DB into RAM and that's why some people were seeing too much RAM usage. But the testnet DB is less than 10 GB, so that hypothesis seems unlikely now.,     

> __< r​ucknium:monero.social >__ "A lot of 150/2 transactions in the txpool causes memory spike / OOM daemon" https://github.com/monero-project/monero/issues/9317     

> __< b​oog900:monero.social >__ I made a small program using Cuprates P2P stack to make and maintain loads of connections to a single node, my plan is to pop blocks back to around when nodes crashed and start pushing txs from the blocks after to the txpool     

> __< r​ucknium:monero.social >__ My hypothesis is that something about preparing txs to be sent p2p and to wallets uses RAM, and then the RAM isn't released maybe.     

> __< b​oog900:monero.social >__ the connections don't do anything, just enough to stay connected, but monerod will still fluff txs to them     

> __< a​rticmine:monero.social >__ What kind of TPS are we talking about here?     

> __< r​ucknium:monero.social >__ I think spackle was pushing 5 tx/sec. It was pushing up txpool size since blocks can't include that many txs at that rate of course     

> __< spackle >__ For the stressnet? In my trials I have used a single daemon instance with an rpc wallet. That setup is limited to creating ~15tps, and I believe that entirely occupies the daemon.     

> __< 0​xfffc:monero.social >__ Once we had stressnet (which is very useful idea), it is going to be much easier to debug the monerod code and find bottlenecks. I would focus on getting stressnet going as first step. ( Thanks to spackle and ruck )     

> __< r​ucknium:monero.social >__ spackle seems to have a configurable spammer. It can change the tx/sec and the fee of the txs     

> __< spackle >__ During tx creation the daemon connected to the rpc wallet would not be able to send txs to other nodes unless there was a break in the spam. At times, there was 40MB of txs that were not relayed.     

> __< r​ucknium:monero.social >__ Anyone can join the stressnet by compiling this monerod and running as `--testnet`: https://github.com/spackle-xmr/monero . Ignore the releases because we are still not getting the releases right.     

> __< r​ucknium:monero.social >__ `--max-connections-per-ip=1000` is also recommended since there are a few nodes running from the same IP     

> __< v​tnerd:monero.social >__ Rucknium:  there's a couple of vectors and deque where shrink to fit could be used. Seems unlikely but worth a look     

> __< v​tnerd:monero.social >__ Or no deque, just a vector I think     

> __< jberman >__ sounding like a productive endeavor, thank you guys     

> __< 0​xfffc:monero.social >__ One of the areas that needs that stressnet is locking. My rwlock, initially introduces something like %15 speed up compared to baseline, but later it causes slowdown of %10 compared to baseline. (As sgp tested it under their heavy usage node). Once we had stressnet, I can run it long time and find out the reason for slowdown for rwlock. Right now I don’t have access to any kind <clipped message>     

> __< 0​xfffc:monero.social >__ of heavy usage node.     

> __< a​rticmine:monero.social >__ I agree. This is a very  productive endeavor. Thank you.     

> __< r​ucknium:monero.social >__ Special thanks to spackle!     

> __< r​ucknium:monero.social >__ 4) Potential measures against a black marble attack https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ I write two more solution concepts for my model. The solution concept in the current paper draft is the ring size/fee optimizers of cost effectiveness when you have certain inequality constraints. Two other ones: 1) Best cost effectiveness when you have the _equality_ constraint of a certain effective ring size (i.e. must be on the effective ring size line). 2) Give Alice a budget<clipped message     

> __< r​ucknium:monero.social >__  constraint. Alice has to spend less than a certain amount on aggregate tx fees and node storage costs. That's another inequality constraint to the main model. I don't have results to share about those two solution concepts yet.     

> __< c​haser:monero.social >__ great! I don't know how helpful that is, but I think a constraint on the tx generation/verification time would (also) be useful     

> __< r​ucknium:monero.social >__ That could be a good idea, too. Thanks.     

> __< r​ucknium:monero.social >__ 5) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< r​ucknium:monero.social >__ Any updates on FCMP to discuss?     

> __< jberman >__ no news from me     

> __< r​ucknium:monero.social >__ Any other agenda items?     

> __< r​ucknium:monero.social >__ I have a question maybe someone could answer. When exactly does monerod verify the expensive cryptography in a tx? When nodes get a new tx from peers, there is some verification, but from my view of the code it looks like it may be quick hash verification. But probably nodes do not wait until they get a fluffy block to do the full verification.     

> __< r​ucknium:monero.social >__ To me it looks like nodes do the hash verification on every tx that they get from a peer even if they have seen the tx from another peer before. If they are doing the full verification at that step, that's more reason to consider boog900 's suggestion to reduce duplicate tx gossip messages.     

> __< r​ucknium:monero.social >__ This log message fires whenever nodes get new txs from peers: https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L990     

> __< r​ucknium:monero.social >__ Which seems to run this hash verification function: https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/cryptonote_basic/cryptonote_format_utils.cpp#L253     

> __< jberman >__ in here: https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1038     

> __< r​ucknium:monero.social >__ I have done most of the parsing work of the p2p logs that were running during some of the spam. This question formed when I was looking at the data since I get all these messages about each tx being added (to something).     

> __< r​ucknium:monero.social >__ Thanks!     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< 0​xfffc:monero.social >__ Thanks everyone     

> __< c​haser:monero.social >__ thank you all for your work!     

> __< v​tnerd:monero.social >__ https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/cryptonote_core/tx_pool.cpp#L263     

> __< v​tnerd:monero.social >__ I believe is where the expensive crypto checks are performed. This will only occur if the tx isn't in the txpool already     

> __< v​tnerd:monero.social >__ https://github.com/monero-project/monero/pull/9135 is a review that should speed up new tx processing a bit. A reminder (mainly for myself) to review as this could/should be shipped by now    

# Action History
- Created by: Rucknium | 2024-06-04T21:02:55+00:00
- Closed at: 2024-06-12T23:53:57+00:00
