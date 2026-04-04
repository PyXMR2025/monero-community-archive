---
title: Time for a serious look at Proof of Work change
source_url: https://github.com/monero-project/research-lab/issues/12
author: shaolinfry
assignees: []
labels: []
created_at: '2017-08-07T02:29:18+00:00'
updated_at: '2024-06-15T21:11:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I believe it's time to seriously review the proof of work algorithm used in Monero in light of the very serious consequences we have all witness with mining centralization in the Bitcoin community.

Mining centralization takes some obvious and non obvious forms. Miners can centralize the network simply by accumulating a majority of hashrate which may be easier to do when there is only specialized hardware from limited sources.

The second form of centralization is more insidious, which is also currently observed in the Bitcoin mining ecosystem where one company commands the monopoly on ASIC hardware supply. This is detrimental to decentralization because the company is able to exert economic force against both competitors and it's own customers. Because they are the major supplier, new players can be quickly starved out of the market through anti-competitive pricing designed to suffocate a new company. In the case of customers, since there is an unlimited demand for mining, and a scarcity of equipment, mining equipment customers can be coerced economically with threats of ceasing new sales. All these things encourage and enforce a cartel that is both difficult to see, and difficult to tame.

It is unclear if the Monero proof of work can be optimized by specialized hardware.

Clearly the best defense against mining hardware monopoly is to make it uneconomical or impossible for specialist hardware to be created for Monero. If the proof of work is only viable on commodity hardware, such as GPU, it's much harder for a manufacture to dominate because GPUs have a wide range of applications and thus plenty GPUs available in the world from a diverse set. CPU only algos are obviously problematic due to botnets from hacked computers. GPUs don't suffer this problem since GPU hijack would be very obvious on PCs.

In any case, I believe Monero is in a precarious situation and given the clear lessons from Bitcoin, we should take proactive action to ensure Monero does not become the center of a similar situation.

# Discussion History
## othexmr | 2017-08-07T07:09:19+00:00
Agree on the principle.

We have different choice In an advent of a malicous miner takeover or wants to enforce his rules on the community:

1) Modify CryptoNight slightly  - it uses 4 different hashing algos, we could replace or modify them slightly so break unflexible hardware, this  should be easy to deal with  for our own  CPU and GPU mining software.

2) Use sth like Cuckoo, which claims to be harder to do on HW, which is think is totally unproven. It also has the downside of being bad for pool mining, i am sure smaller miners would't like this.

3) Switch to something really asic friendly like Blake, Skein or Keccak (which we use already), lowering the costs for asic miners to join the game and letting the market deal with it.

4) Come up with system that makes ASICS harder to do, like using the blockchain as a scratchpad for calculations
In all cases the community should decide that they want to support, UASF style, miners  have only 1 job - to validate transactions and mine blocks.


The main issue with every change is, how do we switch while the  blockchain keeps running?  we could allow 2 PoW for a while and gradually reduce the amount of blocks the old one is allowed to mine.


Slightly unrelated but we should also work on a p2pool like system to counter miner centralization, not  sure how to make this scaleable tho as the variance in ordinary p2pool  systems is hard to cope with for smaller miners.

## fluffypony | 2017-08-07T07:15:19+00:00
We've investigated this before, mostly around Cuckoo Cycle, and at some point it fell by the wayside. I support reopening this. I think that, at a minimum, we'd need to be able to provide:

- reasonable GPU mining kernels
- fast validation to prevent DoS risk
- use both as a mining PoW and as an on-handshake PoW

Some urgency might not be a bad idea, as the window in which we can make such broad and sweeping changes is narrowing.

## ghost | 2017-08-07T07:27:12+00:00
What really matters is what we should call the legacy chain?

## CameronRuggles | 2017-08-07T07:49:35+00:00
This might be a bit too radical/off topic but I think one issue that might be important to consider in PoW is the competitive exclusion principle: http://en.wikipedia.org/wiki/Competitive_exclusion_principle

"In ecology, the competitive exclusion principle...  is a proposition...  that two species competing for the same limiting resource cannot coexist at constant population values. When one species has even the slightest advantage over another, the one with the advantage will dominate in the long term. This leads either to the extinction of this competitor or to an evolutionary or behavioral shift toward a different ecological niche. The principle has been paraphrased in the maxim "complete competitors cannot coexist".

I think that miners are equal to different species that are direct competitors for the limiting resource which is the block reward. If the competitive exclusion principle is correct and applicable here, I think miner centralization might prove inevitable unless you can make it where there is effectively several different resources. This may still result in miner centralization, but likely only for one specific resource and not all. 

If you imagine a coin that has multiple PoW algorithms: ones optimized for GPUs, CPU, ASIC1 type 1, ASIC type 2, etc it might result in a better distribution of miners: some would be botnets, some would be ASIC farms, and others consumer grade hardware. 

Another thought might be to try to make mining linked closely with a volatile resource. If electricity prices fluctuated wildly among populations, perhaps that could prove to be useful. An electricity intensive mining algorithm optimized for consumer hardware and a low electricity consumption ASICs might be less likely be owned/controlled by the same entities. 


## kenmasters21 | 2017-08-07T08:40:26+00:00
Brainstorming and may be "forking" the main practical issue in hand, im am INTP can't help it... 

Do you think "tangle" type configuration (like IOTA) can be suitable and robust enough to fulfill the main function of Money- to be a storage of value that can be deferred through space/time? [https://www.youtube.com/watch?v=T2FJ9hH66b8]- being immutable, decentralized, widely connected enough, and attack proof?

A meshnet network of small devices that do their own validation and PoW simultaneously with a micro ASIC. 

Decentralization could be forced as a function of being rewarded by being the farthest away from concentration of these micro meshnet ASICs, therefore also expanding network/signal coverage and harder to become fallible through centralization. 
Don't know how could this could be spoof-free though (GPS location can be spoofed in cellphones currently)

edit: PS: this micro ASIC should be so simple to produce that you could massively 3D print it if you wanted to anywhere in the world with the bare minimum materials.

## hyc | 2017-08-07T10:49:22+00:00
Coincidentally, this paper came to my attention today - Proof of Work without all the Work
https://arxiv.org/pdf/1708.01285.pdf

Worth reading.

## Makeone11 | 2017-08-07T10:57:05+00:00
One potential attack vector that opens up once you opt for "decentralization" is that the amount of hardware out there that can be put to use in attacking the network becomes a lot higher. 

If you optimize for gpu(s) the investment cost of attacking the network isn't lost if monero goes down. If you compare that with dedicated ASICS the investment cost of attacking is lost if the network is harmed (either they find something new to mine using the same ASIC hardware or they're stuck with a brick). 

## gerardomoscatelli | 2017-08-07T11:00:26+00:00
Maybe this is a stupid idea but wouldn't a small reward paid for running a full node also prevent centralization? We run full nodes as a hobby and to verify blockchain's integrity but most people don't.

## JollyMort | 2017-08-07T11:33:52+00:00
Cuckoo can work with pool mining if a cuckoo round is at low enough difficulty. Worth reading: https://github.com/ignopeverell/grin/blob/master/doc/pow/pow.md

## dEBRUYNE-1 | 2017-08-07T12:26:54+00:00
@gegemos That may cause centralization, because people will put their node on services that guarantee the most uptime in order to maximize their rewards. 

## zachherbert | 2017-08-07T12:34:23+00:00
Taking an opposite viewpoint, at Sia we've decided to embrace ASICs. Mining centralization is definitely an issue, but so is network security and making sure incentives are properly aligned across all users on the network.

