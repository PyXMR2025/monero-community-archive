---
title: Bolstering PoW to be Resistant to 51% Attacks, Censorship, Selfish Mining,
  and Rented Hashpower
source_url: https://github.com/monero-project/research-lab/issues/136
author: kayabaNerve
assignees: []
labels: []
created_at: '2025-08-08T20:13:38+00:00'
updated_at: '2025-08-16T19:02:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There has been a lot of discussions recently on bolstering our PoW security, due to the commentary of a mining pool which is running their own modified software to attempt to centralize the network under their hash power. I personally have created two issues on two different ways to secure the network (#134 #135). Given these issues have overlap, I wanted to create this meta-issue evaluating various strategies and linking to their dedicated issues.

| Idea | Requires a Hard-Fork | Requires a Soft-Fork | Allows Reducing the 10-block Lock | Risks |
| --- | --- | --- | --- | --- |
| ~~[TEE Block Templating](https://github.com/monero-project/research-lab/issues/134)~~ | ❌ | ✅ | Allows Reducing | Withdrawn due to Fundamental Issues |
| [Finality Layer](https://github.com/monero-project/research-lab/issues/135) | ✅ | ❌ | 10-block Lock -> Finality Lock | Can stall/split if 34% of stake is offline/malicious |
| Multiple Block Production Algorithms | ✅ | ❌ | No | Historically been a notable vector of attack |
| Local PoW | ✅ | ❌ | No | Centralizing in that all miners would need additional hardware |
| GPU PoW | ✅ | ❌ | No | Still risks attacks by GPU farms, which are more and more popular with LLM adoption by companies |
| ASIC PoW | ✅ | ❌ | No | Could centralize the network to ASIC manufacturers |
| Merge-Mining With a Larger Network | ✅ | ❌ | No | Makes us a vassal state to the glorious Bitcoin/Litecoin empire |
| Using a Larger Network _as_ our Finality Layer | ❌ | ✅ | Maybe | Makes us a vassal state to the glorious Bitcoin/Ethereum empire |
| Require Block's be Signed by the Miner's Key | ❌ | ✅ | No | 'Enforces' solo-mining, though there are still potential ways to avoid this 'enforcement'. |
| [Require Miner's Sample Historical Data](https://github.com/monero-project/research-lab/issues/98) | ✅ | ❌ | No | Promotes mining with a node (p2pool/solo) |
| Do Nothing/Improve the Existing Protocol's Efficiency | ❌ | ❌ | No | Risks 51% attacks/censorship/selfish mining as currently risked, albeit moving towards the optimal bounds by reducing practical latency which can more easily enable attacks |

---

Please note my definition of "Multiple Block Production Algorithms" is inclusive to both "RandomX + SHA-256d" proposals _and_ "RandomX + PoS" proposals. Both are alternative, distinct ways to produce a block with either accepted by the blockchain itself with likely independent difficulties. If someone has concrete proposals to contribute they'd like separately listed, I'll be happy to make the necessary edits.

---

"Local PoW" isn't something I made an issue for, yet is something I mentioned in MRL today. The idea would be to require _all_ RandomX miners _additionally_ have an ASIC connected. This would _limit_ the ability to competitively mine using rented hardware as _a physical device would have to be connected to the computer to be competitive_. We would want the ASIC to be:
- Widely manufactured, to not centralize to any manufacturer
- Affordable
- Not competitive to replicate in software
- Still acceptable to verify the results of in software
- Use a high amount of throughput with the host device such that USB-over-IP is not a potential solution

This would presumably mean after evaluating the RandomX VM, the final step is to additionally solve a SHA-256d (as widely manufactured, though potentially not for our use-case due to the input being of a distinct format) puzzle (with its own PoW nonce) where the preimage is so large, that the total hash rate _times_ the size of the preimage _is larger than_ 20 Gbps? Potentially as little as 2 Gbps? However much bandwidth that to rent a machine which performs X H/s, the cost of the bandwidth when using USB-overIP for those hashes exceeds the cost of the compute power itself, as to at least double (or whatever preferred factor) the total cost and no longer be competitive,

All to reduce the ability to rent hashpower over the internet/repurpose general purpose server farms.

---

I distinguished 'merge-mining' (simultaneously mining Bitcoin/Litecoin and Monero, inheriting the hash power of Bitcoin/Litecoin pools which simultaneously mine Monero, requiring a hard-fork to change the PoW algorithm) from simply using another network for finality (publishing block hashes onto Bitcoin/Ethereum, require running a Bitcoin/Ethereum node while running a Monero node, only syncing blocks if they're on the chain first committed to on Bitcoin/Ethereum). The latter technically only requires a soft-fork, though it does require whoever mines a Monero block commit to it on Bitcoin/Ethereum for it to be potentially considered the best-chain, and has issues in that a block could be committed to _without_ actually being available. We'd have to very carefully define a best-chain rule to cover all edge cases, or additionally use Bitcoin/Ethereum for data availability (Ethereum does sell blob storage to guarantee data is available for a brief duration of time, at a far cheaper rate than actual block space).

As an anecdote, the Serai network observes sufficiently-confirmed blocks and the Serai validators for that network come to consensus that X block exists with block number N with C confirmations. Once the Serai validators have that agreement, Serai considers that block finalized and will halt if a sufficiently deep re-org occurs. In that sense, the Serai network defines a finality layer _over every external network it interacts with_. I don't suggest having Monero follow the Serai validators, but it's interesting/humorous to me as an existing, _implemented_ definition of this exact _potential_ idea.

---

The idea to have a miner sign their own block (which was not my proposal, it was an idea I saw in MRL inherited from Wownero) was also proposed as having a miner sign their own block, as demonstrated by the first output for at least 10% of the block reward go to the signer. This would allow P2pool to exist as it currently does (albeit with reduced profit for pool miners who don't find the block), along with all other pools (again, albeit with reduced profit for pool miners who don't find the block), but further encouraging solo-mining.

My main concern is there are ways to avoid this 'enforcement', and I'm unsure if it can be properly tuned. Either it's so far in favor of solo-mining even P2Pool doesn't work, or it's so weak it doesn't really make a practical difference to any pool _is my concern_.

# Discussion History
## kayabaNerve | 2025-08-08T23:54:03+00:00
Note: It appears that preventing a 51% attack from censoring the blockchain _requires_ burning at least part of fees. Else, a malicious block producer with 51% of the blockchain can simply create its own full blocks, with its own transactions, paying the maximum fees, as it'll incur no actual cost. By burning part of the transaction fees, the attacker's XMR balance will go down if it pays higher fees than everyone else, to the degree it can no longer so censor transactions.

## tevador | 2025-08-09T10:10:44+00:00
It might be a good time to revisit https://github.com/monero-project/research-lab/issues/98

The purpose of that proposal was to make centralized pools more costly and attract more miners to p2pool, which could significantly improve the overall PoW security of the network.

## peaceAndHodl | 2025-08-09T12:00:49+00:00
IMO the path of abandoning some core values or worst compromising on them, in reaction to what is clearly a PSYOP, an information war, (and also probably a test they're making to evaluate what they need to take us down permanently - we have time to grow the hashrate), is the path they hope we take + it would show weakness.

we just need more miners = good marketing, good pr...
And to monero users first, I'm sure so many didn't even realize what's goin on and would set an old pc to mine on their box if they knew.

## worldwideward | 2025-08-09T13:16:46+00:00
@peaceAndHodl I agree, but there should be an incentive for new miners to join smaller pools instead of larger ones.

## hyc | 2025-08-09T13:54:24+00:00
I can see the potential for selfish mining, but "censorship" still isn't a realistic threat. If it were, that would mean anonymity had already been broken. A miner can certainly choose to preferentially mine its own transactions, but it has no way to select specific transactions of any other particular user, to exclude them. At worst it can attempt to choke the network by mining only empty blocks, i.e. excluding everyone's txns.

## preoncyber | 2025-08-09T14:09:22+00:00
In my mind, cpu POW can still be used but guard rails need to be in place. 

I’m not a mathematician but I’m envisioning a curve on a graph. 

The x is difficulty. Y is hash power. This indicates your probability of reward. Where peak is 10-15% of total network hash before dropping off. Hard cut off at 25%. 

This limits it to 4 pools at most. 

However, we need to incentivize the lone/tiny pools to be created. So, only 60% of total network rewards can go to pools making up +60% of network hash. This gives a reward for 4-6 (15-10% sized) pools being efficient in producing rewards. By doing a hard limit of 25% of total network hash, we must have a minimum of 3 pools to coordinate a 51% attack. 

The other 40% can be any number of pools. This creates 4 pools making max efficiency of block rewards for hash contributed at no more than 10% of network hash.

Combined, we have at most 8 pools. That’s 12.5% power per pool max. 

If an entity wanted to coordinate an attack, syncing these pools up will be difficult. 

## fluffypony | 2025-08-09T14:34:30+00:00
> In my mind, cpu POW can still be used but guard rails need to be in place.
> 
> I’m not a mathematician but I’m envisioning a curve on a graph.
> 
> The x is difficulty. Y is hash power. This indicates your probability of reward. Where peak is 10-15% of total network hash before dropping off. Hard cut off at 25%.
> 
> This limits it to 4 pools at most.
> 
> However, we need to incentivize the lone/tiny pools to be created. So, only 60% of total network rewards can go to pools making up +60% of network hash. This gives a reward for 4-6 (15-10% sized) pools being efficient in producing rewards. By doing a hard limit of 25% of total network hash, we must have a minimum of 3 pools to coordinate a 51% attack.
> 
> The other 40% can be any number of pools. This creates 4 pools making max efficiency of block rewards for hash contributed at no more than 10% of network hash.
> 
> Combined, we have at most 8 pools. That’s 12.5% power per pool max.
> 
> If an entity wanted to coordinate an attack, syncing these pools up will be difficult.

Literally impossible. Pools have NO OBLIGATION to identify themselves in block metadata, and even if they did, a pool could literally pretend to be another pool / multiple separate pools. We only know how much hashrate pools have because they self report + tag blocks.

## kayabaNerve | 2025-08-09T14:44:13+00:00
I've incorporated #98 into the table, which I quite like at a first revisit.

Friendly minder this issue is to discuss options and ensure we're making the best one, not to mandate any. I don't believe Monero is currently 51%d or practically censored. I believe PoW has limitations. The question is how we can improve Monero.

The reputation scheme seems to immediately fail to a Sybil attack and be irrelevant here.

## giaki3003 | 2025-08-09T14:50:46+00:00
https://github.com/monero-project/research-lab/issues/135 seems to be the most straightforward approach. Zcash is another privacy focused PoW chain looking to fix their network security model. I recently connected with Zooko/Nate on consensus and they're moving forward with the same idea over at Shielded labs, except its called a TFL (*Trailing finality layer*) - they modeled some work [here](https://github.com/Electric-Coin-Company/simtfl)
Re: Multiple Block Production Algorithms - this is a giant can of worms. From my understanding not a single project has ever been able to pull this off without some exploit or unintended advantage being given to certain actors. And its not really going to fix the issue indefinetely.
Everything else has the caveat of either turning XMR into a vassal of larger networks, or centralising to specific hw which has its own set of centralisation risks.
https://github.com/monero-project/research-lab/issues/98 is cool - but you won't get rid of the lock - and the lock (or equivalent*) removal seems to outweigh the 51% attack deterrence for most networks.

*I'm referring to how Zcash really wanted to slash confirmations exchanges, more than avoid 51%/centralisation issues

## Slixe | 2025-08-09T16:28:40+00:00
ASIC would be a no-go: fighting them for years to finally embrace them? Manufacturers are legal companies, where under law, can be forced to collaborate and actually implement a backdoor like AntBleed, allowing anyone to actually stop a whole network if really considered as a threat.
Also, this would actually add a "centralization/trust layer".

On the other hand, this would definitely prevent any botnet from mining efficiently.

Another solution would be maybe to tweak the RandomX algorithm to be more CPU/GPU balanced like it was with CryptoNote? We've tried to replicate this behavior on xelishashv2, but ASIC-like gpus (CMP cards) did take over due to the fast memory and low power.

I heard about EquiX, which could be potentially balanced between CPU/GPU, and allowing a near-instant verification of the actual PoW reducing greatly block verification time and preventing bad blocks spam as DDOS.

Having GPU along CPU would add more compatible devices to mine XMR efficiently by "lowering" the barrier for new miners. The more the algorithm is egalitarian, the better it would be.

Hybrid PoW/PoS with "Dash ChainLocks" is something I would consider to ensure no reorg can occurs after N confirmations.

Verge/Digibyte-like multi PoW algorithms is interesting in case ASIC is still envisaged, but (assuming) I don't like the fact some devices would just be on pause while others blocks are mined (my knowledge on this is really limited).

`Block's be Signed by the Miner's Key` could be used as a penality on block reward: if not signed, reduce the reward by like 5% to incentivize solo mining (only if it wasn't possible to bypass that issues for pools).

For merge mining, I'm not a fan because Monero should stay fully independant by not relying on bigger chains.

Just throwing random ideas / thoughts

## viktor4096 | 2025-08-09T17:47:31+00:00
@Slixe GPU-friendly PoW is not enticing... thanks to the AI craze, there are so many GPU power available (not to mention all the GPU mining farms that are practically sitting duck cuz GPU mining dead for a while now).

Block signed by miner's spendkey (aka "Wownero" route) is also not good. Wownero is a small coin, so these loopholes aren't exaggerated. For example, pools might require you submit collateral, ask you to use custom mining software, etc.

Personally, I'm voting for the finality layer solution. My proposal: make each finality layer participants expose their viewkey... if one starts acting maliciously, all their inputs/outputs will be marked as invalid. Any "validator" will have to have minimum 0.1-1 XMR in the wallet so that the cost isn't trivial.

## runatyr1 | 2025-08-09T18:33:24+00:00
@kayabaNerve has it been considered to raise the mining rewards? 

The current [0.6 XMR per 2-minute block equivalent to less than 1% annual](https://www.getmonero.org/resources/about/) inflation seems extremely low. If you buy mining hardware with current rewards it takes many years or will never recover the investment (see estimations below).  Thus, it seems it makes it easy to centralized actors like a government with spare money, to buy a lot of CPU and challenge the network. Most people will not be interested on spending their hard earned $3000-$5000 savings in something that will be never or veery slowly, recovered or just as an act of charity.

If we increased mining rewards by the rates below, inflation would stay at 4% or lower and make mining a worthwhile investment where the cost is recovered within a year.  A 4% or lower inflation still looks low for crypto and should not affect price action much but it would help to bring in more investors and diversify the hash power sources to reduce the chance of 51% attacks. 


- 5x rate of rewards 2025-2035 (if current inflation is 0.8%/annual then new would be 4%)
- 3x rate of rewards 2035-2055  (2.4% inflation)
- 2x rate forever (1.6% inflation)


This is an [estimation](https://www.coinwarz.com/mining/monero/calculator) for a $3000 rig with 2x AMD EPYC 7742 CPUs with [96.534 H/s hashpower](https://xmrig.com/benchmark/GiwVb) and 700W power usage, comparing cheap vs expensive electricity with current rewards, 3x or 5x rewards.

<img width="855" height="613" alt="Image" src="https://github.com/user-attachments/assets/16ece4fb-2c3f-4d4e-98a9-62e217593aaa" />

## fluffypony | 2025-08-09T18:38:58+00:00
> If we increased mining rewards by the rates below, inflation would stay at 4% or lower and make mining a worthwhile investment where the cost is recovered within a year. A 4% or lower inflation still looks low for crypto and should not affect price action much but it would help to bring in more investors and diversify the hash power sources to reduce the chance of 51% attacks.

Absolutely not, under any circumstances.

If Monero loses its social contract on the emission, then it is worthless and deserves to go to 0. Were it not for tail emission, the block reward would be even lower, and that would be fine.

## runatyr1 | 2025-08-09T18:59:23+00:00
@fluffypony I don't think the social contract is lost if it is something that the community votes as majority...  also if you left that reason out for a second, don't you think it makes sense that the network is at risk if investing for mining is pointless as it takes 10 years or it's impossible to recoup the cost of a mining rig?  

For me it seems that enables only people with spare money that wants to mine for charity, people with insignificant hashpower (mining with average desktop pc) or centralized actors with a lot of spare cash that want to attack the network (basically most governments in the world since XMR is the top privacy monetary system and it challenges fiat currency / CBDC). 

> "Were it not for tail emission, the block reward would be even lower, and that would be fine."

If we left the emission as it is and eventually the network is taken over then how is that fine? Don't you think that's a possible scenario if a centralized entity dumps a few million $ in hash power when the network wasn't strong enough due to lack of investor motivation and kill it?   I hope there are other solutions but it seems making the infra investment worthwhile for the average user, and thus decentralize more the network, could be one of multiple solutions. 

## fluffypony | 2025-08-09T19:04:48+00:00
> [@fluffypony](https://github.com/fluffypony) I don't think the social contract is lost if it is something that the community votes as majority... also if you left that reason out for a second, don't you think it makes sense that the network is at risk if investing for mining is pointless as it takes 10 years or it's impossible to recoup the cost of a mining rig?

If Bitcoin and Litecoin and a ton of other cryptocurrencies can survive (and even thrive) without changing their social contract, Monero can to.

If a bunch of posers with lies, fake hashrate, and a handful of empty blocks can force Monero to change it's social contract, then it has proven to be unable to resist a sustained nation state attack (which this very well might be).

The social contract stands, even if the social contract is absolutely terrible. This is a basic tenet of any good "money": predictability of supply over a macro timescale, typically measured in decades.

> If we left the emission as it is and eventually the network is taken over then how is that fine? Don't you think that's a possible scenario if a centralized entity dumps a few million $ in hash power when the network wasn't strong enough due to lack of investor motivation and kill it? I hope there are other solutions but it seems making the infra investment worthwhile for the average user, and thus decentralize more the network, could be one of multiple solutions.

If we change the social contract Monero has already lost. Simple as that.

What happens when another clown comes along and pulls a Lido (see how Lido affected Ethereum staking) in 5 years once you've increased the block reward? Do we just increase the block reward again, because a precedent has been set?

## kayabaNerve | 2025-08-09T19:14:16+00:00
Increasing the security budget via increasing emissions does not directly change the distribution of hash power. While the relative percentage of additional subsidies decrease, any additional subsidy will be greater than no subsidy.

I don't have as strong opinionation on the topic as fluffypony but I also don't care to personally entertain the idea as a potential solution.

## ffwf-hub | 2025-08-10T10:10:32+00:00
Seems to me the attack is merely someone has a worthless AI hype token and is incentivizing people to join their pool in order to receive said token. What's to prevent another pool from doing the same thing?  Create some ERC-20 token called "Super AI Computer" and print them out of thin air and offer them to anyone that joins your pool. Seems stupid, but so does this attack. You can't go changing the monetary policy, that'll kill the coin. I think changing to ASICs creates issues we've wanted to avoid. Why not fight fire with fire?

## mmgen | 2025-08-10T11:26:43+00:00
NACK for finality layer, as this introduces unnecessary complexity, especially if we want to preserve stakers’ anonymity.

NACK for merge mining, because the community will never accept Monero being subordinate to another coin.

NACK for toying with emission. Again, the community will never accept this, and for good reason.

ACK for local PoW. This proposal seems to have very few downsides (aside from the one mentioned above by @Slixe, which in my opinion is not fatal). Use SHA256 ASICs, since they’re the most widely available. Keep the difficulty low enough to permit use of second-hand hardware.

**During a long phase-in period, accept blocks both with and without the additional PoW, only make the difficulty higher for blocks without it.** This permits non-upgraded miners to continue mining, albeit with lower profitability. Gradually increase the difficulty penalty for non-ASIC blocks, incentivizing all miners to upgrade before the phase-in period expires.

Additional comment: Botnet mining is one of the main talking points of Monero’s critics, and getting rid of it will give XMR an enormous reputational boost.


## giaki3003 | 2025-08-10T11:39:07+00:00
> NACK for PoS, because it’s impossible to stake XMR and remain anonymous at the same time.

From my understanding, this is not true - anonymity assumptions do not change with or without an FL. Unless you have some way to substantiate this claim.

## MoneroArbo | 2025-08-10T13:15:31+00:00
While I agree that changing the mining rewards through emissions would be too contentious to entertain, I want to raise a couple of points.

First, the comparison to Bitcoin, etc. The reason we are in this situation is because the Monero emissions curve was so much steeper than the Bitcoin one. If we followed the Bitcoin emission curve more closely, the block reward right now would be more like 6 XMR instead of 0.6, literally 10x higher. Moreover, while there would be additional sell pressure from higher inflation, there would be fewer total coins in circulation so potentially an even higher price.

But that ship has, unfortunately, sailed. The only way to raise mining rewards at this point, which I would support as part of a solution, would be to raise the fees by 10x. Fees on blocks are often 0.05 or even 0.1 XMR, so 10x fees could potentially nearly double the overall mining rewards while punishing miners who mine empty blocks even further.

Re: "local PoW" via sha256 or scrypt ASICs, can we *really* use off the shelf Bitcoin / Litecoin miners for this purpose? Genuine question, as I'm not sure if the requirements would be too different.

## hyc | 2025-08-10T16:07:53+00:00
Remember that mining isn't supposed to be an "investment" - i.e., it's not meant to encourage people to put money in solely for the purpose of pulling even more money out in the future.

First and foremost, it is a *cost*. People decide if they benefit enough from it, in terms of securing a network that provides them a useful service, to justify their cost of participation. Looking at it from a profit-making perspective is just completely wrong.

If you buy a subscription to some media or journal, you're paying for the subscription service. Nobody expects the subscription to pay any monetary ROI in the future. 

Mining is supposed to be egalitarian. Most of the proposals listed above boil down to "everyone's equal but some people are more equal than others" - which is just nonsense that should be instantly dismissed.

A lot of people profited from mining in the early days of a coin, when emissions were high. That method of distributing new coins was essential for bootstrapping a newly launched coin. It really isn't and shouldn't be a factor in a mature, stably operating coin. Monero is well past that now.

If keeping a secure private financial network operating isn't in itself enough incentive for people to devote some personal resources to that expense, then no other incentive matters. If some single entity can break the network, that means not enough people cared to protect it, and so it's unsustainable anyway.

## MoneroArbo | 2025-08-10T16:18:50+00:00
I think that's an idealistic way to look at things. If we pretend people aren't going to follow economic incentives, or that enough people will *volunteer* hashrate to the network to secure it, it truly will be unsustainable.

If we want people to pay to maintain the network, the ways to do it are by inflation or by mandatory fees. Changing the inflation rate is out, so that leaves fees.

## fluffypony | 2025-08-10T17:10:03+00:00
> I think that's an idealistic way to look at things. If we pretend people aren't going to follow economic incentives, or that enough people will _volunteer_ hashrate to the network to secure it, it truly will be unsustainable.
> 
> If we want people to pay to maintain the network, the ways to do it are by inflation or by mandatory fees. Changing the inflation rate is out, so that leaves fees.

That's the Bitcoin NGU model. When we were debating the PoW change many years ago I argued in favour of ASICs, but it became clear that the broad consensus was for RandomX. This was to enable the average at-home Monero user to be able to mine. By choosing RandomX, the community as a whole opted out of the NGU model, and instead for the model @hyc describes: many small miners using their electricity / compute to support the network because it's good for them, not because it's profitable.

## fluffypony | 2025-08-10T17:14:31+00:00
> [@fluffypony](https://github.com/fluffypony) I don't think the social contract is lost if it is something that the community votes as majority... also if you left that reason out for a second, don't you think it makes sense that the network is at risk if investing for mining is pointless as it takes 10 years or it's impossible to recoup the cost of a mining rig?

Sorry I only saw this now - it absolutely is lost. One of the key things that makes Monero a "good money" is that the supply / emission was set in its earliest days, and will not change. It's the equivalent of Bitcoin's "there will only ever be 21m Bitcoin" - even if "the community votes as a majority" to modify that, it would already have destroyed all trust in Bitcoin.

Also, to add, voting is impossible in this - it's too easy to game votes. It would end up going down to miners to decide, and there would be a fork (ala Bitcoin and Bitcoin Cash), and that's not a great outcome for anyone.

## hyc | 2025-08-10T17:16:16+00:00
> I think that's an idealistic way to look at things. If we pretend people aren't going to follow economic incentives, or that enough people will _volunteer_ hashrate to the network to secure it, it truly will be unsustainable.
> 
> If we want people to pay to maintain the network, the ways to do it are by inflation or by mandatory fees. Changing the inflation rate is out, so that leaves fees.

Nobody subscribes to Netflix to make a profit.

## tevador | 2025-08-10T17:25:32+00:00
> raise the fees by 10x. Fees on blocks are often 0.05 or even 0.1 XMR, so 10x fees could potentially nearly double the overall mining rewards while punishing miners who mine empty blocks even further.

This is a good, simple incentive for miners not to mine empty blocks. I would support this.

It could be a relay rule, which would only require a software update.

## fluffypony | 2025-08-10T17:28:14+00:00
> This is a good, simple incentive for miners not to mine empty blocks. I would support this.
> 
> It could be a relay rule, which would only require a software update.

I'd support this - raising the fees would also ensure that spamming attacks are more expensive.

## donttracemebruh | 2025-08-10T17:44:16+00:00
What happens if/when Monero reaches a higher valuation and transacting is unnafordable to many people because fees have 10x'd? I think we should increase fees, but 10x seems excessive imo. 

## NotIshanSingh | 2025-08-10T18:16:10+00:00
One possible mitigation could be taking inspiration from Bitcoin’s FIBRE. Most large BTC pools use it, which is why empty-block mining isn’t a viable orphaning strategy there anymore.

## tevador | 2025-08-10T18:41:38+00:00
> What happens if/when Monero reaches a higher valuation and transacting is unnafordable to many people because fees have 10x'd? I think we should increase fees, but 10x seems excessive imo.

The minimum relay fee is just a node configuration parameter. If fees are deemed too high and we are not under attack, it can be easily reduced without affecting consensus.

## NotIshanSingh | 2025-08-10T22:04:46+00:00
> One possible mitigation could be taking inspiration from Bitcoin’s FIBRE. Most large BTC pools use it, which is why empty-block mining isn’t a viable orphaning strategy there anymore.

Following up on this, P2Pool already does this. It fits one block into a single network packet and sends it to many peers at once at less than 1 KiB packet according to Sech1. Any miner/pool can run a p2pool node connected to their xmr node. Plus supportxmr has their own block relay network.

Doing this would hurt Qubic's selfish mining strategy and get them a lower amount of blocks. It's a bandaid but worked for Bitcoin it can work for us. 

## viktor4096 | 2025-08-11T01:38:54+00:00
@NotIshanSingh What you're saying is basically better overall connectivity as an answer to Qubic's threat. Unfortunately, that's not how it works. With 51% hash rate, you can force drop blocks found by other miners irrespective of the network connectivity.

## NotIshanSingh | 2025-08-11T02:05:41+00:00
That was towards the selfish mining they are doing. My bad I should have been more clear.

## Astrodex-zz | 2025-08-11T11:06:59+00:00
Somewhere I saw a suggestion to use a random selection of 'reviewer' miners of a particular block to verify the block found. That way, even if someone had mined a 'false' block with 51+% hash rate it could not be verified by the random reviewers. The idea of this sounds good to me, but I of course konw nothing about the technicalities of any blockchain, and thus i don't konw if this would be a possible solution.

## viktor4096 | 2025-08-11T13:08:53+00:00
@Astrodex-zz what you're asking about is discussed in the "Finality Layer" proposition. In this proposal, some nodes will be responsible to decide which block will be accepted as canonical so that even if someone tries to reorg the chain, they can't. More on this [here](https://github.com/monero-project/research-lab/issues/135).

## j-berman | 2025-08-11T15:22:32+00:00
Higher fees would increase the honest miner incentive, which seems a rational goal to me.

On logistics: increasing the minimum relay fee without a fork could have two negative consequences:

1) wallets pointing to non-updated daemons could have their txs silently dropped.
2) anonymity puddles (txs constructed via old vs new daemons).

I think the former could have a significant impact on UX. To avoid the former, we could increase the base fee that updated nodes respond with, without raising the minimum relay fee required.

The latter seems unavoidable to me without a fork, but perhaps would be considered acceptable.

Regarding FCMP++ timeline (my own opinion): I would estimate we are still on target for public testnet by EOY, maybe early 2026. If we want 6 months of a smooth testnet before mainnet, then likely mainnet Q2/Q3 2026 at the earliest.

## yanmaani | 2025-08-11T18:35:06+00:00
What about enforcing, on a policy level, that block contents cannot differ too much from the mempool?

Schematically:
- As a node, I have some set of transactions in the mempool
- Some subset of these will be included, if I right now were to build a block
- When I see a block, I calculate the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between which transactions I would pick, and which transaction the miner of that block actually picked
- If the similarity is high, there is no problem
- If the similarity is low, either my mempool is totally broken, or the miner is selecting blocks in a way different from mine

A miner acting out of pure economic self-interest has an incentive to mine only on valid blocks, as this reduces his orphan rate (i.e. if he mines on a consensus-invalid block, he would see an orphan rate of 100%).

My proposal is that, if the similarity is too low, the node should consider the block as valid but "punish" it as though it belonged to a shorter chain, meaning that even nodes that misjudge this would eventually converge.

Practically: Each block that had (at time of receipt) a Jaccard dissimilarity to my mempool > *alpha* would see its chainwork reduced by (let's say) 50-70%, with some cap on the penalty equivalent to (let's say) 1-5 blocks' worth of PoW at the divergence point. The cut-off point for "too high dissimilarity" could be adjusted in configuration, or calculated based on some historical median of what the node saw. It might also be possible to make it linear in some range, so a block which is "on the edge" gets a punishment but a lower one.

To mitigate the current attack, *alpha* could be set to a pretty high value let's say 90%, which really shouldn't be an issue for even completely terribly configured nodes.

This is similar to the way that the network today checks that the block time is somewhat correct, which is necessary for PoW to even function. If memory serves right, nodes also make local decisions to prioritize the first seen block in the case of a tie. So it would not seem completely alien to use policy level for this. It seems also an attractive property that it can be implemented without even a soft fork.

## tevador | 2025-08-11T19:27:06+00:00
@yanmaani

What you are proposing is unverifiable. Mempool contents are not available to future blockchain verifiers., so you can't base chainwork on it.

The only thing that can be done using just local information is delaying a block a little bit. But if its PoW is valid a there are no other candidates, eventually you have to add it to the chain.

There is a selfish mining prevention strategy based on this, which compares local block arrival time to the block's timestamp, but I'm unsure if it works in practice. Described here: https://github.com/zawy12/difficulty-algorithms/issues/76#user-content-selfish

## yanmaani | 2025-08-11T19:57:58+00:00
@tevador 

Yes, my proposal is just to delay it, not to reject it entirely. During IBD, this would not be applied. Nodes do not need to agree on the exact value of chainwork, just (eventually) on the chaintip.

If the adversary has 40%, they can currently force 40% empty blocks at the cost only of fees. If this were added, such that they'd need a run of at least two blocks, they would only be able to produce 16% empty blocks, and they would also forego the block rewards from the orphaned (40 - 16)%. 51% attacks by attackers that control more than ~62% (1/φ) of the network would still be possible, however.

## ACK-J | 2025-08-11T22:02:01+00:00
> > raise the fees by 10x. Fees on blocks are often 0.05 or even 0.1 XMR, so 10x fees could potentially nearly double the overall mining rewards while punishing miners who mine empty blocks even further.
> 
> This is a good, simple incentive for miners not to mine empty blocks. I would support this.
> 
> It could be a relay rule, which would only require a software update.

10x fees may not be enough. They claim that mining qubic is 2x-3x more profitable overall. If I understand correctly, i'm not convinced that would be an effective solution.
https://qubic.org/blog-detail/why-qubic-is-now-the-top-profitable-coin-to-mine-in-2025 



## giaki3003 | 2025-08-12T09:08:01+00:00
> [@tevador](https://github.com/tevador)
> 
> Yes, my proposal is just to delay it, not to reject it entirely. During IBD, this would not be applied. Nodes do not need to agree on the exact value of chainwork, just (eventually) on the chaintip.
> 
> If the adversary has 40%, they can currently force 40% empty blocks at the cost only of fees. If this were added, such that they'd need a run of at least two blocks, they would only be able to produce 16% empty blocks, and they would also forego the block rewards from the orphaned (40 - 16)%. 51% attacks by attackers that control more than ~62% (1/φ) of the network would still be possible, however.

In the even of network connections dropping, mempools not being synchronised, and so on, the ruleset you are proposing would be extremely brittle. There is a reason why the mempool has been completely detached from any type of consensus and pairing it (even "only" after IBD) degrades the networks reliability. 

## moneromooo-monero | 2025-08-12T09:12:00+00:00
I think that's the point of the poster. If a block seems iffy from that calc, you continue mining on the previous block, on the assumption that most other nodes will also do so. Maybe it won't work out and you'll end up accepting the chain you found iffy, maybe not. But in the end, the fact it's not verifiable by a third party does not matter. It'll just create some "fluff" at the tip of the chain when viewing the network as a whole. Which is typically unwanted as it increases orphans, but may in this case (an assessment of fair tx selection) well be.
Might get into some trouble if tx propagation is not very fast over the network though, which is something we typically don't really care much about but which would become a lot more important here.


## giaki3003 | 2025-08-12T09:27:24+00:00
> I think that's the point of the poster. If a block seems iffy from that calc, you continue mining on the previous block, on the assumption that most other nodes will also do so. Maybe it won't work out and you'll end up accepting the chain you found iffy, maybe not. But in the end, the fact it's not verifiable by a third party does not matter. It'll just create some "fluff" at the tip of the chain when viewing the network as a whole. Which is typically unwanted as it increases orphans, but may in this case (an assessment of fair tx selection) well be. Might get into some trouble if tx propagation is not very fast over the network though, which is something we typically don't really care much about but which would become a lot more important here.

PoW is built to be a very low overhead, low synchronicity protocol. The surface level for an attack based off this naive Jaccard diff algo is pretty high with these two properties in mind.
Just as a quick thought, an attacker can withhold *enough of his own transactions and build only his block. When he gets a block, he can then flood the mempool with his own transactions. His block will then be valid for the subset of nodes which receive the transaction flood. He can time this to cause network splits and make more money by splitting honest miners. He won't lose a cent as he pays himself with the large amount of transactions he generates. This would be even more amplified due to network propagation effects and in effect can only be mitigated with some uncle system (which is something higher synchronicity/overhead protocols usually need, not Monero PoW)

*enough to skew the *alpha* in his favour

## kayabaNerve | 2025-08-12T10:10:30+00:00
Then the issue with preferring a chain with less work (a proposal distinct from similarity to the mempool), attempting to 'rescue' an orphaned chain, is you can trap miners on an worse chain such that they're no longer even mining the Monero blockchain.

It'd be like selfish mining, where the attacker withholds the best chain, except now nodes are on-purposely ignoring the published best chain.

## mmgen | 2025-08-12T10:13:00+00:00
Local PoW is hands down the best proposal, in my view.

## Gingeropolous | 2025-08-12T11:50:46+00:00
> That's the Bitcoin NGU model. When we were debating the PoW change many years ago I argued in favour of ASICs, but it became clear that the broad consensus was for RandomX. This was to enable the average at-home Monero user to be able to mine. By choosing RandomX, the community as a whole opted out of the NGU model,

@fluffypony , can you expand on this? It seems that you are saying ASICS = NGU... but from my time watching this space, there are plenty of cryptocurrencies that got ASICd that didn't get that NGU magic. 

## yanmaani | 2025-08-12T15:41:26+00:00
> [...] the ruleset you are proposing would be extremely brittle. [...] pairing [the mempool to consensus] degrades the networks reliability.

Sure; it's a trade-off. I agree it would be a bit more brittle (in the sense of consensus stability) than the current rule set, but the question is *how brittle*.

> an attacker can withhold *enough of his own transactions and build only his block. When he gets a block, he can then flood the mempool with his own transactions. [...] He can time this to cause network splits and make more money by splitting honest miners.

That is a possible attack. I can see a simple mitigation, though. Instead of calculating `Jaccard(choose_tx(my_mempool), block_txns)`, it could calculate `Jaccard(choose_tx(my_mempool_as_of_5_seconds_ago), block_txns)`.

This would penalize miners a little bit for including new transactions, but assuming transactions arrive at an even rate it shouldn't be too bad. And abusing this seems a lot harder, since it would require you to publish actual transactions involving real money and transaction fees to the mempool.

>Then the issue with preferring a chain with less work (a proposal distinct from similarity to the mempool), attempting to 'rescue' an orphaned chain, is you can trap miners on an worse chain such that they're no longer even mining the Monero blockchain.

In the worst case, miners could indeed be "trapped", but they would eventually converge again.

>It'd be like selfish mining, where the attacker withholds the best chain, except now nodes are on-purposely ignoring the published best chain.

Can you elaborate a bit on the attack? In selfish mining, I understand the assumption to be that the attacking pool can control the flow of data in the P2P network to get nodes to mine on their block, despite publishing it later. But in this case, the pool alone would be the ones mining on their chain, putting them at a disadvantage.

What am I missing?

## peaceAndHodl | 2025-08-12T15:56:07+00:00
i might get bashed hard for that, especially if it is not even feasible, it's ok : 

to force mining to go through p2pool only.

And just to be sure with p2pool in selfish mode.

(or is it possible to mess with blocks through p2pool as well ?)

## deficruncher | 2025-08-12T15:56:24+00:00
Additional idea that uses gpu/asic/local-pow ideas:

**Allow using either of CPU/GPU/ASIC or either of CPU/ASIC POW to mine blocks. Each having its own difficulty tracked separately. Additionally introduce some rebalancing penalty that tries to balance different POW types, so that mined blocks are evenly split between different types of POW.** To be clear -> blocks are mined with EITHER of the POW types (not all at once).

For example if last mined block was CPU-one, each successive CPU blocks have difficulty multiplied by 1.25 until ASIC and GPU blocks are mined, after which this additional penalty is reset (or multiplicatively decayed back to neutral 1). Analogous logic applied to all POW-modalities.

That way adversary need to 51% of all POW-modalities to attack chain which makes it unlikely to achieve. 

Lets say someone achieves 51% CPU POW. Due to exponentially-scaling of same-successive-POW penalty, either GPU or ASIC POW block break long-chains of someone who has 51% CPU-only power making it impossible to make long reorgs for such entity.

**This solution is easier to transition to than local-POW. ASIC/GPU entities can plug into the network independently in their own rate, and current CPU-only setups can keep going.** Local-POW requires all miners to have additional hardware. This solution make it optional. Miner can obtain additional ASIC devices to diversify/boost their mining. Imho this idea is a straight-up improvement over local-POW idea.

## redsh4de | 2025-08-12T16:11:56+00:00
Voting for the finality-layer solution #135, as despite the potential complexity, a BFT finality layer both bolsters our quite small security budget by adding a layer of security backed by XMR itself, and **DRASTICALLY** improves UX by eliminating the dreaded 10-block lock. We would be effectively killing two birds with one stone, while diversifying the security model.

Considering how unprofitable Monero is to mine and the resulting relatively low hashpower, one entity managed amass enough hashrate for executing deep reorgs, through offering altcoin incentives. We have to consider about what a state-level adversary could do.

I reckon choosing the path that could render these kinds of hashrate attacks effectively impossible even for state-level adversaries that control much, much larger amount of CPU hardware than Qtip, is the only way forward here for long-term health of the project, i.e. thinking about the worst case scenario, and choosing the most resistant cure for that.

## fluffypony | 2025-08-12T16:14:34+00:00
> [@fluffypony](https://github.com/fluffypony) , can you expand on this? It seems that you are saying ASICS = NGU... but from my time watching this space, there are plenty of cryptocurrencies that got ASICd that didn't get that NGU magic.

No no - it's not that ASICs create NGU, it's that in an NGU-style economic system (fixed supply) it might make sense for large-scale miners to acquire lots and lots of specialized single-purpose equipment, because they're actually being speculative and hoping for future economic reward. The opposite (using general-purpose equipment for mining) instead focuses less on speculative potential, and more on each miner having a specific reason / rationale for mining.

## giaki3003 | 2025-08-12T16:18:50+00:00
> That is a possible attack. I can see a simple mitigation, though. Instead of calculating `Jaccard(choose_tx(my_mempool), block_txns)`, it could calculate `Jaccard(choose_tx(my_mempool_as_of_5_seconds_ago), block_txns)`.
> 
> This would penalize miners a little bit for including new transactions, but assuming transactions arrive at an even rate it shouldn't be too bad. And abusing this seems a lot harder, since it would require you to publish actual transactions involving real money and transaction fees to the mempool.

I don't really understand how this can help mitigate the issue I described - if there is a timed delay for when the mempool snapshot is chosen, the attacker only has more of an incentive to hit the exact delay. Due to block propagation, if he were to release the flood of txes exactly 5 seconds early, some nodes would validate the block, while other would be stuck on a fork due to the network delay. This itself would be enough to cause a split between "closer" and "further" nodes. 

On top of this, the delayed approach does not change any of the assumptions I made previously. If the delay is longer, the attacker only has to make more transactions to keep the alpha skewed in his favour. The block he mines only has to contain global transactions (which everyone sees) plus his early flood (which only he can see for the larger part of the mining process, until the 5s delay triggers). This gives every single miner no possibility to mine a valid block if they have not seen the large flood. For all intents and purposes, a `choose_tx(my_mempool_as_of_5_seconds_ago)` approach seems to make things *worse*, and not better.

## kayabaNerve | 2025-08-12T16:50:30+00:00
@yanmaani You're missing how honest miners get trapped on a worse blockchain for an even longer amount of time, extending for how long they're not mining on the current best chain. It amplifies how bad selfish mining already is.

@peaceAndHodl p2pool can be disturbed as Monero can be.

@deficruncher That's the multi-PoW idea already present in the table. It's historically been a very notable attack vector on other projects which have tried. It somewhat just gives the attacker choice in how they try to achieve 51%.

## mmgen | 2025-08-12T17:12:07+00:00
>  Local-POW requires all miners to have additional hardware. This solution make it optional.

Read the thread more carefully. The  modification of local PoW I propose above also makes the additional hardware optional, during a phase-in period.


## deficruncher | 2025-08-12T17:34:24+00:00
> [@deficruncher](https://github.com/deficruncher) That's the multi-PoW idea already present in the table. It's historically been a very notable attack vector on other projects which have tried. It somewhat just gives the attacker choice in how they try to achieve 51%.

Can you provide some more detailed specification of that solution? From your response it seems like my idea is not the same. Specifically:

> It somewhat just gives the attacker choice in how they try to achieve 51%.

Not at all. Note the 'balancing penalty' in my proposal. You cannot pick one modality and 51% it, because at some point the exponentially growing penalty will dominate you and make it so much less POW from other modality will easily win out. An attacker needs to 51% all POW modalities due to balancing penalty.

## kayabaNerve | 2025-08-12T17:51:03+00:00
Except even with your proposed balancing (which would somewhat inherently exist simply by independent difficulties), an attacker can pay more into one candidate (including the penalty) to avoid having to require as much PoW on another candidate.

You're correct in that my line item was a bucket for this entire train of thought, not a complete, fully-detailed proposal like you're moving towards.

## deficruncher | 2025-08-12T17:59:17+00:00
> an attacker can pay more into one candidate (including the penalty) to avoid having to require as much PoW on another candidate.

That's why POW-type-balancing penalty scales up exponentially making such an attempt infeasible. 

Also I am not sure what you mean by 'candidate'? From the context I assume that by 'candidate' you mean 'POW-type' (so either CPU/GPU/ASIC).

> which would somewhat inherently exist simply by independent difficulties, 

Different thing. Independent difficulties are for responding to new hash-power joining the network. Rebalancing POW-type penalty is about, well, rebalancing blocks in short-term.

## giaki3003 | 2025-08-12T18:10:46+00:00
Re: multi-pow im dropping this here as it explains the difficulties of a multi pow approach on many levels https://github.com/zawy12/difficulty-algorithms/issues/69

## deficruncher | 2025-08-12T18:17:12+00:00
> Re: multi-pow im dropping this here as it explains the difficulties of a multi pow approach on many levels [zawy12/difficulty-algorithms#69](https://github.com/zawy12/difficulty-algorithms/issues/69)

Well, it lacks the idea of 'rebalancing penalty' I proposed which makes all the difference.

The closest to that in their post is:

> In simple chain-work calculations, multi-POWs are only as secure as the least-secure ("rentable") POW **if there is no limit on the number of blocks in a row a given POW can solve.**

Exponentialy-scaling penalty for same-type-of-POW puts an effective upper limit on how many same-type-POW can be in a row.

## josephSummerhays17 | 2025-08-12T18:19:41+00:00
@kayabaNerve, I think deficruncher is right on this one. It might be more obvious if we take an extreme example. The "exponential growth" could be set so ridiculously high that it becomes turn taking; cpu miners will take first block, GPU miners will take second block, ASIC, miners will take the third block.

In this extreme example, no one can build a block chain longer than 2 in secret without a majority of all 3 mining groups.

## deficruncher | 2025-08-12T18:22:30+00:00

> it becomes turn taking; cpu miners will take first block, GPU miners will take second block, ASIC, miners will take the third block.

That was my first idea to be honest, but I discarded it because it would mean that CPU-only miners would need to wait for other POW-type-block after they mined a block. Exponential scaling makes it so they can still work on next block without much hurdle. Exponential scaling hits hard after few same-POW-type blocks, but is relatively easy at the start.

## giaki3003 | 2025-08-12T18:27:01+00:00
What I think we should also consider is the amount of networks currently live and running a finality network vs the amount of networks which successfully implemented multi-pow 

## josephSummerhays17 | 2025-08-12T18:41:34+00:00
I don't think it really matters how many networks have successfully implemented multi-pow. I mean, I get the value of a battle tested algorithm. But if there is even one battle tested multi-pow, it doesn't matter how many other people did it wrong. If there are _no_ battle tested POW, but there's an obvious flaw that @deficruncher is addressing, then we ought to give it a chance to get battle tested, even if we work concurrently on a finality layer.

But I must admit, I like @deficruncher suggestion less so than I just dislike the finality layer, which seems to be the best option so far. I hate a finality layer managed by some other chain, and I hate a finality layer we manage but with PoS. perhaps it's because I just don't understand it enough. But anonymous coin ownership with proof of stake?! how do you distribute? How do you know someone's not getting near 51% of the stake?

## josephSummerhays17 | 2025-08-12T18:44:44+00:00
@deficruncher , your suggestion seems to be more similar to https://github.com/zawy12/difficulty-algorithms/issues/69 than you realize. Not exponential, but still effective.

>**Increased Security Against Double Spending**
In simple chain-work calculations, multi-POWs are only as secure as the least-secure ("rentable") POW if there is no limit on the number of blocks in a row a given POW can solve. To alleviate this, Verge, Raven, Pigeon, and maybe several others have a requirement to switch POW. It's interesting that Multishield reduces the vulnerability if there is no requirement. This isn't simple to describe and explain, but here goes. **In short, his chain work goes up only as a root of his hashrate dominance while his difficulty is going up "linearly" with the difficulty algorithm calculation. To say it another way multishield gives an advantage to chains (or POWs) that do not suddenly increase (or decrease) the hashrate for one (or a subset) of the POWs**.

## josephSummerhays17 | 2025-08-12T18:54:26+00:00
> **DRASTICALLY** improves UX by eliminating the dreaded 10-block lock.

@redsh4de It seems to me a finality layer will take just as long to implement and merge as FCMP++, which already solves this problem, so it seems like a moot point.

## bassyuan | 2025-08-13T04:08:23+00:00
我认为，矿工想单独挖矿 需要质押少量的门罗币，如果需要加入私有矿池挖矿就要根据矿池的比重，质押增加指数级增长的门罗币。这样促进门罗币矿工单独挖矿。

## prfd666 | 2025-08-13T04:45:37+00:00
Q*’s 51% Attack Resembles a Bribery Attack, Not a Traditional Rent/Purchase Attack

Hello Monero Community,
Regarding the recent (August 12, 2025) so-called 51% attack demonstration by Q* on the Monero network, I’d like to highlight that this event is better characterized as a bribery attack rather than a traditional 51% attack involving rented or purchased hashrate. Distinguishing these attack types is crucial for understanding the incident and developing effective countermeasures.
Background
Unlike traditional attacks that rely on renting hashrate (e.g., via NiceHash) or purchasing dedicated hardware, Q* just leveraged its AI-driven network (Proof of Useful Work, PoUW) to incentivize existing Monero miners to switch to its pool, effectively “bribing” them to redirect their hashrate.

Bribery Attack vs. Traditional Rent/Purchase Attack
1. Traditional 51% Attack (Rent/Purchase):

- Mechanism: Attackers rent hashrate from markets (e.g., NiceHash) or purchase hardware (CPUs/GPUs). Attackers need add additional capacity.

- Cost: For Monero’s hashrate (4-5 GH/s) and daily security budget ($100,000 USD), renting 51% hashrate could cost tens of thousands USD/day, sustained over time.

- Characteristics: Requires external resources, limited by market availability and hardware costs.

- Example: The 2018 Bitcoin Gold 51% attack, where attackers rented hashrate for double-spending.

2. Bribery Attack (Q*s Approach):

- Mechanism: Attackers offer incentives (e.g., additional rewards besides mining XMR) to persuade existing miners to join their pool, redirecting hashrate without adding new capacity.

- Cost: as long as there is a marginal increase in reward, such as 10%, miners have a motivation to switch to the attacker’s mining pool to mine. If the threshold is 51%. The cost is 100,000*51%*10%=5,100 USD /day, far blow traditional attack cost.

- Characteristics: Relies on miners’ profit-driven behavior, highly efficient, and harder to detect as it leverages existing network resources.

Why the Distinction Matters

- Different Threat Model: Traditional attacks are constrained by additional capacity, hardware markets and costs, while bribery attacks exploit internal miner behavior, making them stealthier and potentially cheaper.

- Implications for Defense: Mitigating traditional attacks involves increasing hashrate thresholds or monitoring rental markets. Bribery attacks require strategies like decentralizing mining pools or detecting sudden miner migrations.


I’m not an expert in hardware mining algorithms, but based on my limited understanding, introducing a finality layer seems to be one way to counter bribery attacks, as practiced by other cryptos. I don’t fully grasp the other methods Luke mentioned, but if my suggestion makes sense, I hope the community will consider this bribery attack threat when evaluating algorithm.

## prfd666 | 2025-08-13T05:02:11+00:00
Another Risk: Shorting + 51% Attack in Pure PoW Systems
A pure PoW system, where security relies entirely on miners’ computational power and economic incentives (block rewards + fees), is vulnerable to attacks if an entity can control over 50% of the hashrate. this scenario adds a financial dimension:
•  Mechanism: An attacker shorts the cryptocurrency (e.g., Bitcoin or Monero) in the derivatives market (futures, perpetual, or options), betting on a price drop. They then execute a 51% attack (bribery or traditional) to disrupt the network—e.g., through double-spending, chain reorganization, or transaction censorship—causing loss of trust and a price crash. The attacker profits from the short position, potentially offsetting or exceeding the attack’s cost.
•  Why PoW is Vulnerable: Pure PoW lacks a finality layer (unlike PoS or hybrid systems with checkpoints or slashing), meaning blocks can be reorganized if an attacker controls sufficient hashrate. This malleability enables attacks that erode user confidence, making price manipulation via shorting more effective.

## redsh4de | 2025-08-13T08:11:36+00:00
> FCMP++, which already solves this problem, so it seems like a moot point.

@josephSummerhays17 The 10-block lock in Monero's case serves two purposes:
- Reorg protection - ensuring transaction **security** against chain rollbacks.
- Plausible deniability for ring signatures - protecting **privacy** by preventing immediate spends from revealing linkability clues.

What FCMP++ addresses is the privacy side by removing the need to delay spends for plausible deniability. However, it does not address the security side - the risk of deep reorgs if an attacker temporarily controls large amounts of hashrate, which is why even after FCMP++ it would still make sense to keep the lock for security reasons (see comment on [#95](https://github.com/monero-project/research-lab/issues/95#issuecomment-3105667189))

A finality layer directly tackles that second, equally critical security issue: it makes deep reorgs both economically and technically infeasible, providing true settlement assurance. In other words, FCMP++ removes one reason for keeping the lock, while finality removes the need for reorg-based security delays in the first place - which in itself would be massive for the usability of Monero.

My proposal for a plan of action would be as follows:
| Timeline | Action | Effect |
|--------|--------|--------|
| Short-term | Raise default fees by 10x to boost miner incentives (doesn't require any consensus changes) | Increased miner incentives, potential influx of hashrate, improved network security |
| Mid-term | Implement a easier to execute solution, personal preference being #98 as it promotes P2Pool adoption | Higher resistance to single-party reorg attacks, increased full node count, faster deployment than a FL |
| Long-term | After FCMP++, shift focus toward implementing a BFT finality layer that agrees on a freshly mined block, adding it to the chain | Strong reorg prevention, removal of 10-block lock, resolves major Monero UX issue |

## tevador | 2025-08-13T11:46:49+00:00
I agree with the timeline proposed by @redsh4de.

Some notes about the short-term mitigation:

Within a few weeks, we can do a Monero point release which will include a new command that raises the minimum relay feerate ~~or possibly the minimum feerate for a tx to be included in a block template~~.

With the cooperation of major pools, this would enable a fast response to:

* a selfish miner who mines empty blocks
* a spammer, who floods the network with transactions

Against the current malicious pool, raising the overall mining rewards through fees will have two positive effects:

1. It will reduce the perceived profit difference between honest pools and the malicious pool, disincentivizing miners from joining the malicious pool.
2. If the malicious pool continues mining empty blocks, the additional fees will be collected by honest pools, which will mitigate their revenue loss due to orphaned blocks.

For the current situation, I would propose raising the minimum feerate by a factor of 16. That would mean the total fees for a 300 KB block would be at least 0.1 XMR. This would raise the minimum fee for a 2/2 transaction to about $0.2, which is still quite cheap.

> On logistics: increasing the minimum relay fee without a fork could have two negative consequences:
>
>   1. wallets pointing to non-updated daemons could have their txs silently dropped.
>   2. anonymity puddles (txs constructed via old vs new daemons).
>
> I think the former could have a significant impact on UX. To avoid the former, we could increase the base fee that updated nodes respond with, without raising the minimum relay fee required.
>
> The latter seems unavoidable to me without a fork, but perhaps would be considered acceptable.

Without actually raising the minimum feerate, there would be no incentive for users to use the higher fee (apart from altruism). So I don't think just updating the recommended fee is sufficient (especially against a spam attack). Yes, UX would be impacted, but this is for situations when UX is impacted anyways due to an ongoing attack.

As for anonymity puddles, I was thinking that the adjusted feerate could be set to match an existing priority multiplier, which means users with old software could still submit transactions if they used a higher tx priority level and the fee would match a lower priority level of updated software.


## Gingeropolous | 2025-08-13T12:31:30+00:00
the fees make sense, and I've always been a fan of the historical data thing (#98). I'll be interested to see what kind of finality layer we can come up with that doesn't introduce centralization or permission into the protocol.

All that said, I think the recent (perhaps ongoing) attack highlights the impact of rented hashpower on the whole economics of PoW regarding network security. Before rented hashpower was a thing, we could assume that to mount an attack on a PoW network, you needed to invest in infrastructure - something that takes time, effort, and funds.  With rented hashpower, now all thats needed is funds. 

This brings forward two notions that I think should be the focus of any bolstering that may be implemented. 

Notion 1 - disincentivizing pooled mining may be beneficial (or in general, disincentivizing light client mining). I think 98 moves in this direction fairly well. I don't know if its enough to prevent the 182 MH/s of mining currently available on miningrigrentals, or to prevent someone with hundreds of thousands of idle CPU threads in a GPU datacenter from mounting such an attack. In the case of the second, the evil sysadmin could just spin up their own node. But in general, the more costly it is to launch instantaenous megascale hashrate, the better. 

Notion 2. the existing network of miners leading up to an attack can be "trusted". Perhaps this gets to the whole finality layer thing. But if the current (and most likely) attacker can mainly just spin up 20-40% of the existing networks hashrate in an instant, I feel there's gotta be a way for the existing hashrate to somehow say "hey these new blocks are coming in fast and they are coming in from someone new, and maybe they shouldn't be trusted". Granted, this looks like permission. But if its somehow decentralized permission is it acceptable? I mean, the protocol essentially permits behavior based on protocol adherence. Anyhoo, I digress. I imagine some secondary chain with a rolling window of some attestation by the miners, such that when a new block comes in, the protocol can check whether the block came from an existing miner. If it did, then the protocol will prefer this block when compared to another that attempts to fill the current tip within a given timeframe.  If the block came from a new miner, the protocol gets a little wary and says "this block might be OK and it can fill the next spot". And if a chain of 6 blocks, say, comes from a new miner, he protocol can go "uh yeah bud you're not welcome here". I mean really its the later case that would be the most binary and implementable. There's probably few, if any, rational reasons for honest miners to selfishly mine 6 blocks and then dump them on the network. Of course, we have the case of network-split inducing chainsplits and subsequent reorgs, but details....
 

Yes, this doesn't prevent the attack, it just forces the attacker to expend more resources, which is (I think) the only thing we can really do in a decentralized permissionless system. 

## Gingeropolous | 2025-08-13T12:40:23+00:00
perhaps its a forward permission thing. E.g., when you mine a monero block, you get to insert some data into something somewhere that enables your future blocks to have less friction when trying to get into chaintip. 

## kayabaNerve | 2025-08-13T14:03:20+00:00
@bassyuan That doesn't immediately work as pools can simply claim every individual miner in the pool is a solo-miner. The network can't detect pools.

@prfd666 Please don't spam this issue with LLM 'analysis'.

## kayabaNerve | 2025-08-13T14:25:34+00:00
My biggest concern re: #98 is if the entirety of the malicious pool runs local Monero nodes (as feasible if only a few entities actually contribute hash power) yet a lower percentage of miners contributing to other pools migrate. This could actually _increase_ the percentage the malicious pool has by _decreasing_ the overall hash power. I worry the network, as of right now, is too unstable to endorse such a change.

## josephSummerhays17 | 2025-08-13T14:47:04+00:00
> * Reorg protection - ensuring transaction **security** against chain rollbacks.
> 
>     * Plausible deniability for ring signatures - protecting **privacy** by preventing immediate spends from revealing linkability clues.
> 
> 
> What FCMP++ addresses is the privacy side by removing the need to delay spends for plausible deniability. However, it does not address the security side - the risk of deep reorgs if an attacker temporarily controls large amounts of hashrate, which is why even after FCMP++ it would still make sense to keep the lock for security reasons (see comment on [#95](https://github.com/monero-project/research-lab/issues/95#issuecomment-3105667189))

I didn't realize this. (I'm a dev interested in monero, but not a monero dev; there are definitely some gaps in my knowledge. Thanks for being patient with me).

But knowing this now doesn't change my mind on the topic. I object to the idea of enforcing reorg protection. Smaller transactions are less likely to be the target of a double spend, so users should feel free to accept the amount of risk they want. (on the flip side, users already are free to ignore the 10 conf requirement and wait for a whole 20).

IF there MUST be an enforced reorg protection, it should be scheduled based on the size of the transaction (which will be difficult to do because the network isn't aware of its own price level.)

## josephSummerhays17 | 2025-08-13T14:59:14+00:00
> My biggest concern re: [#98](https://github.com/monero-project/research-lab/issues/98) is if the entirety of the malicious pool runs local Monero nodes (as feasible if only a few entities actually contribute hash power) yet a lower percentage of miners contributing to other pools migrate. This could actually _increase_ the percentage the malicious pool has by _decreasing_ the overall hash power. I worry the network, as of right now, is too unstable to endorse such a change.

It's not clear to me why this would hurt mining pools (with the exception of mining pools that pay out in a different crypto currency, like the merge mining monstrocity).

If it's required that 10% of the block reward goes to the miner, then the expected reward for mining in a pool is the same, and the present valued expected reward for mining in a pool is _almost_ the exact same (if the present valued expected reward under the current regime is say, 1 XMR, then the present valued reward under the new regime is .9 xmr + time discounted .1xmr. For small miners with long expected wait times maybe a few years, at a 12% interest rate, this may be say .05 xmr. I haven't actually done the math, I'm just guesstimating).

But if this is a concern, then make the block reward that must go to the miner a parameter that increases over time. If pools start panicking at 3% or something, then we back off. Even giving individual miners 3% of the rewards will seriously curtail the power of merge mining pools.

But I see the primary purpose of this proposal not as a way to push people out of pools, but more as a way to discourage pools that payout in some crypto _other than_ monero, which is part of the tactic in the most recent attack. If as a rule, a miner _must_ recieve some monero, regardless of what the pool wants, that's a win.

## josephSummerhays17 | 2025-08-13T15:14:08+00:00
>All that said, I think the recent (perhaps ongoing) attack highlights the impact of rented hashpower on the whole economics of PoW regarding network security. Before rented hashpower was a thing, we could assume that to mount an attack on a PoW network, you needed to invest in infrastructure - something that takes time, effort, and funds. With rented hashpower, now all thats needed is funds.

This cuts both ways. Defenders also only need funds. And since the market for monero mining rigs is not perfectly elastic, defenders renting rigs are pulling hash directly from the opposition.

## techmetx11 | 2025-08-13T15:44:15+00:00
The finality layer could be a modified form of PoS, where you can get a stake on the blocks you've mined (this can be tied to the P2Pool coinbase transactions too) but if you send over any rewarded XMR, it will be deducted from the amount of stakes you currently have.

This would mean: 
1) the richest people in Monero aren't just gonna get a ton of stakes over others
2) centralized pools would be the minority in the the list of validators, unless they heavily increase their fees or refuse to pay out miners
3) this would benefit independent miners, big or small, over pools

## tevador | 2025-08-13T15:50:52+00:00
@josephSummerhays17 

> If it's required that 10% of the block reward goes to the miner ...

Have you actually read #98? Your comment seems entirely unrelated to the proposal.

@kayabaNerve 

> My biggest concern re: #98 is if the entirety of the malicious pool runs local Monero nodes (as feasible if only a few entities actually contribute hash power) yet a lower percentage of miners contributing to other pools migrate. This could actually _increase_ the percentage the malicious pool has by _decreasing_ the overall hash power. I worry the network, as of right now, is too unstable to endorse such a change.

I think the hashrate of the malicious pool currently attacking Monero is mostly rented or attracted by perceived higher mining profits. I don't think it's just a few entities. Their hashrate has been going up steadily over the past weeks and months. For example, it was only around 300 MH/s at the beginning of June. Also the price of RandomX on hashrate rental services is currently significantly above the market rate, which means they are probably using a lot of rented hash power that would not be available with #98.

A downside of any PoW change (not just #98) is that it can temporarily reduce the overall network hashrate, which could make it more vulnerable. One of the preconditions for implementing the proposal would be to make it easy to migrate to P2Pool. Preferably a 1-click setup with XMRig for hobby miners and also tooling and guides for larger miners with many machines. If updated binaries are available months in advance, that should be enough time for all miners who are able to run a node to migrate away from centralized pools.

## josephSummerhays17 | 2025-08-13T16:19:32+00:00
> Have you actually read [#98](https://github.com/monero-project/research-lab/issues/98)? Your comment seems entirey unrelated to the proposal.

ha, oops. No, my comment was in relation to "require blocks be signed by the miner's key" proposal. I assumed rather foolishly that was what #98 was about because I heard @kayabaNerve make a similar argument against that proposal as against yours. I see now your proposal is about sampling historic data as a way to force miners to run a local node. I'm sorry.

## kayabaNerve | 2025-08-13T17:36:06+00:00
My argument against requiring signatures was it could be dodged, not that it could negatively shuffle mining.

## redsh4de | 2025-08-13T18:58:47+00:00
> so users should feel free to accept the amount of risk they want.

I think i understand where you are coming from, but I don’t think this is a “user should be free to accept risk” type of situation - deep reorgs aren’t just an individual risk, they’re a **systemic** consensus risk.

If an attacker can perform a long reorg, the damage isn’t limited to high-value targets or specific transactions - and smaller/larger is not relevant here anyway, given that transaction amounts are hidden in Monero, so any motive for an attack of this sort would be related to destabilizing the whole system, not individuals. Selfish mining undermines all recent transactions within the reorganized blocks, damages settlement reliability, and erodes confidence for everyone - exchanges (already happening), merchants, and casual users alike. Even users who “accept the risk” are still dependent on the rest of the ecosystem trusting the chain.

What matters is network-wide assurance: every transaction, no matter how small, should have the same confidence in its finality. If there’s a way to remove this risk and give higher confidence assurances - i think we should. This isn’t about limiting users, more about giving immutable integrity assurances.

## josephSummerhays17 | 2025-08-13T19:58:27+00:00
I guess I'm failing to see how one transaction failing is a systemic problem. Suppose A pays B, B doesn't care about confirmation time, and immediately pays C, and C _does_ care an awful lot about confirmation time. Later, a reorg happens such that it appears that A never paid B. Why should C care? C chose not to release his product until there was enough confirmation to his satisfaction. The person who lost the money was the B, who didn't care about confirmation time.

## josephSummerhays17 | 2025-08-13T20:03:54+00:00
> My argument against requiring signatures was it could be dodged, not that it could negatively shuffle mining.

Now this comment is baffling to me, and tells me I must be completely misunderstand what the proposal requiring signatures even was in the first place.

If we require a block be signed by an address that receives x% of the block reward, how could one possibly get around that? The pool can't distribute their private keys and open themselves up to funds being stolen by anyone who joins the pool. The pool can't sign every transaction themselves and ship them to be hashed by pool members, the bandwidth would be incredible. How could this possibly be dodged?

## techmetx11 | 2025-08-13T20:21:14+00:00
> > My argument against requiring signatures was it could be dodged, not that it could negatively shuffle mining.
> 
> Now this comment is baffling to me, and tells me I must be completely misunderstand what the proposal requiring signatures even was in the first place.
> 
> If we require a block be signed by an address that receives x% of the block reward, how could one possibly get around that? The pool can't distribute their private keys and open themselves up to funds being stolen by anyone who joins the pool. The pool can't sign every transaction themselves and ship them to be hashed by pool members, the bandwidth would be incredible. How could this possibly be dodged?

If signatures aren't built into the PoW algorithm, the pools can still offload hash computation to its pool members and sign the block themselves after without exposing their private key.
This isn't something new, You can make a Wownero pool by using `xmrig-proxy`, despite Wownero requiring you to give up your spend key to solo-mine

## wowario | 2025-08-13T20:38:06+00:00
On Block Signed by Miner's Key, if the aim is to go full on solo-mining only, I do acknowledge there are enforcement issues with bonded private pools and xmrig-proxy mining. However, it is my understanding the proposed implementation for Monero would allow pools/p2pool, but with a penalty applied where the "first output for at least 10% of the block reward" goes to the signer of the block. For clarification, is the concern with solo-mining only enforcement (not applicable in Monero's proposed implementation) or circumventing the penalty itself?

imo, it would be hard to dodge enforcement of `X` penalty  if there is a check for `output_size != 1 || !valid_signature` in the `validate_miner_transaction` stage. Blocks with valid signatures and 1 output would get the full block reward, while pool miners get an `X` reduction in the base reward. If a pool tries to claim more than the penalized amount, the block would get rejected. Given this, I don't think a soft fork would be the best approach, it'll get too messy. 

edit: although bonded private pools and xmrig-proxy mining could also be used to get around the penalty, these types of "trusted" pools wouldn't scale up to the level of public pools currently on the network.

## josephSummerhays17 | 2025-08-14T03:08:05+00:00
> pools can still offload hash computation to its pool members and sign the block themselves after without exposing their private key.

The idea is that the signature would be added to the block _before_ being hashed, not after. The signature then becomes part of the hash. Since a pool doesn't know which block will win, they'd have to sign every block and distribute them, requiring more bandwidth than it's worth.

## josephSummerhays17 | 2025-08-14T03:16:48+00:00
> I do acknowledge there are enforcement issues with bonded private pools and xmrig-proxy mining.

Ah! so that's the work around. That is totally a work around I'm willing to accept. My main reason for liking the proposal was never to punish pool mining, which I like a lot. It's to punish mining pools that pay out in an alternate crypto. Of course, pools can still pay out the remaining 90% in their own low liquidity pump and dump scheme token if they wish, but at least the 10% the individual miner would have influence over.

## Gingeropolous | 2025-08-14T03:25:15+00:00
here's my idea turned into math and cryptography and stuff (hopefully correctly) by the bots:

https://github.com/Gingeropolous/friction/blob/main/friction_longer.md

## techmetx11 | 2025-08-14T03:27:31+00:00
> > pools can still offload hash computation to its pool members and sign the block themselves after without exposing their private key.
> 
> The idea is that the signature would be added to the block _before_ being hashed, not after. The signature then becomes part of the hash. Since a pool doesn't know which block will win, they'd have to sign every block and distribute them, requiring more bandwidth than it's worth.

Ah, well that makes more sense.

> My main reason for liking the proposal was never to punish pool mining, which I like a lot. It's to punish mining pools that pay out in an alternate crypto.

To be honest, I do not like centralized mining pools at all and would rather prefer to see them disappear and be replaced with P2Pool, but I doubt you can selectively punish mining pools who choose to use their funds for nefarious purposes. 90% is still a whole lot left for Qubic to continue pumping up their token and I doubt the people mining for them even care about the 10% Monero. It would just be a joke to laugh off for these people

## wowario | 2025-08-14T03:38:04+00:00
> requiring more bandwidth than it's worth

@josephSummerhays17 the barrier is more to do with adding a new field to the block header for the signature. the signature is generated using the miner's private spend key, which is then amended to the block header **before** PoW hashing. Nodes then verify block signatures using the `output_public_key` of `b.miner_tx.vout[0]`.

## tevador | 2025-08-14T05:06:30+00:00
Who can authorize the use of BTC from the general fund? Maybe @luigi1111?

A practical short-term mitigation would be to rent hashrate and point it to a smaller trusted pool, e.g. moneroocean.stream.

Renting hashrate has a dual effect on this attack:

1. It increases the hashrate of honest pools.
2. It denies rentable hashrate to the attacker.

I think it would be advisable to do this, especially since the attacker is announcing the times when they will attack. It seems that at least 200 MH/s should be available for rent, which would cost around 0.1 BTC per day. Part of the funds would be recouped as mined XMR, which could go to the XMR general fund.

## FocuzJS | 2025-08-14T05:11:14+00:00
edit: wrong issue
moved to: https://github.com/monero-project/research-lab/issues/135#issuecomment-3187064011

## josephSummerhays17 | 2025-08-14T05:14:55+00:00
> which is then amended to the block header **before** PoW hashing.

??? Isn't that what I said?

>The idea is that the signature would be added to the block before being hashed, not after. 

## tevador | 2025-08-14T05:18:57+00:00
@FocuzJS 

This issue is for general discussion about strategies to improve chain security.

I think technical details of specific solutions should go to their respective issues:

Finality layer - https://github.com/monero-project/research-lab/issues/135
PoW with a local node - https://github.com/monero-project/research-lab/issues/98

## josephSummerhays17 | 2025-08-14T05:21:41+00:00
> here's my idea turned into math and cryptography and stuff (hopefully correctly) by the bots:
> 
> https://github.com/Gingeropolous/friction/blob/main/friction_longer.md

I only skimmed, but this seems intriguing and relevant. Worth a read.

## wowario | 2025-08-14T07:29:57+00:00
@josephSummerhays17 i was referring to your comment "sign every block and distribute them, requiring more bandwidth"... pool operators would need to share the private spend key with all miners to be able to sign blocks. there's the rub (any miner in the pool could theoretically steal the block reward), not the bandwidth requirements.

## kayabaNerve | 2025-08-14T08:41:13+00:00
Pools could require a deposit from miners.

Pools could assume if a miner enters a race for whatever fraction they can try to take for themselves, their own edge (their hash power) will be sufficient.

Pools can share an _encumbered_ private key only usable to sign blocks, not transactions.

There are many designs which practically work-around the requirement x% of the rewards go to the miner, as proven by a signature being part of the hash.

## josephSummerhays17 | 2025-08-14T09:47:45+00:00
> 我认为，矿工想单独挖矿 需要质押少量的门罗币，如果需要加入私有矿池挖矿就要根据矿池的比重，质押增加指数级增长的门罗币。这样促进门罗币矿工单独挖矿。

The monero network has no way of knowing whether a block came from a pool or not, so that's a no-go. As for staking monero to even be allowed to mine... I mean, maybe? It will certainly have _some_ effect. But it's not clear to me what that will be, or even if it will be relevant to our objectives in any way. But make your case.

There are other proposals to either gentle encourage or outright enforce local mining.

## josephSummerhays17 | 2025-08-14T10:07:25+00:00
> [@josephSummerhays17](https://github.com/josephSummerhays17) i was referring to your comment "sign every block and distribute them, requiring more bandwidth"... pool operators would need to share the private spend key with all miners to be able to sign blocks. there's the rub (any miner in the pool could theoretically steal the block reward), not the bandwidth requirements.

Oh, I understood this. This is one way a pool might try to operate, which obviously fails. But there's another way a pool might attempt to operate, which also fails, which was my point about bandwidth. A pool that wanted to keep it's private keys would have to prepare blocks, sign them, and then distribute them to be hashed. But this is obviously ridiculous given 5 gigahash pe sec, just sending the signatures alone is ridiculous bandwidth.

lets say 64 bytes per sig, a pool w/ 1% of the hash rate, 50 megahash, is 320 megabytes per second... actually now that I've calculated it out, this sounds totally doable.

I've changed my mind, I don't think this will work, unless randomX was changed somehow to produce more hashes on the same fundamental computing power (such that the difficulty went up), a pool could just distribute the signatures of the blocks to be hashed.

(the pool doesn't have to distribute the entire block. The pool can deduce what the miner's block should be, sign that, distribute the signature, and the miner can recreate that same block to hash)

## josephSummerhays17 | 2025-08-14T10:17:08+00:00
> Pools could assume if a miner enters a race for whatever fraction they can try to take for themselves, their own edge (their hash power) will be sufficient.

I doubt a pool would take this risk, unless they had 51% of the hash, which presupposes the problem we're trying to solve.

> Pools can share an _encumbered_ private key only usable to sign blocks, not transactions.

Now, I worry this comment may bewray my ignorance on the subject, but... Aren't encumberences on keys handled in the software, not fundamental to the cryptography? And if so, why would we allow encumbered keys to sign a transaction? If the network can't tell the difference between an encumbered key and an unencumbered key during block signing time, how does it know the difference at transaction time?

But I guess the whole discussion is moot now, I've been convince against the proposal for other reasons, so we're in agreement.



## kayabaNerve | 2025-08-14T11:44:06+00:00
The protocol can't differentiate an encumbered key from an unencumbered key, without a proof it's unencumbered (for which there was a paper written on such proofs).

Despite the protocol being unable to tell the difference, the user may have an encumbered key only usable to sign blocks.

## Kronkmeister | 2025-08-14T14:11:13+00:00
Avalanche protocol integration for finality is another option. It doesn't risk being disrupted by 32% stake. It needs 7/8th of the stake to have a chance at disrupting the network. Also would effectively give you 1-block finality and would use PoS only for Sybil resistance, not for validation. Meaning it would be enhanced PoW, not PoW/PoS like other hybrids. Ideal for low hashrate.

## Schneiderei | 2025-08-14T14:32:39+00:00
**RandomX give the amount/speed of RAM a bigger role**
Since many desktop PCs today and in the future are equipped with much more RAM than back then, I thought it might be an advantage for home miners if the amount/speed of RAM played a bigger role in RandomX. For someone who wants to mine with their powerful computer when not playing games, it probably wouldn't be a big deal to upgrade or expand the computer with 4 fast ram sticks of 8 gigabytes each. However, for attackers trying to get a high hashrate to attack Monero's PoW consensus mechanism, 4x8 gigabytes per CPU would be expensive these days. This would make the hurdle for a potential attack more expensive due to the increase in random-access memory and more difficult due to the lack of such systems.

## techmetx11 | 2025-08-14T14:38:39+00:00
> **RandomX give the amount/speed of RAM a bigger role** Since many desktop PCs today and in the future are equipped with much more RAM than back then, I thought it might be an advantage for home miners if the amount/speed of RAM played a bigger role in RandomX. For someone who wants to mine with their powerful computer when not playing games, it probably wouldn't be a big deal to upgrade or expand the computer with 4 fast ram sticks of 8 gigabytes each. However, for attackers trying to get a high hashrate to attack Monero's PoW consensus mechanism, 4x8 gigabytes per CPU would be expensive these days. This would make the hurdle for a potential attack more expensive due to the increase in random-access memory and more difficult due to the lack of such systems.

2 GB per CPU is already excessive as it is, 32 GB per CPU would be much more likely to significantly hurt honest miners and kill the global hashrate even more.
Not everyone can afford 32 GB of RAM, and not only that, it would be crippling in even the most powerful setups as it would probably starve the OS of RAM in higher amounts of threads (unless you mine exclusively in single-thread).

On another note, this would also make RandomX completely unminable in 32-bit systems (if you're into salvaging e-waste to use as miners)

## Schneiderei | 2025-08-14T14:46:58+00:00
> 32 GB per CPU would be much more likely to significantly hurt honest miners

There is already a very slow mode for devices with very little RAM. There could be another mode that would give computers with a lot of fast RAM a big advantage. The purchase of a four-pack of RAM sticks would pay for itself if the device is often used for mining.

## techmetx11 | 2025-08-14T15:02:56+00:00
> > 32 GB per CPU would be much more likely to significantly hurt honest miners
> 
> There is already a very slow mode for devices with very little RAM. There could be another mode that would give computers with a lot of fast RAM a big advantage. The purchase of a four-pack of RAM sticks would pay for itself if the device is often used for mining.

Making it a seperate mode is fine, but I don't know how you would manage to factor in the speed
I still disagree with increasing the system requirements (other than against ASICs) because it is just delaying attackers (who can bribe others to mine for them) while disqualifying honest miners without the resources required to mine

## kayabaNerve | 2025-08-14T16:43:16+00:00
> Avalanche protocol integration for finality is another option. It doesn't risk being disrupted by 32% stake. It needs 7/8th of the stake to have a chance at disrupting the network.

Wildly untrue. The original Avalanche failed when just a square root amount of nodes where malicious. For 1,000,000 nodes, this would be just 1,000, or 0.1%. Avalanche also was never proven in an asynchronous setting.

https://github.com/serai-dex/serai/issues/445 best describes my thoughts/cites research when I considered it for Serai.

## Schneiderei | 2025-08-14T18:57:31+00:00
**parts of Nakamoto Consensus NC-MAX**

Monero has had 1 minute blocks in its past. Let's go back to the past! I propose transactions that are propagated first. A transaction is then a proposed transaction. After five ten-second block proposals, or 50 seconds, the transaction could be committed to one of the 1-minute blocks.

[NC-MAX](https://github.com/nervosnetwork/docs.nervos.org/blob/5b4aa95a1d1d8ea7072de73b89117c7a7d202a88/website/docs/tech-explanation/consensus.md?plain=1#L18) is splitting the confirmation process into two steps: propose and commit

> A transaction is first proposed to the network. After several blocks have been verified, the transaction can then be confirmed. This gives more time for transaction propagation without slowing down block propagation. Once a transaction has been proposed and fully propagated, then it can be committed. This eliminates transaction propagation as a delay factor to block propagation, eliminating the bottleneck and selfish mining attack.
> With a shorter block interval, blocks are created more frequently, enabling faster transaction confirmations and a higher throughput for the network. The downside of a shorter block interval is that internet congestion has a greater effect on the ability of the network to properly synchronize. There are times when blocks are created while the network is not fully in sync, creating so-called orphan blocks. This means that the efforts towards network security are temporarily divided. Orphan blocks are inevitable; however, if too many occur within a short period of time, shorter block intervals become counterproductive.


## tevador | 2025-08-14T19:43:42+00:00
> **RandomX give the amount/speed of RAM a bigger role** Since many desktop PCs today and in the future are equipped with much more RAM than back then, I thought it might be an advantage for home miners if the amount/speed of RAM played a bigger role in RandomX. For someone who wants to mine with their powerful computer when not playing games, it probably wouldn't be a big deal to upgrade or expand the computer with 4 fast ram sticks of 8 gigabytes each. However, for attackers trying to get a high hashrate to attack Monero's PoW consensus mechanism, 4x8 gigabytes per CPU would be expensive these days. This would make the hurdle for a potential attack more expensive due to the increase in random-access memory and more difficult due to the lack of such systems.

The RAM requirements for mining RandomX cannot be increased due to verification performance constraints. See: https://github.com/tevador/RandomX/blob/master/doc/design.md#14-memory-hardness



## duck-wizard-code | 2025-08-15T00:00:26+00:00
> > **RandomX give the amount/speed of RAM a bigger role** Since many desktop PCs today and in the future are equipped with much more RAM than back then, I thought it might be an advantage for home miners if the amount/speed of RAM played a bigger role in RandomX. For someone who wants to mine with their powerful computer when not playing games, it probably wouldn't be a big deal to upgrade or expand the computer with 4 fast ram sticks of 8 gigabytes each. However, for attackers trying to get a high hashrate to attack Monero's PoW consensus mechanism, 4x8 gigabytes per CPU would be expensive these days. This would make the hurdle for a potential attack more expensive due to the increase in random-access memory and more difficult due to the lack of such systems.
> 
> The RAM requirements for mining RandomX cannot be increased due to verification performance constraints. See: https://github.com/tevador/RandomX/blob/master/doc/design.md#14-memory-hardness

What if we just made it a highly RAM intensive mining algorithm to the point that the more ram you throw at it the more hash rate you get. Obviously until you hit the upper limit of what your CPU can handle. This would favor bare metal solo miners exponentially with the very high cost of high speed RAM in the cloud. Combined with signing a block with your key and it could make it maximumly solo miner favored. This would likely reduce hash rate contributed by giant pools and cloud mining while drastically increasing profitability and shifting majority of the hash rate to full node solo miners. Remember it’s not just about more hash-rate = more security. Part of the equation is how expensive each hash is, you could have lower hash-rate with technically higher security if that hash-rate requires more metal to make.

## techmetx11 | 2025-08-15T00:12:37+00:00
> > > **RandomX give the amount/speed of RAM a bigger role** Since many desktop PCs today and in the future are equipped with much more RAM than back then, I thought it might be an advantage for home miners if the amount/speed of RAM played a bigger role in RandomX. For someone who wants to mine with their powerful computer when not playing games, it probably wouldn't be a big deal to upgrade or expand the computer with 4 fast ram sticks of 8 gigabytes each. However, for attackers trying to get a high hashrate to attack Monero's PoW consensus mechanism, 4x8 gigabytes per CPU would be expensive these days. This would make the hurdle for a potential attack more expensive due to the increase in random-access memory and more difficult due to the lack of such systems.
> > 
> > 
> > The RAM requirements for mining RandomX cannot be increased due to verification performance constraints. See: https://github.com/tevador/RandomX/blob/master/doc/design.md#14-memory-hardness
> 
> What if we just made it a highly RAM intensive mining algorithm to the point that the more ram you throw at it the more hash rate you get. Obviously until you hit the upper limit of what your CPU can handle. This would favor bare metal solo miners exponentially with the very high cost of high speed RAM in the cloud. Combined with signing a block with your key and it could make it maximumly solo miner favored. This would likely reduce hash rate contributed by giant pools and cloud mining while drastically increasing profitability and shifting majority of the hash rate to full node solo miners. Remember it’s not just about more hash-rate = more security. Part of the equation is how expensive each hash is, you could have lower hash-rate with technically higher security if that hash-rate requires more metal to make.

What if you just stick a bunch of high-speed SSDs in, and use swap on them.
Better yet, this just sounds like RandomX but if you tried to use it in multiple CPUs. I've never seen an algorithm like this because memory-hard PoW algorithms like Equihash rely on a pre-determined amount of memory to waste solving a challenge (and the bigger it is set, the bigger the solution is)
How would you somehow factor in the amount of memory a user is using?

## Schneiderei | 2025-08-15T00:40:59+00:00
> due to verification performance constraints

It would of course require a change. Reading and writing about the same amount, which CPU's are very well made for, would not apply with this additional step. Remember when you ran RandomX on a 256GB RAM server? It took a few seconds of blinking command line until the scratchpad was done. For example, you could also measure the time that large fast ram takes and use it as a multiplier. Of course, it would no longer be the RX we have come to know and love.


> This would favor bare metal solo miners exponentially with the very high cost of high speed RAM in the cloud.

You can also pull up the RAM slider for rented instances, but you get my point. It would be shared RAM in the cloud that never has the performance of RAM immediately physically next to the CPU. It would also drive up the cost for potential attackers. I'm talking about CAS latency, which the video renderer, compiler or game player has, but not the cloud.

## antanst | 2025-08-15T07:03:34+00:00
Lots of arguments here have already being rehashed in the old randomx vs asics discussion. For example, going the ASIC way (which I was always a proponent of, along with @fluffypony ) but choosing an existing algorithm like sha256 would be extremely dangerous.

 https://github.com/monero-project/meta/issues/316

## tevador | 2025-08-15T10:11:40+00:00
@duck-wizard-code @techmetx11 @Schneiderei 

Feel free to open an issue in the RandomX repository and make a concrete proposal.

I don't see how we can increase the RAM usage of RandomX without breaking the [design constraints](https://github.com/tevador/RandomX/blob/master/doc/design.md).

## johnr365 | 2025-08-15T10:26:56+00:00
> > This is a good, simple incentive for miners not to mine empty blocks. I would support this.
> > It could be a relay rule, which would only require a software update.
> 
> I'd support this - raising the fees would also ensure that spamming attacks are more expensive.

Just want to resurface the topic of raising fees (which fluffypony and Tevador supported) and see where this conversation has got to?

It seems counterproductive that transaction fees are fractions of a cent, and yet simultaneously we're discussing Monero's security budget being insufficient.

There's people mining on the network right now at a substantial loss in order to help the network. So it would make sense that if "every little helps", there's a raise in transaction fees also.

Of course I appreciate that:

a) Raising fees won't solve the issue on it's own

b) We need another solution in parallel

c) We must avoid raising fees so high that it makes the network unaffordable for every day users

## shortwavesurfer2009 | 2025-08-15T11:14:29+00:00
I would support a fee raise. Normal day-to-day transactions seem to get by with incredibly low fees. Where I could see this potentially being a problem is on multi-input transactions, such as P2pool. I would think the fees could get rather high on those.

Edit: As an example, I just created a transaction where the fee would be 0.000045 xmr ($0.01USD). Even doubling the fee would not make daily transactions unaffordable.

## MoneroArbo | 2025-08-15T13:15:49+00:00
> Where I could see this potentially being a problem is on multi-input transactions, such as P2pool. I would think the fees could get rather high on those.

We should make it so coinbase outputs don't use rings when spent, or get included in other transactions as decoys. It's been discussed before. It will make p2pool consolidation MUCH cheaper and won't really harm privacy. In fact, it would improve privacy for other (non coinbase) spending as you'd no longer have a bunch of coinbase outputs as decoys, which as I figure it were never very good decoys anyway.

## 0range-horizon | 2025-08-15T14:27:29+00:00
Hi All, I'm new and after quickly skimming this whole thread and looking at the solutions proposed, I discovered two things: you're all clearly much smarter and knowledgeable than I am, and 2. I don't think that this idea has been presented exactly yet.

This suggestion was posted here first : monero.town/post/6526877

My guess is it won't work for one reason or another but perhaps it can help build on other ideas.


**Proposal Overview**
The idea is to give a difficulty penalty to new hash power in order to make 51% attacks more expensive. This would penalise short term hash rate increases  whilst minimising the impact to long term legitimate miners.


**How It Would Work**
- **Hash Rate Verification:** Block producers (solo miners, or pools, treated as solo miners) periodically prove their hash rate to the protocol (e.g., 10 times daily).
  - Perhaps prove hash rate by submitting shares.
- **Difficulty Penalty:** If a miner’s hash rate spikes significantly, the protocol applies a higher difficulty to their new hash rate, reducing its effectiveness in mining blocks.
  - A miner’s difficulty would be an average of the standard network difficulty (for their existing hash rate) and a higher difficulty (for their additional hash rate) weighted by percentage of each.
- **Normalisation Over Time:** The penalty gradually decreases over, say, 3 months, as the new hash rate is sustained, the miners average hash rate trends towards it.
- **Seasonal Miner Adjustment:** A separate, decay rate applies to hash rate reductions which can be tuned to avoid overly penalising legitimate fluctuations such as seasonal miners who mine less during warmer months or those who mine on intermittent power sources such as wind or solar power.
  - The hash rate of a miner must decay to prevent a malicious actor 'levelling up' many miners and then utilising rented hash rate across them all at the same time later for an attack.

## tevador | 2025-08-15T15:35:21+00:00
@0range-horizon Your proposal is similar to a previous proposal to "limit the maximum hashrate per pool".

I'll just quote you the response by @fluffypony which explains why none of these proposals are possible:

> Literally impossible. Pools have NO OBLIGATION to identify themselves in block metadata, and even if they did, a pool could literally pretend to be another pool / multiple separate pools. We only know how much hashrate pools have because they self report + tag blocks.

## josephSummerhays17 | 2025-08-15T15:39:10+00:00
> I would support a fee raise. Normal day-to-day transactions seem to get by with incredibly low fees. Where I could see this potentially being a problem is on multi-input transactions, such as P2pool. I would think the fees could get rather high on those.
> 
> Edit: As an example, I just created a transaction where the fee would be 0.000045 xmr ($0.01USD). Even doubling the fee would not make daily transactions unaffordable.

Because the vast majority of miner profit is from  inflation, you could 10x the fees and do essentially nothing to miner profitability.

I have doubts that it's even possible to increase a crypto's security budget just at the dev's command. If inflation were higher, the price of monero would drop. If fees were higher it would also drop. Lets me give an extreme example to make my point.

If you don't believe the security budget is self balancing, then lets just make our security budget a trillion dollars a day! Inflation or fees, doesn't matter, either works.

No, the only way to increase the security budget is to increase the number of users.

As much as I hate it, I'm coming around to a finality layer as the only real solution. Or nothing. Nothing may actually work if monero grows. If monero was BTC sized, there wouldn't be a concern at all. But if monero doesn't grow, then the only solution may just be a finality layer.

## shortwavesurfer2009 | 2025-08-15T15:45:42+00:00
> > I would support a fee raise. Normal day-to-day transactions seem to get by with incredibly low fees. Where I could see this potentially being a problem is on multi-input transactions, such as P2pool. I would think the fees could get rather high on those.
> > Edit: As an example, I just created a transaction where the fee would be 0.000045 xmr ($0.01USD). Even doubling the fee would not make daily transactions unaffordable.
> 
> Because the vast majority of miner profit is from inflation, you could 10x the fees and do essentially nothing to miner profitability.
> 
> I have doubts that it's even possible to increase a crypto's security budget just at the dev's command. If inflation were higher, the price of monero would drop. If fees were higher it would also drop. Lets me give an extreme example to make my point.
> 
> If you don't believe the security budget is self balancing, then lets just make our security budget a trillion dollars a day! Inflation or fees, doesn't matter, either works.
> 
> No, the only way to increase the security budget is to increase the number of users.
> 
> As much as I hate it, I'm coming around to a finality layer as the only real solution. Or nothing. Nothing may actually work if monero grows. If monero was BTC sized, there wouldn't be a concern at all. But if monero doesn't grow, then the only solution may just be a finality layer.

Damn, fair point.

Edit: Actually, I don't think I understand. The miners get the tail emission and the transaction fees, so why wouldn't increasing the transaction fees make the miners more profitable?

## Kronkmeister | 2025-08-15T16:10:58+00:00
> Wildly untrue. 

Well, not sure about the early theoretical papers you are referencing but it works as explained in our real-world implementation. 

## kayabaNerve | 2025-08-15T16:15:40+00:00
@Kronkmeister If you support finalizations even with 87.5% offline, then you only need 12.5% online. This immediately means that re: asynchronous safety (so the asynchronous or partially-synchronous models discussed), any 12.5% can produce a finalization.

Even with a synchronous network, the best bound would be 2f+1, allowing 49% to be offline/malicious.

## MoneroArbo | 2025-08-15T16:18:33+00:00
Speaking of theoretical papers, this reddit user linked to some research on checkpointing that seems worth checking out: 

- https://old.reddit.com/r/Monero/comments/1mqtgwj/rolling_10block_checkpoints_a_fix_for_monero/

## shortwavesurfer2009 | 2025-08-15T16:54:06+00:00
> Speaking of theoretical papers, this reddit user linked to some research on checkpointing that seems worth checking out:
> 
>     * https://old.reddit.com/r/Monero/comments/1mqtgwj/rolling_10block_checkpoints_a_fix_for_monero/

I did not dig into the papers yet, but one comment on that thread caught my eye, and it said that the node of every user would just keep a hash of the tenth block back, and if it was changed it would reject it. Is that how this would work?

Another comment asked what happens if an adversary mines 10 blocks in a row so that they are able to make a checkpoint out of the first block they mined. And the answer it seems as though was that it didn't matter in that case. Because it still would not let you go back further than those 10 blocks anyway. Any node that tried to present a chain longer than ten blocks would just be rejected even if the pow was harder.

## duck-wizard-code | 2025-08-15T17:00:23+00:00
I think we have to consider making Monero a solo-mining exclusive protocol. Pools are not necessary, they are a convenience yes, but it disincentivizes running a full node, and centralizes mining. If we enforced a miner to sign a block and make it virtually impossible to run a pool, I think the pros outweigh the cons. I would go so far as to say we should build anti-pool mining security into the protocol. Allow the mining algorithm to be processed in RAM or be advantageous to have fast and ample ram further disincentivizing cloud hosted miners. The goal would be to make it as desktop friendly as possible and get away from bit pools.

## Kronkmeister | 2025-08-15T17:00:23+00:00
> Speaking of theoretical papers, this reddit user linked to some research on checkpointing that seems worth checking out:
> 
> * https://old.reddit.com/r/Monero/comments/1mqtgwj/rolling_10block_checkpoints_a_fix_for_monero/

Great to see, usually people don't mention ABC tech. But to get you up to speed, Bitcoin ABC removed the 10-block checkpoint since integration of Avalanche post-consensus which acts effectively as a 1-block reorg protection or "checkpoint", making the 10-block checkpoint obsolete.

I'm not too versed in the technicalities but as far as I can tell it is a misconception to say 12.5% can finalize anything. I think there would simply be no finalization going on because you need 7/8th of the total stake, not the current stake that is online. But I might be wrong on these things. But since you are already looking at Bitcoin ABC code, I am sure you can check out the Avalanche part as well.

## techmetx11 | 2025-08-15T17:11:54+00:00
> Allow the mining algorithm to be processed in RAM or be advantageous to have fast and ample ram further disincentivizing cloud hosted miners.

Doesn't RandomX already fulfill the first half? Again, if you have some sort of computational problem that could make the latter half possible then you're free to suggest it.
This sounds like a stupid idea because the CPU speed will always be factored in and will always be SUPER important to the algorithm, Otherwise I'd have better luck mining Monero on a 80386 if I happened to give it 8 EB of RAM

## josephSummerhays17 | 2025-08-15T18:46:49+00:00
> I think we have to consider making Monero a solo-mining exclusive protocol. Pools are not necessary, they are a convenience yes, but it disincentivizes running a full node, and centralizes mining. If we enforced a miner to sign a block and make it virtually impossible to run a pool, I think the pros outweigh the cons. I would go so far as to say we should build anti-pool mining security into the protocol. Allow the mining algorithm to be processed in RAM or be advantageous to have fast and ample ram further disincentivizing cloud hosted miners. The goal would be to make it as desktop friendly as possible and get away from bit pools.

No one is going to solo mine. I guarantee it. Nobody is going to start mining when their expected block time is YEARS away.

This is just an economic fact. EVERYONE prefers money now to money later; when we make decisions about making money in the future, we all discount the money based on how far away it is.

So if you're thinking "small little pay outs spread over 3 years and one big pay out are the same thing", well there's not much I can say but you're wrong. Even if it's the same amount of monero, everyone is present oriented. There's no such thing as a negative interest rates (except in the world of government run central bank scams).

Big miners who will find blocks more often will continue mining. Small miners will just not care at all. They'll drop out.

This will decrease the total security budget, not increase it.

## CyberAshven | 2025-08-15T18:51:41+00:00
> > Speaking of theoretical papers, this reddit user linked to some research on checkpointing that seems worth checking out:
> > 
> > * https://old.reddit.com/r/Monero/comments/1mqtgwj/rolling_10block_checkpoints_a_fix_for_monero/
> 
> Great to see, usually people don't mention ABC tech. But to get you up to speed, Bitcoin ABC removed the 10-block checkpoint since integration of Avalanche post-consensus which acts effectively as a 1-block reorg protection or "checkpoint", making the 10-block checkpoint obsolete.
> 
> I'm not too versed in the technicalities but as far as I can tell it is a misconception to say 12.5% can finalize anything. I think there would simply be no finalization going on because you need 7/8th of the total stake, not the current stake that is online. But I might be wrong on these things. But since you are already looking at Bitcoin ABC code, I am sure you can check out the Avalanche part as well.

Regarding avalanche its contrvasy as people in Bitcoin Cash didn't endorse it. Basically Implementing rolling 10-block checkpoints is the logical thing to do in order to stop deep reorgs. It’s been tested for years in Bitcoin Cash and proven effective. We just need a proof of concept.

## CyberAshven | 2025-08-15T19:02:14+00:00
> > > I would support a fee raise. Normal day-to-day transactions seem to get by with incredibly low fees. Where I could see this potentially being a problem is on multi-input transactions, such as P2pool. I would think the fees could get rather high on those.
> > > Edit: As an example, I just created a transaction where the fee would be 0.000045 xmr ($0.01USD). Even doubling the fee would not make daily transactions unaffordable.
> > 
> > Because the vast majority of miner profit is from inflation, you could 10x the fees and do essentially nothing to miner profitability.
> > 
> > I have doubts that it's even possible to increase a crypto's security budget just at the dev's command. If inflation were higher, the price of monero would drop. If fees were higher it would also drop. Lets me give an extreme example to make my point.
> > 
> > If you don't believe the security budget is self balancing, then lets just make our security budget a trillion dollars a day! Inflation or fees, doesn't matter, either works.
> > 
> > No, the only way to increase the security budget is to increase the number of users.
> > 
> > As much as I hate it, I'm coming around to a finality layer as the only real solution. Or nothing. Nothing may actually work if monero grows. If monero was BTC sized, there wouldn't be a concern at all. But if monero doesn't grow, then the only solution may just be a finality layer.
> 
> Damn, fair point.
> 
> Edit: Actually, I don't think I understand. The miners get the tail emission and the transaction fees, so why wouldn't increasing the transaction fees make the miners more profitable?

This could happen today without a hard fork by introducing a new relay policy with a minimum fee limit, which can be changed at any point in time. This would increase the fee, incentivizing miners.

## josephSummerhays17 | 2025-08-15T19:04:29+00:00
> Edit: Actually, I don't think I understand. The miners get the tail emission and the transaction fees, so why wouldn't increasing the transaction fees make the miners more profitable?

Lets run through an example. a block's reward from tail emission is .6 XMR or 150 USD. There are roughly 40k transactions per day, which breaks down to about 55 transactions per block. The comment I was replying to said transaction fees were about 1 cent, but recently its been more like 12 cents and peak I've seen is 25 cents (though, when the transaction fee was that high, monero was worth more, making tail emissions a bigger factor).

with transaction fees at .01USD, we get: 55tx*.01USD/tx= .55USD, or 0.33% of total reward
with transaction fees at .12USD we get: 55tx*.12USD/tx= 6.6USD, or 4.2% of total reward
with transaction fees doubled to .24USD we get: 55tx*.24USD/tx = 13.2USD or 8.1% of total

tail emmisions dominate even after doubling fees. I'm sure miners wouldn't mind the extra cash but it wouldn't actually be a big deal.

## CyberAshven | 2025-08-15T19:07:04+00:00
> I think we have to consider making Monero a solo-mining exclusive protocol. Pools are not necessary, they are a convenience yes, but it disincentivizes running a full node, and centralizes mining. If we enforced a miner to sign a block and make it virtually impossible to run a pool, I think the pros outweigh the cons. I would go so far as to say we should build anti-pool mining security into the protocol. Allow the mining algorithm to be processed in RAM or be advantageous to have fast and ample ram further disincentivizing cloud hosted miners. The goal would be to make it as desktop friendly as possible and get away from bit pools.

As a miner, I believe that it is quite challenging to scale a mining operation profitably using RandomX. If there were a way to incentivize miners to run their farms on a local P2Pool instance, allowing them to scale their operations easily and efficiently similar to how GPU mining works. It would be ideal for miners, hobbyists and even regular user.

## techmetx11 | 2025-08-15T19:11:51+00:00
Centralized pools are bad, but we shouldn't consider going full-solo mining since it'll kill motivation for the smaller (or even mid) miners while having the blockchain be dominated by the big miners, which means Monero will lose out on some extra hashrate
We should be encouraging people to mine on distributed pools like P2Pool

## josephSummerhays17 | 2025-08-15T19:16:23+00:00
> I believe that it is quite challenging to scale a mining operation profitably using RandomX.

The problem is not RandomX. The problem with scaling profitably is that you're in a market that, by design, is perfectly elastic in supply. One hash is as good as the next and there's nothing you can do to 'distinguish' yourself as a producer of hash. You can't get loyal customers, you can't market your hash as having twice as many wiznats as your competitors. The only thing that matters is cheap electricity, some bandwidth, and tons of hardware. There is no hashing algorithm that will solve that.

## shortwavesurfer2009 | 2025-08-15T19:34:03+00:00
> > I think we have to consider making Monero a solo-mining exclusive protocol. Pools are not necessary, they are a convenience yes, but it disincentivizes running a full node, and centralizes mining. If we enforced a miner to sign a block and make it virtually impossible to run a pool, I think the pros outweigh the cons. I would go so far as to say we should build anti-pool mining security into the protocol. Allow the mining algorithm to be processed in RAM or be advantageous to have fast and ample ram further disincentivizing cloud hosted miners. The goal would be to make it as desktop friendly as possible and get away from bit pools.
> 
> As a miner, I believe that it is quite challenging to scale a mining operation profitably using RandomX. If there were a way to incentivize miners to run their farms on a local P2Pool instance, allowing them to scale their operations easily and efficiently similar to how GPU mining works. It would be ideal for miners, hobbyists and even regular user.

I'm not sure if this is what you mean or not, but you can easily connect multiple miners to the same P2pool instance node just by putting in the address and the port just like you would with any other miner. There's also XMrig-proxy as well.

## techmetx11 | 2025-08-15T19:36:29+00:00
> I'm not sure if this is what you mean or not, but you can easily connect multiple miners to the same P2pool instance node just by putting in the address and the port just like you would with any other miner. There's also XMrig-proxy as well.

P2Pool is more than enough, you can connect several miners to it

## CyberAshven | 2025-08-15T20:10:09+00:00
> > > I think we have to consider making Monero a solo-mining exclusive protocol. Pools are not necessary, they are a convenience yes, but it disincentivizes running a full node, and centralizes mining. If we enforced a miner to sign a block and make it virtually impossible to run a pool, I think the pros outweigh the cons. I would go so far as to say we should build anti-pool mining security into the protocol. Allow the mining algorithm to be processed in RAM or be advantageous to have fast and ample ram further disincentivizing cloud hosted miners. The goal would be to make it as desktop friendly as possible and get away from bit pools.
> > 
> > As a miner, I believe that it is quite challenging to scale a mining operation profitably using RandomX. If there were a way to incentivize miners to run their farms on a local P2Pool instance, allowing them to scale their operations easily and efficiently similar to how GPU mining works. It would be ideal for miners, hobbyists and even regular user.
> 
> I'm not sure if this is what you mean or not, but you can easily connect multiple miners to the same P2pool instance node just by putting in the address and the port just like you would with any other miner. There's also XMrig-proxy as well.

that's not what I meant, my friend basically if you want to scale mining operations now each miner is a whole pc with all the components which makes them harder to manage, scale efficiently and operate at a larger scale 

## keriate | 2025-08-15T23:15:39+00:00
I'd like to throw in an idea I haven't seen so far. The problem with this qubic incident appears to be the low number of _incentivized_ and _distinct_ miners that would decentralize compute power. While increased fees like suggested above should solve the incentive part, here's what could address the distinctness part: how about making the miner club invite-only, where a new joiner has to run a node for free (or for reduced mining rewards and fees) for some time period, while those rewards are going to the inviter?
Getting an invite would be super easy since many would find earning such "referral bonus" appealing, and it would encourage them to call for more people to become miners, expanding the network and awareness of Monero's existence.
Of course, the downside is that it requires that "probation period" where the invitee is paying the inviter because otherwise it would be asking for abuse of the referral system. This probation can disincentivize the invitees, however, it can be addressed by finding a balance between how long the probation lasts, and what portion of rewards the inviter is getting, which could even be dynamic or defined by the inviters, enforcing more "fair" probation tax for invitees through competition.

## techmetx11 | 2025-08-15T23:27:42+00:00
> how about making the miner club invite-only, where a new joiner has to run a node for free (or for reduced mining rewards and fees) for some time period, while those rewards are going to the inviter?

In my opinion, this sounds like the worst idea for a permissioned system I've ever heard, and would most likely just kill the whole coin entirely. I doubt anybody here wants a gatekeeping system

Not only does this system encourage exploitation, it makes Monero sound like a pyramid scheme, which will actually put off more people

## keriate | 2025-08-15T23:45:14+00:00
>In my opinion, this sounds like the worst idea for a permissioned system I've ever heard, and would most likely just kill the whole coin entirely. I doubt anybody here wants a gatekeeping system

As I mentioned, getting an invite would be as easy as looking it up on any Monero-related forum, tg channel, discord channel, etc. It can't kill the project because the project itself is already valuable both to miners and users thanks to mining incentives and real world use cases.

>Not only does this system encourage exploitation, it makes Monero sound like a pyramid scheme, which will actually put off more people

Exploitation should not be possible because the net amount of coins in circulation remains the same: for someone to win, someone should lose. So if you're a single entity inviting fake miners using your own hardware, you will not get anything out of it.
The perception thing is a different story, everyone might look at it differently.

## JavadAllen | 2025-08-15T23:45:16+00:00
Any solution that does not require a hard fork sounds great to me, especially the last one ( Number 3 on the comment update )
 Monero needs a better, **more powerful marketing** system ( They've never achieved 51% as devs mentioned ), and also we need to make Monero profitable for honest miners to continue mining and find more people to join the network.
 ( Let's not forget that many individual Monero miners jumped into the Qbic pool for the extra rewards ) . 

**Another hard fork would be a huge headache, especially with wallets and exchanges, and it further isolates the network ( Isolation = vulnerability).** 

Update:  The ones that are logical and don't require hard forks = 1- Require Block to be Signed by the Miner's Key 2- Using a Larger Network as our Finality Layer & 3- Do Nothing/Improve the Existing Protocol's Efficiency 



## techmetx11 | 2025-08-15T23:52:08+00:00
> As I mentioned, getting an invite would be as easy as looking it up on any Monero-related forum, tg channel, discord channel, etc. It can't kill the project because the project itself is already valuable both to miners and users thanks to mining incentives and real world use cases.

It would disincentivize new miners, since they would be getting no or reduced rewards for a undefined period of time, because the fruits of their labor are getting leeched by from the person who so happened to have a code to give them.
Which is why I'm thinking this just sounds like a MLM

Not only that, it would further incentivize centralized pools, because the miners can actually get more rewards than just mining on their own (referral), which would be a massive footgun for the coin

## keriate | 2025-08-16T00:06:00+00:00
>It would disincentivize new miners, since they would be getting no or reduced rewards for a undefined period of time, because the fruits of their labor are getting leeched by from the person who so happened to have a code to give them.

Fair, this is why I mentioned that the exact algorithm needs to be worked out somehow to strike the right balance to not make mining pointless for new joiners and encourage people to invite others at the same time.

>Not only that, it would further incentivize centralized pools, because the miners can actually get more rewards than just mining on their own (referral), which would be a massive footgun for the coin

If we assume that the entry tax is fixed and cannot be adjusted by miners, this can actually play out the opposite way: centralized miners will be getting more profit from being good actors, discouraging behaviour that can erode trust in the network. Important to note here that this referral system doesn't encourage people to join pools rather than mine solo (at least I don't see how), so it shouldn't make the network more centralized.

## Final-Phoenix | 2025-08-16T04:41:48+00:00
What is everyones opinion on Bawdys proposal?:

"** Time Adjusted Blockweight **

Right now, "longest chain" is determined solely on the basis of difficulty. But if we include time as a weighting factor, attackers would need 60-70% of HP to reorg 10 blocks. And 90%+ for a long chain reorg of 100 blocks or more.

The idea is simple. *Each node* records the UTC time that THEY PERSONALLY saw a block arrive. As blocks age, nodes *individually* calculate a linear upwards weight adjustment.

Meaning that a reorg attacker must have enough hash to reproduce the original difficulty of blocks already recorded by the network, PLUS the time-weighting.

Roughly, we might apply a 10-25% increase in weight of each block, for every 2 minutes of time that passes.

While this doesnt eliminate the possibility of reorgs, it significantly raises the bar. It can also be applied rather quickly; and has improved tradeoffs to simply applying a rolling N-block checkpoint.

<img width="1347" height="1046" alt="Image" src="https://github.com/user-attachments/assets/eed309ca-5c3d-423c-8afc-b13c10cb5427" />

"

https://xcancel.com/BawdyAnarchist_/status/1956537556532597238

## pAulseperformance | 2025-08-16T07:47:38+00:00
In a global network, propagation delays and local clock drift mean that nodes will never agree on the exact time they "saw" a block. Couldn't this lead to different nodes calculating different total chain weights, and risk a consensus failure or network split?

Also, what's going to stop an attacker faking timestamps or manipulating their clock on a private chain to give it an artificial time-weight advantage before broadcasting it?


## viktor4096 | 2025-08-16T07:56:44+00:00
@pAulseperformance regarding that, I have an idea

This proposal was made regarding RandomX. Currently, RandomX hashing is randomx(block_template) = a blake2b hash. The proposal was to re-hash the output again. Both the first and second hashes will be used to prevent spam.

Using this idea, whenever a miner finds a block, he pings the network with these hashes. The ping will traverse the network almost instantly, allowing other nodes to timestamp almost perfectly.

This way, an attacker would need to burn electricity to generate fake hashes that meets the block difficulty. At the same time, he'll need a lot of hashes to overwhelm the network.

## rnb42 | 2025-08-16T10:05:27+00:00
Another thing that could be added is perhaps a lock on block rewards similiar to what exists in Bitcoin right now (A miner can't spend his block reward until 100 blocks have passed). This could help in preventing reorgs.
I also find checkpointing like in BCH to be an interesting solution.

## CyberAshven | 2025-08-16T10:49:58+00:00
> What is everyones opinion on Bawdys proposal?:
> 
> "** Time Adjusted Blockweight **
> 
> Right now, "longest chain" is determined solely on the basis of difficulty. But if we include time as a weighting factor, attackers would need 60-70% of HP to reorg 10 blocks. And 90%+ for a long chain reorg of 100 blocks or more.
> 
> The idea is simple. *Each node* records the UTC time that THEY PERSONALLY saw a block arrive. As blocks age, nodes *individually* calculate a linear upwards weight adjustment.
> 
> Meaning that a reorg attacker must have enough hash to reproduce the original difficulty of blocks already recorded by the network, PLUS the time-weighting.
> 
> Roughly, we might apply a 10-25% increase in weight of each block, for every 2 minutes of time that passes.
> 
> While this doesnt eliminate the possibility of reorgs, it significantly raises the bar. It can also be applied rather quickly; and has improved tradeoffs to simply applying a rolling N-block checkpoint.
> 
> <img width="1347" height="1046" alt="Image" src="https://github.com/user-attachments/assets/eed309ca-5c3d-423c-8afc-b13c10cb5427" />
> 
> "
> 
> https://xcancel.com/BawdyAnarchist_/status/1956537556532597238

In favor👍 with proof of concept and testnet i think it will solve the issue

## shortwavesurfer2009 | 2025-08-16T11:15:14+00:00
> Another thing that could be added is perhaps a lock on block rewards similiar to what exists in Bitcoin right now (A miner can't spend his block reward until 100 blocks have passed). This could help in preventing reorgs. I also find checkpointing like in BCH to be an interesting solution.

I do believe this already exists. I want to say that a miner has to wait 60 blocks before their reward is unlockable.

## CyberAshven | 2025-08-16T11:41:32+00:00
I’ve been thinking what if Monero moved to Scrypt as its main proof-of-work? I don’t mean auxiliary mining or merge-mining, I mean making Scrypt the actual base chain algorithm. The reasoning is simple Monero can never realistically compete in SHA-256 territory because Bitcoin dominates that space. But in Scrypt, the only real competition is Litecoin and Dogecoin, and with Monero’s community and coin price with P2Pool mandatory setup, that space could be overtaken.

The idea would be to combine a CPU step, similar to how RandomX forces fairness, but here the CPU wouldn’t just be a weighting mechanism it would actually run the P2Pool node itself. In other words, every miner, even if they’re using an ASIC, would first run a lightweight CPU process that spins up the local P2Pool instance, and then the ASIC connects through that. This makes P2Pool mandatory unless you’re solo mining, and ensures that every participant is effectively a full mining node.

That design could give Monero thousands of independent nodes worldwide all bound into a decentralized pool, which makes it extremely hard for any single actor to capture enough hashrate to launch a 51% attack or push through deep reorgs like what we just saw with Qubic. On top of that, there’s already a scattered base of Scrypt silent home miners globally who could plug into this as well as industrial scale miners

## techmetx11 | 2025-08-16T11:51:21+00:00
> I’ve been thinking what if Monero moved to Scrypt as its main proof-of-work? I don’t mean auxiliary mining or merge-mining, I mean making Scrypt the actual base chain algorithm. The reasoning is simple Monero can never realistically compete in SHA-256 territory because Bitcoin dominates that space. But in Scrypt, the only real competition is Litecoin and Dogecoin, and with Monero’s community and coin price with P2Pool mandatory setup, that space could be overtaken.
> 
> The idea would be to combine a CPU step, similar to how RandomX forces fairness, but here the CPU wouldn’t just be a weighting mechanism it would actually run the P2Pool node itself. In other words, every miner, even if they’re using an ASIC, would first run a lightweight CPU process that spins up the local P2Pool instance, and then the ASIC connects through that. This makes P2Pool mandatory unless you’re solo mining, and ensures that every participant is effectively a full mining node.
> 
> That design could give Monero thousands of independent nodes worldwide all bound into a decentralized pool, which makes it extremely hard for any single actor to capture enough hashrate to launch a 51% attack or push through deep reorgs like what we just saw with Qubic. On top of that, there’s already a scattered base of Scrypt silent home miners globally who could plug into this as well as industrial scale miners

This just sounds like relaxing Monero's ASIC resistance, which will risk centralization of hashrate by ASIC companies, and making participation (for small miners) unfeasible.
I would not want a future where the only way to feasibly mine Monero is through a bunch of chips you cannot audit without decapping them and spending over a decade studying each transistor

## MoneroArbo | 2025-08-16T13:10:25+00:00
@fluffypony it occurs to me that if Tari hadn't changed mining for 1/3 to be XTM exclusive, non-merged randomx then Monero would have another 300-500 Megahashes/second. Given that Qubic could trivially target Tari if XMR were to fall, mayhaps it would be reasonable to again fully combine the RandomX hashrates.

## fluffypony | 2025-08-16T14:02:17+00:00
> [@fluffypony](https://github.com/fluffypony) it occurs to me that if Tari hadn't changed mining for 1/3 to be XTM exclusive, non-merged randomx then Monero would have another 300-500 Megahashes/second. Given that Qubic could trivially target Tari if XMR were to fall, mayhaps it would be reasonable to again fully combine the RandomX hashrates.

Qubic already mines and dumps XTM, they're very loud and obnoxious about it - part of the reason we did the split (which we've been very quiet about) was to try and pull them off the XMR side and split their focus.

## kayabaNerve | 2025-08-16T15:30:13+00:00
@Final-Phoenix That delays reorganizing to the best chain and actually wastes honest hash rate.


The premise of selfish mining is miners actively keep the best blockchain secret so they're the only ones who mine on it. This proposal means, even if the blockchain is public, miners will actively _ignore it_. Instead of competing for the next block, they'll spend their hash on an alternate chain with less work that they have worse footing on (as they have to do the work to find enough blocks to tie, and enough blocks to reorganize after).

This is ignoring the issues regarding chain splits.

## mechanikalk | 2025-08-16T16:54:13+00:00
# Monero: add 1 Hz “workshares” to harden liveness & selfish-mining resistance

## TL;DR

* Think of PoW as an **information sampling** process. Right now we get \~**1 sample every 120 s** (one block).
* Add a tiny, header-only **workshare** object that miners emit at **\~1 per second network-wide**.
* Let each block **claim** recent shares and make chain selection use **block weight = 120 + number of claimed shares** (simple mode).
* Result: \~**120× more independent samples** per 2 minutes ⇒ way tighter consensus, much harder to stall or game with <51% hashpower.
* Optional: split rewards **proportionally to contributed work** (prevents withholding). See “Proportional Splitting (PRS)” ideas: [https://arxiv.org/abs/2503.10185](https://arxiv.org/abs/2503.10185)


## Why this helps (intuition, not heavy math)

* Every valid proof (block or share) that points to the current parent is one **independent piece of evidence** about honest hash-rate and the “right” tip. More pieces = less uncertainty. (If you like names: this is the Cramér–Rao story—more samples ↓ variance.)
* In longest-chain designs without shares, a \~30–33% miner can sometimes profit by **withholding** (keep a private block, try to win a tie later).
  With **1 Hz shares**, the honest network’s public lead is being updated every second. A withheld block is fighting against \~120 public shares accumulating behind the honest tip. Unless the attacker is near **51%**, that game stops paying.

## Minimal spec

### 1) New object: `Workshare`

A small PoW header that references the current parent.

* **Fields (example):** parent hash, nVersion, nTime, nNonce, extra-nonce (or equivalent), and *no transactions*.
* **Validation:** `hash(header) < Ts` (share target). Parent must be known and valid. Timestamp sanity (e.g., within last 2–3 minutes).
* **Gossip:** new p2p inv/msg for shares. Relay and cache for \~2 block intervals.

### 2) Rate target: **1 share per second (network-wide)**

* Keep Monero’s 120 s block target untouched.
* Choose `Ts` so the network as a whole emits ≈ **120 shares per block**, on average. Roughly **\~7 bits easier** than the block target.
* You can adapt `Ts` with a simple EMA to keep \~1 Hz if total hash-rate drifts.

### 3) Blocks **claim** shares from the recent window

* Each block lists the **IDs** (or short IDs) of the shares it is claiming (those that point to the block’s parent or within its adopted tip set).
* Commit with a Merkle/accumulator root in the block header for easy verification.
* Shares can only be claimed that reference last block. This prevents "hoarding of shares".
* **Anti-double-claim:** a share can be claimed once; if two blocks try, “earliest-seen” or “highest difficulty” tie-break is fine.
* **Safety cap:** at most, say, **240 shares per block** counted for weight (DoS bound). Extra shares can still be included but ignored for weight.

### 4) Chain selection = **sum of weights**

Two options; start simple:

* **Simple mode (good enough):**
  Block contributes **1**, each claimed share contributes **+1**.
  *Block weight = 1 + #claimed shares.*
* **Stat-optimal (later):**
  Weight each proof by its **log-likelihood** (`~ -log p`), which is basically “more leading zeros = slightly more weight.” This squeezes a little more security per share but is optional; the simple mode already gives most of the win.

### 5) Rewards (optional but recommended)

* Split the coinbase **proportionally to contributed weight**: the block finder plus the owners of the claimed shares.
* This “information-proportional” split kills withholding incentives (you earn by broadcasting shares immediately). See PRS: [https://arxiv.org/abs/2503.10185](https://arxiv.org/abs/2503.10185)


## What changes in the code (high-level)

* **Consensus:** recognize `Workshare`, validate against `Ts`, allow blocks to commit a set of share IDs, add the weight rule. This is a scheduled network upgrade (Monero-style “hard fork” feature bump).
* **P2P:** add share inv/relay, light rate limiting.
* **Mempool analogue:** a small **sharepool** (headers only) with TTL \~ 2× block interval.
* **Miner template:** block builders gather recent valid shares, include IDs, compute new share-Merkle root, and report total weight.
* **DAA:** block difficulty stays as-is; share target `Ts` adjusted separately to hold \~1 Hz.


## Costs & limits

* **Bandwidth:** a share header can be \~100–150 bytes. At 1 Hz that’s \~100–150 B/s node-to-node—tiny compared to blocks.
* **CPU/state:** validate a small header and lookup parent; maintain a sharepool capped by time/size; verify claimed IDs against the pool.
* **DoS guards:** cap countable shares per block; reject shares older than a window; basic per-peer share rate limits.


## Expected impact (back-of-envelope)

* Today: \~1 independent sample per 120 s.
* With shares: \~**121** independent samples per 120 s.
* Security tails (reorg/finality) shrink roughly like `exp(-c × samples)`. Going from 1 → 121 samples is **orders of magnitude** better.
* Selfish mining: the classic “\~33% can benefit” region **collapses toward \~51%**, because honest evidence accumulates publicly every second.

## FAQ

* **Does this change privacy or transactions?** No, shares carry **no transactions**. Wallets don’t need changes.
* **What if block propagation is slow?** Shares still flow, so nodes converge on the same heavier tip even before the next block.
* **Can this be gamed by flooding shares?** PoW on shares + per-block caps + TTL + rate limits makes flooding expensive and bounded.
* **Why not make shares more/less frequent?** 1 Hz is a practical starting point (low bandwidth, big gain). You can tune `Ts` later.


If the team wants additional references, they can look at this paper: https://arxiv.org/abs/2503.10185

Or they can refer to the Quai Network codebase: https://github.com/dominant-strategies/go-quai/blob/main/consensus/progpow/consensus.go

Quai has been running workshare based PoW in mainnet for 8 months and in testnets for more than 2 years.

## giaki3003 | 2025-08-16T17:33:15+00:00
Currently an attacker can just spin up more machines/rent more hashrate. That doesn't change under a "workshares" model. You are trading slightly less effective selfish mining, slightly better liveness, for an extremely synchronous, high overhead implementation which is relatively untested in a real world scenario. Quai is a cryptocurrency with no real utility and a few thousand dollars worth of liquidity on some very questionable exchanges, so I don't personally think it can be touted as an example nor as a "reference implementation"

## mechanikalk | 2025-08-16T18:01:49+00:00
> Currently an attacker can just spin up more machines/rent more hashrate. That doesn't change under a "workshares" model. You are trading slightly less effective selfish mining, slightly better liveness, for an extremely synchronous, high overhead implementation which is relatively untested in a real world scenario. Quai is a cryptocurrency with no real utility and a few thousand dollars worth of liquidity on some very questionable exchanges, so I don't personally think it can be touted as an example nor as a "reference implementation"

Yes.

- Prevents selfish mining
- Improves liveness
- "high" overhead 150 bytes/sec

No here.
- There is no impact on the synchronicity requirement.

In terms of tested nature of "shares", Kaspa uses something similar in many blocks in an unstructured DAG. These blocks provide sampling, just like shares, but are significantly more overhead and computationally expensive because they have N^2 complexity in resolving state processing where N is their DAG width.

Not going to say anything is perfect, but shares get you much much closer to the 51% assumption.  Personally, I think its the first step that should be taken before moving to something like #135 ie PoS.

## Rucknium | 2025-08-16T19:01:37+00:00
This discussion has become disorganized. I will lock this issue. Please move discussion to MRL repo issues that describe a single specific proposal in the table in the top-level comment. If one does not exist yet for a specific proposal, feel free to make one. I reserve the right to request clarity in any new issues that get posted. Thank you.

# Action History
- Created by: kayabaNerve | 2025-08-08T20:13:38+00:00
