---
title: '[Enhancement] Improvements to the block reward penalty and minimum block size'
source_url: https://github.com/monero-project/monero/issues/1878
author: bigreddmachine
assignees: []
labels: []
created_at: '2017-03-17T21:09:20+00:00'
updated_at: '2020-02-08T01:17:39+00:00'
type: issue
status: closed
closed_at: '2017-04-24T14:25:03+00:00'
---

# Original Description
The recently merged PR https://github.com/monero-project/monero/pull/1869 increases the minimum block size before assessing a block reward penalty to 300kB. This was merged fairly quickly under the straightforward reasoning that this brings the minimum block size to relatively be in line with pre-RingCT levels.

I expressed concern that this should not have been streamlined through the review process, though seemingly was overruled by no one really agreeing with my argument.

However, out of a lengthy discussion that took place, a larger issue (off topic to that PR) emerged and began to be discussed. Because it was largely off topic there, I am opening this issue where the discussion can hopefully continue.

Below is a quick summary of my concerns over the block reward penalty and minimum block size as currently devised for new participants. There is a lot more detailed discussion that has already taken place in that thread, and this summary is very much insufficient in conveying the entirety of the discussion. Regardless, this is sort of a "tl;dr" of my point.

Paging participants of that discussion: @JollyMort, @iamsmooth, @vtnerd 

---

### My Concern:

I contend that the block reward penalty, as currently devised, becomes less effective the larger the median block size gets and the smaller the block reward gets. Further, when the median block size grows during a demand peak, miners are incentivized to maintain that larger median block sizes than required once demand tails off by in effect stuffing blocks with 0-fee transactions. This incentive comes from two sources: 1) the ability to more quickly respond during peak tx times, scarfing up txs more quickly by utilizing the space that had been being artificially maintained, and 2) excess block size allows mining pools to send 0-fee payouts their miners, reducing their costs and increasing profits.

I go into a lot more detail through back and forth discussions with the participants pinged above in the PR thread. I ask that we try not to rehash too much of those points here, though I am happy to clarify or respond here to anything that was brought up there.

Finally, I believe that the entire setup needs to be further studied, and that the merged PR probably should not have been streamlined to the extent that it was. @JollyMort did good research, but I believe that good, transparent peer review did not take place, as most discussion over the change took place on IRC outside of developer meetings and with no public review period taking place. I am okay if the consensus on the PR to say "let it pass" in this case because the intent of the PR is good and the implementation appears sound, but I think that future consensus-changing PRs like this one shouldn't go from draft analysis on Sunday to merged PR on Tuesday, especially as Monero has grown to now be a project of dozens of contributors, rather than a handful.

Perhaps this last point can be discussed at a future Monero Dev meeting, and discussion here can focus on if and how the block reward penalty and minimum block size can be more robustly designed.

# Discussion History
## iamsmooth | 2017-03-18T00:22:48+00:00
Here's a reply from the other discussion at #1869 

@bigreddmachine 
> Also, mining pools have an extra incentive here: they can utilize the "filler" 0-fee txs to pay miner rewards,

That's just a regular transaction. If those payments are being made to serve pools and miners it means that there is sufficient demand and the block size shouldn't decrease. Putting it in this block just removes it from another block.

I agree with your analysis that the costs of bandwidth, etc. are relatively low, but I argue that so is the benefit (for a non-dominant miner) because it has zero benefit if (other blocks are not padded) and the block size still falls, not not necessarily a large benefit it doesn't. Furthermore, a block size that is economically meaningful with respect to demand from _paying transactions_ actually benefits miners collectively by creating scarcity and fee pressure. It is not clear that there is an incentive for a miner to want to subvert this.

I'm not entirely convinced either way, but I don't think your argument is convincing. At least, you would have to parameterize it on what portion of the hash rate under what conditions would it make sense, and also consider the resulting supply-demand dynamics for tx fees.


## bigreddmachine | 2017-03-18T02:17:40+00:00
Reply to @iamsmooth:

> That's just a regular transaction. If those payments are being made to serve pools and miners it means that there is sufficient demand and the block size shouldn't decrease. Putting it in this block just removes it from another block.

Yes, I used "filler" there just to indicate that the tx could be made in place of a filler one I had previously mention and achieve the same end in the miner's eyes. Probably poor choice of phrase. But this was all under the premise that the median block size was larger than needed because miners are propping it up. So discussing that statement outside of that context is a bit difficult. I can appreciate that you remain to be convinced this scenario would occur in the first place, so I'll build out my point. It could very well be that you eventually convince me this is all moot, and if so that's fine by me. But I think I owe it to myself to continue to build my case until that happens, especially given that my whole point is in the interest of a problem I think exists for Monero in the long term.

> I agree with your analysis that the costs of bandwidth, etc. are relatively low, but I argue that so is the benefit (for a non-dominant miner) because it has zero benefit if (other blocks are not padded) and the block size still falls, not not necessarily a large benefit it doesn't.

The main point behind that reply was to counter the argument that there is a cost using filler txs to maintain a higher block size, and not to make a claim for benefit there. Those are two separate things, and you're right, I don't address the second there. However, I will now argue that there's basically no cost, especially in the long term, which means any benefit, even a tiny one, can still be worth it. Consider a more realistic case for big miners (either individuals or pools), which I will assume make up a majority of hash rate. In the long run, mining will gravitate to those who have the most efficient operations. Even with smart mining, I've yet to see an argument that would indicate a future other than one where a large portion of the hash rate is controlled by a small number of highly efficient pools. Given this, let's adjust the bandwidth parameter to gigabit speeds. Also, let's consider the base reward in another year (~5.2 XMR) or two (~3.2 XMR).

Running the numbers again, the cost in one year of attempting to prop up the medium block size by 100kB is only 0.00003467 XMR per block. If you assume a miner controls 10% of the network hash rate and assume that 1 XMR costs $100, this works out to only $0.25/day. The cost in another year drops further: 0.00002133 XMR per block or $0.15/day. If the benefit is that the pool is guaranteed extra space for 0-fee transactions to pay out miners, this is massively worth doing. All the pool would have to do is show a couple other pools how much optimization of costs can come by them all employing this strategy, a not altogether unthinkable thing, as this kind of miner collusion is cost saving to all involved, without becoming any more centralized. It remains to be shown that this benefit outweighs potential gains from the creation of a fee market.

> Furthermore, a block size that is economically meaningful with respect to demand from paying transactions actually benefits miners collectively by creating scarcity and fee pressure. It is not clear that there is an incentive for a miner to want to subvert this.