As we wrote in our blog post (https://blog.sia.tech/choosing-asics-for-sia-b318505b5b51), GPU mining is a "false panacea that ultimately leaves a cryptocurrency far more vulnerable to attack."

One main issue is 51% attacks. On GPUs, that will always be a serious risk, as a few large Ethereum GPU pools could coordinate to attack Monero's network. Additionally, we don't know for sure how many millions of GPUs sit in the hands of private companies, research centers, and so on. 

There is also a question of whether any algorithm is truly ASIC-resistant. 

Another main issue is incentives – we believe it's more healthy if miners use ASICs that can only mine a single coin. That way, they can't simply switch back and forth on their GPUs to whatever coin is most profitable at the time, and are more invested in that coin's success. 

At Sia, we decided to start a subsidiary called Obelisk to build the first ASIC miners for Siacoin and raise money via a presale. The idea is that, if we can widely distribute the initial hashrate, that should give a good foundation to keep away centralization. Of course we will have to keep making better chips, but we would continue to widely distribute them via presales and do our best to stay ahead of the competition.

This is of course going to be a huge decision for Monero, and I'd recommend that you observe how our Obelisk project at Sia goes over the next several months. We'll be shipping out ASIC miners by June 2018, so this group may be very interested in seeing how the switch goes.


## hyc | 2017-08-07T12:39:22+00:00
I kinda like the idea of tying mining more closely to a node, requiring blockchain lookups to crunch the PoW. Really, why are miners separate from nodes in the first place?

Right now operating a node is a pure expense, totally uncompensated. It would make sense to get at least some kind of payment, periodically. Binding mining to nodes will raise the hardware requirements for mining, making it less feasible to integrate entirely in a single chip. It will also raise the CPU cost of running a node, making it too expensive to run 24/7 on the majority of cloud providers.

## fluffypony | 2017-08-07T12:42:35+00:00
Moderator note: deleted long off-topic garbage post from anonymint.

## kim0 | 2017-08-07T13:34:43+00:00
I very much support bringing down the walls between "miners" and "users". All users should be miners and vice versa. I would like to suggest we consider biocryptics towards that goal. Basically, deriving keys from biometric information (nothing leaves your house though). The main benefit is that each human can run a single miner, not n miners where n is the number of cores they have access to. I do understand this approach can sound too wild, but let's give it a chance

For more details, please check out the [Cicada whitepaper](https://github.com/the-laughing-monkey/cicada-platform/blob/master/Cicada-WhitePaper-2016-10.13.GA.1.pdf) .. I'm also quoting perhaps the most interesting bits below. 

> The "Human Unique Identifier" (HUID) or "Single Identifier" or "Secure Identity Number" is an ID unique to each human on the planet. This allows us to prevent Sybil attacks and ensure everyone has a voice in the system. The HUID must be unique, incontrovertible, incorruptible, and not centrally stored or administered. 

>The HUID uses biometric markers to create public/private key pairs, guarded by passwords, which in turn are used to create IDs and linked sub-IDs. To be very clear, what we are talking about here is biocryptics NOT biometrics. Biocryptics are the intersection of biometrics and cryptography. The HUID is created by generating a public/private key pair from an iris scan and storing that ID in an identity blockchain, known as the HUID chain.

>The HUID has the special advantage of being largely immune or at least incredibly resistant to Sybil attacks, because it is unique to each person and cannot be reused in the system. To create the public/private key pair, we scan for biometric markers known as "minutiae points." We identify these critical minutiae points to create a "template" of the points, convert them into a hash, and use them as seeds for a pseudo-random number generator to create a public/private key pair, along with salt to create additional randomness.

>This public private/key pair will then be used to create an "info wallet." This is similar to a bitcoin wallet, but used for storing personally identifiable information (PII). The public key is run through a function to create a unique numerical ID for a person. The public/private key pair will include a built-in requirement to create a strong password, utilizing a rainbow table of prohibited weak passwords, enforced by the blockchain, to ensure good security practices.

## fluidvoice | 2017-08-07T14:00:44+00:00
I wonder if it would be helpful to have a feature where all miners are not anonymous to the users/nodes such that a node may have a blacklist of miners (which would require miner identities I guess) to exclude one's Tx rewards going to "bad actors".  This is a sort of voting power given to nodes.  

## pierce403 | 2017-08-07T15:01:47+00:00
> It is unclear if the Monero proof of work can be optimized by specialized hardware.

Is that the real issue?  It seems to me that Monero is one of the few coins out there that is not just being mined with a GPU, but there are several people out there mining on CPUs, and they aren't even at a significant disadvantage.  This is a very positive sign that the memory hardness of CryptoNight is working, and that ASICs would be uneconomical.  Other poorly thought out PoW algorithms (I'm thinking of things like PrimeCoin, MemoryCoin, etc) got optimized to hell and left everyone else out in the dust.

Monero is old enough and high profile enough that if building ASICs was economical, I think we would have seen movement in that direction by now.  It clearly isn't as asymmetric as Bitcoin where even 90nm ASICs could blow GPUs out of the water.  Remember that SHA256 was designed to be super cheap in hardware, it was one of NIST's requirements for the SHA competition, and CryptoNight was very much designed to be expensive in hardware.  Of course someone *could* design CryptoNight ASICs, but I doubt they would be able to compete with the economies of scale we get from commodity GPUs.

I'm a fan of algorithms like Yescrypt, Lyra2, Argon, etc, which have had a lot of work done on them in academia to show that they would be uneconomical to put into hardware, but weakening them to enable GPU mining would be really tricky and dangerous (look at the last couple Vertcoin PoW forks).  I've been impressed with how well CryptoNight has held up to attempts to shortcut the algorithm, and I think that unless there is really solid evidence that someone magic'd up a way to do it super cheap in hardware, I think switching PoW would do more harm than good.

## shelby3 | 2017-08-07T15:23:21+00:00
> Monero is old enough and high profile enough that if building ASICs was economical, I think we would have seen movement in that direction by now.

That is not necessarily the case if that someone who had the deep pockets required was preferring to keep it secret so it can run Monero as a Sybil attacked honeypot. How would we know? I posited [the only way we can know](https://gist.github.com/shelby3/5644d5ae82284b5f2bfb24160e62a608#detecting-the-existence-of-a-mining-oligarchy) is to have transaction revenue much greater than block reward and observe if the orphan rate skyrockets. If not, the mining is 51% controlled—otherwise _inconclusive_. I’m not advocating running such a potentially self-destructive experiment.

> Of course someone _could_ design CryptoNight ASICs, but I doubt they would be able to compete with the economies of scale we get from commodity GPUs.

Afaik, having the lowest hardware unit cost (due to high volume manufacturing) its amortization is largely irrelevant because it is a small component of the mining cost, which is dominated by electrical efficiency even though profitable lifespan is limited by Moore’s law. So the only economies-of-scale required is sufficient ROI on mining to payback the _capital cost_ of the ASIC R&D and fab setup. This threshold may or may not have been met yet given Monero is not even a $billion market cap yet, and considering likely higher capital costs you allude to.

Note that GPUs can be re-purposed to continue their utility beyond their mining profitability lifespan.

## ghost | 2017-08-07T15:47:05+00:00
No, don't fix what is not broken.

go back to Litecoin.

## QuickBASIC | 2017-08-07T16:03:25+00:00
@zachherbert We don't know the makeup of those Ethereum pools, but aren't you assuming that the miners in those pools would want to be complicit in committing a 51% attack. How many of those pools are made up of individual miners as opposed to centralized datacenters controlled by a company or individual? 


## shelby3 | 2017-08-07T16:08:52+00:00
> Coincidentally, this paper came to my attention today - Proof of Work without all the Work
> https://arxiv.org/pdf/1708.01285.pdf

Actually I thought of that conceptually before when I was trying to devise a solution for the liveness-gets-stuck issue that [I mentioned](https://gist.github.com/shelby3/67d990230e2dc9eb8be9e43e0b0b77a7) about Byteball, but didn’t bother to fully develop the model, because it has a very obvious and fatal flaw because they ostensibly didn’t model the economics of it. Their model is the provability that it can’t be gamed algorithmically. But afaics, they didn’t model the economic ramifications of their algorithm.

Their algorithm is essentially scaling the amount of PoW difficulty (that all mining node ID’s must have to survive a PoW challenge round) by the rate of changes to the ID set. So assuming there is no attacker, then everyone agrees to play nice then the difficulty remains low. But the specific flaw is its communism because it steals from those who have greater or low-cost hashrate and redistributes to the marginal miners, because every good or bad ID has the same weighted vote. Of course the same entity can create more than one ID to spread its hashrate, but this is attackable because if the threshold of their splits are exceeded by an attacker who issues too many ID joins/deletes per round, then the split IDs are deleted by the challenge round and amplify the attacker’s effect. So the economic implications are amplification instability else communism. We must understand the [economics of decentralized consensus](http://www.truthcoin.info/blog/pow-cheapest/).

Also it appears to me that it requires some trusted setup on the initial randomness to create a non-gamed ID member set for the committee which acts as the “server”. There may be other issues, as this is brand new so peer review is presumably lacking.

## b-g-goodell | 2017-08-07T18:00:40+00:00
Here's a quick pre-amble (3 brief points), then I'm going to comment on folks' individual responses. My entire point of view here is to look at decentralization and egalitarian mining as a matter of financial barriers to new users mining with a hashrate comparable to the current per-user hashrate, and a matter of long-term trends towards coalition mining. TLDR: lethos3 and pierce403, in my estimation, are correct.

Disclaimer: I am happy to be wrong, and I would rather be corrected than to continue disseminating false information. So ask questions and call me out on my mistakes. 

1) High variance is bad. All other things being equal, a system with high variance of per-user hashrate isinherently  more centralized than a system with low variance (in fact, this could be taken as a definition of centralization). The disparity between CPU/GPU/ASICs hashrates is orders of magnitude difference. Very few people would mine with a CPU at 1 H/s if they can mine with a GPU at 1 MH/s, and no one woul mine with a CPU at 1 H/s if the average per-user hashrate is 1 MH/s. Similarly, very few people would mine with a GPU at 1 MH/s if they can mine with a mining ASIC at 1 GH/s, especially if the average per-user hashrate is 1 GH/s. For an egalitarian mining process, every user should have approximately the same hashrate and therefore every user should have approximately the same equipment.

2) CPUs are egalitarian because many people already have them. We certainly can't provide every interested user in the world a big fancy ASIC mining rig, but every interested user has access to at least one CPU. In the interest of decentralization, then, is to determine a mining scheme that is not significantly easier using a GPU or an ASIC compared to a CPU. 

3) CryptoNight forces low efficiency in all equipment. The CryptoNote inventors developed CryptoNight, which is a hashing algorithm designed to i) require large swaths of cache so that no GPU or ASIC can complete a computation without going through the CPU and ii) require so much cache so as to not fit in a computer's L1 or L2 cache, only fit in a computer's L3 cache. Accessing L3 costs more time than any other way of accessing memory. Importantly, this is a fundamental property of modern computer design, and until a fundamental redesign of computer architecture takes place, this cache will always be slow.

That is to say: CryptoNight was designed to force every user, GPU or ASIC or CPU, to utilize the slowest part of the computer in every hash computation. Moreover, all modern human computers will be vulnerable to this slowdown, and will continue being vulnerable to it until a major overhaul of computer architecture takes place. Take 1, 2, and 3 together and I don't see a rather elegant implementation of a decentralized mining process.

IOW, I don't anticipate a long-term trend toward mining cartels due to PoW with Monero unless computer architecture starts to change.




Now, in response to comments:

shaolinfry: "I believe it's time to seriously review the proof of work algorithm used in Monero in light of the very serious consequences we have all witness with mining centralization in the Bitcoin community." The centralization of Bitcoin is directly due to ASICs and the impossibility for a CPU or even GPU miner to break even.

"Miners can centralize the network simply by accumulating a majority of hashrate which may be easier to do when there is only specialized hardware from limited sources." In this case, the word 'simply' is tricky. Like saying "all we need for fusion is to simply get two protons very close together." Accumulating a majority of hashrate right now can only be accomplished by state actors or large botnets mining on equipment without the owner's consent. In the first case (state actors), I don't consider this a reasonable threat model for several reasons (I can elaborate). The second case, I think, is an inevitable consequence of egalitarian, decentralized mining. In fact, I think this is a value of decentralized computing: if many coalitions are capable of launching an attack but any one coalition needs more than 50% of the network to make such an attack, then any one coalition is less likely to succeed.

"The second form of centralization is more insidious, which is also currently observed in the Bitcoin mining ecosystem where one company commands the monopoly on ASIC hardware supply." Disregarding the monopoly-ness, the sheer existence of specialized hardware that costs more than a CPU and is orders of magnitude more efficient leads to centralization. Add on top of that the idea that AMD might be the ones *truly* in control of a mining network... yeah.

"It is unclear if the Monero proof of work can be optimized by specialized hardware." <--- Completely incorrect. See above.

"If the proof of work is only viable on commodity hardware, such as GPU, it's much harder for a manufacture to dominate because GPUs have a wide range of applications and thus plenty GPUs available in the world from a diverse set." CPUs are also commodity hardware. Moreover, the hierarchy of minability goes like this: anything that can be mined on an ASIC can be mined on a GPU, and anything that can be mined on a GPU can be mined on a CPU. It's not really possible to construct a mining system that operates on a GPU but not a CPU or an ASIC. If you a computation can be efficiently performed with a GPU, an ASIC can usually be designed to do the same thing but more efficiently. If we design a mining game that is mine-able on GPUs much more efficiently than CPUs, and if Monero then sees a price increase, then ASICs would be just around the corner.

"CPU only algos are obviously problematic due to botnets from hacked computers. " I think this is a natural and inevitable consequence of any egalitarian system that has no punishment associated with collusion. In particular, the problem with botnets is that user systems have been compromised, not that a large swarm of computers are validating transactions, or that a single entity is in control of the swarm.  If we are concerned about a botnet controlled by a single entity coming in and rewriting our blockchain or selfishly mining, the solution is more competition between botnets, not less.



othexmr: "Modify CryptoNight slightly - it uses 4 different hashing algos, we could replace or modify them slightly so break unflexible hardware, this should be easy to deal with for our own CPU and GPU mining software." If we are concerned about the hashing algorithms being gamed into greater efficiency, you are correct that swapping them around would break inflexible hardware.  However, the bottleneck for CryptoNote mining is not in the four hashing algos that contribute to CryptoNight, the bottleneck is in the usage of the L3 cache. So a user who cleverly designs something that can handle the four hashing algorithms is still sunk in the water because his computer architecture is what's slowing him down, not computation of many hashes.

"Switch to something really asic friendly like Blake, Skein or Keccak (which we use already), lowering the costs for asic miners to join the game and letting the market deal with it." If we want to put up a financial barrier to new users running a node while centralizing mining power with the richest of Monero miners, then sure.

"Come up with system that makes ASICS harder to do, like using the blockchain as a scratchpad for calculations" <--- I don't know how you could use the blockchain as a scratchpad for calculations. But I know that CryptoNight is already more ASIC resistant than almost any other option around (short of designing our own hash functions).




