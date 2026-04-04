---
title: Monero Research Lab Meeting - Wed 20 March 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/981
author: Rucknium
assignees: []
labels: []
created_at: '2024-03-19T20:53:08+00:00'
updated_at: '2024-04-02T15:01:58+00:00'
type: issue
status: closed
closed_at: '2024-03-27T22:52:35+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Possible spam incident](https://bitinfocharts.com/comparison/monero-transactions.html#3m)

4. @jeffro256 [ I think we can improve how the nodes handle alternative blocks in a way that might naturally reduce the number of reorgs on the network.](https://github.com/monero-project/meta/issues/966#issuecomment-1936243293)

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#978 

# Discussion History
## Rucknium | 2024-03-20T23:17:34+00:00
> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/981     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< s​gp_:monero.social >__ Hello     

> __< v​tnerd:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Working on analyzing the possible spam black marble flood. I have a PDF draft, but it's very rough. I have the draft plots ready to share: https://github.com/Rucknium/misc-research/tree/main/Monero-Black-Marble-Flood/pdf/images     

> __< isthmus >__ Hiya. Intermittently here, but multitasking     

> __< c​haser:monero.social >__ "work" would be an overstatement, but I collected all the measures I can think of that can be effective against a black marble flood: https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ chaser: Thanks a lot :)     

> __< rbrunner >__ Good text, helpful     

> __< v​tnerd:monero.social >__ I worked a little on frontend for lws, but stopped after I discovered woodser was already on it. Otherwise have been working on "remote" scanning for lws. A little more confident that it will be possible without destroying the code, but still a possibility that I punt on the feature     

> __< r​ucknium:monero.social >__ 3) Discussion. The large tx volume is still happening. A little lower now, but still filling almost all blocks to the 300 kB minimum limit.     

> __< r​ucknium:monero.social >__ I put some plots here: https://github.com/Rucknium/misc-research/tree/main/Monero-Black-Marble-Flood/pdf/images  The most important ones are empirical-effective-ring-size.png, spam-share-outputs.png, and projected-effective-ring-size-non-log.png     

> __< r​ucknium:monero.social >__ If the tx volume is a black marble flood attempt, an effective ring size low enough to allow chain reaction analysis to deterministically figure out the real spend would be the greatest threat. Effective ring size is about 5.5 now. Less than 1% of rings would be drawing black marbles for all 15 decoys.     

> __< rbrunner >__ "projected-effective-ring-size-non-log.png" is a bit depressing, if I understand that correctly: With ringsize 25 the adversary only needs to double blocksize to about 600, and it's again down to 5.5     

> __< r​ucknium:monero.social >__ Doing actual chain reaction simulation would take time. Chervinski et al., (2021) did a chain reaction simulation. Looking at their parameters, I don't think it's a problem now with the suspected spam volume.     

> __< r​ucknium:monero.social >__ Yes. ArticMine suggested raising ring size to 40.     

> __< s​gp_:monero.social >__ ArticMine should have suggested bumping the min fee 4x :p     

> __< azunda >__ bumping fee is not smart.     

> __< c​haser:monero.social >__ he did actually, but only the relay fee. I think if fees are modified, it makes sense to do it on the protocol level.     

> __< s​gp_:monero.social >__ Raising the ringsize with the current technology is relatively costly. Arguably more harmful than bumping the minimum fee imo     

> __< rbrunner >__ Looking at the list from chaser, I don't think we have any immediate "smart" countermeasures     

> __< r​ucknium:monero.social >__ The budget of the suspected adversary is unknown. There was a 24 hour burst of 1in/2out 320 nanonero/byte txs that was either the spammer or a service that paid a lot temporarily to get fast confirmations. The rest of the suspected spam pays fees much lower (20 nanoneros/byte)     

> __< s​gp_:monero.social >__ a spammer with a truly unlimited budget will always consume 100% of new available block space, making the attach unavoidable. So that's what we're up against     

> __< s​gp_:monero.social >__ a spammer with a truly unlimited budget will always consume 100% of new available block space, making the attack unavoidable. So that's what we're up against     

> __< r​ucknium:monero.social >__ 320 nanoneros/byte is the 3rd tier of fees. The GUI/CLI only increases fees from the 1st to 2nd tier if the txpool is congested.     

> __< r​ucknium:monero.social >__ Can anyone confirm that increasing the ring size would not increase the pruned node storage space very much?     

> __< s​gp_:monero.social >__ The only way the monero network gets around this is assuming that the attacker doesn't have unlimited resources (since then we have to assume it's a lost cause), and we make it significantly more expensive for them     

> __< rbrunner >__ Don't know enough details about pruning to be sure. But for sure the pruned blockchain growth would also accelerate     

> __< c​haser:monero.social >__ no attacker has unlimited budget. we don't know their budget until they stop. the cost requirement is like a fence, what we can do is to raise it in some or multiple ways, which will raise our general defense, and may make an attacker retreat/not raise their volume     

> __< r​ucknium:monero.social >__ I could project the expenditure to achieve some effective ring size. Vary the fee and the nominal ring size.     

> __< s​gp_:monero.social >__ the cost of raising fees is only passed onto the senders. Higher fees also subsidize mining, making mining attacks more expensive as well, assuming no material change to organic demand     

> __< s​gp_:monero.social >__ It might be worth trying to guess the realistic amount an attacker would be willing to spend, and trying to model around that. There will always be some implied number there to target     

> __< r​ucknium:monero.social >__ Raising fees could reduce the volume of txs sent by real users. That would increase the adversary's share of outputs, ceteris paribus.     

> __< s​gp_:monero.social >__ yes, but for them to maintain the same ratio of outputs that we're worried about, the math works in our favor     

> __< s​gp_:monero.social >__ yay ring signatures :)     

> __< s​gp_:monero.social >__ for every 1 real tx cost paid by a user, the attacker needs to pay what, 10x that? for a concerning ratio     

> __< rbrunner >__ That's an interesting way to look at it     

> __< a​rticmine:monero.social >__ Raising the  ring size is the best deterrence against a black marble attack     

> __< r​ucknium:monero.social >__ Real users and the suspected adversary do not have the same willingness to pay per tx.     

> __< s​gp_:monero.social >__ Let me put it this way: if making new transactions costs effectively nothing, then even ringsize 100 wouldn't matter, since there's no cost to spam transactions     

> __< s​gp_:monero.social >__ I'm not saying ringsize is truly irrelevant, it's just that fees matter a lot more     

> __< azunda >__ attacker will need to spend exponentially more with higher ringsize ?     

