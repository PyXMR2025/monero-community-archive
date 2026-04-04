---
title: Monero Research Lab Meeting - Wed 20 August 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1256
author: Rucknium
assignees: []
labels: []
created_at: '2025-08-19T21:15:57+00:00'
updated_at: '2025-08-28T20:54:10+00:00'
type: issue
status: closed
closed_at: '2025-08-28T20:54:10+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).

4. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

5. [Spy nodes](https://github.com/monero-project/research-lab/issues/126).

6. PoW mining pool centralization. [Monero Consensus Status](https://moneroconsensus.info/). [Bolstering PoW to be Resistant to 51% Attacks, Censorship, Selfish Mining, and Rented Hashpower](https://github.com/monero-project/research-lab/issues/136). [Mining protocol changes to combat pool centralization](https://github.com/monero-project/research-lab/issues/98).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1254 

# Discussion History
## venture-life | 2025-08-20T11:11:49+00:00
I have formulated a proposal to counter selfish-mine. It is **not** the one discussed in IRC/Matrix earlier (which admittedly was quite stupid), but a new one. 
I hope it is constructive and makes sense.
https://github.com/monero-project/research-lab/issues/141

## Gingeropolous | 2025-08-20T12:43:08+00:00
**Detective Mining:**
Short Fix
No hard fork

https://github.com/monero-project/research-lab/issues/140
https://eprint.iacr.org/2019/486
https://ceur-ws.org/Vol-3304/paper15.pdf ( i think this is the same idea)

**Fast blocks:**
Hard fork required

i can't find a clear article describing this, but basically faster blocks means a private miner has less time to obtain a lead in secret (in theory). 

## Gingeropolous | 2025-08-20T14:09:37+00:00
**Friction:**
Long term fix
hard fork

Amends fork choice rule to give greater weight to blocks produced by miners that have a history of mining

## spirobel | 2025-08-20T16:47:38+00:00
not really propose an agenda item, but **propose to make two more productive**:

5. On the topic of spy nodes: If I remember correctly from the cuprate meeting on the cuprate tor implementation, boog mentioned there is trouble accepting p2p nodes over tor, because it is too cheap to make new tor hidden service addresses. (so there is the risk of eclipse attacks if tor peers are accepted.) The block lists on spy nodes seem to operate on ip addresses as  well. Is there a similar concern or do they also contain hidden service addresses?

This ties into the proposed TFL work on number 6. **Could the stake be used as a way to mitigate against the costless creation of spy nodes / eclipsing peers?** could that potentially help to reduce our reliance on the cost of acquiring ip addresses to mitigate these issues and we could allow nodes to completely operate behind tor more safely?

6. **We should find some consensus on which questions we want to see answered as a result of the CCS proposal.** The comment by jberman had some very reasonable thoughts. I added two questions as well and gave my reasoning for it: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/604#note_31341

A)  How low can the staked percentage of the total marketcap be, to achieve the same cost that is needed for an attacker to shut off our current PoW system consistently over time?
B) The second question I am interested in is how higher stake behaves during real outages.

Here is my whole comment to spare you the click through:

supporting this proposal does not mean supporting pos or hybrid pow-pos. I also disagree specifically with the stated paper preference and still proudly gave the first thumbs up. This discussion is necessary and it will make Monero stronger in the long run. We need to form a well informed position on this topic that stays up to date with the current state of the art.

The question I am most interested in: How low can the staked percentage of the total marketcap be, to achieve the same cost that is needed for an attacker to shut off our current PoW system consistently over time?

I wrote something on this topic here (copied below for reference): 
https://github.com/serai-dex/serai/issues/333#issuecomment-3194677441

It is interesting that the response to weightless stake is a comment regarding network topology. 

Lets accept the assumption that there will be a time when we have to choose between liveness and safety according to CAP / FLP impossibility. 
This situation happened to Bitcoin multiple times. One time in 2013 and once in 2010:
2010:
>On August 15 2010, it was discovered that block 74638 contained a transaction that created 184,467,440,737.09551616 bitcoins for three different addresses.[1][2][3] Two addresses received 92.2 billion bitcoins each, and whoever solved the block got an extra 0.01 BTC that did not exist prior to the transaction. This was possible because the code used for checking transactions before including them in a block didn't account for the case of outputs so large that they overflowed when summed.[4]

>A new version of the client was published within five hours of the discovery that contained a soft forking change to the consensus rules that rejected output value overflow transactions (as well as any transaction that paid more than 21 million bitcoins in an output for any reason).[5] The block chain was forked. Although many unpatched nodes continued to build on the "bad" block chain, the "good" block chain overtook it at a block height of 74691[6] at which point all nodes accepted the "good" blockchain as the authoritative source of Bitcoin transaction history. src: https://en.bitcoin.it/wiki/Value_overflow_incident

2013:
>What had happened was the following. The latest version 0.8 release of bitcoind, by far the most popular implementation of Bitcoin used by miners, switched the database that it used to store blocks and transactions from BerkeleyDB to the more efficient LevelDB as part of an effort to reduce blockchain synchronization time. **However, what the developers did not realize at the time was that by doing so they also accidentally introduced a change to the rules of the Bitcoin protocol.** src: https://bitcoinmagazine.com/technical/bitcoin-network-shaken-by-blockchain-fork-1363144448

As a result of this assumption we are not operating under Byzantine conditions when we are not faced with this choice.
Both Proof of Work and Proof of Stake impose a cost on an adversary that wants to force the network into this state. 

There are two negative side effects as a result of this state:
1. potential loss for a counterparty not aware of Byzantine conditions
2. temporary existential crisis of the market during these moments (as it operates under the wrong assumption that the network has permanently solved for surviving the Byzantine state automatically)

There is also potential gain (with or without getting caught) for the attacker: 
1. tricking the unaware counterparty into handing over something valuable
2. shorting the market on potentially KYC free exchanges

PoW and PoS impose this cost on the adversary as a side product of their protocols that pretend to operate under Byzantine conditions. To evaluate if this cost is large enough and the system is stable, as well as to assess if any unnecessary caveats are introduced, lets consider a protocol according to this concept we refer to as Proof of Generals for now (if anyone has a suggestion for a better name, go ahead).
Description of the protocol:
A leader is picked with round robin in the order that the Generals Bond of the nodes was locked. The nodes check if the proposed block is valid and publish the result. We define a finality value as such that we are willing to shut down the network if an attacker pays this price. The nodes will calculate the number of votes times the Generals Bond and verify the block. If the value is equal to or higher than the defined finality value and the block is invalid, the node will terminate.

Once the network is restarted, the leader that proposed the invalid block and all the nodes that voted to verify it as a valid block will have their Generals Bond wiped out.

What is the result of this? 

The network is permissionless. The Generals Bond is to be picked reasonably low, so that anyone who can afford to run a server will be able to afford running a node that actively participates in the networks security. 

There is no ability for an attacker to profit from this, as 
1. Every counterparty that runs the node software will be shut down and be aware of the failure. So it will be impossible for an adversary to trick them into handing over valuables while unaware. 
2. The market is aware that a liveness failure is not a safety failure. The finality value has to be picked high enough, to outweigh the potential to profit from a liveness outage.

How do PoW, PoS or PoW-PoS hybrid solutions compare according to this framework?

According to this [article](https://powerupprivacy.com/2025/03/05/monero-fifty-one-percent-attack-analysis.html) the hardware cost is around 13 million usd in terms of CPUs to perform this attack on Monero. To account for other necessary hardware and electricity we set the finality value to 20 million to construct an equivalent under the Proof of Generals framework.
Under PoW the community has to own at least a similar amount of CPUs and consistently outbid the attacker(if the attacker decides to add more CPUs) to restart the network and keep it running. The PoG system will be free to restart while the attacker loses 20 million.

In PoS systems the necessary stake is often picked in such a way that creates a quasi permissioned network as it prices out most people from realistically running a node. This ties back to the beginning: the stake is not just used to prevent this attack it is also used to create a certain network topology. Rewards for block production create incentives to DDOS leaders and make the security of the system harder to reason about in general.

In the case of hybrid PoW-PoS protocols it really depends on the details and which of the two takes precedence.

**The second question I am interested in is how higher stake behaves during real outages.** Continuing the discussion from MRL https://libera.monerologs.net/monero-research-lab/20250818 it seems like the empirical evidence does not point towards higher percentage staked being helpful in securing the network.


## Rucknium | 2025-08-20T16:58:33+00:00

Sub-items for "PoW mining pool centralization"


## Short-term

**Rent hashpower to increase honest hashpower share. (HF not required)**
https://www.miningrigrentals.com/rigs/randomx
https://i.imgur.com/MQZcVC8.png (Chart by Eddie)
https://xcancel.com/xenumonero/status/1957403356462268705

**Follow DNS checkpoints by default (HF not required)**
https://docs.getmonero.org/infrastructure/monero-pulse

**Detective mining (HF not required)**
https://github.com/monero-project/research-lab/issues/140
https://eprint.iacr.org/2019/486
https://ceur-ws.org/Vol-3304/paper15.pdf


## Medium-term

**N-block rolling checkpoint (HF recommended)**
https://blog.bitmex.com/bitcoin-cash-abcs-rolling-10-block-checkpoints/

**Shorten target block time interval (HF required)**
https://bitcoincashresearch.org/t/lets-talk-about-block-time/471
https://blog.ethereum.org/2015/09/14/on-slow-and-fast-block-times/
> The conclusion of all this is simple: faster block times are good because they provide more granularity of information. In the BFT [Byzantine Fault Tolerant] security models, this granularity ensures that the system can more quickly converge on the "correct" fork over an incorrect fork, and in an economic security model this means that the system can more quickly give notification to users of when an acceptable security margin has been reached.


## Long-term

**Require Blocks be Signed by the Miner's Key (HF required)**
https://github.com/monero-project/research-lab/issues/136
> With a minimum of 1% of the block reward before penalty or fees in a single transaction signed. As an option 10% of the total block reward in multiple transactions could also be allowed 

**Construct RandomX cache by selecting random parts of the blockchain (HF required)**
https://github.com/monero-project/research-lab/issues/98

**Countering Selfish-Mine: Promote orphans to uncles (equal pay) and choose deterministically in stratum) who becomes father (HF required)**
https://libera.monerologs.net/monero-research-lab/20250820#c568556-c568579

