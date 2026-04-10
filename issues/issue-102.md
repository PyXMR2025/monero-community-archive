---
title: Investigate possibility of reducing 10-blocks lock
source_url: https://github.com/monero-project/research-lab/issues/102
author: erciccione
assignees: []
labels: []
created_at: '2022-05-18T08:01:07+00:00'
updated_at: '2024-10-09T16:11:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The 10-blocks lock is the most problematic aspect of Monero, which heavily impacts its usability as a currency and the user experience of people using services based on Monero. #95 explores the possibility of removing the lock, which would be the optimal solution, but the problem is not simple to resolve and the total removal might happen in a far future.

It worth considering if there are the premises for reducing the lock to a smaller amount of blocks, without impacting the security and stability of the network. A couple of questions to get the conversation started:

- Did we ever get close to the 10 blocks limit during a reorg?
- What's the highest number of blocks lower than 10 that could be acceptable for the lock?

Note that even a reduction from 10 to 8 blocks would be a significant UX improvements for Monero users.

# Discussion History
## SChernykh | 2022-05-18T08:16:54+00:00
I've just checked my node's logs as far back as 2021-08-31 (I don't have older logs), and the largest reorg was 3 blocks deep:
```
2022-04-10 17:26:24.193	[P2P9]	INFO	global	src/cryptonote_core/blockchain.cpp:2093	 alternative blockchain size: 3 with cum_difficulty 186060274402189254
```

## erciccione | 2022-05-18T08:48:13+00:00
Thanks @SChernykh, would be very useful to know if that reflects the situation for the entire history of Monero or at least the last years. It's already very good that the largest reorg in the last year was only 3 blocks deep.

## SChernykh | 2022-05-18T12:12:39+00:00
I don't have logs anymore, but I vaguely remember seeing some bigger reorgs before, but they never reached 10 blocks. Unfortunately I don't remember if they reached 8 blocks.

## SamsungGalaxyPlayer | 2022-05-18T13:49:18+00:00
I'm okay with >0 reorgs that are 10+ blocks long. We can't avoid this issue without having an infinite funds lock time, which is impractical.

Thus, we're always picking a reasonable value.

Lowering the block time could have the following downsides:

1. Requires changing the default decoy selection algorithm, and requires sufficient testing for this to ensure it works properly.
2. Some clients could use an old algorithm, resulting in different selection models. MyMonero comes to mind, which has its own implementation. This is possible in any case, it's just exacerbated with the transition. Anyone who uses a custom client will need to do part 1 above also.
3. Setting too low a value could enable privacy downsides during re-orgs.
4. Setting a low value could reduce privacy for quick spends even with a good algorithm. Currently, everyone who wants to spend quickly spends around blocks 10-20, which should be easier to fit an accurate decoy selection model to than 5-20, for example.

Speaking completely without any numbers (:p), I would like to set a goal of cutting the lock time in half to 5.

## UkoeHB | 2022-05-18T18:47:32+00:00
[context](https://libera.monerologs.net/monero-dev/20220518#c97036) from @hyc

> fyi, my linode monerod has ~5 years worth of logs, 1082 reorgs. all but 4 had size 2, those 4 had size 3.

## Rucknium | 2022-05-18T18:53:45+00:00
This issue was discussed at the MRL meeting:

https://github.com/monero-project/meta/issues/706#issuecomment-1130386283

## erciccione | 2022-05-19T06:34:39+00:00
>  fyi, my linode monerod has ~5 years worth of logs, 1082 reorgs. all but 4 had size 2, those 4 had size 3.

This is very encouraging, as we didn't get even close to half the current block limit in 5 years. I would say the first 3 years have relatively less importance, since the network was much smaller and not yet robust.

Are there attack vectors that could end up creating reorgs (beside a 50%+1 attack, which is out of scope)? That seems to be the main issue, given that during normal operation of the network reorgs were never more than 3 blocks deep.

> This issue was discussed at the MRL meeting:

@moneromooo-monero mentions smooth was strongly against lowering the blocks to <10 some time ago. Do we know the reasoning?

## chaserene | 2023-04-28T22:34:35+00:00
@hyc could you share an extract of your Linode logs that includes reorg events, their time and their depth? seeing how the size and the frequency of reorgs changed over time, maybe if there is a general trend or a correlation with hash rate/upgrades/etc, could help making an informed decision about what level of reorg probability we are comfortable with.

## hyc | 2023-04-29T15:24:57+00:00
http://highlandsun.com/hyc/reorgs.txt currently contains 1219 lines, 160KB. All but four reorgs are size 2, four are size 3.

But I'd be dubious about using this as a metric in deciding how to change the lock. If we reduce it significantly below 10, that will incentivize attackers to try to double-spend.

## chaserene | 2023-04-29T21:15:49+00:00
thank you!

from lines 395 to 1076 (both inclusive), there are only a few dates for all entries, which seems to be something other than when the reorg happened (maybe that's  when the log file was exported). do you see a way to assign actual dates to those?

also, among those records (so the date is not indicative), I've found a real outlier, supposedly a 26-block reorg (L751):

> bitmonero.log-2018-09-06-21-22-35: alternative blockchain size: 26 with cum_difficulty 14334003971616801[0m

does anyone remember this occurrence? (I don't.)

> I'd be dubious about using this as a metric in deciding how to change the lock. If we reduce it significantly below 10, that will incentivize attackers to try to double-spend.

I agree in that the maximum 3 block depth in this data, presuming there were malicious attempts among those, doesn't mean that a longer-range attack is uneconomic for current potential attackers. but they are always incentivized to some extent to doublespend, even now. only an infinite lock period can remove this incentive. it's that with a shorter one, they are incentivized *more*. 10 blocks has worked out so far, that's valuable empirical data. reducing it to let's say 4 would be clearly reckless, but I do wonder if it would be safe to go below 10.

it's possible that there is no way to know the answer. other than this data set, the only useful source I can think of right now is making a minor reduction in the lock time, collecting reorg data in that environment for an extended period, and then reassessing.

since in general there is no specialized mining hardware, I would assume the wide availability of hardware ready to enter mining, so this decision definitely needs to be made with caution.

## chaserene | 2023-06-06T03:05:29+00:00
here are some quick-and-dirty visualizations that no one asked for from hyc's data. I know this reflects only a single node's view of the network, but this is the best I've encountered so far.

absent further clarification, I excluded reorgs that didn't have a definitive date to them (lines 395-1076, inclusive), because obviously I can't plot them on a time axis without knowing when they occurred. this set amounts to ~56% of the total registered reorgs (`682 / 1219`). however, I don't think this will skew the data in a significant way, because 1) the rest of the data that has proper dates begins at 2019-10 (for the first chart, I used only full months, which includes 531 reorgs), and 2) based on the log file names in the log, 605 of the "dateless" reorgs occurred before 2019-06-11, so they don't interfere with the visualized period. the other 77 "dateless" reorgs happened sometime between 2019-06-11 and 2020-12-25. this means that at most `77 / (531 + 77) ≈ 13%` of the picked up reorgs are missing from the charts, and they are limited to the period up to 2020-12-25.

all reorgs with a definitive date have a reported depth of 2 blocks.

the first chart shows how many reorgs were picked up per month (2019-11--2023-03), overlaid with the hash rate from [Bitinfocharts](https://bitinfocharts.com/comparison/monero-hashrate.html#alltime).

![reorgs-hyc-2023-04-29-monthly](https://github.com/monero-project/research-lab/assets/64873595/e06fe707-77d7-4b6d-b2dd-3a312ef76144)

the amount of reorgs seems to strongly correlate with the hash rate. Carbon Chameleon's PoW change is responsible for the large hash rate jump there. a reduction in reorgs seems to co-occur with it. this can't be clearly stated because some of the "dateless" reorgs may have happened between Carbon Chameleon and 2020-12-25, though I'm not sure that even all 77 "dateless" reorgs could erase that significant reduction.

the correlation seems to weaken after Fluorine Fermi and the amount of reorgs falls significantly.

I wonder if these major reductions are due to networking updates in the forks or something else.

the second chart is a shot at visualizing all reorgs with a definitive date (2019-10-29--2023-04-20, inclusive), each reorg being a dot and the Y axis showing how many hours elapsed since the last reorg, sort of a "time between ~~failures~~ reorgs".

![reorgs-hyc-2023-04-29-hslr](https://github.com/monero-project/research-lab/assets/64873595/c72e2a15-7c5b-4b76-9bba-68042a962d2f)

this chart may not be as useful, but it seems that the time between reorgs kept improving after Fluorine Fermi against a relatively stable hash rate.

these are all subjective observations, I'm sure that with proper statistical methods one can glean better insights.

## Gingeropolous | 2023-06-07T03:43:20+00:00
the noncesense  lab has stuff on re-orgs.

https://github.com/noncesense-research-lab/archival_network

I don't know where the actual data or results are though.

## chaserene | 2023-06-07T20:24:27+00:00
thanks @Gingeropolous. I guess the relevant data is buried in /raw_log_dumps. it would be interesting to see if it matches up with hyc's data, but for now there are serious doubts that a reduction could be done safely, no matter how good the recent results are (see the [chat log of today's MRL meeting](https://github.com/monero-project/meta/issues/846#issuecomment-1581507718)).

**edit (2024-03-29)**: I noticed the above logs have @hyc saying it's dangerous to go below 10 blocks, but his precise reasoning happened outside the meeting hours. I'll offer a summary from memory, which you may be able to find in the full MRL chat logs, unfortunately I couldn't (but it happened around those days):

he basically said the risk of a reorg will increase unpredictably by reducing the lock period. years of experience show that 10 is safe, but reducing even just to 9 may cause catastrophic failures. it's like you're standing blindfolded near a precipice, and you know that the edge is at most 10 steps away, but you can't see where exactly. any step forward may cause your downfall.

## ghost | 2023-12-22T19:22:40+00:00
has [https://github.com/monero-project/research-lab/issues/95#issuecomment-1197336438](url) been looked into? 

## chaserene | 2024-01-01T03:07:50+00:00
@r4v3r23

(correct link: https://github.com/monero-project/research-lab/issues/95#issuecomment-1197336438)

I'm far from having processed the whole problem space, but I think it's a smart proposal, at the cost of protocol complexity that's not negligible nor crushing. I encourage reading it and comments after it through 2022-12-29, they help understanding its strengths and weaknesses. the proposal is in the 10-blocks lock *elimination* thread, but in practice it can only *reduce* it, hence relevant here ("in practice you would only select decoys from blocks [older than some threshold](https://github.com/monero-project/research-lab/issues/95#issuecomment-1366538677) larger than the average time it takes to propagate a double-spend report").

I like that it can (almost always) work without affecting transaction uniformity. it still troubles me that it requires assumptions about network behavior that we can't estimate the probability of, nor do we have enough historical data/experience about. but my takeaway is that it may be impossible to reduce the length of the lock without such assumptions.

going that route *can* lead to breaking aspects of the network. to move forward, I think we'd need a way to quantify the probability of transaction invalidation through a reorg with the current protocol, and see if an alternative model can reliably bring the same level with certain parameters (if any).

off-topic: the conservative in me wants to see the network as robust as possible and solve fast spendability rather on a layer-2. on the other hand, payment channels on Monero are currently only theoretical (I know about five papers and that's it) and rollups haven't even been seriously theorized. it would also prove useful to not fragment the network into layers.

## chaserene | 2024-01-06T08:39:46+00:00
potentially useful regarding quantification (h/t to Rucknium for finding it):
[Isthmus: Framework for assessing safe lock times based on worst case plausible scenario (draft, October 2019)](https://raw.githubusercontent.com/noncesense-research-lab/lock_time_framework/master/writeup/lock_time_framework.pdf)


## shortwavesurfer2009 | 2024-05-16T00:02:52+00:00
Probably a very dumb question, but as a regular user I'm going to ask it anyway. Why not move stage net or test net to say eight or nine blocks and run it and see what happens? After all, isn't that what they are their for, to test experiments with? Either that or maybe Wownero may be willing to try it out

## chaserene | 2024-05-16T19:49:21+00:00
@shortwavesurfer2009 not a dumb question. in my view, that wouldn't help a lot for the following reasons:

* I haven't experimented with stagenet or testnet, but I would bet that the network load is different. block size is a factor in reorg frequency and depth.
* the actual network topology is different. not everyone who's running a mainnet node runs a stagenet/testnet node. Wownero probably also differs a lot.
* incentives are important, think of e.g. a selfish mining scenario. stagenet/testnet coins have no economic value, and WOW is a different asset, so the incentives are different.

## tevador | 2024-05-24T09:54:24+00:00
> has https://github.com/monero-project/research-lab/issues/95#issuecomment-1197336438 been looked into?

FYI, this proposal should be considered obsolete because it can't work with full-chain membership proofs (FCMPs).

With FCMPs, the decoy set will be defined by a reference block and will contain all outputs created up to (and including) that block.

Zcash works nearly the same way (they call their reference block an "anchor"). Interestingly, they don't have a consensus-mandated lock time and simply expect users to resubmit any transactions invalidated by reorgs. Some zcash wallets have a voluntary lock. Here is the relevant discussion: https://github.com/zcash/zcash/issues/1614

## Rucknium | 2024-10-09T16:11:08+00:00
# Success probability of a double-spend attack with minority hashpower share

**TL;DR: The probability of a successful double-spend attack using a minority of hashpower is computed. The attack success probability is very nonlinear with respect to the attacker's hashpower share. When a potential victim waits 10 blocks and the attacker has 10 percent of hashpower, the attack success probability is negligible. When a potential victim waits 10 blocks and the attacker has 30 to 40 percent of hashpower, the attack success probability is pretty high.**

Below I analyze two attack strategies. The first is the classic attack analyzed by Satoshi Nakamoto in the bitcoin white paper. The classic attack has  a single cycle: mine an attacking chain until it outpaces the honest chain or until the end of time. The second attack strategy mines an attacking chain until the "full confirmation" block depth is reached on the honest chain. If the attacking chain is longer at that point in time, the attacker broadcasts the chain and the attack is a success. If not, the attacker tries to restart the attack cycle.

When a potential victim waits 10 blocks and the attacker has 10 percent of hashpower, the classic Nakamoto attack has a 0.0008 percent probability of success. With 30 and 40 percent of hashpower, the attacker has a 6.5 and 37.2 percent, respectively, probability of success in the same scenario. If the attacker uses the second strategy, an attacker possessing 10 percent of hashpower for 12 years will be able to execute a successful attack with 50 percent probability if the potential victims waits for 10 blocks for full confirmation. An attacker possessing 30 and 40 percent of hashpower will need to possess the hashpower for 8.6 and 1.5 hours, respectively, to achieve a 50 percent attack success probability.

In my opinion, an attacker that could pay a roughly linear cost to acquire a linear amount of hashpower would find it advantageous to go big or go home. There is no reason to pay for only 10 percent of hashpower to get negligible success probability when the attacker could be guaranteed success if they pay for 51+ percent of hashpower. It could be reasonable to assume that such an adversary would not attempt a minority hashpower attack and therefore only the probability of benign blockchain re-orgs should be considered when analyzing the best _N_ for the _N_ block lock.

However, the "linear cost" attacker isn't the only potential threat actor. A hacker or malicious insider could acquire control over the block templates of a mining pool. This threat actor would not have linear cost to acquire malicious hashpower. Instead, their malicious hashpower share would be fixed at the aggregate hashpower of miners who hash on block template from the mining pool operator. As of this writing, the top mining pool routinely possesses 30 to 40 percent of Monero's hashpower. See https://miningpoolstats.stream/monero for current hashpower share of the major mining pools.

# Strategy 1: Double-spend attack success probability of the classic Nakamoto attack

The bitcoin white paper describes attempted double-spend attacks when the attacker has a minority hashpower share and the potential victim waits $z$ blocks to consider the transaction "fully confirmed" (Nakamoto 2008). The attacker mines the attacking chain for an indefinite amount of time. It is assumed that the attacker has a one-block advantage at the start of the attack. Rosenfeld (2014) analyzed the attack in detail and provides a corrected formula for the attack success probability. (Nakamoto simplified the scenario by assuming the honest miners always mine new blocks at a constant rate instead of the true random rate.) Grunspan & Perez-Marco (2018) developed an equvalent formula with the regularized incomplete beta function, which I will use here.

Theorem 1 of Grunspan & Perez-Marco (2018) states:

--------

Let $0<q<1/2$, respectively $p=1-q$, be the relative hash power of the group of the attackers, respectively of honest miners. After $z$ blocks have been validated by the honest miners, the probability of success of the attackers is

$$P(z)=I_{4pq}(z,1/2)$$

where $I_{x}(a,b)$ is the regularized incomplete beta function

--------

Below is a table of attack success probabilities based on Theorem 1.

Columns are the hashpower share of the adversary.

Rows are the number of mined blocks that the victim waits before considering a transaction "confirmed".

Cells are the attack success probability, in percent.


|   |     0.05|      0.1|      0.2|      0.3|      0.4|     0.45|
|:--|--------:|--------:|--------:|--------:|--------:|--------:|
|1  | 10.00000| 20.00000| 40.00000| 60.00000| 80.00000| 90.00000|
|2  |  1.45000|  5.60000| 20.80000| 43.20000| 70.40000| 85.05000|
|3  |  0.23162|  1.71200| 11.58400| 32.61600| 63.48800| 81.37463|
|4  |  0.03872|  0.54560|  6.66880| 25.20720| 57.95840| 78.34244|
|5  |  0.00664|  0.17818|  3.91629| 19.76173| 53.31354| 75.71581|
|6  |  0.00116|  0.05914|  2.33084| 15.64496| 49.30037| 73.37548|
|7  |  0.00021|  0.01986|  1.40071| 12.47504| 45.76879| 71.25164|
|8  |  0.00004|  0.00672|  0.84795| 10.00251| 42.62064| 69.29921|
|9  |  0.00001|  0.00229|  0.51629|  8.05539| 39.78730| 67.48712|
|10 |  0.00000|  0.00079|  0.31582|  6.51067| 37.21840| 65.79282|
|11 |  0.00000|  0.00027|  0.19394|  5.27799| 34.87557| 64.19932|
|12 |  0.00000|  0.00009|  0.11948|  4.28960| 32.72869| 62.69347|
|13 |  0.00000|  0.00003|  0.07381|  3.49395| 30.75355| 61.26479|
|14 |  0.00000|  0.00001|  0.04571|  2.85131| 28.93035| 59.90480|
|15 |  0.00000|  0.00000|  0.02836|  2.33077| 27.24259| 58.60650|
|16 |  0.00000|  0.00000|  0.01763|  1.90809| 25.67635| 57.36402|
|17 |  0.00000|  0.00000|  0.01098|  1.56413| 24.21974| 56.17240|
|18 |  0.00000|  0.00000|  0.00685|  1.28371| 22.86252| 55.02740|
|19 |  0.00000|  0.00000|  0.00427|  1.05470| 21.59579| 53.92534|
|20 |  0.00000|  0.00000|  0.00267|  0.86739| 20.41173| 52.86301|
|21 |  0.00000|  0.00000|  0.00167|  0.71398| 19.30344| 51.83759|
|22 |  0.00000|  0.00000|  0.00105|  0.58819| 18.26482| 50.84660|
|23 |  0.00000|  0.00000|  0.00066|  0.48492| 17.29041| 49.88782|
|24 |  0.00000|  0.00000|  0.00041|  0.40007| 16.37531| 48.95926|
|25 |  0.00000|  0.00000|  0.00026|  0.33027| 15.51511| 48.05913|
|26 |  0.00000|  0.00000|  0.00016|  0.27282| 14.70584| 47.18583|
|27 |  0.00000|  0.00000|  0.00010|  0.22548| 13.94388| 46.33789|
|28 |  0.00000|  0.00000|  0.00006|  0.18646| 13.22594| 45.51397|
|29 |  0.00000|  0.00000|  0.00004|  0.15427| 12.54903| 44.71286|
|30 |  0.00000|  0.00000|  0.00003|  0.12769| 11.91040| 43.93344|

R code to reproduce the table:

```R

# install.packages("zipfR")
# install.packages("knitr")

# Rows: 1 to 30 number of blocks to wait
# Column: hashpower share: 5%, 10%, 20%, 30%, 40%, 45%

# Based on Theorem 1 of Grunspan & Perez-Marco (2018). "Double spend races."

n.blocks <- 30
hashpower.share <- c(0.05, 0.10, 0.20, 0.30, 0.40, 0.45)

blocks <- 1:n.blocks
results <- matrix(0, nrow = n.blocks, ncol = length(hashpower.share))

for (i in seq_along(hashpower.share)) {
  q = hashpower.share[i]
  p = 1 - q
  results[, i] <- zipfR::Rbeta(x = 4*p*q, a = blocks, b = 1/2)
}

results <- 100 * results # Convert to percentage
rownames(results) <- as.character(blocks)

comparison.block <- 10
results.comparison <- results

for (j in seq_len(ncol(results.comparison))) {
  divisor <- results[blocks == comparison.block, j]
  results.comparison[, j] <- results.comparison[, j] / divisor
}


knitr::kable(results, format = "pipe", row.names = TRUE,
  col.names = hashpower.share, digits = 5)

```




# Strategy 2: Required possession duration of malicious hashpower for successful double-spend attack with a $z$ stopping rule.

An attacker possesses $q$ share of Monero's hashpower for a duration of $d$ blocks. Honest miners possess $p=1-q$ hashpower share.

Let $z$ be the number of blocks that the potential victim waits for "full confirmation" of a transaction. When a transaction is mined in a block on the honest chain, that means that the transaction has one confirmation, i.e. $z=1$. When another block is mined on the honest chain, $z=2$.

The attacker attempts as many double-spend attacks as possible during the specified duration. Let us label this series of attacks as the "meta attack". The objective of the meta attack is for one of the double-spend attacks to succeed. Once the attacker has mined its initial block, it mines on its attacking sub-chain until the honest sub-chain has added $z$ more blocks. Then the attacker stops mining and broadcasts the attacking sub-chain if the attack is successful or starts mining a new attacking chain if unsuccessful. This attack with the $z$ stopping rule is not the same as the classic double-spend attack described in the bitcoin white paper, which assumed the attacker would continue mining the initial attacking sub-chain for an indefinite length of time.

The simple $z$ stopping rule does not necessarily maximize the probability of one of the attacks being successful. To evaluate the best strategy, the future probability of being successful while continuing to mine on the initial attacking sub-chain would have to be compared with the probability of re-starting the chain at every state change, i.e. each time the attacker or honest miners added a new block to their sub-chains. This kind of analysis would likely require more complicated techniques like Stochastic Dynamic Programming. Hinz (2020) and Jang & Lee (2020) could help with an analysis like that, but at least one additional assumption about about the value at stake is required. Below, the simple $z$ stopping rule is analyzed.

## Meta attack algorithm

(1) Attempt to secretly mine a block containing a self-send transaction.

(2a) If the attacker successfully mines a block before a new block is mined by honest miners, send a transaction that is incompatible with the self-send transaction to the potential victim and go to step (3). This transaction will go into the transaction pool of honest miners, waiting to be mined into the next block.

(2b) If the honest miners mine a block before the attacker, then go to step (1).

(3) Attempt to mine $z$ additional blocks in the attacking sub-chain before the honest miners mine $z$ blocks. (The total length of the attacking sub-chain will be $z+1$ blocks because the first block was mined in step (2a).

(4a) If the attempt in step (3) is successful, broadcast the attacking chain when the length of the honest sub-chain reaches $z$ and the victim considers the transaction to be fully confirmed. The attack is a success.

(4b) If the attempt in step (3) is unsuccessful, request a refund from the potential victim (e.g. request to withdraw the deposited coins from a cryptocurrency exchange) and go back to step (1).

## Attack duration analysis

Let $w$ be the number of times that the attacker can run the (1)-(4) algorithm while possessing the $q$ share of hashpower for a duration of $d$ blocks. $w$ is determined by $z$ and the waiting time until the attacker produces a new first block in the attacking chain in step (2a). The waiting time is the number of times that the attacker has to re-start the algorithm when it fails at step (2b) because the honest miners have mined a block before the attacker.

Let $v$ be the random number of blocks that the honest miners produce while the attacker is trying to mine its first attacking block. $v$ has a negative binomial distribution where the number of successes is 1 and the probability of success is $q$ (Proposition 5.1 of Grunspan \& Perez-Marco 2018). We will make the simplifying assumption that the attacker always has to wait for the mean of $v$ to produce its first attacking block. The mean of $v$ is $(1-q)/q$. $w$ is the number of attempts that the attacker can make while possessing $q$ hashpower share for a $d$ duration of blocks. The attacker can only attack if he or she possesses the hashpower share for at least a full "cycle", so we use the floor function, $\lfloor x\rfloor$. $w$ is $d$ divided by the sum of the full confirmation waiting time $z$ and the expected waiting time until the attacker produces the first attacking block, $(1-q)/q$:

$$w=\lfloor d/(z+(1-q)/q)\rfloor$$

Again, use Proposition 5.1 of Grunspan \& Perez-Marco (2018), but this time we will compute the probability that the attacking sub-chain is longer than the honest sub-chain when the length of the honest sub-chain reaches $z$. Let $x$ be the random number of blocks added to the attacking sub-chain in step (3). Therefore, the total length of the attacking sub-chain is $x+1$ because one block was mined in step (2a). Let $Pr(x\geq z)$ be the probability that step (4a) is achieved by the attacker, i.e. the length of the attacking sub-chain is longer than the length of the honest sub-chain when the honest sub-chain reaches $z$ blocks in length. We will start with the cumulative distribution function (CDF) of $x$, which is distributed as a negative binomial distribution:

$$Pr(x\leq k)=I_{p}(z,k+1)$$

where $I_{y}(a,b)$ is the regularized incomplete beta function.

Let $k+1=z$, so $k=z-1$. Therefore,

$$Pr(x\leq z-1)=I_{p}(z,z)$$

Get the complement of the probability (i.e. get the upper tail of the CDF):

$$Pr(x>z-1)=1-I_{p}(z,z)$$

$x$ and $z$ are discrete. Therefore, $x>z-1\Longleftrightarrow x\geq z$. So:

$$Pr(x\geq z)=1-I_{p}(z,z)$$

Which was the desired probability expression. We can simplify further by using an identity of the regularized incomplete beta function: $I_{1-y}(a,b)=1-I_{y}(b,a)$ and the fact that $q=1-p$:

$$Pr(x\geq z)=I_{q}(z,z)$$

It is interesting that the $Pr(x\geq z)$ success probability of a double spend with this $z$ block stopping rule is exactly half as large as the success probability of a single attack where the attacker continues adding blocks to the initial attacking sub-chain for an infinite amount of time, which is $2I_{q}(z,z)$. The indefinite-time attack is the classic form of the double spend attack described in the bitcoin white paper. The attacker's cost of an indefinite-time attack is potentially infinitely larger than the cost of the attack with the $z$ block stopping rule. (The proof of Theorem 6.1 in Grunspan \& Perez-Marco (2018) shows that $2I_{q}(z,z)$ is the attack success probability for the indefinite-time attack.)

We want to know the probability that at least one of the double-spend attacks attempted during the meta attack is successful. We have $w$ attempts. Since the attack success probability are statistically independent and identical on each attempt, we can use $w$ as an exponent. The probability of attack failure is $1-I_{q}(z,z)$. Compute the probability that all of the attacks fail: $\left(1-I_{q}(z,z)\right)^{w}$. The probability that at least one double-spend attack succeeds during the meta attack is:

$$Pr_{meta}=1-\left(1-I_{q}(z,z)\right)^{w}$$

We want to find the minimum duration $d$ of the meta attack that would allow an attacker to achieve a specified probability of being successful in their meta attack, for several values of the attacker's hashpower share $q$ and the number of blocks for a transaction to be considered "fully confirmed", $z$. We must solve for $d$. Recall that the expression for $w$ contains the floor function. We will ignore that for the moment and use $`w^{*}=d^{*}/(z+(1-q)/q)`$. Now we need to find the minimum $d$ such that $`Pr_{meta}\geq1-\left(1-I_{q}(z,z)\right)^{d^{*}/(z+(1-q)/q)}`$. Solving for $`d^{*}`$:

$$(z+(1-q)/q)\cdot\log\left(1-Pr_{meta}\right)/\log\left(1-I_{q}(z,z)\right)\leq d^{*}$$

To find the minimum $d$ that satisfies this inequality, we need to "round up" $`d^{*}`$ to the next multiple of $z+(1-q)/q$, then round up again to the next integer (recall the definition of $w$). We use the ceiling function, $\lceil x\rceil$. The $d$ that satisfies the requirement is $`d=\lceil\lceil d^{*}/(z+(1-q)/q)\rceil\cdot(z+(1-q)/q)\rceil`$. Simplifying terms, we get:

$$d=\left\lceil \left\lceil \dfrac{\log\left(1-Pr_{meta}\right)}{\log\left(1-I_{q}(z,z)\right)}\right\rceil \cdot(z+(1-q)/q)\right\rceil $$

## Table: Duration of meta attack to achieve attack success probability of 50 percent

Below is a table of the duration of a meta attack that would allow an attacker to achieve a 50 percent probability of being successful in their meta attack. The rows are different values for $z$, the number of blocks a potential victim would wait until considering a transaction "fully confirmed". The columns are different values for $q$, the share of hashpower the attacker possesses. The cells are the number of days that the attacker would have to possess the hashpower to achieve at least 50 percent probability (i.e. $Pr_{meta}=0.5$) of at least one successful double spend attack. For example, if a potential victim considered a transaction fully confirmed after 5 blocks, an attacker possessing 10 percent of hashpower for 15 days would have 50 percent probability of at least one successful execution of a double spend attack.


|   |      0.05|       0.1|       0.2|    0.3|   0.4|  0.45|
|:--|---------:|---------:|---------:|------:|-----:|-----:|
|1  |     0.389|     0.097|     0.028|  0.010| 0.007| 0.007|
|2  |     2.800|     0.382|     0.058|  0.019| 0.010| 0.010|
|3  |    18.303|     1.350|     0.117|  0.031| 0.013| 0.013|
|4  |   114.393|     4.586|     0.233|  0.053| 0.024| 0.015|
|5  |   695.467|    15.128|     0.450|  0.072| 0.028| 0.018|
|6  |  4148.646|    48.833|     0.833|  0.104| 0.032| 0.021|
|7  | 24406.850|   155.156|     1.512|  0.143| 0.036| 0.024|
|8  | > 100 yrs|   486.719|     2.733|  0.201| 0.040| 0.026|
|9  | > 100 yrs|  1511.525|     4.857|  0.268| 0.058| 0.029|
|10 | > 100 yrs|  4654.446|     8.536|  0.360| 0.064| 0.032|
|11 | > 100 yrs| 14229.972|    14.896|  0.482| 0.069| 0.035|
|12 | > 100 yrs| > 100 yrs|    25.778|  0.637| 0.075| 0.038|
|13 | > 100 yrs| > 100 yrs|    44.342|  0.853| 0.101| 0.040|
|14 | > 100 yrs| > 100 yrs|    75.825|  1.112| 0.108| 0.043|
|15 | > 100 yrs| > 100 yrs|   128.989|  1.444| 0.115| 0.046|
|16 | > 100 yrs| > 100 yrs|   218.417|  1.860| 0.146| 0.072|
|17 | > 100 yrs| > 100 yrs|   368.317|  2.390| 0.154| 0.076|
|18 | > 100 yrs| > 100 yrs|   618.781|  3.050| 0.162| 0.081|
|19 | > 100 yrs| > 100 yrs|  1036.086|  3.911| 0.200| 0.085|
|20 | > 100 yrs| > 100 yrs|  1729.467|  4.964| 0.210| 0.089|
|21 | > 100 yrs| > 100 yrs|  2878.854|  6.287| 0.219| 0.093|
|22 | > 100 yrs| > 100 yrs|  4779.739|  7.976| 0.261| 0.097|
|23 | > 100 yrs| > 100 yrs|  7916.962| 10.064| 0.272| 0.101|
|24 | > 100 yrs| > 100 yrs| 13084.633| 12.692| 0.319| 0.106|
|25 | > 100 yrs| > 100 yrs| 21581.438| 15.944| 0.332| 0.110|
|26 | > 100 yrs| > 100 yrs| 35528.583| 19.992| 0.382| 0.114|
|27 | > 100 yrs| > 100 yrs| > 100 yrs| 25.056| 0.396| 0.118|
|28 | > 100 yrs| > 100 yrs| > 100 yrs| 31.344| 0.451| 0.122|
|29 | > 100 yrs| > 100 yrs| > 100 yrs| 39.124| 0.467| 0.126|
|30 | > 100 yrs| > 100 yrs| > 100 yrs| 48.769| 0.525| 0.131|

R code to reproduce the table above is:

```R
# install.packages("zipfR")
# install.packages("knitr")

Pr_meta <- 0.5
n.blocks <- 30
hashpower.share <- c(0.05, 0.10, 0.20, 0.30, 0.40, 0.45)

z <- 1:n.blocks
results <- matrix(0, nrow = n.blocks, ncol = length(hashpower.share))

for (i in seq_along(hashpower.share)) {
  q <- hashpower.share[i]
  Iq <- zipfR::Rbeta(x = q, a = z, b = z)
  results[, i] <-  ceiling(ceiling(log(1 - Pr_meta)/(log(1-Iq))) * (z + (1-q)/q))
}

results <- results / (30*24)  # Convert to days
rownames(results) <- as.character(blocks)

results[ (! is.finite(results)) | results >= 365.25 * 100] <- NA

options(knitr.kable.NA = paste0("> 100 yrs"))

knitr::kable(results, format = "pipe", row.names = TRUE,
  col.names = hashpower.share, digits = 3)
```

# References

Grunspan, C., & Perez-Marco, R. (2018). "Double spend races." Int. J. Theor. Appl. Finance, 21(8).

Hinz, J. (2020). "Resilience Analysis for Double Spending via Sequential Decision Optimization." Applied System Innovation, 3(1), 7.

Jang, J. & Lee, H.-N. (2020) "Profitable Double-Spending Attacks." Appl. Sci., 10, 8477.

Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System".

Rosenfeld, M. (2014). "Analysis of Hashrate-Based Double Spending".



# Action History
- Created by: erciccione | 2022-05-18T08:01:07+00:00