> __< r​ucknium:monero.social >__ IMHO raising the ring size to 40 would be great, given what I know at this point in time.     

> __< a​rticmine:monero.social >__ Of course     

> __< a​rticmine:monero.social >__ Do you mean because of the impact on the output distribution     

> __< r​ucknium:monero.social >__ projected-effective-ring-size-non-log.png tries to accurately project block weight as ring size increases by the way.     

> __< rbrunner >__ Interesting that so far no attempt to drive the effective ringsize lower than about 5, but 5 is still a quite good protection. Is that even useful what they do here, as a black marble attack?     

> __< rbrunner >__ I find this quite a bit puzzling     

> __< s​gp_:monero.social >__ I'm not going to stand against a ringsize increase. You all should know I've advocated in favor of all the previous ones. But, it would be silly imho to bump the ringsize but do nothing about fees.     

> __< s​gp_:monero.social >__ Increasing the ringsize has a permanent network cost. Increasing fees has no direct network cost.     

> __< azunda >__ let's not rule out that it is organic      

> __< r​ucknium:monero.social >__ ArticMine: I mean because of the estimates that I've done in https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/projected-effective-ring-size-non-log.png . If nominal ring size is 40, there would still be a healthy effective ring size if the suspected spammer is filling 300 kB blocks. Actually it would be larger than current nominal ring size (16)     

> __< azunda >__ sgp - it has social effect, people want to use the cheapest means of transacting      

> __< s​gp_:monero.social >__ Monero should not compete to be the cheapest network. Monero won't win that fight :p It needs to be a very private option for a totally reasonable cost     

> __< azunda >__ yes but people care more about money than privacy, that's why low fees are more attractive with the added "privacy" bonus      

> __< rbrunner >__ I think it might be interesting to brainstorm a bit more about possible forms of "PoW before submitting a transaction"     

> __< c​haser:monero.social >__ it doesn't matter if it's organic or not, because we can't know, and we can't afford to think it's the optimistic scenario. and even if it is organic, this event is an invitation to any adversary in the sidelines to come and attack, especially if they see that there is no pushback.     

> __< isthmus >__ I prefer raising the ring size as the most robust way to address this. However I would not object to fee adjustments as part of the response     

> __< rbrunner >__ Maybe we can connect the amount of PoW needed with some network parameters / network statistics, so normally it's negligible     

> __< dukenukem >__ Raise ring size and slightly adjust fees. Ez.     

> __< isthmus >__ For txn pow with existing format could just reroll randomizer until some field is sufficiently low/high :- P     

> __< c​haser:monero.social >__ Monero is a privacycoin, not a "cheap transactions with privacy bonuses" coin.     

> __< r​ucknium:monero.social >__ There is a technical statistical point to keep in mind. Mean effective ring size = 5.5 does not mean that random guessing success is 1/5.5. Effective ring size is a random variable since decoys are selected randomly. 1/x is a strictly convex fucntion. By Jensen's inequality, E[1/x] > 1/[E[x]. The current probability of correctly guessing the real spend is about 25%. Check empirica<clipped message     

> __< r​ucknium:monero.social >__ l-guessing-probability.png     

> __< a​js_:matrix.org >__ Liam Eagen to give talk on Bulletproofs++ at MoneroKon     

> __< s​gp_:monero.social >__ I strongly suggest you hike the fees a higher multiple than the ringsize increase     

> __< s​gp_:monero.social >__ If the attacker continues to consume the majority of the block space, then they will pay the majority of the fee increase     

> __< r​ucknium:monero.social >__ I am not opposed to a reasonable increase in fees, too.     

> __< azunda >__ maybe that's the point of the attack ? so we increase the fees ?     

> __< s​gp_:monero.social >__ unfortunately the motivation doesn't really matter     

> __< azunda >__ as pointed out, it has no effect on privacy     

> __< s​gp_:monero.social >__ there is absolutely a privacy risk and rucknium demonstrated     

> __< a​js_:matrix.org >__ Ariel Gabizon will also give a talk on Circle STARKs https://eprint.iacr.org/2024/278     

> __< s​gp_:monero.social >__ there is absolutely a privacy risk as rucknium demonstrated     

> __< c​haser:monero.social >__ these charts are very good, thank you!     

> __< r​ucknium:monero.social >__ I said in Saturday's #monero-community:monero.social meeting that I am planning to write a statistical research CCS to analyze the black marble flooding and other Monero research tasks. Input is appreciated :) . nioCat suggested that I work with ArticMine to model some scenarios.     

> __< rbrunner >__ If the current amount of spam does not change, it won't get much worse than it already is, right?     

> __< a​js_:matrix.org >__ And Stefanos Chaliasos on Security Vulnerabilities in SNARKs     

> __< s​gp_:monero.social >__ I understand that people have an emotional attachment to small fees. However, it really is important to consider the consequences of having a super low cost of spam. A low cost of spam makes enforcing privacy protections significantly more expensive (through a much larger, less efficient required ringsize)     

> __< r​ucknium:monero.social >__ Yeah, still working on OSPEAD in parallel, but the black marble is more urgent since OSPEAD adjustments probably have to happen at a hard fork to be safest.     

> __< a​rticmine:monero.social >__ I disagree. A critical part of privacy is to increase the ham transactions. This means increasing the anonymity set     

> __< b​oog900:monero.social >__ I don't know if this has already been mentioned but although the effective ring size is ~5 wont these decoys that are left be more likely to be older i.e the ones less likely to be the real spends     

> __< s​gp_:monero.social >__ I would agree with you ArticMine if we already had FCMP     

> __< r​ucknium:monero.social >__ r​brunner: The effect on privacy is not going to become severe quickly if the current tx volume stays the same. It will get worse gradually     

> __< a​rticmine:monero.social >__ Think of drowning the blockchain Surveillance companies in ETH, which is starting to happen     

> __< a​rticmine:monero.social >__ Yes I agree     

> __< rbrunner >__ drowning in ETH? I don't understand     

> __< s​gp_:monero.social >__ boog900: Yes, this is true for certain investigation scenarios. It makes out of band information over these periods more valuable, if that makes sense     

> __< s​gp_:monero.social >__ I don't know if I can explain it simply here     

> __< r​ucknium:monero.social >__ boog900: Yes, but https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/projected-effective-ring-size-non-log.png projects what happens if the spam continues for a very long time at current levels. It doesn't get much worse than effective ring size 5.5 when blocks have 300 kB total weight. Effective ring size about 4.5 I think.     

> __< c​haser:monero.social >__ unfortunately, all these will be possible only with a fork     