**Friction (HF required)**
"Amends fork choice rule to give greater weight to blocks produced by miners that have a history of mining"

**Proportional Reward Splitting (HF required)**
Paper claims that Proportional Reward Splitting can defeat a selfish miner that has up to 38% of hashpower
https://arxiv.org/abs/2503.10185

**Finality Layer (HF required)**
https://github.com/monero-project/research-lab/issues/135
https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/604



## Rucknium | 2025-08-23T16:33:54+00:00
Logs

> __< r​ucknium:monero.social >__ The sub-items I have for mining pool centralization: https://github.com/monero-project/meta/issues/1256#issuecomment-3207278521     

> __< s​pirobel:kernal.eu >__ can you add the two questions from my comment to the TFL subpoint?     

> __< r​ucknium:monero.social >__ Can you type them here? Your comment is long     

> __< s​pirobel:kernal.eu >__ jbermans comment has some good thoughts as well. maybe we can condense those into questions and add them too     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1256     

> __< j​effro256:monero.social >__ Howdy     

> __< s​pirobel:kernal.eu >__ A) How low can the staked percentage of the total marketcap be, to achieve the same cost that is needed for an attacker to shut off our current PoW system consistently over time?     

> __< s​pirobel:kernal.eu >__ B) The second question I am interested in is how higher stake behaves during real outages.     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ hello     

> __< s​gp_:monero.social >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< v​enture:monero.social >__ Hello     

> __< s​pirobel:kernal.eu >__ hai     

> __< g​ingeropolous:monero.social >__ hi     

> __< b​oog900:monero.social >__ Hi     

> __< v​tnerd:monero.social >__ hi     

> __< a​rticmine:monero.social >__ Hi     

> __< k​ill-switch:matrix.org >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< j​berman:monero.social >__ me: final tasks in prep for the FCMP++ alpha stressnet (reviewed 9473, tested forking from testnet). All code right now for the alpha stressnet is in review. I spun up the current testnet, forked it locally, and found/patched a couple bugs. We should be good to go forking from current testnet once the fixes are merged     

> __< a​rticmine:monero.social >__ I am working on the block signing remix proposal and also doing research on Proof of Stake in general     

> __< g​ingeropolous:monero.social >__ me: ironing out monerosim     

> __< v​tnerd:monero.social >__ me: updated/rebased existing prs, bug fix for lwsf tx construction, read a few papers on selfishing mining mitigation/prevention, etc     

> __< s​gp_:monero.social >__ Veridise is nearing completion of their research on the Helios/Selene pair, as part of the FCMP++ work. The formal verification of the library will follow that     

> __< o​frnxmr:monero.social >__ trying to reproduce an issue i had with big blocks. Issue disappeared when the txpool expired     

> __< r​ucknium:monero.social >__ me: Performed some network construction simulations to help analyze "p2p: Improved peer selection with /24 subnet deduplication to disadvantage 'spy nodes'"  https://github.com/monero-project/monero/pull/9939 . See my comments in that PR. Looking at research literature on hardening PoW against attackers. Helping test rolling DNS checkpoints on the public testnet with ofrnxmr   ,  <clipped message     

> __< r​ucknium:monero.social >__ vtnerd , and tevador . Visualizations (4 different subdomains): https://testnetnode{1,2,3,4}.moneroconsensus.info/     

> __< j​effro256:monero.social >__ Trying to hit back review backlog for both FCMP++ and the core repo, and working on integrating tevador's double hashing idea     

> __< s​pirobel:kernal.eu >__ wrote out a framework for judging the relative security of pow / pos / pow-pos hybrid solutions. https://github.com/monero-project/meta/issues/1256#issuecomment-3207233765 and took a look at the monero-oxide audit / started migrating to the crate     

> __< v​enture:monero.social >__ embarrassed myself with a very naive idea with outlandish numbers and that would have let to bifurcations, thankfully the community was there :) Researched more on countering selfish-mine     

> __< r​ucknium:monero.social >__ 3) Transaction volume scaling parameters after FCMP hard fork.  https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf     

> __< a​rticmine:monero.social >__ One of the considerations here is that regardless of the valuation of verification time, we must allow the weight s to scale for large weight transactions     

> __< a​rticmine:monero.social >__ Otherwise it is possible to launch a zero cost DDOS attack on the nodes     

> __< o​frnxmr:monero.social >__ I don't understand why charge more for larger txs, when smaller txs are better to attack with. Makes sense (to me) to not discriminate against any of them (page 2)     

> __< j​berman:monero.social >__ I followed up on that here: https://github.com/seraphis-migration/monero/issues/44#issuecomment-3187685572     

> __< o​frnxmr:monero.social >__ If the tx is ultimately invalid, then the fees dont matter (do they? Im assuming the fees are irrelevant because an invalid tx wont be mined). For a valid tx, the fees should be inline with cost oer input on lower input txs     

> __< a​rticmine:monero.social >__ I will provide a response in the thread on this.     

> __< j​berman:monero.social >__ if tx is invalid, fees don't matter     

> __< a​rticmine:monero.social >__ The response does not address this issue     

> __< j​effro256:monero.social >__ ArticMine: somewhat related, do you happen to know why the transaction weight limit was changed from (block weight minimum - coinbase_size) to (block weight minimum  / 2 - coinbase_size) in hard fork v8 ?     

> __< a​rticmine:monero.social >__ If the tx does not get mined feed don't matter     

> __< a​rticmine:monero.social >__ Do you mean for node relay?     

> __< a​rticmine:monero.social >__ Fees     

> __< j​effro256:monero.social >__ A 128-in FCMP++ can be bigger than 120kb, which is more than half of the block penalty-free zone (unless we change that in the next HF). I was wondering if there would be any downsides if txs above 1/2 the penalty-free zone were allowed?     

> __< j​effro256:monero.social >__ ArticMine: that tx weight limit is a consensus rule     

> __< j​berman:monero.social >__ (*150kb)     

> __< j​effro256:monero.social >__ Sorry, yes that was a typo. 150kb     

> __< a​rticmine:monero.social >__ So 50% of the penalty free zone     

> __< a​rticmine:monero.social >__ Yes I supported that since it mitigates somewhat my concern over a DDOS attack with un economical transactions     

> __< j​effro256:monero.social >__ > One of the considerations here is that regardless of the valuation of verification time, we must allow the weight s to scale for large weight transactions      

> __< j​effro256:monero.social >__ After thinking about this for a few weeks, I'm not quite convinced that this is true anymore. Like ofrn is saying, you can split the tx into smaller parts, pay a smaller fee, but the change to the block reward penalty would be the same. The additional marginal fee to be imposed by a tx really is a function of the sum total size of the mempool, not any individual tx     

> __< a​rticmine:monero.social >__ One can split up a tx and pay lower fees because it attracts a lower penalty for each split tx. This is a given     

> __< j​effro256:monero.social >__ When it really gets down to it, it's a discrete optimization problem, so optimally it's a function of individual txs, but that's a different discussion. I'm talking about approximations     

> __< s​pirobel:kernal.eu >__ the cost to perform a ddos attack could be increased by having the proposing nodes sign transactions with a bond and slash that bond if they propose tons of invalid transactions     

> __< o​frnxmr:monero.social >__ But i can ddos better with smaller txs, at a lower cost, and higher size     

> __< a​rticmine:monero.social >__ The issue is a spam attack with large weight TXs where the spam TXs do not get minef     

> __< a​ntilt:we2.ee >__ /my     

> __< j​effro256:monero.social >__ But it's the same penalty diff for the sum of those 2 txs     

> __< o​frnxmr:monero.social >__ The fee doesn't matter in that case     

> __< s​pirobel:kernal.eu >__ its really the verification cost of invalid transaction that could become a ddos concern, right?     

> __< a​rticmine:monero.social >__ The two TXs can be in different blocks     

> __< a​rticmine:monero.social >__ So the higher penalty rate is never paid     

> __< j​effro256:monero.social >__ ofrnxmr: the fee still matters. We're talking about valid-proof txs, where the relay fee is less than what would make it economical to mine     

> __< a​rticmine:monero.social >__ This is not about invalid transactions     

> __< j​effro256:monero.social >__ That's different from the discussion where a verification-time DoS is performed with invalid txs. The fee makes no difference in that case     

> __< s​pirobel:kernal.eu >__ how can the verification cost of valid transactions ever be an issue for ddos? if thats the case the fees are too low in general     

> __< j​effro256:monero.social >__ It isn't, but you don't know if it's invalid or not until you validate it     

> __< a​rticmine:monero.social >__ This is not about verification t     

> __< a​rticmine:monero.social >__ Time     

> __< a​rticmine:monero.social >__ I will address this in my response in the thread     

> __< a​rticmine:monero.social >__ On GitHub     

> __< a​rticmine:monero.social >__ Is there any else on this topic?     

> __< r​ucknium:monero.social >__ 4) [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< s​pirobel:kernal.eu >__ on scaling in general I would recommend people to read up on the research about tachyaction. other than that no     

> __< j​effro256:monero.social >__ > The two TXs can be in different blocks      

> __< j​effro256:monero.social >__ > So the higher penalty rate is never paid     

> __< j​effro256:monero.social >__ By that same logic, you can wait until the mempool is more empty to mine the bigger one too and not pay the higher penalty rate     

> __< a​rticmine:monero.social >__ True. This is why we have not yet had a problem with this     

> __< j​effro256:monero.social >__ > on scaling in general I would recommend people to read up on the research about tachyaction. other than that no     

> __< j​effro256:monero.social >__ That's more related to cryptography / data availability and not traditional fee markets though. But yes, an interesting topic for sure     

> __< r​ucknium:monero.social >__ spirobel: This one, right? https://seanbowe.com/blog/tachyon-scaling-zcash-oblivious-synchronization/     

> __< r​ucknium:monero.social >__ AFAIK, final bugs that would affect alpha stressnet are being squashed.     

> __< a​rticmine:monero.social >__ This I have to read especially after the brutal attack on ZCash     

> __< j​berman:monero.social >__ (holding on stressnet until above discussion is finished)     

> __< s​pirobel:kernal.eu >__ yes I posted about this before a while ago in the community workgroup channel. the tldr is that it will change node requirements in the sense that not all key images will have to be kept in memory for verification. so ram requirments get decoupled from archiving the blockchain.     

> __< j​berman:monero.social >__ ok, I have 3 items to raise for FCMP++ alpha stressnet:     

> __< j​berman:monero.social >__ 1) Set a fork date.     

