---
title: Switch PoW algorithm to sha256d
source_url: https://github.com/monero-project/research-lab/issues/148
author: A60AB5450353F40E
assignees: []
labels: []
created_at: '2025-10-05T17:50:46+00:00'
updated_at: '2025-10-14T22:31:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm not kidding. CPU algo decentralization is an illusion, because big players like Meta and Google own immense amount of compute, just 5% of one Google's datacenter has enough hash to overtake Monero mining (only 100k CPUs last time I checked). sha256d is the most mature algo, and ASICs are available far and wide, it's as decentralized as PoW mining will ever get.

Whole argument here: https://github.com/monero-project/research-lab/issues/147#issuecomment-3368821660

And opening a new issue because it's kinda off-topic there. I will here address [comments](https://github.com/monero-project/research-lab/issues/147#issuecomment-3369017232) from that thread:

>unfair advantage

No such thing as "unfair" advantage, this is not an argument this is toddler reasoning.

>I mean that every person with a computer has the same weight in the network

What about one person buys 1000 CPUs in a cheap energy area and rents them out for AI or XMR mining, whichever pays better, essentially switch-mining between AI and XMR and making a killing. Economics of scale always wins.

>the cost to dominate a CPU based network is very high and broadly distributed

Only it is not. Pareto distribution rules everything, economics of scale rule everything. Who owns most of general-purpose compute? The few fully KYC’d companies like Google would have the compute to dominate CPU or GPU PoW mining. Last time I did the numbers: [5% of just 1 Google’s datacenter could replace 100% of XMR’s hashrate](https://x.com/bchautist/status/1854474918974382541). So, instead of Foundry, F2Pool, it’d be Google, Microsoft, Meta, Tesla…

Company | H100 GPU shipments (2023)
-- | --
Meta | 150,000
Microsoft | 150,000
Google | 50,000
Amazon | 50,000
Oracle | 50,000
Tencent | 50,000
CoreWeave | 40,000
Baidu | 30,000
Alibaba | 25,000
Lambda | 20,000
TikTok | 20,000
Tesla | 15,000

(source: Omdia Research)

If they ordered this much GPUs just in 2023, how many CPUs do you think they own? [Grok estimates just Google has 10M CPUs](https://x.com/i/grok/share/VC1i2XmUpQYp8JuqgT8Znu8ji). Monero's entire network hashrate is about ~100k CPUs, so 1% of Google.

>In my view, ASICs raise entry barriers and concentrate power in the hands of a few, if only those with capital and factories can mine, the network stops being free and becomes a digital oligopoly.

Just buy latest gen box for $1-2k, plug it in and mine, how hard is that? Oh, you need a few $k capital investment, that's a barrier? It's play money for people in developed nations, and you think some 2013 potato CPU can have "equal vote"? It is a joke when it comes to having influence on the network even though it can still technically mine something - it will still cost you electricity, something big players will have at better price than you, they will have CPUs at better price, and power at better price, and they can scale it. You can't wish away economics of scale and power of capital.

This is why sha256d is the best PoW algorithm, because it is a mature market, multiple producers, and ASIC hardware has penetrated wide and deep, even if you don't buy latest gen, you can still buy some 2nd hand that's good enough if you want a crypto-producing heater. It used to be centralized when first ASICs hit production, but it is not anymore, due to market forces. sha256d is as decentralized as PoW mining will ever get. Don't look at pool stats, look at where real hardware is located and who owns it.

# Discussion History
## zawy12 | 2025-10-06T12:17:45+00:00
Shas256d can't be used because miners have BTC as another source of income.  PoW security crucially depends on "non-repurposeability" which means there must not be a significant source of income for the CAPEX spent on mining other than the chain being protected. The miners must be assured their CAPEX investment will be wasted if they perform a 51% attack.  BCH I believe still uses sha256d and it had a 1-day simple moving average difficulty algorithm that responded faster than XMR's because it doesn't have a lag. Despite this improvement, incredible oscillations in the difficulty resulted from BTC miners jumping on and off when the difficulty jumped lower. The lag in XMR's will make it much worse which is why all the XMR alts had to switch from XMR's to mine. I got BCH to change their's to the ASERT algorithm and now they don't have a problem, but it's still not technically secure because miners have another source of income.  

The way a simple moving average "causes" oscillations is to imagine a tuning fork or metal bar. If you strike it, it has oscillations. To stop that from happening, you dampening. This is done in all improvements to the simple moving average by giving more weight in the adjustment to the more recent blocks (there are about 10 methods).  The BTC algorithm, by not being a moving adjustment, is far worse.  It survives because it satisfies the non-repurposeability requirement to a very high degree. Humorously, if you want to prove your coin is pretty secure, use the BTC algorithm.  It's still not very secure due to the CAPEX invested in the network is barely 1% of the U.S. military budget. The threat it imposes to the U.S. makes this a concern.

Merge mining might be an option, but I'm not sure it satisfies the non-repurposeability requirement.

The majority of hashrate must be directly, indirectly, accidentally, or unknowingly **colluding** to _protect_ the coin out of their own self-interest.  For example, if Child-P etc starts being a problem, the majority of BTC miners could collude to censor it out of selfishness if public opinion affects the exchange price which hurts the net present value of their CAPEX. They would then "collude" to ignore offending blocks. The fees for such content have to exceed their fear of losing their CAPEX. There is nothing in the PoW consensus mechanism that requires or depends on decentralization other than not having a single producer of the CAPEX (equipment) or being at a single location or otherwise easily subject to legislation (or other attack) that could target centralization.

To be clear, I'm not saying the difficulty algorithm can alleviate the 51% attacks that cause reorgs and it can alleviates only some aspects of selfish mining.  A better algorithm would only prevent oscillations from miners jumping on and off from other coin(s) which is often >51% of the hashrate, but they don't usually try to cause reorgs.  It only alleviates catastrophic oscillations that result in long delays between blocks.

## A60AB5450353F40E | 2025-10-09T10:37:25+00:00
Ok, DAA change would have to be part of the proposal to move to sha256d, so if Monero would switch to sha256d & ASERT + implement [your fixes](https://github.com/zawy12/difficulty-algorithms/issues/30), would they still be haunted by deep reorgs? How could Qubic still prey on Monero then?

DAA is effectively an AMM to meet supply of hashes (miners) with demand for hashes (blockchain networks). Miners don't create coins. Network creates the coins (or users offer theirs as fee), and then the network offers the coins in a blind bid for the next block's batch of hashes. Networks bid for hashes, and miners sell the hashes, it's a business relationship. The fact that network can't advance without the hashes, and the fact that miners can't get paid if network halts (they must still sell the coin for some real world currency in which they pay bills, and for that they need to make on-chain TXs, too, and the coin must hold value long enough for them to cash out) makes them more dependent on each other, but it is still fundamentally a business relationship between the network and the miners.

And as you say, if miners have only 1 buyer, then miners own survival depends on well-being of that 1 buyer. Network's survival doesn't depend on survival of the 1 seller, because ultimately the network can change the algo or move from PoW to PoS, but miners can't magically transmute their ASICs into other ASICs or a stake on the chain.

>Shas256d can't be used because miners have BTC as another source of income.

CPU & GPU algos have the entire AI industry as another source of income, but I think you're in agreement with me that ideally a coin would have ASICs all for itself.

But no coin has control over what other coins choose as algo. Imagine an alternative history where all the PoW alts kept picking sha256d. BTC's unique position depends on maintaining the belief that other coins should choose something else, or even aggressively attacking any coin that dares compete for the same hashes, but it will be the network that does the attack because they will feel their security is threatened. Why should miners attack the other network(s)? More demand for hashes, more profitable mining, right?

>The majority of hashrate must be directly, indirectly, accidentally, or unknowingly colluding to protect the coin out of their own self-interest.

I'd argue that ASIC hashrate would be colluding to protect ALL coins with their algo, because coins are the only buyer class of their product (hashes).

CPU/GPU algos, not so much, primary use of CPU/GPUs is something else - and crypto mining is just a way to make money with what would otherwise be idle time.

## zawy12 | 2025-10-09T11:35:39+00:00
Maybe I shouldn't say "Shas256d can't be used" because BCH with sha256d and ASERT is doing OK and they aren't using my timestamp fixes. They didn't want to add 3 more consensus changes.  My fixes in their case would only stop selfish mining attacks which I don't believe they have had.  A big bitcoin pool could do it at anytime. 

There's an EMA algorithm that's almost identical to ASERT but with a lot less code. The inventor of ASERT (Mark Lundeberg) actually likes it better but Jonathan Toomin was the force behind getting BCH to do ASERT and liked that ASERT was more precise.

Other coins using sha256d aren't a threat to bitcoin as long as the sum of such coins' hashrates doesn't get large compared to BTC.  But BTC miners could attack them to get coins at 1/2 the price (a 51% attack ignoring other blocks eventually lowers the difficulty to 1/2) or to do double spends. I guess they don't for medium-size coins because to be that large they could be identified and greatly hurt their reputation.  Also, such an attack could hurt the coin price, hurting their gains.

I don't know why merge mining didn't become a big thing.  Seems like every coin should have used it with sha256d and then bitcoin would be even more secure because it finances more network hashrate for bitcoin and protects the alts using it.  Alts kept abandoning it, but their reasons that I listed in one of my articles weren't fundamental in any way.

BTW there's a [new paper](https://x.com/hashdag/status/1933544298810622335) (and [explainer](https://x.com/DesheShai/status/1934583423122788454)) about using A.I. matrix multiplication as a PoW (PoUW = proof of useful work) that could make a coin more secure than bitcoin which has a huge security problem of having less than 1% or a military budget and only 10% an A.I. budget in CAPEX equipment that's securing Bitcoin. The PoUW researchers are working on a new coin in stealth to implement it and I think it will grow faster than Kaspa because they have the same people helping them on the inside. In effect, A.I. tasks are the primary source of income and compute that can simultaneously solve a PoW.  The coin is in effect merge-mined beneath those A.I. tasks. So the CAPEX securing the coin is the CAPEX of the A.I. budgets that implement the merge mine for extra income. They do have to spend a little extra ( I think O(log(n)) ) in compute to do the proofs. But imagine the consequences of the A.I. compute of the world financing itself with a coin it secures.  When you buy the coin, you're financing and investing in A.I. compute that can do any task.

## A60AB5450353F40E | 2025-10-09T12:35:45+00:00
>In effect, A.I. tasks are the primary source of income and compute that can simultaneously solve a PoW. The coin is in effect merge-mined beneath those A.I. tasks.

Wow this sounds promising, basically some batch of inference tasks that AI HW would be doing anyway would be usable as PoW? How do they avoid double proofs i.e. same work being recognized as PoW multiple times?

Edit: Grok found the answer: If a miner attempts to reuse the same proof π = (A, B, z) for a different σ (e.g., a different block header in the proposed blockchain), verification will fail because the recomputed noise, transcript, and z will differ. Even using the same A and B with a new σ requires a full recomputation due to the new noise, preventing shortcuts or reuse of prior work.

>They didn't want to add 3 more consensus changes.

We have the [CHIP process](https://gitlab.com/im_uname/cash-improvement-proposals/-/blob/master/CHIPs.md) now, we could still have those changes, but a little later. If you remember, I championed the [adaptive blocksize limit algorithm (ABLA) CHIP](https://gitlab.com/0353F40E/ebaa) and we activated that in '24, and now I'm set on building consensus for changing [BCH target block time to 1 minute](https://gitlab.com/0353F40E/fablous). After that, I want BCH to implement your time fixes, and it will be another CHIP unless I burn out on the 1-minute CHIP.

## joggingNjogging | 2025-10-14T20:42:35+00:00
I agree with @zawy12's  first reply about not switching to a mining algorithm that is already dominated by a different network. That said, the OP raises some valid concerns — we should really consider moving away from CPU mining. I'd love to hear the counter argument. It is alarming that a company like Google, Amazon, or Oracle can out-hash the network with a single digit percentage of their available compute the attack costing only technical resources and energy, which as I understand would be much "cheaper", than dominating an ASIC protected network

# Action History
- Created by: A60AB5450353F40E | 2025-10-05T17:50:46+00:00
