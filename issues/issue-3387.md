---
title: Proposal to consider an ASIC-friendly proof of work
source_url: https://github.com/monero-project/monero/issues/3387
author: iamsmooth
assignees: []
labels: []
created_at: '2018-03-12T09:34:03+00:00'
updated_at: '2022-07-21T15:39:09+00:00'
type: issue
status: closed
closed_at: '2022-07-20T20:19:15+00:00'
---

# Original Description
Currently Monero is pending a hard fork to modify the PoW in order to invalidate existing rumored and reported ASIC designs, and in addition to continue making such changes repeatedly to attempt to prevent ASIC development and deployment on the network. For various reasons, there are longer-term concerns with this strategy, particularly going forward, including:

1. Continued and repeated ad-hoc modifications to the PoW algorithm may accidentally (or even maliciously) introduce exploits.
2. ASIC developers may build in more flexibility to their designs to be able to accommodate small algorithm tweaks (indeed this may already be the case, we don't know).
3. Potential for favoritism/corruption if plans for tweaks are leaked or influenced far enough ahead of time that some favored ASIC developers may have enough lead time to produce ASICs, while others do not.
4. A belief that ASICs may be desirable as a means to facilitate industrial scale mining and growing the network beyond what might be called a hobby mining phase.
5. Potential for _increased_ monopolization if the strategy is only partially effective (i.e. keeps all _but one_ ASIC developer from succeeding)
6. Dependence of the network on continued frequent hard forking independent of the need for functional upgrades. This carries with it a greater degree of centralization necessary to design, implement and coordinate these forks, without any real plan to transition beyond it.

For these reasons I would propose that we _consider_ (which does not necessarily mean _implement_) abandoning the ASIC-hostile approach and instead consider adopting an _ASIC-friendly_ approach in a future hard fork.

By ASIC-friendly, I mean something that not only can reasonably be implemented in an ASIC, but which minimizes barriers to creating ASICs, minimizes their costs, facilitates the development of a wide range of compatible hardware at attractive price points, and minimizes opportunities for clever proprietary advantages. By doing so we may maximize the likelihood of a competitive ASIC market developing and minimize the degree of (temporarily or sustained) monopolization. This could possibly be achieved by using a simple, well-known, and well understood algorithm such as SHA3.

There are numerous other potential advantages and disadvantages of this approach relative to Monero's current PoW algorithm and strategy, which can be discussed in comments.

Postscript: My personal view has always been largely ASIC-hostile (primarily based on my analysis the history of the Bitcoin ASIC market when Monero launched in 2014, but reinforced by the continued evolution of the Bitcoin and other coin ASIC markets over the past four years), however I am open to the possibility that unintended consequences of attempting to maintain this approach may cause more harm than overall benefits, in which case it should be dropped.

# Discussion History
## williams-r | 2018-03-12T11:49:06+00:00
Points for ASIC-friendliness:

ASIC manufacturing will see more competition, halong mining is already competing with bitmain, and their defensive patent group is promising.

There are no ASIC botnets.

ASICs are worthless the day after they carry out a 51% attack.

Merged mining with bitcoin would means that monero does not have to compete in the same way for the same electricity and capital investment in mining equipment.



Points for ASIC-resistance:

CPUs and GPUs are more difficult to ban than ASICs

the silicon foundries which produce ASICs are quite centralized

Merged mining with bitcoin right now would increase centralization pressure on bitcoin mining from the increased cost of node operation.

## SRCoughlin | 2018-03-12T17:47:12+00:00
I propose a process that can satisfy many of these concerns: using a sound game theoretic strategy for ASIC resistance. In my proposal, this would continue the current 6-month release strategy, but would also include the following:

1. The addition of a large number (N) of known non-ASIC-implemented POW algorithms, equal probability of implementation assigned to each (1/N).

2. Antagonistic testing of each algorithm to confirm its success and lack of exploitable weakness, and replacement of failed tested algorithms.

3. Rational cost analysis of implementation of each combination of above algorithms in ASIC/MPW fabrication. (Perhaps also including POC in FPGA to get realistic data.)

4. Use of a pure RNG to determine the particular algorithm implemented in the release.

This process would allow for openness in discussion of future direction and would allow for greater trust by the community in the stability of upcoming releases. (i.e. No more "last-minute" POW changes.) And its use of the random strategy will negate any serious investment in ASIC development as means of dominance.

This process would not address botnets, partially effective ASIC exploits (discovered post-release), or the need for "industrial scale mining".

Please let me know if you think this might be viable.

## jwinterm | 2018-03-13T05:09:27+00:00
If you would like something that "...not only can reasonably be implemented in an ASIC, but which minimizes barriers to creating ASICs, minimizes their costs, facilitates the development of a wide range of compatible hardware at attractive price points, and minimizes opportunities for clever proprietary advantages." then why do you immediately disregard SHA256 and propose SHA3?

## iamsmooth | 2018-03-13T05:29:43+00:00
@jwinterm I'm not an expert on this but I've seen various credible claims that SHA256 is not a particularly ASIC-friendly algorithm by design, due to both its internal complexity and susceptibility to various clever optimizations. This has allegedly contributed to the rather less than competitive Bitcoin ASIC market, since barriers to designing competitive SHA256 mining ASICs are higher than they otherwise need to be, and there are too many opportunities to gain an sustainable advantage with proprietary tricks. But who knows, this may be a bogus claim.

SHA3 may or may not be better, but in any case that was only intended as an example which is somewhat more modern by design than SHA256, avoiding some of its pitfalls (for example, length extension attacks, though that in particular may not matter much to PoW). 

There may well be better choices, but the particular choice of algorithm that seems somewhat of a diversion from the core question of whether ASIC-friendliness is useful goal and then defining the selection criteria.







## iamsmooth | 2018-03-13T05:31:12+00:00
@SRCoughlin While your idea is good in theory, I'm not sure about its feasibility in practice. It is hard enough (and may fail) to produce even one well-vetted and carefully-implemented alternative/modification without screwing it up (see #1 in the original issue), much less several.

## jwinterm | 2018-03-13T05:52:05+00:00
> There may well be better choices, but that seems somewhat of a diversion from the core question.

This is true, and I think ultimately it's futile to try and constantly fork away from ASICs. The original idea of cryptonight afaik was that it was somewhat equivalent between CPUs, GPUs, and theoretical ASICs, and I think trying to meet that original vision is probably more realistic than trying to constantly fork to prevent ASICs from mining on the network.

## iamsmooth | 2018-03-13T06:47:39+00:00
@jwinterm 
> The original idea of cryptonight afaik was that it was somewhat equivalent between CPUs, GPUs, and theoretical ASICs, and I think trying to meet that original vision is probably more realistic than trying to constantly fork to prevent ASICs from mining on the network.

That's somewhat getting at the core of the intended topic of this issue: Is that still considered a useful goal, and if so, is it feasible in practice?

If it is useful and feasible, how should it be done?

## otheATgh | 2018-03-13T07:34:15+00:00
> the silicon foundries which produce ASICs are quite centralized


That's non sense and a non issue, those foundries are the EXACT SAME that fab out the chips for NVIDIA and AMD. NVIDIA and AMD don't seem to be able to scale their productions due to the same issues BTC ASIC factories have atm. 


This discussion should have been had in detail way before merging in this untested and unreviewed PoW change.


Using SHA3 or our bastard child of keccak we currently use for the PoW has the advantage that we do not need to implement another unrpoven crypto library besides what we already have.
On the other hand SKEIN seems to be a more sane and even easier to implement in HW as it was meant to be implemented in HW.
Another alternative could be to use a slightly modified double sha256 like Bitcoin as the ASIC chipdesign there is already highly optimized.

I dont think merge mining with BTC makes any sense as i do not think that the same HW should be used for both coins, it gives BTC maximilaists easy access to attack our network. 


The whole securing multiple billion dollar networks using a bunch of hobbyiest miners that can easily overtaken renting some AWS instance is a pipedream to me.

So far it seems mostly mined by botnets and shitty JS webminers that steal other peoples resources and can dump them at whatever price because they were essentially free anyway.

## cAP5L0CK | 2018-03-13T14:10:49+00:00
First of all I strongly favor this conversation.  

One of the  notable outcomes of ASIC resistance besides botnets have been browser miners.  One side effect of dropping the ASIC resistant stance would be to greatly diminish if not eliminate the use web miners both being used nefariously but also in the open like Salon.com etc.

## SRCoughlin | 2018-03-13T14:17:19+00:00
The community has opposed the use of ASIC miners due to the nature of centralization that this entails. If ASIC supporters should wish their implementation, it stands to reason that this case be addressed. (Counterexamples of botnets, Salon, etc. are likely not going to convince the community.)

## Hueristic | 2018-03-13T14:31:58+00:00
No matter what, we should fork away from these current ASIC's, rewarding them is not a good idea.

## metamirror | 2018-03-13T15:29:21+00:00
Perhaps the Monero Project should fund the development of its own open source ASIC design. It could also manufacture ASICs and commit to selling all of its chips retail.

## SRCoughlin | 2018-03-13T16:57:14+00:00
@metamirror Interesting. Consider: the community creates a number of new POW algorithms and, in tandem with development and testing, openly releases the VLSI designs for FPGA/ASIC (even MPW?) to go along with each (every?) algorithm. After the RNG, miners can either coordinate bulk purchases through the community, or use the VLSI to fab an independent run of chips and create a custom ASIC. The beauty is that in 6 months the next network release (hard fork) would choose another algorithm by RNG, negating the processing advantage of the existing ASICs and requiring new VLSI designs.

This would allow for full ASIC implementation to anyone's content, yet this would also be limited (by the random strategy) to be economically viable for only a small number of miners. Hence, it would be predictable and controllable, and, should any of the above criticism prove valid, could provide reason to delay the given POW algorithm change schedule to avoid issues.

This would be, in essence, a completely open source anti-ASIC strategy and unlike anything attempted before.

## iamsmooth | 2018-03-13T19:14:37+00:00
@otheATgh Numerically I think renting a bunch of AWS instances is really not a viable attack. In terms of naive cost estimate, perhaps it is feasible, but while AWS may have a million or more high end CPUs or GPUs to use for this (or an even equivalent even-larger number of small ones), actually renting that many at one time is not trivial at all, and may be totally infeasible. It means you are competing with their other customers, some of whom are not particularly cost sensitive in the short term (the don't want their enterprise computing shut down so you can attack a network for an hour).

Setting aside Amazon KYC-ish requirements on large capacity demand  (they want to see justification and also that you will not disrupt their service), let's look at some numbers. A high end AWS node generates something like $10000/year revenue if rented long term and $4-5k/year if rented on the spot market. AWS total revenue is something like $20 billion/year not all of which comes from instance fees (some from storage, bandwidth, value-add services, etc.). If it were all high-end node instance fees which of course it isn't, the entire company would only be 2 million nodes, and you would need need to pull something like half of it to pull off an attack which you won't be able to do.

This seems implausible. Even combining other providers it seems far from easy.

You are significantly underestimating the strength of the current 'hobbyist miner' network (though it isn't really that, there are definitely some large scale miners) and the difficulty of renting very large amounts of resources from cloud providers (particularly for short time which they _will_ find disruptive and not allow) in practice. 

Nevertheless, given potential price drops, emissions reduction over time, this may become an issue. Also, Ethereum GPU farms have far more than enough capacity, if they decided to be become Ethereum-maximalists doing the attacking instead of the Bitcoin maximalists you mentioned (or just underutilized after Ethereum PoS).


## iamsmooth | 2018-03-13T19:21:31+00:00
@metamirror 

> Perhaps the Monero Project should fund the development of its own open source ASIC design. It could also manufacture ASICs and commit to selling all of its chips retail

I don't think the Monero project wants to be a point of centralization on the design and manufacture even if they are being sold. The issue isn't only who is building the miners, it is that someone is doing so and has a lot of control over the market (who gets miners, how many, when, and at what price). 

Possibly an open source design could make sense, but I don't know enough about the realities of the ASIC design and manufacturing marketplace to know whether this is useful. More generally (not referring to miners here), I see a lot of people talking about 'open source hardware' and not that many actually doing it, particularly at the ASIC level.


## SRCoughlin | 2018-03-13T19:33:23+00:00
@iamsmooth

> More generally (not referring to miners here), I see a lot of people talking about 'open source hardware' and not that many actually doing it, particularly at the ASIC level.

While software experience is highly portable and abstract, hardware requires EE skills, which are much more time-consuming and particular. Very few EEs donate their time to open projects.

> Possibly an open source design could make sense, but I don't know enough about the realities of the ASIC design and manufacturing marketplace to know whether this is useful.

I do, but donating time for EE work would only make sense as a means to an end. In other words, there has to be very specific reason why EE work is being done. The abstract ideal of decentralization may not be enough to justify this.

As an example of the EE work costs, I give you the (very high) fees associated with the optimal GPGPU code for Cryptonight POW algorithms.

In fact, I'm wondering now if including a (much lower) fee in the POW algorithm and VLSI code would allow for FFS bounties for their own development. This could be interesting, but might also create a conflict-of-interest with the EEs working on these very designs.

## iamsmooth | 2018-03-13T19:43:00+00:00
(sorry closed by accident)

@SRCoughlin "Very few EEs donate their time to open projects" 

Donating time and open source are two different things. A very significant portion of Monero development has been paid for. 

> The abstract ideal of decentralization may not be enough to justify this.

The entire purpose of a decentralized cryptocurrency project (indeed the entire purpose of cryptocurrencies at all) is decentralization. It isn't just an abstract ideal, it is at the very core of the mission statement.

My view is that ASICs only make sense if there is an expectation of a commoditized market developing in a reasonable period of time. That hasn't happened with Bitcoin at all, but maybe it still will.

Unless we have some alternative approach which does get there (and at a much smaller scale than Bitcoin _might_ get there), then I would consider the answer to this issue to be in the negative.


## hyc | 2018-03-13T19:47:19+00:00
@jwinterm 
> This is true, and I think ultimately it's futile to try and constantly fork away from ASICs. The original idea of cryptonight afaik was that it was somewhat equivalent between CPUs, GPUs, and theoretical ASICs, and I think trying to meet that original vision is probably more realistic than trying to constantly fork to prevent ASICs from mining on the network.

This makes the most sense to me. While the crypto community always admonishes "don't roll your own crypto" I think it's important to highlight that goals of a PoW hash function don't align with the goals of a typical cryptographic hash function. Most hash functions are designed for efficiency of implementation and execution. (Password hashes may be a notable exception to this goal.) We want something that is equally difficult for CPUs, GPUs, and ASICs. AFAICS this means we want something that is branch-heavy, where multiple branches are all equi-probable. That would defeat CPUs' branch predictors, and GPUs are already poor at branchy code. We also want something that is comprised entirely of serial data dependencies, to defeat any CPU instruction-level parallelism. And we want something that cannot be simply reduced to a compact set of lookup tables. I don't think it'd be hard to come up with such a design.

## iamsmooth | 2018-03-13T20:09:31+00:00
@hyc The cryptographic soundness (at least some aspects of it) is extremely important otherwise the algorithm can be analyzed and shortcuts found which avoid the need to execute some or all of the (branch-heavy, etc.) code you initially assume is necessary to search the space of possible solutions.

That said, something that is _both_ cryptographically sound and better tuned to the needs of PoW (in particular, ignoring efficiency of execution, good point there) is probably possible, but I'm not sure "not difficult". In a sense all previous attempts at ASIC-resistant, GPU-resistant, memory-hard, etc. PoW have been that, and most if not all have failed in some aspect or another. Cryptonight has held up better than most, in terms of maintaining a balance.

Also, I'd guess that intentionally defeating things like instruction-level parallelism in CPUs puts them at a big disadvantage to ASICs and possibly GPUs since those will employe parallelism in hardware (unless there is some method proposed to limit or prevent it, such as a very large non-optimizable scratchpad). To maintain parity, CPUs probably need to take advantage of their accessible parallelism too.


## iamsmooth | 2018-03-13T20:18:51+00:00
Linking because it is worth reading. I don't necessarily endorse every aspect of it, but I endorse (strongly) at least being familiar with the document :)

https://download.wpsoftware.net/bitcoin/asic-faq.pdf

## ghost | 2018-03-13T22:37:57+00:00
Has there ever been a hybrid PoW scheme that combines an ASIC-unfriendly function with an ASIC-friendly one? 

I am thinking of a scheme whereby the first stage of the computation uses an ASIC resistant algorithm, with its output being passed as input to the second stage, which uses an ASIC friendly algorithm. Miners could earn block rewards for performing either (or both) stages. 

Consider a bad scenario: a botnet controls a disproportionate amount of the hashrate and/or ASIC farmers do the same. The botnet could never compete with the ASICs on the second stage, but the ASICs would have difficulty competing with botnet on the first stage. Some separation of hashing power would exist, similar to a bicameral legislature. 

All Google showed me was hybrid PoW/PoS schemes, so I haven't been able to find anything similar to the one I just described. If someone knows of one, please let me know. 

## TheTrueForce | 2018-03-14T01:41:23+00:00
Please pardon me lobbing up out of nowhere and leaving this here.
@jsfierro That seems like a good idea, but:
I can see dedicated miners being made to fit that as well. I have no idea if this is actually the case, but it might be feasible to build a custom computer combining a high-end CPU and/or GPU, combined with an ASIC module, and run by custom software. That might defeat the purpose of the two-part algorithm, as the general-purpose(GP) hardware would do its part of the hashing, and then shove that into the ASICs, and pick up the result. Those could be beastly.
I can also see addon boards being made for regular PCs to accelerate mining, much like a GPU accelerates rendering. This could lead to the same situation as the hybrid miner, though.

Please keep in mind that I'm speaking from ignorance(or at best only small knowledge), so I could be barking up the wrong tree entirely. Or possibly just barking.

What if the two-part algo has some kind of requirement that the same hardware can't do both parts?
That each unit of work needs to be performed by two seperate and different pieces of hardware? That would likely elimenate solo mining, and it would also almost require the existence of ASICs. Probably neither are good things. And probably the ASICs would be substantially faster than the GP hardware. That might be an obstacle. On top of that, enforcing the requirement could be a nightmare... I actually have no idea at all how that could be done, if it even can...

## hyc | 2018-03-14T01:49:40+00:00
Having worked on compilers, optimizers, auto-vectorizers, and the lot, I'd say it's harder to write optimization-friendly code. But it's a heavily studied field by now; we can look at any guide to optimizing code for parallelism, and do the opposite. And what we use can of course start with a cryptographic hash (like Keccak/SHA3) on the front, to decorrelate the intermediate data from the input. After that it's just an issue of making sure nothing we do cancels itself out.

## Gingeropolous | 2018-03-14T12:28:51+00:00
For me, the problem with an ASIC friendly PoW is that you can never beat the economies of scale that ASICs provide. So even when ASICs become commodified, and every phone has an ASIC because reasons, and lightbulbs and toasters because you have to hash for service, we may have achieved an egalitarian access to the hardware, but we may not have achieved egalitarian access to the nonce space. 

When I first encountered Bitcoin, it was post-ASIC. I read about it, saw the mines, and concluded that Bitcoin had already become, and would continue becoming, just another space where the Rich get Richer and the everyperson is forced out. And because ASICs breed centralization, it seemed to me that Bitcoin had failed in its primary purpose - being decentralized. 

At first, I didn't get into Monero because of "the privacy". I got into it because the egalitarian PoW aligned with how I understand decentralization. 

Finally, I think ASICs give too much power to the miners. Yes, I've read the logic that "well the ASIC can only be used to mine that coin so therefore the miners will always support that coin and their intentions are good" but we shouldn't care what the miners support. The miners get rewarded for providing a service to a decentralized network, where the value is completely dependent on the extent of decentralization. 

The network is not rewarded by the service of the miners. 

## SRCoughlin | 2018-03-14T19:55:23+00:00
@iamsmooth

> Linking because it is worth reading. I don't necessarily endorse every aspect of it, but I endorse (strongly) at least being familiar with the document :)

I've completed reviewing this document. It is either incorrect or inapplicable in every claim. While it may have some important information about efficiency when it comes to SHA256 algorithms such as Bitcoin, there is nothing to be learned from it when it comes to Monero and its POW algorithms.

My critiques are as follows:

> all ASIC resistance does is increase the startup capital required and therefore increase centralization of manufacturing

Incorrect. ASIC resistance costs labor primarily (designing VLSI, etc.), as ad-hoc production runs of chip fabrication are common now. Capital outlay for the run is not a concern.

> it is impossible to create an algorithm which runs at the same speed on general-purpose and dedicated hardware

Inapplicable. It is possible to create algorithms which surpass the economic feasibility of ASIC design within the timeframe of change in POW. If it's not profitable, there is no incentive.

> Schemes such as “the developers will just change the proof-of-work algorithm if ASIC’s
appear” do not even make sense — in a decentralized currency the developers have no such
power

Incorrect. This is happening right now.

> Memory hardness has the effect of increasing ASIC board footprint, weakening the heat-
dissipation decentralization provided by the thermodynamic limit.

Inapplicable. As above.

> Also, memory hard proofs-of-work often require lots of memory on the part of the verifiers, which is bad for decentralization

Partially applicable, but only as for certain implementations. Say, Arduino or other small devices.

> memory-hardness worsens the centralizing effects of ASIC’s while weakening the decentralizing effects

Inapplicable. As above.

> An algorithm which is highly susceptible to TMTO has poorly defined memory hardness

Incorrect. Testing and optimization can reveal these issues. See Cuckoo Cycle as an example.

## iamsmooth | 2018-03-14T21:16:19+00:00
@SRCoughlin Cost of labor to design is a capital outlay. Someone is paying for the labor long before revenue. That investment is a form of capital.

Yes the document takes the position that _effective_ ASIC resistance is impossible. That may or may not be correct in practice, but the idea that _ineffective_ ASIC-resistance may make matters worse seems valid to me.

@Gingeropolous "but we may not have achieved egalitarian access to the nonce space" 

I don't see how this is ever possible, outside of some sort of KYC for mining (and not even sure how that would  be done in a decentralized manner). Even if you can mine on a laptop, nothing prevents someone else from using two laptops and therefore having access to twice the nonce space, right?


## jtgrassie | 2018-03-14T23:07:10+00:00
IMHO, the issue is that ASICs _currently_ are very centralized. If there were ASIC products on the market with fair competition then there would be no reason to be ASIC resistant. Currently that's just not the case. The problem is, whilst there is this path of ASIC resistance, what incentive is there for anyone to develop ASICs for Monero mining; zero. It's a double edged sword (or rather chicken and the egg scenario). We either let the current players develop ASICs for Monero and accept it will be centralized to some degree for a period, or we resist, which deters possible ASIC development and competition in the market. I guess I feel a good end-state is multiple ASIC producers, as then ASICs become commoditized, and there's nothing bad about that (hardware the masses can use to mine at commodity prices with better margin, r.e. electricity cost & hardware cost / return).

Let's be honest, mining is _already_ centralized to some degree. GPUs (AMD and Nvidea) and CPUs (really just Intel by the numbers). The price of these, which were once commodity hardware, have been growing due to demand. 

Ultimately I feel mining has to be profitable for the masses. If ASICs make it more profitable for the everyman then great. If there is no profit in mining at all then what's the incentive; ideology alone?

Independent miners is more decentralization, which is the ultimate goal.

In summary, I think we are not yet at a place where there is sufficient ASIC competition, and thus decentralization. But to some degree, by being ASIC resistant, we contribute to the problem.

I'd welcome a world where there were more ASIC manufacturers that current GPU/CPU manufacturers! This _may_ be the future!


## iamsmooth | 2018-03-14T23:24:35+00:00
I'm not sure a competitive/commoditized market for ASICs will ever make sense. 

CPUs and to a lesser (but still some) extent GPUs have the markets they do not because of the manufacturing (which is at least as centralized), but because they are general purpose products which lends itself to having many disperse and competing distribution channels. In most even mid-sized cities you can find multiple stores where you can go and and buy CPU and GPUs both as individual components and as part of a system. Plus of course on-line from both many resellers and manufacturers directly. There are thriving gray market channels (probably actual black market too, thinking about hijacked shipments, etc.), a robust and deep used market, etc. 

None of this really exists for mining ASICs (just as it doesn't exist for other forms of ASICs) and may never exist, because it is far more specialized (er, "application specific"). It is natural to have a narrower and more structured distribution system which in turn naturally lends itself to a higher degree of centralized control and vertical integration where efficiency trumps reach. Though I guess it is possible to envision enough diversity among types of miners that there might be value in broader distribution (if so, then one likely needs to accept 'hobbyist miners' as an important part of the system).

Still this doesn't change the fact that _unsuccessful_ ASIC-resistance (which some argue is inevitable) may still be worse than ASIC-friendliness.

## jtgrassie | 2018-03-14T23:50:07+00:00
> I'm not sure a competitive/commoditized market for ASICs will ever make sense.

It _could_ if there were _no_ ASIC resistance and there was profit to be made. Forget about the profit, there's even no incentive for an open source ASIC design when there is this hardline resistance.

I do get the point of your CPU/CPU general purpose but the prices have had a direct influence based on mining H rate. From production (demand) to gray-market sales (which are often even higher priced). Ultimately it doesn't matter whether CPU, GPU, FPGA or ASIC; whatever is most cost efficient to the person/organization - we risk centralization.

All I'm getting at is that currently, there are just not enough players in the ASIC space, so it risks centralization. If there were more, there would be a lower risk. But to get more, there has to be incentive.

Ideal state is that everyone that wants to be part of the ecosystem can run a node, mine and transact in the cheapest most decentralized way. ASICs _could_ be a help sometime down the road.
 

## iamsmooth | 2018-03-15T01:00:09+00:00
@jtgrassie There is very little risk of centralization at the level of access to equipment any time soon if ever for CPU mining, possibly not for GPU mining. The diverse and diffuse distribution channel and general purpose nature of the devices guarantees this.

There is a high risk of this with dedicated special-purpose ASIC miners. Indeed it is mostly just pure speculation that ASICs _might_, someday, become commoditized. If so, great, but we have no idea if that is actually true.

There will still be geographic, etc. centralization due to some aspects of energy cost, some degree of economies of scale, etc. but that's all additive. 



## stoffu | 2018-03-15T01:33:23+00:00
I wonder the possibility of ASICs becoming so advanced, so cheap and so commoditized that they become the default choice as heating devices. Everyone needs heating especially in the winter. The similar argument in andytoshi's writing sounds somewhat convincing to me.

## Gingeropolous | 2018-03-15T03:11:25+00:00
@iamsmooth , indeed, perhaps egalitarian access to the nonce space was too strong a phrase. But in general I'm trying to communicate that a layperson with consumer hardware should have a chance. Even now, with a network that may or may not be flooded with ASICs, botnets, GPU farms, and webminers, a person mining with 300 h/s, which is on the higher end of a home PC, could get 0.396 XMR / year. Its not nothing. 

I guess, ultimately, I think we should strive to keep mining feasible for your average person. In bitcoin, mining is not feasible with consumer hardware. With bitcoin, you would literally get nothing with a consumer grade home PC. 

There are efforts to keep Cost of Node Operation down in order to make it feasible for your average person (sync optimizations, size reductions of proofs, etc). I don't think mining should be viewed any differently. 

## stoffu | 2018-03-15T04:12:18+00:00
@Gingeropolous 
> There are efforts to keep Cost of Node Operation down in order to make it feasible for your average person (sync optimizations, size reductions of proofs, etc). I don't think mining should be viewed any differently.

I agree, keeping CONOP low is vitally important. Then, what's your response to Andrew Poelstra's following argument?

> #### 4 Actual frequently asked questions.
> ##### 2. Is ASIC resistance desirable?
> No. ASIC resistance typically involves increasing algorithmic complexity to discourage ASIC developers. However, ASIC’s are still inevitable; all ASIC resistance does is increase the startup capital required and therefore increase centralization of manufacturing. Further, increasing the complexity of proof generation often means also increasing the complexity of proof validation, often disproportionately slow. This discourages (unpaid) nonmining validators, which also increases centralization.


## iamsmooth | 2018-03-15T07:05:25+00:00
@stoffu "I wonder the possibility of ASICs becoming so advanced, so cheap and so commoditized that they become the default choice as heating devices. Everyone needs heating especially in the winter. The similar argument in andytoshi's writing sounds somewhat convincing to me."

Okay but this is somewhat extreme future stuff. 21.co tried that and it seems to not work out at all, yet. I don't know that it really has much bearing on whether ASIC-resistance is desirable *in 2018*. The underlying premise seems to be that you can't hard fork and whatever you do now you are stuck with forever, or at least until that somewhat extreme future arrives. Maybe a reasonable premise for Bitcoin...

> increasing the complexity of proof generation often means also increasing the complexity of proof validation, often disproportionately slow. This discourages (unpaid) nonmining validators, which also increases centralization

I don't really buy this. One per block is not that significant. Validating the rest of the block is a lot more expensive, as long as the PoW validation stays within reason (there have been a few really stupid attempts with 10 second PoW validation time or something).

If anything, cheap PoW validation maybe encourages SPV clients (which don't validate the rest of the block), and that seems also centralization-increasing to me.






## stoffu | 2018-03-15T07:35:27+00:00
@iamsmooth 
I agree with both of your points.

My another concern with ASIC mining even in the far future is that their manufacturing will most likely not be commoditized, and there will be a chance that all or most of the manufacturers are pressured by a powerful attacker to secretly implement things like a “kill switch”. This concern is totally irrelevant for CPU/GPU mining because anyone can compile mining software from source.

## jtgrassie | 2018-03-15T09:37:40+00:00
@iamsmooth I think a significant risk right now is your first bullet:
>1. Continued and repeated ad-hoc modifications to the PoW algorithm may accidentally (or even maliciously) introduce exploits.

I also recall a few comments from people on IRC with ASIC experience stating the most recent changes made will actually have little effect on any potential current ASICs. This points to the obvious need for specialist knowledge to help change the PoW each time it gets changed (both expert ASIC wise and security wise knowledge).

Being ASIC resistant thus far has certainly been a great benefit to the Monero ecosystem - how we can effectively maintain it is the issue IMO. 


## egodigitus | 2018-03-15T09:39:54+00:00
@iamsmooth @stoffu There is a company already experimenting with heating buildings through mining (https://www.cloudandheat.com/). And the centralization with ASIC manufacturers is similar to the IC manufacturer's market overall. It's a matured market (http://www.icinsights.com/news/bulletins/Samsung-TSMC-Remain-Tops-In-Available-Wafer-Fab-Capacity/).

## sammy007 | 2018-03-15T10:15:14+00:00
Glad to read @iamsmooth's cold head points here. ASIC resistance is a no go, leads to industrial espionage, corruption. Leads to self isolation and elimination just like every attempt to resist progress. At least status quo is needed for a while, until all pros and cons will be measured.

@williams-r

> Merged mining with bitcoin right now would increase centralisation pressure on bitcoin mining from the increased cost of node operation.

With merged mining you are getting a satellite coin for free also.

Actually, only one coin on a single algo survives. Look at btrash and look at BTC, btrash difficulty is almost 10x lower, easy to attack in case it becomes a real threat for a major group of BTC maximalists.

If you think really long term, only the most efficient PoW survives, there will be a fight for energy.

## SRCoughlin | 2018-03-15T14:56:53+00:00
@jtgrassie

> This points to the obvious need for specialist knowledge to help change the PoW each time it gets changed (both expert ASIC wise and security wise knowledge).

This is the reason that I'm disheartened that people are commenting here on ASIC development when they clearly have never done it before. (The blankets statement about 'resistance is impossible', 'corruption', etc. are not what you hear from experienced chip designers. Even 'commoditization' has little meaning other than run size.)

There are not enough ASIC SMEs talking about this for any useful discussion to occur. If there were a formalized process, then we might learn something.

## lisergey | 2018-03-15T16:04:56+00:00
Why not to seek PoS+PoW+Proof-of-Activity algorithms as a way to make egalitarian use of cryptocurrency?
I dislike PoW for huge energy consumption. 
Lowering CONOP also means easing centralized scaling. Alone it wouldn't incentivize hobbyists either.
PoS would attract long-term investors (pension funds etc) and e-shops, PoA would attract traders. 
Combined, IMO, would promote having a node on your own, with necessary limited mining.
I would also seek for Proof-of-Uniqueness algo to withstand scaling.

## SRCoughlin | 2018-03-15T16:25:53+00:00
@lisergey It's kinda hard to have a Proof of Stake or Activity when the coin is specifically designed to not track stake or activity.

## hyc | 2018-03-15T16:56:16+00:00
Argon2 design is worth a read. They're only relying on memory-hardness, and otherwise simple computations. https://www.cryptolux.org/index.php/Argon2

## lisergey | 2018-03-15T17:53:34+00:00
A miner would seek for most profitable rate/cost algo/hw combination. No interest in running a node if it is not mandatory. Then demand for more profit/cost-effective hw is stronger and wider. That are ASICs.
Sooner or later the progress would solve the challenge to combine FPGA with enough L3 cache, then most changes in PoW algo would be acceptable to high-scale miners. Therefore I support @iamsmooth ASIC-friendly proposal. 

@SRCoughlin, do you see a way to incentivize a hobbyist miner to run a node with current PoW?

## SRCoughlin | 2018-03-15T18:03:27+00:00
@lisergey You, as many others in this thread, seem to be confusing that which is in the interest of Monero miners to be equivalent to that which is in the interest of the entire Monero community. This is simply not true. Your argument about the 'acceptability' of high-scale miners is irrelevant because of this.

As far as hobbyist miners running a node, the best incentive is to continue altering the POW to incentivize the continued success of hobbyist mining, some of whom would run a node as part of the process. The cost-efficiency of nodes are not applicable to people who do so fun.

## jtgrassie | 2018-03-15T18:07:57+00:00
@lisergey 
> A miner would seek for most profitable rate/cost algo/hw combination. No interest in running a node if it is not mandatory.

You're confusing miner, node and user. 

> Sooner or later the progress would solve the challenge to combine FPGA with enough L3 cache, then most changes in PoW algo would be acceptable to high-scale miners.

An FPGA does not need to use L3 cache at all. They can already make use of RLDRAM3. See [here](https://www.reddit.com/r/Monero/comments/7x82yp/technical_cryptonight_discussion_what_about/?st=jesq7o4o&sh=f688e8b0) for better informed dialog on FPGAs.

> Therefore I support @iamsmooth ASIC-friendly proposal.

I think you are miss-reading @iamsmooth OP. I read this as a proposal to _consider_, not a proposal to _actually support_ ASICs. Rather a discussion starter.


## Gingeropolous | 2018-03-15T19:54:09+00:00
@stoffu , I think that argument is flawed. If there's a network that you can participate in that requires the computer you already own vs. a network that requires you to buy some multi-thousand dollar industrial machine, which has the lowest CONOP? I remember reading that post years ago and though it was wrong then as well. Its almost like its arguing for industrial scale mining.

> You, as many others in this thread, seem to be confusing that which is in the interest of Monero miners to be equivalent to that which is in the interest of the entire Monero community. 

excellent point @SRCoughlin .

What is in the best interest of a cryptocurrency whose entire value comes from the fact that its decentralized?

## fluffypony | 2018-03-15T20:05:17+00:00
From my perspective, this move makes TOTAL sense if SHA3 ASICs are commoditised to the point of being common place. Consider: Monero mining *already uses an "ASIC"* in the form of it taking advantage of AES-NI extensions on CPUs to give them an unfair advantage. If SHA3 extensions existed, and most GPUs came with SHA3 ASICs baked in, then the Monero network would benefit by embracing those commoditised ASICs. It would lead to a PoW algorithm that is significantly faster to verify, which would lead to faster IBD and more efficient transaction and block propagation, whilst making it much harder to DDoS the network.

Between now and then I will do everything in my power to help the community prevent the proliferation of centralisation-inducing ASICs on the Monero network.

## malsony | 2018-03-16T01:20:10+00:00
bitmain has released a new ASIC model, X3, https://shop.bitmain.com/productDetail.htm?pid=000201803132107063379CD35Gxy064F what shall we do against them? :sob: 

## iamsmooth | 2018-03-16T02:16:06+00:00
@fluffypony "From my perspective, this move makes TOTAL sense if SHA3 ASICs are commoditised to the point of being common place"

That's a big chicken and egg problem isn't it? If you are expecting some other coin to do the heavy lifting first then you run into this once the hardware is highly optimized and already deployed on another large network:

@otheATgh 
> as i do not think that the same HW should be used for both coins, it gives BTC maximilaists easy access to attack our network.

IMO the only way this can happen is for a major coin like Monero to adopt the algorithm seen as _best suited to commoditization_ and then wait, perhaps through several generations of product and growth of the network until a desirable sufficiently-commoditized outcome is achieved. That can include a degree of lead time and inviting multiple manufacturers in to produce a product, perhaps jump-starting the process a bit.

I agree this is nothing like the current mining ASIC market.

> Monero mining already uses an "ASIC" in the form of it taking advantage of AES-NI extensions on CPUs to give them an unfair advantage

And we've seen this is not nearly enough. The general purpose implementation, even with the embedded ASIC hardware inside CPUs seems to be about 30-50x less efficient. That's a big deal and what it says about viability here can't be ignored

> prevent the proliferation of centralisation-inducing ASICs

Can't disagree with that. The idea here would be promoting ASICs that are not centralization inducing.

I don't think you can dismiss the downsides of this active anti-ASIC strategy. I'm offering an alternative that attempts to reach a more sustainable outcome while _reducing_ centralization harms (or perhaps one could say substituting different, and hopefully less problematic, ones). Neither of these approaches may be fully successful though.

## Gingeropolous | 2018-03-16T03:18:31+00:00
@iamsmooth 

> Neither of these approaches may be fully successful though.

Which may be a reason why something as seemingly bonkers as a multi-PoW system might work.

Block 1 - cryptonight-v1 (or some other ASIC-resistant PoW, lets call it CV1)
block 2 - ASIC-friendly PoW
repeat

or maybe do 2 and 1, or whatever. 

or you could have 3. or 4 PoW that cycle. Code complexity - obviously But what does it accomplish?

By having two PoW, you prevent the control that an ASIC dominated network would have from ASIC mining centralization - because the general purpose hardware mining the ASIC-resistant PoW can also mine the ASIC PoW, just less efficiently. So ultimately, what is the most harm an Evil ASIC power can do, in general? Well, they can 1) stop block creation - just turn off miners with a kill switch 2) censor transactions and 3) perform a 51% attack.  With a bifurcated PoW system, these threats from ASICs are eliminated. If the ASICs get turned off, the general miners can mine. If censorship begins, the transactions will still get included in the general purpose blocks. And can they really perform a 51% attack if they can never control more than 50% of the network hashrate, and they can't continuously keep adding onto their own chain?

Yes, the problem still exists of needing to have an ASIC-resistant PoW, and ultimately the ASIC side of the chain could become completely and undeniably centralized, so we could just be letting the wolf in the door. 

As I've stated before, I am not in favor of ASICs until they are a commoditised, but as you mentioned, this is a chicken and egg problem. So perhaps with a bifurcated PoW (bicameral PoW?) , we can have the chicken and the egg coexist .... Schroedinger's chicken. 

## iamsmooth | 2018-03-16T04:22:50+00:00
@Gingeropolous 

Something like that might work. Some of the proposals to change Bitcoin PoW without bricking existing hardware have involved gradually transitioning to a new PoW over a period of say 18 months. We could do something like that where the ASIC-friendly PoW starts out with a small share and it slowly ramps up. Meanwhile the initially-larger share would remain the forked-every-six-months anti-ASIC strategy. This protects the network in the short term but puts us on a path away from this constant forking to something more sustainable and sane longer term.

A downside to this would be that the small share means less revenue, so less incentive to actually develop and improve the ASICs (particularly for more than one company) early on. Perhaps that would naturally reach some sort of balance over time as the share increased.

## stoffu | 2018-03-16T04:40:00+00:00
@Gingeropolous 
> the problem still exists of needing to have an ASIC-resistant PoW

Like others have noted already, the fundamental problem I see is that any PoW can be ASIC'ed, and perpetually tweaking PoW is probably unsustainable.


## ghost | 2018-03-16T11:08:10+00:00
@Gingeropolous 

A bifurcated PoW would be simpler to implement than the bicameral option I proposed above.  I don't know of any formally defined PoW schemes that do this. 

I'm not sure which is better. As I understand your proposal, in a bifurcated system where the blocks alternate between ASIC-hard and ASIC-friendly algorithms, the general purpose miners would only be able to mine profitably on every other block. In a bicameral system where each block is mined by completing each PoW, both types of miners can be profitable mining each block. But this is more complex and would be in uncharted waters as far as I know. 

@stoffu 

Yes they can be ASIC'ed, and this is a concern, but ASIC efforts will go to where they are most profitable. If the ASIC-hard PoW was simply too expensive to be worth the bother--say Argon2 with a large RAM requirement--it would make more sense simply to focus on the ASIC-friendly PoW. The RAM requirement could grow at fixed intervals to gradually make any existing ASICs obsolete and ensure that it remains unprofitable even with Monero price increases. 

Allowing ASIC miners as part of a two part system and relying on profit incentive to keep them in their place seems  easier than trying to continually keep them away. 

## sammy007 | 2018-03-16T12:06:18+00:00
> The RAM requirement could grow at fixed intervals to gradually make any existing ASICs obsolete and ensure that it remains unprofitable even with Monero price increases.

It's just stupid. You remember scrypt-n, right? RAM requirements will grow for non-asic and for asic miners and the profitability ratio will be the same.

EVERY attempt to beat ASIC will lead to hidden ASIC mining. Now device makers learned the lesson. There is nothing to talk about. We heard a lot of bullshit about how memory hard CryptoNight is, I see a device on market hashing as 300-500 GPUs and laughing.

***Update: I stand corrected, since there is scheduled PoW change every 6 month. Does not cancel my pro-ASIC sentiment tho.***

Next time Bitmain will produce a limited number of chips, spread it across shitcoins, with instant few days ROI it can last forever. By satisfying short term goals of GPU bagholders right now you will achieve nothing, GPUs abandon network when another rich shitcoin walks in.

FYI: Currently a single share validation of CryptoNight takes up to 15ms on relatively good hardware (with AES-NI) and it's a centralisation problem too. Another example is ZCoin with their retarded "ASIC resistant" algo which actually turned into miner resistant eventually making it impossible to verify blockchain on enterprise grade hardware. A great example of race for being ASIC resistant without any resistance at all.


## iamsmooth | 2018-03-16T20:57:32+00:00
> Currently a single share validation of CryptoNight takes up to 15ms on relatively good hardware 

To be fair multiple validations can be done in parallel so if you have multiple cores then it works out effectively a lot less. That doesn't change the fact that it is slow, **and is not performing its intended purpose**.

If we're going to rely on frequent PoW changes for ASIC-resistance (accepting the associated problems), then we should just use some fast hashing algorithm with some tweaks and get rid of this broken "ASIC-resistant" one, which isn't, at all.

> Another example is ZCoin with their retarded "ASIC resistant" algo which actually turned into miner resistant eventually making it impossible to verify blockchain on enterprise grade hardware

Yes, this is an issue with any of the algorithms which attempt to get ASIC-resistance by using large amounts of memory. Large amounts of memory becomes expensive and inefficient for everyone else too.

## iamsmooth | 2018-03-16T21:04:02+00:00
@jsfierro The Myriad method is probably the simplest way to have multiple PoWs active simultaneously. Each PoW has its own difficulty adjustment so (assuming perfect difficulty adjustment; obviously not quite true in practice) each block has a 1/N chance of being mined by each of the algorithms. You can adjust block target to change the mix. For example, if ASIC-resistant has a 2.5 minute block target and ASIC-friendly has a 10 minute block target, then in each 10 minute period you will expect to see four ASIC-resistant blocks and one ASIC-friendly block.



## SRCoughlin | 2018-03-16T21:13:55+00:00
@iamsmooth Isn't the Myriad method just a delaying tactic? The next round of ASICs would do all algos regardless of resistant/friendly and would switch targets to whatever paid the most per joule, etc.

## ghost | 2018-03-16T21:14:55+00:00
@iamsmooth 

Thanks, I had a feeling that someone had done something like this before. I'll have to read about it. 



## iamsmooth | 2018-03-16T21:19:19+00:00
@SRCoughlin I was only referring to the multiple-PoW aspect of Myriad, not claiming that multiple algorithms makes it ASIC-resistant.

The only thing potentially ASIC-resistant that I see as possibly working is this approach of changing PoW frequently. See top comment (and subsequent discussion) for trade offs.


## jwinterm | 2018-03-16T22:53:07+00:00
Myriad is kind of a case study in how the multi PoW approach at best delays ASIC implementation and still requires active intervention to avoid ASIC domination. When it launched in 2014 there were Sha and scrypt ASICs, qubit (similar to x11) was supposed to be the CPU algo, and skein and myriad-groestl (one round groestl followed by one round sha256) were supposed to be the GPU algos. Qubit was forked out for yescrypt when dash ASICs were released that could also do qubit, and skein and myriad-groestl are also both now ASICed due to ASICs targeted at Myriad's higher market cap progeny digibyte. So now myriad is looking to swap out skein I believe for equihash to "give back an algo" to GPUs, but I think this kind of demonstrates that the only real benefit multi PoW offers is that it can allow for some kind of rolling basis that allows some participation from ASICs and home hashers, but still requires constant active intervention. Another maybe more minor negative to this approach is that to then fully validate the chain you have to keep all these discarded algorithms, such as qubit, around in the source code to verify blocks from before they were stopped being used.

## iamsmooth | 2018-03-16T23:02:51+00:00
@jwinterm 
> but I think this kind of demonstrates that the only real benefit multi PoW offers is that it can allow for some kind of rolling basis that allows some participation from ASICs and home hashers, but still requires constant active intervention

Yes, that was exactly what was being discussed here, including the active intervention.

> to then fully validate the chain you have to keep all these discarded algorithms

Applies whenever the algorithm is changed.



## lisergey | 2018-03-17T03:01:03+00:00
How can we numerically estimate how is (de)centralized Monero network now?
By number of public pools? Pardon my noob question, I really like to learn.

## iamsmooth | 2018-03-17T03:35:01+00:00
@lisergey Centralization or decentralization is many-dimensional. One can identify points of centralization (and yes pools would be one of them) but how to weigh their importance against each other is highly unclear.


## lisergey | 2018-03-17T04:27:26+00:00
@iamsmooth, what points of centralization do you see? please list them.

## lisergey | 2018-03-17T04:29:39+00:00
I suggest to weight each point of centralization against risks of:
- 51% attack, including cartelization between large pools and/or mining farms
- renting huge hashrate for short time to close gap to 51%-attack
- selfish mining by large pools
- disproportions in hashrate by regions with cheap electricity (moments of blackout may give potential advantage)
- ddos to particular nodes together with above

Then we see, how ASIC-resistance can really help keep decentralization.

## mrheinen | 2018-03-17T13:53:17+00:00
I would like to point out that besides ASICs there are also PHI servers that currently have at least 50% of the ASIC performance at a lower costs (higher power consumption though). I doubt these will be affected by any PoW change.

https://lukminer.org/2018/02/01/finally-asrock-rack-confirms-2800h-s-on-phi-7210-and-3000h-s-on-phi-7250/


## sammy007 | 2018-03-17T14:33:02+00:00
> have at least 50% of the ASIC performance

You have no idea what you are talking about.

## mrheinen | 2018-03-17T15:16:00+00:00
In that case do you mind educating me ? I was comparing the phi server to the Baikal n.

## jtgrassie | 2018-03-17T15:57:52+00:00
@SadBatman Google: Xeon Phi. You'll find it's a high-end, massed produced processor. Not a "phi server" as you are calling it. They have nothing to do with ASIC resistance as they are quite simply massed produced CPU's.

## sammy007 | 2018-03-17T16:01:10+00:00
> In that case do you mind educating me?

Okay. `3,000` H/s of Phi (according to article) `!=` `220,000 H/s / 2` (according to your 50% statement)

## iamsmooth | 2018-03-17T16:05:36+00:00
@sammy007 he was comparing it with the much cheaper Baikal ASIC which is only 20k h/s. The Phi-based solution claims 10k/sec (though higher power usage).


## iamsmooth | 2018-03-17T16:13:05+00:00
@lisergey I don't think you can numerically measure many aspects of mining centralization, ever. Mining by its nature is not a very transparent process, so we never really know who controls what hash rate and how. The best we can do is infer from observations and market dynamics. 

For example, when an ASIC manufacturer such as Bitmain runs massive farms itself (as it does in Bitcoin) then it is clear there is a high degree of vertical integration and likely a lot of hash rate centralization. Exactly how much is never entirely clear though. Some people claim Bitmain controls >50% by themselves, some claim they don't.

Likewise if we see a lot of individual miners building various size rigs and mining at home or in modest size farms (which they are able to do because the equipment they need is available through  large and diffuse distribution channels), then we can infer mining is likely not that centralized, at least at a hash rate level. Or for that matter, seeing botnets that are small (most credible reports of botnets identified and reported on by the security communities talk about how they have mined $X worth of Monero over some period of time, with $X generally being a pretty small number).

That's at the hash rate level, there is also the pool level, and the developer level, the geographic level, the exchange and merchants ecosystem level, etc. All can be points of more or less centralization. Some of these may overlap, such as the geographic distribution of developers. Mining certainly isn't everything.


## williams-r | 2018-03-17T20:25:36+00:00
The only reason for an ASIC-resistant POW is to prevent centralization from mining ASICs.

When SHA256 ASIC manufacturing is decentralized soon(tm), or those companies are ready to make skein or SHA3 ASICs, that would be a good time to switch the POW to ASIC-friendly.

@fluffypony 
Also, if SHA3 gets baked into commodity CPU and GPU silicon, and Monero then switches to SHA3 POW, the time could be right to not change the POW again when SHA3 ASICs are developed, since there could be multiple successful ASIC manufacturers by then.

When ASIC manufacturing is decentralized, ASIC resistance is obsolete.

## iamsmooth | 2018-03-17T20:31:23+00:00
> The only reason for an ASIC-resistant POW is to prevent centralization from mining ASICs.

Is it the case that is the only reason? I've heard people express that it is good to minimize the barriers to entry so people don't have to make a significant up front investment in hardware in order to mine at all. 

For example, mining without special purpose equipment allows hashes to be used as a form of universally-available micropayments, as we are starting to see with web miners (the legitimate ones salon.com not the malware ones).



## williams-r | 2018-03-17T20:44:37+00:00
A high barrier to entry is centralization. A computer capable of 440 h/s on cryptonight can be bought for 350-ish dollars, and a bitcoin asic with over 20x the mining revenue can be bought from halong for under 3000 dollars. things are moving in the right direction.

I like the idea of a token-less network with cuckoo cycle as antispam.

## iamsmooth | 2018-03-18T03:23:29+00:00
I would not say that barriers to entry and centralization are necessarily the same (note that I said minimizing barriers to entry and not only avoiding "high ones"). You can have non-high barriers to entry and potentially a low degree of centralization, but even low barriers may foreclose some interesting use cases that avoiding ASICs enable.

If you have to have some special purpose equipment that most people don't have, then micropayment systems based on free entry into mining become impossible, because very little of the addressable market will ever have the equipment (i.e. how many salon.com readers will have a Bitcoin mining ASIC?). 

The cost of equipment specifically needed to mine cryptonight (in some hypothetical ASIC-resistant form) in order to access salon.com is effectively _zero_, because effectively everyone already has a mining-capable device (to some extent at least). I'm excluding very old or very low end hardware here of course.

If by "things are moving in the right direction" you think there will be mass market ASIC mining chips included in consumer devices such that the barrier to non-dedicated use is again removed, I would only say, "sure maybe" (and I mean this sincerely, in the sense that it could very well actually happen), but that certainly doesn't describe any world we live in now or in the next few years.

## williams-r | 2018-03-18T06:37:54+00:00
 What I meant, was that it's possible that there will be 350 USD asics capable of 2x the revenue of a 350 USD desktop PC (what i consider the minimum useful for mining monero, since mining on a laptop is bad for its CPU). They don't exist now, but when they do, I think that would be a good time to go ASIC-friendly.

I can see the utility of ASIC-resistant hashing for micropayments, but in terms of economics, that will be less efficient than an ASIC or even a desktop PC, and mining will tend towards what is efficient. 

Letting Salon mine on your CPU or GPU is for sure an easy way to do micropayments, but it's probably better to use LN and payment channels on bitcoin for that(or monero's future second layer), with a higher barrier to entry of course.

New people may not realize that the electricity they are burning and the wear on their CPU and GPU are worth more than visiting Salon, but I hope the public will learn this stuff eventually.

## maesitos | 2018-03-18T10:58:51+00:00
@Gingeropolous

> For me, the problem with an ASIC friendly PoW is that you can never beat the economies of scale that ASICs provide. So even when ASICs become commodified, and every phone has an ASIC because reasons, and lightbulbs and toasters because you have to hash for service, we may have achieved an egalitarian access to the hardware, but we may not have achieved egalitarian access to the nonce space.

There is an egalitarian acces to hardware right now as you can purchase it at the same price I can. But even if we are not in that stage and we reach that egalitarian access, in a free world there will be different people that have different savings for multiple reasons and those with more savings can acquire more of that hardware than the rest. So unless you control every bit of the human activity, there is going to be accumulated capital that invest in the network more than others no matter what you do.

The change in the PoW algorithm is really a much more deep debate than the technical debate. It's the old debate of freedom and inequality or central planing and equality. Free markets are very strong and there is little chance you can fight against it with forks in the long term, the free market are million of people thinking and you'll be blown away with the solutions they'll find to increase productivity and hash rate no matter what you do.

A Proof of Work system  is not a one person one vote system, it is a skin in the game and investment and risk based system. Anyone can mine, if they risk and invest. "_1 CPU one vote_" has been misinterpreted.

At the end of the day, a cryptocurrency has a strong free markets fundamentals. It's an irony that someone is trying to create one and fight the free market at the same time.

My two Shatosis.

## tevador | 2018-03-18T12:43:13+00:00
> 1. Continued and repeated ad-hoc modifications to the PoW algorithm may accidentally (or even maliciously) introduce exploits.
> 2. ASIC developers may build in more flexibility to their designs to be able to accommodate small algorithm tweaks (indeed this may already be the case, we don't know).
> 3. Potential for favoritism/corruption if plans for tweaks are leaked or influenced far enough ahead of time that some favored ASIC developers may have enough lead time to produce ASICs, while others do not.

These issues can be solved by designing for example 4 PoW candidates at once, testing all of them thoroughly for 6 months and then choosing which change will be implemented based on the hash of a block that is for example 2 weeks before the scheduled hard fork date.

The PoW changes would need to be sufficiently different from each other so that designing an ASIC for all of them at once would be cost-prohibitive (not sure if this is possible).

## Gingeropolous | 2018-03-19T04:01:28+00:00
@maesitos , I would put forth the notion that what cryptocurrencies are trying to develop goes beyond what free markets are capable of doing. 

I mentioned this in a conversation elsewhere, but it completely boggles my mind that in discussions about a facet of cryptocurrencies, which were developed to upend, remake, and disrupt our entire financial system, people reference facets of the system that cryptocurrencies hope to replace. 

I would argue its a conceptual divide that can be described as "cryptocurrencies will replace banks" vs "cryptocurrencies will render banks moot", or something along those lines.

I'm reminded of a post I created long ago, where I envisioned a future world where bitcoin becomes the international currency. Its not hard to imagine that the network becomes controlled by the state powers, because they can amass massive mining resources. Meanwhile, the rest of the normal people try to mine with whatever they can get their hands on (which is nothing, because the state controls ASIC production and any new ASIC efforts get consumed by the state because reasons). Add on top of this, the fact that bitcoin is highly censorable, so in order to get mined into a state block you have to follow the rules of the state mining operation, but most of the blocks mined are by the state. Every once in a while, the freeminers get a block, so all is not lost, but its a neverending battle, because the freeminers are a rag-tag bunch using general purpose hardware, pilfered ASICs, and pirate operations. 

So again, this notion of "free markets are strong" is a vestige from what will become an ancient system. And I'm not anti-freemarket. I don't think thats what is the crux here.

The crux is to imagine something beyond these constructs. And if we allow this thing known as cryptocurrency to keep evolving in a state wherein the forces of the ancient system can't poison its development, we might just reach that beyond. 

## juanpc2018 | 2018-03-19T14:39:42+00:00
If you like ASIC, get a S9 and start mining BTC.
ASIC mining already exists, Your proposal is nothing New.

Some history: Dogecoin was an improved version of Litecoin and was killed when Dogecoin algorithm could be mined at same time with ASIC Litecoin Scrypt Miners. Nobody gives $1usd for 1000 Doge.
And is better than Litecoin, but the algorithm & the core Is the same.
Doge was killed again, "twice" when a Doge to Ethereum Token bridge was created last year.
All Doge Coins will eventually move to Doge ETH token, validation method.

ASIC is very centralized "very bad.", ASIC war will kill Bitcoin in the end, 
ASIC only have 1 purpose "Really very bad."
Imagine a CPU & GPU that can only run 1-Game. Back to Arcade Games.
¿What is the ASIC war? There are people making private ASIC Miners, in Rusia, China and others, 
If BTC becomes too popular, or price too high, Nobody will sell ASIC Miners to you.
If yours gets broken... guess what, No parts. LOL. Jajajajajajaja 

The original idea of Bitcoin was Decentralized, Non-centralized.
GPU Only mining "like Ethereum" has increased the price of GPU's & memory world wide... a used GPU has the same price today, when it was New.

CPU mining is the future.
There are 2 coins using the Argon2d algorithm, Dynamics, and Credits CRDS, but Dynamics is a copy of CRDS "1-year old", designed to fool websites like coinmarketcap.com.
It's Like teens purchasing alcohol with fake ID's, there are a lot of artificially inflated coins in the Top100.
But most people like mining Dynamics, because the price is artificially inflated. 
¿How to artificially inflate a coin? 
You pre-mine the first 500.000 blocks in 1-day or week or month, then you say the coin is not pre-mined, then you create a bunch of Bots with Wallets, and start moving the coins like crazy... 
Result: "The coin must be good, look how is moving with just 1-year old.'

I have requested to coinmarketcap.com a minimum of 3-year old to be in the Top100,
"You" should do/request the same.

Things I like about Monero algorithm: low power consumption at 100% load, 
Other algorithms use almost twice the power at 100% load.
Similar to ETH power consumption, but better, because CPU still can be used with decent results.
Needs large L2/L3 Cache is interesting.

Problem with Monero is the fee, too high, 25% for small transactions.


## SRCoughlin | 2018-03-19T22:41:57+00:00
@tevador Yes, the random strategy is the best defense possible against ASICs because it can easily be tuned to kill all returns on investment. I'm preparing to write a paper on this and could use some help. Let me know if you have time.

## maesitos | 2018-03-20T00:34:34+00:00
@SRCoughlin why would you want to kill the return on investment? isn’t that what precisely keeps the miner honest, that is, the hope for the investor to not lose money?



## SRCoughlin | 2018-03-20T00:48:32+00:00
@maesitos The theory is that large-scale ASIC miners want to have return on investment to the exclusion of the success of the community, while CPU miners care as much about the community as their returns. By spoiling the economics of the large-scale ASIC miners' venture, you disincentivize them from bothering the develop ASICs in the first place, leaving the community in a more stable long-term situation.

## maesitos | 2018-03-20T01:15:52+00:00
Any attempt to control the economy has failed and will always fail. Bitmain has only proven how you can’t calculate the future and the economy. The sooner the market evolves the less abrupt the changes on the mining difficulty will be. But yes, I t’ll be disruptive, change always is. Soon you’ll integrate cucku cycle and some guy will bring a mega memory bus...

I don’t know why you think I’m less interested in the project if I buy from Nvidia or Bitmain. I see no relation.

I’m very disappointed with Monero and the boycot on free enterprise. I can’t understand how one can hate miners in a PoW system.

## TheTrueForce | 2018-03-20T01:39:10+00:00
ASICs are targeted because they take the power of 10+ Vegas and put it in one device, making it very easy for ASICs to dominate the network, leaving the common man with a computer to effectively pick up the scraps.
The people who are against ASICs want the hashpower to remain spread out over many users and locations. This makes the network more robust and harder to shut down.
ASICs tend to put a lot of hashpower in one location, in the hands of a very few miners. This makes it relatively easy to take out a large chunk of hashpower. If the power there fails, the network hashrate drops significantly. On the other hand, if I close xmr-stak, that's just a drop out of the ocean.

We're more interested in easy entry. A little bit of profit for everyone in, using hardware they already have.
ASIC miners are made to grab as much as possible. In doing so, they make it much harder for the average joe to get in profitably. That's why we don't like them.

## HeathenPagan | 2018-03-20T05:16:00+00:00
Points to consider:
1. Although GPU & CPU manufacturing is duopoly or oligopoly those commodities serve other purpose than mining alone. Those markets and industries have other profit / revenue motives than making instruments for mining alone. Example, AMD is still struggling even after making the best GPU mining cards for several years. don't get me wrong here I really want them to survive and be a better 2nd for consumers' sake on both cpu & gpu front. Even if a manufacturer can not compete in mining segment for sometime they can come up and compete investing money from say CPU / Gaming segment to fight another day.  It will be a different thing when you sign up for a ASIC monopoly or a duopoly with the no 1 player controlling 99% of the market in the largest coin as well as holding the ownership of largest pool & coin. Rather if we stay ASIC resistance may be AMD, Intel, NVDIA and samsung will improve some of their consumer grade products to narrow the advantage of ASICs.

2. There is a higher chance that as long as it will be reasonably profitable to mine using GPU & CPU we are more likely to retain student / researcher / gamer hobby miners. They are more likely to try mining this way as even if mining fails they will still have a good machine for their study / works / hobby / games. Eventually even if some of them want to grow into a small data center you will have more entrepreneurs from the grass root level. If the only option of an entry level player is to buy an ASIC only from 1 company after spending lot of money and questionable service and payback period, i am sure they will be more hesitant.  That will definitely be bad for decentralization. Mining in small way is also a better model to own and support a currency rather than buying volatile asset directly from market as that is a very difficult to hold for a small investor. That way you will also have a diverse base who would like to spend monero to buy something useful to them. The other way to acquire such a user base is to start a marketing campaign like corporate coins zcash or ethereum. I don't think we are trying to take that path.

3. The choice is not between being ASIC friendly vs ASIC resistant. It is about doing nothing vs being ASIC resistant. If we want CPUs & GPUs to compete with ASICs then we will have to be ASIC resistant. ASICs already have an unfair advantage over CPUs & GPUs so there is no need to be friendly to them.

4. Once CPU & GPU mining is outdated your normal users / miners will be in a higher proportion less hands-on and loose the understanding / learning they get by creating a desktop themselves, running a node, etc. It will be easier to influence them by propaganda / advertisement as they will be less hands on.  I believe Monero today thrives on innovation & technology and not on advertisement & propaganda. There are many products that thrives on technology & innovation rather than marketing and I believe monero is one of them.

So, I essentially agree with FluffyPony under current situations. If the ASIC industry players greatly improve upon their reputation and start treating their customers better in next few years then we might reconsider.

I you were to consider staying ASIC resistant, here are some thoughts (all of you are technically superior to me..........so just ignore if there is no merit in those suggestions.)
1. What about mandating every miner run a full node?
2. What about sharing the reward with running nodes in proportion to their peers/ uptime? this is one Zencash idea I like.
3. increasing the effective memory requirement to 4GB?
  
Disclaimer: almost my entire crypto investment is in monero even more than bitcoin and somewhat comparable to traditional financial investments (I am a small guy). I will stop mining monero if ASIC becomes predominant. Just a data point. 

## maesitos | 2018-03-20T10:51:48+00:00
@TheTrueForce

> We're more interested in easy entry. A little bit of profit for everyone in, using hardware they already have.

This is not spare hardware an average Joe has seating around.
https://www.youtube.com/watch?v=VR1G1qROsrM



> making it very easy for ASICs to dominate the network, leaving the common man with a computer to effectively pick up the scraps.

As for March 2018 I need 100,000$ to match the Antminer X3 that sells for 3000$. If I were to enter the mining space, the Antminer X3 is giving me a competitive advantage over the current 'oligarchy'. I'd argue it's precisely the opposite, free market gives opportunities to new Joes. [Not my math but Riccardo Spagni's](https://twitter.com/fluffypony/status/975412221651103744)


> ASICs tend to put a lot of hashpower in one location, in the hands of a very few miners

[Ethereum GPU](https://etherscan.io/stat/miner?range=7&blocktype=blocks) mining and [ASIC Bitcoin](https://blockchain.info/pools) are distributed in a very similar way.


So what you are pursuing is not happening. Your mental model do not match the reality.

@HeathenPagan You are basically trying to manipulate and control the market at will and as I said earlier, it's been proven throughout history a bunch of humans can't articulate the interaction of the rest, it's immoral and coincidentally impossible. Apart from that you are biased in the debate as you have self interest in not letting the competition to enter the space and I suspect a huge portion of all the noise is caused by miners not willing to stop their business. How's that different from a cartel o licence issuing from governments?


## ghost | 2018-03-20T12:12:09+00:00
How can you guys accept ASICS?
Do not you see that most if not all ASIC miners are made by very few companies?
Do you accept that monero be dependent on a minority who have the technology to make fast miners?

Bitmain has used their miners and ripped off monero network for 3 months if look at difficulty chart and you will know. 
If monero became ASIC friendly how can you guarantee that there is no other company designed 100x speed closed source miners and keeping it for them selves to rip off the network.

The new algo should be more difficult for ASICs and if they could make a miner then it should be sanely faster than its predecessors rewarding their effort but not 100x faster. This simply distablize the network. And will be only 1% of miners having the 99% of hash power which is against decentralization.
 I guess in that case a viat currency will be safer. At least being in the hands of a government is better than being in the hands of a company like bitmain.

Moreover let me tell you what bitmain did is that they violated the GPL that monero is based on. Simply they used the open source cryptonight algorithm and designed closed source ASIC miner for their own benefits are you saying to make monero friendly to those?

## tevador | 2018-03-21T09:35:38+00:00
> This is not spare hardware an average Joe has seating around.
> https://www.youtube.com/watch?v=VR1G1qROsrM
> 
> As for March 2018 I need 100,000$ to match the Antminer X3 that sells for 3000$. If I were to enter the mining space, the Antminer X3 is giving me a competitive advantage over the current 'oligarchy'. I'd argue it's precisely the opposite, free market gives opportunities to new Joes. Not my math but Riccardo Spagni's

The point is that the costs should scale at least linearly with hashrate. You can't stop someone from investing millions of dollars into a GPU mining farm. Egalitarian access to hardware doesn't mean that every miner is entitled to having the same hashrate as a GPU farm.

> Ethereum GPU mining and ASIC Bitcoin are distributed in a very similar way.

While the distribution of hashrate among pools may look similar, 72% of bitcoin hashrate originates from China (based on an article from 7/2017), ETH hashrate is more evenly distributed across the globe.

ASIC manufaturers usually run large scale mining operations with their newly developed hardware before they decide to sell it. You don't see this happening with commodity hardware like CPUs and GPUs. Additionally, ASIC manufacturers can include [backdoors](http://www.antbleed.com/) in their hardware which they can use to control the network.

For these reasons, I strongly support the decision for an ASIC resistant PoW scheme for Monero.

## TheTrueForce | 2018-03-21T13:43:14+00:00
@maesitos Obviously the common man won't have a data center in his pocket. I was talking about the average PC and you know it.
I do not much care about hashrate, as long as I get some. I will not buy an ASIC miner, so that I'm not cutting into anyone else's earnings too much. That's where I'm coming from. Not screwing over my fellow miner.

## maesitos | 2018-03-21T19:03:43+00:00
@tevador

> The point is that the costs should scale at least linearly with hashrate.

I can't  disagree it's a nice idea but will never happen and it's already proven. It's better to have a competitive market to avoid big jumps.

>  ASIC manufacturers can include backdoors 

The bank door you point to, not only has been removed but it's a very weak argument since ANTminer has little to none control over your device. You can connect to a different pool or run your own pool in your localhost network. I think this was just in order to give support to his customers.

I just don't understand why many people hate Bitmain so much, he's done nothing wrong to any project but the opposite.

@TheTrueForce 

> Not screwing over my fellow miner.

Competition is all about improving the guy next to you to make more than him. Mining is not about having friends and having a good time—though you can


## ghost | 2018-03-21T23:50:20+00:00
'''I just don't understand why many people hate Bitmain so much, he's done nothing wrong to any project but the opposite.'''

Because their act represents conflict of interests.
They should not be able to influence the intrinsic value of the crypto currency. However they are the ones who run and produce the most hash power in the world. This simply make the crypto currency under their control. 
They can screw it up and they are doing so for their own benefits.
Monero should not be under control of any party and any one should have almost equal influence this is the-so called decentralization

'''
Competition is all about improving the guy next to you to make more than him. Mining is not about having friends and having a good time—though you can
'''
Do you call a guy with a machine with 100x hash power of high end GPU a competition?

You are actually forming a monopoly.

## malsony | 2018-03-22T01:35:15+00:00
@maesitos 
1st batch of X3 was $11,999, but now 3rd batch of X3 is $3000, and 4th batch of X3 will be $1900. I assume that the decline of the price means that the hardware provider lacks of confidence. Oops, this story sounds familiar, right? Look for their model D3, which is made and designed for Dash Coin mining, and is $550 now, why is it so cheap (comparatively) and why do they still have stock?

You missed one thing, DIFF! You will get giant hashpower if you have an ASIC miner, but sooner or later, greater DIFFICULTY will make it harder to recoup your investment.

## HeathenPagan | 2018-03-22T04:11:08+00:00
@maesitos 

I am not clear what you are trying to convey. You seem to have a lot of contradiction.

"You are basically trying to manipulate and control the market at will"

- I did not understand how I am trying to manipulate and control the market. What is your market experience? have you tried trading stocks, bonds, commodities, futures, options, currency, interest rates, structured products, otcs for living? how is crypto market different from these? which ones of these are manipulated and which ones are not in your opinion? Let us assume some entity is capable of "manipulating" one of these markets for sufficiently long time. What stops such an entity from "manipulating" any/ all of the other markets eventually? 

On the other hand you don't think Bitmain is controlling or manipulating any markets? do you? Or do you not have any issues with Bitmain's vetically integrated monopoly on ASICS, bitcoin pool and bitcoin? Then why are you bothered with GPU miners "oligarchy"?
On a lighter note I wish I was that capable.

 "and as I said earlier, it's been proven throughout history a bunch of humans can't articulate the interaction of the rest, it's immoral and coincidentally impossible."

Suffice to say you are completely wrong. It has been done before, being done now and will be attempted in future and may result into unintended good or bad outcome for the humanity. Such attempts has been more successful controlling greater share of resources available generally speaking as civilization progressed. 

Just because something is immoral does not make that impossible. Morality is personal opinion subject to debate and possibility is Math. If we ever happen to meet we will have that discussion with your favorite beer on me. 

Don't forget bitcoin itself was invented to counter such a highly centralized diktat that only government is allowed to print and value (more so devalue) currency. If you are fine with centralization of treasury / mint function then what is the fault of good old USD or any other stable FIAT? I don't see any value in doing all this to just transfer the mint from federal reserve to Bitmain's control. This is the primary reason I hold & mine monero & other gpu mineable ASIC resistant coins than bitcoin. 

 "Apart from that you are biased in the debate as you have self interest in not letting the competition to enter the space"
You are again personally attacking me just because you don't like my opinion or thought. At least I provided a clear disclaimer. I did not accuse you and all other people that are ASIC friendly to be paid agent / stakeholder of Bitmain. I don't think that is a fruitful way to have a discussion. 

If I am biased who has certified you to be unbiased? Bitmain?

Anybody can buy a computer, GPU, download Wolf's free miner and mine. There are multiple options of GPUs, CPUs, Motherboard, hdd, available from mutiple distributors at different prices. I myself use a computer I bought in 2008 for gaming. That is how I started mining and I still mine using that. It is still profitable with very old cpu & motherboard from 2008. There are fair public pools like monerohash & Crypto-monero.fr for example who had themselves forwarded hashpower to smaller pools when they were approaching >25% size few years back. they are also business. Had bitmain done that ever?

It is very clear that Bitmain and possibly others had developed ASICs around last fall since difficulty suddenly started rising. Did you look at the network hashrate distribution recently? largest public pools are just a mere line in the pie chart most reduced to <1%. Unknow / private is 94%. It had been this way since last fall. They had mined themselves until monero team proposed public statement of their intentions to fork in march april and immediately they came up with a public offer to sell ASIC in march and delivery in May? So they just want to mine themselves untill the fork comes into effect and dump their useless miner on public.
 
Who is closing the door on competition if not bitmain and ASIC manufacturers?

"and I suspect a huge portion of all the noise is caused by miners not willing to stop their business. How's that different from a cartel o licence issuing from governments?"

How is that better for Bitmain who already has monopoly on a much larger market bitcoin trying to establish a monopoly on monero? What if I suspect this blaming the minergame being caused by paid agents of bitmain?

## VEGAtoken | 2018-03-26T14:34:31+00:00
We fully support a decentralised mining arena, giving free meaningful individual choice in contribution to the crypto sphere.

Ofcourse from the small to medium miners viewpoint, we are forever played between the blockchain algo administrators intent and the Bitmain/Baikal order books.

Thus positive steps have been taken by the GPU mining community, to self fund R&D for upgrades instead of waiting for handouts .

We need stringent GPU compute specific blochain algos. This is a near future project for us at VGA.

If you can rely on something is that, absolute power corrupts absolutely every time.

https://vegatoken.org/


## hyc | 2018-04-03T19:45:42+00:00
@polyorca elimination of botnets and malware is 100% an OS vendor responsibility. It's their job to plug their security holes. It is pointless to discuss it in any other context.

## sammy007 | 2018-04-04T02:28:05+00:00
@hyc lol really? It's impossible to close all holes and never will be. The only way to eliminate this shit is to make it economically unprofitable. Just in case somebody cares about practical aspect.

## hyc | 2018-04-04T02:34:31+00:00
@sammy007 botnets existed before cryptocurrency. Your argument is totally invalid.

## sammy007 | 2018-04-04T02:38:00+00:00
My argument is totally valid, it's about removing malicious source of hashrate from monero network which is even more weird than any ASIC manufacturing scam. I am not trying to make world perfect. What is worse, ASIC manufacturer who only want to dump devices on morons or windows defender which can wipe out miners from millions of machines around the globe at once and make network diff fall dramatically leaving network open for 51% attack?

## polyorca | 2018-04-04T06:26:02+00:00
@sammy007 what is your practical solution, or if you had to choose the lesser of two evils between ASIC friendly or windows defender situation? 

## sammy007 | 2018-04-04T06:56:36+00:00
@polyorca practical solution is in the title of this issue. Or at least make it CPU-resistant like ethash which is 20x less profitable to mine on CPU.

## iamsmooth | 2018-04-04T07:20:33+00:00
@polyorca I opened the issue but it isn't 'my' issue. There seems to be plenty of (arguably) productive discussion going on that doesn't involve me.


## iamsmooth | 2018-04-04T07:20:48+00:00
(closed by misclick)

## sammy007 | 2018-04-04T08:23:27+00:00
Somebody with access please delete this trash https://github.com/monero-project/monero/issues/3387#issuecomment-376187537 and this my post too.

## ghost | 2018-04-04T12:25:20+00:00
Sumokoin is under attack by ASICs now that their network is staling for over 5 hours. that is what will happen with ASIC friendly coins.

## TheTrueForce | 2018-04-05T05:37:28+00:00
I think it's more that they're mining as much as they possibly can before the algo changes over. TurtleCoin got hit by them a few days ago.

## VEGAtoken | 2018-04-05T11:17:03+00:00
Cryptocurrencies are founded on the philosophy of decentralized use, access and processing so as to avoid the current FIAT mess created by the **centralised**  funnymoney printers. Anything that works against the decentralised mentality is a threat to people power and we strongly oppose it.

## erkinalp | 2018-04-05T11:51:27+00:00
> Consider a bad scenario: a botnet controls a disproportionate amount of the hashrate and/or ASIC 
> farmers do the same. The botnet could never compete with the ASICs on the second stage, but the 
> ASICs would have difficulty competing with botnet on the first stage. Some separation of hashing 
> power would exist, similar to a bicameral legislature.

One thing is missing: you put the senate in the wrong place. ASIC-resistant algo needs to be go after ASIC-friendly algo.

## juanpc2018 | 2018-04-05T14:27:42+00:00
There is a New Ethereum ASIC miner "The E3" = 4.5x Watercooled Vega64 @ 800w, 
ETH has 2 threats now, the ASIC miner & the Metropolis update from PoW to PoS,
Some people claim China had the Ethereum ASIC miner long ago, but is selling Now because the Metropolis update is coming. 
The E3 probably was a "Declassified Secret Weapon"

GPU Miners are asking for a Fork, a New Algorithm, Probably will make the Metropolis update launched sooner, incomplete with bugs creating chaos... "All GPU & ASIC Mining Farms will be left outside the game with the PoS algorithm."
All that power will have to move somewhere.... 
But where?  Ethereum Classic "Never Changes" will continue to use the same algorithm, and those ASIC Miners will make Ethereum Classic a comeback from the Ashes.!

Make your bets, I bet the price of ETC will increase when ETH goes PoS.
There is No point making a Fork to soon from the Metropolis Update.., Could make the coin crash, Making a Fork Now will make harder to launch the Metropolis Update...
Making 3 Ethereum coins...
Classic "Inmutable."
2016 Fork, mutated again in 2018.
And the Metropolis Update...

Anyway.. back to Monero... the New v7 algorithm, will be launched in April. 
XMRig is CriptoNight v7 ready.
Automatically detects if the pool server is v6 or v7.

Monero is making a pre-ASIC Fork, Ethereum was caught with the pants down. LOL. Jajajajajaja
 making another algorithm, disappoints, "the original algorithm was Not good enough."
we're are all playing the Cat & Mouse game... 
but is "good" because it makes secret ASIC Miners useless. "No Secret ASIC Mining cheating."

There is people that do not care about centralization, only want to make a quick $$, and those people love ASIC, that's why I think, the Ethereum ETC price will increase in 2018, & the Ethereum war has begin.
People mining ETH with GPU will have to face a hard & fast decision, stay with ETH crash & burn...
Or sell GPUs buy ASIC and bet on ETC price will increase...
Or stay with GPU and move to another software, probably NiceHashMiner...
But mining with NHM is time consuming with less than 20x GPU's, same as Monero.
And NHM probably will make an update that works with the E3.
GPU makes less sense everyday.

## erkinalp | 2018-04-05T18:35:25+00:00
ETH requires work which cannot be solved by ASICs, though. It has an account-based ledger with Turing-complete operation on accounts. You can only offload signature check onto ASICs. EVM script would still need a general purpose processor.

## juanpc2018 | 2018-04-05T21:46:20+00:00
https://shop.bitmain.com/product/detail?pid=00020180403174908564M8dMJKtz06B7

## juanpc2018 | 2018-04-05T21:57:04+00:00
Maybe you don't understand what ASIC means:
https://en.wikipedia.org/wiki/Application-specific_integrated_circuit

## erkinalp | 2018-04-09T08:14:02+00:00
Ethash ASIC only works for optimising Ethash, i.e. signature verification part of ETH. Remaining parts of EVM is optimised for general-purpose 256-bit-wide stack machine. Since EVM scripting is Turing complete, one can easily defeat Ethash ASIC by including a more complex signature verification in a transaction script (by trading for necessary transaction fees, called gas in ethereum jargon). Extreme block sizes (you quickly go off-sync on a home broadband) are more a limiting factor for commons than block difficulty in Ethereum, unlike Monero, where mining difficulty prevails.

## timolson | 2018-09-24T21:42:16+00:00
> Cryptocurrencies are founded on the philosophy of decentralized use, access and processing so as to avoid the current FIAT mess created by the **centralised** funnymoney printers. Anything that works against the decentralised mentality is a threat to people power and we strongly oppose it.

A fiat mess... You mean like a central group of developers creating a new PoW in secret? IMHO Monero is secured by nothing other than GitHub logins and the decrees of core devs, who impose their will on the community and coin regardless of opposition.  Any coin which is always hard forking like Monero doesn’t need a PoW. Why don’t you just rely on signatures from a quorum of core devs instead and give up the pretense that power is distributed?  Whatever the devs say goes.  They are the new Fed.

The argument that ASIC’s become monopolized is ill-founded, IMHO.  BitMain is about to get its ass kicked by WhatsMiner, and there are several other viable competitors now.  We just needed the boom of late 2017 to make the NRE costs worth it for other companies to enter the market with strong offerings.  Yes I know about Butterfly in the old days but that was still a tiny market without legitimate, experienced competition, which we are seeing now.

And to whomever said that a few big mining companies could be forced to put a backdoor into the miners is clearly unaware of the history of Monero as ByteCoin. The CryptoNote developers put backdoors into the code and absconded with an unknown amount of XMR.  In fact, they could have been printing an unlimited amount of XMR in secret until recent patches.

And you people are worried about BitMain?  At least SHA has academic review and a long history.  Now the Monero devs propose to create another new, untested, _untestable_ PoW from scratch, with no academic review, and they are implementing it _in secret_.

+1 for a transparent, long-standing, heavily reviewed PoW which yes would be ASICable.  ASIC resistance is a pipe dream and specialized hardware is inevitable for any coin of sufficient value.


## hyc | 2018-09-25T01:01:22+00:00
@timolson nobody is developing new PoW algorithms in secret. See the lengthy discussion on https://github.com/monero-project/monero/issues/3545. Your entire comment is completely off base.

## timolson | 2018-09-25T01:43:17+00:00
Sorry for the tone, but all the repositories I looked at were 3 months old.  Where can I find the latest code?

## juanpc2018 | 2018-09-25T02:11:12+00:00
The ideal Anti-ASIC coin would be one that has a Russian Roulette type Algorithm every 1x Month...
Anyway... Bitmain has announced a 7nm ASIC, more efficient, making old ASIC miners Obsolete.
Bitmain kicking Bitmain ass. LOL Jajajajaja

https://ambcrypto.com/bitmain-to-maintain-mining-monopoly-with-new-7nm-asic-chip/
https://www.coindesk.com/bitmain-ceo-announces-new-7nm-bitcoin-mining-chip/
https://blog.bitmain.com/en/bitmain-announces-next-generation-7nm-asic-chip/




## Gingeropolous | 2018-09-25T02:19:05+00:00
@timolson , its been bouncing around a couple of PRs for a while. This is the latest

https://github.com/monero-project/monero/pull/4404

its started out as 

https://github.com/monero-project/monero/pull/4218

also, for your reference, everyone is hoping that a new PoW can be developed that is actually ASIC resistant, because it compiles and runs random code, as opposed to just doing cryptographic hashes

the most complete implementation of the idea is

https://github.com/tevador/RandomJS

which was kinda fleshed out here

https://github.com/monero-project/monero/issues/3545

and hyc had a version here

https://github.com/hyc/randprog

and it all actually started from some random dudes posting on the monero subreddit which I actually can't find right now



## timolson | 2018-09-25T03:04:29+00:00
Thanks, but I did review those other threads before commenting.  You pointed me to the CN tweaks, not the new PoW in development.  RandomJS and randprog are hopelessly outdated, thus my accusation of doing it in private.

Is there no newer code?  Nothing being developed in private?  No backdoor discussions? If there's nothing else going on, my apologies.  If there is code being developed in private, WTF?  That would give a huge advantage in miner development to anyone in a privileged position.

BTW, I'm a Monero hodler since 2014.  Great project, but I strongly object to the recent fork-by-fiat without miner consent or participation.  We can agree to disagree.  :)


## iamsmooth | 2018-09-25T07:57:58+00:00
There is no organized 'private' development effort whatsoever on this afaik. Individual volunteer contributors may choose to tinker on their own for a while but the outcome of that (which results in anything at all) will only ever be that eventually their work is shared publicly and discussed publicly.

And no there has never been any discussion of backdoor anything.

## timolson | 2018-09-25T13:18:03+00:00
I owe you all an apology for that rant.  What an asshole I am.  It was born of lingering resentment of the fork plus a particularly bad mood yesterday.

I do think hard forks by unelected devs is no better than fiat money.  If you override miners once, you'll do it again, and what kind of cryptocurrency is that?

## Gingeropolous | 2018-09-25T13:29:14+00:00
> I do think hard forks by unelected devs is no better than fiat money.

I mean, I do get part of what you are saying... but every hard fork *is* an election. The devs are maintainers, mostly, stewards of the project, etc. During the last hard fork with the first PoW tweak, multiple attempts to keep the old chain popped up. The ecosystem, including both the established pools and exchanges, decided to fork with the current set of stewards. 

Every hardfork is an opportunity for change. 

Honestly, I think no one wants the responsibility. Having been around these 4 years, I don't blame them. 

## juanpc2018 | 2018-09-26T01:36:16+00:00
most people do Not understand what coins are...
let me shine some light.
Coins follow Neo Darwinism Evolution, that joins Natural Selection + Mutation of the code.

For example: Bitcoin, someone changed the sha256 algo with Scrypt, and Boom, LiteCoin was born, the 1st mutation, and many other algorithm mutations followed, you name it.
Bitcoin Reward was too coarse and unnatural, half, trying to imitate the radioactive decay, but with a Sample & Hold version, Not gradual like real life, 
Boom, a New coin was born, Bytecoin with Cryptonight Algorithm,
more mutations happened, Monero was Born, more mutations happened, Monero v7 algorithm was born,

Mutations are Not always Evolution, sometimes are Involution...
for example:
Bitcoin-Core original Satoshi Nakamoto design, had Send with 0-Fee if Node Wallet was Mining...
but that was removed from the code, ¿why Satoshi had that? why it was removed?
 was removed because Developers do not understand Satoshi Nakamoto Vision...
they thought that CPU wallet mining was Obsolete with ASIC miners, and decided to remove completely CPU Wallet mining since 0.10
¿What was Satoshi Nakamoto Vision that Core developers do Not understand?
the idea was to Motivate the Use of Node Wallets, how? giving 0-Fee, if mining.
why? to avoid a 51% attack...
Nodes are decreasing, making a 51% attack more probable.
https://bitnodes.earn.com/

thats the problem with Ethereum ETH, has 2MB blocks every 15 seconds, Without instant Notification, making to have a Node Wallet almost impossible in the future, making a 51% attack almost inevitable.

after analyzing lots of coins, and mining, i like Bytecoin BCN, BitcoinDiamond BCD, BitcoinCash BCH, DOGEcoin & Credits CRDS, for different reasons...
Monero Cryptonight v6 algorithm was the most power efficient, and also most balanced CPU:GPU Ratio, until ASIC miners were born.
Monero has nice things, the GUI, the Daemon, Light wallets like CAKE for iOS, and Monerujo for Android, 
but... other things, Not as good.
 
for me, Non mineable coins, that are Not backed by Real Gold, Silver, Oil or something are 100% Scam.
coins that rise very fast, are very young "less than 2 years", and does Not have any technological improvement, are 99% scam.
 
Evolution of the coins/ mutation of the code is very interesting...

Bitcoin-Core code is involving since 0.10, but still very popular, # 1 because it was the 1st,
but i think it wont survive the 2nd or 3rd wave... because transfer fees are too high, waiting lines too long, has too much decimals for most humans to understand... and most nodes have Assumed Valid blocks & Pruning, making the Blockchain unstable & prone to a 51% attack.
also SegWit is like .mp3 "lossy algo", thats why i like more BCH, its like .FLAC or .WAV "lossless."

Ethereum wont survive the 2nd or 3rd wave because it does Not have instant notification...
simply absurd.
etc...etc...etc...etc... LOL. Jajajajaja

## BreakingSiam | 2018-10-11T08:00:21+00:00
> The argument that ASIC’s become monopolized is ill-founded, IMHO. BitMain is about to get its ass kicked by WhatsMiner, and there are several other viable competitors now. 

@timolson Can you expand on this statement? Why do you believe WhatsMiner, or anyone else, will be able to challenge BitMain?  BitMain has a monopoly on the TSMC 7nm tech node, which is by far the most advanced process available today. Their new equipment is being released at 43J/THash, 50% more efficient than anything anyone else is offering.

What is your basis for stating that BitMain will not continue to dominate the market? They seem to have the resources and relationships to do just that.


## timolson | 2018-10-11T15:36:09+00:00
@BreakingSiam WhatsMiner is getting 60 J/T at the 16nm process node with their first product, while the comparable S9 runs at 96.  Oof!  To my knowledge, BitMain does not have a 7nm product released yet, so you are comparing apples and oranges.  Starting out at 16 is a smart move by WhatsMiner to get off the ground first with some revenue before advancing to 7nm.

As for the claim about a “monopoly on the TSMC 7nm tech node” that is totally contrary to the fundamental business model of TSMC.  They were _founded_ on the idea that they would be a neutral silicon fabricator during an era (the 80’s) when all computer manufacturers also had wafer fabrication vertically integrated.  TSMC became who they are by breaking the vertical integration of manufacturing.  It’s true that they won’t work with just anyone, because there are lots of posers who would waste their time, but if you can prove your credentials, it is possible.  They would take my money to make a 7nm chip, and I’m nobody compared to BitMain.

Monopolies are gained and held when there is an insurmountable advantage (often called a “moat”) accrued to the market leader. We see this in operating systems for example, because Microsoft and now Apple could leverage their OS to also force their applications on people.  There is also a _very_ high barrier to entry to create an OS or entire computer, far higher than making an ASIC miner. BitMain cannot leverage its dominance the same way.  There are two extremes of markets: those that commoditize like steel, and those that monopolize like OS’s.  There is no “multiplicative effect” in ASIC miners, and it has a relatively low barrier to entry, so it will commoditize. Anyone with $20m and the right skills can make a miner. That may sound like a lot to an individual, but it is not much for a company. Startups in Silicon Valley can get that amount.  Plenty of crypto hodlers have that kind of cash.

IMO, it took the boom of late 2017 for the markets to be big enough to fund real competition.  Yes we had Butterfly et al. back in the day, but the stakes were still small and the competition quite amateur. Now we are finally seeing lots of ASIC manufacturers give it a go again, and they have real resources with real hardware teams. BitMain will only survive by making the best product.

## timolson | 2018-10-11T16:06:00+00:00
@Gingeropolous 
> every hard fork _is_ an election.

That’s an odd view of elections.  I’m a Monero hodler and was never asked to vote.  This is the kind of “election” we see in totalitarian regimes, where there is only one choice on the ballot.  At _best_ it’s similar to shareholder votes that offer:

* Approve the entire board and all their recommendations 
* Abstain


## BreakingSiam | 2018-10-11T19:20:24+00:00
> 
> 
> @BreakingSiam WhatsMiner is getting 60 J/T at the 16nm process node with their first product, while the comparable S9 runs at 96. Oof! To my knowledge, BitMain does not have a 7nm product released yet, so you are comparing apples and oranges. Starting out at 16 is a smart move by WhatsMiner to get off the ground first with some revenue before advancing to 7nm.
> 
> As for the claim about a “monopoly on the TSMC 7nm tech node” that is totally contrary to the fundamental business model of TSMC. They were _founded_ on the idea that they would be a neutral silicon fabricator during an era (the 80’s) when all computer manufacturers also had wafer fabrication vertically integrated. TSMC became who they are by breaking the vertical integration of manufacturing. It’s true that they won’t work with just anyone, because there are lots of posers who would waste their time, but if you can prove your credentials, it is possible. They would take my money to make a 7nm chip, and I’m nobody compared to BitMain.
> 

@timolson While I can definitely appreciate what you are saying, I have a sneaking suspicion you have not actually tried to produce a mining ASIC with TSMC, and I'm not sure I can accept your word that TSMC would accept your money when many very large, very well funded entities in the crypto industry are currently unable to get TSMC to work with them. Of all who have tried, Bitmain is the only one who has been successful. That is not conjecture. You will forgive me for thinking your reply sounds more like a theoretical statement, rather than an actual fact. Anecdotal evidence strongly disagrees with your contention.

In terms of comparing apples to oranges, Bitmain has already announced their new chip, and most who are looking at purchasing mining equipment are delaying their purchases right now on the basis of this announcement at WDMS in Georgia a few weeks ago. I don't know if you attended that show or not, but if you did not you may not be aware of the current feelings of many of the big mining players. 

Anyone currently producing a 60+ watt miner is going to have a very limited market going forward. So unless you can beat 43J/Thash, a manufacturer is very soon going to have a warehouse full of outdated equipment that has a negative return on investment. 50% lower operating costs is a huge barrier to overcome, and although power isn't the only consideration in mining equipment, it is the largest.

When someone actually produces a real chip that can better Bitmain, I may be more inclined to believe your contention that they are not on course to dominate the industry. At the moment however, I just don't see your claim to have any support in the real world marketplace.


## timolson | 2018-10-11T22:32:44+00:00
@BreakingSiam
We used a lower process node, not 7nm, which helps a lot.  7nm at TSMC is in high demand and has a tight production schedule, so that is much tougher to get into.  Also, most crypto people trying to produce a chip are just subcontracting the work and have neither engineering expertise nor a history of hardware production.  If you showed up to a steel factory and said "I want a car frame," but you've never built a car and have zero background in industrial engineering, what do you think they'd say?

Your contention that BitMain has a "monopoly" on TSMC is just not true.  Doesn't BitFury use them?  TSMC also makes chips for both Nvidia and AMD.  They don't play favorites, and that's a core value of their company.  I'm not surprised that plenty of people got their 7nm projects rejected, but I _know_ there are non-BitMain 7nm chips underway.

## iamsmooth | 2018-10-12T00:57:03+00:00
@timolson 
>  I’m a Monero hodler and was never asked to vote

If you are using a wallet then you have decided which fork you want to use. If you are holding pre-fork coins and have done nothing, then you own coins on both forks, and you are free to choose which if any of those to sell or hold (and in additional which fork(s) to use going forward).

That is absolutely a vote (actually several).

## tevador | 2018-10-16T09:46:15+00:00
Going back to the original topic of this issue.

I have designed a proof of work algorithm that *may* fit the description of an algorithm that minimizes barriers for creating a competitive ASIC, while having other advantages such as instant verification.

https://github.com/tevador/nppow

Personally I don't think the time is right to implement an ASIC-friendly PoW yet, but it may be ultimately the best solution.

The complexity of the algorithm is one thing to consider. NPPoW took just a few days of research and coding, while RandomJS is still months away from being usable and several weeks of development have been spent on the CNv2 tweak alone.

## timolson | 2018-10-16T17:30:54+00:00
Huge applause for @tevador producing a good-faith effort at an alternative PoW approach.  It's the right kind of idea IMO.

Positives:
* Well-studied problem, not inventing something new
* Hard to compute, easy to verify
* Not a _complex_ solver BUT:

Negatives:
* No _proven optimal_ solution.
* Sorting is _not_ simple

The fact that _any_ heuristics are known should be a concern.  Shouldn't we prefer a polynomial-time problem with known optimal solution over an NP-hard problem that may or may not have new heuristics?

Also, sorting, although well-studied in hardware, is neither simple nor widely commoditized.  Optimal sorting networks are only known up to N=17, and above that it's all proprietary heuristic algorithms.  If we rely on sorting in hardware above N=17, it's a matter of licensing the best proprietary library.  We would just be giving e.g. high-end database companies an unfair advantage.  (Sorting is an essential part of database join operations, and both large database companies and startups alike are putting lots of research and money into fast joins in hardware.)  Sorting is not simple _enough_.

## timolson | 2018-10-16T17:45:45+00:00
Proven optimal solutions for PoW problems may be hard to find.  Mathematicians look for approaches which _guarantee_ finding _all_ solutions that exist, which is not a valid premise for the PoW context.  PoW miners may use heuristics which are "good enough" to find _some_ solutions and skip nonces when convenient.  This is not generally the way mathematicians frame their basic research...

We need a well-studied problem where a simple optimal implementation is known for finding _any_ solution at all, even if many exist.

## tevador | 2018-10-16T22:27:02+00:00

@timolson Thanks for the review. I appreciate your comments.

> The fact that any heuristics are known should be a concern.

Do you know any NP-hard problems for which there are no heuristics at all? My understanding is that NPP has perhaps the poorest heuristics of all NP-hard problems. 
Anyways, most (if not all) cryptographic hash functions are not actually mathematically proven to be secure. At best, they have just resisted years of scrutiny and peer review. Even RSA is not theoretically secure because an efficient factorization algorithm could be found in the future. 

In my opinion it's the same with the NPP problem. The best heuristic algorithm has been around since 1982, which is longer than the oldest cryptographic hash functions.

> Also, sorting, although well-studied in hardware, is neither simple nor widely commoditized. Optimal sorting networks are only known up to N=17, and above that it's all proprietary heuristic algorithms.

I wasn't aware of the difficulty of hardware sorting. Anyways, I don't think that it would be a big issue because full sorting of the list is only required at the beginning of the algorithm and could be done using any good heuristics. Then, there are N-1 steps where the list is partially sorted and only one iteration of insertion sort is required, which (AFAIK) can be done in one clock cycle using N comparators. Proprietary improvements in the initial sort should not make a significant difference in efficiency.

> We need a well-studied problem where a simple optimal implementation is known for finding any solution at all, even if many exist.

It's true, but I'm not sure if such problem that is usable as PoW even exists.






## timolson | 2018-10-17T04:02:22+00:00
I'm not well-versed in the literature and don't know if a suitable problem exists.  This is really just a wish list.  But I would challenge the idea that an NP problem is required.  Even if the solution and validator are both in class P, it's ok as long as the solution polynomial is of higher order than the verification polynomial.  Again I don't really know, but it seems like plenty of P-class problems should have known-optimal solutions and plenty of those optimal solutions should be "simple."  Most search problems will have fast validation relative to solution time, and although standard hashing against a network target would fit into this category, I don't consider SHA to be simple, and it doesn't have a proven optimal implementation. But even something like finding an FNV hash under the network target... FNV is nothing but a multiply and XOR and is basically "optimal by inspection."  It's incredibly tiny and easy to implement. Even if it's your first program in C, you're probably compiling down to optimal object code for a CPU miner.  ASIC's would be easy, too.  XOR is primal, and multipliers are well-studied and everywhere.  There would be no advantage to extract from clever algorithm tricks.

Anyway, maybe such a formal problem and proof doesn't exist and that's why cryptography currently relies on factoring and discrete logs and things like that.  But PoW is _different_ from other security objectives, so maybe it's worth rethinking.


## SChernykh | 2018-10-17T05:46:23+00:00
@tevador Using NP-hard problem as PoW is a bad idea. There is no proven lower complexity bound for NP-hard problems, and a breakthrough can happen any time. It's better to search for problems that have known lower bounds like O(N^2) or O(N^3) and use them.

## tevador | 2018-10-17T10:23:45+00:00
@timolson Interesting idea with FNV. Is the hash non-reversible, though?

## timolson | 2018-10-17T17:05:57+00:00
@tevador I’m not a cryptographer but would doubt that FNV is secure enough. Almost certainly not. I was just brainstorming, and it’s probably not a good idea. But take it as inspiration?

There are some lightweight ARX hashes that may be suitable... no multipliers only add, rotate and xor. But can we do better than a hash function that has no proof behind it, only “lack of attacks?”

Maybe someone knows of a search problem with a proven solver that’s simple to implement?

## tevador | 2018-10-17T20:33:10+00:00
> But can we do better than a hash function that has no proof behind it, only “lack of attacks?”

The main problem is that the algorithm must have either an unpredictably random output (to use the standard difficulty algorithm comparing to a threshold) or adjustable complexity / solve time. Otherwise it's not really usable as a PoW by itself even if it fulfills all the conditions you mentioned earlier (simplicity, proven optimal solution, fast verification).

So for the time being we are stuck using cryptographic hashes for the final PoW value and the only way to make the miner simpler than the hash algorithm is to combine it with a simpler problem that is much harder to solve, so the hash calculation time is negligible. However, to keep the verification time low, you need an asymmetric algorithm. This was the rationale behind NPPoW and for example Cuckoo cycle also fits this description.

## stoffu | 2018-10-18T13:29:51+00:00
@tevador 
Just a minor question, I didn't understand your above comment:

> So for the time being we are stuck using cryptographic hashes for the final PoW value and the only way to make the miner simpler than the hash algorithm is to combine it with a simpler problem that is much harder to solve, so the hash calculation time is negligible. 

which seems to correspond to the following description in NPPoW's README:

> The encoded solution is then appended to the block header and the whole header is hashed once again, this time using the SHA3-256 hash function to determine the final PoW.

I don't see the point of this "final PoW" because the work is not targeted at producing small hash values. Doesn't it suffice to include only the nonce and its corresponding solution in the block?


## tevador | 2018-10-18T18:48:51+00:00
> Doesn't it suffice to include only the nonce and its corresponding solution in the block?

The PoW hash is not included in the block. It's calculated to check if the block meets the required difficulty. The NPP solution is not a hash and cannot be used as one. In order to keep the difficulty targeting mechanism, a random 256-bit value must be produced at the end.

Another option would be to set the difficulty by adjusting B (the number of bits), but this has low granularity (difficulty could be adjusted only in approximately powers of two), so it could skew the block emission frequency. Also pooled mining would be very difficult if not impossible (how do you define a partial solution?).

## timolson | 2018-10-18T20:14:14+00:00
If we’re worried about mining centralization, why aren’t pools demonized as much as ASIC manufacturers? Almost all of them are Stratum based, not getblocktemplate, and Stratum pools can forge malicious blocks without the pool users knowing or approving. 

IMHO few people really care about decentralization or they would force pools to use getblocktemplate instead of Stratum. Let’s be honest: most people just want to make “easy” money at home and they tout “decentralization” as a moral excuse. Getblocktemplate puts more work on the client which means less money, and clearly home miners have chosen money over “decentralization.”

Anyone crying about “decentralization” while pointing their home rig to a Stratum pool should STFU and just admit it’s greed that drives them, not some abstract democratization principle.

So really, why should we be worried about whether a PoW is useable in a pool?  Shouldn't we design one that's NOT useable by pools?

## juanpc2018 | 2018-10-19T02:19:17+00:00
the original protocol was getwork, but was replaced...
the replacement was a developer war,
it was getblocktemplate "GBT" vs stratum developers, stratum "won" because it was pushed/supported by largest Bitcoin pool...

...many years later:
doing BitcoinDiamond mining, using a modified ccminer from vvpool, that has both GBT and stratum,
also i use a proxy, that can accept getwork, gbt, and stratum, and convert to stratum to communicate with the pool in stratum or gbt.
when using the ccminer as gbt vs. stratum there are very interesting differences, specially with verbose active on the miner, very interesting,.. 

BUT...
after lots of mining, my conclusion was:
 is better for small miners to get into a pool that has more than 51% of the total miners.
is better for small miners, if the pool has more than 95% of the total miners in 1 pool.

what avoids a 51% attack is Not the pool, is the Node wallets,
what decides the future of the coin, is the Node wallets,

if 99% of the miners are in 1 pool, and all miners have light wallets = just 1 Node Wallet,
if that 1% left has 10k people, each with a Real Node wallet, a Fork or a 51% attack is impossible, if the 1% does Not agree/download the New version. 
all miners in 1 pool is bad for other pools, and coin centralization... more on that,

Mining Decentralization is Bad for small miners,
What people that understand coins mean by Decentralization, has a completely different meaning.

where do i start?
the laws of the world...
1-old example:
the alexandria library,
had all the knowledge of the world, at that time, and got burned, oil lamp, burning arrow, does Not matter, all knowledge was lost...
why? because it was Centralized,
"Don`t put all eggs in one basket." 

to copy books was slow, by hand, a lifetime work,
when technology advanced enough, printers appear, and to copy books was easy, faster...
information Decentralized...

when technology has advanced enough, Decentralization happens Naturally,
Now there is a library everywhere... with similar knowledge.
when technology is Not advanced enough, Centralization occurs Naturally.

for example the Earth, technology is Not advanced enough, Humans are Centralized in 1 planet.
if a Meteorite is big enough and hits the earth, kills all humans. 
see Salvation TV series on NetFlix, https://www.imdb.com/title/tt6170874/

Decentralization allows survival.

Economy, is Not advanced enough, is Centralized by Banks, by government,
but Technology has advanced enough, and is getting slowly but Naturally Decentralized, 
if happens another economic crisis like 2008, or an EMP attack, world will choose a Decentralized economy/technology, that can survive,
is just Natural Selection,
each time a New economic crisis Big enough happens again, world economy will become Decentralized, because technology has advanced enough,.

but there are other Centralized vs. Decentralized problems, "layers" inside the Decentralized Economy,
like Miners, Pools, Wallets, Developers, etc...

a proper Decentralized algorithm will give equal opportunity to CPU, GPU & ASIC, or FPGA and other pools, 
"in the future everyone will have 15-minutes of fame" -Andy Warhol,
to avoid pool/coin centralization, the algorithm must rotate all miners to a different pool every 15-minutes or 15-days, depends on the pools/nodes available.
Each Node wallet is a Pool automatically, Pool code is included in each Node Wallet, Motivating the use of Node Wallets, "avoiding a 51% attack" and also avoiding coin centralization by only 1-pool with 99% of the miners.

Bitcoin is ASIC centralized,
Ethereum was GPU centralized,
GPU Only coins made GPU prices to increase = BAD for Small Miners. 
if there is No small miners, Coins become Centralized, and Market Dumping happens, more on that.
the problem with ASIC or GPU Centralized miners/coins, are several,
for example:
 if Bitcoin Price gets High enough, & ALSO very popular, or Traditional Economy becomes too weak, ASIC developers will see that Not selling miners becomes more profitable...
 
if price is high, but popularity is Not enough, they could develop a secret faster Miner, and use it, Not sell it.
they can Not sell replacement parts, eliminating the competition..
taking over the world.
Centralizing the Network,
if a Small Meteorite or an EMP hits the Only ASIC FARM/Factory in the world, the SHA256 coin will disappear = World Economy Chaos.

The goal of Decentralized Economy is to allow Survival of the Economy, 

anything that goes against Decentralization is wrong...
but when all miners are Centralized, "looks wrong" but gains are Decentralized more easy,
i wish i could explain more easy, why something that looks centralized is actually Decentralized...

anyway...
World economic crisis will happen again, is a matter of time, don`t know when, 
the problems that caused the 2008, were Not solved, just the symptoms were solved.
 when happens again, e-coins will rise when there is a New economic crisis again, but Not all e-coins...
coins that do Not have instant Notification wont survive the 2nd or 3rd wave, small daily transactions, becomes impossible without instant Notification, for example.

e-coins price is "down" now, because 3 reasons, traditional economy is strong now, and most e-coins were centralized by few miners & pools, most had 10k coins, those people are dumping the coins in the traditional economy, lowering the price more...

Bitcoin was Not mass adopted by small daily economy, because 21Million coins are Not enough, making too much decimals, and transaction fees too high, also waiting lines too long but thats another story... solving 1 problem with another, few coins, high fees, long waiting lines with assumed valid blocks, pruning & segwit.
coins that have less than 100million coins, wont survive the 3rd or 4th wave, 
because most humans do Not understand 0.0015 btc + fee = Burger + Fries. LOL. Jajajajaja
economy / technology must be easy to understand, to be mass adopted.

each wave ripple, ecoins will become less & less centralized...

https://mining.bitcoin.cz/media/download/mining_proxy.exe
https://github.com/slush0/stratum-mining-proxy
https://en.bitcoin.it/wiki/Getblocktemplate
https://en.bitcoin.it/wiki/Stratum_mining_protocol
https://en.bitcoin.it/wiki/Getwork
https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list
https://en.bitcoin.it/wiki/Getwork_support

## stoffu | 2018-10-19T05:12:59+00:00
@tevador 

> The NPP solution is not a hash and cannot be used as one. In order to keep the difficulty targeting mechanism, a random 256-bit value must be produced at the end.

Oh, I thought the idea was to adjust the difficulty of NPP according to the network's compute power and replace the current hash-based PoW with it. In other words, is your idea to change the current scheme:

- pick nonce -> compute hash -> accept if below threshold

to something like this?

- pick nonce -> solve NPP -> compute hash -> accept if below threshold

So, the difficulty adjustment will apply to these two places (NPP and hashing)? How should it be done? I'm new to this idea. Or perhaps, the difficulty of NPP is fixed?

> Another option would be to set the difficulty by adjusting B 

How about fixing B and adjusting N? AIUI, decreasing N seems to make the problem harder progressively.

> Also pooled mining would be very difficult if not impossible (how do you define a partial solution?).

I see this as well, which is also true with Cuckoo Cycle ([a relevant post on Monero StackExchange](https://monero.stackexchange.com/a/1803/1279)).


## stoffu | 2018-10-19T05:34:01+00:00
@timolson 

I think you misunderstand how pool mining works.

> IMHO few people really care about decentralization or they would force pools to use getblocktemplate instead of Stratum. 

Pool miners calling getblocktemplate doesn't make sense at all; this PRC is called by the pool operator against the operator's node with the operator's wallet address as the (only one) argument. Each time a new block is found, the operator receives the block reward in full, and pays out to the contributing miners later. If a pool miner were to call getblocktemplate with his own wallet address as the argument, he is effectively solo mining. Pool mining works by having many miners work on the same block template.

> Let’s be honest: most people just want to make “easy” money at home and they tout “decentralization” as a moral excuse. 

> Anyone crying about “decentralization” while pointing their home rig to a Stratum pool should STFU and just admit it’s greed that drives them, not some abstract democratization principle.

The basic assumption in any cryptocurrencies is that all participants are greedy and will cheat/attack the system if they can. The whole point of our effort is to eliminate the possibility of cheating and make the adherence to the same strategy optimal for everybody w.r.t. financial gain. We seek for decentralization because it's fundamentally valuable, not because it's moral.

IMO, pool mining by itself is not a problem as long as miners are reasonably spread out, which is quite a different kind of question.


## timolson | 2018-10-19T06:54:54+00:00
@stoffu 
Oh really _I_ don't understand?  `getblocktemplate` was _designed_ to allow clients to choose their own transactions so that they wouldn't have to trust the pool operator's choice.  Don't say _I_ misunderstand.
Miners using `getblocktemplate` is the _only_ way GBT makes sense.  It's the whole _purpose_ for GBT.  Otherwise just use Stratum and let the pool operator have control of the TX selection.
In GBT, the pool still creates the coinbase but allows clients to choose the TX's so the _clients_ can choose which transactions they think are valid.  The pool still gets the coinbase.
Here's a refresher since _you_ clearly don't understand
https://en.bitcoin.it/wiki/Getblocktemplate

## timolson | 2018-10-19T07:09:08+00:00
So it's probably different in Monero.  I'll humbly admit very little knowledge of what a Monero block looks like.  But GBT vs Stratum for the majority of coins, you are way off base.

## timolson | 2018-10-19T07:27:31+00:00
Maybe this is our misunderstanding: you're talking about the pool operator calling GBT on the daemon, building the block, then using Stratum to broadcast to miners.  This is a bastardization of what GBT is about.  I'm talking about the _original_ purpose of GBT where it was meant to be a pool protocol for mining clients so that pool operators wouldn't be able to effect a 51% attack containing malicious transactions.

## stoffu | 2018-10-19T08:15:25+00:00
@timolson

Oh yes, I was assuming you were talking about the Monero daemon RPC of the exact same name. I was unaware of this GBT protocol in Bitcoin which seems to have never been implemented in Monero AFAIK. Indeed, this type of pool can be helpful for decentralization.

> I'll humbly admit very little knowledge of what a Monero block looks like.

I'm also largely ignorant about how exactly Bitcoin blocks look like, but apart from the vast differences in the individual transactions' format, the basic structure of blocks should be mostly the same between Bitcoin and Monero in my understanding (merkle root, prev block id, difficulty, timestamp, nonce, etc).


## LordMajestros | 2018-10-19T08:36:38+00:00
> If we’re worried about mining centralization, why aren’t pools demonized as much as ASIC manufacturers? Almost all of them are Stratum based, not getblocktemplate, and Stratum pools can forge malicious blocks without the pool users knowing or approving.
> 
> IMHO few people really care about decentralization or they would force pools to use getblocktemplate instead of Stratum. Let’s be honest: most people just want to make “easy” money at home and they tout “decentralization” as a moral excuse. Getblocktemplate puts more work on the client which means less money, and clearly home miners have chosen money over “decentralization.”
> 
> Anyone crying about “decentralization” while pointing their home rig to a Stratum pool should STFU and just admit it’s greed that drives them, not some abstract democratization principle.
> 
> So really, why should we be worried about whether a PoW is useable in a pool? Shouldn't we design one that's NOT useable by pools?

NERVA, Blur and Turtle coin are 3 projects that are experimenting with mining without pools.
The first two are indirect monero clones through masari. The last one is a crypto note clone.
I'm paying attention to them because I'm very interested in seeing how this plays out. 
I think pools help to prevent a different kind of centralisation, centralisation of the supply. I think if people solo mine for long stretches of time without rewards they are likely to quit mining altogether. I'm watching to see this proven or disproven. 
I'd also like to point out that due to ring signatures in crypto note coins it might be difficult or perhaps impossible for pool operators to censor transactions based on anything other than fees. I might be wrong.

## FromMeanas | 2018-10-19T09:50:44+00:00
> If we’re worried about mining centralization, why aren’t pools demonized as much as ASIC manufacturers? Almost all of them are Stratum based, not getblocktemplate, and Stratum pools can forge malicious blocks without the pool users knowing or approving.
> 
> IMHO few people really care about decentralization or they would force pools to use getblocktemplate instead of Stratum. Let’s be honest: most people just want to make “easy” money at home and they tout “decentralization” as a moral excuse. Getblocktemplate puts more work on the client which means less money, and clearly home miners have chosen money over “decentralization.”
> 
> Anyone crying about “decentralization” while pointing their home rig to a Stratum pool should STFU and just admit it’s greed that drives them, not some abstract democratization principle.
> 
> So really, why should we be worried about whether a PoW is useable in a pool? Shouldn't we design one that's NOT useable by pools?

What is your point exactly Tim?
Everyone is greedy so let the _itmains and asic desgners like you dominate the hashrate, the coin supply, in fact dominate everything?

## LordMajestros | 2018-10-19T11:54:49+00:00
@timolson I'd love to hear your thoughts on this https://medium.com/@turtlecoin/introducing-cryptonight-soft-shell-2c2d4c497efd
I think ASICs can be built for this.

## tevador | 2018-10-19T13:00:03+00:00
@stoffu 
> pick nonce -> solve NPP -> compute hash -> accept if below threshold

Yes, that was the original idea. The difficulty of NPP would stay fixed with B = 42 and N = 128 and just the hash threshold would change.

Cuckoo cycle actually uses the same mechanism (with a SHA-256 hash of the cycle solution).

> How about fixing B and adjusting N? AIUI, decreasing N seems to make the problem harder progressively.

Adjusting N would also work, but the dependence of NPP difficulty on N is more complex (for example N also affects the value of the critical ratio and size of the search space). 

For a fixed value of N, the difficulty would be simply proportional to 2<sup>B</sup>. The only problem is that with a high enough B, 64-bit integers are no longer enough and CPU performance would drop sharply.

Third option would be to adjust both N and B to set the required difficulty.

@timolson 
> So really, why should we be worried about whether a PoW is useable in a pool? Shouldn't we design one that's NOT useable by pools?

Someone could argue that pools help decentralization (up to some point), because most small miners wouldn't consider solo mining viable. Without small/hobby miners, it would be just big GPU farms who would mine.

The fact that existing Monero pools are stratum pools is a different point.

## timolson | 2018-10-19T16:52:14+00:00
@FromMeanas
I was challenging the idea we should prioritize a pool friendly PoW. Compared to other coins, Monero has a pretty good distribution of hashrate across pools right now, yet if only 2 of the bigger ones colluded, they have more than 50% easy. 
There seems such hatred toward ASIC makers, saying Bitmain is a monopoly (they aren’t) but if people really cared about decentralization and not just their wallets, they would complain about pool power. They don’t. But they should.

There are ways to prevent pools from being malicious even if they have >50% hashrate (getblocktemplate) so as long as we’re talking about PoW and ASIC’s, I thought a quip about pools and pool support was germane.

@LordMajestros
Interesting about the non-pool coins. I’ll bet home miners don’t do it. They want immediate rewards not decentralization.

This doesn’t mean I’m against distributing mining power and coins. Maybe pools are a necessary evil just like ASICs.

## BreakingSiam | 2018-10-19T17:30:12+00:00
@timolson
You know some of what I do, so you should understand when I say that I agree with most of your position, but I think you are over generalizing here. Yes, part of it, possibly a very large part, is due to greed, but if that was all it was, then people would simply have bought the miners from Bitmain and continued to make money. After all, they bought the nVidia cards. What's the difference?  I have studied this problem in detail.

Bitmain really did bring this problem on themselves, and it isn't fair to disparage those who are reacting to it by calling them greedy. Sadly, I am going to have to stereotype here, but there is no way around it. I've lived in Asia for more than 20 years, and Chinese companies just don't see the world in the same way as we do in the West. In their eyes, things like insider trading, giving mining equipment preferentially to their friends, etc. is not necessarily wrong. That is not to attack the Chinese. Westerners have customs that are equally bizarre. But I will point out that Bitmain has never been fair in the Western sense of the word when selling devices, and people are now naturally suspicious of every mining equipment manufacturer due to this. 

The same is not true of pools. When a new pool starts mining, it is quite clear. When a much more efficient ASIC unit comes on line however, it can be disguised such that it can only be seen in hindsight as the difficulty level slowly creeps up.  And those who have early access to the miners are very adept at keeping it under the radar for a while.

Until your new vision of a Utopia comes true, where there is a large group of competitive mining manufacturers that are all competing fairly during the day and singing Kumbaya together at night, you need to be a bit more open minded about the feelings of the community.  This isn't solely greed. The emotion of fear plays a very large role here as well.


## iamsmooth | 2018-10-19T19:59:37+00:00
@timolson People have definitely expressed concerns about pool centralization but it is hard to solve. GBT was not a solution because its usage isn't enforced and neither an individual pool nor an individual pool miner has any incentive to use it. Their individual optimization is to stick with stratum. For a pool decentralization solution to work it needs to be enforced (or at least properly incentivized) at the consensus level and also avoid or address various work-arounds and cheats/semi-cheats that people have come up with or will come up with. It's not easy, but a good solution that avoided too many negative unintended consequences would indeed be valuable.

## timolson | 2018-10-20T19:05:01+00:00
@LordMajestros 
Soft Shell not convincing
https://medium.com/@timolsoncrypto/turtlecoin-cryptonight-soft-shell-is-nonsense-8e5c3ca5f572
I apologize to the Soft Shell authors for my previous tone. Article is cleaned up.

## dEBRUYNE-1 | 2019-03-14T10:57:59+00:00
A relevant discussion currently occurring here:

https://github.com/monero-project/meta/issues/316

## Cactii1 | 2022-07-20T20:13:44+00:00
This seems to have been decided against when Monero was upgraded to RandomX.

Propose to close.

## SamsungGalaxyPlayer | 2022-07-20T20:18:48+00:00
Agree, it can be referenced in a new issue if we need to have this discussion again.

## erkinalp | 2022-07-21T10:30:42+00:00
@selsta Wrong type of closure: The correct one is closed as *not planned*.

## juanpc2018 | 2022-07-21T15:19:28+00:00
ASIC Friendly Monero = Old algorithm = XMC
https://coinmarketcap.com/currencies/monero-classic/
http://explorer.monero-classic.org/
https://nitter.fdn.fr/xmccurrency/status/1244549359414308864#m
https://bitcointalk.org/index.php?topic=3256439
https://github.com/monero-classic
https://t.me/xmccurrency

XMC for Android works ok, its a forked light weight Monerujo wallet.
for Linux, has many compile errors, Needs K/Ubuntu 17, because a special library.so6 that is Not available anywhere else, 
but K/Ubuntu 17 had many problems because Wailand, and was Abandoned, "Hard to Find",
Needs a lot of work to build make & compile in Newer 20.04 LTS,
and a lot more in 20.10, 
and incredible more in 21.10

has too many deprecated functions.
also needs a very fast CPU, compile takes too long.
Case [CLOSED]
End of Story.


# Action History
- Created by: iamsmooth | 2018-03-12T09:34:03+00:00
- Closed at: 2022-07-20T20:19:15+00:00
