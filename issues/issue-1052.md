---
title: Monero Research Lab Meeting - Wed 07 August 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1052
author: Rucknium
assignees: []
labels: []
created_at: '2024-08-07T14:39:46+00:00'
updated_at: '2024-08-19T18:10:55+00:00'
type: issue
status: closed
closed_at: '2024-08-19T18:10:55+00:00'
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

#1048 

# Discussion History
## Rucknium | 2024-08-13T15:22:10+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time!     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< c​haser:monero.social >__ hello     

> __< rbrunner7 >__ Hello     

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< o​ne-horse-wagon:monero.social >__ Hello     

> __< r​ucknium:monero.social >__ me: I read a few p2p network privacy papers so I can give feedback about proposed changes to tx propagation protocol. Prepping a new stressnet fork.     

> __< j​effro256:monero.social >__ howdy     

> __< j​effro256:monero.social >__ me: carrot doc     

> __< j​effro256:monero.social >__ me: I found a weird indistinguishability issue with the ephemeral pubkeys that I'm still trying to sort out     

> __< 0​xfffc:monero.social >__ Mostly did spend time on these: (a) reviewed a bunch of different PRs. (b) erlay [1] R&D is almost finished. I am trying to start coding.  ( https://github.com/monero-project/monero/issues/9334 )     

> __< 0​xfffc:monero.social >__ 1. https://arxiv.org/abs/1905.10518     

> __< j​berman:monero.social >__ me: about to submit a WIP PR for fcmp++ integration that presently includes the Rust FFI, curve trees merkle tree, `grow_tree` & `trim_tree` algos, growing the tree in the db as the node syncs, db migration of outputs into the tree, and changes to `cryptonote::transaction` for fcmp's, with a fairly detailed PR description for all components     

> __< j​berman:monero.social >__ Aiming to finish my current CCS this week and open another one to continue on fcmp++ integration     

> __< r​ucknium:monero.social >__ Is the consensus to implement Erlay or just implement the more bandwidth-efficient tx propagation in #9334?     

> __< 0​xfffc:monero.social >__ A bandwidth-efficient tx propagation is the plan so far. Because it is easier. But after some review / coding I will talk to boog about the final decision. ( and of course we have to plan something that we can merge to master eventually )     

> __< r​ucknium:monero.social >__ 3) Stress testing monerod https://github.com/monero-project/monero/issues/9348     

> __< j​effro256:monero.social >__ Are we sure Erlay doesn't impede Dandelion++'s effectiveness at network level privacy?     

> __< r​ucknium:monero.social >__ We plan to continue stressnet for two more months. The stressnet room voted to re-fork testnet from scratch to keep the storage requirements lower. An unpruned stressnet node is about 65GB now.     

> __< 0​xfffc:monero.social >__ Very Good question. There are some side effects from erlay on dandelion++ ( and privacy, generally speaking ). About the bandwidth-efficient tx propagation there is a discussion on that GitHub link I sent.     

> __< r​ucknium:monero.social >__ IIRC the Erlay paper does a privacy analysis for diffusion (i.e. the fluff phase), but it wasn't too detailed.     

> __< b​oog900:monero.social >__ Erlay claims it shouldn't as it will only change the fluff phase     

> __< 0​xfffc:monero.social >__ Yes. And IIRC they don’t have dandelion++ . They just privacy test on bitcoin stack. Which is some-case provided better privacy and somecases worse privacy. ( worse privacy case was not real world imho. It provides worse privacy when substantial portions of the attackers nodes are private node. Which generally does not make sense )     

> __< 0​xfffc:monero.social >__ I have to talk to boog more about this though. To verify I have understood it correctly.     

> __< r​ucknium:monero.social >__ IMHO, with issue #9334, the changes should be implemented in a way to not provide a way of querying the fluff phase txpool with zero delay. Only give the transaction in "push" mode. And the notify_txpool_complement that already exists could be changed to add some delay.     

> __< v​tnerd:monero.social >__ Hi, sorry late     

> __< r​ucknium:monero.social >__ There is at least one privacy risk if malicious nodes can query fluff phase txpools at will. That was my purpose for reading some of the tx proagation papers.     

> __< b​oog900:monero.social >__ we would also have to change fluffy blocks ...     

> __< 0​xfffc:monero.social >__ My apologies. It seems I have missed it. Can you send me few of those tx propagation papers? I am interested in reading more about it.     

> __< b​oog900:monero.social >__ what would be the issue with querying the fluff phase txpool with zero delay?     

> __< 0​xfffc:monero.social >__ ( in your spare time of course )     

> __< r​ucknium:monero.social >__ boog900: An adversary can more easily learn the edges in the p2p network graph.     