fluffypony: "I think that, at a minimum, we'd need to be able to provide: reasonable GPU mining kernels, fast validation to prevent DoS risk, use both as a mining PoW and as an on-handshake PoW." Providing a GPU miner that is markedly more efficient than the CPU is a centralization move. The short-term benefit would be more miners (for a time... until all the CPU miners are flushed out), but the long-term cost of this would be that no one will mine with CPUs anymore.



CameronRuggles: Your observation about competitive exclusion between species is important. There is a behavioral version describing competitive exclusion between behavioral strategies and individuals deploying different strategies. The idea is not that only one species remains, but only one *behavioral strategy* remains. In our case, each miner is an individual, the resource being fought over is a nonce that makes a block's hash sufficiently small, and the strategy is the equipment they employ while mining. The competitive exclusion principle, then, implies that only one strategy for finding nonces (i.e. type of mining equipment) will remain after a sufficiently long period of time.

I have some ideas of what it might look like to compete for many resources. As you say, a mining game using more than one cryptographic hash function could possibly work... but it would require some thought. I'm not convinced this would be the right approach, but I find the idea interesting.


Makeone11: "If you optimize for gpu(s) the investment cost of attacking the network isn't lost if monero goes down. If you compare that with dedicated ASICS the investment cost of attacking is lost if the network is harmed (either they find something new to mine using the same ASIC hardware or they're stuck with a brick)."

If a GPU can do it, an ASIC can do it better.



gegemos: "Maybe this is a stupid idea but wouldn't a small reward paid for running a full node also prevent centralization? We run full nodes as a hobby and to verify blockchain's integrity but most people don't." <--- I think I fully support providing slightly larger block rewards to full nodes. As hyc points out, running a full node is pure expense. If we can come up with a way to offset the cost without rewarding users with enough personal resources to run a full node, I would support that, but I'm not convinced it's possible.

Maybe we could have a a block reward bonus on top of the usual block reward, where the bonus is inversely proportional to the number of full nodes on the network. Fewer nodes -> bigger bonus -> more nodes -> lower bonus -> fewer nodes -> ...



zachherbert: "Taking an opposite viewpoint, at Sia we've decided to embrace ASICs. Mining centralization is definitely an issue, but so is network security and making sure incentives are properly aligned across all users on the network." This is a logical way to go, maybe... except it puts up a barrier to an arbitrary user participating in the network, which in the end leads to fewer non-colluding users participating in the network, which risks all that netsec you were hoping for. After all, fewer coalitions mining means any one coalition has an easier time hitting 51%.  Your idea about incentives and miners using ASICS that can only mine a single coin does the same thing, by reducing the total number of participating users and hence reducing the total number of coalitions. Having said that, I can't see the future of an ASIC-based POW system that doesn't resemble the current problem in the bitcoin universe. That doesn't mean it can't exist, it means I have a failure of imagination.




kim0: "I would like to suggest we consider biocryptics towards that goal." Interesting idea. Identity-based encryption, where keys come from some arbitrary data like your e-mail address or a photograph of you (or a scan of your iris), has experienced some theoretical problems in the past and recently, where cryptanalysis is quite effective. Having said that, presuming we find a secure system... I'm not sure how you can verify that, say, an iris scan used to generate a pair of keys, actually came from a human instead of a random iris generator. If I can code up a piece of software that randomly generates realistic iris information, I can feed each randomly generated iris into the keygen and run as many bots as I like. As technology improves, we can also assume that arbitrarily realistic iris scans could be simulated by computers. In order to fix a problem like that, usually cryptographers introduce trusted third parties or certificate-based systems, where some authority determines if a real human is behind the iris. It's still an interesting idea.


pierce403, lethos3: Agreed.


shelby3: I am super happy to talk with you if you have a specific concrete proposal for POW. After all, in a high-txn-fee-with-respect-to-block-rewards environment, you are correct that PoW doesn't operate too well. I will also engage with you about your claimed honeypot situation if you identify all of your assumptions, fix the ones that are blatantly incorrect, and if you develop any verifiable concrete numbers on the complexity of solving the combinatorial problems associated with de-anonymizing a cryptonote blockchain. However, I will not engage with you if the conversation will resemble something like "Like it or not, you are going to use my solutions!!1 Checkmate, son!!112 Fluffypony is gestapo1l1khj." Your choice.

## iamsmooth | 2017-08-07T18:25:41+00:00
@pierce403 can you elaborate on this:

> look at the last couple Vertcoin PoW forks

for those of us who don't follow Vertcoin

What happened there and what did you learn from it?


## peronero | 2017-08-07T18:32:54+00:00
Not sure how to take seriously any 'decentralize mining' proposal that would centralize mining in two US-based corporations subject to export regulations that already restrict the proliferation of high-end hardware along political lines. Keeping commodity CPUs and architectures such as ARM, POWER, and OpenRISC competitive with the most powerful chips is surely a better approach to 'decentralization'...

## fluffypony | 2017-08-07T19:24:54+00:00
Removed another derailing post. Just a reminder to anyone passing by that this is a moderated issue on the research repo, and requires serious and/or academic responses. Known contributors preferred, but this repo is open and input from anyone is welcome. That said, derailing and nonsense will be moderated in order to keep the conversation on-topic.

## bigreddmachine | 2017-08-07T19:29:58+00:00
Please use markdown when replying to people, especially in big blocks. Most notably, "quote" someone by beginning their quote on a new line with a leading "greater than sign" followed by a space. Otherwise this is super tedious to read.

(A bit off topic but in the interest of the discussion... @fluffypony feel free to delete if you think too spammy.)

## ghost | 2017-08-07T19:38:21+00:00
Would it be possible to implement a cpu/gpu combination algorithm? 
That is to say tie it mostly to cpu but with the requirement that a certain amount of gpu power be involved in the calculations as well but only to a certain extent.

Could this not mitigate the botnets since most infected computers probably don't have a dedicated gpu and igpus are not that powerful to begin with anyways?

## hyc | 2017-08-07T19:46:20+00:00
That would also eliminate a lot of non-PC devices (phones etc.) as they tend to have poor GPU driver support for OpenCL/generic compute.

## bigreddmachine | 2017-08-07T19:48:07+00:00
@b-g-goodell, referring to @fluffypony's point and your response:

> > I think that, at a minimum, we'd need to be able to provide: reasonable GPU mining kernels, fast validation to prevent DoS risk, use both as a mining PoW and as an on-handshake PoW.
> 
> Providing a GPU miner that is markedly more efficient than the CPU is a centralization move. The short-term benefit would be more miners (for a time... until all the CPU miners are flushed out), but the long-term cost of this would be that no one will mine with CPUs anymore.

I believe the point he was making is that if we switch PoW and we switch to something that can still be mined with a GPU, we should make sure we have mining software that has been relatively optimized, otherwise someone can take advantage with private mining software and that defeats the purpose of the switch.

----

On the topic of CPU+GPU mineable algorithms, one thing I'd like to bring up here is that a consequence of the economics of Cryptonight mining being somewhat similar on both CPU and GPU is that this drives towards a state where GPU mining is actually *not* economical from an opportunity cost perspective, unless Monero's mining rewards are much greater than that of other coins that are only economical on GPUs. For example, today it might be profitable to mine ZEC, ETH, or XMR with a GPU. However, the fact that XMR is also profitable on CPU drives the reward per hash down relative to ZEC and ETH because CPUs can only mine XMR. As a result, anyone GPU mining XMR is incurring losses in terms of opportunity cost. If XMR rewards were much more valuable than everything else, this effect would lessen, as most hashrate would point to XMR regardless. But that's not the case today, nor likely in the near future, and therefore GPUs will tend towards those coins that are only GPU mineable.

## fluffypony | 2017-08-07T19:54:00+00:00
> I believe the point he was making is that if we switch PoW and we switch to something that can still be mined with a GPU, we should make sure we have mining software that has been relatively optimized, otherwise someone can take advantage with private mining software and that defeats the purpose of the switch.

