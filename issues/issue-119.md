---
title: potential measures against a black marble attack
source_url: https://github.com/monero-project/research-lab/issues/119
author: chaserene
assignees: []
labels: []
created_at: '2024-03-19T05:48:14+00:00'
updated_at: '2024-06-15T14:39:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
updated: 2024-06-15

## motivation

during March 4--27, 2024, Monero experienced a sudden surge in [on-chain transaction volume](https://bitinfocharts.com/comparison/monero-transactions.html#1y) (15k-25k tx/day -> 115k-140k tx/day). as of May 29, there have been a couple of subsequent spikes to levels rarely breached during the months before the surge, but the flood had mostly subsided. (there have been two minor consolidation floods that don't seem to be relevant to privacy and black marble attacks). however,  there has been/is a [suspicious rise](https://gist.github.com/Rucknium/567fc52380acaf2991a2f1ad91a95) in the share of 1-in / 8-16-out transactions which could be a less visible way of conducting the attack that this issue focuses on.

it has been known since the birth of the network (see [Noether, et al: A Note on Chain Reactions in Traceability in CryptoNote 2.0](https://www.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf) from 2014) that ring signatures as a method of obfuscating the transaction graph are vulnerable to an adversary flooding the network with transactions and progressively eliminating the decoys of honest users, thereby reducing their privacy in the graph, potentially to the point of identifying the real spend. following the above paper's terminology, this is called here a *black marble attack*, although it has other names as well, e.g. *flood(ing) attack* (from [Chervinski, et al: Analysis of transaction flooding attacks against monero](https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=43&browserTabID=)).

for an analysis of this event, see @Rucknium's paper "March 2024 Suspected Black Marble Flooding Against Monero]" in the resources section.

some in the community don't believe that the current situation is a black marble attack (attributing it to organic activity or other sources); others do. I posit that this is irrelevant, because of the following:

1. we can't prove it's **not** a black marble attack, and since Monero is primarily a tool for preserving privacy, we should err on the side of defensiveness. we don't have the luxury of assuming the optimistic scenario, since the downside is that people who rely on Monero are exposed to excess danger.
2. this situation is simply a reminder that such an attack is currently very practical and cheap in Monero, and serves as the best available opportunity to try to tackle it (that is, before an ultimate solution is deployed; see the "omitted measures" section below). if the current flood were to abruptly stop, the probability of a black marble attack would remain at least the same. if anything, this demonstration is rather an invitation for future attackers.

## measures

the below is an informal summary of potential measures we are discussing that can counter such an attack, applicable to the Monero protocol in its current state (fork version v16, code name "Fluorine Fermi"). I will try to keep the information here in sync with the state of the discussion in the Monero Research Lab and Monero Research Lounge chat rooms.

since none of these measures solve the root issue, some of them can be thought of as temporary changes that can be reverted if/when Monero is upgraded to full-chain membership proofs (FCMP). most of them can be combined with each other.

| measure | pro | con
| - | - | -
| **do nothing** | * avoids rushed decisions/mistakes that could make things worse and take an(other) fork to remedy<br><br>* many of these interventions can be rendered ineffective if attacker has a lot of resources | * attacker can keep lowering the effective ring size at the same costs as now<br><br>* we don't know how much resources an attacker has without trying to exhaust them (defeatism)
| **increase ring size** | * tx's have more non-attacker decoys on average (in absolute terms); attacker may choose not to increase their tx volume in accordance (due to higher tx fee costs)<br><br>* depending on ring size, can prepare the network for tx sizes under [FCMP++](https://libera.monerologs.net/monero-research-lab/20240529#c382558) or [Seraphis](https://raw.githubusercontent.com/UkoeHB/Seraphis/master/seraphis/Seraphis-0-0-18.pdf#page=18) | * requires fork<br><br>* higher node/wallet resource requirements<br><br>* higher tx fees?
| [**modify existing dynamic block size parameters**](https://libera.monerologs.net/monero-research-lab/20240314#c347713) | * attacker may reduce/stop their tx's due to higher tx fee costs | * requires fork<br><br>* higher tx fees in general
| **introduce [ultra-long-term sanity median](https://libera.monerologs.net/monero-research-lab/20240314#c347714)** | * attacker may eventually reduce/stop their tx's due higher tx fee costs | * requires fork<br><br>* eventually higher tx fees in general<br><br>* will have effect only on a very long time scale |
| **increase "effective minimum tx fee"** | * attacker may reduce/stop their tx's due to higher tx fee costs |  * requires fork<br><br>* higher tx fees
| [**penalize outputs above 2**](https://github.com/monero-project/research-lab/issues/119#issuecomment-2125473270) | * attacker may reduce/stop their tx's due to higher fee-per-output costs<br><br>* the penalty for most honest tx's is zero/moderate | * requires fork<br><br>* higher fees for honest tx's with >2 outputs<br><br>* attacker may continue with 1/2s, making their activity less detectable
| **increase minimum node relay tx fee** | * attacker may reduce/stop their tx's due to higher tx fee costs<br><br>* can be activated without a fork | * requires fork to work effectively (otherwise nodes can stay on older version)<br><br>* higher tx fees<br><br>* attacker can coordinate with mining pools to get their tx's mined<br><br>* same best-case outcome as with increasing the "effective minimum tx fee", but with the above added risk
| **introduce per-peer tx PoW for relay** | * attacker may reduce/stop their tx's due to introduced hardware + electricity costs<br><br>* can be activated without a fork | * attacker can coordinate with mining pools to get their tx's mined<br><br>* higher wallet resource requirements; can price out senders with low-end hardware, expensive electricity and/or in hot climates
| **introduce tx PoW for inclusion in block** | * attacker may reduce/stop their tx's due to introduced hardware + electricity costs | * requires fork<br><br>* higher wallet resource requirements; can price out senders with low-end hardware, expensive electricity and/or in hot climates
| **reduce tx lifespan in tx pool** | * less of an attacker's transactions may get mined<br><br>* can be activated without a fork | * attacker can fine-tune the rate of tx broadcast to reach same inclusion rate<br><br>* requires fork to work effectively (otherwise nodes can stay on older version)<br><br>* attacker can coordinate with mining pools to get their tx's mined<br><br>

## omitted measures

measures discussed but omitted from the table because they don't seem to be (immediately) applicable:
* **introduce [full-chain membership proofs (FCMP)](https://github.com/kayabaNerve/full-chain-membership-proofs) with [Seraphis](https://github.com/UkoeHB/Seraphis)**: FCMPs are the ultimate solution to attacks related to ring signatures, but they are currently not in a deployable state. ideally, they would be introduced together with the Seraphis transaction protocol designed by @UkoeHB. presuming the current rate of progress won't change, they estimate such a deployment would be ready in [5+ years](https://libera.monerologs.net/monero-research-lab/20240329#c354069).
* **introduce FCMP on top of ring confidential transactions**: @kayabaNerve designed the [FCMP++](https://raw.githubusercontent.com/kayabaNerve/fcmp-ringct/develop/fcmp%2B%2B.pdf) protocol, which is a way to deploy FCMP on top of the current transaction protocol (RingCT/CryptoNote), that is, before Seraphis. there is strong general support for this new direction. kayabaNerve's optimistic timeline for deploying such a setup is about 12-18 months. this would radically fast-track the statistical proofing of Monero's privacy, but still wouldn't make it applicable on the short/mid term.
* **shift decoy selection distribution toward older enotes**: this would make it easier in certain cases to guess the real spend, and any advantage would be eroded over time if an attack is sustained. this would also require a fork.
* **counterattack**: this would rely on honest participants conducting a counter-flood, keeping the resulting deanonymizing transaction data safe, and then securely erasing it. all these involve unverifiable actions (trust), and, unless perfectly coordinated among all participants, they would be unable to tell if an attack was over or not.
* **miners limit the size of their blocks**: this would limit the ratio of an attacker's enotes to all enotes in a block, but relies on altruism and well-enough coordination from miners.

## resources

* @Rucknium: [March 2024 Suspected Black Marble Flooding Against Monero](https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf) (direct PDF view)
* @Rucknium: [Defeating a Black Marble Flood Against Monero: Best Options for Ring Size and Transaction Fee](https://raw.githubusercontent.com/Rucknium/misc-research/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-optimal-fee-ring-size.pdf)  (direct PDF view)
* @ArticMine: [Scaling Monero in Response to Blockchain Surveillance (MoneroKon 2024)](https://odysee.com/@monerocommunityworkgroup:8/francisco-%27articmine%27-cabanas-scaling:b?t=1172)  (19:32, "Proposed Scaling Changes") (Odysee)
* @Rucknium: [Black marble defense parameters -- R Shiny app ](https://black-marble-defense-params.redteam.cash/)

# Discussion History
## monerobull | 2024-03-19T14:18:52+00:00
i like artics suggestion of raising the minimum fee to the level a standard transaction will cost in the future under FCMPs.

## mmgen | 2024-03-22T16:18:45+00:00
Raising the minimum fee, along with the possible addition of transaction POW, seems like the easiest-to-implement and least disruptive interim solution to me.

## johnr365 | 2024-03-24T14:24:04+00:00
After reading through the [March 20 MRL meeting](https://github.com/monero-project/meta/issues/981), my vote would be for increasing the minimum transaction fee as a first step.

That doesn't preclude raising the ring size later, if needed, whilst waiting on FCMPs.

I saw that rbrunner, sech1 and Alex of Local Monero were against raising the minimum fee. Which does give me pause for thought. I'd like to hear more about their rationale not to.

One argument against raising minimum fees is that *if* Monero fiat value goes 10x then the fees may look too expensive, and would require another fork to correct. 

But simultaneously, *if* Monero goes 10x, it's a nice problem to have, and the community can probably manage the small tweak needed to make fees more affordable.

## donttracemebruh | 2024-03-24T21:16:43+00:00
I support raising the minimum fee with plans to revert the fee raise during the FCMP fork. Cheap fees make sense in a FCMP protocol, but cheap fees are detrimental to privacy under a ring signature protocol as rings have this spam attack weakness. 

I would also support a ring increase, although I think it would be better to aim for something like 50% (or less) of the tx size under FCMPs, in order not to increase the blockchain size any more than we have to. 

## tarris034otheracc | 2024-03-26T16:11:42+00:00
Increase ring signatures, leave fees at current level as the attacker surely won't be affected by 10x fees and we will have to do another hard fork if we see 10x FIAT evaluation.

If the attacker is chainanalysis company, we would need to increase fees 100x to make a dent in their accounts.

## donttracemebruh | 2024-03-27T12:39:50+00:00
Its about increasing the cost to attack. There will always be entities with seemingly unlimited resources that no amount of fees will ever deter. The goal should be to price out small to medium sized attackers while making miners more profitable and increasing network hashrate. Currently mining is very much not profitable to the point that a certain Monero fork is more profitable to mine and has surpassed Monero in hashrate. We shouldn't increase fees too drastically, but targeting fees of 1 cent to 5 cents for example would still be a negigible amount for most Monero users while drastically increasing miner's profits and the cost to spam the network.

## wallart1 | 2024-03-27T12:54:09+00:00
Just a random thought from a neophyte: How about building in a laundering system that would, _in effect_, increase the anonymity set by multiples for even non-linearly. Do the laundering in the nodes, making it distributed. And figure out some way to make the distribution random. God help you if coins get lost, and you need to figure out what happened.

I apologize if this has been considered already.

## molangning | 2024-03-27T12:57:25+00:00
I’m not good with crypto stuff, but isn’t that technically a counter attack?

## wallart1 | 2024-03-27T12:59:13+00:00
I don't think it is. It's just a way to increase privacy. 

Edit: Bitcoiners do it all the time, and the government hates it.

## Rucknium | 2024-03-27T21:19:39+00:00
I have preliminary analysis of the possible black marble flood:

https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf

## March 2024 Suspected Black Marble Flooding Against Monero: Privacy, User Experience, and Countermeasures

### Abstract
On March 4, 2024, aggregate Monero transaction volume suddenly almost tripled. This note analyzes the effect of the large number of transactions, assuming that the transaction volume is an attempted black marble flooding attack by an adversary. According to my estimates, mean effective ring size has decreased from 16 to 5.5 if the black marble flooding hypothesis is correct. At current transaction volumes, the suspected spam transactions probably cannot be used for large-scale “chain reaction” analysis to eliminate all ring members except for the real spend. Effects of increasing Monero's ring size above 16 are analyzed.

## tarris034otheracc | 2024-03-28T18:23:02+00:00
> ...The goal should be to price out small to medium sized attackers

In this case, more attackers that don't collude is better when it comes to black marble attack. (just saying)

> Currently mining is very much not profitable....

Auto adjusting difficulty will take care of this, some miners will drop and some new will come.
I wouldn't worry about some premined fork taking over miners that could mine for Monero network, ALL premined projects rug pull eventually.



## aleksify | 2024-04-15T18:17:53+00:00
Can someone explain how introducing tx PoW would have a different effect than increasing the minimum tx fee? Fundamentally, a piece of Monero already represents that some PoW was done. So if someone is willing to make "tx PoW", they could just mine some monero (in case of increased minimum tx fee) and it would have the same exact effect. Except that if you can't mine it, you could just buy some, while in the case of tx PoW you're not able to. It worsens the user experience by removing this alternative, while the effect for an attacker would be ultimately the same as if the minimum tx fee was raised (if they have money to flood the network, they have money to rent powerful enough hardware to do the tx PoW required). In the end, I see no scenario where tx PoW would be preferable to raising the minimum tx fee.

## Gingeropolous | 2024-04-16T11:03:17+00:00
you should indicate that 2 versions of the tx-pow exist. The one where PoW is block inclusion consensus (which requires a fork), and one that requires a PoW for relaying transactions (which does not require a fork). 

> they have money to rent powerful enough hardware to do the tx PoW required).

do they? It depends on how its done. The way I imagine tx-PoW is to require the PoW for relaying a transaction, and the diff requirements are dynamic per node connection. 

Here I tried to put together a simulation and the flow of how it would work (the sim doesn't work because I can't code that well and I need a time multiplier so I can do more things in a day):
https://github.com/Gingeropolous/txsim/blob/main/prompt_flow_description.txt

But basically, your node tracks the transaction rate of every node you are connected to. In normal conditions, the PoW diff is so low as to not even be noticeable, even by phone users. Perhaps it takes 5-10 seconds to craft a PoW to package your tx for relay. 

If your node starts receiving transactions way over some rolling average (or something), your node increases the PoW requirements in an exponential fashion. It can be designed that in a matter of seconds (10 seconds?), if so many transactions come in from a peer (who is clearly an attacker), the difficulty requirements skyrocket to the point where it would take many minutes for the attacker to craft a PoW for each tx. 

So, this decreases the rate at which an attacker can actually submit txs to the network. Yes, it is still possible for the attacker to submit transactions, but the effort wall has been raised ... exponentially. 

To me, the only downside is the critique proposed by articmine, where low-end users wouldn't be able to submit txs during an attack. I attempt to mitigate this by creating a re-packaging process, whereby nodes can re-package a tx with a new PoW to facilitate relay in instances where they receive txs with low diff from a "friendly" node connection (one that has a low rate of txs etc). 



## chaserene | 2024-04-16T22:08:33+00:00
@Gingeropolous 

> you should indicate that 2 versions of the tx-pow exist. The one where PoW is block inclusion consensus (which requires a fork), and one that requires a PoW for relaying transactions (which does not require a fork).
 
that's a very good point. I split it up into two entries in the table in the OP.

## hundehausen | 2024-04-16T22:14:56+00:00
@Gingeropolous do all nodes increase their PoW requirements, or only the node receiving the spike in transaction? What stops the attacker from switching to the next node to relay the transactions, where the PoW requirement is still low? Or what about the attacker using a new tor circuit or other proxy server to relay their txs?

## Gingeropolous | 2024-04-17T11:17:48+00:00
>  do all nodes increase their PoW requirements, or only the node receiving the spike in transaction? 

Only the node receiving the spike in txs

> What stops the attacker from switching to the next node to relay the transactions, where the PoW requirement is still low? 

Nothing, but nodes have connection limits. I've witnessed plenty of incoming connection denials to my nodes due to my node being at its connection limit. 

> Or what about the attacker using a new tor circuit or other proxy server to relay their txs?

I think at some point, whatever the tor circuit or proxy, you're going to hit the connection limit of a node. 

All of these moving parts is why I wanted to build a simulation for this. 

## tevador | 2024-04-29T09:28:40+00:00
> The way I imagine tx-PoW is to require the PoW for relaying a transaction

It should be noted that Monero already has an indirect PoW requirement for relaying transactions. Because we use CPU-friendly PoW for mining, you can convert tx fees to equivalent CPU hashes. With the current network hashrate, a 1/2 transaction with the minimum relay fee needs about the equivalent of 12 000 000 RandomX hashes. To put that into perspective, a relatively powerful PC can do around 10 000 hashes per second, so we are talking about 20 minutes of PoW to submit one transaction.

With that in mind, we can clearly see that any "5-10 second PoW to submit a tx" makes little sense in comparison with the necessary transaction fee. Equivalent functionality would be achieved by simply adjusting the minimum relay fee.

## Gingeropolous | 2024-04-30T01:50:29+00:00
I get what you're saying, but the fee as currently designed doesn't create a per-node rate limiter, which is what a PoW could do.

Much the same way in which PoW essentially rate-limits block production, we could use it to rate limit the amount of transactions your node will receive from a single peer. 

Like, the spam attacks probably operated as such: Attacker Alice spins up some nodes (A1-An) and then relays transactions to whichever nodes they happened to connect to, nodes B1-Bn.  So B1-Bn went from the standard trickle of transactions it would receive for relay to hundreds of transactions per second, perhaps thousands. 

If Alice had to craft a Pow for each transactions, and the difficulty of the PoW increased as they tried to send thousands of transactions to the node they are connected to...

then yes they'll hop to another node, but they will also get rate limited there, expending more work. 

In the current system, the attacker is only limited by IP address space. If there was dynamic PoW for relay, the attacker is limited by compute space. 

at least thats how it makes sense in my head. 


again, sure if we could make the tx fee dynamically related to a per node thing, then we could just do this with fees....

but we could also make the tx-pow where the sender actually mines on a block for the receiver.... well that could get complicated. 

* edited to add - i was on some thought train about some flaws, but then i realized that node A can have a bundle of txs and negotiate relay with node B using the cumulative PoW. That could help in a scenario where the attacker tried to stall the network by driving up the difficulty. 

## wallart1 | 2024-04-30T02:47:42+00:00
I don't understand why one wouldn't just set a tx rate limit as a node setting and ban any node that insists on exceeding it. Maybe one could be nice and put some back pressure in the protocol. Otherwise ban the bastard if he refuses to play by the rules.

## Gingeropolous | 2024-04-30T10:35:46+00:00
Because the tx rate limit needs to change in response to the demand. Like the blocksize. 

And also, a simple rate limit would allow the attacker to just get more IP addresses to make more connections. 

## tevador | 2024-05-22T18:22:36+00:00
The most efficient strategy for a black marble attacker is to spam 16-output transactions. The cost in fees per output is less than 1/4 of the cost of using just 2-output transactions.

We could mitigate this by introducing a weight penalty for transactions with `n>2` outputs. For example, a penalty of `600*(n-2)` bytes seems reasonable. Here are the estimated weights in KB with such a penalty:

| tx (in/out)  | current weight | new weight |
|-----|----------------|------------|
| 1/2 |     1.5        |    1.5     |
| 1/3 |     1.6        |    2.2     |
| 1/16|     2.7        |   11.1     |

This would make black marble attacks 4x more costly in terms of fees, while not affecting the fees of most users.

While this technically belongs under the "increase effective minimum tx fee" measure, I think it's sufficiently distinct and can be combined with a general increase of the base fee to compound the effect.

## chaserene | 2024-05-24T03:57:40+00:00
@tevador that's an attractive idea. I've added it to the OP.

~~I'd just suggest another term, since "transaction weight" is already used in the penalty calculation. I'll use "transaction fee weight" in this comment.~~

below is a table of approximate transaction ~~fee~~ weights per output in bytes, without penalty (current system) and with the proposed 600 B/out penalty. tx_extra = 33 B for all transactions (AFAIK the smallest achievable).

in/out|weight/out<br>(no penalty)|weight/out<br>(600 B/out penalty)
-|-|-
1/2|750|750
1/3|710|910
1/4|550|850
1/5|660|1020
1/6|560|960
1/7|490|920
1/8|440|890
1/9|630|1100
1/10|570|1050
1/11|530|1020
1/12|490|990
1/13|460|970
1/14|430|950
1/15|410|930
1/16|390|910

~~this still leaves 1/16's as the cheapest way to create outputs, but only marginally. if complete erosion of the 1/16 advantage is desirable, a 700 B/out penalty would achieve it.~~

~~in either case,~~ there is a potential downside: once costs will have increased, if an attacker still engages, they ~~could~~ would use 1/2's ~~at about the same new costs as 1/16~~, which would make it harder to isolate/detect their activity. however, that's arguably better than leaving them at the current cost level (~~4.4x~~ ~1.9x cheaper) with better detectibility.

## tevador | 2024-05-24T07:54:46+00:00
> I'd just suggest another term, since "transaction weight" is already used in the penalty calculation. I'll use "transaction fee weight" in this comment.

To be clear, the new weight would also apply to the penalty calculation. It's not just a relay rule. This must be done to prevent a black marble attacker from bypassing the rule by mining their own blocks filled with 1/16 transactions.

With this change, a block filled with 1/16 transactions would start burning fees at around 73 KB of actual size, when the effective block weight would exceed 300 KB.

## chaserene | 2024-05-25T04:16:00+00:00
> the new weight would also apply to the penalty calculation

it's good that you pointed that out, because it made me realize I made two mistakes in my calculations and thus some conclusions (now corrected above):

* transaction fees are calculated based on transaction weight, not size (if I read that right, your table has this too).

* the clawback expression in [Zero To Monero 2.0.0, p63](https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf#page=71) is no longer accurate. with Bulletproofs+ (from v0.18.0.0 on), the proof size was reduced, resulting in a slightly different expression (differences in bold):
  * transaction_clawback = **⌊** 0.8 ∗ ((**20** ∗ (*p* + num_dummy_outs)/2) · 32 − (2 · ⌈log<sub>2</sub> (64 · *p*)⌉ + **6**) · 32)**⌋**

## tevador | 2024-05-25T09:54:36+00:00
Thanks for the correction. So in that case, a penalty of 600 B/output is not suitable. Instead, we should modify the clawback formula so that all 1/N transactions have the same weight per output.

Batch payments will still be more efficient because of the saved change outputs (a 1/16 transaction can pay 15 people with 1 change output, doing the same with 1/2 transactions would require 30 outputs). But they would not be useful for spamming.

## j-berman | 2024-05-26T00:54:16+00:00
> It's not just a relay rule. This must be done to prevent a black marble attacker from bypassing the rule by mining their own blocks filled with 1/16 transactions.

Could be missing something here, but if mining their own blocks, the fee is going to themselves anyway and so the penalty would have no effect

## tevador | 2024-05-26T09:33:15+00:00
It would have an effect. 

1. They would lose the fees from legitimate transactions.
2. It would reduce the number of 1/16 transactions the attacker can fit into the penalty-free block weight.

The fees from legitimate transactions are mostly constant for a given block and would be lost in both scenarios (with or without the weight penalty). But the number of malicious outputs created would be lower with the weight penalty, leading to overall higher cost per output.

This also shows that spam transactions created by miners are basically free if there are not enough legitimate transactions in the mempool. This is a result of having a penalty-free block weight of 300 KB. For maximum spam protection, block reward should be burned for any block weight larger than the minimum, but this is out of scope of this discussion.

## j-berman | 2024-05-27T17:05:11+00:00
Got it, I see what I was missing

## Gingeropolous | 2024-05-29T11:15:47+00:00
regarding the PoW cons, I think this is false:

* higher wallet resource requirements;

the whole point of a well designed PoW (of which randomx and equix) is to be expensive to complete, but cheap to verify. Besides, a wallet wouldn't really be involved in the verification of the PoW. That work would fall on the node when it processes and/or verifies the transaction for inclusion/relay.

also to add, i think we could address the PoW4relay con "* attacker can coordinate with mining pools to get their tx's mined" by combining the relay requirements with the block inclusion requirements. So the relay PoW could be adaptive (rate limited per node by each nodes unique view of the network), and also have a minimum PoW for block inclusion. (because any relay PoW *should* also be high enough for block inclusion PoW). 

ima get ollama running and build this simulation soon (tm)


edited - of course now i realize you are talking about the creation of the transaction causing higher wallet resource requirements. Which is true. I guess I'll just ... uh..... get that sim running. 

# Action History
- Created by: chaserene | 2024-03-19T05:48:14+00:00