> __< a​rticmine:monero.social >__ FCMP is the goal. My interim solution is to all for a tx size of around at least 5000 - 6000 which is the estimated size for FCMP     

> __< a​rticmine:monero.social >__ So we have the scaling in place for when FCMP come on line     

> __< s​gp_:monero.social >__ Why 4x the cost of transactions to be stored permanently if we could instead 4x the cost of fees paid by the attacker for the same privacy improvement     

> __< rbrunner >__ Because that improvement is not assured?     

> __< azunda >__ not if they have large budget      

> __< r​ucknium:monero.social >__ chaser: Yes, but the hard fork node parameters need to be ready before the wallet parameters need to be ready. Ring size is node. Decoy selection algorithm with OSPEAD is wallet.     

> __< rbrunner >__ They might be ready to pay 4x     

> __< s​gp_:monero.social >__ I think we need a sanity check. Are there really reasonable use-cases where a Monero transaction *should* cost less than, say, $0.10? What demand does that actually turn away     

> __< azunda >__ increasing fees may even decrease privacy as people will use lower than default fees and just wait longer     

> __< r​ucknium:monero.social >__ They have have paid 16x when we saw the 320 nanoneros/byte burst.     

> __< a​rticmine:monero.social >__ A 4x increase in fees below the minimum penalty free blocksize is part of my proposal. So both     

> __< r​ucknium:monero.social >__ There are a lot of people in the world who would not transact at $0.10 per tx     

> __< rbrunner >__ Well, maybe people would even grudgingly put up with USD 1 as a fee. Does not mean that makes sense as a course of action     

> __< s​gp_:monero.social >__ currently the cost is $0.004 per tx, right?     

> __< a​rticmine:monero.social >__ I agree     

> __< s​gp_:monero.social >__ a 4x proposal would make the per tx fee $0.016. Which would cost the attacker how much in USD terms per day Rucknium? Apologies if you don't have the # of txs they make handy     

> __< r​ucknium:monero.social >__ We will need 3D images :D     

> __< r​ucknium:monero.social >__ I will do some more projections on fees, ring size, and privacy impact.     

> __< c​haser:monero.social >__ ~$2400     

> __< r​ucknium:monero.social >__ I see about 3 XMR per day spent by the suspected spam now.     

> __< rbrunner >__ And that's why "let's rise fees" is such a slippery sloppy: USD 2400 is still almost nothing for certain adversiaral "use cases"     

> __< c​haser:monero.social >__ assuming same tx volume as during peak     

> __< s​gp_:monero.social >__ so about 98k spam tx/day?     

> __< a​rticmine:monero.social >__ ....  and combining this with ring 40 we have an additional ~2.5x     

> __< plowsof >__ and if monero drops 80% in usd price .... or increase to the same as btc     

> __< s​gp_:monero.social >__ sadly there's always some implicit price assumption in these calculations, and we can't predict the future. Yay hard forks (or at least soft forks) :p     

> __< a​rticmine:monero.social >__ You mean all on chain like BTC or staying decentralized. There is a big difference here when considering fees and spam attacks     

> __< s​gp_:monero.social >__ a 4x to fees will bring their cost to roughly $46k/mo, which is still low     

> __< r​ucknium:monero.social >__ IMHO, ways to link fees to the purchasing power of XMR should be researched. Does not mean a formal oracle.     

> __< a​rticmine:monero.social >__ The question here is settlement on chain or on a centralized ledger     

> __< rbrunner >__ Nice idea, but raises the complexity of the system yet again. Already now we may have the most complex fee algorithm of them all     

> __< r​ucknium:monero.social >__ For example, fees could be linked to network hashpower. Since aggregate mining revenue is 0.6 XMR per block and hashpower is proportional to revenue (mostly), maybe that could help.     

> __< s​gp_:monero.social >__ what centralized ledger? monero was already delisted everywhere! /s, kinda     

> __< dukenukem >__ articmine is your proposal documented somewhere, or just in chats thus far?     

> __< a​rticmine:monero.social >__ I am working on putting this together with documentation     

> __< r​ucknium:monero.social >__ The BTC fees are linked to BTC purchasing power by demand and completely inelastic block space supply. It's not a model to follow exactly, but it has a link there.     

> __< c​haser:monero.social >__ I agree that we shouldn't be *too* attached to measuring these costs in dollars. markets are fickle. what we can know is that higher attack costs raise the probabilistic security.     

> __< s​gp_:monero.social >__ You need to be able to mitigate the spam risk by causing actual USD equivalent costs to a potential attacker, that's what it comes down to     

> __< c​haser:monero.social >__ yes, I know it's inevitable, as you said     

> __< a​rticmine:monero.social >__ You can link to USD cost if one assumes no settlement on centralized ledgers. Then the equation of exchange predicts a linear relationship between blocksize and price over time assuming a constant velocity     

> __< s​gp_:monero.social >__ clearly this attack proves there's no given relationship between blocksize and price     

> __< a​rticmine:monero.social >__ M is constant, assuming V is constant the PQ is constant     

> __< azunda >__ add captcha before sending tx /s :D     

> __< a​rticmine:monero.social >__ Most of the recent growth in transactions rates have been below the penalty minimum     

> __< a​rticmine:monero.social >__ With no penalty. pricing     

> __< c​haser:monero.social >__ how do you all feel about the resource requirement increase that a larger ring size would impose? can Seraphis/Seraphis+FCMP justify pre-introducing these requirements?     

> __< s​gp_:monero.social >__ imo, no, not really. But it an important consideration if we consider the other costs reasonable for their advantages     

> __< a​rticmine:monero.social >__ Graphics verification is required in my opinion for the current and subsequent proofs     

> __< r​ucknium:monero.social >__ IMHO, node performance should be benchmarked if ring size would increase to 40. It has to pull lots of data from the database when there are a lot more outputs referenced per ring.,     

> __< a​rticmine:monero.social >__ We have to take advantage of parallel processing on CPU and GPU     

> __< s​gp_:monero.social >__ yes but that takes time, resources, testing, etc. bumping the fee does not take effort and comes with no network costs     

> __< s​gp_:monero.social >__ if the network fee was raised to $0.10, the attacker would be spending $300k per month. Just to give you an idea of how much the fee matters for these mitigations     

> __< s​gp_:monero.social >__ versus today's $11k     

> __< a​rticmine:monero.social >__ Not necessarily if the ham drops down by a factor of 10     

> __< a​rticmine:monero.social >__ It is a band aid, not address the issue     

> __< c​haser:monero.social >__ do you approach it as "delay that bump as much as possible, hopefully hardware and uplink will grow by then"?     