Correct - anyone who was mining during the [artforz time period](http://www.ofnumbers.com/2014/04/20/how-artforz-changed-the-history-of-bitcoin-mining/) (BTC and/or LTC's predecessors, Tenebrix and Fairbrix) will know how icky things get when a subset of miners have access to a GPU miner and the rest don't.

## mbarkhau | 2017-08-07T20:03:55+00:00
I think Bram Cohen has an idea he calls "Proof of Space" which is worth pursuing. He hasn't published any details yet, but I have outlined my understanding of the idea here: https://gist.github.com/mbarkhau/00129f99e19cf28cbfb2cdf8c58c5f60

## bigreddmachine | 2017-08-07T20:12:08+00:00
@hyc said:

>  kinda like the idea of tying mining more closely to a node, requiring blockchain lookups to crunch the PoW. Really, why are miners separate from nodes in the first place?
> 
> Right now operating a node is a pure expense, totally uncompensated. It would make sense to get at least some kind of payment, periodically. Binding mining to nodes will raise the hardware requirements for mining, making it less feasible to integrate entirely in a single chip. It will also raise the CPU cost of running a node, making it too expensive to run 24/7 on the majority of cloud providers.

I'm not sure I follow your point, can you elaborate/clarify? Are you arguing miners should be required to run a node, or that node operators should be compensated just for running a node?

Mining *does* require a node. Pooled mining allows individual workers to delegate who runs that node, and maybe that's not ideal (though maybe it is). I know you know that, given the extensive work you've done on the various mining softwares, which is part why I'm confused...

## hyc | 2017-08-07T20:34:09+00:00
@bigreddmachine I was looking for a way to bind them together more tightly. E.g., so that if you're not running a node on the same box as your miner, the latency of talking to a remote node will significantly reduce your hashrate.

And yes, looking for ways to compensate people who just operate nodes. The simplest approach is to tell node operators to mine, and then it's a non-issue, they get compensated just like any miner.

## olarks | 2017-08-07T21:24:35+00:00
I see no reason why Cryptonight PoW should be changed in the near future. I was an advocate for Cuckoo Cycle, but with [recent performance improvements](https://github.com/tromp/cuckoo/issues/18) in Cuckoo Cycle the gap between CPU miners and GPU miners has widened by a considerable margin entirely assimilating CPUs, compromising PoW egalitarianism. 

The arguments for an egalitarian PoW like Cryptonight stem around Cryptonight being very accessible to both CPU and GPU miners making it very decentralized, but prone to a 51% by a large coordinated attack from supercomputers and large botnets.

The arguments for ASIC friendly PoWs like SHA256 stem around reduced risk of 51% attacks because presumably the ASICs are not as accessible as GPUs or CPUs. However, ASICs present a large centralization risk for entities who are fortunate enough to have easy access to ASICs, typically China, pushing out all other miner competition with large warehouse mining operations. Ultimately, resulting in closed door meetings of miners as present in Bitcoin agreeing on segwit2x.

In my opinion having an egalitarian PoW like Cryptonight is far more valuable despite 51% attack risks because over time the the network hashrate will grow as seen in Monero in the past year growing from sub 20MH/s to over 100MH/s, minimizing 51% risks.

As long as miners are responsible and distribute their hashrate to smaller pools, then a centralization of hashrate in a single pool will never be present and centralization issues that are so common in ASIC friendly coins will not weigh down on Monero.

If Cryptonight ASICs are ever produced and are able to greatly increase efficiency over GPU and CPU mining breaking PoW egalitarianism then a new PoW should be seeked out.

## mbarkhau | 2017-08-07T21:31:08+00:00
Maybe I'll just go over the motivation for the "Proof of Space" concept without getting into the implementation details.

In short, I think it is possible to use disk space as a resource for an alternative (or additional) proof of work system. Each node could dedicate 10-100GB of disk space to participate in the mining of new blocks and not require any specialized hardware. I think unused disk space is a much more distributed resource and I think it would contribute greatly to keep mining decentralized.

The devil is in the details of course and I won't claim to have thought everything through. But I think the core idea has merit and would be happy to go over it with somebody who has a better idea of what implementation issues there might be.

## olarks | 2017-08-07T21:32:06+00:00
@shelby3 If you have nothing else to contribute to this discussion and are only going to continue to derail the discussion at hand in this github issue please post elsewhere.

## banastas2 | 2017-08-08T04:49:53+00:00
Can someone clearly define "mining centralization" -> Is it too much hash rate by geography or pool or ownership? Is it possible to design and algo that understands geography?

A good approach is to devise a strategy to attack the perceived/foreseen problem by creating a system that "forces" change of protocol under certain circumstances.

I like the idea of compensating nodes at a variable rate that _increases_ as the concentration of mining (however defined) increases. Problem is intelligent coding that 'understands' centralization. 

My 2 cents as a complete outsider/non-programmer... :)

## benkloester | 2017-08-08T05:05:29+00:00
Peter Todd's [distinction](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2014-March/004818.html) between "mining - the act of validating and constructing new blocks, and hashing - the act of solving proof-of-work problems." is useful to think about. Centralization/concentration of either presents risks, but there may be natural reasons for the latter to decentralize (eg heat dissipation), so the former is more likely to be a focus of centralization. 

Making pools impossible probably prevents this but comes with its own trade-offs.

Paul Stztorc also has a decent [discussion](http://www.truthcoin.info/blog/mirage-miner-centralization/) of this question.

When I think of miner centralization, I tend to think of what Paul calls "Managerial Miner Concentration". Ie the concentration of power with few decision-making agents.

## apertamono | 2017-08-08T06:52:40+00:00
@mbarkhau Bram Cohen wasn't the first to invent Proof of Space. It's the algorithm used by Burstcoin. They call it Proof of Capacity. I think he wasn't aware of that. And it leads to hard-disk farms instead of GPU farms. You need multiple terabytes to be a competitive miner. That's not much of an improvement compared to GPU mining. A CPU-focused algorithm is better for decentralization. 

## mbarkhau | 2017-08-08T07:19:59+00:00
@ProkhorZ Thanks for the tip. I found this whitepaper which I will go over: https://eprint.iacr.org/2013/796.pdf

I'm not convinced that the centralization story is the same as for CPU/GPU/ASIC focused PoW methods. It seems to me that lots of people have idle disk capacity which they could put to use for mining at a marginal cost of practically zero. Maybe I'm missing something, but wouldn't it be hard to compete with that if you have to spend money to buy disks for your farm, when hundreds of thousands of computers are each contributing say 107GB (my current idle disk space). I also don't think the story is the same wrt. hardware specialization. The most cost efficient online storage technology (Ferromagnetic HDD) is the same that is already being used in consumer hardware and there are no specialized technologies such as ASIC which would give an orders of magnitude advantage to centralized miners.

## apertamono | 2017-08-08T07:41:11+00:00
@mbarkhau Yes, I agree that Proof of Capacity is more decentralized than ASICs. But it's unlikely that you'd get 100 casual miners for every 10 TB miner. The UX would have to be very user-friendly.

@othexmr said:
> We have different choice In an advent of a malicous miner takeover or wants to enforce his rules on the community

Since the discussion started with lessons learned from Bitcoin mining, let's take into account that we may not recognize an attacker before it's too late. For example, the Bitcoin community doesn't agree whether Bitcoin is being attacked or defended by Bitmain.

When I think through the strategy 'modify the algo just a bit to put an attacker on the wrong foot', the faster you change it, the better, so the optimal version is using multiple algos at the same time, the way DigiByte uses 5 competing algos separately.

@hyc Using the blockchain as a scratchpad is a fascinating idea. But wouldn't that make miners vulnerable to DDOS attacks?

As an altcoin historian with a limited understanding of cryptography, I don't see any obvious improvements to CryptoNight. I wouldn't want to change anything if I didn't know that Monero mining is extremely centralized already at the pool level: [two pools control 51% of the hashrate at the moment](http://minexmr.com/pools.html).

## mbarkhau | 2017-08-08T07:52:12+00:00
@ProkhorZ The marginal cost of 10TB across 100 casual miners is practically zero. Install the application so it boots at startup (maybe select a mining pool) and forget about it. The marginal cost of 10TB at todays prices for a centralized miner is ca 250 €.

## apertamono | 2017-08-08T12:33:19+00:00
@mbarkhau Does it matter that competitors who can't scale up have zero cost? (Actually hidden/subsidized cost.) Vegetable gardens don't make industrial farming unprofitable.

## mbarkhau | 2017-08-08T14:44:56+00:00
@ProkhorZ Vegetable gardens have a decidedly non-zero cost because people's time isn't free. Count the hours together you spend on the tomatoes in your garden and even at minimum wage they end up pretty expensive. The HDD based mining on the other hand is actually zero, neither hidden nor subsidized. At least that is the case if you only dedicate storage to mining, which you wouldn't have used otherwise anyway. The more significant cost is probably network traffic to participate in the mining.

## JollyMort | 2017-08-08T14:50:45+00:00
HDDs are the bottleneck of modern PCs. Having some additional I/O load would kill PCs usefulness whereas you can easily throttle CPU/GPU mining use and multitask. I'd never use my HDD to mine. For those with SSD, it's better, but it would be of interest to see how many write operations mining would cause as it would hasten the SSD's inevitable death. Then again, it's expensive and I need my precious space for storing actual files. Again, would not SSD mine. I think the HDD mining concept is rather misguided, sorry to say.

## mbarkhau | 2017-08-08T16:01:58+00:00
@JollyMort The I/O load for responding to a single challenge is a single seek operation (assuming the index of hashes is in memory) and reading maybe one kilobyte of data. The number of challenges corresponds to the number of blocks generated, so for monero one seek every two minutes. In other words, the I/O load is minimal.

The main I/O load is generated during (re)populating of the hash database, this might only be required every few weeks or so and then the CPU load would be more problematic than the disk I/O.

The idea is Proof of Space, not Proof of Throughput or Proof of IOPS.

## ghost | 2017-08-08T20:35:13+00:00
It's simply too late now, people are welcome to launch an altmonero with a different PoW. I have not seen a rebuttal of the points brought forth by @b-g-goodell, there is nothing wrong with Cryptonight currently, and for the foreseeable future, as it makes sure the slowest parts of the machine need to process the hashes.

## moneromooo-monero | 2017-08-08T22:16:19+00:00
> there is nothing wrong with Cryptonight currently, 

Cryptonight is slow to verify.

## ghost | 2017-08-08T23:43:10+00:00
Worth note @shaolinfry is the same guy that out of nowhere created the [UASF](https://medium.com/@metalzip/segwit-locked-in-on-bitcoin-thanks-for-bip148-633ef55f655e) movement in Bitcoin which aims to bypass the nakamoto consensus that relies on miners and nodes on the same page and not on war against each other (a war that nodes lose because they don't actually secure the ledger) and opened a dangerous precedent of nodes unilaterally ''modifying'' a network, he started this over at Litecoin and after running it to the ground with Segwit [abandoned](https://twitter.com/shaolinfry/status/889904255435452416) the development there and appeared here, he clearly has a hidden agenda here and doesn't give 2 piconero to Monero.

>Cryptonight is slow to verify.

and it works.

## kenmasters21 | 2017-08-08T23:49:39+00:00
I'm a nobody but I vouch for the creation of a new coin in which all problems that plague the current ones are overcome, and if be needed, create a new one again and again until the evolution of a system that maximizes freedom and the disposal of private property, boundless, and wealth preservation is perfected.
Slaves no more to concentrated malicious powers, whether governments, miners, mafias or anybody.

## Gingeropolous | 2017-08-09T03:36:58+00:00
@moneromooo-monero said
> Cryptonight is slow to verify.

What is the transaction rate at which this will actually become a problem?  This seems to me like a similar "problem" as the block size. As long as technology advances, so will the verification speed. Cryptonight does what a lot of other aspects of Monero do - tie a critical element of the network's function to an aspect of the physical world to void the need of human intervention. I don't fully understand the mechanisms of cryptonight, but from what I do understand, it exploits a fundamentally challenging aspect of computing, in general, to achieve its egalitarian nature - the communication between a CPU and memory. Basically, if a new technology is developed that drastically increases the speed between a processing unit and its memory, this technology will permeate every aspect of computing - consumer CPUs, server CPUs, GPUs, phone CPUs, toaster SOCs, you name it. 

Thus, i don't think hashing centralization is a problem. However, I am concerned about mining (block formation) centralization. Pooled mining. At one end of the spectrum, I say we move to cuckoo cycle (once its been figured out to work as I hope it does). If its prevents pooled mining, great. The problem is that a large entity could just control a lot of CPUs, so in effect it could end up with a very unequal distribution of hashing and mining power. I.e., 5000 individuals with 1 hash/s each and one individual with 5000 h/s. And will those small miners continue mining without seeing any rewards? 

@pierce403 said
> Monero is old enough and high profile enough that if building ASICs was economical, I think we would have seen movement in that direction by now. 

As mentioned elsewhere, its possible this could occur without us knowing. Though the adage "selling pick axes during a gold rush is more profitable than mining gold" applies here, so perhaps they don't exist. 

In conclusion, I think cryptonight is currently adequate to inhibit ASIC development. However, I think a plan should be in place to be acted upon in the event of ASIC development, or perhaps a plan to just fork PoW every n years. In my mind, this has sort of been an unwritten social contract in Monero to date, but I think the deterrent nature of such a policy would add to the inhibition of ASIC development. If a potential ASIC developer knows that upon public release of their ASIC (or in n years) that Monero will shift PoW, they might not make an ASIC. And even if they did create an ASIC, they would have to adopt a some sort of "stealth" policy to avoid detection, which could be in the form of distributing their hashrate to different pools or slowly spinning up their hardware over multiple years. 

I don't have a conclusion regarding pooled mining. We have yet to see how smart mining will play out, and we really don't have a means to actually measure its effectiveness (besides public pool tracking and inferring unknown hashrate to be solo miners). I think p2pool would be of great benefit to the monero network infrastructure and should be the focus of development and research. I also speculate that the mining infrastructure will change as the use of monero increases and the block reward decreases. It may be that, in the future, mining is not economical enough for professional miners, and instead private, solo miners may dominate the network. Part of the reason block rewards exist is to boot strap the network by distributing the currency. After this primary emission, the behavior of the network may be vastly different than it is today. Finding small blocks may be advantageous because they propagate the network faster, but a big pool will want to mine big blocks so they can pack them full of transactions. 

Maybe a way to combat pooled mining is to find a way to increase the latency between a hasher and the pool. I think this was what @hyc was hinting at. 

## banastas2 | 2017-08-09T03:39:05+00:00
Thank you @benkloester - both were helpful readings but they don't help get us anywhere concrete. Could not help but smile at Paul's conclusion "... in order to have a conversation, the conversation has to actually be about something."

But, we're human and we're comfortable operating in a fuzzy world. 

Let's say the fear is about 'centralization' of 'managerial control' of mining. For all practical purposes this signifies pool operators since we can't be worried about the kid in Hangzhou colluding with the kid in the UK.

So, if the problem is reduced to discouraging very large pools, then _some_ node compensation will help mitigate the problem. How much compensation can be made variable to answer the concentration seen by the network. What I don't know is if it would be practical for a mining pool to present itself to the network as many nodes? Otherwise, with CPU compensation it becomes a problem of mitigating against bot-mining?

- I don't understand @dEBRUYNE-1 how node compensation encourages centralization?
- @b-g-goodell I thought the idea is to maximize the number of nodes so that you want the bonus reward to larger the more nodes there are -- am I missing something?

 

## wavepruner | 2017-08-09T04:33:21+00:00
Howdy all, random trader here. I'm not much of a coder but I've studied several cryptocurrencies and been around since 2012. I've also been following Monero since the announcement on Bitcoin Talk.

I find Proof-of-Capacity incredibly intriguing, and BURST, as @mbarkhau said, is the first (and only) implementation in a cryptocurrency. I don't see any harm to decentralization from mining farms (which are always inevitable imo); what's important is that the mining hardware is readily available, and electricity requirements minimal, so newcomers can start easily and small miners are able to turn a profit (or at least break even). Proof-of-Capacity satisfies these requirements, as storage space will always be readily available and cannot be optimized dramatically by specially designed hardware, and storage itself uses no electricity. Once "plots" are written to a disk, they only need to be read from time-to-time to find blocks. No continuous write operations are necessary. Also, since electricity requirements are negligible, locations for miners/mining farms are not limited to areas with free electricity, which happens to be mostly China. I suspect that the cultural differences between Bitcoin's Western development team and Eastern miners play a big role in the breakdown of communication between the two sides.

Ultimately though, any Proof-of-whatever algorithm that uses readily available hardware lends itself to being attacked by any actors with significant resources. That is, until there are so many miners that no one actor can possibly cobble together enough hardware to surpass them all. That point is probably long into the future though for Monero or any other altcoin. ASICs solve this problem since it is probably extremely difficult for even the most well funded actors to design and build their own ASICs faster and better than the main industry can. Anonymous cryptocurrencies like Monero are the most likely to be attacked by a nation-state I think, for obvious reasons, so ASICs for Monero wouldn't be all bad....(Just had a thought though, a nation-state could just buy all the newly manufactured ASICs from whatever suppliers there were, so maybe ASICs are not good for fighting off nation-states after all.)

Back to BURST, the network is currently under attack. I'm not familiar with the details, but I believe it is a DDoS vulnerability, and not just someone doing a 51% attack. Something as new as Proof-of-Capacity may not be wise to implement on a network that is already being used by individuals in need of financial privacy.

That being said, I'd love to see a Cryptonote coin with Proof-of-Capacity run by a team as capable as y'all in the Monero project. That would potentially solve the two biggest issues with cryptocurrencies with one coin, that is, anonymity/fungibility and mining decentralization. In my opinion, it is impossible for any of us to predict how this will all shake out, so it's best to have several solutions(i.e. cryptocurrencies) in the works, and eventually one(or a few niches) will eventually win.

## wavepruner | 2017-08-09T04:35:52+00:00
Also, regarding node compensation, mining and running a full node used to go hand-in-hand before mining pools were the norm. Mining with a pool means that you no longer have to run a full node to mine (the pool operator still has to run a full node). The Bitcoin community has been talking about compensating nodes for a long long time, but no one has come up with a solution afaik.

## benkloester | 2017-08-09T05:32:20+00:00
Isn't that because if we're talking about rewarding nodes just for being nodes, you'd need to solve the Sybil attack problem, but such solutions as we have available collapse into one of the existing proof-of-somethings, be it Work, Stake or even Capacity?

One solution to reducing agent centralization is to make pools impossible, or to somehow introduce incentives that create negative feedback against pool size - ie profitability is somehow reduced with pool size.

Andrew Miller has done some [work](https://bitcointalk.org/index.php?topic=309073.0) on the former though I'm not sure what happened with it, and I believe it relies on zk-SNARKS (haven't read the white paper)

## JollyMort | 2017-08-09T05:55:44+00:00
Could we have a separate circuit for nodes? Like some mini-PoW challenge, taking random places of blockchain + block header as input and spitting out a PoW which gives participating nodes a little reward. Cuckoo seems perfect for this precisely because many can't simultaneously work on the same problem if the parameters are set so. The reward would not go to the node first to solve, but instead just let them be part of the pool from which a random winner is picked based on some random variable like the next block hash.

## anonimal | 2017-08-09T06:46:26+00:00
>Worth note @shaolinfry is the same guy that out of nowhere created the UASF movement in Bitcoin which aims to bypass the nakamoto consensus that relies on miners and nodes on the same page and not on war against each other (a war that nodes lose because they don't actually secure the ledger) and opened a dangerous precedent of nodes unilaterally ''modifying'' a network, he started this over at Litecoin and after running it to the ground with Segwit abandoned the development there and appeared here, he clearly has a hidden agenda here and doesn't give 2 piconero to Monero.

@lethos3 I did find it odd that he appeared here out of nowhere with an ambition to stir the pot. Perhaps he can comment further?

## mbarkhau | 2017-08-09T07:35:50+00:00
@catcow Do you have any more info on the DDoS Attack that is happening to BURST? It would be interesting to see if there are ways to protect against it in any new Proof-of-Capacity implementation.

## bigreddmachine | 2017-08-09T13:16:56+00:00
@lethos3, @anonimal - It doesn't matter so much who authors an idea as it does whether the idea is good. I read the original posted issue as saying "Please don't pretend this is solved, unless you know it either actually is solved or you know it is unsolvable." Let's explore whether the idea is good, rather than whether the person is good.

---

To talk about Proof of Work and whether/when to change it, we need to recall the purpose of PoW, nicely spelled out in the Satoshi white paper and summarized here:

1. The role of PoW is to allow consensus on the timestamp server that establishes the entire history of transactions.
2. PoW brings consensus by stating that the chain with the most work that follows the established consensus rules is the correct timestamp server.
3. PoW consensus only works because miners are incentivized to be honest via the block reward and transaction fees. If these incentives are ever outweighed by some other factor, then PoW consensus will become unstable or fail.
4. Therefore, miners have one job: uphold and secure the rules established by the network. Miners are the only ones paid because they must be incentivized to work towards consensus and not disrupt it.

Two major ramifications come from this: 1) miners do not set the consensus rules but rather uphold them, and 2) if miners ever stop doing their jobs then the time comes to "fire" the miners via a change of PoW. Miners work for the network of users, and just like any job if the miners stop doing what they are paid to do then they must go.

But changing the PoW algorithm only works if it also means a change of hardware required for PoW. The reason is simple. If CPUs and/or GPUs are used to secure the network before the fork and the same are used to secure the network after the fork, then it's highly likely that you won't see any turnover in miners and therefore the PoW change does nothing to combat miners working against the network. This is actually an argument then that ASICs conceivably are the optimal state of mining because that makes miners the most "fireable". ASICs after a fork become paperweights, adding incentive for ASIC miners to work for rather than against the network.

Therefore, while I agree that the Cryptonight PoW should be analyzed and made better from a performance standpoint, I disagree that a PoW change is needed at this time. I do think it would be good to have an alternative ready and waiting however (if that alternative uses different hardware), as this makes "firing" miners that have stopped working for the network possible. This might take the form of a perpetually threatened UAHF to a new PoW. 

One last thought: I'm not convinced an "egalitarian" PoW ensures mining decentralization. Mining will always move towards a state of semi-centralization because economies of scale and regional cost advantages will always be an important factor in mining. Egalitarian PoW helps level the playing field, but dreams of establishing a PoW ecosystem that follows the "one CPU one vote" vision where every user shares equal responsibility in securing the network are unfounded. Mining will always consolidate around players that can afford the investment. The only thing CPU and/or GPU mining helps with here is helping keep hardware access less game-able.

## ghost | 2017-08-09T17:12:28+00:00
@bigreddmachine Ok, his idea is very bad, terrible, consensus changing when more than half of the main emission is done much like in Bitcoin. NACK etc.

## fluffypony | 2017-08-09T17:33:24+00:00
@lethos3 three things to consider:

1. We didn't design CryptoNight. We have a fairly good grasp of the mechanics thanks to people like Prof. Dave G Andersen (who commented the source code), but the lack of a deep understanding of the algorithm is disconcerting at best, dangerous at worst. After all, the implementation was poisoned in two different ways at the outset (which we caught early on), so there's always the very small risk that a crafty trick remains.

2. There is little-to-no formal research on CryptoNight, unlike things like SHA2 or SHA3 or Cuckoo Cycle. This, again, has lead to a set of assumptions, such as you claiming that it "isn't broken" when it very well may be.

3. CryptoNight's slow validation presents a MASSIVE and unfixable DoS risk. Something like Cuckoo Cycle provides extremely fast validation, which means it costs more to create attack transactions/blocks than to validate them.

Also I'm not sure what emission has to do with PoW - the one is economic and part of the social contract and must not change, the other is a security mechanism and MUST BE ABLE TO ADAPT to advancing attacks. If we can't rapidly change our security mechanisms to provide ever greater security on an ongoing basis then this project is as good as dead.

## anonimal | 2017-08-09T18:55:56+00:00
>Let's explore whether the idea is good, rather than whether the person is good.

@bigreddmachine they can be mutually exclusive. A wolf in sheep's clothing, with a good idea of which the sheep cannot see as a threat (because they're sheep), is certainly not a good idea. We're not all sheep, but we can't pretend that we are always aware of every aspect of an idea. As such, we can use the repeating of history as a measurement of judgment (history almost always repeats itself).

## Dr-facecancer | 2017-08-10T10:14:12+00:00
I really agree with @hyc about the 1 node 1 miner concept.This can breakup mining pools and create more decentralized network.Of course this hinges on being able to CPU/Gpu mine simultaneously.Also having a static probability for CPU miners to earn block rewards with cuckoo cycles like jollymort suggested could possibly increase hashpower exponentialy. This just causes a problem of what magnitude this effects larger solo miners but if they are Also solo mining with a static probability of reward it most likely balances out. (Insert mathematical proof)??

## onidlo | 2017-08-10T10:35:44+00:00
@Dr-facecancer I think that mining pools are the only protection of small miners against big miners. A small miner doesn't want to run his/her node 7 months and then get finally **a lot of** money at once (by mining a block). It is better to share their profits during that period and get paid regularly by smaller amounts of money. 
We need to distinguish between pools and big miners, who pretend to be pools :-)

## Dr-facecancer | 2017-08-10T10:40:05+00:00
@onidlo How do you make that distinction?

## LordMajestros | 2017-08-10T10:40:27+00:00
How easy is that? A big miner can easily connect to a known pool. He then becomes a big miner at a pool. A merging of identities.

## ghost | 2017-08-10T14:46:26+00:00
@fluffypony I'm still not convinced the PoW needs change.

## onidlo | 2017-08-10T15:17:10+00:00
@Dr-facecancer, @hyc, would you mine, if you win a block once per year? Even it would be a lot of money, lets say  6.74 XMR would be equal to 6 740 USD. A lot of miners have already answered this question for themselves - they do not want to risk, spent money for electricity for one year and wait for lucky day. And therefore they joined a pool to have regular income.

On the other hand, if you are a big miner with many devices - lets say you have 10% of all hashrate, you win every day 10% of all blocks (24hours*60min/2min=720 blocks). So you earn 72x 6 740 USD in an avarage day. Sometimes you get 50x 7640 USD, the next day you get 100x 6 740 USD. You don't risk too much. You don't need a pool.

There are no problems with pools, which members are small miners. Take Slushpool as an example (I think it is still the biggest non-Chinese bitcoin pool). What's more, small miners can anytime change a pool if they are not happy with its direction. 

What you actually suggest is to get rid off small miners and allow only big miners to be profitable. This is not decentralization.

## QuickBASIC | 2017-08-10T15:21:27+00:00
> I'm still not convinced the PoW needs change.

@lethos3 Since this is a discussion on a research repo can you put forth any counterpoints other than, it's not broken so don't change it. Saying you're not convinced is not an argument.

## ghost | 2017-08-10T16:25:39+00:00
@QuickBASIC if you want to change a working system you better have convincing arguments FOR, the onus is on you.

I rather be wrong than let outside forces easily subvert Monero for their own hidden agendas, this is my last comment on this subject here.

## QuickBASIC | 2017-08-10T20:16:55+00:00
@lethos3 I don't want to get stuck in a FOR... LOOP, so I'll suggest you scroll up and read fluffypony's last comment again. I agree with him that it's disconcerting that we don't know for certain whether there's any problems with the algorithm that's currently being used.

## Dr-facecancer | 2017-08-12T05:46:43+00:00
@onidlo, I think making every miner run a node would have a more adverse effect on large miners.It would also level the playing field a bit for small miners, you can still pool nodes but hardware and electricity cost increases quite a bit if you plan on megahashing.Also I know this wont be popular but a hash cap per node and pool might be useful.So if you can gpu/cpu mine + run a node I think we wont lose much hashpower and it would actually attract more small time cpu/gpu miners if they were able to be more competetive.

## JollyMort | 2017-08-12T08:47:36+00:00
Which is the problem we are solving, again? It's already solved by CryptoNight, no? Central planning of anything seems like a horrible idea, and "hash cap per node" looks like one of those measures. We must always be careful not to fall into the [perverse incentives](https://en.wikipedia.org/wiki/Perverse_incentive) trap.

Seems to me that it's 2 different philosophies which are being evaluated: specialized hardware vs consumer grade hardware. And even with the first, decentralization looks possible, as Bitcoin proved.

Decentralized != Distributed. As long as mining power is free to change center(s), mining will be decentralized.

Sure, it's a topic of research and maybe it takes us to interesting places but I don't agree it's "time for a serious look". On what grounds would it be so serious as the title implies? Where's the evidence? Where's the analysis? If someone wants to do research, he's free to do it and share the results. I don't see any new information presented in this thread in favor of the "there's a problem" view. Until then, I fear the signal-to-noise ratio of this discussion could drop close to 0.

As for the node incentives, not all incentives have to be monetary. This is something often forgotten in this space. But yeah, finding a way to add some incentive to nodes seems like a worthwhile goal. Especially if one day we go with pruning, and want to make sure there are some archival nodes out there.

## onidlo | 2017-08-12T09:29:53+00:00
@Dr-facecancer I agree with you! I reacted to your statement: "1 node 1 miner concept ... can breakup mining pools". Now you are talking about large miners instead of pools, so that's correct. We need to distinguish between pools and big miners, who pretend to be pools :-)

## iamsmooth | 2017-08-12T10:01:35+00:00
I've never been sold on the alleged denial-of-service threat, especially not a massive one. To accomplish the DoS requires that the attacker, who will be disconnected upon sending a bad PoW, reestablish a new connection each time while at the same time avoiding being banned or triggering network-level DoS mitigations. 

Historically when the original (unoptimized, de-optimized, whatever you want to call it) cryptonight implemention came on the scene it took 1-2 seconds to validate a hash and it was widely criticized as being a massive DoS issue (which, at that speed, it likely was). But after optimization it now only takes 20ms or so (one core, so on a multicore system this doesn't by itself deny service all that much), and the original concern has clearly already been mitigated to a significant degree (though whether sufficiently so is less clear).

Also this statement is incorrect:
> Cuckoo Cycle provides extremely fast validation,  which means it costs more to create attack transactions/blocks than to validate them.

In fact, creating attack PoW is generally free because it is by definition bad/fake, and might as well be random, so there is no actual asymmetry. It only costs more to create _real_ PoW values (essentially mining, at some difficulty at least) which is of no use to an attacker.

The main difference is simply that the _absolute_ speed of verification is faster, which may or may not matter much in practice (as discussed above). At some point it is _fast enough_, although we don't know where that point lies.

Also, there is a method that can be used to essentially equalize the CPU required by an attacker of an algorithm like cryptonight, should it be necessarily. That is to store some intermediate values at appropriate intervals while computing the hash, and requiring these be sent along with the block. As soon as one of these values fails to match during verification you can reject the hash without continuing. Garbage/random values would fail almost immediately, while producing matching intermediate values would require the attacker to do equivalent work.

@bigreddmachine

Your last paragraph reads a lot like a straw man fallacy to me. I don't think anyone has claimed that an idealized one-cpu one-vote would ever be achieved. But in that very same paragraph you dismiss a lot of advantages to a _more egalitarian_ algorithm including greater pressure on those who do achieve economies of scale to remain honest because they are less likely to achieve total dominance, and preventing access to hardware from itself becoming a source of (potentially catastrophic) centralization. 

One other quibble. In addition to the consensus role you described (enumerated list), PoW also serves to distribute coins without becoming a source of concentrated wealth or power that may serve to undermine the legitimacy of the token or the ability of the broader base of users and investors to have any influence. To serve this role requires that mining remain economically competitive and lack significant barriers to entry. An oligopoly of miners who are able to exclude entrants and mine at a high sustained profit margin might work perfectly fine from the point of view of timestamping (hell, even an actual monopoly might work if, as satoshi suggested, the monopoly miner sees mining honestly as more profitable than attacking the network) but would be a massive fail for distribution.

I agree on the point of at least thinking about alternatives in the event it becomes necessary to 'fire the miners'.

## Dr-facecancer | 2017-08-12T13:49:29+00:00
@JollyMort Don't really understand how hash cap per node would be "central planning" it's an exchange of an apparently horrible idea.It's also a security solution for having botnets or asics pointed at an algorithm in my opinion.Im pretty sure it would never be something that this community would support.Applied to the context of this thread it might be noise,I may be mistaken in thinking this thread was about the security of an algo.However I watched hashpower increase 5x in about a three day period is this a security concern to anyone else?Is this normal?

## onidlo | 2017-08-14T10:16:14+00:00
This article is worth reading:

**Quantifying Decentralization**
_We must be able to measure blockchain decentralization before we can improve it._

In this post we propose the minimum Nakamoto coefficient as a simple, quantitative measure of a system’s decentralization, motivated by the well-known Gini coefficient and Lorenz curve.

More here: https://news.21.co/quantifying-decentralization-e39db233c28e

## DanielPlante | 2017-08-16T06:54:45+00:00
There is a PoW + PoResource (ie, DRAM) that can't be spoofed.

The explanation is here: https://twitter.com/Daniel_Plante/status/846930293164457984

I'll be happy to field any questions, but seriously, stop and think, and re-read before you ask. It's quite simple. It involves hashing, and DRAM.


## hyc | 2017-08-16T12:35:52+00:00
@DanielPlante sorry but that's ridiculous. If you want your suggestion to be taken seriously, write it down in a proper long-format medium. Not a series of tweets. Even a gist here on github would be better. Otherwise, if you actually believe your design is so obvious that it can be adequately explained 140 chars at a time, you're delusional.

## DanielPlante | 2017-08-17T03:43:42+00:00
This GitHub UI is ridonculous. How do I respond to the last comment? well, here goes: hyc, the tweet storm would take you just as much time time to read as an in-line post here, except it would take me several hours to reformat for this site. So did you read it? Do you have any insights to offer? I said the approach was ungamable. I would love to be proved wrong.

## DanielPlante | 2017-08-17T03:45:18+00:00
PS -I'm @Daniel_Plante on twitter.

## javilm | 2017-08-17T04:39:58+00:00
I have to agree with @hyc. A series of loosely-connected tweets is not the appropriate medium to propose an algorithm. If you want to be taken seriously then take the time to write an actual document, instead of referring to a transcript of a conversation you had with someone.

## DanielPlante | 2017-08-17T04:57:05+00:00
Understood Javilm. We all have our own personal limits of appropriate format when it comes to ideas. Can't blame you. I've done the same myself.

## javilm | 2017-08-17T06:20:57+00:00
@DanielPlante Thanks. And please note that this is not criticism of your idea. Based on the little I understood it seems to make sense. However, it's difficult to comment and discuss it when presented on Twitter. It will be much easier to talk about it if presented as a single document somewhere.

## DanielPlante | 2017-08-18T18:55:49+00:00
Ok, I'll try to make time in the next couple of days to reformat and repost.

## gerardomoscatelli | 2017-08-22T12:57:33+00:00
Rephrasing my initial bad idea of rewarding full nodes. By not rewarding nodes or not linking full nodes to mining you end up actually giving too much political power to some sensitive nodes running and updating code that the rest will have to follow. You also end up concentrating too much power at mining pools. If the proposal of @hyc is technically feasible, linking hashing to some random data lookup in the blockchain would prevent the current split between hashing and nodes. It would also be a way to avoid the excessive concentration of power at mining pools if the latecy makes it uneconomical (or significantly less profitable) to hash pointing to a pool. I am not a developper so I do this analysis from an economic prospective. There is certainly a lot of downside associated with this.

## gerardomoscatelli | 2017-08-22T13:15:16+00:00
But if we don't think a 51% attack is economically viable (I don't think it is) then this is not even an issue. Agree there are more serious issues to focus on than changing PoW. 

## DanielPlante | 2017-08-25T05:01:20+00:00
In the short to medium term, PoW change actually is the most serious issue. Whether it appears in Bitcoin itself (unlikely due to economic/corporate/social momentum) or a new alt (much more likely), it is still currently the most important change by far.

## DanielPlante | 2017-08-25T07:38:57+00:00
I'm working on a re-write, but the tweet storm I posted is actually a very easy and natural read. Might take me a few more days to translate.

## bigreddmachine | 2017-09-15T16:42:04+00:00
@iamsmooth - I'm very sorry for not replying to you sooner. I was following this issue via email and either I missed your comment or since edits get emailed out, I may have missed your reply to me due to that too. I'll quote the first bit of each paragraph just for reference.

> Your last paragraph reads a lot like a straw man fallacy to me. [...]

In retrospect (which thanks to having not seen this until now I can actually consider) you may be right. I was not trying to create a straw man argument, more just trying to say that regardless the proof of work there is probably a limit to how egalitarian it might be. I do think striving for something that can be done on consumer hardware is a useful philosophy, just a challenging one.

> One other quibble. In addition to the consensus role you described (enumerated list), PoW also serves to distribute coins without becoming a source of concentrated wealth or power that may serve to undermine the legitimacy of the token or the ability of the broader base of users and investors to have any influence. To serve this role requires that mining remain economically competitive and lack significant barriers to entry. [...]

Yes, Proof of Work does create a way to distribute coins. I personally feel this is likely the least interesting part of Proof of Work, though it certainly checks a box in terms of use, and there's not really an obvious alternative that doesn't have major problems. Proof of Work to me (and this is why I have grown to really dislike Proof of Stake) is primarily about driving consensus by making it economically infeasible to re-write the history of the chain, and so the block rewards are as much about incentivizing miners as they are about distribution. But they do certainly play both roles, and also determine inflation, etc.

I'm not sure I agree with your point about being mining necessarily being "economically competitive and lacks significant barriers to entry". I don't subscribe to the idea that Bitcoin mining is broken, which I think is somewhat what is being alluded to here, but welcome any input that would support this argument.

## YellowOnion | 2017-09-29T02:41:46+00:00
I have a bunch of semi-disconnected and somewhat contradictory thoughts I would like to add.

Economics of scale.

Abusing the laws of thermodynamics, 100-200watts of power is fairly easy to handle at a premises, but when you scale up a mining operation you will run into all sorts of problems, including cooling (aircon is a large part of a data centers power usage), access to power, cost of land/rent, maybe trying to make the computation as expensive as possible on power is actually a strength against centralisation, though this favours "seasonal" mining, shifting between the poles, where profits increase in winter, and disadvantaging equatorial regions, I in fact use mining to offset the cost of running my heater in winter.

Cryptonight relies heavily on AES operations, this section of the algorithm favors ASICs and GPUs, the only reason CPUs keep up with GPUs in the first place is that they have dedicated silicon for this algorithm, and currently the fastest hardware for cryptonight mining is a CPU! [The AMD Epyc 7601](https://forums.servethehome.com/index.php?threads/monero-mining-performance.12116/), why? because it's effectively an ASIC with 64MB of SRAM, This brings up the interesting question of "commodity" ASICs, can we abuse specialised features of modern CPUs, so there's no way a "mining ASIC" could compete with the likes of Intel/AMD, every budget phone comes with 8 ARM Cortex A53's these days, and they include AES instructions and an onboard DSP.

Considering access to hardware, in a strange way favouring CPU or memory is actually detrimental, upgrading from a consumer laptop to a server CPU is not straightforward, but cheap consumer motherboards come with 2-4 PCIe slots, and available from many computer stores that supply gamers, and offer a smooth upgrade path by buying one cheap consumer graphics card, than say a $4000 Epyc with 128GB of RAM (I assume blockchain as as scratch-pad could be accelerated with in memory storage), which may not even be available to consumers in your region.

## senselt | 2017-10-08T12:15:12+00:00
I've been around since 2011 and remember well what happened with Artforz. After the GPU code, he went over to fpga then structured ASIC. He completed his structured asic he said "it wasn't profitable" and disappeared from the face of the earth? hmm..

I'm doing myself a disservice by saying this, but there are better solutions for cryptonote than cpu/gpu. I'm currently mining at 4kh/s on FPGA. My FPGA code only uses a small fraction of the logic space but all of the available memory. I'm able to continue using most of the logic to mine some other logic only coin. I'm pulling in $35/day+/board at a cost of $3000/board. 

As much as everyone would like an egalitarian proof of work, it's not possible. You're fighting against human nature and you will lose that battle every time. Everyone is always looking to give themselves an advantage that no one else has. If you make a CPU only coin, people will mass large amounts of CPUs at low / no cost. You have botnets, used / old server hardware (There are some servers you can buy right now on ebay for $500 that would return $125/mo mining XMR). If you make a GPU only coin, people will mass large amounts of GPUs as fast as possible. If you make an ASIC coin, people will take advantage of that to sell overpriced hardware that will never hit black unless the value of the coin rises (which means it would have been better to just buy the coin outright in the first place). When it comes to cpu and gpu only coins, people are always looking for an advantage to try to produce a high level (90-130nm) ASIC to gain an edge. People are looking at FPGA for the same purpose but keeping the general purpose capabilities. If no other advantage can be obtained, people will move over to trying to reduce their costs going to locations with very low power to give themselves an advantage. No matter what you do, someone will find a way, however slight, to gain an advantage (and in the process centralizing the currency). In my opinion, all of this egalitarianism is a futile effort and wasted energy. 

The best thing (IMO) you can do is embrace all of it and accept the fact that you can't change human nature. Then go the multi-pow route like digibyte, myriadcoin, auroracoin, etc. 1-2 ASIC friendly algos (small fast logic), 1-2 GPU friendly algos (large memory usage and bandwidth intensive), 1-2 CPU friendly algos (small memory usage but L3 cache memory intensive (cryptonote)).. And I'm sure some very smart / enterprising individual could figure out how to implement a non-PoW proof along side these other algos. Allowing the ability to do something like PoS at the same time as PoW.  Which would be pretty cool IMO as doing PoS along side of PoW would negate the inherent flaws of PoS. It would also give miners a reason to hold their coins as opposed to dumping them immediately (which the majority of miners do now).


## hyc | 2017-10-08T12:31:54+00:00
@senselt with respect, the existence of FOSS disproves your point. Not *everyone* is looking to give themselves an advantage that no one else has. Some of us are looking to make sure everyone has equal access to the best possible solution. Obviously we can't compensate for environmental advantages, cheap electricity, whatever. Some people will always have natural advantages, true, that's life. Saying "life isn't fair" is an accurate observation, but *we aren't merely observers*. We are changing the world, and I personally prefer to change toward greater fairness.

## senselt | 2017-10-08T13:22:28+00:00
@hyc I would say FOSS proves my point, not disproves it. Companies externalize operations that don't give them an advantage to reduce costs, which gives them an advantage. If AT&T developed and produced openstack internally it wouldn't give them as much of an advantage as it would to distribute those costs across others who need a similar platform. Others use FOSS as a way to build a name (increasing reputation), which allows them to find clients, sponsors, etc. Just because something is free / open, it doesn't negate the possibility (or likelihood) that it gives someone, somewhere an advantage. 

## fluffypony | 2017-10-08T13:29:19+00:00
@senselt of course we’re aware that any system designed will have people able to eek a little more performance than the rest. The point is not wether someone can $2/hour more profitable than the next guy, but whether they are so massively more profitable that they cloud everyone else out.

As an example, we know that botnets can mine Monero at effectively zero cost. However, the ease of access to equipment that GPU miners have, coupled with the usual murky nature of running botnets, means that botnets have never made up more than 10-15% of the network. Thus the network is broadly secured despite the fact that all professional Monero miners should be using botnets if they really wanted to be cost-effective.

## hyc | 2017-10-08T13:42:23+00:00
@senselt you have a very limited view of open source. Everything I write is open source. Only a tiny fraction of it has any bearing on my reputation or income. I'll stop here before digressing further.

## DanielPlante | 2017-10-26T05:44:47+00:00
Riccardo is correct. The maximum GPU advantage over CPUs is approximately 5 orders of magnitude. ASICs is about 12. DRAM is about 2. It would behoove us to grasp the metrics and do that math.

## DanielPlante | 2017-10-27T07:35:36+00:00
And how do you respond to a specific post on GitHub? This UI is atrocious.

## QuickBASIC | 2017-10-27T09:43:16+00:00
> And how do you respond to a specific post on GitHub? This UI is atrocious.

@DanielPlante It can be helpful to use Markup to quote specific people and @ to mention them, but there's no threaded conversations.

## DanielPlante | 2017-10-30T07:14:57+00:00
Sorry, I don't know what "markup" means in this context. And does the "@" mean the same here as it does on twitter? Seriously folks, when did format dethrone content? It is, and has always been,  just semantics trying to convey semantics. Embrace plain communication. That said, I will still try to find the time to reformat the tweet storm into the approved format. But you are free to surprise me by engaging with questions based on the original post.

## qertoip | 2017-11-16T16:40:08+00:00
What would be the next step here?

I just want to keep the topic alive :)

Plus, I can chip in a little bit if there is some serious initiative to be funded.

## JollyMort | 2017-11-16T17:44:33+00:00
IMO there is no next step since first step was skipped: proving there is a problem to begin with :) Sure, someone can look into solutions ahead of time, but what problem is being solved again? I thought solution comes after the problem, and not the other way around.