> __< r​ucknium:monero.social >__ And an adversary that knows the edges can use more powerful attacks against D++ privacy     

> __< r​ucknium:monero.social >__ I am working on a write-up to put as a comment to the GitHub issue     

> __< r​ucknium:monero.social >__ 0xfffc: Here are the papers I read recently (D++ is a re-read):     

> __< r​ucknium:monero.social >__ Fanti & Viswanath (2017) "Anonymity properties of the bitcoin p2p network"     

> __< r​ucknium:monero.social >__ Venkatakrishnan, Fanti, & Viswanath (2017) "Dandelion: Redesigning the bitcoin network for anonymity"     

> __< r​ucknium:monero.social >__ Fanti et al (2018) "Dandelion++: Lightweight Cryptocurrency Networking with Formal Anonymity Guarantees"     

> __< r​ucknium:monero.social >__ Franzoni & Saza (2022) "Clover: An anonymous transaction relay protocol for the bitcoin P2P network"     

> __< r​ucknium:monero.social >__ They are all on moneroresearch.info     

> __< r​ucknium:monero.social >__ Any comments or questions or about stressnet?     

> __< r​ucknium:monero.social >__ The original Dandelion paper is worth reading since it has theorems on fundamental bounds on the precision and recall of an adversary with any message propagation system.     

> __< 0​xfffc:monero.social >__ Thanks a lot for the list. Particularly the 2022 one. I will read it ( and skim all the papers cited that paper or by that paper ).     

> __< r​ucknium:monero.social >__ And it also contains the calculation for the 10 minute D++ epochs.     

> __< 0​xfffc:monero.social >__ I read dandelion paper like 7,8 months ago. I need a re-read to remember exact details.     

> __< r​ucknium:monero.social >__ IMHO, the clover paper didn't do as deep of an analysis as D++. The Clover paper says D++ and Clover have similar privacy, but it needs more analysis IMHO. The main benefit of clover is that it works for nodes with closed ports. D++ doesn't really work for those nodes.     

> __< r​ucknium:monero.social >__ 4) Potential measures against a black marble attack. https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ Anything on this? If not, we can move on.     

> __< r​ucknium:monero.social >__ 5) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< r​ucknium:monero.social >__ kayabanerve, kayabanerve , jeffro256 , Things to discuss on FCMP?     

> __< j​effro256:monero.social >__ Not too much to mention, just that I'm continuing to work on the Carrot paper     

> __< j​effro256:monero.social >__ jberman is more involved in FCMP development     

> __< j​berman:monero.social >__ I think the incoming PR will yield some more discussion, but nothing for now from me     

> __< r​ucknium:monero.social >__ Anything more to discuss? AFAIK, hinto 's question about deprecating binary JSON contents is being put in the Seraphis workgroup and/or in a bigger #monero-dev meeting.     

> __< rbrunner7 >__ Yes. Is it ok I bring up now the meta-issue of re-establishing something like dev meetings?     

> __< a​aron:cypherstack.com >__ AIUI kayabanerve is fine with Cypher Stack releasing the recent divisor review report     

> __< r​ucknium:monero.social >__ Sounds good to me :)     

> __< rbrunner7 >__ Alright     

> __< a​aron:cypherstack.com >__ but will wait for another confirmation on this     

> __< rbrunner7 >__ We have Monero dev related topics and questions every now and then that are not a natural fit for the MRL meeting, nor for the Seraphis wallet workgroup meetings on Mondays in the form and scope those two meetings currently have.     

> __< rbrunner7 >__ Like that issue of hinto you mentioned     

> __< rbrunner7 >__ As that issue came up here last Monday, later that day in the workgroup meeting I asked people what they would think about broadening those meetings and turn them into something more general like the dev meetings of yesteryears.     

> __< 0​xfffc:monero.social >__ Apologies for asking unrelated question in the middle of meeting.      

> __< 0​xfffc:monero.social >__ Do we have specific group to follow fcmp integration / dev? I am very interested to follow their work too. (Eventually I want to get involved there too.)     

> __< a​aron:cypherstack.com >__ kayabanerve kayabanerve: if you could confirm this, would be very helpful! Then we can get it posted to a GH repo within the hour     

> __< j​effro256:monero.social >__ Closest thing is #no-wallet-left-behind:monero.social     

> __< 0​xfffc:monero.social >__ Thanks.     

> __< rbrunner7 >__ Anyway: The attending people mostly found "dev meetings again, same day and time as the workgroup meetings so far" a good idea. What do people here think about this?     

> __< rbrunner7 >__ Yeah, those meetings, for lack of a Seraphis wallet push, have more or less mutated into FCMP meetings now :)     

