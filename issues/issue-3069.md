---
title: 'Algorithmify ringsize '
source_url: https://github.com/monero-project/monero/issues/3069
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-01-05T05:37:47+00:00'
updated_at: '2018-09-21T21:56:50+00:00'
type: issue
status: closed
closed_at: '2018-09-21T21:56:50+00:00'
---

# Original Description
This is a spinoff of #3035 , a proposal to increase ringsize and possibly remove the option of using variable ringsizes. 

I feel that if we fix the ringsize as proposed by multiple people, ringsize will become our blocksize debate, and should therefore be algorithmified. 

In an ideal situation, a transaction would be made with a ringsize of the entire chain. 

In the real world, we are discussing moving from a ringsize of 5 to a ringsize greater than 8 but less than 16. From my understanding of things, we are not going to use a ringsize of the entire chain due to the cost of validation and size. This is logical. 

However, computers will get faster. In another year or two, we may once again have this debate of "well, now it only takes 40 usec to verify a transaction of ringsize 16 on a raspberry pi Cream Filling edition, so we should increase it to 32"

What if, instead, the protocol assesses the state of computational power of the network and adjusts the ringsize accordingly?

Yes yes, I once again am proposing to use the network difficulty as a source of information about the real world. 

Granted, I don't know *which* combination of variables it would be based on (I imagine a combination of blocksize and difficulty - difficulty would act as a more or less raw measure of computational power of the meatworld, but blocksize would possibly act as a denominator, because -using the assumption that increased chain activity == higher value (as used in the transaction fee adjustment) - the more valuable the monero network is, the more people are mining on it. So possibly something as "simple" as the difficulty / blocksize plotted over time, and then you evaluate the slope, and certain slope characteristics would trigger certain behavior)...

but the protocol could create a yearly adjustment that adds 0 or a positive number to the current ringsize (or we can think about allowing it to decrease, say if world war 3 knocks out 90% of the worlds computers and the network is struggling to run on smart toasters). Basically, the protocol can analyze the last years worth of block data and assess that conditions favor an increase in the ringsize, the current ringsize matches the system as assessed by the analysis, or that a decrease in ringsize is needed. 

# Discussion History
## b-g-goodell | 2018-01-11T13:37:52+00:00
There is no perfect answer, afaict, because we haven't assessed the complexity for determining a "true path" of signers in a tree of ring signatures/implications, but I'm not sure if that's necessary or possible. 

I suspect that exposing a path of transactions on the Monero blockchain is a problem with at least exponential complexity (2^2^k), in the absence of an EABE attack. We don't want the ring sizes to change over time with, say, difficulty, because then someone will be better able to use ring sizes and dynamic fees to pinpoint the IRL time of the transaction, although having a slow ring size updating each month or two-week period or something like that (slower than difficulty adjustments) I think would also be acceptable (maybe set a different fixed ring size for each HF for a few years or something like that).

_Below, I'm going to justify selecting a fixed ring size between base_ring_size = 5 and base_ring_size = 200, and either just leaving it alone forever or changing it occasionally._