> __< j​berman:monero.social >__ - As proposed in a past meeting, it would fork from current testnet. So get your testnet nodes synced up and ready to go.     

> __< j​berman:monero.social >__   - I would prefer to have all code merged before announcing the official start date and releasing instructions on how to join the stressnet.     

> __< j​berman:monero.social >__   - I would hope to target this coming Tuesday (Aug 26th), but that depends on our ability to get the code merged beforehand.     

> __< j​berman:monero.social >__   - Blocking code is linked here: https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262     

> __< r​ucknium:monero.social >__ IMHO, it's best to wait until the code is 100% ready before setting a date.     

> __< j​berman:monero.social >__ Ok     

> __< j​effro256:monero.social >__ In summary, the blockers now are the PRs created in the wake of the other stressnet, and a wallet sync speedup PR. Nothing super FCMP++ related     

> __< r​ucknium:monero.social >__ Do we need to announce anywhere except here? Isn't there a non-alpha stressnet planned for more community participants?     

> __< j​berman:monero.social >__ 2) Here is a draft post written and ready to blast out: https://paste.debian.net/1392565/     

> __< j​berman:monero.social >__ - It includes instructions (borrowed from jeffro) on how to build monerod, CLI, RPC, and GUI using the expected alpha stressnet code.     

> __< j​berman:monero.social >__   - The code would live on a new branch called "fcmp++-alpha-stressnet" in the seraphis-migration repo.     

> __< o​frnxmr:monero.social >__ Then we'll need to set some roles/rules. I, for example, will volunteer to run a seed node. i think we might have to have controlled mining due to the speed (lack of) of generating txs     

> __< j​berman:monero.social >__ I figured it would be good to make a reddit post     

> __< j​effro256:monero.social >__ What do you mean by "controlling mining"?     

> __< j​effro256:monero.social >__ *controlled     

> __< s​gp_:monero.social >__ Imo, it needs a paragraph on top to remind people what FCMP++ is, in ELI5 language     

> __< o​frnxmr:monero.social >__ i mean, i have a script that only starts mining under certain conditions     

> __< o​frnxmr:monero.social >__ Instead of every 2mins, since i cant fill blocks that fast     

> __< j​effro256:monero.social >__ > Do we need to announce anywhere except here? Isn't there a non-alpha stressnet planned for more community participants?     

> __< j​effro256:monero.social >__ Rucknium : probably the stressnet Matrix room I would think     

> __< r​ucknium:monero.social >__ Difficulty will fall off fast you that is done     

> __< r​ucknium:monero.social >__ fast if*     

> __< o​frnxmr:monero.social >__ For building stressnet - we should release binaries. Building shouldnt be necessary, but of course people can build if they choose to     

> __< o​frnxmr:monero.social >__ Thats fine. My diff is at 2 and i oroduce blocks every 20mins :P     

> __< o​frnxmr:monero.social >__ They are ~17mb, spamming from 4 wallets     

> __< r​ucknium:monero.social >__ I think I can probably use the testnetnode1.moneroconsensus.info nodes as seed node, too. 4 nodes.     

> __< j​effro256:monero.social >__ ofrnxmr: perhaps I could add a tool which re-uses EC blinds and speeds up stressnet tx creation     

> __< j​berman:monero.social >__ Discussed binaries briefly with jeffro. We haven't messed with GUIX building yet, so not sure how that'll go. I pinged tobtoht on it too for thoughts     

> __< j​effro256:monero.social >__ Obviously, you wouldn't want to ever, ever use that for production     

> __< r​ucknium:monero.social >__ I can manage some spamming from the Monero Research Computing Cluster and maybe some from my seed nodes.     

> __< o​frnxmr:monero.social >__ Depends works     

> __< o​frnxmr:monero.social >__ Guix not ready afaict     

> __< j​berman:monero.social >__ Blinds construction is fast now with fabrizio's code merged. It's prove() that's the bottleneck: https://github.com/kayabaNerve/fcmp-plus-plus/issues/34     

> __< s​pirobel:kernal.eu >__ yes I posted about this before a while ago in the community workgroup channel. the tldr is that it will change node requirements in the sense that not all key images will have to be kept in memory for verification. so ram requirements get decoupled from archiving the blockchain.     

> __< j​effro256:monero.social >__ Oh, you're right..     

> __< j​effro256:monero.social >__ Nvm     

> __< r​ucknium:monero.social >__ I think we should see how things go at normal mining speed at first and then adjust if necessary.     

> __< j​berman:monero.social >__ I'm fine with releasing binaries too. I have some reservation on it because it might end up a little annoying if people start doing stuff like using the wrong node/wallet and report bugs from that, and so requiring building at least raises the bar somewhat     

> __< j​berman:monero.social >__ But, if no one shares that concern, then we can do binaries     

> __< j​effro256:monero.social >__ Perhaps we could switch to a fixed difficulty at some point     

> __< r​ucknium:monero.social >__ Is that easy to do? Don't all nodes on the network need to agree for that?     

> __< o​frnxmr:monero.social >__ Probably need like 30+ wallets spamming if were actually pushing for large blocks     

> __< j​effro256:monero.social >__ IIRC, `monerod --version` shows the current commit hash if not a release version, right?     

> __< r​ucknium:monero.social >__ Maybe I can try to Dockerize something :D     

> __< r​ucknium:monero.social >__ I don't really like Docker, but this may be a good usecase.     

> __< o​frnxmr:monero.social >__ it uses 100% cpu     

> __< j​effro256:monero.social >__ We can just ask them what version they're using as the first question     

> __< o​frnxmr:monero.social >__ (wallet does)     

> __< r​ucknium:monero.social >__ 100% of one thread or 100% of the whole CPU?     

> __< j​effro256:monero.social >__ > Is that easy to do? Don't all nodes on the network need to agree for that?     

> __< j​effro256:monero.social >__ Yes, they all need to agree on that. It can be supplied with a CLI argument     

> __< r​ucknium:monero.social >__ The new MRC box has 256 threads and 1TB RAM     

> __< r​ucknium:monero.social >__ Can almost run a Qubic node ;)     

> __< j​berman:monero.social >__ doing things like mixing and matching and not realizing etc.     

> __< r​ucknium:monero.social >__ https://ccs.getmonero.org/proposals/gingeropolous_1TB_MRC.html     

> __< o​frnxmr:monero.social >__ 100% of 8-12cores here     

> __< j​berman:monero.social >__ binaries are fine with me in any case     

> __< r​ucknium:monero.social >__ IIRC, no one got confused when binaries were released for the last stressnet last year. Anyone remember anything about that?     

> __< g​ingeropolous:monero.social >__ yaaas, someone use it!     

> __< o​frnxmr:monero.social >__ binaries were the main deployment     

> __< o​frnxmr:monero.social >__ Only issues we had were "idle" users who didnt update, probably at all     

> __< j​berman:monero.social >__ probably biggest difference is that wallet cache /wallet impl was compatible across versions for that stressnet. the changes for fcmp++/carrot are much more significant     

> __< o​frnxmr:monero.social >__ gingeropolous   how does mrc work, can you set me up a vm or something i can try to spam from?     

> __< r​ucknium:monero.social >__ Anything more that we need to discuss here that shouldn't be shifted to #monero-stressnet:monero.social  ? ( ##monero-stressnet on IRC, IIRC )     

> __< g​ingeropolous:monero.social >__ yeah we can figure it out     

> __< j​berman:monero.social >__ 3rd thing from me:     

> __< j​berman:monero.social >__ I propose that 9473 (allow unrestricted RPC when pool is >100mb) not remain a blocker for stressnet. It has some issues and I want to give 0xFF time to continue on it. If pools end up exceeding 100mb, we can roll out the patch (or push people to use a restricted RPC instead).     

> __< o​frnxmr:monero.social >__ Can just use restricted for the time being, thats what we did last time     

> __< j​berman:monero.social >__ going to remove that as a blocker unless anyone raises objections     

> __< o​frnxmr:monero.social >__ Even if dynamicbss isnt merged to fcmp++-stage, we should merge it to the stress branch/repo     

> __< j​berman:monero.social >__ good with me^     

> __< j​berman:monero.social >__ nothing else from me     

> __< r​ucknium:monero.social >__ Thanks for making the final checklist and moving alpha stressnet forward, jberman     

> __< o​frnxmr:monero.social >__ Rucknium, so you have testnet wallets with a lot of outputs? Or only stressnet     

> __< r​ucknium:monero.social >__ Not so many now, but I will try to mine some.     

> __< r​ucknium:monero.social >__ On public testnet, fees are lower than a from-genesis private testnet, AFAIK     

> __< g​ingeropolous:monero.social >__ i should have a testnet wallet somewhere. xmrchain is mining.     

> __< o​frnxmr:monero.social >__ Yeah, pre-tail, fees are higher     

> __< o​frnxmr:monero.social >__ But my rewards are in the 100s of xmr :P     

> __< r​ucknium:monero.social >__ 5) [Spy nodes](https://github.com/monero-project/research-lab/issues/126).     

> __< r​ucknium:monero.social >__ I ran some network construction simulations to help analyze "p2p: Improved peer selection with /24 subnet deduplication to disadvantage 'spy nodes'" https://github.com/monero-project/monero/pull/9939#discussion_r2285992169     

> __< r​ucknium:monero.social >__ Some interesting findings: The longest distance between nodes on a realistic network of reachable nodes is 4 hops. Converting that to milliseconds of latency using GeoIP data, it takes a maximum of about 110 milliseconds for a message to originate from one node and arraive at the farthest node, assuming speed-of-light speed, shortest straight-line distance between points on the Ea<clipped message     

> __< r​ucknium:monero.social >__ rth's surface, and no CPU processing of messages.     

> __< j​effro256:monero.social >__ Thank you for doing that, Rucknium     

> __< r​ucknium:monero.social >__ By the way, you could probably get an analytical formula to the number of hops, since the graph is approximately 24-regular (12 outbound connections by each node). Somewhere a paper probably has the formula.     

> __< r​ucknium:monero.social >__ Anything else on spy nodes?     

> __< rbrunner >__ Yeah, interesting work, as always     

> __< r​ucknium:monero.social >__ My pleasure :)     

> __< j​effro256:monero.social >__ Switching "already" connected subnet filtering from /16 to /24 doesn't seem to change eccentricity very much, which is good     