> __< s​gp_:monero.social >__ chaser: sure, that's part of this. Performance improves over time. Further, FCMP benefits are far greater than a moderate ringsize increases. We get a lot more benefit for the same cost     

> __< a​rticmine:monero.social >__ Uplink is not an issue, and hardware is heavily underutilized with little or no parallel processing     

> __< s​gp_:monero.social >__ the cake nodes are already having major issues handling rpc connections fwiw. That can be improved, but not in an immediate fashion     

> __< a​rticmine:monero.social >__ Take the Monero Nodo for example. These devices have a very personal graphics processor that literally sits idle     

> __< a​rticmine:monero.social >__ They could not take advantage of parallel processing     

> __< s​gp_:monero.social >__ no, it's the speed of the monerod locks (and related) that's the issue. The whole blockchain currently needs to be stored in ram     

> __< c​haser:monero.social >__ yes, FMCP is the silver bullet, the cost is that we can't have it at least for over a year, probably more     

> __< a​rticmine:monero.social >__ We have to deal with the cause instead of just focusing on the symptoms     

> __< r​ucknium:monero.social >__ Doesn't the RPC performance have little to do with ring size?     

> __< hyc >__ the monero blockchain does not reside in RAM     

> __< s​gp_:monero.social >__ larger transactions will slow down all connections, read/write, etc     

> __< a​rticmine:monero.social >__ Monero needs to be run on SSD     

> __< a​rticmine:monero.social >__ Not HDD     

> __< s​gp_:monero.social >__ it is an ssd :p     

> __< s​gp_:monero.social >__ nvme     

> __< s​gp_:monero.social >__ cake nodes already need ram cache to keep up     

> __< hyc >__ monerod locking is the biggest problem there     

> __< s​gp_:monero.social >__ absolutely     

> __< s​gp_:monero.social >__ and again, these things can be solved, but not with a snap of our fingers     

> __< s​gp_:monero.social >__ _unlike the minimum fee_     

> __< a​rticmine:monero.social >__ Why is it locking     

> __< azunda >__ 4x will do nothing to a professional adversary      

> __< s​gp_:monero.social >__ that's how monerod is written     

> __< r​ucknium:monero.social >__ If there was something like a bitcoin electrum server for Monero, maybe you would not have conflicts: https://blog.keys.casa/electrum-server-performance-report-2022/     

> __< hyc >__ because back in the mists of time, when monerod's blockchain was entirely RAM resident, you needed fine-grained locking to be able to use it safely     

> __< hyc >__ with LMDB transactions you don't really need that any more, but it's a major rewrite to change the interaction style     

> __< a​rticmine:monero.social >__ So is this a database issue?     

> __< hyc >__ no, the database is lock-free.     

> __< hyc >__ it is an interface to the database issue     

> __< s​gp_:monero.social >__ cake is bottlenecked by the lock implementation currently, yes     

> __< a​rticmine:monero.social >__ So Monero needs to be optimized     

> __< a​rticmine:monero.social >__ Monerod     

> __< hyc >__ yes     

> __< s​gp_:monero.social >__ which they can design around, but that will take months of testing or for a completely fresh rewrite     

> __< hyc >__ the whole blockchain_db pile of code is fuggly     

> __< hyc >__ but it was a shim layer between the memory-only blockchain and the DB-oriented one, so it is heavily compromised in many ways     

> __< s​gp_:monero.social >__ I agree with articmine that this stuff can be optimized, at that it's good to take advantage of the performance that we have. But, I also think Monero should have much higher fees to discourage attacks like this, and yes, even micropayments     

> __< azunda >__ *even micropayments - step back in adoption ?     

> __< azunda >__ and how much of increase would be enough ? because i don't believe 4x will do anything to an adversary like this      

> __< r​ucknium:monero.social >__ I will draw some budget lines and indifference curves :D     

> __< s​gp_:monero.social >__ thanks rucknium, these are always very useful to use in discussions like these     

> __< g​fdshygti53:monero.social >__ 10 cents is still reasonable territory imo.     

> __< azunda >__ 10 cents - if price stays at course     

> __< r​ucknium:monero.social >__ sgp_: I can't tell if you're serious or not 😁     

> __< r​ucknium:monero.social >__ I will try to figure out a way to compare these things     

> __< azunda >__ if we make changes to the fees and suddently price increases 10x which would not be a sci-fi event - it would grow to $1 USD per tx ?     

> __< s​gp_:monero.social >__ I know you will :)     

> __< a​rticmine:monero.social >__ Fees impact both ham and spam. To put it bluntly a crude tool. Furthermore imposing an artificially high node relay fee can cause miners to accept transactions directly. This can be a privacy and decentralizion nightmare     

> __< s​gp_:monero.social >__ soft fork or hard fork, just like we're discussing now. Unfortunately, that's the way it'll have to be to protect privacy before FCMP     

> __< hyc >__ there must be a better tool to deter spam. like a PoW required before submitting a txn     

> __< a​rticmine:monero.social >__ Also if the ham falls by 10x then we are effectively back at 0.01 USD from a spam cost perspective     

> __< s​gp_:monero.social >__ yup, and hooray, we would need to adjust again. I don't see another way around it, unless we find some pow thing promising I guess     

> __< azunda >__ seems that PoW until FMCP is the way ?     

> __< a​rticmine:monero.social >__ PoW to submit is even worse. For starters it discriminates against most of the developing world     

> __< s​gp_:monero.social >__ new plan: everyone needs to have an account at the monero kyc blockchain to send transactions     

> __< hyc >__ I suppose it's all the same thing, adding a cost to making txns, whether in monetary fees or in resource costs     

> __< s​gp_:monero.social >__ :p     

> __< r​ucknium:monero.social >__ PoW spam prevention didn't really work for Nano. They got spammed anyway and had to change their model.     

> __< s​gp_:monero.social >__ arguably monero has pow as an option already: mine, get xmr, use that to pay fees :p     

> __< a​rticmine:monero.social >__ They are mostly in the tropics, while the spammer can launch the attack from a cold place     

> __< a​rticmine:monero.social >__ Call it the ArticMine attack     

> __< hyc >__ we need a surge pricing model that takes network topography into account     

> __< azunda >__ to think of it, if adversary can spend 3 XMR per day today, he can surely afford PoW attack      

> __< s​gp_:monero.social >__ yup, and higher fees will also make a PoW attack more expensive     

> __< hyc >__ txns from low volume networks get lower fees     

> __< azunda >__ yeah make the fee model so complicated they run away just from seeing it :D     