**Assumptions:** Assume the probability of success of the attacker decays exponentially to zero with parameter L > 0  as ring size increases (I'm being super vague about how the attack is going down on purpose here, we will use L * exp(-x/L) as the density function), and assume the "cost" (again, vague and abstract) of securing the network by boosting ring size grows linearly with ring size, say mx+b. Hence the average "cost" blown/wasted by the network in the case that a ring size x will be L * exp(-x/L) * (mx+b). The units here: L has units "number of ring members", m has units "1/(number of ring members)", and b has units "cost points" (which I left abstract). We can assume m != 0 (this corresponds to: cost of finding true signer is constant regardless of ring size) and L != 0 by assumption. We can probably assume b = 0 (zero cost to determine the true signer of a regular signature, the pubkey comes along). 

**Minimizing:** Then to minimize the attacker's success P = L * exp(-x/L) subject to the constraint that we still keep costs C = mx+b = mx reasonable we merely must minimize the function P*C. This point occurs when L * (-1/L) * exp(-x/L) * mx + L * exp(-x/L) * m = 0. The factor L * exp(-x/L) appears in both terms, so it cancel out (assuming L!=0) and we end up with (-1/L) * mx + m = 0 or x = L.

Note that this kicks the can down the road: we answer the question "how do we minimize the average cost blown by the network in the event of a successful attack" with an answer "estimate the inherent rate of decay of the probability of success and use that." Unfortunately, estimating this ring size decay rate requires a rigorous definition of the various sorts of attack to reveal the true signer, and estimating the complexity of doing so, etc etc. 

So, we have reduced the problem to a specific answer, but in order to find an actual numerical result, we need to do a lot more work. But we have reduced the problem and we can ask some questions. Such as: what if L = ln(k) for some security parameter k? This gives us an indication of how small ring sizes *could* be to optimize this process: if k = 10^3, ln(k) = 6.9-ish, so a ring size of 7 "should" be optimal in this scenario. Even if k = 10^80 (about the number of particles in the known universe) we would end up with a ring size around 185, and something like k=2^256 has a ring size of 177.

That is to say: if costs are linear and ring sizes can be chosen to be logarithmic in a security parameter and if probability of attack success is exponentially decaying as the ring size gets larger, the range of ring sizes from 5 to 200 all seem reasonable to me. Without more information, more rigorous models, more justification for each of these choices... this is the best we can go for, I think. If we get crazy? Say we want k = biggest prime yet discovered, which is approximately 2^( 7 * 10^6)? With logarithmic ring sizes, we still need a ring size of 700,000. With RTRS ring signatures, this signature would be only 4.5 times as large as a ring signature with 20 signers. Really not bad at all, although verification time would be more than prohibitive.

**Caveats/etc:**

- I chose logarithmic ring sizes purposely to demonstrate a point. We probably want to select ring size sublinearly in a security parameter: logarithmic ring sizes are *of course* only going to present small numbers from 5 to 200, because a^200 is a huge freaking number for any a > 2. But another choice is like Sqrt(k). In this case, for something absurd like k=10^80 will, unfortunately, also produce an absurd ring size (10^40), which, even with RTRS signatures, is pretty cumbersome in size (not to mention verification time!)

- Not only have I selected logarithmic ring sizes rather arbitrarily, I also have not justified any particular choice of security parameter k. I have merely explored a space of possibilities between roughly 10^3 and 10^80. This may seem convincing, but keep in mind: since we don't have a good model for how the attack unrolls, maybe we should look at even larger numbers like 10^(10^(10^80))).

-  I suspect that probability of success to track a *path* of transactions through the implication tree is doubly exponential, exp(-L * exp(S * x)) but parallelizable. If this is true, then even moderate ring sizes of 5-10 is probably sufficient to balance security and cost.

**Conclusions:** For these reasons, I would support a fixed ring size of something like 8 or 16 for now, and if we have RTRS ring signatures, we can double it a few times every few hard forks... or every few decades... and we will have sufficiently protected our users from casual blockchain analysis. This may not be sufficient to stop large-scale state actors, especially in light of the EABE attack, but 16 year old hackers living with their parents in Cape Town some place will be very unlikely to be capable of exposing the blockchain using a nonogram-style attack. Fee structures probably also need to be changed in order to accommodate fixed ring sizes. Choosing a minimum ring size of 8 or 16 or 32 will "probably" be sufficient for several years, and anything between 5 and 200 can cover a very large region of the security parameter space. 

**Homework problem:** Whether we use RTRS ringCT or MLSAG ringCT for ring sizes in this range is completely different question, which might needs its own issue: RTRS RingCT roughly has twice the verification time for a similarly sized MLSAG ringCT, but takes up a logarithmic amount of space. For which ring sizes between 5 and 200 is it worthwhile to use RTRS RingCT instead of MLSAG?

## b-g-goodell | 2018-01-11T13:53:47+00:00
For the record, I am uncomfortable suggesting any particular number between 5 and 200, and I am uncomfortable recommending a short-term dynamic ring size change: essentially, I think ring sizes should be constant/fixed/enforced for several months at a time. However, I am comfortable with between 5-ish and and 200, and I am comfortable with a dynamic ring size change as long as it happens sufficiently slowly. Ring size is very different from difficulty: when difficulty drops, the network can be swamped with a botnet switching over to mine Monero because it's suddenly profitable/easer, but the same can't be said about difficulty. In the previous sentence, if we switch "difficulty" with "ring size" and "mining" with "de-anonymizing," you'll see what I mean.

## iamsmooth | 2018-01-11T14:10:39+00:00
> Fee structures probably also need to be changed in order to accommodate fixed ring sizes.

I don't understand why. Setting aside the non-linear size/verification tradeoff of for example RTRS ringCT (which raises other concerns), why would fee structure need to change? Fees are mostly a function of size and transactions still have a well-defined size with or without fixed ring sizes.




## b-g-goodell | 2018-01-11T14:28:02+00:00
@iamsmooth : I honestly don't remember what scenario I had in mind when I wrote that...what you say is reasonable.

## Gingeropolous | 2018-01-12T19:52:42+00:00
@b-g-goodell 

> We don't want the ring sizes to change over time with, say, difficulty, because then someone will be better able to use ring sizes and dynamic fees to pinpoint the IRL time of the transaction, although having a slow ring size updating each month or two-week period or something like that (slower than difficulty adjustments) I think would also be acceptable 

Agreed. The idea was to use difficulty as a proxy for the computational ability of the world,  and automagically adjust the required ringsize policy for a given year.

> (maybe set a different fixed ring size for each HF for a few years or something like that).

The point was to remove the human hand. When thinking about these things, I always imagine our next hardfork is our last one, or at least that our hardforking abilities have a relatively small viable window, compared to the hopefully long lifespan of the monero chain.



## stoffu | 2018-01-13T02:49:56+00:00
@Gingeropolous 

> The idea was to use difficulty as a proxy for the computational ability of the world, and automagically adjust the required ringsize policy for a given year.

I don't really get it - the difficulty represents the sum of all the computational power in the network, while the ringsize affects the computational load on every participant in the network. For example, if the number of participants (with the same computational power) grows 10x, the difficulty also grows 10x, but each user's computational power remains the same. If the uniform ringsize is raised according to this 10x difficulty growth, users will just suffer from increased verification cost.

## Gingeropolous | 2018-01-14T06:29:11+00:00
@stoffu , indeed. I agree that its not a straightforward proxy, and I've been kicking around some ideas  to get at this concept that also might apply here, but I need to find a way to simulate or harvest some information from existing data.

That is, the ratio of difficulty to blocksize. The monero protocol, as of now, treats the blocksize as a measure of real world usage - more transactions means that monero has a greater value to the outside world, so the transaction fee *decreases* to accommodate this increased cost in outside world value to use the monero network. 

So real world usage (blocksize) is obviously a muddy metric, but part of that metric is the number of participants. 

Thus, if we observe a relatively static blocksize over time, but the difficulty increases over this same amount of time, what does this tell us about the outside world?

Either, 

A) The outside world value has increased such that mining the currency is advantageous, independent of actual blockchain usage. This is essentially what we are seeing now. We can barely get the blocksize to budge from 300 kb, but our difficulty is skyrocketing because of price speculation. 