> __< a​ntilt:we2.ee >__ is there something else to review ?     

> __< r​ucknium:monero.social >__ On the PR? I don't know. I commented where I thought I could contribute.     

> __< j​effro256:monero.social >__ That was my main concern with /16 to /24 already connected change, so I don't have any major criticisms after that     

> __< j​effro256:monero.social >__ (for the moment)     

> __< a​ntilt:we2.ee >__ jeffro256     

> __< a​ntilt:we2.ee >__ tx     

> __< r​ucknium:monero.social >__ For the next agenda item, I gathered a list of possible proposals to organize the discussion: https://github.com/monero-project/meta/issues/1256#issuecomment-3207278521     

> __< r​ucknium:monero.social >__ We will open the floor for discussion of any type of proposal after we have walked through this specified list.     

> __< r​ucknium:monero.social >__ 6) PoW mining pool centralization. [Monero Consensus Status](https://moneroconsensus.info/). [Bolstering PoW to be Resistant to 51% Attacks, Censorship, Selfish Mining, and Rented Hashpower](https://github.com/monero-project/research-lab/issues/136). [Mining protocol changes to combat pool centralization](https://github.com/monero-project/research-lab/issues/98).     

> __< r​ucknium:monero.social >__ ## Short-term     

> __< r​ucknium:monero.social >__ **Rent hashpower to increase honest hashpower share. (HF not required)**     

> __< r​ucknium:monero.social >__ https://www.miningrigrentals.com/rigs/randomx     

> __< r​ucknium:monero.social >__ https://i.imgur.com/MQZcVC8.png (Chart by Eddie )     

> __< r​ucknium:monero.social >__ https://xcancel.com/xenumonero/status/1957403356462268705     

> __< s​pirobel:kernal.eu >__ just wanted to add one thing on the topic of spynodes     

> __< s​pirobel:kernal.eu >__ If I remember correctly from the cuprate meeting on the cuprate tor implementation, boog mentioned there is trouble accepting p2p nodes over tor, because it is too cheap to make new tor hidden service addresses. (so there is the risk of eclipse attacks if tor peers are accepted.) The block lists on spy nodes seem to operate on ip addresses as well. Is there a similar concern or do<clipped message>     

> __< s​pirobel:kernal.eu >__  they also contain hidden service addresses?     

> __< r​ucknium:monero.social >__ The ban lists do not contain onion hidden service nor I2P addresses. Only clearnet IPv4     

> __< s​pirobel:kernal.eu >__ This ties into the proposed TFL work on number 6. Could the stake be used as a way to mitigate against the costless creation of spy nodes / eclipsing peers? could that potentially help to reduce our reliance on the cost of acquiring ip addresses to mitigate these issues and we could allow nodes to completely operate behind tor more safely?     

> __< r​ucknium:monero.social >__ There is some speculation about if renting hashpower from miningrigrentals (MRR) actually contributes hashpower or if it is just re-distributing honest hashpower.     

> __< j​effro256:monero.social >__ Let's wait to discuss that spirobel     

> __< o​frnxmr:monero.social >__ rucknium, in addition, i also think qubic hash is available to rent     

> __< v​enture:monero.social >__ increase honest hashpower share might be counter-productive. Honest miners are being duped by first_seen and depending on connectivity might even fuel any attack     

> __< r​ucknium:monero.social >__ IIRC, sech1 said he rented hashpower from MMR during the approach of MineXMR to majority hashpower a few years ago. I wonder if he has any information that could shed light on this question.     

> __< v​enture:monero.social >__ imho     

> __< s​gp_:monero.social >__ Does anyone support the monero core team renting hashrate? I'm not sure if this is an idea with supporters or just an idea     

> __< o​frnxmr:monero.social >__ IIUC, MRR can shoe the current hashrate of unrented miners, assuming they arent idle     

> __< sech1 >__ I did, but I don't know where the rigs are mining when not rented     

> __< g​ingeropolous:monero.social >__ i should just setup an account and put my hashrate up for rent and see if it switches me between "mining for me" and "mining for the bidder".     

> __< r​ucknium:monero.social >__ Simply based on observed prices, I think the MRR rigs are not mining when not rented. If they were mining, I would expect that the price would be lower.     

> __< o​frnxmr:monero.social >__ Honestly, imo, no     

> __< o​frnxmr:monero.social >__ It does     

> __< o​frnxmr:monero.social >__ gingeropolous  kawaii did exactly that     

> __< g​ingeropolous:monero.social >__ oh, then, there yah go     

> __< r​ucknium:monero.social >__ I think tevador and myself showed tentative support for the idea of Core renting hashpower.     

> __< o​frnxmr:monero.social >__ https://x.com/kawaiicrypto/status/1950967882747134402     

> __< o​frnxmr:monero.social >__ https://xcancel.com/kawaiicrypto/status/1950967882747134402     

> __< j​effro256:monero.social >__ I think about renting hashpower the same way that Qubic uses their coin to subsidize rewards to spur a higher hashrate: you are infusing external rewards to incentivize participants that wouldn't otherwise be mining without the incentive. Except, ostensibly, you wouldn't donate to a selfish miner     

> __< v​enture:monero.social >__ is that not valid? happy to be wrong..     

> __< o​frnxmr:monero.social >__ Jeffro, qubic could very well be the entity that you are renting from, at 40% surcharges     

> __< tevador >__ If qubic approaches or exceeds 50%, it can help to rent some hashrate.     

> __< r​ucknium:monero.social >__ Qubic had its coin emission "halving" today, by the way: https://qubic.org/halving     

> __< j​effro256:monero.social >__ > Does anyone support the monero core team renting hashrate? I'm not sure if this is an idea with supporters or just an idea     

> __< j​effro256:monero.social >__ sgp_ no since it's a slippery slope and the optics lead people to believe that we've more or less given up on PoW as a secure consensus mechanism     

> __< r​ucknium:monero.social >__ Possibly, the halving means that Qubic has less money to subsidize miners in its pool.     

> __< r​ucknium:monero.social >__ And rbrunner seems to have lost the bet to no one.     

> __< o​frnxmr:monero.social >__ example, i saw rentals from from 0.7ltc per mh to 0.95, and while qubic was doing "4gh" xenus rentals were underperforming     

> __< rbrunner >__ Right!     

> __< v​enture:monero.social >__ no one?     

> __< o​frnxmr:monero.social >__ Go from*     

> __< g​ingeropolous:monero.social >__ in general I don't think its a great first option, but it makes sense to have it as a last resort... though there's no way to tell if we'd be just inadvertently putting money into qubic     

> __< r​ucknium:monero.social >__ No one took to opposing side of the bet, for 0.1 XMR. The bet that Qubic wouldn't actually halve.     

> __< o​frnxmr:monero.social >__ Its a smart business model, for them to rent their hashrate at exotic prices during their marathons     

> __< v​enture:monero.social >__ i should take the handle "no one". I said I take it, question was only how to verify.. than it got lost in chatter     

> __< v​enture:monero.social >__ but i don't claim it     

> __< v​enture:monero.social >__ *then it got lost in chatter     

> __< r​ucknium:monero.social >__ If the Qubic halving has a negative effect on their hashpower, the period of maximum risk have have now passed.     

> __< a​rticmine:monero.social >__ So the threat to Monero with its tail emission has dropped by 50%     

> __< r​ucknium:monero.social >__ may have now passed*     

> __< j​effro256:monero.social >__ Not necessarily, the price per unit of Qubic has gone up in the last 3months     

> __< rbrunner >__ That "halving" is a bit murky anyway     

> __< rbrunner >__ If I understand correctly, issue continues, but burning intensifies: https://qubic.org/blog-detail/qubic-s-epoch-175-halving-understanding-its-role-in-tokenomics     

> __< j​effro256:monero.social >__ Also, the rewards for XMR haven't halved, so I think the threat is definitely not reduced by 50%     

> __< r​ucknium:monero.social >__ We have a lot of items. Any important points remaining on this idea?     

> __< a​ntilt:we2.ee >__ I think checkpointing should deliver an organized PR blow to Q* - is this the next item ?     

> __< a​rticmine:monero.social >__ The price of Qubic in terms of Monero is the critical parameter here     

> __< tevador >__ Renting hashrate is the exact opposite of giving up on PoW.     

> __< a​rticmine:monero.social >__ The other critical parameter is the ratio of the emission rates     

> __< s​pirobel:kernal.eu >__ the tokenomics of this marketing project with a blockchain are wild. so many billions     

> __< rbrunner >__ trillions     

> __< r​ucknium:monero.social >__ **Follow DNS checkpoints by default (HF not required)**     

> __< r​ucknium:monero.social >__ https://docs.getmonero.org/infrastructure/monero-pulse     

> __< s​pirobel:kernal.eu >__ the question is really what the TAM is for their marketing campaign. by know everyone who could possible hear about it has probably been exposed to this     

> __< s​pirobel:kernal.eu >__ the question is really what the TAM is for their marketing campaign. by now everyone who could possible hear about it has probably been exposed to this     

> __< s​pirobel:kernal.eu >__ the question is really what the TAM is for their marketing campaign. by now everyone who could possibly hear about it has probably been exposed to this     

> __< g​ingeropolous:monero.social >__ How often would these checkpoints be checked by monerod?     

> __< r​ucknium:monero.social >__ Like I said in my update, ofrnxmr  , vtnerd  , tevador and myself have been testing following rolling DNS checkpoints to avoid deep re-orgs.     

> __< o​frnxmr:monero.social >__ tristate is doing 2mins. Mainnet selsta proposed 5min. I dont know what is a safe number due to performance hit     

> __< o​frnxmr:monero.social >__ Testnet* is doing 2mins. ginger     

> __< r​ucknium:monero.social >__ Mechanically, it seems to work ok, but some problems to smooth out. Philosophically is a different question.     

> __< v​enture:monero.social >__ yeah, it's akin to trusted seed nodes.. right?     

> __< j​effro256:monero.social >__ I abhor the idea of DNS checkpoints by default. Perhaps a knee-jerk reaction, but the centralization of that approach is unpalatable to me. And "HF not required" is not quite accurate. Every single time a checkpoint is pushed, a new hard fork is created. Ideally, this hard fork is not contentious, non-disruptive, and retroactive, but it is technically a hard fork     

> __< tevador >__ This was proposed as an emergency measure in case qubic gets to 51% and starts orphaning everyone, as they announced.     

> __< o​frnxmr:monero.social >__ i think the main thing here is to not enforce by default     

> __< o​frnxmr:monero.social >__ And to allow mining pools to opt-in     

> __< r​ucknium:monero.social >__ You would want good, reliable DNS propagation. We observed a lot of peer banning when our simulated attack occurred. On mainnet, those net fissures could heal, but it is hard to know how quickly and easily. Monero nodes _love_ banning each other.     

> __< j​berman:monero.social >__ on fluffy's proposal, I brought up the idea of requesting >50% of hash rate defend the network by not mining on top of the attacker's blocks     

> __< j​berman:monero.social >__ I would probably prefer that to checkpoints. But that would not work if the attacker has >50% of the hash rate     

> __< o​frnxmr:monero.social >__ dns blocklist doesnt work for >50% either     

> __< o​frnxmr:monero.social >__ But should work for selfishmining deep reorgs     

> __< tevador >__ DNS checkpoints work for >50%     

> __< o​frnxmr:monero.social >__ only if enforced on everyone     

> __< r​ucknium:monero.social >__ ofrnxmr: It does work in that case, but only for the subset of nodes who have enabled DNS checkpoint enforcing.     

> __< r​ucknium:monero.social >__ technically     

> __< tevador >__ Yes, it's essentially a hard fork that nodes would need to join. Either that or follow the 100% qubic fork.     

> __< o​frnxmr:monero.social >__ The main chain wouldnt be able to overtake an attacking chain with >50%, so those nodes wouldnt switch back     

> __< g​ingeropolous:monero.social >__ I definitely feel the philosophical clash, but moneropulse was meant as training wheels... the ability of the stewards of the project to keep the network healthy as it grows     

> __< o​frnxmr:monero.social >__ yeah     

> __< g​ingeropolous:monero.social >__ the problem is our little network still needs to grow     

> __< o​frnxmr:monero.social >__ Less than 50% is _my_ goal for dns checkpoints. It makes qubic choose to mine honestly, or at mininum, keep reorgs to a low depth     

> __< r​ucknium:monero.social >__ Before this month, CfB (major person in Qubic) announced that they would try to selfish mine Monero for the month of August. Maybe in Sepetmber they will stop.     

> __< a​ntilt:we2.ee >__ PR: we should get the word out on twitter that the option exists;  that their are wasting their time; futile; running against a firewall; etc     

> __< rbrunner >__ In any case, if we do something stupid that makes their win of prestige and attention even larger     

> __< o​frnxmr:monero.social >__ The option doesnt work properly as-is, imo, due to the 1hr interval to check. that would revery 1hr worth of blocks and invalidate a lot of txs     

> __< r​ucknium:monero.social >__ DNS checkpoints are a break-glass-in-case-of-emergency countermeasure. I don't see an emergency yet, but it could happen. I want to keep testing its behavior so the available options are known.     

> __< g​ingeropolous:monero.social >__ and *why* it hasn't grown is a fun rabbit hole of price suppression conspiracy. there are a lot of headwinds, and using this tool to plow forward (if necessary) seems fine. its not a permanent change to anything. it can get turned off. thats not the same as other solutions being proposed     

> __< sech1 >__ tbh they don't rent on MRR, at least the majority of their hashrate comes from datacenters. AWS or Google cloud     

> __< o​frnxmr:monero.social >__ Sech1, i meant they lease their hashrate out on mrr     

> __< o​frnxmr:monero.social >__ During their marathons     

> __< r​ucknium:monero.social >__ selsta said in #monero-dev:monero.social  : "we can reduce the DNS checkpoint load frequency from 1h to like 5min, but i don't think there will be consensus for enabling DNS checkpoints by default, too risky"     

> __< o​frnxmr:monero.social >__ I think thats probably sane, and to recommend miningpools enable the enforcement option, just in case     

> __< r​ucknium:monero.social >__ That is in regards to the next version release of Monero, coming very soon.     

> __< g​ingeropolous:monero.social >__ yeah regardless of whether it will be used, we should definitely figure out if we can use it     

> __< rbrunner >__ +1     

> __< r​ucknium:monero.social >__ IIRC, DataHorader complained that the DNS checkpoint network call was "blocking", i.e. other node operations were paused while it completed. Maybe that could be fixed.     

> __< o​frnxmr:monero.social >__ The other thing that needs to be set/changed if its to be enforced, is reducing the ban time     

> __< r​ucknium:monero.social >__ rbrunner: which statement did you +1?     

> __< rbrunner >__ ginger: find out whether we can use it     

> __< r​ucknium:monero.social >__ DataHoarder*     

> __< DataHoarder >__ correct. that's why it's disabled in recommended p2pool config     

> __< o​frnxmr:monero.social >__ Could be ok if the whole network doesnt ban itself, but probably not ideal to 86400second ban all of your peers that werent using the checkpoints     

> __< j​effro256:monero.social >__ ofrnxmr: what would reducing the ban time do in this scenario? If there is a network split b/t nodes which did not implement DNS checkpoints we can merge together again quicker?     

> __< j​effro256:monero.social >__ Ah ok     

> __< o​frnxmr:monero.social >__ yes     

> __< DataHoarder >__ it blocks operations for a certain number of time, increasing latency for block data     

> __< v​enture:monero.social >__ I think a short-term fix against deep-reorgs at least, is to choose on stratum deterministically which branch to adopt.      

> __< v​enture:monero.social >__ it frees trapped hashrate and would prevent deep reorgs. incentive-wise..i don't know. it fixes gamma to 0.5.     

> __< DataHoarder >__ (it should be done asynchronous from main logic)     

> __< r​ucknium:monero.social >__ Ok I will keep experimenting with it. I have https://testnetnode4.moneroconsensus.info/ set to follow rolling DNS checkpoints on testnet and testnetnode 1 - 3 not following. I will probably change #3 to follow checkpoints to have half  of them following.     

> __< tevador >__ DNS checkpoints are the nuclear option. If we are ready to "press the button", it might be enough to discourage the attack.     

> __< r​ucknium:monero.social >__ _How I learned to stop worrying and love the DNS checkpoints_     

> __< rbrunner >__ Maybe. Attacking and then not succeeding might not cost them much either way.     

> __< r​ucknium:monero.social >__ **Detective mining (HF not required)**     

> __< r​ucknium:monero.social >__ https://github.com/monero-project/research-lab/issues/140     

> __< r​ucknium:monero.social >__ https://eprint.iacr.org/2019/486     

> __< r​ucknium:monero.social >__ https://ceur-ws.org/Vol-3304/paper15.pdf     

> __< a​ntilt:we2.ee >__ yep, psychology is part of it     

> __< v​enture:monero.social >__ "and immediately mines a "counter" child block on top" <-- doesn't this need to have valid PoW, ie takes time?     

> __< a​rticmine:monero.social >__ This falls in my view into the category of low impact mitigations and as such should be supported     

> __< tevador >__ Detective mining won't work against >50%, it's only against selfish mining strategies.     

> __< g​ingeropolous:monero.social >__ well, you can still have >50%. it would prevent the attacker from using the 51% nefariously... maybe?     

> __< v​enture:monero.social >__ tevador I learned your proof, anything that fixes 50% is not PoW anymore :)     