## DanielPlante | 2017-11-21T10:13:51+00:00
Sorry, I meant "syntax dethroning semantics". That said, JollyMort has a point: do we all perceive that there is a problem here in the first place? If you disagree, then why are you spending the effort to argue? Stick to the point you presumably want to address. I'm available to answer questions. Thank you all for your input.

## qertoip | 2017-11-23T10:53:45+00:00
The two biggest practical problems I see with CryptoNight:
* very DoS prone due to super slow verification; CryptoNight does not really fit a PoW definition even though it was "designed" as a PoW
* unknown properties due to virtually no formal research; can "explode" one day in unexpected ways

CryptoNight represents a lame approach to cryptosystems design.

## fresheneesz | 2017-11-29T09:54:59+00:00
@banastas2 

> Can someone clearly define "mining centralization" -> Is it too much hash rate by geography or pool or ownership? Is it possible to design and algo that understands geography?

Geography doesn't really matter. Ownership is what matters. I created a definition of "centralization pressure" in my post here: https://np.reddit.com/r/Bitcoin/comments/74t4ua/an_explanation_of_why_the_block_size_debate_is/

Basically, centralization pressure is all about profit margins. The lower the profit margins, the higher the centralization pressure. Along with @CameronRuggles, I also worry that competitive pressure will inevitably centralize any static proof of work system. 

