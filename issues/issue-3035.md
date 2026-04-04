---
title: increase ringsize / block time
source_url: https://github.com/monero-project/monero/issues/3035
author: ghost
assignees: []
labels: []
created_at: '2017-12-30T18:18:02+00:00'
updated_at: '2018-09-14T12:24:58+00:00'
type: issue
status: closed
closed_at: '2018-09-14T12:24:58+00:00'
---

# Original Description
With bulletproofs coming in a few months wouldn't it make sense to increase the min rigsize to 10 at v7? To damper the increase in block validation costs, blocktime can be changed to 4 min (along the necessary emission curve parameters so it would remain intact like the change from 1m to 2m).

# Discussion History
## Gingeropolous | 2017-12-31T18:25:00+00:00
Ringsize 10 seems reasonable, based on gut feeling. Blocksize increase doesn't seem useful (same amount of transactions just in 1 block instead of 2). 

## b-g-goodell | 2017-12-31T19:33:13+00:00
I think we should do this:

1. For spring HF, we should not implement any changes to our ring ct or range proofs yet. I don't think we should implement any changes yet because I believe further code review will be more valuable than pushing out an under-reviewed scheme. 

2. I do think we should implement a **uniform ring size** for Spring HF.  One could ask "why shouldn't users be able to set their own levels of privacy?" but we don't allow users to set key length, for example, or number of rounds of chacha encryption during multisig (or whatever). I view ring size as a security parameter: everyone should agree on one ahead of time. And I don't really care what the uniform ring size **is**, although I think something between 8 and 16 would be a good choice for now. The specific number should be chosen based on some worst-case computational power assumptions plus some recent transaction throughput historic rates on the Monero network (with a healthy wide margin).

3. Until the autumn HF, we do rigorous code review on bulletproofs. We pull the trigger on implementation if and only if we still think they are mathematically correct, secure, and correctly coded. 

4. Also until the autumn HF, we investigate efficient implementations of RTRS RingCT (exploiting multi-exponentiation on our elliptic curve), and investigate overall timing possibilities of RTRS RingCT. We look at how much of a PITA it will be to change monero's key structures accordingly, we look into multisig/threshold versions of RTRS RingCT, we do a full-scale plausibility analysis. By the time the autumn HF rolls around, we should have an expectation about whether it would be worth implementing RTRS RingCT at all (it may be the case that despite their efficient scaling in space complexity, they are just too darn slow to ever make it faster to sync new nodes). 

5. I think there are some reasons we might relate the block arrival rate to transaction verification time, but I think I would need a bit of elaboration in order to really understand where you are going with that.

## ghost | 2018-01-01T11:56:52+00:00
@b-g-goodell I have not run tests, I'm borrowing the logic from Aeon that uses 4min blocks and aims to become mobile friendly, larger blocks over a longer period of time would reduce overhead to people running nodes on their phones considering how cpu-intensive ringct is. I agree on all fronts, the relatively low and pick-able ring-size remains a relative vulnerability. Meticulous code-review is a hallmark of Monero now, the Multisig implementation is a good example of that and I bet most of the community would agree as much as we need bulletproofs for reducing fees and bloat, thanks for all your work and Happy New Year to the entire Monero team.

## SamsungGalaxyPlayer | 2018-01-02T00:20:56+00:00
This was previously discussed in the other thread, but is there any argument that increasing the ringsize will have a quantifiable increase in privacy? Or are these benefits still theoretical?

## stoffu | 2018-01-02T13:10:26+00:00
@lethos3 
> larger blocks over a longer period of time would reduce overhead to people running nodes on their phones considering how cpu-intensive ringct is.

Just to be clear: the verification cost of RingCT is the same regardless of the block time. Aeon's 4 min block time means that the number of PoW hashes a full node needs to compute (verify) per day is half compared to that of Monero. The magnitude of this cost reduction may become less significant given the high cost of RingCT verification, but I'm not exactly sure.

## danrmiller | 2018-01-02T14:47:11+00:00
But high verification costs effectively shorten the block interval because you now have less time to propagate the verified block.