> __< a​rticmine:monero.social >__ While an individual low impact mitigation may have a limited impact on the attacker, the cumulative impact of multiple low impact mitigations can effectively block an attack.     

> __< g​ingeropolous:monero.social >__ just because you have a majority of the hashrate doesn't mean you are going to find all the blocks, unless you selfish mine. probabilistic random blah blah     

> __< v​enture:monero.social >__ question is do we want that protection or encourage mining adoption.     

> __< r​ucknium:monero.social >__ sech1 had thoughts on detective mining. (Just trying to ping sech1 )     

> __< sech1 >__ Either I don't understand something, or it won't do anything against the current attack. I commented there.     

> __< r​ucknium:monero.social >__ sech1 : I agree that there is a risk when the attacking chain gets long.     

> __< j​berman:monero.social >__ On first pass, detective mining seems sensible to attempt me assuming hash rate <50% is willing to implement. If >50% is willing, then I think ignoring the attacker's blocks is optimal. I'll respond to fluffy in a second     

> __< v​enture:monero.social >__ to prevent long growing attacking chains, I think a short-term fix against deep-reorgs at least, is to choose on stratum deterministically which branch to adopt. It frees trapped hashrate and would prevent deep reorgs. incentive-wise..i don't know. it fixes gamma to 0.5.     

> __< tevador >__ I also have doubts about it. I think it's a good strategy to detect a potential attack, but probably not a practical defense. On a related note, it might be a good idea to put an explicit block height into the hashing blob at the next HF.     

> __< g​ingeropolous:monero.social >__ as mentioned, it seems low-impact, otherwise benign     

> __< r​ucknium:monero.social >__ Isn't an attacking chain with parity to the main chain usually last-seen? And when it has +1 advantage over the main chain, it will be chosen to mine on top of anyway?     

> __< g​ingeropolous:monero.social >__ and it falls mostly on pool-ops to implement, and they should be incentivized because they are losing block rewards.     

> __< s​gp_:monero.social >__ I'm certainly interested in a no/low-downsides way to make selfish mining worse, even if it doesn't address 51%+. I haven't had enough time with the proposal to really think about what the potential downsides could be. I think this proposal warrants continued discussion/research     

> __< r​ucknium:monero.social >__ With a hard fork, you could require the RandomX hash to start with the whole block, right? Then mining pools would have to send the whole block and a "detective" would have the block in plaintext.     

> __< r​ucknium:monero.social >__ That would reduce the incentive to produce high-tx blocks, however, I think.     

> __< j​effro256:monero.social >__ This approach simply seems like a much, much more complicated scheme of just not mining on newly encountered alt chains. Selfish mining alt chains will almost propagate after "honest" alt chains, so if miners don't switch chains up to a certain depth, I would think that you can achieve almost the same effect without all the detective work     

> __< v​enture:monero.social >__ that is the re-org point.     

> __< v​enture:monero.social >__ and no, it's not always last-seen. depending on gamma (connectivity of the selfish pool to honest miners), it traps honest ppl onto mining their chain and leaves less hashpower to original one     

> __< tevador >__ rucknium: No, the pool would just send the Blake2b midstate, which is ~200 bytes.     