I liked Cameron's suggestion of having many algorithms that work alongside each other. This would prevent the system from being static, and would allow for an equilibrium state with at least 1 owner / strategy. If each algorithm had a completely separate difficulty, it would mean various types of miners could pop up and compete separately from other types of miners.

Another thing that would keep the system from becoming static and tending toward centralization is to have the algorithm change over time. If there was some way to slowly mutate the algorithm to force miner strategies to change in unpredictable ways, it would ensure competition required innovation, which inevitably requires changes of the guard. 

Finally, I disagree with @fluffypony that the window for a PoW change is closing. I don't think we need to treat this with any major urgency. We don't want to rush into a minor PoW change. We should really think this through and make a breakthrough around this - something we can be far more confident will stand the test of time. As for the window closing, like someone else suggested, we can have multiple PoW algorithms active at the same time and slowly phase out the old one. This means there doesn't have to be any disruption to the network, no matter how big it is.

## dave-andersen | 2017-12-09T02:21:42+00:00
Hi, @fluffypony  - just a quick drive-by:  Cryptonight is a quite solid algorithm from an ASIC perspective.  It's designed very well to take advantage of three features that conventional CPUs have:  (1)  Built-in AES acceleration;  (2)  fast 64-bit multipliers;  and (3) large caches.  If you look at the architecture diagram:  http://www.cs.cmu.edu/~dga/crypto/xmr/cryptonight.png   and trace the critical path, you'll spot each of these features being used, and to quite good effect.  I haven't attempted a really deep cryptanalysis of everything in the PoW, but as you know, I, er, worked rather hard to find any vulnerability I could in it, and didn't see anything I could exploit.  I don't *think* there are subtle, hidden evilnesses in there -- whomever designed it had a good grasp of both modern CPU architecture and the design of mixing functions.