> __< c​haser:monero.social >__ I'm sympathetic to that. or maybe a multi-faceted approach that distributes the "pain": moderate txPoW, moderate ring size increase, moderate minimum free increase, and modifying the median parmeters as Artic outlined.     

> __< c​haser:monero.social >__ how do you mean taking network topo into account?     

> __< hyc >__ we can't really do it, since we have dandelion / tor / i2p to anonymize txn origin     

> __< a​rticmine:monero.social >__ I mean instead of PoW to submit consider an XMR micro burn to submit. At least it is fair to those in the tropics     

> __< hyc >__ assuming none of those existed, we could see when large volumes are coming from clustered network addressese, like all coming from OVH, or Linode, or AWS     

> __< c​haser:monero.social >__ that would be a fair trade-off, but a horrible UX. people shouldn't have to understand this choice and make a decision when they transact     

> __< a​rticmine:monero.social >__ It exposes the reality. I do agree it is a horrible UX     

> __< c​haser:monero.social >__ I see. I think taking factors external to the blockchain is a very slippery ground.     

> __< azunda >__ attacker would just proxify      

> __< rbrunner >__ I still hope somebody will give submit PoW a bit more thoughts. Over the years we must have spent many person months analysing rings, but almost nothing yet where we could go with that     

> __< azunda >__ or use a botnet     

> __< hyc >__ sure but that slows them down     

> __< s​gp_:monero.social >__ it would kill accountless public nodes fwiw     

> __< rbrunner >__ And "It did not work for Nano". Yeah, maybe, but we can do better sometimes. See our "Your can't beat ASICs" breakthrough with RandomX     

> __< a​rticmine:monero.social >__ Still I have seen nothing better than a ring size increase combined with a 4x increase in the minimum node relay fee below the minimum penalty free blocksize     

> __< s​gp_:monero.social >__ What if we did >4x min fee increase     

> __< hyc >__ realistically - how do these fees compare to a credit card txn fee?     

> __< hyc >__ at some point you just have to acknowledge that there is a cost to a well maintained network     

> __< s​gp_:monero.social >__ with 4x increase and today's prices, that's $46k/mo in fees     

> __< r​ucknium:monero.social >__ By the way, last meeting I said effective ring size decreases with increased spam in an exponential decay. It is actually hyperbolic decay. The plots look similar.     

> __< rbrunner >__ I don't want to be "only 20% as bad as credit card" for all the hoops you have to jump through with a cryptocurrency     

> __< s​gp_:monero.social >__ current monero fee per tx starts at $0.0039, or 100x cheaper than a credit card min fee     

> __< rbrunner >__ I react to the thought experiments "What if the fee is 10 US cents"     

> __< s​gp_:monero.social >__ the US Fed is proposing a cut of the debit card fees to 14.4 cents per transaction     

> __< a​rticmine:monero.social >__ It is a partial solution, which can be implemented without a hard fork     

> __< rbrunner >__ I really don't want to take any of that as a yardstick. "Look how much worse credit cards still are". Yikes.     

> __< a​rticmine:monero.social >__ Just do a fee modification     

> __< s​gp_:monero.social >__ I think it's a reasonable upper bound to consider, even if the ideal is much less than that if there were no spammers     

> __< a​rticmine:monero.social >__ Credit card fees are a real mess. Even worse when hidden exchange rate surcharges are factored in     

> __< azunda >__ what if the "attack" keeps on going after increasing the fee x4 ?     

> __< a​rticmine:monero.social >__ Certainly not what I would use as a standard     

> __< azunda >__ at what point should we consider it organic ? after fee  is increased to 10$ usd ?     

> __< s​gp_:monero.social >__ does anyone oppose to $0.10 fee as a sanity check?     

> __< sech1 >__ Just look at an all-time chart and stop telling it's organic: https://bitinfocharts.com/comparison/monero-transactions.html#alltime     

> __< c​haser:monero.social >__ doing it without a hard fork could have minimal effects. people may just not update to the point release. even with a hard fork, if it's only the relay fee, an attacker can coordinate with a pool (send them their tx's). if there is a fee increase, it should happen on the protocol-level.     

> __< s​gp_:monero.social >__ not as an actual proposal, but "this is roughly in the 'feels correct' territory"     

> __< r​ucknium:monero.social >__ $0.10 fee/tx is too high IMHO     

> __< sech1 >__ No one anywhere is posting on "how to download a wallet", so we don't have many new users now     

> __< s​gp_:monero.social >__ Rucknium why do you feel it is too high?     

> __< rbrunner >__ If we have to raise fees to 0.10 US cents per transactions to keep a reasonable level of privacy, IHMO we have simply lost.     

> __< a​rticmine:monero.social >__ I agree     

> __< azunda >__ at 10 cents it's 10% of a 1$ coffee     

> __< azunda >__ pure rage     

> __< sech1 >__ Fee increase is a dangerous thing to do     

> __< r​ucknium:monero.social >__ We can ask Monero users in Argentina.     

> __< sech1 >__ When price pumps 10x, you will hardfork again to decrease fees?     

> __< rbrunner >__ You mean with a fee explosion we make many new friends there?     

> __< a​rticmine:monero.social >__ Good point     

> __< s​gp_:monero.social >__ sec1: there must be an implied value of XMR before FCMP, it's unavoidable     

> __< azunda >__ sech1 - switch to log view, we had many events like this     

> __< azunda >__ and add to this the current big exchange delisting      

> __< s​gp_:monero.social >__ clearly we made an assumption about the price of XMR right now and it was too low     

> __< sech1 >__ all previous events had news linked to them, like Alphabay starting using Monero     

> __< s​gp_:monero.social >__ the relationship between blocksize and XMR value did not correlate as articmine had hoped     

> __< sech1 >__ Big exchange delisting and transactions spike didn't happen on the same day     

> __< r​ucknium:monero.social >__ The skepticism about the spam hypothesis just means it's in my research agenda :). https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60     

> __< azunda >__ sech1 - didn't happen the same day because of the price drop, people were scared it will go to zero     

> __< azunda >__ after dust settled people came back     

> __< s​gp_:monero.social >__ regarding the $0.10 is too expensive for people in some countries, unfortunately I don't know how we can possibly plan around accommodating this     

> __< r​ucknium:monero.social >__ But first: Assume it's a black marble flood and measure potential impacts and options. Then evaluate the spam hypothesis empirically.     

> __< s​gp_:monero.social >__ even if we don't hike the fees and the attacker keeps spamming, then users will still be priced out since their transactions have too low of a fee to be confirmed     

> __< sech1 >__ Binance has closed withdrawals most of the time, they couldn't physically release so many coins to so many users, so I don't believe this connection     