> __< v​enture:monero.social >__ gamma will reduce over time, or the majority will anyways catch-up, that's when they publish all and do the re-org     

> __< r​ucknium:monero.social >__ tevador: Thanks.     

> __< g​ingeropolous:monero.social >__ jeffro256: , but how do you distinguish between that and a re-org. I guess the case of a netsplit and recover is the only case perhaps.     

> __< sech1 >__ tevador no, not if the whole block is the RandomX input     

> __< s​gp_:monero.social >__ fwiw, my understanding is that this proposal would not discourage selfish mining by an entity that doesn't solicit hashrate from the public. afaik. So there's limited potential benefit     

> __< j​effro256:monero.social >__ gingeropolous: You don't, or you could allow very shallow re-orgs (1 to 2 blocks). But if majority does the same, then you don't lose funds from building "behind"     

> __< tevador >__ If the nonce field comes before the block data, you can't use a midstate. If it comes after, you can.     

> __< g​ingeropolous:monero.social >__ sgp_: but its potentially the most relevant. idle hashpower is sorta the problem here.     

> __< g​ingeropolous:monero.social >__ forcing an attacker to build datacenters is sorta the juice of PoW IMO     

> __< g​ingeropolous:monero.social >__ juice = essence.     

> __< s​gp_:monero.social >__ I think it's hard to definitively say it's the most relevant. If it is expected to be profitable, an attacker could rent private servers and still selfishly mine on their own     

> __< a​rticmine:monero.social >__ It is part of it     

> __< g​ingeropolous:monero.social >__ thats the same sgp_     

> __< r​ucknium:monero.social >__ Is Diego Salazar  from Cypher Stack here?     

> __< d​iego:cypherstack.com >__ always     

> __< r​ucknium:monero.social >__ Are you still considering looking into this issue? Maybe we could divide-and-conquer the vast literature on this topic.     

> __< d​iego:cypherstack.com >__ Yes, we've already done several days of research here.     

> __< r​avfx:xmr.mx >__ y     

> __< r​ucknium:monero.social >__ And I will use this opportunity to share some big-picture papers that I have tentatively put on my reading list:     

> __< r​ucknium:monero.social >__ Zhang, R., Preneel, B. (2019) "Lay down the common metrics: Evaluating proof-of-work consensus protocols’ security." https://doi.org/10.1109/SP.2019.00086     

> __< r​ucknium:monero.social >__ Azouvi, S., Hicks, A. "Sok: Tools for game theoretic models of security for cryptocurrencies." http://arxiv.org/abs/1905.08595     

> __< r​ucknium:monero.social >__ Judmayer et al. (2021) "SoK: Algorithmic Incentive Manipulation Attacks on Permissionless PoW Cryptocurrencies" https://eprint.iacr.org/2020/1614.pdf     

> __< r​ucknium:monero.social >__ Andrew Lewis-Pye, Tim Roughgarden (2024) "Permissionless Consensus" https://arxiv.org/abs/2304.14701     

> __< r​ucknium:monero.social >__ Eric Budish, Andrew Lewis-Pye, Tim Roughgarden (2024) "The Economic Limits of Permissionless Consensus" https://arxiv.org/abs/2405.09173     

> __< r​ucknium:monero.social >__ Budish, E. (2025). "Trust at Scale: The Economic Limits of Cryptocurrencies and Blockchains" https://moneroresearch.info/101     

> __< d​iego:cypherstack.com >__ Luke Szramowski: Rigo Salazar ^     

> __< d​iego:cypherstack.com >__ cuz     

> __< r​ucknium:monero.social >__ The Azouvi & Hicks paper is (2020)     

> __< r​ucknium:monero.social >__ Someone can decode the computer science jargon and I can decode the game theory jargon.     

> __< r​ucknium:monero.social >__ ## Medium-term     

> __< r​ucknium:monero.social >__ **N-block rolling checkpoint (HF recommended)**     

> __< r​ucknium:monero.social >__ https://blog.bitmex.com/bitcoin-cash-abcs-rolling-10-block-checkpoints/     

> __< r​avfx:xmr.mx >__ Diego Salazar Focus follow Mouse, it moved into the matrix window... The "y" was ment for the package manager... just did not want to pollute more the room with edit because we have IRC.     

> __< r​ucknium:monero.social >__ This is a rule that nodes don't re-org if the proposed alt chain is longer than N blocks     

> __< s​pirobel:kernal.eu >__ Rucknium: there is also this https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4727999 compares cost of attack on eth vs btc     

> __< d​iego:cypherstack.com >__ k     

> __< v​enture:monero.social >__ I'm sorry Rucknium did anyone comment on my short term proposal? just the stratum determinist mining     

> __< v​enture:monero.social >__ *proposal as in mentioned here in the meeting while this agenda short term fix was brought up     

> __< r​ucknium:monero.social >__ I did, but maybe the relationship was not clear.     

> __< tevador >__ Here is a consensus mechanism specifically designed to prevent selfish mining, might be worth reading: https://eprint.iacr.org/2016/916     

> __< v​enture:monero.social >__ anyways, seems not catching on. ok     

> __< d​iego:cypherstack.com >__ We're looking into things, obviously, but I'd like to say something about this whole shebang. PoW and PoS has been debated for years at this point. Yes there's new research, but pretty much all this research is going to come with tradeoffs to the current social contract that many will find unacceptable.     

> __< d​iego:cypherstack.com >__ There's very little "new" in any of our debates or research here.     

> __< r​ucknium:monero.social >__ tevador: I have a newer, better proposal later on the agenda that builds on Fruitchains.     

> __< d​iego:cypherstack.com >__ At some point, somebody is going to have to take lead on something and code it up for discussion. Someone gotta take charge a bit.     

> __< d​iego:cypherstack.com >__ The transition from full PoW, if that is what is decided, is going to be painful, and we will lose people. And where we end on the spectrum from PoW to PoS is honestly kind of irrelevant.     

> __< s​gp_:monero.social >__ I might prefer dns checkpoints to n-block rolling checkpoints, honestly :/ at least those won't cause a chain split among adopted nodes     

> __< d​iego:cypherstack.com >__ Every step along the spectrum has its own trade-offs, with the either end of the spectrum generally requiring the least centralization     

> __< d​iego:cypherstack.com >__ things like DNS checkpoints and other stuff more towards the middle require more centralization     

> __< r​ucknium:monero.social >__ Diego Salazar: I don't know what the literature says, so it's still new to me. And the big-picture articles I shared were released in the last few years. Some of those are "top-down" theorem-building. Different from specific protocols.     

> __< d​iego:cypherstack.com >__ anyways, that's my thoughts. I'm done.     

> __< tevador >__ I just wanted to note that several proposal in #136 were marked as "needing a soft fork". Soft forking requires the majority of the hashrate to start following the new rule, so it can't work against a >50% attacker. It would have to be a hard fork.     

> __< d​iego:cypherstack.com >__ We're trying to go over newest literature now, but there's nothing new under the sun.     

> __< r​ucknium:monero.social >__ More on N-block rolling checkpoint?     

> __< tevador >__ I wouldn't recommend rolling checkpoints due to chain split concerns.     

> __< a​ntilt:we2.ee >__ iirc rolling checkpoints can be gamed (comment in #136)     

> __< r​ucknium:monero.social >__ I think the concern with forcing a netsplit when releasing a N-block alt chain at exactly teh right time could be fixed by deterministic chain tip selection (based on hash) for only that 10-block re-org threshold. Maybe.     

> __< r​ucknium:monero.social >__ **Shorten target block time interval (HF required)**     

> __< r​ucknium:monero.social >__ https://bitcoincashresearch.org/t/lets-talk-about-block-time/471     

> __< r​ucknium:monero.social >__ https://blog.ethereum.org/2015/09/14/on-slow-and-fast-block-times/     

> __< r​ucknium:monero.social >__ > The conclusion of all this is simple: faster block times are good because they provide more granularity of information. In the BFT [Byzantine Fault Tolerant] security models, this granularity ensures that the system can more quickly converge on the "correct" fork over an incorrect fork, and in an economic security model this means that the system can more quickly give notificati<clipped message     

> __< r​ucknium:monero.social >__ on to users of when an acceptable security margin has been reached.     

> __< r​ucknium:monero.social >__ By the way, I put these two in "medium-term", because they require a hard fork, but not much code-writing.     

> __< b​lurt4949:matrix.org >__ tevador: they could also be done with a UASF, a hard fork is not necessarily required even assuming we have <50% honest hashrate     

> __< g​ingeropolous:monero.social >__ the simplicity of "shorten target block time" is impressive.     

> __< s​gp_:monero.social >__ back to 1 minute block times #thankfulfortodaywasright     

> __< g​ingeropolous:monero.social >__ and this could be in addition to whatever else ends up getting implemented.     

> __< s​pirobel:kernal.eu >__ Diego Salazar: agree somewhat. the literature can only get us so far. academics are only mere mortals after all. Rucknium regarding big picture theory building there seem to be not much out there. Building a reading list for this category seems helpful. The only one I came across was this one by Roughgarden (one of the authors of the papers that you mentioned) https://arxiv.org/pd<clipped message>     

> __< s​pirobel:kernal.eu >__ f/2304.14701 after reading it I am a bit skeptical its helpful. We should really do a critical reading of those and not accept them at face value.     

> __< tevador >__ USAF is essentially a hard fork because it can cause a chain split, unlike a mining-majority soft fork.     

> __< r​ucknium:monero.social >__ Agree on critical reading.     

> __< s​gp_:monero.social >__ I'm ultimately for whatever block time makes sense, I don't really care. I just know this won't address selfish mining on its own     

> __< r​ucknium:monero.social >__ ## Long-term     

> __< r​ucknium:monero.social >__ **Require Blocks be Signed by the Miner's Key (HF required)**     

> __< r​ucknium:monero.social >__ https://github.com/monero-project/research-lab/issues/136     

> __< tevador >__ 1 minute block time was abandoned for a reason - high orphan rate.     

> __< r​ucknium:monero.social >__ > With a minimum of 1% of the block reward before penalty or fees in a single transaction signed. As an option 10% of the total block reward in multiple transactions could also be allowed     

> __< a​ntilt:we2.ee >__ stupid question: how would 1min blocktime that hinder Qubic?     

> __< r​ucknium:monero.social >__ ArticMine is writing a formalization of this     

> __< r​ucknium:monero.social >__ Didn't the high orphan rate happen because Fluffy Blocks weren't implemented yet?     

> __< s​gp_:monero.social >__ I'm against this one unless I'm missing something major. It seems to do nothing afaict     

> __< j​effro256:monero.social >__ The orphan rate for 1-minute blocks will probably only get worse under FCMP++ unfortunately because of higher bandwidth and computation requirements for txs     

> __< g​ingeropolous:monero.social >__ but healthy orphans are fine, right?     

> __< v​enture:monero.social >__ it's still wasted hashrate     

> __< j​effro256:monero.social >__ I'm not convinced that a lower block time helps the state converge when one of the participants is purposefully withholding state information like in a selfish mining scheme     

> __< g​ingeropolous:monero.social >__ i wonder if it could be coupled with uncle blocks     

> __< r​ucknium:monero.social >__ AFAIK, uncle blocks make selfish mining worse.     

> __< v​enture:monero.social >__ 😅 oh shit     

> __< r​ucknium:monero.social >__ Check the Selfish Mining Re-examined paper     

> __< r​ucknium:monero.social >__ **Construct RandomX cache by selecting random parts of the blockchain (HF required)**     

> __< r​ucknium:monero.social >__ https://github.com/monero-project/research-lab/issues/98     

> __< o​frnxmr:monero.social >__ i commented there, but this essentially cuts out thr majority of gupax users     

> __< s​gp_:monero.social >__ (gupax defaults to using a remote node fwiw)     

> __< o​frnxmr:monero.social >__ Which is probably only like 15mh.. but is also probably 90% of the vocal minority     

> __< a​ntilt:we2.ee >__ +1 if drop in HR is no concern. Major re-org of network topology     

> __< tevador >__ 15 MH is almost nothing, but it would hurt centralized pools and hashrate rental services hard.     

> __< r​ucknium:monero.social >__ Reachable node will probably be hit with a big increase of their inbound connections.     

> __< g​ingeropolous:monero.social >__ it seems like something we should move towards. hard to see it as a binary switch. maybe there's a transition period where n% of blocks require it ?     

> __< o​frnxmr:monero.social >__ The mh is nothing, but its potentially 1000+ users     

> __< tevador >__ Centralized pools are also thousands of users.     

> __< a​ntilt:we2.ee >__ no way to phaze this in slowly... ?     

> __< o​frnxmr:monero.social >__ thousands of p2pool users*     

> __< s​gp_:monero.social >__ I think this proposal will mostly harm small miners who will no longer be able to mine (in practice) without a node. Yes they're a minority of total network hashrate, but it does substantially deviate from a goal of "anyone can mine". That said, I do see the arguments for, even if I think they are somewhat marginal (large miners still have incentives to use pools, and the costs ar<clipped message>     

> __< s​gp_:monero.social >__ e constant not scaling with hashrate)     