The path to a cryptonight ASIC is fairly obvious:  A small-ish chip with 2MB of SRAM for the scratchpad, an AES implementation, and a 64 bit multiplier.  Maybe more AES for doing the initial scratchpad fill.  Interestingly, this looks quite a bit like the CPU implementation, but an ASIC designer would have a few advantages:  (1)  Less area wasted on "other" functions that CPUs support;  (2)  Fixed function - no instruction decode overhead;  (3)  Better locality from the fixed-functions to the scratchpad (a large CPU has ~20MB of cache for 10 cores, so each core is a bit farther from L3 cache);  and (4) Yield.  By yield, I mean that the ASIC for this would be smaller than a modern CPU, and it's usually easier to produce smaller chips than absolutely massive ones like an Intel or Nvidia beast.  You can fit them more effectively on the silicon wafer, and errors aren't as deadly.

But even with those advantages, they're still going to take a lot of area, and area is the major determinant of cost -- a modern CPU devotes much of its die area to cache, for example.

The other alternative is more AES/multipliers together with HBM -- high-bandwidth memory.  This would look a lot like what Nvidia offers in the Volta.  I suggested this as a path for running Cryptonight about three years ago:  https://bitcointalk.org/index.php?topic=717267.msg8129454#msg8129454

but I think I was overly-optimistic about the progress people have made in getting HBM working.  Nvidia took about two years more than planned to get it released, and the implementation isn't as technically nifty as some of the earlier plans had it looking.  There will still be progress in this front.  There's also the potential of trying a compute-in-memory architecture for Monero, but the AES and 64-bit multiply do make that a bit harder.  And we're seeing GPUs with HBM right now, which should provide a pretty good boost to hashing speed - and steal a bit of the thunder from a potential HBM ASIC.