> __< azunda >__ large amount of people could use Binance to trade between themself without actually doing it on the chain     

> __< s​gp_:monero.social >__ the transaction fee will always need to be anchored in real network costs, irrespective of one's ability to afford the transaction fee     

> __< rbrunner >__ We could also think a bit about our limited dev time budget. Every person week going into battling this moves Seraphis/Jamtis and FCMPs further out     

> __< c​haser:monero.social >__ I'm not, but I do oppose gauging protocol parameters in dollars. XMRUSD may halve or 5x in a year.     

> __< rbrunner >__ And Seraphis has a much higher ringsize more "naturally"     

> __< sech1 >__ azunda to move from Binance to on-chain, they first need to withdraw and withdrawals are nowhere near at the capacity needed for this flood     

> __< a​rticmine:monero.social >__ The delisting by Binance eliminated a very significant centralized ledger where settlement of XMR was occurring. This is not unlike what has happened with Bitcoin where centralized ledger settlement has taken over     

> __< sech1 >__ asticmine same, read my message     

> __< sech1 >__ You both don't understand that it's just not enough coins there to provide all this flood     

> __< sech1 >__ Numbers don't add up, so maybe 1-2k transactions per day come from Binance refugees, but not more     

> __< rbrunner >__ And all of a sudden almost magically most people only produce 1 in, 2 out transactions. Nice fairy tale, IMHO.     

> __< s​gp_:monero.social >__ agreed, this is one of the biggest signs. All 1in/2out is impossible to reconcile at this scale     

> __< sech1 >__ I understand people want to believe in sudden 5x adoption, but reality is more likely to be some spam     

> __< a​rticmine:monero.social >__ Actually looks at the surge just when Binance delisted. It is close to double     

> __< azunda >__ withdrawals were closed but not incoming transactions     

> __< azunda >__ they could still do business     

> __< azunda >__ now they do it outside     

> __< s​gp_:monero.social >__ sech1: why are you against raising fees?     

> __< sech1 >__ because fees are fine?     

> __< a​rticmine:monero.social >__ https://bitinfocharts.com/comparison/monero-transactions.html#3m     

> __< sech1 >__ Compare to BTC fees (in BTC terms vs XMR fees in XMR terms)     

> __< rbrunner >__ azunda, go a bit back in time and look carefully at block before this attack, how transaction sizes vary if they are "organic"     

> __< sech1 >__ they're literally the same     

> __< sech1 >__ you raise fees today, few years down the road you have to drop them because price pumped 10x     

> __< sech1 >__ stupid     

> __< s​gp_:monero.social >__ what do you mean fees are fine? fees are supposed to discourage this behavior. Pricing where BTC == XMR makes no sense to me, since the attacker isn't acquiring at those BTC costs     

> __< sech1 >__ I mean it's a stupid thing to do every time something happens     

> __< s​gp_:monero.social >__ it's not stupid because the alternative is not having an adequate deterrent     

> __< s​gp_:monero.social >__ I 100% agree it's shitty     

> __< s​gp_:monero.social >__ but what else is realistic? not having a deterrent? that's even worse     

> __< azunda >__ if it's one or couple more big players that started using some automated tools, the tx could have patterns ?     

> __< rbrunner >__ Really not sure about "no adequate deterrent". They spam well below their technical capacity, no?     

> __< sech1 >__ If it's a big resourseful attacker, believe me 10x fees won't help     

> __< r​ucknium:monero.social >__ I plotted the daily tx volume of txs with the "spam fingerprint" (1in/2out 20 nanoneros/byte) in Feb and March 2024: https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/images/spam-fingerprint-tx-volume.png     

> __< sech1 >__ Bigger ring size could help better     

> __< r​ucknium:monero.social >__ From about 15,000 to 100,000 in about a day.     

> __< s​gp_:monero.social >__ we need to draw the line somewhere, else we should just roll out the "we're fucked" map     

> __< c​haser:monero.social >__ that was a 50% surge which then quickly ended.     

> __< s​gp_:monero.social >__ bigger ringsize is a similar lever as higher fees, but with more network costs     

> __< sech1 >__ Plus I'm against raising fees because it will screw up p2pool miners big time     

> __< sech1 >__ Not until there is a cheap way to consolidate p2pool payouts     

> __< sech1 >__ i.e. coinbase outputs     

> __< s​gp_:monero.social >__ that's the real reason you hate it; is there no way to give people fewer, larger outputs?     

> __< sech1 >__ That's the main reason but not the only one     

> __< sech1 >__ the USD price is the other one     

> __< r​ucknium:monero.social >__ IMHO, when (if) ring size increases in next hard fork, make all coinbase output spends ringless like MRL issue #...     

> __< azunda >__ if this is an attack, we would need to increase the fee 100x - that's not "ideal".     

> __< azunda >__ to even make a dent     

> __< sech1 >__ You can't just change fees because price is low and fees are cheap. Next you'll have to change them all the time to fit a new XMR price     

> __< s​gp_:monero.social >__ the ideal state is not being under attack lol. But given we're here, we need to compromise on something     

> __< r​ucknium:monero.social >__ This one: https://github.com/monero-project/research-lab/issues/108 "Coinbase Consolidation Tx Type"     

> __< s​gp_:monero.social >__ and I'm begging you all for the compromise to not be massive transactions because we can't agree to make transactions more expensive     

> __< rbrunner >__ With the danger of being a heretic: We do not "have to" do something. I can live with ringsize 5.5 and the danger they will spam more until Seraphis and FCMPs.     

> __< azunda >__ sgp pushing hard on fee increase      

> __< a​rticmine:monero.social >__ It targets the spam and not the ham     

> __< azunda >__ is there a hidden agenda ? /s :D     

> __< rbrunner >__ Given the "shitty" alternatives     

> __< sech1 >__ Transaction sizes will increase with Seraphis anyway, so why not increase ring size a little before that?     

> __< s​gp_:monero.social >__ I don't know what you mean by ham, but fees literally target the spammer directly by requiring them to pay more, without costs to nodes. And it also benefits miners (p2pool mini dust outputs aside)     

> __< rbrunner >__ Not to forget that we always only talk about 1 out of 3 privacy mechanisms ...     

> __< s​gp_:monero.social >__ as I said before, I'm not against a ringsize increase. But I am begging you to additionally hike the fees     

> __< a​rticmine:monero.social >__ Ham legit transactions as opposed to spam     

> __< s​gp_:monero.social >__ zunda: you must be new here; I've been a (the?) major proponent of most ringsize increases haha     