> __< g​ingeropolous:monero.social >__ in qubics case, they would just having to spin up a node doing this, some pool software, and then find a way to get the blockchain data to their workers... really fast?     

> __< o​frnxmr:monero.social >__ a good chunk of p2pool mini are gupax users     

> __< tevador >__ It would be possible to slowly decrease the RandomX epoch from the current 2048 block down to the proposed 64 blocks.     

> __< r​ucknium:monero.social >__ ofrnxmr: Source on that data?     

> __< o​frnxmr:monero.social >__ "i made it up" rucknium     

> __< b​lurt4949:matrix.org >__ Not sure if anyone else sees this is as a serious threat especially given the current pressing Qubic situation, but fwiw this proposal would obviously decrease total hashrate by a lot, making us more vulnerable to coordinated attackers (institutional, nation-state, etc)     

> __< o​frnxmr:monero.social >__ the opposite is likely more true. (almost) all gupax users are on -mini, but not all -mini users are gupax users     

> __< a​ntilt:we2.ee >__ might actually put Qubic (AWS) in an advantage     

> __< s​gp_:monero.social >__ I think this proposal will cause a net decrease in the total hashrate, with most of the drop contained to small miners     

> __< tevador >__ Any PoW change will likely decreased the hashrate temporarily.     

> __< g​ingeropolous:monero.social >__ what would an attacker have to do if we had this protocol     

> __< o​frnxmr:monero.social >__ right. This hurts pools and unattended botnets, but not necessarily qubic, who has 700 nodes with 2tb ram. Can probably afford the bandwidth     

> __< s​gp_:monero.social >__ I think it'll be a net decrease at equilibrium     

> __< g​ingeropolous:monero.social >__ does anyone know? has there been a paper on this?     

> __< o​frnxmr:monero.social >__ So this could, in theory.. lead to qubic (immediately) having a (much) larger %     

> __< g​ingeropolous:monero.social >__ well it depends if they can get the data from a blockchain quick enough right?     

> __< o​frnxmr:monero.social >__ Any pow change at all will knock botnets offline for a while, but not qubic     

> __< b​lurt4949:matrix.org >__ ofrnxmr: I think that is most likely. I think the average Qubic hash/sec is more likely to run a node than the average honest hash/sec     

> __< tevador >__ Probably 80% of the honest hashrate comes from the top 20% largest miners, who can easily afford to run a node and join p2pool. I don't see a reason for a large permanent drop in hashrate. Qubic's distribution is likely very similar.     

> __< r​ucknium:monero.social >__ **Countering Selfish-Mine: Promote orphans to uncles (equal pay) and choose deterministically in stratum) who becomes father (HF required)**     

> __< r​ucknium:monero.social >__ https://libera.monerologs.net/monero-research-lab/20250820#c568556-c568579     

> __< o​frnxmr:monero.social >__ I think 80% of "honest" hashrate is botnets, who would drop off     

> __< s​gp_:monero.social >__ I agree the largest miners will be essentially unaffected     

> __< o​frnxmr:monero.social >__ Again, i dont have a source for my thoughts     

> __< tevador >__ It would be a big win if 80% of the hashrate migrated to p2pool.     

> __< v​enture:monero.social >__ i guess this agenda can be skipped. didn't know uncles make it worse. i checked the paper quickly, not sure that they do make it worse in combination of a join (banded together) mining strategy (stratum)     

> __< v​enture:monero.social >__ with an orphan / uncle and re-org: avg payout would be 0.5.      

> __< v​enture:monero.social >__ either 0.5 + 0.25 (if branch was chosen)     

> __< v​enture:monero.social >__ or 0.25 (if branch was not chosen)     

> __< v​enture:monero.social >__ avg: 0.5     

> __< v​enture:monero.social >__ the point is, it collapses the 2 branches into one as quickly as possible     

> __< v​enture:monero.social >__ *joined     

> __< a​ntilt:we2.ee >__ I doubt, that uncle rewards change the way Qubic operates. Switching miners (~5%) does not seem relevant at large.     

> __< r​ucknium:monero.social >__ **Friction (HF required)**     

> __< r​ucknium:monero.social >__ "Amends fork choice rule to give greater weight to blocks produced by miners that have a history of mining"     

> __< s​gp_:monero.social >__ I think the most realistic outcome is that the largest miners will continue to use pools. It's simpler (and potentially even cost effective) to have the pools deduct the bandwidth costs from payouts for these large miners than the cost for the miners to need their own nodes (storage and local bandwidth costs)     

> __< r​ucknium:monero.social >__ I think gingeropolous  know info about this Friction idea     

> __< g​ingeropolous:monero.social >__ here's the bat bones     

> __< g​ingeropolous:monero.social >__ 100% human generated     

> __< g​ingeropolous:monero.social >__ https://github.com/Gingeropolous/friction/blob/main/batbones.md     

> __< s​gp_:monero.social >__ Wouldn't this encourage people to join the largest pool, to ensure the blocks mined there have the greatest "weight" (friction?)     

> __< g​ingeropolous:monero.social >__ yeah its not anti-pool, its mostly anti selfish mining     

> __< tevador >__ sgp_: I'm not convinced that the costs of running a node are higher than the bandwidth costs for mining at a centralized pool + the pool fee.     

> __< a​ntilt:we2.ee >__ "the secret"... whats that, again ?     

> __< g​ingeropolous:monero.social >__ which i view as the main fulcrum of the current attack     

> __< g​ingeropolous:monero.social >__ but in general, friction doesn't affect honest mining     

> __< r​ucknium:monero.social >__ **Proportional Reward Splitting (HF required)**     

> __< r​ucknium:monero.social >__ Paper claims that Proportional Reward Splitting can defeat a selfish miner that has up to 38% of hashpower     

> __< r​ucknium:monero.social >__ https://arxiv.org/abs/2503.10185     

> __< r​ucknium:monero.social >__ I haven't finished reading this paper, but I like it because it's recent (2025) and actually claims to have computed the Nash equilibrium game theory of the proposed protocol.     

> __< tevador >__ Is this the paper that builds on fruitchains?     

> __< v​tnerd:monero.social >__ most likely, it mentions it in the abstract     

> __< r​ucknium:monero.social >__ I think there could be some downside (the paper states that the "optimal" and "practical" parameter values are different), but I haven't gotten there yet.     

> __< v​tnerd:monero.social >__ er maybe not     

> __< r​ucknium:monero.social >__ tevador: yes     

> __< r​ucknium:monero.social >__ It says FruitChains had some problems. This protocol fixes them.     

> __< a​ntilt:we2.ee >__ tldr; not wort the efford     

> __< r​ucknium:monero.social >__ Might not be worth the effort of coding and testing. Right.     

> __< a​ntilt:we2.ee >__ *h -- it redestributes rewards ok (nice to have) but works for >51% only. Very complex to implement.     

> __< r​ucknium:monero.social >__ But. To compete with this proposal I would prefer novel proposals on selfish mining to try to quantify their benefit.     

> __< r​ucknium:monero.social >__ Works for >51% of miner adoption? This is a consensus change, not opt-in.     

> __< a​ntilt:we2.ee >__ of hash power     

> __< s​pirobel:kernal.eu >__ the paper seems complex and math heavy. the consensus should be as simple as possible so that people can trust it and it stays easy to reason about     

> __< s​pirobel:kernal.eu >__ would the implementation mirror this complexity?     

> __< r​ucknium:monero.social >__ I don't think I like a weak protocol that is easy to reason about instead of a strong protocol that is difficult to reason about.     