## xeyleukfnd | 2018-01-02T15:09:14+00:00
@SamsungGalaxyPlayer 

> This was previously discussed in the other thread, but is there any argument that increasing the ringsize will have a quantifiable increase in privacy? Or are these benefits still theoretical?

ring signatures leave a trace in the sense that there is one chance over / (insert ringsize here) that your input came from a specific output. so I would say that increasing the ringsize will have a quantifiable increase in privacy

if someone (big exchange, LE, chain analysis) knows a lot of outputs, then they have a real chance to uncover other transaction inputs (not their amounts). monero is also mostly speculation and if a lot of transactions are some sort of EABE, EAE or EE then chain analysis could have a lot of known outputs. so even if some privacy freaks are using a high ringsize, a low (and default) minimal ringsize only helps chain analysis to grow their known outputs over time. they can also uncover your transaction inputs in the future if they have more outputs to do so (through e.g. future DNM seizures or demanding peoples wallet to let them cash out). so some transactions who are private today may not private in the future any more.

my gut feeling is that a minimum ringsize of 10-15 (together with 2-3 fixed higher ringsizes to choose from, e.g. 40, 85, 150) would be currently way better, if we like to do anything against this issue.

## SamsungGalaxyPlayer | 2018-01-02T23:55:17+00:00
@xeyleukfnd I am familiar with these sorts of attacks. I'm asking whether any of them have been quantified. Of course, it would increase from 1 in 5 to 1 in 10, but this isn't specific enough.

## xeyleukfnd | 2018-01-05T02:43:00+00:00
@SamsungGalaxyPlayer I don't know how we could ever quantify these. I think we should just assume a worst case (more or less), which would probably be that coin analysis will know something between 90% and 99% of outputs _in the future_ - I cannot imagine that they know that much today.
  
  

## iamsmooth | 2018-01-07T17:37:57+00:00
@b-g-goodell 
> By the time the autumn HF rolls around

I like your overall plan but:

1. Remember that "by the time the autumn HF rolls around" means summer, to have time for a reasonable code freeze and testing period
2. For similar reasons we need a decision "soon" on the proposed fixed ring size. 

## b-g-goodell | 2018-01-11T13:39:55+00:00
@iamsmooth 1) Yep! 