While I agree with this in theory, given the current design I don't see the easy establishment of a fee market in reality. This is a point I haven't discussed in detail, but I will expand on it here. This will take some time, and is my final point in this response. It also addresses a bit more some of what @JollyMort and I were discussing at one point in the other thread:

The block reward penalty's primary role is spam prevention, putting a cost on the expansion of the median block size, and therefore disincentivizing certain attack vectors. Without the penalty, miners could just include superfluous transactions sending coins to themselves or elsewhere either just for the hell of it or some malicious purpose.

A major effect of the block reward penalty is that miners are only incentivized to increase block sizes beyond the median size if there is financial incentive to do so. The most obvious incentive is if there are fee-paying transactions needing to be confirmed than can't fit into the median sized block, and the fees paid in those transactions outweigh the penalty associated with including them.

The Monero block reward penalty for block "A" is related to the median block size and the size of block "A" as such:

```
Penalty = BaseReward * (1 - BlockSize / Median) ** 2
```

This penalty does not scale in absolutes... The cost per kB to increase the median block size costs less the larger the median block size gets. An additional factor is that the base reward itself is always decreasing, but we can ignore this for now.

**Examples:**

Today, the base reward is in the ballpark of 8.24 XMR, and the median block size is in the ballpark of 100kB. This makes the penalty for increasing the block size by 1 normal TX (which I am going to approximate as 13kB):

```
Penalty = 8.24 * (113/100 - 1) ** 2 = ~0.14 XMR
```

I think we can all agree this is a problem, as most txs seem to pay a 0.001 XMR/kB fee, or ~0.013 XMR, which is an order of magnitude smaller than the penalty. This makes increasing the block size difficult because miners aren't really incentivized to do so unless users pay 10x fees. This also points to why the patch originally discussed was put forward and the design choice for 300kB, where the penalty to increase to 313kB is:

```
Penalty = 8.24 * (313/300 - 1) ** 2 = ~0.0155 XMR
```

This is approximately the same as the typical tx fee, and thus it is highly likely the median block size will be able to grow, *even without users paying increased fees*. This caveat is because blocks won't grow from exactly 300 to exactly 313, but likely through a more smoothed growth curve since txs aren't all exactly the same size, and thus blocks naturally vary over time even as they all contain similar numbers of txs.

Increasing by two transactions would cost:

```
Penalty = 8.24 * (326/300 - 1) ** 2 = ~0.062 XMR
```

and by three transactions would cost:

```
Penalty = 8.24 * (339/300 - 1) ** 2 = ~0.14 XMR
```

Clearly the penalty scheme's design is working: Each additional transaction beyond the median block size limit costs more than the previous, meaning that blocks will only grow quickly if transactions exist that pay higher than the minimum fee rate.

Okay, nothing too controversial so far, and ironically everything I've said pretty much agrees that 300kB is the right choice for the PR and that the penalty/minimum block scheme is not broken. But I believe that this whole discussion needs to be thought about more deeply given a longer term view than what I've just presented, an here's why:

As the median block size continues to increase, the penalty to further increase it by ~1 TX decreases:

* Median = 400kB, `Penalty = 8.24 * (413/400 - 1) ** 2 = ~0.0087 XMR`
* Median = 500kB, `Penalty = 8.24 * (513/500 - 1) ** 2 = ~0.0056 XMR`
* Median = 600kB, `Penalty = 8.24 * (613/600 - 1) ** 2 = ~0.0039 XMR`
* Median = 1000kB, `Penalty = 8.24 * (1013/1000 - 1) ** 2 = ~0.0014 XMR`

This is because the penalty is a function of the ratio of the block size to the median block size, rather than of the difference between the two. This might be a desirable trait, but I would argue this is in fact not at all desirable because the median block size can now grow much faster at the same penalty as before.

As an illustration, as currently devised the block reward penalty is the same for 1 extra transaction in a 300kB block as for 2 extra in a 600kB block, 4 extra in a 1200kB block, and 8 extra in a 2400kB block.

* Median = 300kB, `Penalty = 8.24 * (313/300 - 1) ** 2 = ~0.0155 XMR`
* Median = 600kB, `Penalty = 8.24 * (626/600 - 1) ** 2 = ~0.0155 XMR`
* Median = 1200kB, `Penalty = 8.24 * (1252/1200 - 1) ** 2 = ~0.0155 XMR`
* Median = 2400kB, `Penalty = 8.24 * (2504/2400 - 1) ** 2 = ~0.0155 XMR`

But the extra transaction fees collected with each step up also increase (0.013 XMR for 1 tx, 0.026 for 2, 0.052 for 4, and 0.104 for 8).

So trying to find that equilibrium where (fees minus penalty) is maximized becomes important. This code snippet (with moderate adjustments) allow you to find the number of extra TXs a miner would want to include to maximize (Extra TX Fees - Block Reward Penalty) for expanding median block sizes. I didn't flesh out a full function to find the maximum because it is easy enough to do so from visual inspection of what's printed out.

```python
MBS = 2400.
Ns = range(20,35)
for N in Ns:
    print(N, 0.013*N - 8.24 * ((MBS+13*N)/MBS - 1) ** 2)
```

A summary of the ideal # of normal fee paying TXs at various median block sizes is below:

| Median | # Approx Median TXs | Optimal # Extra TXs | Extra TX Fees | Penalty | Max(Fees - Penalty) |
| --- | ---:| ---:| ---:| ---:| ---:|
| 300kB | 23 | 1 | 0.013 XMR |  `8.24 * ((300 + 13*1)/300 - 1) ** 2` = ~0.0155 XMR | ~(0.0025 XMR) |
| 600kB | 46 | 2 | 0.026 XMR | `8.24 * ((600 + 13*2)/600 - 1) ** 2` = ~0.015 XMR | ~0.011 XMR |
| 1200kB | 92 | 7 | 0.091 XMR | `8.24 * ((1200 + 13*7)/1200 - 1) ** 2` = ~0.047 XMR | ~ 0.044 XMR |
| 2400kB | 185 | 27 | 0.351 | `8.24 * ((2400 + 13*27)/2400. - 1) ** 2` = ~0.176 XMR | ~0.175 XMR |

The takeaway here is this: the current mechanism does not really incentivize the creation of a fee market in the long term. As long as blocks are small, that fee market will exist to a very small extent, but as the median block size expands, I don't see how a fee market is incentivized. The base fee is already large enough to fund further expansion of block sizes, and expand them at a large rate (`(7+92)/92 = ~1.076` so ~8% growth at 1 MB blocks, or 15% growth at 2 MB blocks).