> __< r​ucknium:monero.social >__ Anyway, the selfish mining attack is against the Nakamoto "simple" protocol.     

> __< r​ucknium:monero.social >__ The paper has a lot of jargon that is not necessarily needed.     

> __< r​ucknium:monero.social >__ Because it's formal     

> __< a​ntilt:we2.ee >__ may be not so complex to implement, but I dont understand their criticism/weakness of fruitchanes tbh     

> __< s​pirobel:kernal.eu >__ problem with complexity is, it is harder to judge if its actually stronger or not.     

> __< r​ucknium:monero.social >__ If you have a mathematical proof, that's the reasoning.     

> __< r​ucknium:monero.social >__ We are at the last specified sub-item (open floor discussion can continue after).     

> __< r​ucknium:monero.social >__ **Finality Layer (HF required)**     

> __< r​ucknium:monero.social >__ https://github.com/monero-project/research-lab/issues/135     

> __< r​ucknium:monero.social >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/604     

> __< r​ucknium:monero.social >__ kayabanerve: This is the Trailing Finality Layer discussion.     

> __< g​ingeropolous:monero.social >__ is this like if the N-block rolling consensus was conscious? had human input?     

> __< a​ntilt:we2.ee >__ a long term efford, tbs     

> __< v​enture:monero.social >__ not sure about these fruits, and what they abstract. but they do have the concept of uncle-fruits, claiming nash equilibrium because of the reward allocation. so my 2 cents, the existence of uncle blocks alone does not necessarily mean they benefit selfish mine     

> __< a​ntilt:we2.ee >__ yep, iiuc     

> __< a​ntilt:we2.ee >__ also envisioned as a separate binary/p2p net (?)     

> __< r​ucknium:monero.social >__ I am lukewarm (pun not intended) toward this TFL CCS proposal because I think it's a few weeks premature and kayabaNerve obviously has a high opportunity cost of his time.     

> __< r​ucknium:monero.social >__ I say premature because the whole space of countermeasures and alternative proposals has barely had its surface scratched. The high opportunity cost is reflected in the budget of the proposal.     

> __< tevador >__ It introduces PoS, which might be opposed by some people as being against the ethos of Monero.     

> __< v​enture:monero.social >__ TFL question, would a finality layer completely override the longest/heaviest chain rule from the underlying PoW? Because, to me, once finality is required (eg, by exchanges) miners will always jump ship and mine on any branch endorsed by that layer.     

> __< r​ucknium:monero.social >__ I'm not against it. I think more research is good. Just lukewarm on it.     

> __< s​pirobel:kernal.eu >__ i think we should at least reach consensus on which questions we want answered     

> __< tevador >__ IMO, a good way forward would be: (1) Test the DNS checkpointing as an emergency short-term measure. (2) Research a consensus protocol that works with PoW (assuming >50% of honest hashrate) and fixes selfish mining.     

> __< g​ingeropolous:monero.social >__ im not a fan of how it seems to be PoS-like     

> __< a​ntilt:we2.ee >__ yes, we should subdevide the topic. BFT has many many options     

> __< g​ingeropolous:monero.social >__ yeah i think we have 2 issues. 1. selfish mining 2. mining centralization.     

> __< a​ntilt:we2.ee >__ ... and I like recursive elements (including friction :)     

> __< a​ntilt:we2.ee >__ ... like malicious collective detection, in Gasper -- but thats too far away.     

> __< s​pirobel:kernal.eu >__ dns checkpointing as a long term solution seems more centralizing than pos     

> __< tevador >__ I don't think anyone is proposing DNS checkpointing as a long term solution.     

> __< s​pirobel:kernal.eu >__ there could be a benefit to have nodes with a bond that could be slashed beyond consensus     

> __< s​pirobel:kernal.eu >__ we could discuss this outside of the pow-pos paradigm and think about it pragmatically     

> __< s​pirobel:kernal.eu >__ brought this up earlier at agenda point 5: it could help increase the cost for malicious nodes spinning up tor hidden services     

> __< s​pirobel:kernal.eu >__ blocking based on ips is a form of centralization as well     

> __< s​pirobel:kernal.eu >__ anyway its 4am here i am running out of steam: wrote down a comment on this earlier: https://github.com/monero-project/meta/issues/1256#issuecomment-3207233765     

> __< a​ntilt:we2.ee >__ maybe we could have a work group instead a book ??     

> __< s​pirobel:kernal.eu >__ i also like what jberman said about no fees + rewards. Its similar to what I said earlier that pow can be seen as pos with negative staking rewards if people are willing to defend the network by mining at a loss     

> __< r​ucknium:monero.social >__ Feel free to discuss any idea now, including those not on the specified list.     

> __< v​tnerd:monero.social >__ the few papers I looked at were junk, lots of half attempts to fix selfishin mining     

> __< r​ucknium:monero.social >__ Thanks for wading through the junk. Can you share a few so we know to avoid them?     

> __< s​pirobel:kernal.eu >__ flip flop: good idea, only question is how do we make sure it stays structured? can we agree on the core questions that should be answered?     

> __< v​tnerd:monero.social >__ google ai recommended this: https://link.springer.com/article/10.1007/s10207-024-00857-5     

> __< v​tnerd:monero.social >__ but I didnt like it. so much for ai     

> __< v​tnerd:monero.social >__ I spent way too much time looking at it, their algorithm wasn’t quite clear imo which threw everything off     

> __< a​ntilt:we2.ee >__ 1. DIff. BFT <> Pos 2. Design choices based on historical imlementations     

> __< v​tnerd:monero.social >__ they also assumed that the selfishing miner would have an older timestamp which is rubbish because you would just set to the max allowed by protocol     

> __< v​tnerd:monero.social >__ its possible that I missed something, but I wasn’t getting it. not sure if I can share it because its all begin paywall     

> __< r​ucknium:monero.social >__ I skimmed the abstract on this one I think. I remember thinking that the tone was informal. Maybe that's an arrogant thought, but it stopped me from going further.     

> __< v​tnerd:monero.social >__ *behind     

> __< v​tnerd:monero.social >__ well their own algorithm has     

> __< v​tnerd:monero.social >__ NumOfBrBlocks <- 0     

> __< v​tnerd:monero.social >__ if (NumOfNrBlocks = 1) then     

> __< s​pirobel:kernal.eu >__ Rucknium:  more formal == better at hiding the skeletons in the closet 💀     

> __< j​effro256:monero.social >__ This is especially true since we have a block difficulty calculation lag, so setting the timestamp ahead doesn't make our mining harder. If they set it too far in the future (>2 hours in Monero) then it will be rejected, but they can wait a certain amount of time depending on how far ahead they are of the honest chain     

> __< v​enture:monero.social >__ "It’s very unfair for honest miners, and it’s a big problem that needs to be stopped." from the abstract... yeah quite informal to put it nicely 😅     

> __< v​tnerd:monero.social >__ like what? I think they meant to say NumOfBrBlocks published at once or something but even with that assumption I dont think it worked     

> __< v​tnerd:monero.social >__ sorry there was typo in that algorithm, they indeed set a value to 0 and then do an if on that value with stating what it really should be     

> __< r​ucknium:monero.social >__ spirobel: I don't disagree with you on that. You need a closet detective for that.     

> __< v​tnerd:monero.social >__ I wish I could copy+paste a portion from this pdf but I cant sorry (wont let me copy for whatever reason)     

> __< v​tnerd:monero.social >__ anyway, hopefully I didn’t misread it and it was a good paper in the end. May go over it again since I paid for it and all. Never trust AI lol     

> __< j​effro256:monero.social >__ Oops, sorry, falsely setting the timestamp in the future would make the mining *easier* with real-time targeting, but the point still stands: faking timestamps is still possible and doesn't hurt a selfish miner if done correctly.     

> __< v​tnerd:monero.social >__ yes, an excerpt from the paper:     

> __< v​tnerd:monero.social >__ "If miners broadcasted more than one block in the same time interval, one block should be selected as the valid block. Selfish miners keep their blocks secret for some period of time. Therefore, selfish miner’s block’s timestamp is old.”     

> __< v​tnerd:monero.social >__ like what? how can you assume that? not all papers are the same     

> __< r​ucknium:monero.social >__ We can end the meeting here. Feel free to continue discussing, as I know you will. Thanks everyone.     

> __< s​pirobel:kernal.eu >__ thanks     

> __< v​enture:monero.social >__ bye     

> __< a​ntilt:we2.ee >__ bye     

> __< s​gp_:monero.social >__ thank you     

> __< s​pirobel:kernal.eu >__ vtnerd: i heard about this new ai project called aigarth that mines ai on cpus maybe it can solve that 😆     

> __< s​pirobel:kernal.eu >__ the marketing material says something about growing the ai in a garden     

> __< v​tnerd:monero.social >__ the other interesting thing about all of this is that not all tokens in the available supply were generated for ai computation - some were used to selfish mine xmr, etc.     

> __< v​tnerd:monero.social >__ just interesting from an optics standpoint     

> __< v​tnerd:monero.social >__ this is assuming the ai computation is genuine also     

> __< s​pirobel:kernal.eu >__ as genuine as an ai garden could be     

> __< s​pirobel:kernal.eu >__ if only jensen new. he could have invested in cpus instead of gpus     

> __< s​pirobel:kernal.eu >__ if only jensen knew. he could have invested in cpus instead of gpus     

> __< k​ayabanerve:matrix.org >__ Apologies for missing the MRL meeting. I've been working on migrating monero-serai to monero-oxide and upstreaming the FCMP++ libraries (which had included >13,000 lines forked from Serai's cryptography, but doesn't anymore).     

> __< k​ayabanerve:matrix.org >__ Rucknium: Heard you're lukewarm as we haven't scratched the surface on proposals. My CCS would scratch the surface on a finality layer :p     

> __< k​ayabanerve:matrix.org >__ (I understand and respect Rucknium's point)     

> __< b​awdyanarchist:matrix.org >__ Not sure if it was mentioned, but here's the implementation of Eth Classic Modified Exponential Subjective Scoring (MESS). Basically depth penalty based on the time differential between the last common ancestor, and the new (reorg'd) head.     

> __< b​awdyanarchist:matrix.org >__ https://ecips.ethereumclassic.org/ECIPs/ecip-1100     



# Action History
- Created by: Rucknium | 2025-08-19T21:15:57+00:00
- Closed at: 2025-08-28T20:54:10+00:00
