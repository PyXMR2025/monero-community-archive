---
title: '[Discussion] Raising the mandatory ringsize in the v6 hardfork, September
  2017'
source_url: https://github.com/monero-project/monero/issues/1673
author: olarks
assignees: []
labels: []
created_at: '2017-02-04T14:51:01+00:00'
updated_at: '2018-08-23T02:23:57+00:00'
type: issue
status: closed
closed_at: '2018-08-23T02:23:57+00:00'
---

# Original Description
**TL;DR** There is an edit at the bottom of this post highlighting what is going on because a lot has changed over many discussions, and better alternatives are being explored.

You may want to grab a drink for this one...

As we all know there will be a hardfork in September 2017 that will raise the mandatory ringsize to 4
based on the recommendations of [MRL-4](https://lab.getmonero.org/pubs/MRL-0004.pdf), but this paper was published before RingCT was found to have extraordinary savings in transaction size for transactions with larger ringsizes.

We have 7 months to explore alternatives and I would like to discuss some viable options
for raising the mandatory ringsize for the v5 hardfork, so that we do not need to again change it in a
future hardfork unless certain circumstances arise.

It is important to note that raising the ringsize of a transaction will increase the time it takes to verify
transactions for nodes, but as far as I am aware this scales linearly(?). So this can be maintained to a reasonable degree and if we assume processor speeds continue to improve, then this problem does not greatly impact the scalability of the Monero network in comparison to the relative gains of privacy for its users. Optimizations in ring signatures and rangeproofs will certainly ease these concerns.

There are two options I would like to explore:

1) Simply raising the mandatory ringsize to a value greater than 4 that can take full advantage of RingCT's optimizations in transaction size without sacrificing very much performance. Ring size 8 could for example easily be used instead of 4 and still have very good performance for example.

and the more interesting option

2) Raising the mandatory ringsize and have it be static so no other ringsizes are accepted in the Monero network. Static ringsizes 9, 12, or 15 would be good options and I will explain a bit more about why those ringsizes specifically are special later below.

The first option would be simple to implement and the optimizations of RingCT would be immediately realized with very little added cost. However the second option will bolster privacy on the Monero network by a much higher degree. By enforcing only one valid ringsize for transactions this removes any confusion and complexity for new users who do not understand why you would want to increase the ringsize of a transaction if transactions in Monero are all already private. Since the protocol would be enforcing a static ringsize, then all transactions would be homogenous and would circumvent analysis of transactions by adversaries who may know that for example exchange x uses ringsize y for all their outgoing transactions, or that there is a user that regularly specifies atypical ringsizes like 41 for all their transactions. This removes a human element to transactions that could save people from unintentionally reducing their privacy as well as other users' privacy.

In the future, businesses and services could be 'assigned' very specific ringsizes that would stick out on the blockchain for passive observers to more easily identify their outputs in other ring signatures, this is only hypothetical and one of many possible scenarios where irregular ringsizes could reduce privacy in the Monero network.

I believe that this is a very valuable and natural addition to Monero since the protocol already makes decisions to protect its users like dynamic fees and randomly choosing their ring partners according to specific parameters. A static ringsize would just further streamline the user experience while defending against many attacks via passive analysis of ring signatures.

In addition to the arguments I made for a static ringsize I will also propose a new output selection algorithm to assist a static ringsize. Going back to why I had specifically mentioned static ringsizes 9, 12, and 15 is because if a third of ring partners are chosen randomly from the past five days and the remaining two thirds of ring partners are chosen at random then a few narrow edge cases that would threaten privacy would be completely eliminated or at the very least much less impactful than only having a default ringsize 4.

I will demonstrate these claims with some hypothetical scenarios using a ringsize of 12 as an example.

Scenario 1: Alice sends Bob a transaction with an output that is two days old. In Alice's ring signature are four inputs from the past five days chosen by our output selection algorithm(plus Alice's real spend) and eight additional inputs chosen at random.

Alice has complete financial privacy as her real output is masked with the other 12 ring partners without any major inconsistencies in our output selection algorithm. Since there is a chance at least one of those eight outputs chosen at random could have been from the last five days the additional recent output in the ring signature is not entirely suspicious. This will still be taken into account by passive observers since a lot of people will be spending money soon after it has been received. Possible scenarios where this would definitely question the legitimacy of randomly chosen outputs and directly threaten privacy is discussed in more depth later.

Scenario 2: Same as Scenario 1 but instead Alice has an output that is one month old. Our output selection algorithm will again choose four random outputs from the past five days and eight outputs at random.

Now the problem is Alice has an output that is older than the outputs that would be specified from the last five days and if the other eight random outputs do not coincide with the last five days then only four recent outputs will exist in the ring signature. This is a direct indication that none of those outputs is the real spent output because only four recent outputs would be chosen from our algorithm anyway, hence being fake. Luckily the other eight random outputs still mask Alice's real output so this scenario does not greatly threaten her privacy as the transaction would effectively still have the strength of ringsize 8 down from 12.

Scenario 2 is less likely to occur if a larger timespan is chosen for recent outputs in our algorithm so the randomly chosen outputs have a higher chance to be in that timespan, but since money is typically spent within a short time after being received this will directly weaken the obfuscation of our recent outputs selected for a ring signature.

The output inconsistencies in Scenario 2 cannot be solved very well without adding additional formality to the output selection algorithm making it easier to single out specific outputs that are not consistent with our output selection rules like in Scenario 2. With a ringsize of 12 at the very least an effective strength of ringsize 8 would still exist for a transaction.

However if an observer were able to find inconsistencies within a transaction with multiple inputs, all or at least some, containing more than four outputs younger than five days old it is incredibly unlikely the other eight random outputs for each input's ring signature would contain very recent outputs. This would question the legitimacy of the eight other outputs older than five days giving the transaction a hypothetical strength equal to the number of outputs in the ring signature younger than five days old or at the absolute bare minimum the strength of ringsize 4.

These scenarios will need to be accepted to exist and thankfully do not completely destroy the privacy of a transaction with poorly chosen ring partners by the output selection algorithm.

Increasing the static ringsize would decrease the likelihood of these contradictions in ring signatures, but it is a tradeoff with transaction sizes. Ideally most transactions would be able to take full advantage of ringsize 12, but the privacy of ringsizes 4 and 8 can still be obtained in worst case scenarios.

I personally prefer ringsize 12 because at the bare minimum when the output selection is not in your favour then at the very least ringsize 4 can still be obtained, which is the original ringsize scheduled for v5 hardfork. Ultimately any ringsize greater than 9 that is a multiple of 3 can be used and if we take into account optimizations of ring signatures and rangeproofs then even larger ringsizes, factors of 3s, could be considered.

The privacy that would be gained with a static ringsize 12 far outweighs any short term scalability issues that may arise in my opinion and would be a boon to the privacy and security of the Monero network while having good safe guards for maintaining a minimum privacy level of ringsize 4.

I hope valuable discussions can be made from this post and further optimizations that can further the security of the network can be discovered.

Thanks for taking the time to read my writeup. Any input is greatly appreciated.