> __< s​gp_:monero.social >__ azunda: you must be new here; I've been a (the?) major proponent of most ringsize increases haha     

> __< sech1 >__ If ring size increase will reduce the efficiency of the spam attack, why increase the fees then?     

> __< s​gp_:monero.social >__ because fees arguable reduce the efficiency even more     

> __< s​gp_:monero.social >__ because fees arguably reduce the efficiency even more     

> __< azunda >__ i'm from the very beginning, had different names.     

> __< sech1 >__ Not against an attacker who presumably has huge resources     

> __< s​gp_:monero.social >__ sech1, if the attacker has near unlimited resources, then a larger ring won't do anything either     

> __< azunda >__ we should assume that attacker has close to "infinite" recources when it comes to fees     

> __< sech1 >__ nor increased fees     

> __< s​gp_:monero.social >__ they'll just hike their fees and take a higher ratio to account for the stronger ringsize protections     

> __< sech1 >__ increased fees will only reduce legit on-chain activity, and spam tx will stay the same     

> __< s​gp_:monero.social >__ which is why we need to accept that they don't have unlimited resources, or else we would need to admit this is all pointless     

> __< azunda >__ seems like an attack, on adoption by forcing devs to increase the fee.     

> __< azunda >__ if they can afford 3 XMR today, they can afford x4 easily too     

> __< rbrunner >__ Yes "unlimited resources" will overpower everything, that's not a reasonable base for discussion     

> __< s​gp_:monero.social >__ anyway, I've made my same points three times now. It's clear that most people here would rather have massive transactions than hike the fee to still-reasonable-levels     

> __< azunda >__ how long the attacker could sustain the attack while having "just" 1 Mil USD ?     

> __< r​ucknium:monero.social >__ Ring size 40 is 5.5 Kb for 2in/2out, right? Not massive IMHO.     

> __< azunda >__ after increase of the fees     

> __< s​nowman:tetaneutral.net >__ Fee increase does nothing against an attacker with infinite money to spend.  Fcmp, keep devs focused and keep moving forward is the only answer.     

> __< rbrunner >__ Secretely I almost start to hope that our decision process will sort-of-deadlock like it did regarding tx_extra stay/remove, and we just do nothing.     

> __< s​gp_:monero.social >__ that's over a 2x size increase, no?     

> __< r​ucknium:monero.social >__ Yes, we are in the 3rd hour of the "meeting". We have run out of new points to make with the current information available.     

> __< r​ucknium:monero.social >__ yes. Only 2x     

> __< sech1 >__ I think it's more of a psychological attack than a real black marble attack     

> __< a​lex:agoradesk.com >__ Guys, let's discuss other solutions please. The fee increase bandaid is pointless in my opinion. I would rather the Monero general fund spend 3 XMR per day to counter-spam and thereby dilute the effect of the attacker until FCMP is deployed.     

> __< sech1 >__ it's not intensive enough to deanonymize most rings     

> __< sech1 >__ forcing devs to "do something"     

> __< s​nowman:tetaneutral.net >__ Agreed     

> __< a​lex:agoradesk.com >__ sech1 is correct, and so is rbrunner, there is no forced action here.     

> __< a​rticmine:monero.social >__ I proposed increasing the reference transaction size from 3000 bytes to 8000 bytes, but only increasing the minimum penalty free blocksize from 300000 bytes to 400000 bytes.  This requires an increase in the minimum node relay fee of 4x     

> __< a​rticmine:monero.social >__ The 8000 byte figure is to accommodate full membership proofs with tx sizes around 5500 bytes vs around 2000 bytes now     

> __< azunda >__ if price of Monero goes up by 10x the new fee would be painful to some     

> __< a​lex:agoradesk.com >__ Just raising the fees based on an arbitrary American's understanding of what's reasonable is not how things should be done in Monero.     

> __< a​rticmine:monero.social >__ As an interim solution this can also accommodate a ring size of 40 or even more     

> __< s​nowman:tetaneutral.net >__ Can we tie ring size dynamically to spam     

> __< a​rticmine:monero.social >__ No     

> __< azunda >__ due to uniformity problem or other technical problem ?     

> __< c​haser:monero.social >__ we don't know that.     

> __< a​lex:agoradesk.com >__ I prefer ArcticMine's solution, but honestly I don't think this is an urgent situation. I think counterspamming until FCMP comes is something people who are worried about this should do. This doesn't require any hardforks or deployments.     