Now, this does not account for two things, which partially cancel each other out though I haven't run the numbers: 1) the base block reward will continue decreasing (~5.2 XMR in 1 year, ~3.2 XMR in 2 years, ~2 XMR in 3 years) which means the block reward penalty will decrease, and 2) the price of Monero could rise, which might mean a further adjustment to the minimum fee per kb would be needed. Anyone should feel free to play with those parameters to see what effects they have. Possibly a simple fix to this is to fix the minimum fee per kb to be in proportion to all of this, but that seems like it would just undercut mining profits and therefore doesn't seem like the best strategy.

## iamsmooth | 2017-03-18T04:25:46+00:00
What you are calling the 'base fee' is nothing more than a suggestion. It is only the underlying economics that can make such a fee sustainable. If the economics don't support it, the equilibrium fee could fall arbitrarily low (people will just bypass the relay limit one way or another).

The importance of back pressure in the form of a meaningful block size limit and penalty to increase it, is to limit supply and cause those wanting to transact to bid (at least mildly) for that space. If a miner keeps the block size unnecessarily high then it subverts that bidding process, and those transacting will be able to pay lower and lower fees, essentially to zero, destroying the penalty-free fee revenue that the miner in your scenario is trying to maximize. 

Even if the miner doing this doesn't like the fees going lower, there is nothing to prevent other miners from accepting those transactions into the additional free space that this action is creating. To suppose otherwise devolves to a 51% attack. 