**EDIT:** If anyone is just now finding this discussion and does not want to go through the entire backlog(I don't blame you ;) ) then to catch everyone up to speed what is happening right now is I have been surveying bitcoin transactions for the age of outputs and categorizing them by the last day, week, month, year, and older than a year to get the probability of these outputs being spent to help construct an output selection algorithm for Monero's ring signatures. 

After long discussions with @iamsmooth, having only one static ringsize may be a bit extreme and does not give a user the freedom to increase their ringsize for transactions. @moneromooo-monero mentioned possibly having three static ringsizes for users to choose from. I have been favoring having only three static ringsizes because of its similarity to users being able to choose three different fee options based on urgency, we could have three ringsize options based on paranoia for users to choose from.

So for the time being we are just trying to narrow down what an output selection algorithm would look like. I have to thank @iamsmooth for giving critical feedback and nitpicking different ideas. There is no need to be increasing the ringsize from 4 after we come to a conclusion on a suitable output selection, however I still favor giving the mandatory ringsize a slight bump(to 6?) based on ringct savings in transaction size, but if there is no consensus for doing so ringsize 4 is still a strong option. 

# Discussion History
## ghost | 2017-02-05T02:51:43+00:00
This is a great topic to highlight. To my knowledge, we haven't really had a decent post-RingCT discussion of ringsize. I assume keeping the size of the database smaller rather than bigger will be a part of this discussion, but personally I like your thinking, particularly the idea of a static ringsize.

## ghost | 2017-02-05T09:22:12+00:00
Is this inspired by the latest work by @knaccc describing the churn required for true anonymity in ring sets?

## olarks | 2017-02-05T16:35:01+00:00
@NanoAkron I have not been around the last few weeks, so I must have missed that discussion. This writeup was inspired after looking deeper at the ring signatures and output selection algorithms. Though I am not aware of anything else that could fix these problems without setting a suitable static ringsize 12 like I discuss above. The problems are just inherent to the output selection algorithm and taking those flaws into account with a ringsize that can still protect users.

## RandomRun | 2017-02-05T20:44:33+00:00
Hey, I am glad to see input selection and ringsize value being put under the microscope to fix some information leaks that still exist. Indeed, if one looks at the high ringsize transactions, it is possible to trace back the user's inputs with some probability of success, assuming that the user is "the high ringsize guy" that uses all the highest values in each ring.

I think that @olarks approach is in the right direction, but I'd like to make a few suggestions. But before moving on to those, I just wanted to note that there are two different issues at play here: (i) inputs age correlation, and (ii) their ringsize values correlation, both of which may leak information and help with traceability.

**Inputs age:**

If we knew *the actual* probability distribution for the ages of the inputs actually consumed on each new ring, then we could just sample that distribution as much as needed to build new transactions. AFAIK, we don't have that distribution yet, but it would be a worthy endeavour to try to obtain it by looking at the blockchain of some non-private coins, like Bitcoin. I bet that if some one did that, we would be looking at something that resembles a [Zipf distribution](https://en.wikipedia.org/wiki/Zipf's_law), or otherwise some form of [power law](https://en.wikipedia.org/wiki/Power_law) distribution. In that regard I think that the distribution suggested in the OP might not be the best fit for that, since it is the superposition of two uniform distributions.

If we assume for the moment that the actual distribution is a Zipf. Then all that the wallet has to do is pick a day according to it, and then, within that day, just choose one input uniformly at random. Repeat this process untill you get enough inputs to complete your ring. Add your own input to it, which by definition can be viewed as picked according to the actual distribution, and you are done.

[As a side note, if it turns out that that "the actual distribution" and hence the one we use to sample the inputs does follow a power law and has a long tail, it might make the blockchain a bit more prunable, in the sense that over time it would be very rare to see a transaction involving a very old input, real or decoy. And so, maybe not all nodes will have to keep the blockchain history older than say 5 years (although of course all the inputs would still have to exist somewhere). This would not be possible if we keep sampling inputs according to a uniform distribution, though.]

**Ringsize:**

Monero has a good level of privacy, and that comes in part from the size of your anonymity set in each transaction, which in this case is the ring size, so the bigger the better.
I agree that we should make it easier for the user not to do something stupid everywhere we can, and that includes ringsize selection; and I like the idea of increasing the minimum ringsize way beyond 4, since that doesn't seem to be a bottleneck, at least in the forseeable future. But on the other hand, I would prefer it to be done by way of selecting good default options rather than banning some ringsize values (except for values under the minimum, that is good of course).

So instead of simply defaulting the wallets to set ringsize to 4 or 8, why not have the default be a random value as well? Perhaps let it be a uniform random value between 8 and 50, or a triangular distribution from 8 all the way down to 100, or even another power law. I don't have a completely well formed opinion about the choice of distribution for the ringsize, except that I really think it should be random by default. That way, if a user does decide to use a higher ringsize, hopefully they won't stand out as much as right now, when it is prety much all ringsize 2 and 4... 

---------------------------------------------------------------------------------
@NanoAkron: Could you please link to @knaccc's work that ou referenced?






## hyc | 2017-02-05T21:38:52+00:00
@knaccc's latest draft is here http://termbin.com/kplo

## JohnnyMnemonic22 | 2017-02-05T23:08:11+00:00
As a possible solution to the scenario 2 issue, instead of the number of selected 5-day-old ring partners being fixed to ringsize/3, why not make it a random number between 0 and ringsize-1? Wouldn't that eliminate the possibility of clever deductions based on input age?

## kenshi84 | 2017-02-06T01:24:42+00:00
@RandomRun 
> So instead of simply defaulting the wallets to set ringsize to 4 or 8, why not have the default be a random value as well? Perhaps let it be a uniform random value between 8 and 50, or a triangular distribution from 8 all the way down to 100, or even another power law. 

But the tx fee is proportional to the ringsize. For example, currently the fee for a 2-in/2-out transaction with ringsize of 8/50/100 would be 0.024/0.033/0.045, respectively. So I can imagine users will cancel and repeat the tx construction algorithm until the algorithm picks a smaller ringsize to reduce the fee. I think that was the point of the enforced minimum mixin.


## olarks | 2017-02-06T04:09:48+00:00
@JohnnyMnemonic22 The main problem with a randomly variable output distribution is now your minimum privacy guarantee is random too. While this could make scenario 2 less likely to occur the minimum privacy level being guaranteed could be lower than ringsize 4, in some scenarios, which I think is undesirable. Having a concrete minimum ringsize that can be accepted to fall back on, like ringsize 4, when randomly chosen outputs are unfavorable for a user is the better alternative imo. 

@RandomRun Zipf distribution or other power laws could be possible, but this would add an additional uniform pattern to how outputs are chosen wouldn't it? Any output that does not fit the uniformity of the power law would likely to be the real spent output right?

The reason why I chose the output selection to have a completely random distribution, within two seperate timeframes, is because it is less likely to be successfully scrutinized by an attacker sorting through randomness. By having the number of outputs from the last five days be ringsize/3. this can provide a 'minimum' functioning ringsize to ensure that even if our random output selection are poorly chosen we have a safety guard in place to still provide good privacy.

I had also pondered having a random ringsize be chosen for every transaction within a defined range, but this won't be enforced in all wallet software. The network would still allow any ringsize in our chosen range to be used which means not all transactions would be using random ringsizes, rather favoring the minimum ringsize to save on transaction fees like @kenshi84 points out.

I think having a static ringsize would be invaluable for the level of homogeneity it would provide because the more transactions stand out from eachother the more likely passive analysis can make a connection among them.

Thanks for your input @RandomRun

## Gingeropolous | 2017-02-06T04:27:35+00:00
@RandomRun @olarks , I'm digging the higher fixed ringsize. And hopefully we're all agreed that its ringsize now . I've had a longstanding concern over inputs age. 

@iamsmooth posted something recently in IRC and I dunno if it was followed up, but it sounds like its related, so I'd thought I'd post, and I hope smooth doesn't mind that I copy and pasted his words.
```"Jan 30 11:04:03 <smooth>        given enough transcation volume (unclear whether we have this now or not) what i think should be done is
Jan 30 11:04:30 <smooth>        to pick some random recent transaction, pick a random input, and then use that (approx) age to pick your fake out
Jan 30 11:04:58 <smooth>        repeat until done
Jan 30 11:06:21 <smooth>        this will converge to fake outs having the same distribution as real outs, even though real outs cant be identified. statistical magic
Jan 30 11:10:53 <smooth>        there might be some reasonable refinements like picking a random recent transaction of the same or similar shape (in terms of number of inputs and outputs)
Jan 30 11:11:12 <smooth>        at the cost of needing even more volume for that to be reasonable
"
```
what do you guys think? 

## iamsmooth | 2017-02-06T06:45:56+00:00
The discussion of a single fixed ring size is worth having, from the perspective of increasing homogeneity, and therefore offering a potential _system-wide_ benefit. I'm generally not a fan overall of proposals to blanket increase the minimum ring size because of the accompanying increase in tx size, cost, and therefore likelihood of reduced usage (which in turn carries its own cost in reduced privacy _in practice_ in addition to probably increased likelihood that Monero fails to reach a critical mass of adoption quickly enough or at all, and fails entirely). 

It is certainly usually true that one can improve the privacy of _individual transactions_ in various ways by increasing the ring size, but this is different in kind from the sorts of catastrophic cascading _system-wide_ failures/attacks that motivated the MRL-0004 recommendations. The bar to mandating increased costs is higher when it is a more direct quality/cost trade-off and not a system-wide failure mode or benefit (acknowledging the potential that a fixed size might carry such system-wide benefits).

I expect there will be a variety of wallets and tools built on top of the Monero protocol that will improve privacy at higher cost or with different tradeoffs (such as delayed availability of funds) by managing transactions in various useful ways (and likewise some that will minimize costs within the protocol rules for users who care more about _that_). Those don't all need to be built into the Layer 1 core protocol. Unless there is demonstrated systemic effect, I'm reluctant to (attempt to) impose a more expensive one-size-fits-all solution upon everyone.


## olarks | 2017-02-06T08:32:09+00:00
Another concern is as the TXO set ages, then each randomly chosen output is less effective because in the future if four year old outputs are being selected for ring signatures it is likely those aren't the real outputs being spent. At the same time you don't want to be only favoring newer outputs for selection because then spending older outputs will stick out and be suspect for the real output being spent.

There would need to be in place some kind of schedule for increasing the mandatory ringsize every x years to offset this problem, so even though old outputs are being selected there is enough ring partners not to look suspicious in the ring signature. Hopefully by then we will have good scaling solutions, so this increasing bound does not bog down the network.

## hyc | 2017-02-06T08:57:26+00:00
How about: for ring size N, we pick N/2 outputs around the same age as the real one, and N/2 outputs clustered around a randomly chosen one?

## olarks | 2017-02-06T09:20:08+00:00
@hyc Overall I like your idea, but the group of outputs with the real spend would stand out by having (N / 2) + 1(real spend) outputs. So every transaction's effective ringsize would be cut in half immediately.

## hyc | 2017-02-06T09:42:49+00:00
Assuming this approach is worth pursuing, then we can (1) make sure that the total number of outputs N is always even, so the real spend group is (N/2)-1 random outs + the real out, and the other group is N/2 random outs. Or, (2) if the total number of outputs is odd, randomly choose whether the real group or the random group gets the odd random out.

## olarks | 2017-02-06T11:54:21+00:00
@hyc To expand on your idea, the outputs could be selected based on whether or not the spending output is in the last five days. We could use a static ringsize 10 to ensure that both groups of outputs have the strength of ringsize 5(4 ring partners + 1(potential spend)). 

If the spend is in the last five days then four additional outputs are chosen at random in that timespan. For selecting the last five outputs then you could randomly choose one output in the TXO set and have it be a base point for randomly choosing four additional outputs within five days of the base output.

If the spend is older than five days then it is pretty much the same situation, but instead of choosing another random base point you would just randomly choose five outputs from the past five days. So in either scenario it is not obvious if the real spend is in the last five days or in the random group of outputs because both situations would be occurring in every ring signature regardless of the age of the real spending output.

A major hole in this though is the spend output only being a few days older than the randomly selected outputs from the past five days. What could occur is all the randomly chosen outputs within five days of the spend output all happen to also be less than five days old which would directly expose the real spend output since it would be the only output in the ring signature older than five days.

Choosing the extra four outputs randomly from the TXO set does not solve this problem very well either because now spend outputs that are only a bit older than five days look out of place in the ring signature because they are unlikely to be randomly chosen very often, and now you risk having the five outputs from the past five days being discarded as potential spend outputs. Giving the transaction effectively only a ringsize 4 with a threat of unmasking the spend output a little older than five days because it is unlikely to be selected often from four outputs in the TXO.

This goes back to my original proposal with static ringsize 12, but in the same scenario only four outputs would be discarded while giving a much higher level of plausible deniability of the real spend output because you get 8 random outputs being selected from the selection algorithm instead of 4, so the suspect spend output is scrutinized to a much lesser degree while only being slightly larger in ringsize 12 up from 10 for this selection scheme.

## JamesCullum | 2017-02-06T12:37:04+00:00
I think in this discussion we should also keep in mind that a higher ring size would lead to a bigger transaction and therefore higher fees. We want to make sure that people are using it for normal transactions which don't necessarily require perfect privacy and are just not supposed to not threaten the legitimacy of the whole network, which is why MRL4 proposed the minimum ringsize. I agree with @iamsmooth that a higher ringsize could be suggested for people seeking better privacy, maybe including a different output picking algorithm, but increasing the ringsize this dramatically will have more downsides on the economic part than benefits from the privacy part.

Nobody wants to **use** a currency where the transaction fees are a major cost. If I want to buy a coffee with a cryptocurrency, I won't choose the one where I pay lots of money to make sure nobody knows I bought the coffee. If coffee is illegal in this country I may be willing to do so, hence I would increase the ringsize myself.

Mandatory ringsize of 4? Yes.
Mandatory ringsize of >4? No.

## hyc | 2017-02-06T13:11:28+00:00
@JamesCullum Your concern doesn't seem valid. The txn size (and thus the fee) is dominated by the number of outputs, not by the ringsize. http://monero.stackexchange.com/questions/3323/with-ringct-on-can-i-lower-mixin-safely-to-save-on-tx-fees

## hyc | 2017-02-06T13:12:27+00:00
@olarks I have no problem with your suggestion of ringsize 12 in this context.

## olarks | 2017-02-06T13:51:11+00:00
@JamesCullum Thanks for your input. The cost of increasing the ringsize with RingCT transactions is very overstated and I did also mention that MRL-4 did not take into account RingCT savings because that paper was written much before RIngCT existed, hence why I want to discuss increasing the ringsize now.

This proposal is to make sure that at the bare minimum a transaction gets the security of ringsize 4 when under heavy analysis. Ringsize 12 is just the cost of being able to strongly maintain this minimum security. 

Your point regarding coffee is not really valid here because I am trying to make sure that when you do buy that coffee your money is still fungible. We would not want you to be getting investigated by authorities because your money had been used in the past by someone else for 'suspicious' things and now you get framed for it. This is what currently is plaguing Bitcoin for ever being used in the real world as a digital cash.

The results of this discussion and proposal I made will allow Monero to resist strong analysis of ring signatures and allow it to be real digital cash.

## JamesCullum | 2017-02-06T14:14:58+00:00
Ups, sorry then. If I recall correctly, before RingCT the ring size was a bigger influence, hence my statement to keep the fees low. If we can do that while at the same time having more privacy, we should do this.

Of course it is important to stay fungible, but it is already at the moment and a transaction age correlation would still give sufficient plausible deniability, meaning that a filter to block tainted coins would hit high false negatives. So I think we are currently (maybe not for long though, hence a higher ringsize than 2) fungible and should work on maintaining that. 12 may be a little high, but if it doesn't cost much more its alright.

## RandomRun | 2017-02-06T15:35:57+00:00
@kenshi84: I can see your point about users choosing to minimize their fees and therefore the ringsize of most transactions converging to the minimum alowed, as it already happens and motivated OP's suggestion to fix the ringsize. I guess if that is the way fees are computed we can't escape the scenario with only minimum ringsizes are used. Unless we change how fees are calculated to subsidize higher ringsize transactions (something like: flat fee of 0.033 for all transactions not bigger than the 2-in/2-out ringsize 100 you used as an example). But this is more me thinking out loud about your comment than giving a concrete suggestion. I actually don't fully understand how fees are calculated, or even why they are "fixed", as opposed to their price being defined by market forces on the network.

@olarks: 

> Zipf distribution or other power laws could be possible, but this would add an additional uniform pattern to how outputs are chosen wouldn't it? 

I don't see how it would add any information. Zipf distribution or other power laws are biased distributions, and therefore *not* uniform, which is the reason why I was suggesting to use them, as I believe this is the way real outputs ages behave.

> Any output that does not fit the uniformity of the power law would likely to be the real spent output right?

An output is just a possible outcome from the distribution. I believe it doesn't make sense to say that it doesn't fit its distribution. At best you could say that it is a rare outcome, but that is fine, as it would be rare both when it happens through a real spend, or through sampling.

> The reason why I chose the output selection to have a completely random distribution

All distributions suggested on this thread are completely random. I believe you are using uniform and random interchangeably, but those are not the same thing. In fact, my main point has been that the actual distribution of real spent outputs is a biased distribution, and therefore if we use a uniform distribution to create our rings, that will leak information.

Let me exagerate the scale, and simplify your suggestion a bit, to hopefully make this more visible:

Let's say outputs ages are in fact a Zipf distribution, and that we are producing our rings sampling outputs from the blockchain uniformly at random. Assume we have ten years of blockchain history and that users are choosing to produce a rings of size 10.

The rings produced with this uniform sampler wouldn't be too far from say having one output from each year, roughly. But as a user, by assumption, you would be very likely spending a very recent output, and it would be very unlikely that one of those 10 outputs chosen over the course of a decade would be more recent than yours. So an attacker could guess that your real input is the most recent one, and be correct with high probability. 

Now you may shrink the interval to 5 days, but the effect is still there, and in the end what you are suggesting is overlaying two samples obtained from two uniform distributions that suffer from the same attack just described.

> At the same time you don't want to be only favoring newer outputs for selection because then spending older outputs will stick out and be suspect for the real output being spent.

They won't be suspect because it would be both rare occurences to see them being actually spent, or randomly selected as a decoy, since both events would be occuring according to the same distribution. You might feel exposed seeing your output alone as the oldest one in the ring, but that is only because you know a priori that that is your output. To everybody else, it will look just like any other ring in any other transactions, all with more more recent outputs than older ones.

The main point I am trying to make is that within each ring, all outputs should have equal probability of being the real one, and that doesn't happen if you are using a uniform distribution to mask events that are modeled by a non-unifrom distribution.

@Gingeropolous @iamsmooth: The problem with using outputs that are close in time to the real one is that it leaks information about the time of the real output being spent. And worse, the higher the number of decoys chosen according to that method, the better the estimation of that piece of information.

## olarks | 2017-02-06T17:01:46+00:00
@RandomRun Ok, I understand what you mean a lot better now. I was getting caught up in semantics. We could try surveying Bitcoin, maybe Litecoin and Dogecoin too since they have good histories going back multiple years and still get good transaction volume to this day. Hopefully some insight can be gained from what their zipf distributions look like and hopefully can be translated into an output selection algorithm Monero can take advantage of.

## luigi1111 | 2017-02-06T18:26:24+00:00
BTW, (I haven't read the entire thread) ring size in RingCT actually scales identically to pre-RCT. It scales very slightly worse with number of inputs (this could be remedied if there was strong need, which I do not believe is the case).

Now, as a % of base transaction size, it is of course smaller. It can still balloon with high input count with high ring size (using the two together is dubious anyway, due to likely real input correlation).

## kenshi84 | 2017-02-06T23:25:07+00:00
I also wanted to bring up the subject about temporal alignments of ring members across different rings, for example:

- https://xmrchain.net/tx/614c4d596e1e69dc190adf00be4c360948cd2930e7ea1ef6a74770dd4aef004c
- https://xmrchain.net/tx/26d6a1e7bca6700014e5a769134ccb142cd3fb19b72ebbc8df596610c9284961

If this kind of temporal alignment happens in a tx with many inputs, and especially if it happens for the ring members in the older time, then it becomes highly probable that those are the real spent outputs. knaccc expressed a similar concern on IRC. A possible remedy might be to artificially increase the chance of temporal alignments for even older outputs so that this kind of event is not too rare. I have no idea how to achieve that, though.

Edit:
A similar question already asked on [StackExchange](https://monero.stackexchange.com/questions/231/how-will-the-temporal-output-alignment-of-ring-partners-mixins-be-addressed)

## kenshi84 | 2017-02-06T23:34:36+00:00
@JamesCullum 
> We want to make sure that people are using it for normal transactions which don't necessarily require perfect privacy

I think your argument goes against the original idea of Monero, i.e., there's no such thing as 'perfect privacy' vs 'moderate privacy'. If the strongest possible privacy feature is not enforced to all participants by default at the protocol level, there's actually no privacy at all; look at Dash/Zcash etc. A small group of paranoid users choosing some 'more private' transaction method at higher cost won't help, because such transactions will stand out in the blockchain which would be easy to analyze. The more uniform transactions, the better privacy.

## iamsmooth | 2017-02-07T01:52:00+00:00
> If the strongest possible privacy feature is not enforced to all participants by default at the protocol level, there's actually no privacy at all

This is not the original idea of Monero at all. The changes to apply a mandatory minimum ring size were made to address specific issues identified in MRL-0001 and MRL-0004 where individual users choosing lower ring size could severely compromise the privacy of other users, and make certain Sybil attack vectors much cheaper for an attacker. That justified imposing higher costs, because the alternative meant severe damage or vulnerability to the system as a whole.

There is no such case being strongly made here, at least nowhere near the degree to which the case was made in MRL-0001 and MRL-0004,

> A small group of paranoid users choosing some 'more private' transaction method at higher cost won't help, because such transactions will stand out in the blockchain which would be easy to analyze

This needs further study and characterization to better clarify what is meant by "won't help". It certainly does help in the sense of increasing the immediate anonymity set on a particular transaction, including the strength of plausibility deniability of having spent a particular output. This carries tradeoffs in terms of standing out from the crowd, but it is not clear (at least to me) without more rigorous analysis how or when these tradeoffs might apply, nor whether this imposes damage or vulnerability onto _other_ users of the system (if a particular user finds the tradeoffs of using a larger ring size to be unattractive, that user can choose not to do so).

## iamsmooth | 2017-02-07T01:57:25+00:00
@kenshi84 
> I also wanted to bring up the subject about temporal alignments of ring members across different rings

That should probably be made into a different issue. Simply increasing the ring size a little won't solve that problem, at least not entirely. 

Time alignment is somewhat addressed in MRL-0004 and the recommended solution is largely to avoid or limit how related outputs are combined and instead send multiple transactions, but that has some costs, including potentially increased costs from RingCT.


## iamsmooth | 2017-02-07T01:58:46+00:00
@RandomRun

> @Gingeropolous @iamsmooth: The problem with using outputs that are close in time to the real one ...

That wasn't my suggestion. Maybe you meant to direct that at someone else though, I think @hyc made a suggestion something like that

## iamsmooth | 2017-02-07T02:01:42+00:00
@hyc 
> The txn size (and thus the fee) is dominated by the number of outputs, not by the ringsize.

It isn't _always_ dominated by the number of outputs. As @luigi1111 mentioned a few replies back, the signatures can still balloon up and exceed the size of the range proofs if the ring size and number of inputs is both large (since they scale with n*m), assuming of course that the number of outputs isn't also large.

A large number of inputs is less common with RingCT but currently it still does happen (I've seen txs with >100 inputs recently). There might be other reasons to discourage that though.

## kenshi84 | 2017-02-07T03:59:12+00:00
@iamsmooth 
> This is not the original idea of Monero at all. 

Well, maybe I just took the idea wrong and am being an extremist. But I do get a puzzled feeling when users are currently allowed to use Monero with different degrees of privacy by changing ringsize. I saw someone on IRC (forgot who) questioning: "Oh, isn't it always private when I use Monero?" There have been quite some questions asked about the degree of privacy w.r.t. ringsize, e.g.:
- https://www.reddit.com/r/Monero/comments/5lli6l/question_about_impact_of_the_payment_id_on/
- https://monero.stackexchange.com/questions/2103/what-would-be-the-minimum-mixin-for-full-privacy
- https://monero.stackexchange.com/questions/757/is-there-a-minimum-effective-mixin
- https://monero.stackexchange.com/questions/100/is-there-a-minimum-and-maximum-mixin-size
- https://monero.stackexchange.com/questions/26/what-factors-are-influenced-by-ring-size-selection

So at least this seems like a common point of question and possibly a source of confusion. Also, users might even _damage_ their privacy by choosing high mixin inappropriately.

I really wonder: does using higher mixin really provide more privacy than using default mixin (currently 4, possibly higher in the future)? If so, does that mean users using the default mixin are somehow risking their privacy?

I wish to be able to tell people simply that "Your privacy is well protected if you're using Monero", instead of "Your privacy is protected very well/so so if you configure your Monero wallet in this/that manner". In my opinion, MRL should continuously conduct studies on the level of possible Sybil attacks and blockchain analysis at present time to come up with a particular ringsize that should provide good enough privacy for everyone, and enforce it at the protocol level on every hardfork.

The community decided to accept the increased cost of RingCT favoring the improved privacy, despite some users complaining. Likewise, shouldn't we accept the increased cost for the fixed higher ringsize to ensure high enough privacy?

Those who want to sacrifice their privacy to save fees may switch to other coins. Or alternatively, some Lightning Network built on top of Monero that offers lower fees at the cost of privacy may be able to satisfy such demand in the future.

## kenshi84 | 2017-02-07T07:07:56+00:00
Maybe I'm being just too naive/opinionated and not seeing the big picture. Please understand that my intention is not to divide or troll this community; Monero's privacy functions only if its user base and transaction volume is large enough, after all. Probably I should carefully read MRL-0001 & MRL-0004 once again.

## anonimal | 2017-02-07T09:35:55+00:00
[He who from the Rhinegold fashioned the ring that would confer on him immensurable might could win the world's wealth for his own](http://www.rwagner.net/libretti/rheingold/e-rhein-s1.html).

[One ring to rule them all, one ring to find them, one ring to bring them all and in the darkness bind them](https://en.wikipedia.org/wiki/One_Ring).

## JamesCullum | 2017-02-07T11:23:32+00:00
@kenshi84 Its a ring size. If you use 2, you can be either one of them and there is no way of really telling but if one of them is evil and tries to spam the network to reveal his outputs, his share is degrading over time and becomes unfeasible - this is why there is a network minimum. A minimum of 4 can do this even faster. This is the reason why Monero chose a minimum, not because that's perfect privacy. After all, with a ring size of N there is a 1/N chance of guessing correctly who you are, with good analysis (and maybe opsec mistakes) this can be drastically increased. If your brother had to choose between you and an evil robot imitating you, having 50% (ringsize 2) or 10% (ringsize 10) can be a big difference on your level of privacy.

So do we really want to force a better privacy even though this doesn't have anything to do with the reason for the minimum? Shouldn't it be the users choice to choose a balance between costs and privacy? This is why you can choose a ringsize and there is not one level for everybody. If we can increase it from 4 to N without more costs or bloat, its an obvious yes. Otherwise, this risk may not be worth it, like my example of buying a coffee or trading from/to an exchange that knows you anyways.

## RandomRun | 2017-02-07T15:31:17+00:00
@iamsmooth: I was referring to the quote in this thread atributed to you by @Gingeropolous. I apologise if I misread what you meant, but if that was indeed you being quoted, could you please clarify what you meant by the "statistical magic"?
_______________________

IMO the problem of  temporal alignments of ring members across different rings brought up by @kenshi84 is a very serious one, and perhaps the solution is not that hard. @kenshi84 has already included code in the wallet that warns users when this issue arises, so how about just making it so that if the user has two or more outputs that are close in time, the wallet, if possible, simply picks at most one of them for a given transaction, otherwise warns the user about the issue? In fact, if the wallet notices that there are two such outputs, then it might prioritize spending just one of them in the first chance it gets just to avoid running out of options in the future. 

If the user does get to a point where all their outputs are close in time, then perhaps they should be allowed/encouraged to spend (to themselves) one at a time. AFAIK there is no option yet for a user to send just one selected output entirely to himself, but it might be handy in these situations.

I realize that when @kenshi84 suggested giving users more say one output selection, he was met with some resistance on the basis that users messing up with output selection might invite more problems, perhaps of the likes of what we are seeing with ringsize selection, but if that is done in the wallet background, I believe this shouldn't be a problem.

IIRC there was also an objection aong the lines of "not allowing for outputs too close in time might reduce the randomness of the output selection algorithm", which I guess is technically true, but given that a time collision is overwhelmingly more likely to occur because they belong to the true sender than otherwise, I think avoiding these collisions in the transaction building algorithm might be a better way to go. Actually, since if this gets implemented only for the true spent outputs, an attacker would be able to deduce that any collision is therefore necessarily made of decoys, maybe it would be a good idea to make things more homogeneous and even not allow for decoy coillisions as well.



## t4777sd | 2017-02-07T19:03:35+00:00
In my view, ever-increasing ring sizes is not the solution. This is not a discussion where simply increasing a value leads to more privacy. You increase this value and it may have the opposite effect where **privacy is reduced by raising ring size**. In this way, the correct value to use is non-obvious.

The best way for Monero to obtain privacy is to drive adoption. Not just in users, but in number of transactions. If ringsize is too high, then it will deter adoption and without adoption, monero has no utility. What is the point of having a fungible coin with a utility of 0? And, how private is monero when the population size is only a few thousand people? Certainly, even the blackbox solutions in more popular transparent chains could be more private than monero (given the higher adoption rate and hence higher # of people who use the blackbox solutions versus monero).

The existing ring system already has a lot of issues. For example, governments can create a lot of dust transactions on the network. When generating rings users will include these addresses when selecting what other addresses to use. And, this can be used by the attacker to reduce the effective size of the ring.  The same effect occurs as people publicize their addresses (either willingly or they are forced to to meet compliance regimes, which erode privacy of the whole network).

The solution might be to increase the ring size, but you do that and you just decreased the number of users and transactions on the network. Few are going to pay all the costs that super-super obfuscated chain requires to purchase coffee. So, the result will be, those transactions disappear from Monero which is sad because those are the transactions that help provide anonymity for everyone else.

So, in my view, the solution is instead to offer "pretty good" privacy on-chain that is econmical, by default. A level of privacy that still allows a large number of people to use the coin (which increases absolute privacy offered) and still provide a lot of deniability. A ring-size of 4 does this IMO.

For those people that need more than coffee-purchase level of obfuscation, the best solution to them would probably be to churn transactions. Or, alternatively, they can use higher ring sizes for those specific transactions. 

## iamsmooth | 2017-02-08T01:27:25+00:00
@ RandomRun

My suggestion (quoted by @Gingeropolous) was to use the distribution of ages of outputs spent by inputs of recent transactions (say from the most recent month) as a model distribution for choosing random fake outputs. This does not suggest using outputs similar in time to your own real output at all. 

What it does do is include a distribution of unknown real outputs in the fake output selection since each candidate model transaction input necessarily includes a real output, as well as several fake ones. If everyone uses this algorithm, and there is no apparent reason why they shouldn't, then everyone's fake outputs will be chosen with ages from a distribution that matches the distribution of ages of real outputs, even though there is no other way to direct measure the distribution of ages of real outputs. That is the 'statistical magic' part, and it is the gold standard of minimizing statistical inferences from the fake output selection being biased relative to real output usage.

The vulnerability I see in this is someone spamming the network with bogus transactions using a deliberately poor distribution of fake outputs to pollute the distribution used by the above method. As @t4777sd commented, this really needs to be addressed by maximizing legitimate usage (and I agree in principle with his comments on that point). Indeed someone performing this sort of spam/Sybil attack is already compromising privacy to a large degree, though in neither case is the attack fully effective, it is more of a degradation.

> a time collision is overwhelmingly more likely to occur because they belong to the true sender than otherwise

This is not entirely clear. When there are many transactions being performed there will be many (at least approximate) time collisions that randomly occur. This assumes that the wallet avoids the worst failure modes, which it already does, such as using multiple outputs from the same transaction. A certain number of real collisions become largely if not entirely indistinguishable from the background noise, or at a minimum still provide plausible deniability (there is no way to know, with certainty or necessarily high confidence that a candidate collision is actually real, even if you might suspect this). To the extent that they don't, @t4777sd is also correct that those requiring absolute iron-clad protection against any possible inferences or statistical bias will need to take stronger measures _at higher cost and at their own expense_. Many people do not and will not need that (for example to prevent your landlord from easily seeing that you got a pay raise and raising your rent as a result).

## olarks | 2017-02-08T04:14:10+00:00
@t4777sd I agree there needs to be a balance. Increasing the ringsize does not immediately mean there are less users and transactions taking place, it has a bell curve distribution. My intentions are for all transactions to obtain a minimum ringsize of 4 for plausible deniability, however there are many situations where having a ringsize 4 or even higher does not obtain our goal, as explained extensively in this thread. 

The ringsize and output selection go hand in hand because the output selection algorithm is not a secret and if the algorithm is predictable then you are making an attacker's job very easy, hence why my OP favors a largely random output selection which can only realistically be used by having a larger ringsize to increase obfuscation.

Monero touts being a private currency, but most users do not know how to evaluate ringsizes. The user should not burden these decisions when the protocol by design is supposed to protect them. If a coffee transaction does not have strong privacy then many other types of transactions in the network also don't have strong privacy. I don't think this is acceptable regardless of how "unimportant" a transaction is. All transactions in Monero are supposed to have strong privacy.

## iamsmooth | 2017-02-08T05:53:31+00:00
> All transactions in Monero are supposed to have strong privacy.

No. All transactions provide privacy on the basis of a strong mathematical and cryptographic foundation. But it is not the case that any of these small ring sizes (3, 5, 12, etc.), by themselves, provide "strong privacy". That is just not a very high degree of obfuscation when viewed at the individual transaction level.

The system works by combining several techniques including stealth address, ring signatures, confidential transactions and later i2p to so that even narrowing down the potential output to a small number of candidates (as ring signatures inevitably do) still allows users to retain a reasonable degree of privacy in a majority of cases (even in some cases where a subset of these techniques individually fail). In cases where people want or need even more privacy than this base level, additional techniques and tools can be layered on top of the sound foundation.



## olarks | 2017-02-08T06:22:14+00:00
@iamsmooth I understand what you are getting at, but for this discussion I am purely interested in the analysis of ring signatures. RingCT, stealth addressing etc are all strong as long as their underlying cryptographic assumptions are sound, which I believe they are. 

Ring signatures on the other hand are bound to different assumptions relying on the output selection for the strength of the ring signature. Ring signatures are arguably the most important part of the system because if you know where money is coming from it does not necessarily matter where you sent money or the amount pertaining to the transaction if you can go back and decipher the history of all the transactions involved.

I am skeptical that regular users would use anything but the default option for sending transactions. The majority of transactions in Monero right now are all using ringsize 2 and 4 because of the default options in their wallet of choice. This is also evident in other cryptocurrencies with optional private transactions, they just are simply not used in 95 out of 100 transactions. 

Thankfully Monero already protects users by default to a degree, but I want to ensure that there are as few holes as possible by default because most people will only be using the default option for transactions, hence why I favor a static ringsize that uses a larger ringsize so the output selection is less prone to advanced analysis by adversaries. 

Treating some transactions differently than others in Monero is putting everyone's privacy at risk.

## iamsmooth | 2017-02-08T08:48:19+00:00
@olarks The problem I have with your claims is that you aren't backing them up with any sort of research:

. Treating some transactions differently than others in Monero is putting everyone's privacy at risk. [Everyone? By how much?]
. I favor a static ringsize that uses a larger ringsize so the output selection is less prone to advanced analysis by adversaries. [How much less prone? Under what conditions?]
. if you can go back and decipher the history of all the transactions involved [Can all transactions involved really be deciphered, or only some of them? In the latter case especially, things like stealth addresses and arguably CT do matter, because a partial analysis that leads to a dead end (unknown amount coming from an output not tied to any other outputs nor any particular public address) does not necessary accomplish anything useful.]

You see what I'm getting at here. There are a lot of hasty assumptions and without support for those conclusion the case for imposing higher costs isn't very strong, nor is there a good basis for deciding how much higher those costs should be (why not make ring sizes even bigger!).




## olarks | 2017-02-08T10:57:36+00:00
@iamsmooth I have made it clear that I am using a ringsize 4 as a baseline for the minimum amount of privacy a transaction should expect to have, and that just having a transaction default to ringsize 4 does not mean it actually achieves our goal because of how outputs are chosen. I explain quite thoroughly in the OP and throughout this thread why it does not in many situations.

The goal here is to have every transaction meet a MINIMUM effective ringsize of 4 for plausible deniability. I explain how static ringsizes help reduce connections made between transactions in my OP. The static ringsize idea is separate from our goal of maintaining ringsize 4 for all transactions. I only mentioned a static ringsize because it is in the same spirit of protecting users privacy in Monero by having all transactions look the similar and thus less prone to analysis, not much needs to explained here for how it does this.

I never said CT and stealth addressing do not matter. I am only saying that if a ring signature is exploited then it is not hard to find out, for example, that the real output could be linked back to an exchange or a store that will have both the identity of the spender and the amount for the transaction logged in their system, completely disregarding both CT and stealth addressing. Hence why getting ring signatures and the output selection right is so important.

The ringsize and output selection go hand in hand. It is an interesting information theory problem because if the selection algorithm is predictable an attacker can easily just pick out any outputs in a ring signature that are expected to occur based on the algorithm. A combination of randomness and formality is required in the selection and balancing this properly is the result of what assurances in ringsize we are trying to make when being analyzed. I chose ringsize 4 as this minimum because that is what MRL suggested and is why we are currently scheduled for a hardfork in September, seems most people agree this is a pretty good baseline for privacy.

In the end it does not matter if the mandatory ringsize we decide on is 7, 12, or 50, as long as the minimum assurance for privacy we can make is ringsize 4 and is accompanied with a selection algorithm that can ensure this, the rest is icing on the cake. Obviously we want to find the minimum mandatory ringsize to have these qualities so scalability is not greatly sacrificed.

I hope you see what I am trying to get at here.

## JamesCullum | 2017-02-08T11:04:21+00:00
> I am skeptical that regular users would use anything but the default option for sending transactions.

Actually most of them use the default in the wallet, not the protocol level minimum. This is why MRL already recommended to have a default of 4 but a minimum of 2. I think we should set the minimum to 4 (it doesn't endanger the privacy of others, so everybody should be able to choose if they want more obfuscation) and can set the default in the official GUI to 12.

## olarks | 2017-02-08T11:12:01+00:00
@JamesCullum I mentioned that it is because of the default in the wallets in the sentence after the one you quoted :) 

## JamesCullum | 2017-02-08T11:44:43+00:00
You are correct, but in the context of you asking to raise the minimum it felt to me that you mean that a raise of the minimum would implicitly result in higher default transactions (which it would do), while I tried to say that you can raise the wallet defaults in the GUI very easily without changing the protocol minimum in a similiar manner.

And I think that we now need some kind of compromise (there are many different opinions here), hence I suggested the minimum of 4 and wallet default of 12 :)

## olarks | 2017-02-08T13:00:15+00:00
@JamesCullum So far only @iamsmooth has spoken up against what I have written. My specific proposal only pertains really to ringsize 12. The algorithm does not work well enough for ringsize 4. 

This is why I made this discussion 7 months before September so we can come to a conclusion on this. The problem is not simple and I don't think what I wrote is the best option or the only possible option. I imagine I am not the only person who has ever thought about these problems with ring signatures and I hope that we can all figure this out, so we don't just keep kicking the can down the road and need to hardfork again to fix any problems with ringsize/ring signatures etc.

## JamesCullum | 2017-02-08T14:27:39+00:00
I understood that the ringsize is the major point of this discussion, not the algorithm for output selection. I would stick with the random triangle but allow users to pick own outputs. While this may not be used too often, it would effectively reduce the probability of making a connection between the outputs as this could always be a manual selection as well and statistical analysis can not analyse decentralised output selection.

However, this is a rather different approach to it and I can understand that it may not be feasible compared to other methods.

EDIT: I thought I made it obvious, but I was talking about an optional possibility, so that the current one would be used for the majority of transactions but during an analysis it wouldn't be certain if this was automatically or manually chosen.

## olarks | 2017-02-08T15:00:44+00:00
The output selection algorithm is more important than the ringsize. If the outputs are poorly chosen the ring signature is wholly useless no matter how many ring partners exist. Allowing users to pick their own ring partners will likely have the opposite effect, as people would lazily choose them and open users up to another way to accidentally compromise theirs and others privacy.

## ghost | 2017-02-08T15:24:55+00:00
@JamesCullum Users picking outputs == less random than a machine picking outputs. Always.

## JollyMort | 2017-02-08T17:03:28+00:00
@olarks wrote:

> In the end it does not matter if the mandatory ringsize we decide on is 7, 12, or 50, as long as the minimum assurance for privacy we can make is ringsize 4 and is accompanied with a selection algorithm that can ensure this, the rest is icing on the cake.

Do you mean to say that, regardless of what the actual ring size is, you want to make it near certain that you can't ever eliminate all of the ring partners as being the fake ones, and would always remain with minimum of 4 for which you can never tell for sure?

With actual ring size of 5, in some cases it could be trivial to narrow it down or even immediately tell which is the real one and which are fakes. Your proposal seems to want to make this narrowing down hit a wall around 4?

Like, using 4x3=12, where these groups of 4 would be scattered close to some random 3 heights picked as per triangular distribution?

## RandomRun | 2017-02-08T20:20:23+00:00
@iamsmooth: Thank you for taking the time to write a more detailed explanation of your method, but I must confess I still don't understand it fully. For instance, when you say:

> use the distribution of ages of outputs spent by inputs of recent transactions

I am understanding that you would take a recent transaction, and pick one of its inputs *I* (fake or real, no way to tell for sure), look at the outputs present in the rings that generated it, and keep their ages as a sample point. repeat this process for all inputs *I* being used in recent transactions. Infer the distribution behind all those ages, and use this distribution for generating your rings going forward.

If that is what you meant, and if people are just using say a uniform, or triangular distribution, because that is what is encoded in their wallets, then wouldn't you just be rediscovering that fact through your measurements? I understand that it shouldn't be exactly that, since whatever the distribution of the real outputs is, it is going to bias the sample even if just a bit. So are you saying that if this process is iterated, over time it should converge to the real outputs age distribution? (I guess assuming participants are not deliberately producing bad rings to destabilize this convergence?) If so that would be very nice. Do you by any chance have this formalized?
___________________________________________ 

@iamsmooth: 
>["a time collision is overwhelmingly more likely to occur because they belong to the true sender than otherwise"] is not entirely clear. When there are many transactions being performed there will be many (at least approximate) time collisions that randomly occur.

After you pointed this out I realized that I wasn't so sure about the estimations either, so I did a few simulations in Sagemath to gauge how likely decoy collisions really are when using various distributions.

Using Sagemath, and this [referrence](http://doc.sagemath.org/html/en/reference/probability/sage/gsl/probability_distribution.html), I simulated the scenarios where we pick 2 and 4 random decoys for each ring, and kept track of the number of collisions between the two rings we get after 1 million trials. In the table we can see what proportion of those trials contained collisions. (A collision here is when two inputs are picked from the same 2-minute interval.)

| Ringsize | Uniform | Triangular | Power(1/2) | Zipf |
|------------|------------|--------------|----------------|--------|
|      2       | 0.000194 | 0.000259 | 0.000465 | 0.055021 |
|      4       | 0.000770 | 0.001017 | 0.001960 | 0.185124 |
-------------------------------------------------------------------

So that if we are using a uniform, triangular, or even a power law with exponent 1/2, random decoy collisions are pretty rare leaving user's exposed. With the Zipf distribution, the collision level seems more in line with reality, if I had to guess.

Everybody please feel free to tinker with the code and test other scenarios! The code can easily be modified to check for likelihood of collisions happening between more than two rings in a transaction, and for other time frames, of course.
______________________________________________

**Code:**
```python
'''Slots are 2-minute intervals over the course of a month:'''

TimeSlots = 30*24*30

trials = 1000000
ringsize = 2

'''Distributions:'''

Unif = [1 for i in range(1, TimeSlots + 1)]
Tria = [1-(i-1)/TimeSlots for i in range(1, TimeSlots + 1)]
PowerHalf = [i**(-0.5) for i in range(1, TimeSlots + 1)]
Zipf = [1/i for i in range(1, TimeSlots + 1)]

'''Set RHS to desired distribution:'''
Distribution = Zipf

X = GeneralDiscreteDistribution(Distribution)
Collisions = 0

for j in range(trials):
    
    '''generating Ring1...'''
    L = []
    for i in range(ringsize):
        L.append(X.get_random_element())
    Ring1 = set(L)
    
    '''generating Ring2...'''
    L = []
    for i in range(ringsize):
        L.append(X.get_random_element())
    Ring2 = set(L)
    
    '''Set of collisions...'''
    Set = Ring1 & Ring2

    if Set != set([]):
        Collisions += 1
print "Proportion of trials containing collisions: ", float(Collisions/trials)
```

## moneromooo-monero | 2017-02-08T20:21:18+00:00
The info leak from uncommon mixin use was known for a long time, and I would suggest quantizing usable mixins similarly to the fee quantization ArticMine proposed, so that there will be three possible mixin values. Maybe 4 (network enforced minimum), 15, and 127. These values are arbitrary, and should not be viewed as an actual proposal, merely a starting point. These might be made 12, 40 and 150 for the purposes of that paragraph. The wallet default might not be the smallest one.

I am not sure whether it is clear to everyone here, so: the current fake output selection algorithm will select 25% of the fake outs from the last 5 days or so, and the rest from the whole blockchain. The 25% is set so that (1) there is at least one output (meaning it might be a bit over 25% if mixin 2), and (2) the real output is taken into account, so that if your output is alread in the last 5 days, one less fake out will be selected in the last 5 days, so Eve can't say "hey, one more output than usual in the last 5 days, which means the real output is recent". Both picks use a triangular distribution. Note that this means picking a fake out within the whole blockchain might well pick an out that's within the last 5 days too.

I lilke the Zipf (power law) idea. This seems to be a good replacement for the whole 25% recent and 75% whole chain current system. Research would nice to have, but realistically it will only happen if someone decides to do it, so we should not block on this.

Output selection will pick unrelated outputs where available (where related means within 10 blocks (IIRC) of an output that's already selected). This does introduce a slight bias of course, but probably insignificant.

Effect on blockchain size is something that's not insignificant compared to the increase in privacy. It is also not 100% clear how "privacy" increases with mixin in the first place.

I agree that adding a real output to a distribution of fake outs which maps the actual use of outputs does not by itself bias. However, the real problem lies within the addition of a second ring within the same transaction. I believe the comparison of two (or more) rings in a tx is what can give the most information on what the real inputs are in each ring, with the current selection algorithms.

A user cancelling a transaction after seeing "obvious correlations" in the "are you sure" prompt will cause information to be leaked to the daemon. If this is your own daemon, all is good. If you're using a third party daemon, then your privacy will be compromised to some extent. This is because you asked the daemon for the keys to all those outputs (fake and real). If you cancel and try another tx, different fake outs will be selected, but chances are the same real outs will be selected (especially now that the the code tries to use only one or two inputs). Therefore, the daemon can compare both requests, and see which outs are yours with very high probability. Besides, a totally random process can very well include patterns. If is, after all, random. The best defense against this is to avoid having many inputs. In fact, maybe forcing all transactions to be 1 input and 2 outputs might be a good thing... ?


## RandomRun | 2017-02-08T20:34:39+00:00
I forgot to conclude my previous comment: if it turns out that something like Zipf is the actual distribution we should use, then random collisions will be so common that we might even not worry about the real ones, since they won't stand out.

## knaccc | 2017-02-09T00:25:34+00:00
My thoughts:

1. Churn

As mentioned in my paper http://termbin.com/jp5r (full text pasted in comment below this one) there is a big problem when:

Bob obtains multiple outputs from Alice and then spends multiple outputs with Charlie, and then Charlie's owned outputs are exposed to Alice.

  The only way I can see to solve this problem is with churn (sending funds to yourself multiple times). In the paper I've determined that between 7 and 12 levels of churn are required if there is mixin 4. Increasing mixin to 12 would  reduce the number of churn operations from 7 to 5, which would mean a 28.5% reduction in churn costs.

I agree with @iamsmooth's comment about erring on the side of keeping transaction costs down for most users, rather than saving users fees on their occasional churn operations.

Note that it doesn't much help if the person performing a churn uses a higher mixin - what really helps is when most other people are using a minimum mixin.

For this reason, I don't like the idea of communicating to a user that higher mixin will give them more privacy, since there are so many situations where increasing it at all is a pure waste of money and gives the user anxiety over a choice which is not of great significance for their privacy. I believe @kenshi84 agrees with this.

2. Pure RingCT trees for churn

@kenshi84 pointed out that this churn idea only works when we're churning with trees of possible predecessor outputs that are pure-RingCT. This is because pre-RingCT outputs of known sizes can be excluded from the set of possible predecessor outputs when the real value of Charlie's owned outputs are exposed. This situation will cure itself as the majority of outputs on the blockchain become RingCT outputs. 

3. Temporal alignments

As @kenshi84 has pointed out, temporal alignments of older outputs mean that the real outputs in a ring signature can be determined with significant probability. This is a problem because it reduces the effectiveness of churn when outputs are selected which have obvious probable real predecessor outputs.

A solution, as @iamsmooth suggested, would be to select decoy outputs with the same distribution as the real outputs in the ring signature.

4. Churn detection

The churn suggestion also breaks down if it's possible to detect a churn occurring. If it can be deduced that a set of n outputs have merely been translated through several churn operations because they keep appearing as the inputs of immediately subsequent transactions, then the benefit of churning is lost.

To counteract this, it's important to ensure recent outputs are used heavily as part of transactions.

I like @olarks's idea about two timeframes used when selecting outputs. Here is something I've previously written:

An alternative method of selecting ring signature inputs:                                                                                                                                                                 

The function currently used to determine the index of each output that is added to the ring signature is:
                                                                                                                                                                 
`(number of outputs in existence) * ((random number between 0 and 1) ^ (1/2))`

Source: https://github.com/monero-project/monero/blob/a3de797e5778b189f3e18877516ab8a72563badf/src/cryptonote_core/blockchain.cpp

This function will favor recent outputs for selection in the ring signature. However, it does mean that as the size of the blockchain grows, outputs from the past 30 days will be increasingly less well represented.
                                                                                                                                                                                                         
We therefore propose a hybrid function to solve this problem, where half of the inputs selected will come from the entire blockchain history, and the other half will come from the last 30 days of outputs created. This ensures that however large the blockchain grows, the last 30 days of inputs will be very well represented.

Therefore the hybrid function proposed is as follows:

For each of the first half of ring signature inputs:

`index = (number of outputs in existence) * ((random number between 0 and 1) ^ (1/2))`

For the second half of ring signature inputs:

`index = (number of outputs in existence - number of outputs in last 30 days) + (number of outputs in last 30 days) * ((random number between 0 and 1) ^ (1/8))`

Conclusion: Maybe push mixin a little higher since it's relatively cheap, and set it so that the ring size is an even number. Focus on advising users about when to churn, and don't ask them to make any decision about mixin.

## knaccc | 2017-02-09T00:39:20+00:00
Description of a potential privacy leak and recommendation to mitigate

3rd draft - February 2, 2017


--------
Abstract
--------

Consider the scenario where Alice will send funds to Bob on multiple occasions. 
This could be because Alice is an employer, a business partner, a friend or an 
exchange. Alice knows Bob's identity.

We demonstrate that if Bob makes multiple purchases from a vendor Charlie, and 
Charlie's wallet is ever exposed, Alice can easily see that Bob has been paying 
Charlie. The promise of untraceable payments is broken.

We show that Bob can regain his privacy by sending funds received from Alice 
back to himself several times before sending them to Charlie on each occasion. 
We refer to this as a 'churn'.

We use a simulation to demonstrate that a minimum of 7 churns would be required 
for Bob to regain his privacy.

We recommend a the introduction of a 'churn' wallet feature that will send a 
user's funds back to themselves with one click. 



--------
Scenario
--------

1. Alice knows Bob's identity, and pays him on multiple occasions. Alice 
therefore knows that certain outputs are now under Bob's control.

2. Bob purchases from Charlie on multiple occasions. Charlie does not know 
Bob's identity.

3. Charlie's wallet is exposed, perhaps due to a hacking incident. The outputs 
that Charlie has received are now known to Alice.

4. If Bob had only made one purchase with Charlie using funds originally 
received from Alice, then Alice cannot tell that Bob made a purchase from 
Charlie. Bob can claim the transaction was by someone else that had 
coincidentally included his input in the ring signature for that transaction.

5. Bob, however, made several purchases from Charlie. This means multiple 
transactions will exist with different outputs received from Alice as ring 
signature inputs in multiple transactions destined for Charlie. The probability 
that someone other than Bob had coincidentally used Bob's outputs in 
transactions with Charlie on multiple occasions is vanishingly small. Bob's 
payments to Charlie are therefore exposed to Alice.

In order for Bob to have privacy, Bob needs to be able to demonstrate that many 
other users could easily have had their inputs used for each of the many 
transactions Bob had with Charlie.

The only way for Bob to ensure this is to send the funds he receives from Alice 
to himself several times before then sending them to Charlie. We refer to this 
operation as a 'churn'. Let's assume all Monero users use a ring signature size 
of M. If Bob churns N times prior to sending funds to Charlie, he will ensure 
that the funds received from Alice are obfuscated within N^M possible inputs 
that could be the real source of funds sent to Charlie.

We will now use a simulation to demonstrate that N should be 7 or greater to 
provide Bob with privacy.



----------
Simulation
----------

At the time of writing, there are approximately 21 million outputs in existence 
on the blockchain. We use a Zipf power law distribution to distribute between 1 
and 1000 outputs to a set of simulated users.

The simulation shuffles the set of outputs and then determines how many outputs 
would have to be selected at random before more than 10 outputs are found to be 
owned by a single Monero user. This therefore tells us the minimum number of 
decoy outputs that Bob would need to hide his outputs within, if he'd made 
purchases on 10 different occasions. Because of the element of chance, we 
repeat the simulation 1000 times to determine an estimate for the minimum 
number of outputs Bob would require in the worst case and median scenarios.

The results of the simulation are as follows:

minimum: 26236
median: 54983
maximum: 72417

This means Bob should churn his funds at least 7 times to provide him with 
privacy, since 5^7 = 78125, which is higher than the worst case scenario 
simulated of 72417.

Remember that this simulation applies to the situation where Bob retrieves 
funds on 10 different occasions and spends them with the same merchant on 10 
different occasions. Bob would not need to churn at all if he'd purchased funds 
on just one occasion and then spent them on 10 different occasions.

If we reduce the number of purchases from 10 to 3, then the simulation results 
are as follows:

minimum: 79
median: 1958
maximum: 4258

This means Bob only needs to churn a minimum of 6 times to protect his privacy.

Note that the results depend on our choice of output-per-user distribution. To 
err on the side of caution, we'd recommend increasing the churn count beyond 
the minimum that our particular simulation would suggest. The maximum that 
could ever be necessary is for N^M to meet or exceed all outputs in existence. 
At the time of writing, that would mean 12 churn operations at most would ever 
be required.


    
----------
Conclusion
----------

Monero users should be educated that if they are using an exchange that knows 
their identity, and if privacy is of paramount concern, they should churn the 
funds they  receive from exchanges. Funds should also be churned prior to 
sending them back to an exchange to cash out.



--------------------------------------------------------------------------------
-----
Appendix A - Source code for simulation
--------------------------------------------------------------------------------
-----


```
import java.util.*;

public class TransactionDepthAnalysis {

  public static class ZipfGenerator {

     private double skew;
     private double bottom = 0;

     public ZipfGenerator(int size, double skew) {
      this.skew = skew;

      for(int i=1;i < size; i++) {
      this.bottom += (1/Math.pow(i, this.skew));
      }
     }

     public double getProbability(int rank) {
       return (1.0d / Math.pow(rank, this.skew)) / this.bottom;
     }
  }

  public static void main(String[] args) {

    int simulationIterations = 1000;
    int minOutputsPerUser = 1;
    int maxOutputsPerUser = 1000;
    int merchantPurchaseCount = 10;
    int totalOutputs = 21*1000*1000;
    double zipfDistributionPower = 1.3d;

    ZipfGenerator zipf = new ZipfGenerator(maxOutputsPerUser-minOutputsPerUser, 
zipfDistributionPower);

    int highestUserId = 0;

    List<Integer> outputs = new ArrayList<>(); // list of owners per output
    List<Integer> userOutputCounts = new ArrayList<>(); // list of user owned 
output counts

    double[] rankProb = new double[maxOutputsPerUser];
    for(int i=1; i<=maxOutputsPerUser; i++) rankProb[i-1]= 
zipf.getProbability(i);

    while(outputs.size()<totalOutputs) {
      double r = Math.random();
      double cumulativeProb = 0;
      int rank=0;
      while(cumulativeProb < r) {
        rank++;
        cumulativeProb+=rankProb[rank-1];
      }
      userOutputCounts.add(rank);

      int outputsForUser = minOutputsPerUser + rank;
      userOutputCounts.add(outputsForUser);
      int userId = highestUserId++;
      for(int i=0; i<outputsForUser; i++) outputs.add(userId);
    }

    Collections.sort(userOutputCounts);
    System.out.println("Zipf distribution power:" + zipfDistributionPower);
    System.out.println("Total outputs simulated: " + outputs.size());
    System.out.println("Total users simulated: " + userOutputCounts.size());
    System.out.println("Distribution of user owned output counts:");
    System.out.println("minimum: " + userOutputCounts.get(0));
    System.out.println("1st percentile: " + 
userOutputCounts.get((int)Math.round(userOutputCounts.size()*.01d)));
    System.out.println("5th percentile: " + 
userOutputCounts.get((int)Math.round(userOutputCounts.size()*.05d)));
    System.out.println("10th percentile: " + 
userOutputCounts.get((int)Math.round(userOutputCounts.size()*.10d)));
    System.out.println("median: " + 
userOutputCounts.get((int)Math.round(userOutputCounts.size()*.50d)));
    System.out.println("90th percentile: " + 
userOutputCounts.get((int)Math.round(userOutputCounts.size()*.90d)));
    System.out.println("95th percentile: " + 
userOutputCounts.get((int)Math.round(userOutputCounts.size()*.95d)));
    System.out.println("99th percentile: " + 
userOutputCounts.get((int)Math.round(userOutputCounts.size()*.99d)));
    System.out.println("maximum: " + 
userOutputCounts.get(userOutputCounts.size()-1));
    System.out.println("");

    List<Integer> minSelectionCounts = new ArrayList<>();
    for(int i=0; i<simulationIterations; i++) {
      int  minSelectionCount = getMinimumOutputSelectionsRequired(outputs, 
merchantPurchaseCount);
      minSelectionCounts.add(minSelectionCount);
    }
    Collections.sort(minSelectionCounts);
    System.out.println("Distribution of minimum selection counts required for 
privacy:");
    System.out.println("minimum: " + minSelectionCounts.get(0));
    System.out.println("median: " + 
minSelectionCounts.get(minSelectionCounts.size()/2));
    System.out.println("maximum: " + 
minSelectionCounts.get(minSelectionCounts.size()-1));
  }

  public static int getMinimumOutputSelectionsRequired(List<Integer> outputs, 
int merchantPurchaseCount) {

    Collections.shuffle(outputs);

    Map<Integer, Integer> userIdOutputCount = new HashMap<>();
    for(int i=0; i<outputs.size(); i++) {
      int userId = outputs.get(i);
      if(!userIdOutputCount.containsKey(userId)) userIdOutputCount.put(userId, 
1);
      else {
        int existingCount = userIdOutputCount.get(userId);
        int newCount = existingCount + 1;
        userIdOutputCount.put(userId, newCount);
        if(newCount>=merchantPurchaseCount) {
          return i;

        }
      }
    }
    throw new RuntimeException("This line should be unreachable");
  }

}
```


## olarks | 2017-02-09T04:39:50+00:00
@JollyMort wrote:
> Do you mean to say that, regardless of what the actual ring size is, you want to make it near certain that you can't ever eliminate all of the ring partners as being the fake ones, and would always remain with minimum of 4 for which you can never tell for sure?

Yeah this is what I would like to try to achieve here as a minimum assurance for users or very close to it.

## olarks | 2017-02-12T07:22:00+00:00
Ok, so to update on what is going on here. I am going to take @RandomRun's advice and see if there is a zipf distribution by surveying Bitcoin transactions using the blockchain.info api and try to figure out sagemath for making a graph. 

If a static ringsize is too extreme, then @moneromooo-monero's idea of having three valid ringsizes in the network is a good compromise imo. Possibly having the minimum ringsize not be the wallet default. Could be for example 6, 18, 75 or something similar.

## RandomRun | 2017-02-13T14:25:39+00:00
@olarks: Thanks for taking on the effort to find out Bitcoin's distribution, I am very curious to see what comes out of it!

I am figuring out Sagemath too, and how to plot some probability bar charts. I wrote the plotting code below adapting code from Sage Beginner's Guide, page 161 (pdf available online). (Also, hint: if you are calling Sage from the terminal, you might like to try: "sage -n jupyter", which opens sage in the nicer Jupyter interface.) 

Unfortunately at the time I only know how to print it to a picture file, but if you run the code below and open the picture, you can see the result of simulating the creation of a ring using my best interpretations of @moneromooo-monero's above description of the current output selection algorithm, with the real output being drawn according to a Zipf, and afterwards we check its position in the ring. The bar chart captures in a picture how likely the real output is to be in each position, according to age, 0 representing the most recent one.

As expected, with the Zipf assumption, it is overwhelmingly more likely that the real output will be in the first position, but also very likely it will be at the *i*th position, where *i* is the ringsize/4, i.e., after we are done choosing the recent decoys.

For convenience, I am making a table with a few results. (They are 1,000,000 trials in each scenario, and with the simplifying assumptions that: we have 34 months for the long term triangular distribution, and that each possible outcome is a 2-minute interval, which corresponds to one block, which in turn is viewed as a just one output.)

| Ringsize  |   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |   10   |   11   |   12   | 13 | 14 | 15 | 16 |
| ----------- | ------|-------|------|------|-------|------|-------|------|------|-------|-------|---------|--------|----|---|---|---|
| 4             | 61.99% | 20.86%|7.59%|4.61%| 4.95%  |
| 8             | 51.39% | 10.47%|16.43%|7.01%|3.94%|2.85%|2.36%|2.30%|3.25%|
| 12           |47.27%|8.19%|6.32%|13.94%|6.70%|3.80%|2.61%|2.08%|1.76%|1.61%|1.55%|1.64%|2.54%|
| 16           |44.85%|7.73%|4.58%|4.77%|12.10%|6.46%|3.70%|2.55%|1.97%|1.62%|1.40%|1.27%|1.19%|1.17%|1.18%|1.33%|2.12%|

I am looking forward to rerunning those simulations substituting the Zipf with Bitcoin's distribution when we have that!
_____________________________________
**Sage Code:**

```python
LongTerm = 34*30*24*30
ShortTerm = 5*24*30

trials = 1000000

ringsize = 12

Zipf  = GeneralDiscreteDistribution([1/i for i in range(1, LongTerm + 1)])
TriaL = GeneralDiscreteDistribution([1-i/LongTerm for i in range(LongTerm)])
TriaS = GeneralDiscreteDistribution([1-i/ShortTerm for i in range(ShortTerm)])

position = [0 for i in range(ringsize+1)]

for i in range(trials):
    
    num_rec = max(1, round(ringsize/4))

    Real = Zipf.get_random_element()

    if Real < ShortTerm:
        Set = set([Real])
    else:
        Set = set([Real])
        num_rec += 1

    #selecting recent decoys:

    while len(Set) < num_rec:
         Set.add(TriaS.get_random_element())

    #select old decoys:
    
    while len(Set) < ringsize + 1:
         Set.add(TriaL.get_random_element())

    Ring = sorted(list(Set))
    
    if len(Ring) < ringsize + 1:
        print "Fail", len(Ring)
    
    for i in range(ringsize+1):
        if Ring[i] == Real:
            position[i] += 1
            break

histogram = [float(item/trials) for item in position]
print histogram
```
```python
import numpy
import matplotlib.pyplot as plt

# Define experimental data
cluster1_data = numpy.array(histogram)
cluster1_x = numpy.array([i for i in range(len(histogram))])


# Plot
fig = plt.figure(figsize=(10,8))

# size in inches
plt.bar(cluster1_x, cluster1_data,  width=1.0, align='center', color='white', ecolor='black')
plt.ylabel('frequency')


# Label ticks on x axis
axes = fig.gca()
axes.set_xticks(cluster1_x)
axes.set_xticklabels([str(i) for i in range(len(histogram))])
plt.savefig('Bar_Chart.png')
plt.close()
```



## moneromooo-monero | 2017-02-13T19:56:38+00:00
Thanks, this is interesting. Especially the bump in probability at a quarter of ring size.

## kenshi84 | 2017-02-14T04:01:20+00:00
@moneromooo-monero https://github.com/monero-project/monero/issues/1673#issuecomment-278449820
> The best defense against this is to avoid having many inputs. In fact, maybe forcing all transactions to be 1 input and 2 outputs might be a good thing... ?

I believe we definitely need the ability to combine more than one inputs, otherwise amounts associated with individual outputs keep declining and users become unable to make big purchases. But forcing the number of inputs to be no more than 2 sounds not too crazy to me. Citing my own comment above: https://github.com/monero-project/monero/issues/1673#issuecomment-277847772

> If this kind of temporal alignment happens in a tx with many inputs, and especially if it happens for the ring members in the older time, then it becomes highly probable that those are the real spent outputs. knaccc expressed a similar concern on IRC. A possible remedy might be to artificially increase the chance of temporal alignments for even older outputs so that this kind of event is not too rare. I have no idea how to achieve that, though.

If the number of inputs was only two, the strategy I described here would be quite straightforward to implement. Let's take [this transaction](https://xmrchain.net/tx/08197da3dd5dbe93989e45baf9b7fca308f6bbc144f5f9fc5c3f6dda26eed10c) as an example. The second output in the first ring and the third output in the second ring are quite close to each other, which might suggest they are the real outputs. The confidence will become larger if this kind of temporal closeness happens to even older outputs.

```
|_*____________________________________*________________________*_______________________*|
|________*____*_________________________*____________________________________________*___|
```

What if we modify the algorithm so that the two rings look like this:

```
|__*__________*________________________*________________________________________________*|
|_*___________*_________________________*______________________________________________*_|
```

If the real outputs are not so aligned, for example in [this tx](https://xmrchain.net/tx/bfb5e011916817c8df7e794e71e247741f135685846d998d0fb00833132cd6c5) where I denote the hypothetical real outputs by `x`:
```
|_*_______________*_______________________*____________________________x________________|
|_______________________*_____________________________________x____________*___________*|
```
the modified algorithm would make the two rings like this:
```
|_*___________________________________________________________*________x_______________*|
|__*__________________________________________________________x_________*______________*|
```
Maybe I'm making total nonsense here, but I just wanted to get my thought out :P


## kenshi84 | 2017-02-14T07:46:18+00:00
Let me add a bit more to my above (possibly nonsense) idea: let's say you want to spend two outputs from recent days that are e.g. 20 days apart:
```
|____________________________________________________________________________________x__|
|_________________________________________________________________________________x_____|
```
Then the modified algorithm would generate two rings (with ringsize 4) like:
```
|_______*___________________________________________*_____________________________*__x__|
|____*____________________________________________*______________________________x___*__|
```
But if these outputs were from very old time and apart from each other by 20 days, it would NOT be OK to create rings like:
```
|__*__x__________________________________________________________*_____________________*|
|_x___*________________________________________________________*_______________________*|
```
because older outputs are supposed to be chosen much less frequently than newer outputs. IMO, the notion of 'temporal alignment' should be less strict for older outputs and more strict for newer outputs, thus the algorithm should create rings like
```
|_____x________________________*_________________________________*_____________________*|
|_x_______________________________*____________________________*_______________________*|
```
The degree of temporal alignment of each pair of corresponding ring members would be randomized following some distribution.

## iamsmooth | 2017-02-18T07:42:54+00:00
> I believe we definitely need the ability to combine more than one inputs, otherwise amounts associated with individual outputs keep declining and users become unable to make big purchases. 

Yes this is right and in fact it is perhaps a good idea to prefer to use 2 inputs rather than 1, because otherwise, with frequent uses of 1 input the change outputs will get smaller and you will end up with a sequence like this, even if all transactions spend the same amount:

1
1
1
1
1
1
6

The transaction with 6 inputs likely presents more association issues than would this:

2
2
2
2
2
2
2

and the two sequences are comparable in total size.

However, the conjecture that the form is preferable in terms of associations is unproven and could be wrong. Clearly the 1-input transactions are the ideal case interns of associations between inputs and provide (absent other problems) statistically ideal untraceability, so perhaps N-1 transactions with "ideal" untraceability and one with poor untraceability is better than N transactions with only slightly degraded untraceability.

One approach (which also addresses other issues) would be to feed change back into a separate pool which is then recombined (with reasonable time delays) back to yourself as a single 6 -> 1 transaction (where degraded untraceabiltity is accepted) before being reused as as a larger input for a 1-input spend transaction. This is essentially a limited form of 'churn', designed to combine change outputs into a larger, more-usable form (and also to ensure at least one strong-untraceable step between change created by a wallet and another transaction from that wallet that spends it)

## moneromooo-monero | 2017-02-18T10:04:12+00:00
If a single input was to be used, there would not necessarily be a change output. In the case where you'd need, eg, 5 inputs and 2 outputs, you could send 1/1, 1/1, 1/1, and 2/2. You pay more in fees though, due to the extra number of outputs.

## iamsmooth | 2017-02-19T00:35:37+00:00
sure sending separate transactions is an option but there are at least three issues with it  (besides potentially cost, which you mentioned):

1. it is kicking the can. the recipient ends up with smaller outputs. if people keep splitting (sometimes) without combining, then there is still sooner or later going to end up being more combining to be done (somewhere, by someone)

2. the recipient always knows the transactions are related, so can uses this to perform time correlations,etc. on the inputs. there is only a privacy advantage (over many inputs in one tx) with respect to third parties.

3. slower, due to the need to send multiple tx and introduce some delays to prevent the obvious timing attack.

## moneromooo-monero | 2017-02-19T09:31:34+00:00
1 is true, but lessens the number of places such linkage will be done, which should be good for privacy
2 is an unfair criticism, since the recipient would also know it without this change.
3 is true, but it could be optional (it is in my code)

## iamsmooth | 2017-02-19T22:22:02+00:00
1. is incorrect. Once the outputs are combined once then the issue no longer occurs on subsequent transfers which would use a smaller number of larger-valued inputs. By kicking the can, there is either linkages in one spot (when the are eventually combined) which is the same, or linkages in multiple spots (if timing or other analysis is able to connect the pieces, or by recipients performing the linkages) which is worse.

2. See 1) above. If this is done multiple times, then multiple recipients learn of these linkages, which is worse than just combining the outputs once (especially if sent back to yourself which means no recipient learns anything). Viewed at the system-wide level, this is a symptom of outputs becoming smaller and smaller, which in turn is a consequence of an imbalance between splitting and combining. Passing them along as-is rather than combining them means the next recipient continues to experience the same issue.

3. Optional is okay, but what is the benefit here if the transaction is slower, and the fees higher?

## olarks | 2017-02-24T09:04:24+00:00
Ok everyone I have finally gotten around to surveying the Bitcoin blockchain for the age of spent outputs in transactions. I am currently trying to get sagemath to write points to a static graph file so I can just keep adding more data without having to start over, but for the meantime I have surveyed 37517 bitcoin transactions consisting of 74947 spent outputs and I have categorized the age of spent outputs separately by the last day, week, month, year, and beyond.

| Last Day | Last Week | Last Month | Last Year | 1 Year < |
| ---- | ---- | ---- | ---- | ---- |
| 71% | 13% | 5% | 8% | 1% |

Due to minor rounding errors in the number of spent outputs older than a year the real percentage would be roughly 1-3% of spent outputs.

Interestingly enough 43% of outputs spent in the last day were actually less than an hour old. I removed that stat metric so things are less convoluted, but feel free to put it back in if you like.

I think this data is pretty indicative of the trend in age of spent outputs but I would like to gather a lot more transaction data because this data consisted of only 15 blocks worth of transactions.

Occasionally the api throws errors which can be kind of frustrating, but for the most part it is pretty stable. Feel free to play around with the code and add any metrics you may think are useful.

```python
import json
import urllib2

target_blocks = 1 # number of blocks to parse
block_count = 0
current_hash = urllib2.urlopen('https://blockchain.info/q/latesthash').read()
blockheight = int(urllib2.urlopen('https://blockchain.info/q/getblockcount').read())

# variables used for gathering basic stats
num_inputs = 0
num_transactions = 0
last_day = 0.0
last_week = 0.0
last_month = 0.0
last_year = 0.0
old = 0.0

while block_count != target_blocks:
    block_data = json.loads(urllib2.urlopen('https://blockchain.info/block/%s?format=json' % str(current_hash)).read())
    transaction_count = block_data['n_tx']

    i = 0
    while i != transaction_count - 1:
        i += 1 # skip coinbase tx
        transaction_input_count = block_data['tx'][i]['vin_sz']
        num_transactions += 1

        j = 0
        while j != transaction_input_count:
            input_transaction_index = block_data['tx'][i]['inputs'][j]['prev_out']['tx_index']
            input_data = json.loads(urllib2.urlopen('https://blockchain.info/tx-index/%s?format=json' % str(input_transaction_index)).read())
            input_age = input_data['block_height']
            # plot the points on the graph here with sage
            j += 1
            num_inputs += 1

            if 144 >= (blockheight - input_age):
                last_day += 1
            elif 1008 >= (blockheight - input_age) > 144:
                last_week += 1
            elif 4320 >= (blockheight - input_age) > 1008:
                last_month += 1
            elif 51840 >= (blockheight - input_age) > 4320:
                last_year += 1
            elif (blockheight - input_age) > 51840:
                old += 1

    current_hash = block_data['prev_block']
    block_count += 1

print "\nNumber of spent inputs: %i" % num_inputs
print "\nNumber of transactions: %i" % num_transactions
print "\nSpent inputs in the past day: %i%%" % ((last_day / num_inputs) * 100)
print "\nSpent inputs in the past week: %i%%" % ((last_week / num_inputs) * 100)
print "\nSpent inputs in the past month: %i%%" % ((last_month / num_inputs) * 100)
print "\nSpent inputs in the past year: %i%%" % ((last_year / num_inputs) * 100)
print "\nSpent inputs older than a year: %i%%" % ((old / num_inputs) * 100)
```

## moneromooo-monero | 2017-02-24T09:09:02+00:00
"Interestingly enough 43% of outputs spent in the last day were actually less than an hour old."

That could be because people are trying to mix coins for anonymity :)

## iamsmooth | 2017-02-24T09:18:53+00:00
I did the same analysis on Bitcoin a year or two ago and got similar results. In fact, I found that a significant fraction of outputs were being spent in the same block. I also found that the mean age was around 7 days but the median obviously is much lower.

We can't assume that Monero usage is the same for various reasons (including technical differences such as the impossibility of spending unconfirmed outputs) but also differences in usage (@moneromooo-monero is probably correct that some of it is based on mixing!) and also business processes that are likely different even for similar usages, but it is interesting data nevertheless and certainly somewhat relevant.

@olarks I just glanced at your code and I noticed using blockchain.info. I tried them and a couple of other services and I found using foreign APIs for this to be a pain since they end up throttling or banning for too many calls. I ended up using Bitcoin Core with REST enabled so I could do all the queries locally. That was much faster and avoided excess use issues.

## iamsmooth | 2017-02-24T09:31:44+00:00
Also I agree that using some distribution closer to this data (with a much higher probability of fake outputs chosen from recent sources) would be an improvement (most likely a large one) over the lifetime-triangular distribution that is (with modification) used now. The triangular distribution was added much earlier as a replacement for uniform and we understood at the time that over time it would become less and less effective.


## olarks | 2017-02-24T10:08:09+00:00
@iamsmooth Yeah I had a couple run-ins with the api booting me for too many queries, but as long as I took breaks every couple hours it wasn't too bad. The replacement output selection algorithm would need a ringsize large enough to both largely obscure recently spent outputs(the vast majority of transactions) and have enough trailing fakes for older spent outputs to not look out of place since older outputs being spent are not very common anyway.

I have been thinking having only one static ringsize may be a bit too limiting for users. I have been favoring @moneromooo-monero's idea of having 3 static ringsizes users can choose from so they are still protected from picking irregular ringsizes, but can choose a default strong option, a very strong option, or paranoid option for their transactions. I had mentioned 6, 18, and 75 being a possible option for the static ringsizes because 6 is only a marginal increase from 4, so very little performance is being lost and having 6 fake outputs to work with, at minimum, for designing an output selection algorithm should give us enough leg room to strongly obscure all transactions with varying spent output ages.

What do you think about this @iamsmooth?

## iamsmooth | 2017-02-24T12:41:26+00:00
@olarks regarding your first paragraph, i don't think anything special is needed if you get the fake output selection right. Yes older spent outputs will come up occasionally and may "look out of place" but with the right fake output selection older fake outputs will come up occasionally as well. If you see a transaction with one output being old, is that real or fake? With a decent fake output distribution, there is really no way to tell, and that's precisely the goal.

I think it will be very interesting to plug in something like a reasonable Zipf distribution and take a look at the resulting rings. I think we'll be surprised to see that very little ever actually stands out (unlike now).

Regarding ring sizes, I think once you realize that good fake output selection solves the problem without needing to arbitrarily decide on and stuff ranges (and arguably does so better in some models) you don't need to be too concerned about ring size. Its really more of a space/ambiguity tradeoff and there isn't a clear answer.

The more interesting questions to me were the ones about multiple inputs.

Regarding the APIs, if you want to analyze more data, using the APIs will get tedious. I think I managed to process a whole year of BTC transactions (though it might only have been six months, I don't remember). Although probably unnecessary to get a reasonable picture, good luck trying to do that through a public API.

## olarks | 2017-02-24T16:27:32+00:00
@iamsmooth I guess my main concern with not having a large enough ringsize is there not being enough commotion and doubt in the ring signature which could enable statistical analysis to more easily determine the real spend. 

Now this would depend on the results of what a zipf distribution would look like, but in addition to that I can't foresee an output selection algorithm paired with a small ringsize be enough because if you only have 4 fakes to use and have 2 of them be used for recent outputs and 2 for trailing outputs this does not give a lot deniability to either recent or old outputs. Not having enough fake outputs chosen randomly in the selection makes it more predictable because we would know for example if there is only two recent outputs in a ring then the real spend is one of the three other outputs in the ring which is pretty poor deniability between yourself and two others imo.

One thing I wanted to bring up that is enabled with a ringsize 6 but not with ringsize 4, because there are not enough fakes to utilize, is you can have 0-1 random outputs be selected in the most recent portion of the algorithm with two extra recent outputs selected and 3 trailing outputs be selected if the the variable output is a 0 then it gets added as an extra trailing output instead of a recent one.

This selection is very intriguing because for analysis if the real spend is not recent and the variable output is selected to be an extra recent output it would appear that the real spend is one of the recent outputs in the ring but an observer would not know if the random variable output was selected to be a recent output or a trailing one. Even if the real spend was recent it at least bolsters the real spend's obfuscation with 4 other fake recent outputs. And vice versa with having the real spend be recent but the random variable output be selected for a trail output which could also look like a potential spend is in the trail, but again an observer does not know the result of the random variable output.

I just wanted to mention that option because honestly it is nearly impossible to deduct if a real spend is recent or trailing based on the secret result of the random variable output and does not require much of a bump in mandatory ringsize for the network to become feasible as an algorithm by taking advantage of the fact most spent outputs are recent, this adds a great deal of question into analysis.

I am glad to hear any possibilities for alternative selections with only 4 fake outputs but the algorithm is run very thin to provide good obfuscation for both recent and old outputs.

Funny you mention the APIs being tedious because I can only parse roughly 3-4 inputs a second through it and it took me about 5 and half hours to complete my results I posted. The first time resulting in an API error about half way through haha. I will try to spin up a Bitcoin node for future surveying so I don't have to deal with that :)



## iamsmooth | 2017-02-24T20:18:28+00:00
@olarks You are still stuck on this idea of having recent outputs and trailing outputs. There really isn't any such thing; the distribution is continuous, and to the extent it even has meaningful regions, it doesn't necessarily have only two. The recent/trailing distinction is needed (or at least, is used) now as a result of the poor fake output selection which otherwise chooses much too many trailing outputs (and increasingly so over time). Doing things that way actually introduces other problems. Getting the fake output selection right is better.

> not being enough commotion and doubt in the ring signature which could enable statistical analysis to more easily determine the real spend.

This is always going to be the case with a smaller number. 5 has less obfuscation than 10 which has less than 100. The trade off is against size, processing cost, and reduced transaction flow due to those higher costs. There is also another tradeoff against using multiple (smaller) sequential transactions with greater fan out relative to signature size (though adding a time cost). So bigger certainly adds obfuscation at the individual transaction level but beyond that the tradeoffs are much less clear.


## olarks | 2017-02-26T10:03:29+00:00
I see what you mean now @iamsmooth. I have actually been toying around with an idea where output selection is similar to going through "gauntlets", where a random number needs to consecutively meet certain parameters with decreasing probability to determining the age of an output selected for a ring signature. My original concept was for 1/2 chances for an output to be defined within the last day, if this check returns true then program control would carry onto the next gauntlet where a random number has a 1/4 chance to selected in the last week and if it fails it would just return the previous gauntlet selecting, for this example, an output in the last day. Otherwise program control would proceed to the next gauntlet, if successful and so on. These odds look like 1/8 outputs would be in the last week, 1/16 outputs would be from the last month and so on for selecting outputs in the last year and beyond.

I figured it would be a lot simpler to scrap the "gauntlets" and just average these probabilities over the range 0-100 for random numbers falling in the defined ranges for selecting outputs and coincidentally the distribution is very similar to what the results of my Bitcoin survey returned. On average, 68/100 outputs would be selected from the past day, 17/100 outputs would be from the past week, 8/100 outputs would be from the past month, 5/100 outputs would be from the last year, and 2/100 outputs would be older than a year.

This would allow for older outputs to be chosen on occasion closely resembling the probability of a real output with that age being spent. There is no defined number of "recent" or "trailing" outputs in the algorithm, which solves problems you had with explicitly defining x number of outputs being "recent" and y number of outputs being "trailing". 

I feel like this is more on track with what we would want from a selection algorithm because the ringsize is less important since outputs with all ages would still appear on occasion all appearing equaprobable to their likeliness of actually appearing in a transaction. Finally the output selection isn't a product of what ringsize is being used because the output selection itself should be good enough in itself and can be dynamic enough to be used for any ringsize. Through more bitcoin transaction surveying we can refine what these values should be.

I still favor bumping the mandatory ringsize from 4 to 6(?) for more raw input going through the selection algorithm to take advantage of optimizations in transaction size provided by ringct. However this is the first selection algorithm I feel comfortable with using ringsize 4 with and am not against keeping it at 4 if there is no consensus to raise it because like you say it is difficult to quantify how much extra benefit there is by increasing the ringsize.

I will, over the coming weeks and months, continue to survey Bitcoin transactions to gather a larger data set for narrowing down what probabilities we should be using, till we figure out exactly what to do.

## olarks | 2017-04-16T00:10:09+00:00
Hello everyone, it has been a while since I have made an update on the progress of this issue and a recent paper was released that is somewhat related to the discussion here. For those interested the paper is at https://monerolink.com/monerolink.pdf. The paper does not reveal any new discoveries that
we were not already aware of and while a large portion of the paper does not apply to the Monero network anymore the discussion of age distributions on outputs in ring signatures still definitely applies and is what helped inspire the creation of this issue in the first place.

It is nice to see other people take an interest in this and come to a similar conclusion as discussed in this thread. It would be nice to see the simulation code they used to come to their conclusions to play with, but that is up to the authors of the paper.

As discussed in the previous irc [meeting](https://monerobase.com/wiki/DevMeeting_2017-04-09) the output selection algorithm I am proposing based on the age of spent outputs in bitcoin transactions should probably be written for the MRL, but just to briefly touch on some challenges this output selection will face I figured I should briefly explain a bit more.

My surveying of the Bitcoin blockchain is still progressing and I would like to bring up some issues that will need addressing since there is a large bias towards outputs being spent in the past day which will impact output selection. Particularly the attack that is described in MRL-001 changes because an adversary would not need to control a large amount of outputs on the entire blockchain, they would only need to control a large number of outputs in the past day and to a lesser extent the last week and month to reliably unmask the real spent output in a ring signature with reasonable success, assuming a transaction is using 4 decoy outputs in a ring signature.

With approximately 3000 daily transactions present on the network, the increased blocksize from our v5 hardfork, and reduced transaction fees this attack is much cheaper and less complex to mount because there is not enough real demand in the network currently to combat this.

If we assume, for simplicity's sake, these 3000 daily transactions on average are 13kb in size, 1 input / 2 outputs, then currently only 20% of the daily blocksize capacity is being used. According to monero.how the new cheap transaction fees are roughly $0.08. To control 80% of outputs in the past day(13600 2 output / 1 input transactions) without going over the 300kb minimum for the dynamic blocksize then this costs $1100 a day to sustain. With, for example, a 70% chance the output selection algorithm chooses an output from the past day then a transaction has a 24% chance all 4 decoys will be selected from the past day. The probability all 4 of those chosen outputs are controlled by an adversary with 80% of outputs of the past day is 41%. An attacker would be able to unmask the spent output in 10% of all transactions with 4 decoys in their ring signatures.

Since this attack needs 4x the number of transactions to be present in the network to reliably execute then this attack would be trivial to spot such a sudden large uptick in transaction volume, but it would be better to make this attack not worth it in the first place. To combat this the minimum ringsize would need to be increased to reduce the probability for spent outputs being unmasked as illustrated above. Mandatory ringsize of 12(+1) would give an attacker a 0.1% probability to unmask the spend of a ring signature with 12 decoy outputs. Paranoid users would still be able to increase the ringsize if they don't want to take the 0.1% chance their spent output is revealed to such an attacker.

I want to emphasize this increased minimum ringsize would only be a temporary measure in response to minimizing this attack until transaction volume increases and sustains itself over time so this attack is less realistic because it is only inexpensive and simple now because blocks are much larger without enough demand to accompany the increase. Regular monitoring of transaction volume in the network and determining if it is an organic increase will be required. A dedicated adversary would slowly ramp up this attack over months so it looks natural attempting to feign real network activity. It will require an extremely conservative approach to slowly reduce the mandatory ringsize as transaction volumes increase so we do not expose the network to this currently inexpensive attack for an adversary with a moderate budget.

The attack gets worse the longer it is sustained as the attacker-owned outputs begin to be selected for decoys for the past week, month, and year etc. I will only cover outputs being selected from the past day for now because I think it alone expresses the importance of this problem and will leave the rest for future considerations like when more network activity is present and the dynamic blocksize comes into play etc.

We will need to agree on what ringsize is reasonable such that spent outputs cannot be easily unmasked under this attack whether this is 1 / 1000 transactions or more etc. We will need to choose an acceptable ringsize because this attack will always exist in some fashion, we just need to find a balance where the pay off is not worth the cost for an attacker. Ringsize 12(+1) seems like a reasonable option with 1 / 1000 transactions being unmasked seems hardly worth it for an attacker. Ringsize 8(+1) having 1 / 100 transactions being unmasked, ringsize 10(+1) having 1 / 300 transactions being unmasked, ringsize 16(+1) having 1 / 10000 transactions being unmasked and so on, all assuming an adversary controls 80% of outputs in the past day.

This attack will be present in any output selection algorithm with very strong bias for recent outputs where it is easier for an adversary to control outputs in a small timespan and the degree of success varies on how much transaction volume is in the network and the amount of unused space in blocks for exploitation, so it is paramount this gets figured out.

Till next time.

## knaccc | 2017-04-16T00:48:19+00:00
I just fired up my GUI to cost a transaction, and it says ring size 26 only costs 10.6 cents vs 9.3 cents for default ring size 5.

This is probably due to luck with the way my transaction size hits the KB barriers, since I think fees are based in increments of KB instead of increments of bytes. I wouldn't blink an eye if the minimum enforced ring size moved to 26. Makes churn less time consuming too.

## olarks | 2017-04-16T00:53:45+00:00
@knaccc, The issue with larger ringsizes is when more inputs and outputs are involved then the size of the transaction escalates rather quickly. Normal 1 input / 2 output transactions can have quite large ringsizes with minimal increases in transaction size and fees.

## iamsmooth | 2017-04-16T08:38:23+00:00
> We will need to choose an acceptable ringsize because this attack will always exist in some fashion, we just need to find a balance where the pay off is not worth the cost for an attacker.

Well in my view, the balance is up to the person making the transaction. That's the person paying the cost, and is the person gaining the benefit (as long as amplification doesn't occur; see below). 

As you say the attack will always exist in some form. The issue raised with MRL-0001 is amplification, which doesn't occur as long as the minimum ring size is large enough (roughly >2 but some extra safety margin in reasonable, but by the time you get to say 5, amplification is absolutely negligible). 

The reason being that unmasking say 1/100 or even 1/10 (or even a bit more) transactions does not give the attacker any significant amplification. They get the knowledge of their own transactions (which is always going to be the case), and for example a relatively modest 10% more, but that's it.

> Ringsize 12(+1) seems like a reasonable option with 1 / 1000 transactions being unmasked seems hardly worth it for an attacker. Ringsize 8(+1) having 1 / 100 transactions being unmasked, ringsize 10(+1) having 1 / 300 transactions being unmasked, ringsize 16(+1) having 1 / 10000 transactions being unmasked and so on, all assuming an adversary controls 80% of outputs in the past day.

These numbers are wrong assuming the attacker controls 80% and looking at the real numbers suggests why this approach of just requiring people make the rings bigger is not particularly useful.

With an attacker controlling 80%, 12+1 gives an attacker 6.9% success rate (0.8^12). With 16+1 the attacker's success rate is still 2.8% (0.8^16). 

These numbers are extremely high simply because defending strongly against an 80% sybil attack in this manner is extremely hard, to the point where it really isn't feasible to do at all by just taking the brute force approach of "Make all the rings bigger!" (unless we make them _much_ bigger, which I would argue is not feasible at all, not only for size reasons but also significantly increased computational cost).

Conversely, if we give the attacker a smaller share, say 20%, then even much smaller rings become quite strong. 4+1 gives the attacker only a 0.16% success rate. Obviously the others are to the point of being quite negligible.

I'm all for adjusting the defaults a bit, and maybe the defaults can even adjust depending on the number of inputs to balance against cost (say 10 on transactions with only 1-2 inputs but 5 on transactions with more inputs). But I do not see a justification for placing higher mandates on people who really just want to transact with reasonable privacy at modest cost, _as long as it doesn't lead to significant chain reaction effects_ that harm others. 0.16% risk of tracing (which doesn't necessarily give the attacker any useful info anyway) on a 4+1 against a 20% sybil attacker, may be quite acceptable for someone who is just doing a routine payment.

EDIT: I just realized you are assuming that only 24% that all the fake outputs are chosen from the last day (assuming 4, obviously the number decreases with more fake outputs. This is why your numbers are much lower. However, I find this quite unrealistic. An algorithm that chooses 70% from the last day will choose a much higher percentage from the past few days. So an attacker with 80% over just a few days is going to get a much higher success rate. A high degree of safety against an attacker who happens to persist for only one day is not particularly meaningful. (In practice, such an attacker may well persistent indefinitely since they will have increasing success by doing so.)

However, based on the data in the paper your estimate is also overly pessimistic in a sense. Their data show only about 30% are spent within a day (11.36 on the graph), which would mean 4 fake outputs within the past day only 0.81% of the time (again obviously becomes negligible quite quickly at the higher numbers).

## iamsmooth | 2017-04-16T08:43:53+00:00
BTW, with regard to surveying the Bitcoin blockchain, the results in the monerolink paper are quite interesting in one regard. They show a big difference in outputs that are respent in less than 20-30 minutes (Figure 10; 7.5 on the horizontal axis is approximately 30 minutes). This is obvious with a bit of thought, of course, as Bitcoin allows outputs to be spent immediately (and in fact many are spent in the same block), but Monero requires a minimum of 10 confirmations before outputs can be respect. The authors of the paper seem not to have identified the reason for the difference, but took note of it.

However, it does illustrate that on the low end we have to be very careful if applying Bitcoin data. Beyond that the overall behavior in two coins appears reasonably similar.

## olarks | 2017-04-16T17:19:50+00:00
> Well in my view, the balance is up to the person making the transaction. That's the person paying the cost, and is the person gaining the benefit (as long as amplification doesn't occur; see below).

I agree, I just figured since the average user may not be aware of this and we should to try to mitigate this but ultimately it is the user's responsibility to protect himself.

> (...) it really isn't feasible to do at all by just taking the brute force approach of "Make all the rings bigger!" (unless we make them much bigger, which I would argue is not feasible at all, not only for size reasons but also significantly increased computational cost).

Absolutely. There is a fine balance here but even if we did increase the ringsizes it would only be a temporary answer till network activity grows to better fill the new enlarged blocks.

> EDIT: I just realized you are assuming that only 24% that all the fake outputs are chosen from the last day (assuming 4, obviously the number decreases with more fake outputs. This is why your numbers are much lower. However, I find this quite unrealistic. An algorithm that chooses 70% from the last day will choose a much higher percentage from the past few days. So an attacker with 80% over just a few days is going to get a much higher success rate. A high degree of safety against an attacker who happens to persist for only one day is not particularly meaningful. (In practice, such an attacker may well persistent indefinitely since they will have increasing success by doing so.)

Yeah I purposefully did not do the calculations for when the attacker outputs begin to be chosen for selection past a day because it complicates things a bit but definitely amplifies the attack significantly when nearly 90% of outputs selected will be from the past day, week, and month.

> However, based on the data in the paper your estimate is also overly pessimistic in a sense. Their data show only about 30% are spent within a day (11.36 on the graph), which would mean 4 fake outputs within the past day only 0.81% of the time (again obviously becomes negligible quite quickly at the higher numbers).

The number 70% for the past day only comes from the bitcoin blockchain survey. It hovers between 68-72% or so. 

> However, it does illustrate that on the low end we have to be very careful if applying Bitcoin data. Beyond that the overall behavior in two coins appears reasonably similar.

The general trend of the age of spent outputs is definitely useful. Slight tweaking to take into account slight differences in Monero like the 10 block wait time you mention is important to note.

As suggested by others on irc I will get to surveying Bitcoin in 2011 and 2012 to see if there are any differences that we might want to take into account when Bitcoin was still young that could apply to Monero considering the network is still young.

## GitHayden | 2017-04-20T07:56:39+00:00
Hey all, this was posted on reddit, but ant-n suggested it should be posted here...

"Can we use/enforce fibbonachi numbers as ringsizes? 1, 2, 3, 5, 8, 13, 21, 34, ... This would reduce the set to choose from greatly, and allow continuously growing mixins through time."

Keep up the great work everyone
Gh



## dnaleor | 2017-04-20T12:06:50+00:00
what about a simple exponential approach?
(5,) 10, 20, 40, 80, 160, 320, 640, 1280, ...

Having no upper limit doesn't really matter, as it'll become very expensive very quickly to consistently transact with ring size 1280

edit: Not even sure if 1280 would even fit in the current blocks ;)

## hyc | 2017-04-20T12:15:04+00:00
The specific size chosen is really secondary to using a better selection algorithm. Although obviously at ridiculously large sizes distribution becomes less important, it'd be better if we can avoid the excessive size and cost.

## Gingeropolous | 2017-04-21T04:01:36+00:00
It seems that 1280 does fit in the current blocks, if you have only one input. 

http://moneroblocks.info/search/1c51a4a70873fae13695fd9a0fd7127a3e9b5b9c771def7c3740b23a7ec4ccb5



## perl5577 | 2017-04-21T05:57:30+00:00
Only if you spend one input.
How much input spent in average ? And not speak fee for make TX





## RandomRun | 2017-04-22T22:13:41+00:00
@kenshi84: Has there been any follow up on your idea to increase temporal alignment within ring members of different rings used in the same transaction expressed [here](https://github.com/monero-project/monero/issues/1673#issuecomment-279601931)? I would love to see more discussion on the topic, but I do think that that makes a lot of sense.

With respect to what is meant by two outputs being "close" or "far" from each other, I wonder if we couldn't use the following notion: 

Let `a` and `b` be the ages of two outputs `A` and `B`, and let CDF(x) represent the cumulative distribution function of their ages (for now we can imagine that is the distribution described in the monerolink paper, but it can be whatever is our best guess at the time being actually used to pick the decoys in the wallet software). We define `d(A,B) := |CDF(a) - CDF(b)|`. (This is the area under the PDF between the ages of `A` and `B`, and it gets smaller as their ages increase.)

This seems like a natural way to express how rare it is to see a pair of outputs "like `(A,B)`" being randomly sampled from the distribution. That distance could be used to pick the temporally aligned decoys withing the "right" range.

Also, optionally, the wallet could let the paranoid user know when some of their outputs are "too close" to each other, giving them the chance to sweep them individually, so that they would be transformed into newer (more distant) outputs before finally being used in the same transaction. For instance, the user could set that if the distance is smaller than say 1/10000 (made up number, not a suggestion), then they would like to recycle the output(s) by sweeping it/them, whereas the non-paranoid user may be fine with their outputs being at a shorter distance, say up to 1/100000.



## JollyMort | 2017-06-21T20:36:52+00:00
Here's a proposal which I believe has merit: https://medium.com/@jumpingjack/monero-input-collection-algorithm-idea-a7df6bd61f8b [link to reddit post](https://www.reddit.com/r/Monero/comments/6inggt/an_idea_to_decrease_linkability_between/)

Would be great to combine it with some number of randomly picked points on the blockchain and "spray" around those as well. This way you get multiple possible timeframes, and for each possible timeframe multiple possible outputs.

Edit also gonna quote myself from a previous [discussion](https://www.reddit.com/r/Monero/comments/6duun2/nonscientific_survey_minimum_of_ring_signatures/?utm_content=title&utm_medium=front&utm_source=reddit&utm_name=Monero) on redderp, because why not :)

>I'd like at least 15, divided into groups of 5, and those 5 "shotgun sprayed" around the real one, and other 2 groups "shotgun sprayed" around some 2 random points on the blockchain, at least one being close to the tip of blockchain. Something like that.
>We often hear "timing makes the most recent stand out", well, what if you pick at least 4 decoys from last 20 blocks or so, who can tell which one is yours if they all have nearly the same height? This would also increase chances of yours getting picked up by someone else, so the "live tip" would be completely scrambled at all times :)

## knaccc | 2017-06-21T23:45:48+00:00
> Here's a proposal which I believe has merit: https://medium.com/@jumpingjack/monero-input-collection-algorithm-idea-a7df6bd61f8b link to reddit post

I like this approach because it provides much better cover for a chain of churn transactions, which may otherwise stick out on the blockchain. If the output of a churn suspiciously keeps getting picked up as a ring member 10x in a row, the churn could be detected without something similar to this clustering proposal.

## JollyMort | 2017-06-22T09:10:35+00:00
If 1 cluster is always picked somewhere at the tip of the blockchain then you will pick up someone's fresh outputs and someone will "always" pick up your newly created one, likely more than once. The tip would be scrambled all the time effectively leaving a beautiful non-analyzable entangled mess behind as it fades into history. Maybe other outputs don't even have to be clusters, but just uniformly randomly picked 1 by 1 from historical blockchain.

## iamsmooth | 2017-06-22T10:31:48+00:00
@JollyMort that is already essentially exactly what we are doing (and indeed what would also  happen if we just picked outputs according to a reasonable usage-based distribution such as the one in the monerolink paper). Currently half of outputs are chosen from the most recent 1.8 days, and those are chosen with a triangular distribution so it actually clusters somewhat newer than that in practice (3/4 within the more recent 0.9 days I think). With everyone doing this, every, or very nearly every, fresh output is going to be picked up at least once if not multiple times before it gets old.

Regarding the specific clustering proposal, I haven't analyzed it carefully but it concerns me that it doesn't look at systemic effects and focuses narrowly (as do some of the earlier comments in this issue) on one particular spend transaction. In fact, transactions also provide cover for each other, as they spend each others outputs, as suggested in your last reply. Those effects also need to be considered carefully. We can easily see that in the ideal case of one-input transactions and perfectly matching the fake output distribution to the real output distribution, both same-transaction hiding and other-transaction cover are highly effective, but for other approaches (and also considering non-ideal cases) both issues would need to be looked at very carefully.

Anyway, I was kind of wanting to get back to the title of this issue, which was raising the size for September (which is getting closer!). The minimum size will already increase to 5 from 3. The question is whether it is necessary and useful to increase the minimum size even more than that, considering the corresponding increase in tx size.

One interesting point I'd make is that unlike increasing one _individual_ tx size, increasing _everyone's_ tx size does not increase the tx fees under the current dynamic fee formula. This is because on average the block size will grow by the same ratio, and the tx fees will therefore fall by that ratio, with the fee for each (now-larger) transaction remaining the same. This seems kind of bad to me, although you could argue (and I guess that would be the point of this issue) that the higher system-wide processing costs are offset by improved system-wide privacy. Still it seems less than ideal that increasing costs have no offsetting increase in price to transmit those costs back to the demand side.

## knaccc | 2017-06-22T11:09:03+00:00
If the Eve->Alice->Bob->Eve attack possibility is nonsense, then no increase is needed from that perspective.

If it is a real problem, then I'd vote for a ring size of 20 so that mitigating the attack would only take 3 churns prior to a real transaction. This means on the 4th transaction (the first real transaction performed after churning) your anonymity set will be 160,000.

With a ring size of only 5, achieving the same level of anonymity would take 7 churn operations prior to the real transaction.

Ideally, increasing the ring size to 20 would happen at the same time as @luigi1111 's range proof size reduction goes live.

Hopefully Surae can give an opinion on this, since it relies on the assertions in the churn paper https://github.com/monero-project/monero/issues/1673#issuecomment-278509986

As a side note, if the ring size does increase to 20, I'd vote to not allow users the ability to specify a ring size other than 20. If they need more anonymity than this, it should be achieved by choosing a 'churn level' for their transaction rather than a higher ring size. A way of describing the purpose of 'churn level' to the user might be something like accompanying it with the 'anonymity set size', so that rather than just seeing options for churn 0...5, they'd also see a potential anonymity set choice of 20, 400, 8k, 160k, 3.2m, 64m.

Churn allows us to say that Monero is just as anonymous as ZCash, except without the trusted setup.

## iamsmooth | 2017-06-22T15:59:32+00:00
I wouldn't say the EABE attack is nonsense but it needs to be better quantified given a reasonable range of expectations about usage, especially in terms of false positives.

Also, reducing the range proof size arguably makes it less desirable to increase the ring size because signatures become more significant.

Once you get into churn, well I'm not sure how I feel about 3 steps at 20 vs. 7 steps at 5 (or likewise other equivalencies that can be drawn). In some ways the latter is actually more efficient (though not accounting for range proofs and other overhead).

I like the idea of expressing multiple steps as an anonymity set size.

Also, do we actually know how to do churn such that recombining your own outputs with each other doesn't give up information? Maybe as a sequence of one-input-one-output transactions? I guess that would be okay since these (at least the one-input part) happen routinely.

FWIW, I've always taken the view that 'churn' is not a protocol function, it is something that can be built on top of the protocol. I don't think there is any way to avoid that, because the blockchain can't tell which transactions are churn and which are not (which is probably good).

## knaccc | 2017-06-22T17:18:10+00:00
> FWIW, I've always taken the view that 'churn' is not a protocol function

Absolutely agreed. The reason I bring it up is because if churn is deemed necessary for privacy, then choosing a higher mandatory ring size reduces the number of churn operations and therefore the transaction waiting time required (because it's mostly pointless to try to set a higher ring size for your churn operations than the ring size that other users have applied to their own transactions whose outputs are being used as decoys).

> Also, do we actually know how to do churn such that recombining your own outputs with each other doesn't give up information?

If people are giving out one subaddress per entity that needs to send to them, then it's fine to combine all inputs directly received to that subaddress in the first churn operation. Then you'd continue churning the resulting output the required number of times prior to making the ultimate transaction.

If inputs that need to be spent were received via multiple subaddresses, then one can be used directly and the others would be churned separately and combined only as part of the very last transaction when payment is made.

Note that the introduction of subaddresses will make the need for a 'churn' operation more acute, since it is a privacy problem if outputs received via different subaddresses need to be combined directly in order to spend them all together. At the moment the CLI will warn the user and ask the user to manually 'churn' by transferring the funds all to the same subaddress prior to spending. This will be much better implemented such that the wallet will queue up the churn operations and the final spending transaction internally so that the user does not have to set a countdown timer and return to the wallet after the intermediate transactions have been completed.

## JollyMort | 2017-06-22T20:25:46+00:00
I'm of the view that Monero provides all necessary tools for privacy but it's up to everyone to decide how to use. It still seems a bit clunky as the "best practice" is not really agreed upon. And it may not ever be. As we grow, there may come different strategies etc.

The defaults (or enforced rules) should be such that they provide some acceptable baseline, and more importantly, generate enough noise so those who really want to hide have places to hide. For me personally, I'm fine with current defaults but if I were ever to be in the need to buy some forbidden book, I'd consider some better-than-default strategy.

Churn is just one possible strategy and I wouldn't really advertise churning to normal users because it means locking your change and waiting 1h+ before you can spend.

And what's to stop someone from wanting to optimize to just use a higher than min. ringsize and churn only 1-2 times? You say the TX would stand out - so what? If I would announce to you that I will now churn my wallet 2 times with ringsize 100, and you can see those 2 TX-es and know even that they belong to me what else you can tell about my money? Nothing. Where did I get it from, where did it go? So you likely know the endpoint output, so what, you don't know with who it is. It could be in someone else's hands and then it's his problem to hide it came from me and maybe he'll want to churn 2 times with ringsize 100 :) And you're sure to have many false positives later on, because with 10000 outputs involved, chances are many of them will light up in other peoples transactions. You can't view this from the point of view of one wallet, one person, one TX. It's way more fuzzy already :) To top it off, say you're the exchange and I want to troll you. I could take the output you made for me and include it in 10 different other TX-es of mine as decoys. Even better, just make 10 outputs, with 9 of 0 amount. Now you have no idea of destination output, even. And all those outputs will get picked up by others and lead you to false positives. I'm actually waiting for a day when someone releases his own modded wallet to do things with some new strategy. Maybe there already are but are kept... private.

Thinking about this, maybe using a big mixin is actually better. I mean, objective of ring signatures is to hide the **origin**. So what if my TX with 100 ringsize stands out, the origin of the input side is successfully hidden, and so is the recipient and then it's the next guy's problem to hide the origin if it matters to him. Maybe he likes to use ringsize 100 as well, what do you know?

I get the feeling we may be overthinking this - is it just me? Just lift the min. ringsize to 5, default to 8, add preset steps at 16, 32 and 96 and wait for someone to release a paper to see how it worked =) Wouldn't really enforce the steps because if someone wants to play around with different numbers - why not let him? Sticky defaults FTW.

>that is already essentially exactly what we are doing (and indeed what would also happen if we just picked outputs according to a reasonable usage-based distribution such as the one in the monerolink paper). Currently half of outputs are chosen from the most recent 1.8 days, and those are chosen with a triangular distribution so it actually clusters somewhat newer than that in practice (3/4 within the more recent 0.9 days I think). With everyone doing this, every, or very nearly every, fresh output is going to be picked up at least once if not multiple times before it gets old.

Great, so all we need is a bigger ringsize really, no?

## knaccc | 2017-06-23T05:36:31+00:00
> Churn is just one possible strategy and I wouldn't really advertise churning to normal users because it means locking your change and waiting 1h+ before you can spend.

Agreed, the default would be no churn in most situations. So essentially with every transaction, we offer the user an instant transaction (regular privacy) or a churned transaction (high privacy). They make the simple decision as to whether they need the high privacy or not. Maybe the high privacy option is hidden in the advanced pane so that most users don't even see the option, just like we hide the ring size choice at the moment.

> And what's to stop someone from wanting to optimize to just use a higher than min. ringsize and churn only 1-2 times? 

If I churn three times with ring size 5 and then send my actual transaction with ring size 5, and if all of the decoy inputs had a tree of ring size 5 transactions behind them, then I get an anonymity set of `5 * 5 * 5 * 5 = 625`. Think of this as a pyramid filled with the number 5.

If I increase the ring size to 1000 for all of my churns and for the final transaction, but everyone else is mostly just using a ring size of 5, then my anonymity set pyramid will have the number 1000 in it only down one side, and the other numbers in the pyramid would be 5 since all of the other decoy outputs only had a ring size of 5.

Let's explore the anonymity set sizes in different scenarios.

Code for determining this pyramid is:
```
function anonymitySetSize(churnsPriorToFinalTransaction, yourRingSize, mandatoryRingSize) {
  if(churnsPriorToFinalTransaction==0) return yourRingSize;
  var total = 0;
  for(var i=0; i<yourRingSize; i++) {
    total += anonymitySetSize(churnsPriorToFinalTransaction-1, i==0 ? yourRingSize : mandatoryRingSize, mandatoryRingSize);
  }
  return total;
}

To hit the anonymity set level recommended in the churn paper, the options are:

// 3 churns prior to transaction, everyone uses ring size 20:
anonymitySetSize(3, 20, 20); // = 160,000 at a cost of $0.92, extra wait = 1h

// 5 churns prior to transaction, you use ring size 1000, everyone else has ring size 5
anonymitySetSize(5, 1000, 5); // = 155,845 at a cost of $12.27, extra wait = 1h40mins

// 7 churns prior to transaction, everyone uses ring size 5
anonymitySetSize(7, 5, 5); // = 390,625 at a cost of $1.61, extra wait = 2h20mins


To hit an anonymity set of *everything*, the options are:

// 5 churns prior to transaction, everyone uses ring size 20:
anonymitySetSize(5, 20, 20); // = 64,000,000 at a cost of $1.15, extra wait = 1h40mins

// 7 churns prior to transaction, you use ring size 1000, everyone else has ring size 5
anonymitySetSize(7, 1000, 5); // = 97,558,345 at a cost of $16.36, extra wait = 2h20mins

// 10 churns prior to transaction, everyone uses ring size 5
anonymitySetSize(10, 5, 5); // = 48,828,125 at a cost of $2.22, extra wait = 3h20mins

```
So this is a trade-off between the fee for regular privacy transactions, the fee for high privacy transactions, and the time required for high privacy transactions to be processed.

A mandatory ring size of 20 will approximately halve both the fee and time required for high privacy transactions vs a mandatory ring size of 5.

For comparison, a regular privacy transaction at ring size 5 at today's prices is $0.20, and a regular privacy transaction at ring size 20 is $0.23.

So a mandatory ring size of 20 increases the regular transaction fee by 3 cents, saves high privacy users 1hr20mins in transaction time and saves them between $0.69 and $1.07 on fees.

A high privacy transaction taking 20mins + extra 60 mins to fully confirm seems reasonable compared to a regular Bitcoin transaction that takes 60 mins to fully confirm. 

Notes:

There is the possibility to 'pre-churn' any funds received to the wallet so that there is no extra transaction wait at all for high privacy transactions when the time comes to make those transactions.

For ultimate peace of mind, you may want your anonymity set to be *everything*. Such a  transaction would rival a ZCash clone with always-on private transactions (the ZCash team have mentioned that they have a transaction accelerator server in the works that would make this feasible).

It may be possible to follow backward the path of churn if the churn transactions use a higher ring size than most other transactions, negating the benefit of using churn at all. Churn is only effective if an observer cannot tell that the same person had made each churn transaction in the chain.

To repeat a proposition made in an earlier comment, I would recommend forcing all transactions to use the same ring size of 20, because allowing the user to raise the ring size beyond this would in too many scenarios only offer pretend extra privacy. Genuine extra privacy beyond the default ring size in many common scenarios requires an anonymity set size that is large enough that it can only come from churn.

Churn is the only way I can see that we can avoid every exchange from knowing about huge numbers of interactions between Monero users that currently incorrectly assume their transactions are anonymous in the repeated Exchange->Alice->Bob->Exchange scenario. This is an extremely common scenario because it's how users make purchases while avoiding XMR/local currency exchange rate risk.

## SamsungGalaxyPlayer | 2017-07-04T21:54:11+00:00
Adding some more information here to look at the effects of churning from a pure fee perspective. This approach's goal is only to minimize the total transaction fees paid by everyone on the network. It does not take anything else into account, though of course other things (such as time) matter in practice.

I think it's important to consider the proportion of people who need to churn to make a higher mandatory ringsize worthwhile, again only from a fee perspective. This can help determine whether a higher mandatory minimum ringsize is necessary. I am personally convinced that the new minimum should be **at least** 10, since that's what was documented in previous MRL research papers. This post tries to look at the impact on fees for ringsize 10 and 21 transactions to see if it is worth it to make the benefits of churning more accessible.

I made some test transactions of 10 XMR of ringsize 10 and 21 with the default fee multiplier of 4x.

Ringsize 10 fee (1 transaction): 0.0158732 XMR
Ringsize 21 fee (1 transaction): 0.0181408 XMR

To determine the proportion of people who need to use the churning feature to make a minimum total transaction size, I used to the following equation, wherein x is the percentage of users who do not churn:

`(x)(ringsize 10 fee)+(1-x)(ringsize 10 fee)(number of churns 10) = (x)(ringsize 21 fee)+(1-x)(ringsize 21 fee)(number of churns 21)`

For high privacy (as documented by @knaccc), the equation is:

`(x)*(0.0158732)+(1-x)*(0.0158732*6) = (x)*(0.0181408)+(1-x)*(0.0181408*4) -> x= 0.909`

For ultimate privacy (again as documented by @knaccc), the equation is:

`(x)*(0.0158732)+(1-x)*(0.0158732*8) = (x)*(0.0181408)+(1-x)*(0.0181408*6) -> x = 0.889`

Thus, increasing the minimum ringsize from 10 to 21 is considered appropriate from a strict total-fee perspective if at least 9.1% of people churn with high privacy or at least 11.1% of people churn with ultimate privacy. 

I will leave the speculation about the proportion of transactions that will use churning up to others. However, these results give me some reservations. I am doubtful that churning will see this much use, though the increase to 20 or 21 can be justified in other ways (such as time, or wanting to incentivize it, or protections to non-churning users). This is definitely an interesting topic for discussion.

## knaccc | 2017-07-05T00:01:43+00:00
### The EABE attack defined

It's been pointed out to me that many people only following this discussion on GitHub and not on IRC are so far unaware of the "EABE attack". I'll explain it here for those new to the concept.

To avoid exchange rate risk, it's common for Alice (A) to withdraw XMR from an exchange (E), and then use that XMR to make a purchase from Bob (B). At some point in the future, Bob will cash out at the exchange (E).

Hence, "E->A->B->E".

This pattern of purchasing cryptocurrency from an exchange immediately prior to making a purchase from a vendor, in order to avoid exchange rate risk, was described by a merchant on Reddit as the almost universal practice of his customers.

If E->A->B happens only once, then the exchange cannot tell Alice has been sending money to Bob.

But if E->A->B happens multiple times, then when Bob cashes out with the exchange, the exchange can look at the set of outputs referenced in the ring signature of the transaction B->E. For each of those outputs referenced, the exchange can go backwards by several more transactions, to determine the set of outputs that each of those outputs must have originated from. The set of possible originating outputs grows dramatically as we travel backwards.

If the exchange only has to go backwards by one or two transactions in order to discover multiple outputs it knows it had sent to Alice, then this is extremely strong evidence that Alice was sending money to Bob.

For Alice to have been implicated incorrectly by chance, the person that sent money to Bob would have had to have chosen one of Alice's outputs as a decoy not only once, but on several occasions. Given that there are over 21 million outputs to have chosen from, the chances of choosing decoy outputs owned by Alice (or multiple outputs owned by any other Monero user) on multiple occasions is vanishingly small.

This means that a KYC exchange will know of large numbers of interactions between customers that the customers had incorrectly assumed would be private.

This is a serious problem for a cryptocurrency that prides itself on delivering private transactions.

The solution is for Alice to put distance between the outputs she receives from the exchange and the outputs she sends to Bob. She does this by churning, i.e. sending outputs to herself before then sending to Bob. Each time she churns, the size of the anonymity set will increase because the exchange will have to go back backwards many more transactions to eventually see the outputs that the exchange knows were previously given to Alice by the exchange.

The goal is for Alice to increase her anonymity set such that it is large enough that it will include not just multiple outputs owned by her, but multiple outputs owned by other Monero users or customers of the exchange. This gives Alice back her plausible deniability, because many other people could have, by chance, had more than one of their owned outputs caught up in the anonymity set.

Churning can deliver enormous anonymity sets, because each churn will multiply the anonymity set by the ring size of the transaction used to churn (as long as most other people's outputs referenced as decoys in her churn transaction had themselves used the same or larger ring size as Alice).

Increasing the mandatory ring size therefore requires drastically fewer churn operations by Alice in order to generate the anonymity set required to hide her activity with Bob from an exchange.

The ability of Alice to increase her anonymity set when sending funds to Bob can be implemented as a "high privacy" transaction option that automatically takes care of queuing up the intermediate churn transactions prior to funds ultimately being sent to Bob. 

To avoid having to wait for churns to happen when sending to Bob, Alice may choose to ask her wallet to churn incoming funds in advance, so when it's time for her to make a purchase with Bob the anonymity set of the funds she intends to spend with Bob has already been enlarged. Without the need for local storage, a wallet can automatically determine whether funds have been pre-churned or not, to avoid Alice wasting time and money by churning inputs that have already been churned.

## iamsmooth | 2017-07-08T02:23:57+00:00
@SamsungGalaxyPlayer 

> I am personally convinced that the new minimum should be at least 10, since that's what was documented in previous MRL research papers. 

What was documented about 10? I don't remember it.

Based on these past several messages (including the analysis of 'total fees' (see note below) between 10 and 20),  I'm thinking that a reasonable proposal may be to mandate a _fixed_ (not minimum!) ring size of 10. This is a modest increase (which therefore avoids extreme increases in either chain size or verification costs) that gains from the status quo not only from the increase itself but from standardizing on a single size which reduces distinctions between transactions, which is already an improvement in chain-level privacy/fungibility, and which also can avoid impairing the effectiveness of churning.

Those who want a wider fan out than that will have to use some form of churn (even just _one step_ gives a fan out comparable to the larger ring sizes that might actually be used in practice). The utility of variable ring sizes doesn't really seem to be there to me, relative to the costs of it.

We need to come to some conclusion soon in order to deploy stable consensus code well ahead of the scheduled fork. 

Note: Fee _levels_ are arbitrary and especially so when considering an exchange rate to dollars. A better analysis is to look at costs in terms of chain size and verification time (somewhat correlated), though in practice at a static fee rate and exchange rate these are equivalent.

## knaccc | 2017-07-08T03:53:08+00:00
@iamsmooth I'm very much in favor of your recommendation of a fixed ring size instead of allowing choice, and forcing people to churn to get higher anonymity sets. It'll simplify the user interface too. For your reference, here is a comparison of ring size 10 vs 20:


|   | Ring size 10 | Ring size 20 |
| ------------- | ------------- | ------------- |
| Churns prior to final transaction required for high privacy  | 4 | 3 |
| Churns prior to final transaction required for ultimate privacy  | 7  | 5  |
| Regular privacy transaction cost (1x/4x priority) | $0.20 / $0.80  | $0.23 / $0.92 |
| High privacy transaction cost (1x/4x priority) | $1.20 / $4.80  | $0.92 / $3.68 |
| Ultimate privacy transaction cost (1x/4x priority) | $1.61 / $6.44 | $1.15 / $4.60 |
| High privacy extra wait time  | 1h20mins  | 1h  |
| Ultimate privacy extra wait time  | 2h20mins  | 1h40mins |
| Minimum high privacy anonymity set required  | 73,000  | 73,000  |
| Minimum ultimate privacy anonymity set required  | 25,000,000  | 25,000,000  |
| High privacy anonymity set achieved  | 100,000  | 160,000  |
| Ultimate privacy anonymity set achieved  | 100,000,000  | 64,000,000  |

Note: transaction costs calculated on the basis of $50 XMR.

## JollyMort | 2017-07-08T13:22:01+00:00
Make ringsize fixed how? Wallet hardcoded - OK. Daemon rejecting wallet non-conforming TX sent via RPC - OK. Daemon rejecting a non-conforming TX from another node - NOT OK. I don't think putting it into network/consensus rules would be a good idea. Always fearing some BTC1MB-like situation could arise in the future if you hard-set things.

The discussion was about increasing the min. ringsize, and it diverged to churning and EABE. Can we get back to min. ringsize and agree on a number and set it as concensus-enforced-minimum already? I vote for 16 as minimum. It's a nice number with only 2s as factors, so why not.

Whether use only 1 or a set is of lesser importance as it could be simply hard-coded into the wallet but still allowing TX-es with non-standard to fly around if someone really wants to recompile the wallet and have a choice.

As for the EABE... can we please call it a weakness. It's not an attack - who's attacking who there? An attack would be a deliberate action exploiting the EABE weakness.

While EABE is a real weakness I think it's being overblown. I fear there's a lot of confirmation bias involved in analyzing this weakness. For every example of EABE I can draw a counter-example where some R,G,H's actions make E's head spin really really hard. If E is an exchange with lots of users and we have 16 ringsize as min, and 8 of those get picked from last day, chances are E will be getting lots of fake positives with no way of telling they're fake. And even if E can tell A transacted with B, what's the big deal? As long as A and B are aware of the risk - they can choose to churn, or not to - depending on how serious it is for them that E could know they're transacting.

While it's an interesting research problem, let's not be too hasty with conclusions and call to arms.

Let's see some examples:

E sends to A. For this scenario, A is your normal user who doesn't like to think too much.

A decides to donate to B. B is running a campaign on some forum hiding under a pseudonym with an address (even better, sub-address :)) publicly posted for donations - collecting funds for printing a ton of illegal bibles. Really makes some people angry who would like nothing better than to know who B actually is. In fact, E hates those damn bibles the most.

B cashes out to E.

So, E knows who both A and B are. E knows A **maybe** sent some funds (on multiple occasions) to B. That's it. Does E know that B is collecting funds for bibles? No. Does E know that those funds were for the bibles? No. Does E know for what purpose A spent his funds with B? No. Does E know the amount? No. Can E be 100% sure of anything? No.

Not knowing anything really, gets frustrated and decides to actively find out who B is. She assumes B could be using her service. So E decides to perform an EBE attack. E herself donates to B and watches out for those funds coming back to her. Can this work reliably?

E sends to B and waits.

B is doing nothing for 30min, he's out buying paper for those bibles.

Meanwhile, R just got some work paid and decides to cash out at E. It just so happens that the TX picked up the "flagged" output (E to B). Now E thinks R is selling bibles and R is fucked. R can easily prove he's not since he's really not, but that ruins reputation of E because its none of her business what R is doing. R makes a really big deal of it and sues E for harassment. E is pissed off and starts to campaign to make ring size of 1 mandatory but nobody listens. E loses.

## SamsungGalaxyPlayer | 2017-07-08T13:26:21+00:00
@iamsmooth I really only took 10 from [this chart](https://user-images.githubusercontent.com/12520755/27985693-f8d5cae8-63ef-11e7-958f-b0568e3c009b.png) in MRL-0001. They don't specifically recommend 10 (sorry for the previous wording), but it suggests 10 is better if blockchain bloat is less significant.

@knaccc thanks for the simple table. Based on the provided info, I think that a minimum of 20 is excessive.
@JollyMort, is there a significant threat that 16 mitigates over 10? Why not, for example, 12?

## JollyMort | 2017-07-08T13:27:02+00:00
@JollyMort, is there a significant threat that 16 mitigates over 10? Why not, for example, 12?

my point is - it's arbitrary. it only has to be a "big enough" number

## danrmiller | 2017-07-08T15:58:24+00:00
@JollyMort, fixing the weakness that allows some transactions to be identified due to user-chosen ring size seems relevant to discussion of changing the hard-coded network consensus minimum size. I don't find your argument against it compelling.

## dnaleor | 2017-07-08T16:35:40+00:00
I understand the fear for adding a new consensus rule, but having some uniformity makes transactions less able to "stand out" and adds fungibility. I do agree that the users should have the option to still use higher ring sizes. Therefore I want to remind you about a proposal that was floating around to make the ring size just follow a certain mathematical rule. Someone proposed the fibonacci numbers, I personally prefer just an easy x*2^n with x being the minimum ring size and n being the privacy level. If minimum is 10, users can chose between 10, 20, 40, 80, 160, ... 



## JollyMort | 2017-07-08T16:50:13+00:00
@danrmiller if it's only the user making such TX who is at risk, it's no reason to ban the behavior entirely.

The minimum, on the other hand, affects privacy for everyone and that's why it has to be a consensus rule.

What's wrong with simply hard-coding the desired behavior to the wallet? Hell, even to the daemon to reject non-conforming wallet-made TX-es. But network/consensus should still allow for anything >minimum, IMO.

## dnaleor | 2017-07-08T17:01:58+00:00
If there is one guy always using 37 then those transactions DO affect other users... 
When this guy who loves the number 37 turns out to be a criminal, decoys that are used in his transactions can be investigated and may lead to a knock on the door by law enforcement. Also, users have a disincentive to use the newly created txo's by this guy as decoys for their own ring signatures for the same reason. 

## JollyMort | 2017-07-08T17:16:37+00:00
But you can't know if it's just one guy using 37 or there's a cult following of number 37. And why would I avoid to put an output from a 37-ring in mine? I mean, maybe the guy just likes 37 and is legit. Maybe I like 37, too. I could be putting an output from a common 10-ring which is incriminated and have a knock on the door. The whole point of stealth addresses & ring signatures is that you can't know what you're ringing with and thus can't be held responsible.

## dnaleor | 2017-07-08T17:22:51+00:00
My point is that all transactions with ring size 37 are linked together, so when you own a decoy that is used in a non suspicious transaction by that guy, but that guy later on turns out to also receive ransom payments, and then spends that money with ring size 37, you may be linked to the ransom money, even when you were not part of the transaction containing the ransom money as an input. 

## JollyMort | 2017-07-08T17:34:45+00:00
That's really stretching it. I mean, you don't know if it's the same guy even if it's uncommon - until you actually get his wallet, and the same argument could be built if the ransom guy uses normal ringsize but has his wallet confiscated which shows also some of your outputs. The whole point of ring signatures is to make any story we can let our imagination come up with a plausible one.

## dnaleor | 2017-07-08T17:37:02+00:00
I agree it's a weak link, but nevertheless it's a link. It's easy to fix, while still keeping flexibility. I don't really see big disadvantages. 

## JollyMort | 2017-07-08T17:58:07+00:00
So how about this, then:

10 as consensus-rules-enforced minimum, requiring a HF

10, 20, 40, 80, 160 ... (2^n * 10) as allowed presets by the network rules ie offending TX-es will not be passed on, but a mined block with 37 would be accepted. Same like we're already enforcing min. fees.

Btw, you'd want a bigger ringsize when merging multiple outputs in a TX to make any association between them weaker. Churn doesn't help there.

For the wallet, maybe not give an option per TX, but put the setting somewhere in settings under advanced tab. Could do the same for CLI, to remove the [mixin] part from `transfer` command and only be able to set it via `set` command. Instead of [mixin], we could put [priority] into `transfer` command for convenience.

## dnaleor | 2017-07-08T18:42:24+00:00
Sounds cool. If for whatever reason in the future we want to make it easier to use non standard ring sizes, it can easily be re-enabled without even a soft fork needed. 

I also agree on adding the priority to the cli transfer command 

## iamsmooth | 2017-07-08T20:34:09+00:00
@JollyMort the problem is that the different sizes are going to interfere with the effectiveness of churning which is really a special case of making the entire chain more traceable. If I churn with a ring size of 20 on each step then if you trace back from my final outputs, the previous transactions that are 20 are mine, the ones that are something other than 20 are likely fake output that can be disregarded.

In the case of the person who for whatever reason uses 37 (assume not for churning, as that case would be catastrophic), there will be change outputs back and those will likely be spent with 37 too. That makes the real spends on the change outputs identifiable, and any fake spends of those outputs disregardable, hurting others (not 100% _certain_ of course, but the inference may be reasonably strong)

Even with the fixed set of sizes, if we look at the chain today, about 70% use the absolute minimum (3). The rest are likely to be infrequently used and therefore identifiable in some cases, creating a hazard not only for their own creator but for others who want to interact with them as fake outputs. The reason we have a minimum size is the observation that without a minimum size many users will tend to cluster at the smallest sizes (even 0) for cost reasons, resulting in a lost of privacy for the chain as a whole. A similar argument applies to multiple sizes (usage will tend to cluster at the smallest size). Both have been borne out in practice.

IMO we have a better way to offer larger anonymity sets, which is even mild forms of churning such as _one_ additional step. With uniform transactions on the chain, one step of churning with a standard ring size of 10 on each step results in 100 equiprobable sources with a small delay and a total transaction size just 2x normal, or 400 with a uniform ring size of 20 (two steps of course results in an anonymity set of 1000/4000, which is approaching the point that is not even achievable at all with a single tx). The delay may even potentially be reduced/removed in the future if we allow spending (which would include fake spending) of unconfirmed outputs.

But this won't work well if the potential sources are not indistinguishable, because the churning must choose outputs that are indistinguishable from its own not only at one step but at N steps backward _along every possible path_. Possibly those wanting to churn could use a randomly selected mix of ring sizes to avoid identifying the true path, but this is complicating things for, I think, minimal gain (and possibly might still be less effective).

One last thought. Look at a block explorer now. Does it not seem likely that there are a few high-ish volume transaction creators who are using one of the lesser-used sizes? That would make it possible to identify a lot of their transactions. Example: one of the exchanges is doing this. If you send coins to the exchange and your output is spent with that non-standard size, you can infer that is likely the real spend, and any others are fake. Someone could even deliberately send many deposits to the exchange for this purpose.

In summary, I think the gain to _overall chain_ privacy from standardizing on a single size (and generally reducing the visible differentiation between transactions) outweighs the loss of utility to an individual user who might on occasion want to use a non-standard (larger) ring size. but by doing so steps out of the crowd making it harder for everyone (possibly including themself) to be "lost in the crowd".



## iamsmooth | 2017-07-08T20:53:30+00:00
@JollyMort 
> There's a cult following of number 37

This is actually bad. It splits the chain into cult members and non-cult members, reducing the anonymity set of both. In general terms, everyone gains from: a) a larger set of users sharing the same anonymity set, and b) transactions being as indistinguishable as possible to make the anonymity set robust (not subject to attack by breaking it apart into identifiable subsets).

Obviously if people want to deliberately identify or differentiate their transactions (for example by posting them on a web site, or intentionally packing their "cult ID" into their transaction), we can't do anything about that. But we can do something about unnecessary knobs that serve to unintentionally identify or differentiate transactions without adding a lot of value.

A similar example of something that serves to differentiate transactions is number of inputs/outputs. I would love if there were a reasonable way to standardize that (say 2-in, 2-out) but there really isn't, because certain types of users/businesses will receive small payments and need to make large payments (or possibly the reverse). The cost of making many tiny payments in place of one large one is astronomically higher. So there is no viable substitute at this point (though perhaps we can develop one). By contrast the cost of achieving an anonymity set of 100 or 400 with one step of churning rather than one enormous transaction is very low (in fact the churning solution is actually _cheaper_ to the system in terms of signature verification)

## JollyMort | 2017-07-08T21:07:02+00:00
Fair enough. So 10 as consensus minimum, and 10 as network-rule only allowed value? In case some new research comes up, it's later easier to push a daemon update on some % of network instead of another HF.

## iamsmooth | 2017-07-08T21:59:06+00:00
Network rule seems fine at this point. Or even just removing UI support from the wallet (but also need to consider the API, and that it was historically user-selectable in the standard wallet might encourage third party wallets to continue supporting it). I don't think people need much discouragement from using transactions which cost more, just stop encouraging it. There really aren't any good guidelines for recommending what ring size to use for what purpose so given options/inputs people may just make arbitrary choices. That likely doesn't help anyone much.

## knaccc | 2017-07-09T00:14:47+00:00
I'd previously written a comment about how churn could work, involving asking the user certain questions. Please disregard that comment.

A much better solution is to simply put a churn button on each account in the user's wallet. Users will separate their activity by having one account for highly sensitive transactions and another account for regular transactions. 

If users press the churn button, their wallet will determine which incoming funds have not yet been churned, and will churn them. Thus they will not pay to re-churn funds that have already been churned.

The reason for this approach, instead of a high privacy/ultimate privacy choice on every single transaction, is that a user only really needs to do churn once after receiving funds from a KYC exchange. From then on, no further churn is required as long as they keep sensitive transactions to one account and regular transactions to another account. 

Another benefit is that they can churn their incoming funds far in advance of needing to spend them, so that there is no extra churn delay when it comes time to spend their funds. It also ensures they don't waste money by paying for a churned transaction when every single future transaction is made. They should only need to pay churning fees once after each large purchase of funds from an exchange.

If the user needs to cash out their sensitive account at an exchange, they will push the churn button prior to cashing out.

Note that if the user pushes the churn button, they should be able to queue up a subsequent transaction or transactions without having to wait for the churn to finish. This saves them having to set a timer for when to return to their wallet. 

## dnaleor | 2017-07-09T00:42:43+00:00
I know we're now basically talking about UX... but what about a checkbox "sensitive address" when you create a sub address? Then you could turn churning on automatically when funds are received. (ofc automatic churning can be disabled in settings etc) 

Also, maybe an additional churn button next to each transaction in the transaction history would be useful (maybe even with drop down menu for number of rounds) to execute additional background churning for certain transactions. 

Just some random ideas. 

## iamsmooth | 2017-07-09T01:29:14+00:00
I think these UX questions are best considered elsewhere unless they impact on protocol decisions (which is possible). I expect that as the Monero ecosystem matures there could be different wallets with different UX approaches, but they absolutely must share the same protocol.

@knaccc KYC exchange is not the only reason one might want a very high anonymity set. Situations can arise in a purely p2p settings where someone knows who you are and knows something about you but you don't necessarily want that person getting insight (even merely statistical) into some or all of your other transactions.

## knaccc | 2017-07-09T01:42:25+00:00
@iamsmooth The reason I mentioned the UX is to give a better indication of the expected frequency of churn vs regular transactions. This affects how important churn fees and churn duration are when deciding the ring size.

I'm happy with your suggestion of a ring size of 10 for September. The churn time is longer, but the ability to churn in advance means this isn't a huge annoyance. The ability to churn in advance also means that users will be able to decide the timeframe over which to churn when they click the churn button. So I would personally probably press the churn button and ask for the 7 churns to happen randomly over a period of 24hrs or more, 4hrs if I was in more of a rush. Thinking about it, I'd not even bother offering users a high privacy vs ultimate privacy churn option, especially given that at first they won't have all that many ring size 10 transactions to use as decoys. Instead they would always get the ultimate 7x churn when they pushed the churn button, and their only choice would be about timeframe.

It's worth repeating what I think @moneromooo-monero pointed out, which is that a 15% transaction size increase will in the future become a 30% transaction size increase, because when the range proof sizes are eventually reduced by @luigi1111 the rest of the transaction will be smaller by comparison.

## JollyMort | 2017-07-09T15:01:02+00:00
>Network rule seems fine at this point. Or even just removing UI support from the wallet (but also need to consider the API, and that it was historically user-selectable in the standard wallet might encourage third party wallets to continue supporting it). I don't think people need much discouragement from using transactions which cost more, just stop encouraging it.

On a second thought, network rules could be too restrictive. If someone wants to experiment with output selection with a bigger ringsize we'd be preventing that. So yeah, just on wallet side should be enough, and likely outcome will be 99.99% TX-es using that. Our experimenter could easily do the tweaks to let him broadcast "strange" TX-es and be the 0.01%.

## knaccc | 2017-07-10T14:50:36+00:00
Monero Deep Anonymity Accounts: http://imgur.com/a/ZvJQ8

Note that the user never needs to see or know the word 'churn'. Also note that there is no longer any need for 'high privacy/ultimate privacy' transactions. If you need high/ultimate privacy, you simply use funds from a deep anonymity account instead of from a regular account.

## JollyMort | 2017-07-10T21:05:38+00:00
nice work! btw, how did you establish the criteria for high/ultimate privacy?

## knaccc | 2017-07-10T21:27:42+00:00
@JollyMort Thanks, I hope it's clear to everyone that even if this concept of deep anonymity accounts is not implemented, this scheme is still the suggested best practice that people engaged in highly sensitive transactions should follow anyway. Of course, it's much easier to follow this scheme if the wallet keeps track of things, queues up churn automatically for you, and gives you helpful hints about what you can and can't do without compromising your privacy.

The high privacy anonymity set size was chosen, based on the results of the Java simulation code above, to be the minimum required for at least one other user to be caught up in the anonymity set alongside you. This is the threshold at which the chance of you being the real sender suddenly drops from >99.9%+ to 50% or less.

The ultimate privacy threshold was chosen such that the anonymity set size can come as close as reasonably possible to plausibly implicate most other users alongside you, so that there is not even circumstantial evidence of your activity.

## JollyMort | 2017-07-11T18:22:34+00:00
25m outputs was based on entire history, right? Pre-RCT people used to have lots of outputs for every TX because you had to split into denominations. What do you think of taking only RCT data and extrapolating to age of Monero, or X years, to get some numbers suitable to the new reality? Since 99% TX-es are RCT, nobody is ringing with old ones anyway.

For outputs/users distribution - trying something other than Zipf distribution might be worth looking into and see what criteria you'd get for "high". Maybe uniform distribution, as a "catch-all" and see if it's a big difference - that could give some hints.

I understand that, for simplicity, you randomized outputs-users but that seems rather unrealistic as it doesn't consider output picking algorithm and some patterns which should be in the data like: an user can't spend if he doesn't have funds and funds must originate from a coinbase TX. In your simulation, there are probably cases of users having outputs with no source. It kind of bothers me that it doesn't take these things in consideration (or does it?) but I understand that a better fit simulation would be more complicated.

Maybe take the real (RCT) data, assume number of users (even better, number of potential users / day) and start from X height matching a TX to user by random picking an user from the pool of users for recipient of an output. Randomly pick which input will be the "real" one. That ought to give some plausibly realistic data from where you could extract what you want. What do you think? Maybe Surae could recommend a method/software, or if we know someone analyzing similar phenomena. 

In any case, what you did is valuable and can give a good idea on where to look further. For sure it's an area which requires more research, but as pointed above we must consider it now to find a kind of "optimum" ringsize to make churning less cumbersome.

Instead of 10, maybe ramping it up a bit (but <20) could reduce required number of churns for some assumed distribution. Simpy using the criteria above, 17 is the number where we can reduce the number of churns to 3 for "high" (83k set) and to 5 for "ultimate" (24m set). Thing is, if some later research, with better fit to realistic data, shows that you need less churns than expected for a given ringsize then we kind of wasted space.

On a second though, might just stick with 10. Opinions seem to converge around the number 10, so might as well pick that. If it turns out we need more, we can always bake it in later as a soft rule: into wallet or network rules, avoiding an immediate HF but having a quick fix until the next HF to set it in stone.

Tabulating the TX size and TX size increase per additional input/output would be useful in seeing how it scales with regards to blockchain growth (before/after range proof reduction)

Thoughts?

## SamsungGalaxyPlayer | 2017-07-11T19:13:43+00:00
@JollyMort having a higher minimum ringsize would reduce the number of churns needed, but it will increase the cost of all transactions. I personally feel that a ringsize of 10 is the sweet spot where people who want to churn can churn reasonably, people who do not still have low transaction costs, and the higher ringsize adequately mitigates some of the current attacks with ringsize 3 discussed in the MRL papers.

I feel that if over 10% of people churn, then that could warrant a larger minimum ringsize (perhaps to 17). I suggest waiting though since I am pessimistic about this, especially if more users in the future will use lightweight wallets focused on ease-of-use.

## JollyMort | 2017-07-11T19:20:47+00:00
Sure, and maybe some later research shows that even for 10, a lower number of churns is required. We'll see.

In any case, am I right to say that it seems like we're converging towards 10 here implemented as HF-enforced minimum and wallet fixed setting?

## knaccc | 2017-07-11T20:25:33+00:00
@JollyMort I think the consensus seems to be moving in that direction. I'm happy with a fixed ring size of 10.

I think there is still work to be done to determine:

1. How high the minimum ring size needs to be to ensure that most outputs will be used at least once as part of a decoy in another transaction. I'm particularly keen to see outputs regularly referenced as decoys fairly quickly after they are first created, in order to provide cover for a series of churn transactions.

2. How high the minimum ring size needs to be to mitigate the threats mentioned in MRL0004.

## JollyMort | 2017-07-11T20:46:25+00:00
>I think there is still work to be done to determine...

I agree, but that is something we can't conclude here since it requires more research.

I believe that the required amount of churns could vary significantly depending on the method chosen to analyze it, especially if the output selection algorithm is taken into account.

As for the minimum ringsize, a month after the HF, there will be enough real data to analyze how many times the new outputs get picked :) Since 50% is chosen from last 1 day or so and the ringsize will be 10, I expect them to get picked up quite often if the network usage doesn't oscillate much. We'll see.

## ghost | 2017-07-11T20:51:02+00:00
Fixed ring size of 10 looks good.

## iamsmooth | 2017-07-11T21:16:55+00:00
> How high the minimum ring size needs to be to ensure that most outputs will be used at least once as part of a decoy in another transaction

It is not hard to calculate this using the binomial distribution as a function of the number of outputs created per day and the ring size.


## fluffypony | 2017-07-26T17:42:16+00:00
FYI: we're aiming for a code freeze, tag, and release on August 15th, so that we have a month before the September hard fork. This means we need to pick a magic number in the next two weeks, bearing in mind that we can also change it in the subsequent hf.

## luigi1111 | 2017-07-27T17:03:50+00:00
I object to picking a "magic number" with this little lead time. I prefer leaving the currently/previously planned ring size 5 in place for September.

The wallet can absolutely be changed to use 10 as default.

In any case this does mean the the ringsize bump is the only thing going into this hard fork, though obviously a lot of non-forking changes will go in the release.

## iamsmooth | 2017-07-27T17:16:27+00:00
The wallet default, in practice, seems to have limited practical effect. A large majority of the transactions tend to be made using the minimum allowed. In fact it might be better for users to just let the default be the minimum since that provides the best 'blend into the crowd' protection on the network anyway, and anyone wanting to do something else maybe should be explicit (and informed, i.e. 'advanced setting') about it.

However, I don't disagree with what @luigi1111 says about lead time and making the adjustment to the already planned minimum=5 now while considering, well in advance, another minimum or fixed ring size for a future fork. For example, this would be a reasonable time, now, to decide on an April fork.

## JollyMort | 2017-07-27T17:17:54+00:00
The wallet can absolutely be changed to use 10 as **minimum**, even if it's not consensus minimum.

## dnaleor | 2017-07-27T17:24:30+00:00
I prefer the minimum to be equal to the default, as exchanges tend to use the minimum to save on fees (or maybe for regulatory reasons) 

Poloniex for example used the minimum for a long time, making it easy for people to trace monero coming directly from them. 

## peronero | 2017-07-27T20:38:32+00:00
The September hardfork and mid-August freeze seem to have pretty awkward timing taking into account progress on other important work - is there any merit to pushing back the fork?

1. Almost all TXs are already RCT so enforcing RCT at protocol level is of negligible benefit
2. Minimum ringsize bump at this point in time seems to be almost arbitrary and ad-hoc as a bump below 10 is of negligible benefit but a bump above 20 would bloat the blockchain beyond what is reasonable with current rangeproofs (paraphrasing Surae, I think I got it right) - optimized rangeproofs could be ready in several months and informed ringsize research could come a couple months after that
3. 0MQ and multisig are not ready to make it into the release either but could be in several months

Does it perhaps make sense to wait for 2 and 3 and have a well-informed ringsize bump with shiny new rangeproofs and feature-full release in 6 or so months as opposed to waiting until next spring? 

On the other hand, a GUI release is long overdue, but maybe we could squeeze out an interim GUI release with a 0MQ- and MS-less daemon sometime this summer and have the hardfork release in the winter?

## iamsmooth | 2017-07-27T22:25:33+00:00
1. 0mq and multisig are not consensus, they can be released (either together or separately) on any schedule independent of forks.
2. Agree completely about RCT. 
3. Not sure if the planned increase 3->5 is negligible or not. I'd prefer to see it happen all else being equal, especially since its been sort of part of the social contract for like 2+ years. I'd consider all other enhancements, whatever their merits, to be in a somewhat different category.




## rusticbison | 2017-07-31T10:41:41+00:00
The specification for the X Wallet is a fixed mixin of 4. At this level, the cost to use the wallet is already uncomfortably high.

On a related note: it would be a critical event if the network forks and enforces a higher minimum ring size. That would mean that our app would suddenly fail to send, trapping the user's money and creating a lot of stress. They would certainly lose trust in the technology at that point. 

## Gingeropolous | 2017-07-31T11:29:54+00:00
> The specification for the X Wallet is a fixed mixin of 4. At this level, the cost to use the wallet is already uncomfortably high.

I wouldn't fix the ringsize at 5. It should be whatever the protocol minimum is, at the least. 

Also, increased ringsize doesn't increase the tx size that much, compared to what ringct has done. 

## barnyardanimal | 2017-07-31T23:11:26+00:00
I have read every comment above and will summarize my thoughts citing the following recent points:

>I prefer the minimum to be equal to the default, as exchanges tend to use the minimum to save on fees (or maybe for regulatory reasons)

>Not sure if the planned increase 3->5 is negligible or not. I'd prefer to see it happen all else being equal, especially since its been sort of part of the social contract for like 2+ years.

>It's worth repeating what I think @moneromooo-monero pointed out, which is that a 15% transaction size increase will in the future become a 30% transaction size increase, because when the range proof sizes are eventually reduced by @luigi1111 the rest of the transaction will be smaller by comparison.

>FYI: we're aiming for a code freeze, tag, and release on August 15th, so that we have a month before the September hard fork. This means we need to pick a magic number in the next two weeks, bearing in mind that we can also change it in the subsequent hf.

I think an increase from 3 to 5 seems fairly negligible. I agree with the (very loose) consensus of 10 as the network minimum AND the client default. Range proofs come soon enough and a few months of transactions happening with a larger ring size before they are implemented wont be the end of the world.

Lets settle on 10 NOW a few weeks before August 15, so that wallets now in development can plan accordingly @rusticbison 

>The specification for the X Wallet is a fixed mixin of 4. At this level, the cost to use the wallet is already uncomfortably high.

I have seen the cost projections above and strongly disagree with this statement. People that use Monero care about privacy and security and 10 is much better fit for the current Monero social contract. An increase in ring size has been long expected.




## olarks | 2017-08-07T20:15:37+00:00
Hello everyone. I am glad to see discussion has still continued on this topic in my absence. There is lots of catching up to do! I had fallen off the earth for the past few months, but I am finally back. My last post mentioned continued surveying of the Bitcoin blockchain for the age of spent outputs and it is mostly the same, but with a larger survey size.

Total Outputs | Last Day | Last Week | Last Month | Last Year | > 1 year 
---------- | ---------------- | ----------------- | ------------------ | ---------------- | ----------------
7,029,369 | 4,533,277(64%) | 1,274,759(18%) | 672,399(10%) | 467,780(7%) | 81,154(1%)

Here is the improved python script that will dump the results to a json file in the same location as the python script. Feel free to play with it and modify it if there are other things you want to survey in the Bitcoin blockchain.

```python
import urllib2
import json
import os
import time

# this takes over a day's worth of blocks to parse so parsing
# the same block twice is unlikely
target_blocks = 144

def survey():
    if not os.path.isfile('survey.json'):
        with open('survey.json', 'w') as writefile:
            json.dump({'inputs': 0, 'transactions': 0, 'day': 0, 'week': 0, 'month': 0, 'year': 0, 'old': 0}, writefile)

    with open('survey.json', 'r') as readfile:
        data = json.loads(readfile.read())
        num_inputs = data['inputs']
        num_transactions = data['transactions']
        num_day = data['day']
        num_week = data['week']
        num_month = data['month']
        num_year = data['year']
        old = data['old']

    # timeouts are for lazily dealing with HTTP 429 errors and other errors from the API
    try:
        current_hash = urllib2.urlopen('https://blockchain.info/q/latesthash').read()
    except:
        time.sleep(60)
        try:
            current_hash = urllib2.urlopen('https://blockchain.info/q/latesthash').read()
        except:
            time.sleep(900)
            current_hash = urllib2.urlopen('https://blockchain.info/q/latesthash').read()

    num_blocks = 0
    while num_blocks != target_blocks:
        try:
            block_data = json.loads(urllib2.urlopen('https://blockchain.info/block/%s?format=json' % current_hash).read())
        except:
            time.sleep(60)
            try:
                block_data = json.loads(urllib2.urlopen('https://blockchain.info/block/%s?format=json' % current_hash).read())
            except:
                time.sleep(900)
                block_data = json.loads(urllib2.urlopen('https://blockchain.info/block/%s?format=json' % current_hash).read())

        block_height = block_data['height']
        transaction_count = block_data['n_tx']

        i = 0
        while i != transaction_count - 1:
            # skip coinbase tx
            i += 1
            transaction_input_count = block_data['tx'][i]['vin_sz']
            num_transactions += 1

            with open('survey.json', 'r+') as writefile:
                data = json.loads(writefile.read())
                data['transactions'] = num_transactions
                writefile.seek(0)
                json.dump(data, writefile)

            j = 0
            while j != transaction_input_count:
                input_index = block_data['tx'][i]['inputs'][j]['prev_out']['tx_index']
                try:
                    input_data = json.loads(urllib2.urlopen('https://blockchain.info/tx-index/%s?format=json' % input_index).read())
                except:
                    time.sleep(60)
                    try:
                        input_data = json.loads(urllib2.urlopen('https://blockchain.info/tx-index/%s?format=json' % input_index).read())
                    except:
                        time.sleep(900)
                        input_data = json.loads(urllib2.urlopen('https://blockchain.info/tx-index/%s?format=json' % input_index).read())

                input_age = input_data['block_height']
                j += 1
                num_inputs += 1

                with open('survey.json', 'r+') as writefile:
                    data = json.loads(writefile.read())
                    data['inputs'] = num_inputs
                    writefile.seek(0)
                    json.dump(data, writefile)

                if (block_height - input_age) <= 144:
                    num_day += 1

                    with open('survey.json', 'r+') as writefile:
                        data = json.loads(writefile.read())
                        data['day'] = num_day
                        writefile.seek(0)
                        json.dump(data, writefile)

                elif 1008 >= (block_height - input_age) > 144:
                    num_week += 1

                    with open('survey.json', 'r+') as writefile:
                        data = json.loads(writefile.read())
                        data['week'] = num_week
                        writefile.seek(0)
                        json.dump(data, writefile)

                elif 4320 >= (block_height - input_age) > 1008:
                    num_month += 1

                    with open('survey.json', 'r+') as writefile:
                        data = json.loads(writefile.read())
                        data['month'] = num_month
                        writefile.seek(0)
                        json.dump(data, writefile)

                elif 52560 >= (block_height - input_age) > 4320:
                    num_year += 1

                    with open('survey.json', 'r+') as writefile:
                        data = json.loads(writefile.read())
                        data['year'] = num_year
                        writefile.seek(0)
                        json.dump(data, writefile)

                elif (block_height - input_age) > 52560:
                    old += 1

                    with open('survey.json', 'r+') as writefile:
                        data = json.loads(writefile.read())
                        data['old'] = old
                        writefile.seek(0)
                        json.dump(data, writefile)

        current_hash = block_data['prev_block']
        num_blocks += 1

while True:
    survey()
```

## olarks | 2017-08-07T20:30:48+00:00
My thoughts quickly on the last few posts regarding the September hardfork and the chat logs of the recent meeting. If having a single static ringsize is back on the table I am in full support of the idea and if there is consensus for ringsize 10 as a candidate I also support it. A bump to ringsize 10 not intervening with the new adaptive blocksize algorithm is reassuring and a mere 1kb increase in 2/2 transactions is a small price to pay for ringsize 10. 

I am not aware of any recent improvements in the decoy output selection, but a random selection in accordance to approximate age of spent outputs still seems to be a good step in the right direction. I am sure Surae and Sarang can improve further on this though. 

## moneromooo-monero | 2017-08-09T20:36:03+00:00
> I am not aware of any recent improvements in the decoy output selection

https://github.com/monero-project/monero/commit/ac1aba90f8037d29803699bedc782f87ed9698ad

It tries to more or less match the distribution from Miller et al, with no change in overall algorithm.

## knaccc | 2017-08-14T02:00:45+00:00
Transaction fee calculator, to help with ring size decisions:

https://www.monero.how/monero-transaction-fee-calculator

## joijuke | 2017-09-08T04:27:23+00:00

When the cookie meets the blockchain: Privacy risks of web payments via cryptocurrencies
https://arxiv.org/pdf/1708.04748.pdf

## iamsmooth | 2017-09-10T00:36:32+00:00
This issue should be closed as the september 2017 hardfork is finalized. A new issue can be opened if there is a need for further discussion (referencing this one to avoid duplication).

## moneromooo-monero | 2017-09-10T10:17:55+00:00
Seems simpler to continue here. If the date in the title seems a problem, just remove it.

## panopolis | 2017-09-10T17:48:48+00:00
Sorry to jump in randomly, but I've read almost all of this discussion and wanted to give my input. First, is that having a mandatory fixed ring size seems best, to make all transactions look as indistinguishable as possible. Having few set options, ie 10, 20, or 40, is also reasonable, but allowing users to choose arbitrary ring sizes appears to have zero benefit and possible downsides. 

I also agree that whatever the minimum ring size is, this should also be the default option. I also like the idea of a churn button, as long as a clear explanation (perhaps in a bubble text on mouse over) is provided as to what it does and how/why one should use it. The average person will not have the technical knowledge to understand what's really happening when they press the churn button and will assume it makes them invincible, so it should be as idiot proof as possible.

## moneromooo-monero | 2017-09-22T21:11:15+00:00
Hi olarks, have you made any further progress with Bitcoin usage analysis ?

## Gingeropolous | 2017-09-26T17:50:23+00:00
hi @olarks , there we go we pinged

## iamsmooth | 2018-08-23T02:16:29+00:00
Once again I would point out this is stale (almost a year) and should be closed. Not only have multiple hard forks already occurred, many of the assumptions made in this discussion above no longer apply to the current protocol, but the bitcoin analysis which seems to be an open subtopic was already done by the monerolink paper (and others), and output selection is, for now, being done with a gamma distribution mostly in accordance with the recommendations of that paper.

Whatever issues remain can go into a new, better focused, issue. Any Bitcoin-based (or other) research which eventually gets done can stand on its own without this stale issue.

Closing the issue doesn't mean deleting it of course. It can still be referenced by new issues or even reopened if necessary.

# Action History
- Created by: olarks | 2017-02-04T14:51:01+00:00
- Closed at: 2018-08-23T02:23:57+00:00