> __< azunda >__ the organic growth we had will counter attack the adversary (if it's adversary) more and more     

> __< r​ucknium:monero.social >__ Uncoordinated counterspam is hard to stop. How do the counterspammers know that the malicious flood is finished?     

> __< azunda >__ time is on our side     

> __< a​lex:agoradesk.com >__ They don't. But after FCMP it doesn't matter.     

> __< a​lex:agoradesk.com >__ Additionally, counterspammers can declare on /r/Monero that we stop counterspamming for a day to see if the attack subsided.     

> __< a​lex:agoradesk.com >__ The fundamental issue here is not going to be solved until FCMP, no matter how many bandaids you apply.     

> __< r​ucknium:monero.social >__ Alex | LocalMonero | AgoraDesk: "The fundamental issue here..." I agree.     

> __< a​rticmine:monero.social >__ There is also the possibility of multiple black marble attackers working against each other. This attack only works with only one spammer     

> __< r​ucknium:monero.social >__ (It's a live system and people depend on it for privacy now FWIW.)     

> __< c​haser:monero.social >__ yes, as was stated last time, we're looking for the least bad strategy (in case we're looking at all)     

> __< a​lex:agoradesk.com >__ Does anybody want to start a counterspam task force? Let's make a group and coordinate this. PM me.     

> __< plowsof >__ burn 3xmrday on tx spam or fund FCMP development with it      

> __< a​lex:agoradesk.com >__ AFAIK, FCMP development doesn't lack funding.     

> __< azunda >__ what we really need is more adoption, this attacks would be worthless if we had 100x more real tx     

> __< nioCat >__ plowsof: why not both?     

> __< c​haser:monero.social >__ that is very unwise, for the reasons I outlined in my summary on Github. you don't want to make Monero's privacy depend on the unverifiable altruistic actions of trusted parties. moreover, you don't want Monero to be *seen* like that. it would create a disastrous reputation, which would also reflect in the price.     

> __< a​lex:agoradesk.com >__ Like it or not, rings are a weak point of XMR and have been for a while.     

> __< a​rticmine:monero.social >__ That is my understanding. If I understand correctly ring 40 would also significantly mitigate the spam. So this looks like a valid option     

> __< a​lex:agoradesk.com >__ If you're worried about the marbles, without FCMP, this is one solution.     

> __< plowsof >__ localmonero should fund a tumbler address then. every piconero sent to it will be churned over and over. it can have a vanity address "Sp4mt4skforce"     

> __< azunda >__ increasing it was the best idea so far but i would leave fee alone as increasing them by 4x or even 10x will do nothing to let's say chainalysis company that earns millions of dollars      

> __< azunda >__ and it will only harm adoption which fixes this      

> __< azunda >__ *increasing ring size      

> __< azunda >__ as articmine suggested     

> __< c​haser:monero.social >__ I asked last summer if it lacked talent; the answer was no.     

> __< s​nowman:tetaneutral.net >__ Has there been any effort to reach out to cake, changenow, trocador, localmonero to see if there is any significant bump in usage since binance delisting     

> __< r​ucknium:monero.social >__ Yes FCMP needs more talented labour.     

> __< r​ucknium:monero.social >__ Having capital does not mean that you have labour.     

> __< 1​23bob123:matrix.org >__ Torcador just ask morpheus     

> __< 1​23bob123:matrix.org >__ Not in this room tho     

> __< a​lex:agoradesk.com >__ Assuming that yes, it still doesn't explain away the 1 in/2out flood.     

> __< s​gp_:monero.social >__ a​zunda: you realize a >2x increase in the transaction size also means an implied >2x increase in Monero fees right? Just making sure     

> __< c​haser:monero.social >__ I posted charts of Bisq daily trade numbers and volume in the #monero-research-lounge:monero.social . there is nothing there that would explain this volume (not that it would matter).     

> __< s​gp_:monero.social >__ a​zunda: you realize a >2x increase in the transaction size also means an implied >2x increase in Monero fees per transaction right? Just making sure     

> __< azunda >__ yes     

> __< a​rticmine:monero.social >__ Not if you increase the minimum penalty free blocksize by the same amount..     

> __< azunda >__ nice     

> __< s​gp_:monero.social >__ ArticMine: I really hope you ask for Cake's opinion before you double node requirements lol. Their monthly node cost is already thousands of dollars. They already move over 200 TB/mo     

> __< azunda >__ sgp - and how much do they earn ?     

> __< azunda >__ it's probably a fraction of their income...     

> __< azunda >__ *small fraction     

> __< a​rticmine:monero.social >__ In my proposal the minimum penalty free zone would be increased by half.  So in terms of the current penalty free blocksize this is equivalent to 150000 bytes. With quadratic scaling the fee would fall back to the current at 300000 bytes equivalent or 800000 bytes.     

> __< azunda >__ so on one hand we have a company that earns a lot of money to pay a bit more for their servers and on the other hand ALL users of Monero     

> __< r​ucknium:monero.social >__ I don't think we know how increasing ring size affects remote node performance. How much of the ring sig data actually needs to be sent to wallets?     

> __< c​haser:monero.social >__ not that I wish ill on Cake, but calibrating the protocol according to the needs of large centralized RPC providers is quite against the ethos of decentralization.     

> __< r​ucknium:monero.social >__ Pruning eliminates most rig sig data and it is not supposed to affect wallet operation at all.     

> __< r​ucknium:monero.social >__ If you need to keep the whole blockchain in RAM, prune the node in RAM.     

> __< s​gp_:monero.social >__ so we can assume roughly 50% more p2p traffic with this proposal?     

> __< s​gp_:monero.social >__ unless there's something else I'm missing     

> __< a​rticmine:monero.social >__ A better solution in my view is to optimize monerod and support large scale parallel processing on CPU and GPU. This will help all users both large and small     

> __< r​ucknium:monero.social >__ boog900, hinto , SyntheticBird45 : Any comments about how cuprate plans to parallelize?     

> __< a​rticmine:monero.social >__ It is 2.5x in bandwidth, and the same as expected for FCMP     

> __< a​rticmine:monero.social >__ FCMP     

> __< s​gp_:monero.social >__ the issue is that cake can't whip up a custom, prod-ready lmdb reader in a week. In time for FCMP, sure     

> __< a​rticmine:monero.social >__ This hard fork will not happen in a week. Seriously     

> __< r​ucknium:monero.social >__ ArticMine: When you have a range of fee and blocksize adjustment options available, I can do some modeling.     

> __< b​oog900:monero.social >__ better and we will have no locks for RPC requests.     

> __< b​oog900:monero.social >__ For my last CCS while I was implementing Monero's consensus rules in Cuprate I made an RPC scanner to test them, it gets data like outputs from public node's RPC. I ran it side by side with monerod doing full verification and the RPC scanner completed first around 170,000 blocks ahead     

> __< a​rticmine:monero.social >__ 👍     

> __< b​oog900:monero.social >__ monerod was ahead until RCT and then the RPC scanner started to catch up, over taking around block `2428000`     

> __< c​haser:monero.social >__ that's great news. for scanning speed, is that number relevant though (blocks per full chain scan)? wouldn't a metric like "tx type 6 rings per second" be more descriptive?     

> __< g​ingeropolous:monero.social >__ some thoughts as im reading through logs. re: raising the fence. adding a tx-pow might do stuff.  oh i see rbrunner7 brought that up. And yeah, somehow hooking the PoW difficulty into tx_pool size could be interesting.  I share the concern about "real" fees re: the need to have lots of ham for monero's ring sigs to work right. And yeah Rucknium , i've talked about tieing fees to h<clipped me     

> __< g​ingeropolous:monero.social >__ ashpower. i personally think hashrate is closes we can get to a within-chain metric of monero's extrinsic value. ArticMine , how does PoW to submit discriminate against most of the developing world? I'd imagine the PoW requirement for a single tx would be minimal, but if we could somehow find a way to connect the PoW requirement to volume. Perhaps its at the peer level. I.e., I al<clipped me     

> __< g​ingeropolous:monero.social >__ ready received a transaction from this peer within the past 10 usec. I need a higher PoW to receive another.     

> __< b​oog900:monero.social >__ Those  exact numbers don't really mean anything more just the point that we are requesting outputs for rings over RPC and we completing verification faster than monerod getting them locally and that monerod becomes significantly slower around RCT.     

> __< b​oog900:monero.social >__ We don't have a working database yet so until then I don't think any measurements of how fast we can verify txs will be completely accurate. I am planning to bench Cuprate vs monerod more thoroughly though when more is done.     


# Action History
- Created by: Rucknium | 2024-03-19T20:53:08+00:00
- Closed at: 2024-03-27T22:52:35+00:00