I would never say that ASICs won't get a factor of ten or so on Cryptonight, but I believe the algorithm will continue to fare very well for a while to come.

The price you'll pay for it, of course, is expensive verification, as you and others note already in this thread.

Cuckoo Cycle and Equihash both have worse CPU/GPU ratios but offer faster verification, and now that xenoncat chipped in with a set of optimizations to Cuckoo Cycle, I'm feeling less paranoid about unanticipated speedups in that area -- though I retain some caution.  Maybe in another year I'll believe it's not going to surprise us much more. :)

@qertoip  - you wrote "CryptoNight represents a lame approach to cryptosystems design." -- I actually suspect that the designer of CryptoNight was an expert, though operating in the shadows.  I've examined a lot of proof-of-work functions, and CryptoNight is one of the few memory-bound ones that I haven't been able to find algorithmic improvements against (as opposed to implementation hacks).  That's no guarantee there aren't gotchas, but it holds up well.

If you want a second opinion - which is always a good idea - y'all might see if Solar Designer would consider providing an analysis, similar to what he did for Equihash.  I've read his analysis of that one and it's solid.

## fresheneesz | 2017-12-09T19:37:40+00:00
> expensive verification

Why is expensive verification a problem? Is it because the expense is constant no matter how large of a miner you are?

## dave-andersen | 2017-12-09T21:56:56+00:00
Verification cost has a few problems:  (1)  Time to synchronize a new node if you don't want to trust a snapshot (takes a lot of CPU to verify the blocks);  (2)  DoS resilience, if someone tries to mount an attack involving large floods of fake (invalid) blocks.  For pools, for example, this opens an avenue for mounting a denial-of-CPU attack by submitting invalid shares.  Pools and nodes have mechanisms to handle that, but the "perfect" PoW function (which may not exist...) would have nearly instant verification.

## iamsmooth | 2017-12-09T23:38:05+00:00
(1) is a theoretical issue but in practice not much of one. First it is only an issue at all for SPV-type nodes, since the cost of verifying the actual transactions is a lot higher than the PoW. Even for SPV (1) is not a huge factor; on a shitty desktop it still only takes about 3 seconds to verify one day worth of PoW (so 20 seconds if catching up after a week offline). Mobile raises battery consumption issues but still not a huge issue unless doing a fresh sync from 0 (which can be done plugged in and/or shortcut with checkpoints).

Agree of course about 'perfect PoW' in all respects (would be great, may not exist).

Most of these concerns were thrown around when cryptonight first came on the scene with (artificially impaired) 1-2 H/s performance, and at that point they were serious issues indeed (many minutes to verify one day of chain, etc.). Once the function was properly optimized the issues are far less signfiicant in practice.

## induane | 2017-12-18T22:16:51+00:00
There is another option I never see given which is to avoid the contribution to payout link.

In other words:

1. Given the overall hashrate of the network for a particular block specify a minimal hashrate  for which a miner would be rewarded.
2. All miners who met the threshold value split the reward evenly
3. Require a fee for a new miner to enter the network rather than allowing anyone to enter the network - i.e. spend X amount to create a new valid mining address. 

Centralization is probably still possible using a method like this but would happen at a greatly reduced rate. It could likely be fiddled with (it's oversimplified in 3 bullet points) to find a sweet spot in terms of rate of centralization vs usability. I'm not sure centralization given the current concepts around mining is fully possible to avoid but it can be mitigated significantly and that's the point. It's theoretically possible to brute force wallet generation to find the private key for every bitcoin address for instance - except that also in theory it would take longer to solve than the age of the universe. One may not be able to fully prevent centralization but one might feasibly slow the rate at which it occurs by being clever and making the time it would take so long as to not matter.

## fresheneesz | 2017-12-19T00:01:18+00:00
@induane Mining is the process by which its determined who gets to choose the transaction ordering for the next block. As long as miners mine a valid block, they can put anything in it they want to. If you want to reward all the miners that exceed a threshold, you still need one canonical block. That canonical block would have to contain a record of which other blocks reached the "hashrate threshold" and the addresses to send the mining reward to. Why would any miner voluntarily decide to give other miners a cut of their block reward by including them in their block? A block would have to be rejected by network rules in order to enforce this, but the question then becomes: "how do you determine canonically which threshold-reaching blocks the canonical next block should contain?" 

It seems like the idea is impossible to implement. You'll either have a nothing-at-stake problem like with PoS, or you simply have a system that gives miners no incentive to do anything differently than they're currently doing it. The only way to smooth out the time-variance of successfully mining a block is by reducing the block time. 

## senselt | 2018-04-07T15:19:18+00:00
@fluffypony how are you feeling about changing monero PoW now? Apparently they were mining monero with asics when we were having this conversation. I still think multi-pow is the step in the right direction. Otherwise, next time, bitmain may just keep mining secretly. DGB had / has far fewer problems in changing their PoW than monero. When the change occurred, monero was at risk for being targeted by large GPU pools, where as, DGB will not be at risk (or at least no where near the same level of risk). 

## DanielPlante | 2018-06-03T07:57:55+00:00
And so this thread, and the promise of it, died not with a bang but a whimper.

Thank you al for your time.

Maybe there are other more productive avenues.

## fluffypony | 2018-06-03T08:30:30+00:00
@danielplante I don’t think the discussion is over, it’s just that these things move slowly in FOSS. In my mind the only three possible options are:

1. SHA3, but only when SHA3 ASICs are commoditised (like to the point where everyone has one, like USB flash drives)

2. Cuckoo Cycle, but I’d want to be cautious and wait for Grin to be the proving ground for that

3. Some as-yet undiscovered algorithm

None of these are going to be pushed into production any time soon, as they all have time constraints.

## LordMajestros | 2018-06-03T10:49:24+00:00
@fluffypony Cuckoo Cycle is not ASIC resistant.
See here https://www.grin-forum.org/t/being-asic-resistant-or-not/372/3

## hyc | 2018-06-03T11:55:34+00:00
@DanielPlante the discussion didn't die, it just evolved from the realm of research into actual development. https://github.com/monero-project/monero/issues/3545

We have (at least) two viable PoCs now.

## DanielPlante | 2018-06-04T03:43:16+00:00
Sorry folks, I still can't see how to reply to a specific post with this UI, so this is directed at the last 3 responses:

My underlying point was that the thinking on this issue seems to have become almost intractably moribund. I have seen no recognition that computational proof of work is simply one facet of a more general concept: shareable digital proof of the control and use/expentiture of a real world asset.

If we step back and take in this wider view, we should see that there are other hard proof avenues besides simple computational power (and the implied energy burn - that's a real world resource and important too) that can anchor the virtual world to the physical, which is another way of describing the kind of proof regime we need.

Seen in this light, what other approaches can we take advantage of? Well there is the DRAM based approach I mentioned, and that is a hard proof. 2nd-level storage such as hard disks/SSD's are an available avenue as well but the throughput time makes it impractical. I've tried to imagine a scheme that can link digital proof to gold and other non-computational assets but I think that's not possible.

Maybe I should change gears myself on this issue, and pursue this issue in a different manner:

Read my initial post. The original Nakamoto consensus proof approach was gamed by a trillion times - 12 orders of magnitude. You will not be able to economically game the approach I described by more than 1 order of magnitude.

I will take the time to explain in detail why you are wrong, and hopefully a consensus about the technical nexus between the virtual world and the real world will emerge as a bonus.



## DanielPlante | 2018-06-04T04:28:40+00:00
This might provide a bit more clarity:

https://twitter.com/Daniel_Plante/status/1003419231352811520

## fresheneesz | 2018-06-04T06:26:16+00:00
So i know you guys probably wouldn't want to use monero as a proving ground for this either, but i developed a PoS protocol that I've calculated to be several orders of magnitude more secure (ie higher cost to attack) than PoW.

But basically it uses 1 minter and many validators for each block to maximize the amount of stake needed for an attack. It also fines minters for minting too far on the wrong chain, which solves the nothing at stake problem while also solving PoW's latency-related centralization problem. This fine also doesn't require any coins to be locked, which minimizes the barriers to participate in the minting process - further increasing the security. 

It's in need of review: https://github.com/fresheneesz/ValidatedProofOfStake

## hyc | 2018-06-04T06:48:22+00:00
@DanielPlante DRAM-based approach is a fool's errand. Moore's Law still works as originally stated - number of transistors doubles every 18 months. DRAM density and capacity correspondingly doubles, so what constitutes a "hard limit" on DRAM is a continuously moving target. In contrast, CPU performance has plateaued, so computational hardness doesn't change much at all over time.

> I will take the time to explain in detail why you are wrong,

Fix your own assumptions first.

## DanielPlante | 2018-06-04T07:22:11+00:00
@hyc nope.

Read my thread. Tell me how you would game it by more than 1 order of magnitude. I described how the current paradigm failed. Give me capital cost and watt hours per found block. Be specific.

## DanielPlante | 2018-06-05T07:09:16+00:00
Read my tweet thread. Attempt to explain to me why that approach isn't better than simple hashing.

I will take the time and effort to explain where you went wrong, but to be frank you should have realized that for yourself if you honestly took the time and effort to understand what I was saying.

I'm available. Up to you.

# Action History
- Created by: shaolinfry | 2017-08-07T02:29:18+00:00