Your comment about pools making payouts is an interesting one since that is a case where the miner itself is the one making the transactions and arguably would benefit from a lower fee equilibrium (that's basically what your claim here is saying). However, I am doubtful that pool payouts will ever be an economically meaningful share of transactions. To the extent they are now that is unrepresentative of a useful system.

Worth noting that as the block size goes _arbitrarily_ high (say gigabytes), the penalty becomes _extremely_ mild at the median, with a mathematical limit of zero. Possibly increasing value will address this, but possibly not. This may be a problem, but if so it is a distant one. 


## ArticMine | 2017-03-18T04:37:04+00:00
Reply to @bigreddmachine

I will first address the concern that miners have an incentive to maintain larger median block sizes. A rational miner will include the highest paying transactions first, so in reality it is lowest paying transaction(s) in the block that have to support the penalty. 

We can consider a situation where there is a mix of transactions that pay the minimum fee 1x and transactions that pay the next fee level 4x. For a median blocksize at 300000 bytes the 1x fee is not sufficient to support the penalty while the 4x fee does support the penalty at least for the first transaction. I am assuming a transaction size of 13000 bytes and that the transaction included just over the penalty boundary. Under these circumstances  for a miner to increase the blocksize and pay the penalty the block must consist entirety of 4x or higher fee transactions. If there are not enough 4x transactions in the mempool a rational miner will first add higher fee, then 4x fee transactions and then only add 1x transactions up to the median and not pay the penalty for the blocksize increase. Now let us contrast this with a situation where there are not enough transactions in the mempool. Under these circumstances there is little incentive for users to pay the higher fees, and the miner is presented only with say 1x fee transactions. The net result is that the fees paid to the miner after the penalty can fall by a factor of 4 or more. For a miner the penalty paying block becomes actually significantly more profitable since the miner in effects collects the penalty on the entire block not just on those transactions in the penalty area. Furthermore the deeper into the penalty, the more profitable for the miner the block becomes. The same rational miner argument also applies here. It is the most expensive part of the penalty that sets the price for the entire block. I do not see here the incentives for a miner to pad blocks with “0 fee transactions” since there is both a finite, although small cost, individually and a significant collective cost that exceeds the possible collective benefits to a miner of preventing the blocksize from falling to meet actual demand.   

I will now address the second much more fundamental concern. @bigreddmachine is of course correct in the assertion that there is no incentive for a fee market, if a fee market is understood in the Bitcoin sense of eventually having to replace the base emission as a source of funds for miner incentives. The critical difference here is a minimum base reward of 0.6 XMR per block in perpetuity. It is this minimum base reward and not fees that is relied upon to ensure miner incentives. Fees continue to serve the purpose the serve now, to deter spam and control the growth of the blocksize. To place this into perspective a 0.6 XMR per block  is currently approximately comparable to a 3 XBT reward per block in Bitcoin, if one considers the respective money supply of both crypto currencies .

## iamsmooth | 2017-03-18T04:42:17+00:00
@ArticMine 
> minimum base reward and not fees that is relied upon to ensure miner incentives

Not entirely accurate. Fees are an "incentive" for a miner to include the transaction in the block, avoiding various forms of bad behavior, and being an important part of the overall scheme (offsetting penalty, etc.). However, not the primary incentive to mine at all, which is the key distinction you are making (and with which I agree).

## ArticMine | 2017-03-18T04:47:16+00:00
To clarify. I mean fees as a replacement of the base block reward  when it comes to miner incentives. There are of course many other miner incentives that fees in the presence of a base block reward address.

## bigreddmachine | 2017-03-18T05:12:56+00:00
@ArticMine Expanding what @iamsmooth wrote a few minutes before you, isn't your 1x/4x scenario rendered meaningless in the long run? It would seem @iamsmooth is saying the 1x fee is essentially arbitrarily set, and not at all enforceable, but that miners won't take lower fees as long as they don't have to. By the same argument, fees wouldn't go from 1x to 4x but from 1x to ~1.1x, which would be enough to expand the median block size 1 tx at a time. It would seem the only reason they would go 1x to 4x is that's how the client is written, which does not seem to be a good reason. Also expanding on what @iamsmooth said, doesn't this also mean that as demand drops, fees shouldn't just drop to 1x but actually something smaller than that until the median block size decreases? Granted, the median block size adjustment adjusts down much faster than up, but there would still be a small lag I suppose. It would seem then that perhaps the overall conclusion of this entire discussion might be that the base fee rate should be a function of the median block size, since ultimately fees should be a functions of how to ensure a tx gets mined in a reasonable amount of time, which is entirely dependent on block size. If this is the case, then a decent part of my arguments are probably refuted, but it brings up an interesting question of the fee design in the client, and that perhaps a much better fee design could be implemented that is actually based on supply and demand. Is that making any sense?

## ArticMine | 2017-03-18T06:02:20+00:00
The base fee is proportional to (base block reward)  / (effective median blocksize). So for example at 600000 bytes the 1x fee is 1/2 of the 1x fee at 300000 bytes for a given base block reward. The same for the 4x fee etc. As the blocksize increases the 4x fee is needed for the same percentage increase in the blocksize; however this will include a greater number of transactions. It would be possible eventually to increase the blocksize with only 1x transactions but only at the 1x rate. If the blocksize falls the base fee increases accordingly so in a drop from 600000 bytes to 300000 bytes the fee rises back up to the 300000 byte rate corresponding to the new block reward. This is actually a further incentive for miners to not pad blocks with “0 fee transactions”. So the argument still applies but in the more generalized form where it is advantageous for the miner to allow the blocksize to fall; however in this case the miner would benefit from the higher penalty rate when the blocksize rises again. 

The minimum fees are to a degree enforced by the nodes in that they will not relay a transaction where the fee is below the minimum. This allows the nodes to protect themselves from a spam attack by not relaying transactions that are unlikely to be mined. Can the base fee for a given blocksize fall? Yes; however the fees are ultimately set by the penalty, so if the market finds a way to minimize the penalty for example by keeping fluctuations in the effective median blocksize to a minimum then this can happen. One must keep in mind that miners have no incentive to do this, but users may have this incentive. One way users may influence this for example is by paying a minimal fee and being prepared to wait a while for confirmation. Still this type of market behaviour may be more theoretical than practical. 

On another note. One cannot enforce minimum fees in the protocol since miners can pay “out of band” rebates to get around such a limitation.  

## JollyMort | 2017-03-18T10:59:28+00:00
>However, out of a lengthy discussion that took place, a larger issue (off topic to that PR) emerged and began to be discussed. Because it was largely off topic there, I am opening this issue where the discussion can hopefully continue.

I still don't agree there's an issue to begin with. Do we see any symptoms that the current setup could be problematic? Could we model exactly how it would be problematic? There are many assumptions being made but I fail to see a strong rationale behind them.

>Further, when the median block size grows during a demand peak, miners are incentivized to maintain that larger median block sizes than required once demand tails off by in effect stuffing blocks with 0-fee transactions.

Not quite. If you look at the min. fee formula you will see that the total fees (in xmr) per full block will remain constant for any given median, **as long as it's stuffed to 100% by TX-es which are coming from the network**. So really, a miner would want the median such that he can always fill them to 100% or more, otherwise he loses out. If there are TX-es coming in to sustain a block size of X, then a miner would want the median exactly at X, or even a little less becuase otherwise he'd be using his dummy TX-es to stuff the blocks which don't bring in revenue. See table below:

![block-stuffing](https://cloud.githubusercontent.com/assets/20967651/24071347/d2b8f2d6-0bcf-11e7-80e7-b47ddec8a232.png)


>This is approximately the same as the typical tx fee, and thus it is highly likely the median block size will be able to grow, even without users paying increased fees.

So what? It will not be able to grow **fast**, though. So, if there's a rush hour or whatever, people will want to use multipliers to get confirmed smoothly. Don't forget, it will not grow if there's nobody transacting because there won't be enough TX-es to fill the blocks. If there are enough TX-es, then obviously there's a demand for growth and it needs to grow, so where's the problem?

>This might be a desirable trait, but I would argue this is in fact not at all desirable because the median block size can now grow much faster at the same penalty as before.

It is desireable because if adoption drives (and block size is a good metric of adoption) the market price, and anything is fixed in xmr terms, then the price grows and we have a problem again and again. This should be a set-and-forget kind of thing and not something which should require constant supervision.

>The takeaway here is this: the current mechanism does not really incentivize the creation of a fee market in the long term. As long as blocks are small, that fee market will exist to a very small extent, but as the median block size expands, I don't see how a fee market is incentivized.

And why would we want a "fee market" at all? Fees are there to encourage rational use, that's it. Monero mempool wants to be empty.

Actually I made a similar table a few days ago, but the motive was to show how 300kB is "just enough" to make each increase "step" with x4 profitable, and that's how it was picked.

![median-increase 13kb-300kb](https://cloud.githubusercontent.com/assets/20967651/24071282/b80609a2-0bce-11e7-86da-5d6faef2353b.png)


## moneromooo-monero | 2017-03-18T13:51:08+00:00
> This is because the penalty is a function of the ratio of the block size to the median block size, rather than of the difference between the two.

We want that though, don't we ? Usage increase will be more geometric than linear as usage grows (ie, if monero use grows at 1% per fixed amount of time, then this "constant" rate of growth will mean a growing amount of extra txes per amount of time). This means that if we use the difference, then we'll end up unable to grow fast enough to meet demand.


## JollyMort | 2017-03-18T13:55:25+00:00
And likely the market price will follow the rate of growth in some fashion, so we'd want transacting to become cheaper in xmr terms to keep a reasonable real-world cost of transacting. I'd use a cheaper alt if I had to pay a growing amount of $/tx in minimum fees. Bitcoin's failure led people to Monero, and Monero failure would lead people to some xy solution. Let's not get overconfident.

## danrmiller | 2017-03-18T16:27:21+00:00
> I'd use a cheaper alt if I had to pay a growing amount of $/tx in minimum fees.

Monero offers features that may technically cost more to provide without harming the system than other networks. Other projects may be broken yet offer lower fees and there may be users who switch.

## JollyMort | 2017-03-18T16:41:12+00:00
Problem is in quantifying "harming the system". With my 50Mbit connection, theoretically I'd be fine until blocks of what, 90MB? From where are all those TX-es needed to lift blocks that high supposed to come if there's no adoption? How long until we reach that level of adoption? What connection will I have at that time? If there's adoption the market price will be higher and with it the cost of attack. Also, the system has tools at its hand which don't require changing a single line of consensus code. It's not like everyone would passively watch as the blocks creep up to 90MB.

Yes, others may be inferior but cheaper. But if we get it wrong, others might as well be equal/better but cheaper - like a clean Monero clone with just the difference in fee policy. Sure, there's the network effect, community support, etc. and massive shifts take time so it's a weak argument that you can move to "competition" just like that, but I just wanted to make a point that users can't be expected to tolerate crazy prices forever.

## bigreddmachine | 2017-03-18T20:30:06+00:00
Lots to reply to so I'll reply shortest to longest and also by branch of the topic:

@moneromooo-monero 
> > This is because the penalty is a function of the ratio of the block size to the median block size, rather than of the difference between the two.
> 
> We want that though, don't we ? Usage increase will be more geometric than linear as usage grows (ie, if monero use grows at 1% per fixed amount of time, then this "constant" rate of growth will mean a growing amount of extra txes per amount of time). This means that if we use the difference, then we'll end up unable to grow fast enough to meet demand.

Yes, maybe we do want that, if we assume usage increase will be geometric. And that's fine if that's the assumption. I think I was more trying to get to the point that this mean the growth of the blocks will be geometric, which might not be ideal long-term.  There's a limit to on-chain scaling somewhere, but we don't really need to debate where that is right now perhaps.

---

@JollyMort 
> And likely the market price will follow the rate of growth in some fashion, so we'd want transacting to become cheaper in xmr terms to keep a reasonable real-world cost of transacting. I'd use a cheaper alt if I had to pay a growing amount of $/tx in minimum fees. Bitcoin's failure led people to Monero, and Monero failure would lead people to some xy solution. Let's not get overconfident.

@danrmiller 
> Monero offers features that may technically cost more to provide without harming the system than other networks. Other projects may be broken yet offer lower fees and there may be users who switch.

@JollyMort 
> Yes, others may be inferior but cheaper. But if we get it wrong, others might as well be equal/better but cheaper - like a clean Monero clone with just the difference in fee policy. Sure, there's the network effect, community support, etc. and massive shifts take time so it's a weak argument that you can move to "competition" just like that, but I just wanted to make a point that users can't be expected to tolerate crazy prices forever.

Well, this is sort of getting at some of my motivation in discussing all this. I don't think Monero needs to be the cheapest if it is the most private. Along with that, Monero never really has been the cheapest, at least not in a long time. Did you see Roger Ver's tweet about moving $70000 for less than a penny (or something like that) with DASH? I don't really see a scenario where Monero could ever do that except the highly unlikely case where use skyrockets but the price doesn't. But I do agree that Monero should be as cheap as it can be, which if it is the most private, in many ways means it is the cheapest. With this, we have to be aware of the fact that if the price skyrockets, costs in terms of fiat likely skyrocket too, and then will be relieved if demand can push up the block size.

---

@JollyMort 
> Problem is in quantifying "harming the system". With my 50Mbit connection, theoretically I'd be fine until blocks of what, 90MB? From where are all those TX-es needed to lift blocks that high supposed to come if there's no adoption? How long until we reach that level of adoption? What connection will I have at that time? If there's adoption the market price will be higher and with it the cost of attack. Also, the system has tools at its hand which don't require changing a single line of consensus code. It's not like everyone would passively watch as the blocks creep up to 90MB.

If the bottleneck is strictly bandwidth, and you don't want to use your bandwidth for anything else, and you want to run a node full time which would mean you never have to play catchup, and you're willing to limit how many connections your node makes, then yes, the theoretical block size limit is quite high even at only 50 Mbps. But first, that's a lot of assumptions that likely aren't universal, and second, many people also face a data cap, which is sometimes as high as 1024 GB per month but often 2-10x smaller. Just getting one copy of every raw block puts these users at a 45 MB/block limit if they have the 1024 GB cap, but that's not really how the system works. In reality, even a node with lots of constraints in place on connections and the like is going to be capped at something closer to 2-4 MB per block before they simply can't operate a node from home. And that's if you assume they don't do other things with their internet connection. For example, the average Netflix users watched 47 hours per month (http://time.com/4186137/netflix-hours-per-day/), which at 3 GB per hour for full HD is already 141 GB per month used. Worrying about where that level of adoption comes from is kind of beyond this discussion, which is really mostly motivated by an overarching question of "Is the block reward setup capable of scaling the way we want it to?", and perhaps the answer to this is "yes", or maybe "yes but...", or maybe "no". Regardless, if the answer is or becomes yes, then all this becomes important, and if the answer is no, then maybe it isn't. But I'm definitely starting to ramble here so I'll move on, though happy to keep discussing the point if you're looking to.

Now, regarding the final bit of your statement, this gets to the core of my whole original post! Yes, the system does have the tools at its hand which don't require changing a single line of consensus code. It's called the block reward penalty + the min block size. But despite this, the PR originally prompting all of this *does change the consensus code*. I completely understand the rationale here... the RingCT hard fork increased the size of an average tx quite precipitously, and the adjustment algorithm wasn't adjusted to compensate for that. This PR attempts to compensate, which is great. My whole concern was that this seemed to go from "JollyMort is investigating" a few weeks back to "JollyMort has a draft that's almost done of his investigation" on Sunday to "PR accepted, fork next month" on Tuesday. That seems *really fast*, especially since a final version of your report was never discussed at length during a developer meeting. It might have been discussed on IRC after, I don't know, but my whole point in all of this was originally that the process that has always happened didn't seem to happen. Maybe I missed some bigger discussion. With all this, it's become clear to me that I need to state one last thing: in raising this question, I'm not saying what you did isn't good work, or making any negative claims against you or the work. I'm very appreciative of what you did. I just feel like the review and discussion of the work should have been a little more public and extended... more eyes are better.

---

Okay, and now after all that, I'm left with responding to @ArticMine and @JollyMort (your main post, with tables and lots of great detail).  I'm not going to quote everything but do want to highlight one new piece of information from @ArticMine which I was unaware of that puts everything I've been arguing in a different light:

> The base fee is proportional to (base block reward) / (effective median blocksize).

In other words, the base fee (or 1x fee, or whatever we want to call it) scales. I didn't realize this, though it makes sense and also get's to the other point of how tx fees aren't meant to enrich miners but (in conjunction with the block size penalty) are meant to support block size scaling.

This is really valuable, and a piece of the puzzle I was missing, primarily I think because this looks like it was fairly recently introduced? http://monero.stackexchange.com/questions/2531/how-does-the-dynamic-fee-calculation-work

And so it seems that some of my concern is alleviated. But, if you'll entertain me one last bit, I would like to raise one last question about this...

@ArticMine discussed how the median block size will increase when there is fee pressure to do so, and that fee pressure comes from there being transactions willing to pay for that expansion. In the statement, you argue that just one 4x transaction wouldn't be enough to increase the block size, because a logical miner would include that transaction first, and not last, and so it would require all high-paying txs to expand the block size. 1x fee paying txs would only be included if there weren't enough larger txs, and therefore wouldn't be able to pay for block size expansion. In other words, the cheapest fee paying tx is the one that has to pay for the increase.

Wouldn't this mean that the base tx fee should be a function of the cost to maintain a given median block size? This cost is essentially the minimum fee the lowest fee paying transaction in a median-sized block could pay before that tx wouldn't be economical. So shouldn't the "1x" fee be determined by essentially the same formula as the block reward, something like this:

```
# BR   -  Block Reward
# MBC  - Median Block Size
# TXKB - Size of a typical transaction in KB

Fee = BR * (1 - (MBS+TXKB)/MBS) ** 2
```

At 300kb and the current block reward, this is:

```
Fee = 8.2 * (1 - 313/300) ** 2  = 0.0155 XMR
```

This would mean that the base transaction fee is always attempting to pay to maintain the current block size, and that people could pay less but miners will only be incentivized to include those transactions if the present median block size is greater than demand or if we are at the minimum block size. And it would also mean that regardless of if demand goes up or down, the transaction is paying a fee that will be accepted? The current fee formula doesn't seem to be optimized for paying the actual price of the transaction.


## iamsmooth | 2017-03-19T07:38:41+00:00
@JollyMort 
> And why would we want a "fee market" at all? Fees are there to encourage rational use, that's it. 

Well it depends what you mean by fee market. I guess maybe that term carries some loaded meaning from Bitcoin or something, but to me the term is equivalent to people using multipliers and such (as you suggested is intended) when they care more about urgency than cost, and there is a need for such a market because block space at any time is finite and may not meet demand. That is _a form of_ a fee market.

Maybe the distinction is between a short-run fee market (which does exist in Monero) and a long-run fee market (which may not, depending on how you define it).

> Monero mempool wants to be empty.

As a long term average that may be approximately correct but it certainly won't be correct in the short term given fluctuations in tx demand or volume (and even block rate).

@bigreddmachine 
> Wouldn't this mean that the base tx fee should be a function of the cost to maintain a given median block size? This cost is essentially the minimum fee the lowest fee paying transaction in a median-sized block could pay before that tx wouldn't be economical.

That would actually tend to increase the block size, since block would then be over the median. It seems undetermined whether the 'lowest useful fee' should increase the block size or not. In practice that can't be enforced. If people want to submit cheaper transactions to miners that only fit into the free space (for example, when demand is decreasing and blocks are shrinking), there is nothing to prevent it (not relaying can only make this inconvenient).

Also, one detail. In general when considering adding another transaction the block will almost never be exactly at the median, it will generally be slightly below. So the fee you calculated is slightly more than necessary on average or even to be included 90% of the time (it is the worst case). I guess to 'maintain' a median, in a simple model you would want to assume half the transaction pays penalty, meaning it will be included half the time (resulting in a block above the median) and not included half the time (resulting a block below the median), in which case the median mostly won't change.

Sorry, I don't have time to read all of the longer replies on this issue right now. If there is something specific where anyone wants my input, please break it out and tag me.

BTW:
> Did you see Roger Ver's tweet about moving $70000 for less than a penny (or something like that) with DASH?

This doesn't mean that the actual cost of that transaction is less than a penny, it could also mean that the Dash network is extremely underutilized and there is no real longer-term economic viability behind Roger's experience at all (perhaps somewhat less so during the recent pump, but has generally been the case).

We have free (no penalty) space in blocks and if we really wanted to we could have < a penny per-tx fees for that space. As long as the network remains underutilized it would work fine. No one is designing or planning for that though.

## JollyMort | 2017-03-19T18:02:46+00:00
@bigreddmachine 

>If the bottleneck is strictly bandwidth, and you don't want to use your bandwidth for anything else, and you want to run a node full time which would mean you never have to play catchup, and you're willing to limit how many connections your node makes, then yes, the theoretical block size limit is quite high even at only 50 Mbps.

My point was just that there's plenty of headroom and that by the time adoption grows there may be more headroom. We just don't know, maybe that's why it's so frightening to many. Contrary to the popular opinion, the sky is not falling.

>Worrying about where that level of adoption comes from is kind of beyond this discussion,

It was not a worry, more like a relief. We discuss imaginary situation of block size of 90MB for which we'd really need to beat Bitcon's level of adoption. By the time that happens, we'll probably have LN or have thought of something else.

>But despite this, the PR originally prompting all of this does change the consensus code.

Yes, but it changes nothing of significance. I mean, 300kB could be achieved without any HF but it would be a pain to get there because of that spike due to txSize/minBlockSize ratio. **Whether we get to 300kB by consistent network use or by skipping to 300kB by a HF, it really makes no difference in the big picture of things.** It's just jumping to a network state, but such network state is allowed by the current rules anyway. The major difference is relieving everyone of many cycles of "oh why are the blocks not growing and my TX sits for hours" pains. If the system works as intended, it should never be as severe as it was recently because the blocksize would be able to respond more swiftly and go back down more swiftly, keeping some fee pressure but not sacrificing smooth experience for those willing to pay a little more for TX-es.

>My whole concern was that this seemed to go from "JollyMort is investigating" a few weeks back to "JollyMort has a draft that's almost done of his investigation" on Sunday to "PR accepted, fork next month" on Tuesday. That seems really fast, especially since a final version of your report was never discussed at length during a developer meeting. It might have been discussed on IRC after, I don't know, but my whole point in all of this was originally that the process that has always happened didn't seem to happen. Maybe I missed some bigger discussion. With all this, it's become clear to me that I need to state one last thing: in raising this question, I'm not saying what you did isn't good work, or making any negative claims against you or the work. I'm very appreciative of what you did. I just feel like the review and discussion of the work should have been a little more public and extended... more eyes are better.

Well, nobody asked me to do any research or counted on me to do it. My motivation was purely out of curiosity and because I saw a gap I thought I could fill. Whenever someone discussed the dynamic block size / dynamic fees there was a lot of unpolished ideas floating around on how it works - many of them wrong, and I really wanted to explain it to myself first and then show the results to the world - which I did. What happens after, happens.

But thanks to that research, now I have some good insights and reference to use in future discussion about the subject. The more I think about it, the transition formulas I proposed seem unneeded and maybe unnecessarily adding complexity. I feel like 300kB could fix the issue forever unless adoption would significantly lag behind the market price.

During this research, I realized how simple and elegant the system is and see some beauty in it and that's why I kind of *defend* it here now. Before, I had no idea. ArticMine really did a good job in devising the min. fee formula and I'm glad that I see it now. It's a perfect match for the penalty formula and I strongly feel like it doesn't need touching. But we can re-asses this as we go along. As I pointed out before, we will not wake up tomorrow morning and see 10MB blocks. All it takes is 51% miners to agree to keep them suppressed until they're ready for more. So really, I'm all for "let it play out and see how it works out". It worked just fine until RCT introduced the anomaly.

>Wouldn't this mean that the base tx fee should be a function of the cost to maintain a given median block size?

The cost to maintain is really anything >0. As long as there are >0 TX-es in the pool, a miner would want to stuff them all until 100% block size. If the offered fees are such that it's economic to go to 101% than he'd do just that. There's only the cost of increase, and that's where the "last" TX fee counts. I think [this](https://www.reddit.com/r/Monero/comments/5y5w2l/higher_payouts_from_pools_to_mitigate_mempool/deolxj1/?context=3) may give you some good insights.

If there's not enough TX-es, he wouldn't want to stuff with his because they don't earn him anything and he knows that when the median goes down so will the user's 1x fee auto-adjust higher and he'll earn more in total. For the miners, they'd really want to keep the blocks as small as possible because it's most economic for them. That's why I think this system is so clever.

The min. fee is currently such that, if mempool is full, it can sustain some minimum growth rate of 0.6-1.2% until blocks grow such that the mempool can be cleared. At that tipping point, the median ought to start going down because there are no more TX-es in the pool to stuff blocks with. So really, it's designed to kind of "breathe" in&out and find a balance somewhere. Tx/blocksize issue really means we're coughing water every time we'd have to move from 60kB to 300kB, thus the fix.

>I guess maybe that term carries some loaded meaning from Bitcoin or something

That's right, unfortunately.

>but to me the term is equivalent to people using multipliers and such (as you suggested is intended) when they care more about urgency than cost, and there is a need for such a market because block space at any time is finite and may not meet demand. That is a form of a fee market.

Agreed.

>As a long term average that may be approximately correct but it certainly won't be correct in the short term given fluctuations in tx demand or volume (and even block rate).

Agreed, it's designed to breathe.

## iamsmooth | 2017-03-19T21:02:40+00:00
@JollyMort
> If the system works as intended, it should never be as severe as it was recently because the blocksize would be able to respond more swiftly

I'm not so sure about this. In practice, the block size did increase. It takes a signifiant amount of time to do so under any reasonable conditions because the median window is 100 blocks (arguably too short) and you can't expect massive percentage increases to occur (penalties would be extremely high). There is a theoretical concern that if too many miners wanted to be more stubborn about not incurring penalties then the block size wouldn't grow, but that _hasn't actually happened_. In fact, the tx/blocksize issn't isn't altogether relevant here because even with smaller txs, without very high fees you will then just get very, very slow block growth (small txs at a small fee added to a block will only increase the median very slowly)

If there were enough demand to push it to 300K, it would have gotten there, in practice. It got to 100K+, multiple times. There's nothing harder about getting from there to 300K (actually easier, I think).

_There are going to be backlogs_ when demand increases by more than incremental amounts in a short period of time (hours/days), and it will. The short-term fee market is really the only way to address that (or a brute force approach of jumping the block size above observed demand). We've also considered some sort of RBF approaches to improve the short-term fee market.

## JollyMort | 2017-03-19T21:23:23+00:00
>I'm not so sure about this.

Neither am I. Thing is, the current min. fee is already kind of expensive. If adoption grows (but price doesn't) the min. fee ought to go down so people could be willing to use x4 or x20 to skip the line and make things move at the same time.

>just get very, very slow block growth (small txs at a small fee added to a block will only increase the median very slowly)

That's right, and min. fee gives incentive for a 0.6% increase but it's hard to tailor when TX-es are so big.

>If there were enough demand to push it to 300K, it would have gotten there, in practice. It got to 100K+, multiple times. There's nothing harder about getting from there to 300K (actually easier, I think).

That's also right, and it gets easier as long as the mempool is stuffed with "old" TX-es, ie those that offered a fee at a smaller median then it is "now". A "permanent" backlog like Bitcoin's simply can't happen.

>There are going to be backlogs when demand increases by more than incremental amounts in a short period of time (hours/days), and it will. The short-term fee market is really the only way to address that (or a brute force approach of jumping the block size above observed demand).

Yup. But it also doesn't make sense to have to brute-force every time. Hopefully this one-time bump will be enough to avoid getting stuck over and over again in high txSize/currentMedian zone.

>We've also considered some sort of RBF approaches to improve the short-term fee market.

Actually I tried to skip the line by attempting a double-spend-to-same-destination with a higher fee but it never got relayed - you have some guards against this? Anyway, to allow to re-issue a TX with only the fee changed would be nice for rush-hours.

## iamsmooth | 2017-03-20T08:36:57+00:00
> Hopefully this one-time bump will be enough to avoid getting stuck over and over again in high txSize/currentMedian zone.

Except that it hasn't gotten stuck, in practice. The one-time bump is more preventative, avoiding the problem just in case it would get stuck.

> Actually I tried to skip the line by attempting a double-spend-to-same-destination with a higher fee but it never got relayed - you have some guards against this? Anyway, to allow to re-issue a TX with only the fee changed would be nice for rush-hours.

Normally nodes won't accept (nor relay) a double spend so on relay first-seen takes precedence currently (until the older one expires). With RBF this would be changed to accept the new version if the fee is sufficiently higher. 

## Gingeropolous | 2017-03-22T15:52:31+00:00
Can anyone provide a nice wrap-up / summary of this discussion at this point? This convo needs a DAG. 

## bigreddmachine | 2017-03-22T15:57:38+00:00
@Gingeropolous - I don't know what DAG means but if no one else posts a summary up to this point by tonight, I can. Can't do a wrap-up because the conversation is ongoing (though in a couple day lull I suppose).

---

Edit - I haven't had the time to write a tl;dr yet, and might not until the weekend. if someone else has the time, great, if not, I promise to get to it soon^tm.

## bigreddmachine | 2017-03-26T05:46:42+00:00
@Gingeropolous as promised, here's my best attempt at a tl;dr. sorry that it took a few days. I've tried to stick to just presenting the conversation in a straightforward, factual, third-person way, but probably have glossed over some things or misrepresented someone somewhere. If I did, I promise it wasn't intentional, and part of the problem is that i'm trying to summarize a quite extensive discussion. Finally, this summary does not cover the original conversation on the PR referenced in the opening post here. That conversation wasn't too long, so you could read it if you want. probably not necessary.

---

## Summary of conversation up to here:

**bigreddmachine**:

Wanted to start a discussion on three concerns with recent PR and also with the block reward penalty and median block limit. Concerns:

1. Block penalties don't seem to allow blocks to expand; the penalty/fee difference does not seem to allow median block sizes to adjust as expected; PR aims to address this but might not be looking at the big picture
2. Miners might be incentivized to "stuff" blocks with filler transactions to keep the median block size high. these filler transactions are "free"
3. The PR linked changes consensus rules and therefore requires a hard fork, but was never discussed extensively in dev meetings or not seemingly peer reviewed. It went from draft to PR in a couple weeks and merged in 2 more days. That might be okay for now, but seems to call for a better process on consensus-changing PRs in the future.

**iamsmooth** and **ArticMine** give good responses and clarify a few things for **bigreddmachine**:

* Base block fees are no longer static, as of January, but adjust based on the base coinbase reward (which is ever decreasing) and also the median block size. This alleviates some of the original concerns. Also, fees are not a consensus thing - miners can accept whatever fees they want, and node operators can pass along low fee paying txs if they want.
* There's nothing wrong with "filler" transactions - they are just transactions and miners could use this type of transaction to their benefit theoretically. But they are still just transactions. Further, these might be counterproductive because miners should not want to artificially prop the median block size, as only a true median block size will allow them to maximize fees collected.

**JollyMort** adds to discussion with info from his simulations:

* Shows more evidence to support what ArticMine pointed out about miners wanting to be at a true median block size, rather than propping one up artificially, from a fee perspective.
* Also points out that block size growth speed is good when using the 4x fee multiplier.

---

Then a side discussion takes place about how fees should be low or people won't use Monero. Wasn't really too relevant here, but you can find it if you want.

Another discussion takes place about bandwidth and the maximum extent to which Monero could scale off chain. Didn't really get resolved, but also not super relevant so not writing more about it.

---

**bigreddmachine** replies to everyone up to this point, and basically says that he sees everyones points on concerns 1 and 2, but proposes one last question, essentially amounting to this:

- Why doesn't the dynamic fee algorithm reflect the true cost of a transaction, which is analogous to the cost of adding 1 transaction to a block that will maintain the current median?

The argument being that blocks will only include txs paying the highest fees, and also will only include transactions beyond the median size whose fees offset the penalty, and so therefore the minimum fee that will be included is at which pays for a block size increase of 1 TX. lower-paying txs cannot help expand the median block size, and therefore will only be included in blocks when demand is falling below-average.

**iamsmooth** responds to the posed question:

The model proposed (min TX fee = fee to add one TX to block) isn't quite right. You'd want something that maintains a median, so 50% of the time it adds an extra TX and 50% doesn't. Also blocks aren't all equal in size, there is variance about the median. Says a simply adjustment to the model might be that the base tx fee be that which pays for half the block reward penalty.

**JollyMort** replies to the original 3rd concern, that the PR was merged quickly:

No one asked him to research, he just did, found some good results, things happened. Thinks the PR could fix the issue over block size issues forever.

**iamsmooth** and **JollyMort** discuss whether this really is the ultimate fix, both somewhat conclude "hard to know for sure".

---

And that's pretty much where we are. 

Of the original 3 concerns, 1 and 2 were mostly alleviated, and the remaining bit was merged into the question about why the dynamic fee calculation doesn't reflect the cost of maintaining a median block. This question was discussed but in my opinion was not resolved.

The 3rd concern (the speed of the PR) was only addressed very limitedly, and wasn't resolved. But in the original post, **bigreddmachine** also said something like "maybe this point should just be discussed at the bi-weekly dev meeting" so perhaps it wasn't viewed as important to this thread.

Apologies if anyone feels misrepresented or if I missed somethign important, feel free to add a quick note if so. I would like to see the discussion moving forward address these last two parts that are still open.

## JollyMort | 2017-03-26T08:47:02+00:00
Nice summary. Regarding the last point:

>Why doesn't the dynamic fee algorithm reflect the true cost of a transaction, which is analogous to the cost of adding 1 transaction to a block that will maintain the current median?

It's because the cost "to maintain" is 0. If we would relay 0-fee TX-es, they could be used as stuffing to maintain some median. Even now, miners can add their own 0-fee TX-es to either optimize fees like pool payouts or play the game of maintaining the median. But then, as pointed above, they're not doing themselves any favors by stuffing the blocks for no reason because they'd earn more if they let the median drop to match actual fee-paying network load. Miners earn the most on 100%+ full blocks. It is in their best interest to match the block size such that there's never under-utilization.

Imagine that new TX-es are coming in at a rate of 5 TX / 2min. That means a miner can't build a block of 10 TX without adding his own TX-es because there's simply not enough user-made TX-es available to fill the blocks. But if the block size is 60kB, those 5 TX-es will be just right for 100%. However, if he artificially inflates block size to 120kB now they will be 50% full. BUT, the fee/TX will be 50% lower because user wallets auto-adjust to the current median! So by artificially doing a x2 on blocksize, ALL miners would suffer a 50% loss on fee revenue.

Since right now, we DO have a minimum fee and it reflects the cost of increasing the median for 0.6% I don't see how it should be adjusted to match what you propose. It could be made to reflect the cost of increasing the median for a fixed amount of kB, like 1 TX size. That would make the min. fee become cheaper at a faster rate than now! We are still young, so it's hard to say whether that would make sense in the long run but more importantly - the min. relay fee can always be adjusted without a HF so it can be done at any time if there's a need.

## Gingeropolous | 2017-03-31T06:29:03+00:00
Excellent summary - thank you for putting it together. It clears up a lot of things for me actually - Reading this now, I finally understand the brilliance of the decreasing min fee in relation to the block size: In addition to decreasing minimum network fees in response to perceived Monero network usage, it also prevents block padding (miners putting "fake" transactions in blocks with no fees), because if the miners collude to do that, the network will accept lower fees from the regular users. 



## iamsmooth | 2017-04-24T09:47:16+00:00
Good discussion and summary. Maybe this issue can be closed?


## bigreddmachine | 2017-04-24T14:25:00+00:00
Well... I don't know that everything was ever fully addressed/agree on, but I won't have the time for another month or two to build out a simulation to support some of my points, so I guess we can close it for now and then I'll bring something up either here or on the Research Lab page when I have more to talk about.

## UkoeHB | 2020-02-08T01:11:02+00:00
For anyone else doing research like me. It seems the discussion here was incorporated into the v8 protocol hardfork.

The current dynamic minimum fee is based off the amount required to offset the penalty incurred by a reference transaction that gets added when the default penalty free zone is full of transactions. The reference weight is 3000 bytes, the default penalty free zone is 300kB, and a typical 2-in/2-out tx is around 2600 bytes. This means the minimum fee, using this formula, will always be enough to, if all transactions use exactly the minimum, create blocks at least 1% larger than the contemporaneous median.

# Action History
- Created by: bigreddmachine | 2017-03-17T21:09:20+00:00
- Closed at: 2017-04-24T14:25:03+00:00