B) The outside world has become much more efficient at hashing cryptonite, and by extension, possibly more efficient at computations *in general*

I would argue that the nature of this ratio - as possibly observed using a linear regression of this ratio over time - will be drastically different for the above two scenarios. Scenario B will be much more gradual and constant, whereas scenario A will have a lot of spikes. And of course, its very possible that *both* are occuring, and then it becomes a matter of deconvoluting the two signals. 

So how would your proposed scenario affect this ratio ...

With 10x participants, the blocksize would grow *to some extent*. What happens to the difficulty?

Now, suppose none of these new participants engage in mining. The blocksize will grow, but the difficulty should stay the same. The only reason the difficulty would increase is if the existing participants became more efficient or generally more powerful - this indicates that the computational abilities of the real world are better than before. 

Suppose all of these participants engage in mining. The blocksize will increase and the difficulty will increase. The ratio will be much different than above. 

Damn... i lost the train. 

## afighttilldeath | 2018-01-14T20:22:44+00:00
Instead of using the network difficulty as a way of adjusting ring sizes, could you use the bottom 1% of miners in the network in terms of hash rate? Seems to me that if their hash rate goes up, it's likely computers in general will be faster as the bottom 1% are likely older computers.

## Gingeropolous | 2018-01-15T00:18:51+00:00
@afighttilldeath , there's no way of getting those data. The only trustable data are in the blocks. 

## afighttilldeath | 2018-01-15T08:36:02+00:00
@gingeropolous , gotcha, thanks for that info.

## b-g-goodell | 2018-01-18T13:18:07+00:00
@Gingeropolous that's a good observation about the ratio of blocksize to difficulty. It reduces two-dimensional questions about 1) the economic activity being secured (using block size as a proxy) and 2) computational power securing the network down to a single dimension.

If this ratio is large, blocksize/diff is big... relative security of the network with respect to economic activity has decreased, or the economic activity has increased with respect to current security levels... if this ratio is small, vice versa, so... relative security of the network with respect to economic activity has increased, or the economic activity has dropped with respect to current security levels...  Security here meaning "resistance to a 50% attack."

Unfortunately, without information about total network size (in terms of number of CPUs), this is insufficient to make determinations about ring sizes killing egalitarian mining. Maybe this merely means that fees should change with respect to this ratio, but not so fast that it incentivizes miners stuffing blocks with spam. Either way, it provides me a new predictor variable in my fee regressions. :P



## Gingeropolous | 2018-01-18T19:15:41+00:00
> ring sizes killing egalitarian mining.

you mean ring sizes killing egalitarian access to the network? I.e., if ringsize is algorithmically increased massively, slower machines won't be able to verify & sync.

> without information about total network size 

I do ponder whether blocksize can be used as a very crude indicator of this as well. 


## moneromooo-monero | 2018-09-21T21:44:43+00:00
Ring size is now algorithmically selected (except for those cases when pending pre-rct outputs with few/none other amounts on the blockchain).

+resolved

## SamsungGalaxyPlayer | 2018-09-21T21:52:32+00:00
@moneromooo-monero I strongly recommend keeping this open for now. Even if Monero technically meets your definition of using an algorithm set to 11, I do not believe it covers @Gingeropolous's intent behind this issue.

The idea is that the ringsize could adapt to certain parameters.

# Action History
- Created by: Gingeropolous | 2018-01-05T05:37:47+00:00
- Closed at: 2018-09-21T21:56:50+00:00