> __< v​tnerd:monero.social >__ I'm in support of a more general -dev meeting, primarily because the bulk of my reports would be more appropriate there     

> __< rbrunner7 >__ If yes, the proposal was also made to relocate the meeting to the monero-dev channel. To make things clear, so to say.     

> __< rbrunner7 >__ If people are ok with me, I am ready to continue to moderate     

> __< j​effro256:monero.social >__ Right now reviews are lagging pretty hard behind development (primarily IMO because so many people are focused on the upcoming upgrade, myself included). General -dev meetings *might* help that     

> __< j​berman:monero.social >__ I think it makes sense to relocate NWLB meetings to -dev meetings at this point     

> __< a​aron:cypherstack.com >__ \     

> __< a​aron:cypherstack.com >__ Ugh, sorry... cat walked on my keyboard     

> __< rbrunner7 >__ Ok. I will announce next Monday's meeting as such, and if no surprising opposition or alternative arrives, we will have a "dev meeting 2.0" then :)     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< j​effro256:monero.social >__ Thanks everyone. (Especially Aaron's cat)     

> __< a​aron:cypherstack.com >__ Alas, it is not sarangcat, who sadly passed away last year. It is one of his successors, whom we fostered-to-adopt from a nearby shelter!     

> __< k​ayabanerve:monero.social >__ Apologies for not being present. I don't have anything to add other than my work on prepping libs for auditing, assuming review passes.     

> __< k​ayabanerve:monero.social >__ AaronFeickert: If you're fine with it and have made any presentation changes you want.     

> __< k​ayabanerve:monero.social >__ Though I'll note it likely opens its own discussion to have within a MRL meeting.     

> __< a​aron:cypherstack.com >__ OK, will post to GH shortly     

> __< j​berman:monero.social >__ RIP sarangcat     

> __< a​aron:cypherstack.com >__ Thanks jberman; was a very very sad day     

> __< a​aron:cypherstack.com >__ I like to think that his kitty spirit lives on in his successors, who are very delightful little demons     

> __< a​aron:cypherstack.com >__ Fortunately sarangcat lived to the ripe old age of 17     

> __< j​effro256:monero.social >__ Wow     

> __< o​frnxmr:monero.social >__ Perfectly on topic, no worries     

> __< o​frnxmr:monero.social >__ My condolences     

> __< a​aron:cypherstack.com >__ Much appreciated! May I recommend supporting local animal shelters     

> __< a​aron:cypherstack.com >__ One of his successors was found wandering a neighborhood, and was brought in to keep him safe. The other successor was abandoned in a carrier at a big-box store     

> __< a​aron:cypherstack.com >__ But I am happy to report that both are doing well and living their best cat lives :D     

> __< a​aron:cypherstack.com >__ Divisor report: https://github.com/cypherstack/divisor-report/releases/tag/final     

> __< a​aron:cypherstack.com >__ ^ kayabanerve     

> __< k​ayabanerve:monero.social >__ My summary is the technique is agreed to be sound, yet there's questions about how to derive an actual efficient proof from it. Veridise is currently reviewing my derived R1CS gadget premised on divisors. That at least gets their signature, even if it doesn't let people trivially do their own review. There's an open question of if we want to have Veridise expand their work (expand<clipped mess     

> __< k​ayabanerve:monero.social >__ ing their hours) and what additional review we'd like on the gadget.     

> __< nioCat >__ <r​ucknium:monero.social> ...The main benefit of clover is that it works for nodes with closed ports. D++ doesn't really work for those nodes. <<>> does this mean that D++ doesn't really work without inbound connections open?     

> __< 0​xfffc:monero.social >__ nioCat Can you expand on “closed ports”?     

> __< nioCat >__ I guess that's the question I was asking  :)     

> __< v​tnerd:monero.social >__ D++ stem phase uses outbound connections only. If a node has closed incoming ports, the first/next hop could theoretically determine that a tx originated at the prior node, assuming they can determine closed port vs full incoming p2p table (which I believe is possible)     

> __< v​tnerd:monero.social >__ One is at the OS/router level, and the other is a policy of monerod     

> __< v​tnerd:monero.social >__ Although, if node has tor/i2p setup, they could be relaying a tx received over those networks, so the check isn't foolproof     

> __< v​tnerd:monero.social >__ The main issue is that the node is never participating in d++ stem phase     

> __< k​ayabanerve:monero.social >__ cc AaronFeickert to agree/disagree/expand on the above     

> __< k​ayabanerve:monero.social >__ (my above message, not the D++ commentary, sorry)  

# Action History
- Created by: Rucknium | 2024-08-07T14:39:46+00:00
- Closed at: 2024-08-19T18:10:55+00:00