2)  See my comment [here](https://github.com/monero-project/monero/issues/3069)

## SamsungGalaxyPlayer | 2018-02-17T21:40:40+00:00
I have attached some images below showing what happens to the network is a certain proportion of TXOs are compromised. Keep in mind that this assumes the attacker has this proportion equally spread across the TXO set (eg: same x% of both newer and older inputs). The wallet software prioritizes newer outputs in the selection process. Currently, 50% are selected from the past 1.8 days. Thus, an attacker could hold the following TXO sets to get 50% of the available inputs for selection (though of course not limited to just these):

1. 100% TXOs before 1.8 days
2. 50% TXOs before 1.8 days, 50% TXOs within 1.8 days
3. 100% TXOs within past 1.8 days

I think the most important scenarios to plan for are 2 and 3, since they either include a consistent proportion of TXOs or a spam attack for a large amount in single waves.

Below are the images for ringsizes 5-10 for transactions that would be sent at the specific point in time. It includes the probability of chain reactions where newly revealed inputs would contribute towards revealing others:

![image 1 ringsize 5](https://user-images.githubusercontent.com/12520755/36345804-97fac274-13f7-11e8-9e74-26cb2914c05b.PNG)
![image 4 ringsize 6](https://user-images.githubusercontent.com/12520755/36348312-88e783cc-1432-11e8-9d19-7880430a2e25.PNG)
![image 2 ringsize 7](https://user-images.githubusercontent.com/12520755/36345805-9809d1f6-13f7-11e8-97d3-fa7beb2bc627.PNG)
![image 5 ringsize 8](https://user-images.githubusercontent.com/12520755/36348313-8dfa1fbe-1432-11e8-9877-acff4d372ccf.PNG)
![image 6 ringsize 9](https://user-images.githubusercontent.com/12520755/36348314-8e08dba8-1432-11e8-82d8-9d2c8ff2eb0a.PNG)
![image 3 ringsize 10](https://user-images.githubusercontent.com/12520755/36345807-98191008-13f7-11e8-86f2-eaea3f681b7b.PNG)

Increasing the ringsize is the best way to protect users from many attacks, including key image association attacks. While a large ringsize does nothing to protect these transactions with matching key images, it protects other transactions.

---

[It has been observed](https://forks.network/dashboard/db/bch-btc-fork?orgId=1) in substantial forks such as BCH that a similar number of UTXOs can be spent. In my opinion, it should be prudent to assume that Monero should withstand attack from 50% compromised inputs, at the minimum. As shown in the image above, ringsize 7 reduces this risk to ~1.5% of all transactions, whereas ringsize 10 reduces this risk to ~0.2%. Ringsize 10 is more effective at protecting the network where 70% of the inputs are compromised than ringsize 5 does at protecting the network where 50% are compromised.

## iamsmooth | 2018-02-18T04:27:09+00:00
@SamsungGalaxyPlayer Your analysis considers only benefits not cost. How much do these proposed increased ring sizes increase chain size, verification time, bandwidth usage, etc. including after bulletproofs are activated? How does it compare in terms of both benefits and costs with churn (for example, one step with a smaller ring size at each step) against various types of attackers/attacks?



## SamsungGalaxyPlayer | 2018-02-18T05:16:38+00:00
@iamsmooth I am only considered with this attack, which is essentially outlined in MRL-0001. The key image exploit is effectively a new mechanism to introduce this attack. My primary concern is making sure that the Monero network is resilient against large-scale attack. I believe it is reasonable for up to 50% of the output set within the likely selection period to be compromised with a widely-used chain split attack. I think it is absolutely necessary that Monero provides strong protections in this case.

I will get into the negatives of increasing the ringsize later, but let me start of by explaining why I feel the issue is relatively dire.

Refer to my comment above for the probability that transactions have all their decoys known to be false (SUM column) for a proportion of compromised outputs among those that will be likely selected (first column).

If a chain split temporarily compromised 50% of the outputs, it would completely ruin the ring signature for the proportion of transactions at that point:

| Ringsize | Proportion Compromised | Transactions Compromised per Day with Current Volume
| ------------- | ------------- | ------------- |
| 5 | 6.251431% | 226
| 6 | 3.125003% | 113
| 7 | 1.5625% | 56
| 8 | 0.78125% | 28
| 9 | 0.390624% | 14
| 10 | 0.195314% | 7

You can see why I recommend increasing the ringsize to at least 7 or 8 to reduce the impact of this large-scale attack, which is essentially an onslaught of 0-mixin transactions.

# Disadvantages

The most notable disadvantage of increasing the ringsize is the additional transaction size. As a consequence, transactions will cost slightly more. I took [previous data](https://github.com/monero-project/monero/issues/1673#issuecomment-277566744) collected by @kenshi84 and plotted it in a regression to find that the (deprecated yet still proportionally the same) fee for a a ringsize x is: y=0.0002x + 0.022. Thus, the following relationship occurs:

| Ringsize | % Increase in Size & Fees Over Ringsize 5 | Value on Line
| ------------- | ------------- | ------------- |
| 5 | 0% | 0.023 |
| 6 | 0.87% | 0.0232 |
| 7 | 1.74% | 0.0234 |
| 8 | 2.61% | 0.0236 |
| 9 | 3.48% | 0.0238 |
| 10 | 4.35% | 0.024 |

You are reading this correctly. In order to increase from ringsize 5 to 10, it will add 4.35% to the total transaction size. The other values are in the table. If we don't want to make the jump to 10, I think the jump to 7 or 8 is highly warranted.

# Conclusion

Chain splits pose potentially great threats to Monero. We need to make sure Monero's ring signatures are resilient enough to protect users. For a modest increase in fees and transaction size, we can be much more assured that Monero's ring signatures are prepared for large chain split attacks.

It provides additional benefits regarding churning, etc., but I think the decision makes sense even without considering these benefits.

## iamsmooth | 2018-02-18T08:08:10+00:00
> I took previous data collected by @ke nshi84 and plotted it in a regression to find that the (deprecated yet still proportionally the same) fee for a a ringsize x is: y=0.0002x + 0.022. Thus, the following relationship occurs:

I'm pretty sure that was pre-bulletproofs. It needs to be reworked.

This size argument also does not consider verification time (at least not directly; given that most of these things are so far linear, it may be somewhat close).

> It provides additional benefits regarding churning

i'm not convinced, at least when considering the issue broadly. Churn has the potential to increase the anonymity set exponentially and increasing ring size only linearly. There are advantages and disadvantages to each. We need a more comprehensive analysis here, including the effect of bulletproofs (very large range proofs are definitely bad for churn; bulletproofs reduces this disadvantage a lot).

## endorxmr | 2018-02-18T15:48:39+00:00
As a potential counter to the MoneroV split: would it make sense for Monero-only users to churn their wallets a couple of times for a few days right after the split? That way, if enough people do it, we will be generating a significant amount of fresh inputs for others to use, and the forked chain won't be able to taint them.
By churning repeatedly, (possibly by sending only partial sums, rather than the whole wallet every time, in order to mix the ins and outs as much as possible), each user would be catching so many inputs and outputs in his wake that it would be significantly harder to comprimise his operations, even if some of those inputs get deanonymized by the split chain, and the outputs of the churns would be safe for others to use as decoys.

Does that make sense?

## SamsungGalaxyPlayer | 2018-02-18T18:05:00+00:00
@iamsmooth I think the inclusion of bulletproofs is irrelevant. The ability for ring signatures to mitigate large-scale attack is not dependent on bulletproofs. I understand your point about cost-benefit analysis, but this can be re-assessed for the bulletproof hardfork. We have an imminent threat to the network here that can be substantially mitigated at little relative cost. We should take action, even if this may mean adjusting it later.

I agree that churning is important, but my point is that this bring benefits independent of churning. Churning doesn't work very well if a large proportion of the outputs are compromised, and it provides little to no benefits to those who do not churn. Simply increasing the ringsize benefits everyone, including those who churn and those who do not churn.

@endorxmr a potential counter to the attack is to have Monero users "churn" their funds to make up a large proportion of the percentage of outputs, yes. However, keep in mind this is significantly more expensive than simply raising the ringsize slightly for the same effect. I suggest simply changing the ringsize so the network can have a built-in, (mostly) passive defense mechanism.

Eg: suppose 2,000 tx needed to meet acceptable proportion. (2000)(0.023) = 46
Suppose 4,000 tx simply used ringsize 10 (4000)(0.024-0.023) = 4


And finally, just to make sure there is no confusion, I do not support increasing the block time, as was introduced by OP.

## iamsmooth | 2018-02-18T21:25:43+00:00
> I agree that churning is important, but my point is that this bring benefits independent of churning.

The benefits are not independent. The cost-benefit is intertwined. For example, more expensive individual transactions discourage churning.

> Churning doesn't work very well if a large proportion of the outputs are compromised

This sees false to me, although against that particular attack it may be _slightly_ less effective. One transaction with ring-size 10 has foreign 9 outputs that need to be compromised to become traceable. One churn (two transactions) with ring size 5 has 8 foreign outputs that need to be compromised.

Cost-benefit is important.

> I understand your point about cost-benefit analysis, but this can be re-assessed for the bulletproof hardfork

If your suggestion is to make an immediate change for the hardfork that is already late for code freeze then I would object to it as no analysis of costs (other than size) has been made. I feel at this point that are verification costs are bordering on wildly out of control, echoed by complaints from users who find it much too slow to sync an node and use public nodes instead (though also somewhat  lacking in analysis, at least with respect to effects other than user complaints about syncing). This is directly resulting in high load and costs on (uncompensated) public nodes and a weaker p2p network.

I agree with your point that there are issues with chain split forks, but I view the proposed solution as still numerically arbitrary. _Assuming_ (!) 50% of outputs exposed, according to your chart above, you have roughly 6% traceable at ring size 5 and 0.2% at ring size 10. 0.2% seems so much better than 6% this almost seems like a free lunch (though of course in terms of costs it is not free) but tinker with the numbers, say push up the exposed share to 80% or down to 20%, and it all looks very different. In terms of chain reactions (the primary concern of MRL-0001), 6% is not a significant increase on the 50% that is already known (recall that ring size 5 is _already_ an arbitrary and defensive increase over the actual minimum required to prevent sustained chain reactions, which is >2). In terms of personal impact on users, reducing to 0.2% does not matter if you are one of the 0.2% (and certainly some people will be, even _every single day_). 

The brute force solution of just increase every ring size (and therefore costs) is not that interesting to me, at least not without a careful analysis of those costs. I'd rather see other solutions that do not (certainly) increase costs directly along with any (uncertain) benefit. People who are highly concerned can churn which can easily (with 2-3 steps) reduce the risk far below even 0.2%


## SamsungGalaxyPlayer | 2018-02-18T22:06:55+00:00
@iamsmooth 

> For example, more expensive individual transactions discourage churning.

Actually, a larger ringsize *decreases* the expenses related to churning. Users have to make fewer transactions to achieve their desired anonymity set. These fewer transactions speed up the churning process. As @knaccc documented in #1673, increasing the ringsize from 5 to 10 reduces the number of transactions for "high" privacy from 7 to 4. It cuts the wait time from 2h20mins to 1h20mins. The slightly higher per-transaction cost is significantly offset by the fewer transactions required. A higher ringsize absolutely benefits people who churn the *most*, since they need fewer transactions to get a given desired anonymity set.

The MRL has not stated whether churning is even something you should do. It is a far greater theoretical benefit than the decoys in a ring signature documented since MRL-0001.

Luckily, the complexity of changing the code from ringsize 5 to another number is very low, so it should not require any serious auditing. Since code is still being merged now, including the significantly larger change for a different PoW algorithm, this is incredibly minor and can be done with little effort if enough people agree.

The *worst* thing for the Monero network to endure during the time of the chain split is for people to send multiple transactions for fear of their ring signatures being compromised. The cost of one transaction is far greater than the cost a few additional inputs.

I am hoping to have some MRL people chime in here. Earlier in the thread, Brandon Goodell recommended 8-16. My recommendation is to come in at the very lowest end of this: 8. An a situation where 50% of the "weighted output" selection is compromised, an increase from 5 to 8 would reduce the number of compromised transactions per day by about 88%.

> In terms of personal impact on users, reducing to 0.2% does not matter if you are one of the 0.2% (and certainly some people will be, even *every single day*).

I disagree with this argument. The idea that we can't mitigate risk just because some risk remains is... counterproductive.

## knaccc | 2018-02-19T18:39:35+00:00
I just wanted to share some javascript source code for easily calculating transaction sizes for different ring sizes. When the size of bulletproofs becomes known, this source code can easily be modified by altering the line that adds range proof sizes (currently 6176 bytes per output). Paste this code into your web browser's javascript console to easily execute it.

```
var inputs = 2;
var outputs = 2;
var ringSize = 5;
var txSizeBytes = 0;
txSizeBytes += (1 + 1); // tx version and unlock time=0
var inputOffsetsBytes = (3 * ringSize); // 3 byte varint per input offset per ring member
txSizeBytes += (inputs * (1 + 1 + 1 + inputOffsetsBytes + 32)); //type, amount=0, ringsize varint, input offsets, key image
txSizeBytes += (outputs * (1 + 1 + 32)); // amount=0, type, output public key
txSizeBytes += (32 + 4); /* 4 is a guess*/ // field lengths, txpubkey and sometimes an integrated address
txSizeBytes += (1 + 5); // tx type and tx fee
if(inputs>1) txSizeBytes += (inputs * 32); // pseudoouts, only for rct type 2 (multiple input) transactions
txSizeBytes += (outputs * 64); // ecdhinfos
txSizeBytes += outputs * 32; // outpks
txSizeBytes += outputs * 6176; // range proofs
txSizeBytes += inputs * ((64 * ringSize) + 32); // mlsags
console.log('Transaction size in bytes: ' + txSizeBytes);
```


## SamsungGalaxyPlayer | 2018-02-19T19:46:18+00:00
@knaccc this is awesome, thanks! Do you happen to have any data on approximate validation time?

## knaccc | 2018-02-19T20:47:28+00:00
@SamsungGalaxyPlayer Hopefully my notes are accurate. I have it noted as follows:

The main verification cost is for the MLSAGs and range proofs.

MLSAGs, per ring member, require 4 scalarmults and 2 scalarmultbases. 10k Scalarmults take 2.46 seconds, and 10k scalarmultbases take 1.50 seconds on my Macbook Pro.

Range proofs cost 128 doublescalarmultbases per output, where 10k doublescalarmultbases take 2.28 seconds.

The code to compute verification time is therefore:

```
var scalarMultTimeSecs = 2.46/10000;
var doubleScalarMultBaseTimeSecs = 2.28/10000;
var scalarMultBaseTimeSecs = 1.50/10000;
var inputs = 2;
var outputs = 2;
var ringSize = 5;
var mlsagVerificationTimeSecs = (inputs * ringSize) * (4 * scalarMultTimeSecs + 2 * scalarMultBaseTimeSecs);
var rangeProofVerificationTimeSecs = outputs * (128 * doubleScalarMultBaseTimeSecs);
console.log('Verification time for MLSAGs (ms): ' + mlsagVerificationTimeSecs*1000);
console.log('Verification time for range proofs (ms): ' + rangeProofVerificationTimeSecs*1000);
console.log('Verification time per transaction (ms): ' + (mlsagVerificationTimeSecs + rangeProofVerificationTimeSecs)*1000);
```

That works out to 13ms for the MLSAGs, 58ms for the range proofs and therefore an overall 71ms transaction verification time for a 2 input, 2 output transaction at ring size 5.

If @b-g-goodell can provide EC mult counts for bulletproof verifications, we can then figure out timings for transactions that use bulletproofs instead of the existing range proof scheme.

Btw it has been mentioned that batch verification can speed up bulletproof verification through multi-exp savings. I'm not sure if this saving can be applied to MLSAGs, so I'm assuming not for now. If the saving doesn't apply to MLSAGs, then the MLSAG verification times would be more burdensome to nodes syncing from scratch than bulletproofs would be.

## SamsungGalaxyPlayer | 2018-02-19T23:26:58+00:00
All right, so here is the final mega table of the specific ringsizes and what they bring. Assumes 50% of outputs in the "weighted output" set (those likely to be selected) are compromised, 1 input, and 2 outputs.

| Ringsize | Prop. Compromised | Transactions Compromised/Day w/Current Volume | Transaction Size | Size & Fee Increase Over Ringsize 5 | Verification Time(s) | Verif. Increase Over Ringsize 5
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 5 | 6.251431% | 226 | 13058 | 0% | 0.064788 | 0% |
| 6 | 3.125003% | 113 | 13125 | 0.51% | 0.066072 | 1.98% |
| 7 | 1.5625% | 56 | 13192 | 1.03% | 0.067356 | 3.96% |
| 8 | 0.78125% | 28 | 13259 | 1.54% | 0.068640 | 5.95% |
| 9 | 0.390624% | 14 | 13326 | 2.05% | 0.069924 | 7.93% |
| 10 | 0.195314% | 7 | 13393 | 2.57% | 0.071208 | 9.91% |

[Link to Excel document with the data and calculations (download to edit and view formulas)](https://1drv.ms/x/s!AjOt8D-0YjBHgblk6lOraHi2QUp5RQ).

Anything else you want @iamsmooth?


## knaccc | 2018-02-20T12:39:39+00:00
@SamsungGalaxyPlayer There is a small error in the spreadsheet. It looks like your formula does not take the number of inputs into account when calculating MLSAG verification time. For ring size 5, 2 inputs and 2 outputs the verification time should be about 71ms. There are 10 ring members in total for a transaction with 2 inputs at ring size 5.

The transaction fees also look off to me. Here is code that I've written in the past to determine fees (taking into account the KB fee boundary):

```
var inputs = 2;
var outputs = 2;
var ringSize = 5;
var txSizeBytes = 0;
txSizeBytes += (1 + 1); // tx version and unlock time=0
var inputOffsetsBytes = (3 * ringSize); // 3 byte varint per input offset per ring member
txSizeBytes += (inputs * (1 + 1 + 1 + inputOffsetsBytes + 32)); //type, amount=0, ringsize varint, input offsets, key image
txSizeBytes += (outputs * (1 + 1 + 32)); // amount=0, type, output public key
txSizeBytes += (32 + 4); /* 4 is a guess*/ // field lengths, txpubkey and sometimes an integrated address
txSizeBytes += (1 + 5); // tx type and tx fee
if(inputs>1) txSizeBytes += (inputs * 32); // pseudoouts, only for rct type 2 (multiple input) transactions
txSizeBytes += (outputs * 64); // ecdhinfos
txSizeBytes += outputs * 32; // outpks
txSizeBytes += outputs * 6176; // range proofs
txSizeBytes += inputs * ((64 * ringSize) + 32); // mlsags
console.log('Transaction size in bytes: ' + txSizeBytes);
var blockSizeLimit = 600000;
var medianBlockSize = blockSizeLimit/2;
var totalSupply = 15742767;
var emission = totalSupply * 10e12;
var baseReward = Math.max(0.6, 1e-12 * ((Math.pow(2, 64)-1) - emission*1e12) * Math.pow(2, -19));
var dynamicFee = 2e9 * 60000 * baseReward / (medianBlockSize * 10e11);
var txSizeKB = Math.ceil(txSizeBytes / 1024);
var txFeeXmr = txSizeKB * dynamicFee;
var txFeeXmr4xMultiplier = 4 * txFeeXmr;
console.log('4x multiplier fee (xmr): ' + txFeeXmr4xMultiplier);
```

## SamsungGalaxyPlayer | 2018-02-20T16:58:38+00:00
@knaccc I have updated the Excel document to account for a variable number of inputs. I updated the description of the table to make clear that this is for 1 input and used the code you provided for the transaction size. Here is another table for the change in verification time in ms for a different number of inputs:

| | 1 Input | 2 | 3 | 4 | 5 | 6
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Ringsize 5 | 65 | 71 | 78 | 84 | 90 | 97 |
| 6 | 66 | 74 | 81 | 89 | 96 | 104 |
| 7 | 67 | 76 | 85 | 94 | 103 | 112 |
| 8 | 69 | 79 | 89 | 99 | 110 | 120 |
| 9 | 70 | 81 | 93 | 105 | 116 | 128 |
| 10 | 71 | 84 | 97 | 110 | 123 | 135 |

## SamsungGalaxyPlayer | 2018-02-24T20:23:50+00:00
[I've updated my Excel document](https://1drv.ms/x/s!AjOt8D-0YjBHgblk6lOraHi2QUp5RQ) with a summary of the details for compromised transactions, size and fees, verification time, and churning time and fees. You can manipulate the top 4 variables (and other derived variables lower in the data section).

![ringsize 7 details](https://user-images.githubusercontent.com/12520755/36634663-7f328c74-196d-11e8-8672-f1b142ab0481.png)

## iamsmooth | 2018-02-25T01:01:57+00:00
@SamsungGalaxyPlayer "Actually, a larger ringsize decreases the expenses related to churning, Actually, a larger ringsize decreases the expenses related to churning. Users have to make fewer transactions to achieve their desired anonymity set."

The second sentence is true but the first does not follow from it. It depends on the costs of the transactions and this very much depends on the particulars of transaction sizes and bulletproofs affect that greatly.

To make a toy example for _obvious_ illustration of the principle (not intended to be realistic), ignoring range proofs and other per-tx or per-output overhead, consider a desire to reach a potential anonymity set of 100. We can do this by churning once (plus the regular spend tx) using a fixed (chain-wide) ring size of 10 or not churning at all (just regular spend tx) with a ring size of 100. The latter uses fewer transactions, but the former clearly has higher costs attributable to the ring signatures themselves. This becomes more extreme if we compared two churns at fixed ring size 10 (reaching potential anonymity set of 1000) vs. a fixed ring size of 1000.

Once range proofs and other non-ring-signature costs enter into it, the results certainly shift, but my point is that one can't simply equate fewer transactions with lower costs relative to anonymity set. 

Costs relative to compromise of a given proportion of the output set are somewhat different from anonymity set, but as I mentioned earlier are highly sensitive to the _assumed_ compromise share. For example, at 50% (in some sense perhaps the optimal share for making the argument for an increased ring size), going from ring size 5 to 10 reduces the compromise rate from 6.25% to 0.195%. But with an assumed compromise share of 20%, going from ring size 5 to 10 decreases from 0.16% to 0.000051% and with an assumed compromise share of 80%, from 40% to 13%. I suppose there are probably different views on how to interpret these numbers, but it is clear to me that both the numbers and character of the improvements changes _greatly_ depending on the _assumed_ compromise share, with no real basis to choose one assumption over another afaik.

> I disagree with this argument. The idea that we can't mitigate risk just because some risk remains is... counterproductive

That was not really my argument. My argument is more that there is nothing qualitatively different about any of these numbers. They are just trading off modest increased costs for modest increased benefits in a more or less inverse manner. Small increases in ring size will always results in marginally increased costs and marginally increased benefits. How do we decide? 

We already shifted upward from the clearly-research-suported 3 (due to potentially-catastrophic chain reaction effects) to 5 purely for "It seems better and the cost isn't that high" reasons. If we shift form 5 to, say, 8 on the same basis, then why would we not again shift from 8 to, say, 10, for _exactly the same reasons?_ And likewise from there.

I don't see a good qualitative reason to prefer any of these increases, nor to support one increase and then not support the next until the costs pile up and become really burdensome (even more burdensome than they already are, and to say they are is not an extreme view by any means).

Personally I think the costs are too high and threaten both usability and even moderate degrees of on-chain scaling, and we should stop increasing them until and unless there is a clear reason to do so that does not rely on arbitrary assumptions (or until hardware or protocol improvements make the costs not too high). At the given number of 71ms, a single full-size block _at the minimum scaled block-size_ takes nearly 2 seconds to verify (on whatever hardware that was assuming, which may or may not be a minimum reasonable target). That's borderline too-high in my view (for example, it means that verification takes roughly 1/60 of the block interval, so syncing a day of chain would take over 20 minutes. Someone who doesn't run a node continuously but wants to catch up after a week or two will wait hours. These numbers would decrease with multiple cores, but IMO this is still at or beyond the border of too high, and the numbers will increase if (usage increases and) block sizes increase at all.  Of course others may disagree with any or all aspects of this opinion.



## SamsungGalaxyPlayer | 2018-04-16T16:02:39+00:00
@lethos3 does this need to remain open? If you want to recommend an increase from 7 to 10, I feel it's best to open a new issue.

## iamsmooth | 2018-08-23T02:12:45+00:00
This is clearly stale and should be closed. Whatever issues remain can go into a new, better focused, issue.

## moneromooo-monero | 2018-09-14T11:20:24+00:00
Ring size is fixed to 11 from v8. Block time is unchanged.

+resolved

# Action History
- Created by: ghost | 2017-12-30T18:18:02+00:00
- Closed at: 2018-09-14T12:24:58+00:00
