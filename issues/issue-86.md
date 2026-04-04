---
title: Decoy Selection Algorithm - Areas to Improve
source_url: https://github.com/monero-project/research-lab/issues/86
author: j-berman
assignees: []
labels: []
created_at: '2021-08-25T18:57:37+00:00'
updated_at: '2022-02-02T05:07:33+00:00'
type: issue
status: closed
closed_at: '2022-01-30T04:41:45+00:00'
---

# Original Description
# Abstract

When someone sends you Monero, you receive an output. When you spend your Monero, you spend that output. When constructing a transaction, your wallet hides the output you are spending among a set of decoy outputs to obfuscate which among them is your real output being spent. If you receive an output on May 4th, then go to spend it on May 5th, the decoy selection algorithm will pull in 10 decoy outputs from across the chain's history to include in your transaction on May 5th, so that no one can tell which among the 11 total outputs is yours.

To be clear, the block in which each output is created constitutes metadata that is transparent on-chain, along with metadata that shows which outputs are included in which transactions. It is not transparent which outputs are real outputs being spent in each transaction, since the real outputs spent in transactions are obfuscated among decoy outputs.

All outputs on the blockchain do not have an equal probability of being selected by the decoy selection algorithm, because that would allow someone analyzing the chain to make strong guesses about which outputs are really being spent in a transaction (for example, by using a "newest spend" heuristic). Instead, the algorithm uses known spending patterns to select decoys, hiding outputs among the crowd.

# Overview of this improvement proposal

There appears to be significant room for improvement in the decoy selection algorithm, and I'd like to summarize what I've found over the last month to show what is worth focusing attention on today. I'm planning on submitting a CCS proposal to work on these areas (among other tasks) full-time. This issue will be divided into 2 parts:

1. Evidence highlighting room for improvement in the decoy selection algorithm.
2. Areas to focus attention on today in order to improve upon the discovered evidence.

On the latter, I'm sure most reading this are already familiar with the "binning" strategy (discussed in #84 and in [Möser et al. (2018) section 6.2](https://sciendo.com/article/10.1515/popets-2018-0025)). I'll be presenting a case here for why binning should be more seriously considered for implementation in the next hard fork, even before a significant ring size bump that will come when one of Triptych/Seraphis/Lelantus is ready. For those who don't know what binning is, I will explain it in more detail later on.

# Evidence highlighting areas the decoy selection algorithm could improve

Currently, the decoy selection algorithm selects 10 decoys using a distribution fit to the spending pattern based on linkable Monero transactions back in 2016/17 (as recommended in Möser et al. (2018)). This approach has known weaknesses:

- Assume you use Monero throughout the day one day, and have some change outputs collected from the day. Weeks later, you decide to send some Monero somewhere else. If your wallet uses multiple outputs from that same day in distinct rings in your transaction, those outputs stick out in the rings, and make it easier to guess real spents with accuracy. [TO-DO: quantify the chances of 2 distinct rings in a transaction having outputs within 100 blocks of each other, plotting age on the x-axis]. As partial mitigation to this, some wallets may warn the user that [spending multiple outputs older than 30 days in a single transaction may be harmful for privacy](https://github.com/monero-project/monero/blob/2d3ce2d64a29caa9d2f526e01f9311a2eb676d6d/src/simplewallet/simplewallet.cpp#L6470-L6480), or that [spending outputs that are within 5 blocks of each other can break ring signatures](https://github.com/monero-project/monero/blob/2d3ce2d64a29caa9d2f526e01f9311a2eb676d6d/src/simplewallet/simplewallet.cpp#L6438-L6447). However, there is not always much recourse available to the average user to avoid doing these things.

- Assume you have 1 transaction tied to a known user. You can do temporal analysis on the outputs used in the rings of the transaction, and arrive at more likely outputs used as inputs to the transaction. For example, maybe you know around what time the user would spend an output, and therefore can deduce that only the outputs in that time window are likely the user's.

- If the gamma distribution is off for whatever reason (for example, general spending patterns change materially as adoption picks up and usage changes), and the gamma fails to select decoys proportional to the real spends, then it becomes easier to guess real spends. Below is evidence showing where the gamma distribution seems to be off.

### Inconsistencies with the observed shape of the distribution to the expected

CAUTION: drawing conclusions about real outputs from the following analysis is ill-advised, since the analysis is too raw to be useful for that purpose. It isn't clear if the analysis can even be used for that purpose, though, it does highlight potential issues worth assessing to improve the algorithm. Added this note after @vtnerd and @SamsungGalaxyPlayer's comments in the discussion below.

#### **Outputs between 10 and 100 blocks old**

![output_age  avg_output_time shift - fix earliest spent](https://user-images.githubusercontent.com/26468430/130850097-22694dbe-de3f-4014-9e01-655ad92009d2.png)

The current decoy selection algorithm (orange) appears to be *under-selecting* outputs relative to the observed output ages in rings (blue), as is apparent by the large triangular gap above the orange line to the blue. Basically, there are many more outputs observed on-chain than the current decoy selection algorithm would produce over that age range, which is visualized as the triangular gap.

Here are 3 potential causes for this triangular gap:

1. Different algorithms are in use out in the wild.
2. An actor with many outputs is modifying their client to select more recent outputs.
3. Recent real outputs aren't as well covered by the decoy selection algorithm as they can be.

EDIT: removed my opinionated analysis toward a cause while raw research is ongoing, since it's not as clear yet which is the cause, and doesn't serve much use for purposes of seeking to improve the algorithm at this point.

It should also be noted that there are known implementations in use that do not use the "Current decoy selection algorithm" (and to be clear, the "Current decoy selection algorithm" is wallet2's implementation before the latest round of patches for [the earliest spend issue/incorrect curve fit](https://github.com/monero-project/monero/pull/7821)).

Here are the distributions of outputs between 10 and 100 blocks old over various hard fork intervals for consideration:

![output_age  v14 - fix earliest spent](https://user-images.githubusercontent.com/26468430/130846265-d9fa5363-4b5b-4440-b1e9-fb656c614f4a.png)

![output_age  v12 - fix earliest spent](https://user-images.githubusercontent.com/26468430/130846271-5adfc3a9-7780-45cb-a967-99f4290914ba.png)

#### **Outputs around 100,000 to 250,000 blocks old**

Notice how many more outputs are observed on chain in the following regions than the decoy selection algorithm would produce:

##### **Outputs between 170,000 - 230,000 blocks old**

![output_age  avg_output_time shift - 170k - 230k](https://user-images.githubusercontent.com/26468430/130846363-a3f2fa6b-3036-4f12-b5fd-bf62190bb695.png)

##### **Outputs between 80,000 - 240,000 blocks old**

![output_age  v14 - 80k - 240k](https://user-images.githubusercontent.com/26468430/130846400-05bb14da-b181-474c-89b1-25c0a59f26b3.png)

#### **Easier visual across the chain**

Below are additional charts that quantify the above gaps noticed on chain as a ratio of Current / Observed:

![Current : Observed  v14](https://user-images.githubusercontent.com/26468430/130846439-86dc84c0-b868-4d8b-aeee-3e00866017f8.png)

![Current : Observed  avg_output_shift](https://user-images.githubusercontent.com/26468430/130846455-3b3db5d9-a5cc-4842-beae-9f84e09b8f1f.png)

EDIT: note that the following is ONLY true assuming the decoy selection algorithm is the only algorithm in use, which we know is not the case. However it is still useful to understand what the charts are saying.

If the blue line is below 1 AND that algorithm were the only one in use, that means the decoy selection algorithm would be *under-selecting* outputs. If it is above 1 AND that algorithm were the only one in use, that means the decoy selection algorithm may be *over-selecting* outputs. If it is equal to 1, the decoy selection algorithm is perfectly hiding outputs.

However, considering the algorithm is not the only one in use, it seems going much further with this analysis without taking all other algorithms in use into account wouldn't be very useful.

# The areas to focus attention on today

Here are 4 areas to focus attention on in order to improve upon the above aspects of the decoy selection algorithm:

1. Safely fix integer truncation in the wallet ([#7798](https://github.com/monero-project/monero/pull/7798)).
2. Get "binning" to a production-ready implementation.
3. Improve the distribution criteria used to select decoys (possibly move beyond the gamma).
4. Implement validation at the consensus level that ensures constructed rings use the expected distribution.

## 1. Safely fix integer truncation in the wallet ([#7798](https://github.com/monero-project/monero/pull/7798))

As highlighted in in [#7798](https://github.com/monero-project/monero/pull/7798), there is a line in wallets that causes a step in the decoy selection algorithm to truncate an integer after division (Integer truncation example: 260 / 100 should equal 2.6, but truncated is 2). Today, this causes the `average_output_time`, which is just the average seconds spaced between each output over the prior year, to truncate to 1 from its true value which is around 1.9 today. This ends up causing the selected decoy to be about ~1.9x older than it would otherwise be if integer truncation were patched. Unfortunately it is not completely clear whether it is safe to make this change today for 2 reasons:

1. It may cause an under-selection of older outputs.
2. It may cause a significant change in transaction uniformity, leaving non-updated clients more vulnerable than they would otherwise be.

Both points 1 and 2 need further analysis to arrive at a stronger conclusion.

## 2. Get "binning" to a production-ready implementation

Binning mitigates weaknesses from selecting decoys using spend-time patterns as the sole criteria. The basic idea behind binning is that outputs are bucketed into bins of a fixed size of similar height. With binning, when you spend an output, you reference a bin that the output is a member of, and include outputs from that bin as the decoys in your transaction. For example, your real output is in block 100, so you'll construct a bin using your real output and another output in block 100. With binning, an observer would have a much tougher go at using temporal analysis to deduce which output is yours, since your output is among a bin of similar aged decoy outputs.

Binning can be combined with the gamma selection like this: with ring size 14, you could have 7 bins of size 2 (numbers strictly meant for illustration). 6 of the bins your transaction references would be composed of 2 decoys, and the 7th would include your real and 1 decoy. The 6 bins would be selected via the gamma distribution.

**Weaknesses that binning protects**

Binning provides protection for users in the circumstance where they spend multiple older outputs in a single transaction, especially when those outputs are close in age. Going off the first example given in the weaknesses section above, assume you use Monero throughout the day one day, and have some change outputs collected from the day. Weeks later, you decide to send some Monero to someone. If your wallet uses multiple change outputs from that same day in distinct rings in your transaction, those outputs would be packed into bins among outputs of similar age. While it may be clearer which bins contain the real output, it would not necessarily be clear which outputs in the bins are the real outputs.

Importantly, binning *also* provides protection in the event the gamma is off. Assume the gamma does not correctly pick up that people are frequently spending outputs that are 100,000 blocks old. Without bins, the decoy selection algorithm would infrequently select decoy outputs that old, and therefore outputs observed on chain that are 100,000 blocks old would be clearly identifiable as very likely real. Now, if binning were in place as a fallback, then perhaps an observer can more easily recognize which *bin* is more likely the real bin as mentioned above, but still cannot deduce with certainty which output from the bin is the real output. It provides an additional fallback, and considering the known issues highlighted above with the gamma distribution today, I believe it is an important fallback to implement today.

**Current status of binning**

@UkoeHB has proposed a way to implement binning (#84) that still requires much deeper research and exploration to ensure it is both feasible and safe. As an alternative, we could implement a naive client-side binning approach, that would be very simple to implement, but would not have the space-saving benefits that @UkoeHB's proposal brings. If we are looking to bump the ring size a small amount soon without any other changes, I figure it would make sense to introduce a client-side binning implementation alongside that ring size bump, since there is no loss in space efficiency compared to the current approach. I plan to introduce a PoC in a separate issue.

## 3. Improve the distribution criteria used to select decoys (possibly move beyond the gamma)

More to come from @Rucknium on this section separately.

Here is a summary of his ideas in my words: the gamma distribution is too limiting in its application, since its shape can only be affected by 2 parameters. There are 2 general approaches of selecting outputs that would allow for a more malleable shape of the expected decoy distribution, to better match spending patterns compared to the current gamma distribution:

1. **Short- to Medium-term solution**: Use a generalized gamma distribution, which essentially takes in a larger number of parameters than the normal gamma. The shape of the generalized gamma could be flexed to better match historically observed spending patterns. Other more flexible parametric distributions could also be explored.

2. **Long-term solution**: Use a nonparametric estimator to bridge the divergence of the expected decoy distribution to the observed. As spending patterns change, the algorithm would adjust to match, rather than stay constant.

@Rucknium plans to expand on this in much more detail in a separate doc.

## 4. Implement validation at the consensus level that ensures constructed rings use the expected distribution

Today, there is next-to-no validation that a wallet is constructing decoys that follow the expected distribution. This validation can be more robust. More robust validation guarantees transaction uniformity to the distribution, and provides a stronger guarantee that all wallets conform to the expected specification. It may also make a FloodXMR attack less beneficial to the attacker (or other privacy opponents) by preventing an attacker from placing transactions on-chain that are intentionally distinguishable by their mixin distribution. Further, it can prevent users from accidentally leaving a trail (for example, by consistently delaying in submitting pre-signed transactions).

In the past, it was decided that validation for this would be too complex to implement. There may also be pernicious edge cases that cause transactions to fail unexpectedly, such as the pre-signed delayed transaction submission failure case. However, I figure it is worth revisiting to get a PoC going that shows how it can work simply, but understood if this faces pushback.

One way to do this validation is to divide the PDF of the expected distribution up by the ring size, and ensure that the ring contains outputs from each chunk of the divided PDF. For example:

```
The newest output in the ring must have P(X < x) < 1/11

The next output in the ring must have P(X < x) > 1/11 && P(X < x) < 2/11

etc.
```

When the client constructs rings, it would slot the real into its position in the PDF, and fill out the rest of the PDF chunks with decoys.

Another way proposed by @Rucknium is to perform a formal hypothesis test, with the null hypothesis being that the mixins' ages was derived from the enforced distribution. The p-value could be set to 0.05, for example. This approach is not without challenges.

# Going Forward

The general idea behind this issue is to establish an understanding for exactly why these 4 areas are worth exploring further in order to improve the decoy selection algorithm. This issue could serve as a task manager of sorts for the above 4 areas to continue exploring. If an area is deemed unworthy of further exploration, it could be removed from this issue. Once all 4 areas are sufficiently explored, accepted or rejected, this issue could be closed.

Edit 1: used correct chart
Edit 2: added one of the ways wallet-cli warns users who spend outputs that are temporally close
Edit 3: removed my claims on likely or unlikely causes and/or calculations that can't necessarily be fully justified with the above information as per comments below

# Discussion History
## Rucknium | 2021-08-25T19:09:20+00:00
Shortly I will have a draft of a roadmap to tackle "3) Improve the distribution criteria used to select decoys" for review by relevant parties. However, it will _not_ be public at this time. It is too early and too sensitive for public release.

## vtnerd | 2021-09-08T21:22:21+00:00
Those blue+orange plots (output age):

 * What is the "current selection algorithm" - `wallet2` before the recent changes?
 * Was the orange plot calculated at each block height to simulate the real-time nature of the original blue plot, or was it done from a fixed bock height?

> This suggests observed outputs in the blue spikes are much more likely to be real outputs. There does not seem any other likely explanation for the spikes.

I do not see how you can draw any conclusion (regardless of the answers to the above) from those graphs. MyMonero+Monero-LWS didn't have the integer truncation issue in the decoy selection, and was used for an unknown percentage of outputs. We'd need to see how both algorithms, done in "real-time", compared to the actual data to even start guessing at real spends. And even then we would be assuming that there isn't some other algorithm in the wild, etc.
 
> Long-term solution: Use a nonparametric estimator to bridge the divergence of the expected decoy distribution to the observed. As spending patterns change, the algorithm would adjust to match, rather than stay constant.

This should make the flood attack issue worse - an attacker can flood the network with spends AND custom decoy algorithm to alter how honest wallet users are selecting decoys. OTOH, I don't think its possible to identify "honest" spend patterns from "attacker" spend patterns to create a correct decoy distribution algorithm.

## UkoeHB | 2021-09-08T21:39:02+00:00
> Was the orange plot calculated at each block height to simulate the real-time nature of the original blue plot, or was it done from a fixed bock height?

This question makes me wonder if some of the difference between orange and blue is due to rising tx volume. Perhaps noticeably more recent decoys are selected than otherwise would be if tx volume were uniform.

## Rucknium | 2021-09-09T01:41:18+00:00
>We'd need to see how both algorithms, done in "real-time", compared to the actual data to even start guessing at real spends. And even then we would be assuming that there isn't some other algorithm in the wild, etc.

Statistical methods can reveal a lot.

>This should make the flood attack issue worse - an attacker can flood the network with spends AND custom decoy algorithm to alter how honest wallet users are selecting decoys. OTOH, I don't think its possible to identify "honest" spend patterns from "attacker" spend patterns to create a correct decoy distribution algorithm.

@vtnerd  I agree that this is a tricky issue to handle. We are still in the very early stages of examining the idea of a rolling estimator. One alternative approach would instead be to have expert analysis of the data determine the correct distribution and filter out attacks, and update it periodically. Or there could be some hybrid approach. Enforcement of a particular distribution at the consensus level would bring another set of costs and benefits. There are game theoretical issue at play, for sure. This needs CCS-funded research, which I intend to carry out.


## vtnerd | 2021-09-09T03:50:19+00:00
> Statistical methods can reveal a lot.

This response is misleading given the original context for my criticism. The author of the post (@j-berman ) was claiming that two graphs show real spends, but that doesn't appear to be true. Perhaps other statistical methods can reveal this information, but I don't see where this is demonstrated in his posts or yours.

> filter out attacks, and update it periodically.

The ability to distinguish between attack transactions and regular transactions is a bold claim, particularly in the generic flood attack where the decoy algorithm is followed. This reminds me of the person claiming to identify "Satoshi transactions", which was definitely flawed horribly.

> Enforcement of a particular distribution at the consensus level would bring another set of costs and benefits.

Might be possible, but always seemed too risky. A sharp corner in a floating point calculation would cause a chain split, etc., although luckily this seems to be usually well behaved.


## Rucknium | 2021-09-09T06:18:01+00:00
>Perhaps other statistical methods can reveal this information, but I don't see where this is demonstrated in his posts or yours.

@vtnerd  You are right: it is not. We are working on it. I am the first qualified statistician to review Monero's mixin selection algorithm and I have been able to make quite a bit of headway in a short time, with the support of @j-berman and others.

>The ability to distinguish between attack transactions and regular transactions is a bold claim, particularly in the generic flood attack where the decoy algorithm is followed. 

Stay tuned on this. Something quite concrete will be released within 10 days. I will be sure to ping you once it is released.


## j-berman | 2021-09-09T06:38:48+00:00
> What is the "current selection algorithm" - wallet2 before the recent changes?

Yes

> Was the orange plot calculated at each block height to simulate the real-time nature of the original blue plot, or was it done from a fixed bock height?

It was calculated at each block height for that exact reason. I iterated over every observed rct input in every ring over a block range, then re-selected an output using the wallet2 implementation from the distribution of rct outputs *that would have been used in the algorithm* (edit: trying to make it clear I used `rct_offsets` correctly). The intervals in chart titles are the block ranges I iterated over (for example, `[v14 2210720 - 2413735]`).

> MyMonero+Monero-LWS didn't have the integer truncation issue in the decoy selection, and was used for an unknown percentage of outputs. We'd need to see how both algorithms, done in "real-time", compared to the actual data to even start guessing at real spends.

Adding the MyMonero+Monero-LWS implementation to the mix:

![mymonero recent shift from 2 to 1](https://user-images.githubusercontent.com/26468430/132760672-6e4fc670-3915-412d-8a6c-92d5dd315626.png)

![mymonero v14](https://user-images.githubusercontent.com/26468430/132760651-a2be2ae9-0aa3-4531-ac34-713c0766d4ea.png)

![mymonero v12](https://user-images.githubusercontent.com/26468430/132778007-b4f8ff65-d514-4198-a69b-f3f348d72368.png)

EDIT: updated above charts to keep consistent with the OP for clarity

The triangular gap is still present in all cases (though smaller in the more recent interval), which seems to suggest that either another implementation is out in the wild selecting younger outputs with a high degree of frequency, or real outputs are not as well covered by the decoy selection algorithm in that triangular gap than they could be, but are still covered to a solid extent (edit: softened my wording here).

More work dedicated toward trying to remove rings that are highly unlikely to be selected using the old wallet2 or monero-lws implementation from the set of all rings could be done to determine if there other implementations out in the wild.

But at this point, I don't think that's a necessary pre-requisite to continuing work on patching integer truncation (# 1), or trying to move forward on binning (# 2), which are still likely tangible improvements given the evidence presented imo. Certainly my wording could have and should have been less strong in my conclusions, but the fact remains that these are areas where it *seems* the decoy selection algorithm *evidently* has room to improve via the solutions suggested.

I'm trying to use the information in the best way possible to improve the algorithm, and I feel this information presented reaches the bar of providing enough tangible evidence which could be used to say for example: "we should probably go with a binning approach soon-ish because of this, even before bumping the ring size a significant amount", and I personally want to shift more of my focus and work toward solutions. If it fails to reach that bar, I'm cool with going back to the drawing board, or scrapping my ideas entirely and moving on.

#### EDIT: Adding analysis on the 80k-230k range discrepancy

![openmonero cause of 100k spike v14](https://user-images.githubusercontent.com/26468430/132897084-bece1a70-1f93-43b0-8075-4a45a3c88c4e.png)

![openmonero cause of 100k spike v12](https://user-images.githubusercontent.com/26468430/132897109-871df988-f35a-4986-9fc4-fb4d92099624.png)

![openmonero cause of 100k spike average_output_time shift](https://user-images.githubusercontent.com/26468430/132897130-5002c409-2d3a-46d5-b495-fc842dbb877f.png)

I also added [openmonero's implementation](https://github.com/moneroexamples/openmonero/blob/9a447493469cd0ca5cd593aba07ae4adf1df9e98/src/RandomOutputs.cpp), which seems to have use too, for this part (and not the other) because it is more likely to select older outputs (and I zoomed out to make the charts a bit clearer and lend more context).

While neither openmonero's nor MyMonero+Monero+LWS implementation seem to corroborate the apparent blue spikes (why would the spikes be confined to the 80k - 230k age range?), it is making me think there is a higher likelihood of some implementation out in the wild that could be causing the spikes, and would agree that I am jumping too strongly to the conclusion that those spikes seem to be caused by real outputs. Analysis trying to identify rings not created via the known algorithms (and bucketing rings by algorithm if possible), seems to be a necessary pre-requisite to get a better idea of causes for the spikes. Perhaps you have other ideas of known algorithms that could feasibly be out in the wild, @vtnerd?

### General defense of my decision making in the analysis

I left out the MyMonero implementation's results in the original post so as to make this analysis simpler to understand. I agree the analysis and conclusions needed that piece of evidence to be stronger, but I didn't want to make it more confusing than it already is, and felt I provided enough information that makes it clear that what is identified is worth improving via the solutions mentioned. My point here wasn't to say "You can 100% identify real spents with certainty because of these things", it was to say, "because of these things, it seems that statistical analysis could potentially be utilized to make better guesses as to real spents, and here are some things we can do today to thwart that analysis." My wording/conclusions could have and should have been less strong, and I should have worded the post more in line with my intent, but the fact remains that these are areas where it *seems* the decoy selection algorithm *evidently* has room to improve via the solutions suggested.

For the record, if I fail to defend my logic and reasoning to support what I've done thus far (and included as a huge component of my CCS proposal), I think it would make sense for me to issue refunds to anyone who wants one (and can show their tx key) for my CCS proposal, and return remaining funds to the general fund. I have no interest in money I don't deserve.

EDIT: Perhaps  I am taking your criticisms and questioning too personally, and this was unnecessary for me to include in my initial reply:

> I feel I'm being challenged on my competence both here and [here](https://github.com/vtnerd/monero-lws/pull/22), which I'm fine with. 

I understand your criticisms are all geared towards writing the strongest code, and maintaining the strongest algorithm possible, with the strongest evidence. And all your comments have been strictly related to the work I've shown, and nothing about me personally.

EDIT 2: removed my claims on likely or unlikely causes that can't necessarily be fully justified with the above information as per comments

## SamsungGalaxyPlayer | 2021-09-10T18:11:02+00:00
I'd like to separate the claims from the raw research, since I think some people are getting carried away with the claims. A bad selection algorithm brings forward many problems, so the selection should fit reality. However, I caution pulling specific impact from these, since are mostly unfounded and difficult to measure. With that established, I think reasonable discussion on how to improve the selection algorithm, where applicable, can proceed.

## j-berman | 2021-09-10T19:25:11+00:00
Edited my comments as per above comments, feedback, and criticism.

Github probably isn't the best place for this and sorry to bring my personal thoughts here, but FWIW I think @vtnerd 's criticisms were fair, and I was incorrect in leaning too strongly toward conclusions given the evidence presented. The criticism was a bit harsher than I'm used to, and will probably take some getting used to on my part, but I'll develop thicker skin. It is completely understandable to maintain a very high standard for research done on the protocol (*especially* public research where in the worst case could be misconstrued as useful in targeting an innocent person), and for what ultimately ends up in the code, *especially* considering how important for people's privacy it is to get this area of the code right. Plus, over in our discussion in monero-lws, I did frame this analysis as a precursor for what could end up in the code over there, and as a precursor for patching/not patching integer truncation.

So basic conclusion, as far as who was more in the right and who was more in the wrong above, I accept that he is more in the right than me (edit: and me more in the wrong), both here and there.

Trying to improve. Unfiltered criticism is also welcome toward that end.

## Rucknium | 2021-09-10T19:36:58+00:00
@SamsungGalaxyPlayer What do you mean by this?:

> I'd like to separate the claims from the raw research, since I think some people are getting carried away with the claims.

## j-berman | 2021-09-17T13:39:34+00:00
On validating constructed rings match the distribution (4), here's a working code sample that shows the intuition behind the idea to assign each ring member a chunk of the PDF, and allows a margin for error for a floating point corner:

```CPP
#include <iostream>
#include <random>
#include <boost/math/distributions/gamma.hpp>
#include <fstream>

double RING_SIZE = 11;
int NUM_DECOYS = RING_SIZE - 1;

int NON_MATCHING_RING_MEMBER_BUFFER = 1;

double GAMMA_SHAPE = 19.28;
double GAMMA_SCALE = 1/1.61;

boost::math::gamma_distribution<double> boost_dist(GAMMA_SHAPE,GAMMA_SCALE);

std::random_device rd;
std::mt19937 gen(rd());
std::gamma_distribution<double> distribution(GAMMA_SHAPE,GAMMA_SCALE);

int get_index_in_ring(double x)
{
  double cumulative_probability = boost::math::cdf(boost_dist, x);
  return floor(cumulative_probability * RING_SIZE);
}

std::vector<double> select_decoys(double real_x)
{
  std::vector<double> ring(RING_SIZE, 0);

  int real_index_in_ring = get_index_in_ring(real_x);
  ring[real_index_in_ring] = real_x;

  int num_decoys_selected = 0;
  while (num_decoys_selected < NUM_DECOYS)
  {
    double x = distribution(gen);
    int idx = get_index_in_ring(x);
    if (!ring[idx])
    {
      // could over-select outputs like client does for each index, just need to make sure request enough, especially for younger index (coinbase outputs unlock after 60 blocks)
      ring[idx] = x;
      ++num_decoys_selected;
    }
  }

  // in actual code, would iterate over all members and get output indexes here
  return ring;
}

bool validate_ring_member_distribution(std::vector<double> ring)
{
  for (int i = 0; i < RING_SIZE; ++i)
    std::cout << "Ring member "<< i + 1 << ": " << ring[i] << "\n";
  
  for (int i = 0; i < RING_SIZE; ++i)
  {
    // in actual code, would work backwards from output index to derive x.
    // need to carefully handle how output is randomly selected from a block at the end of the gamma picker -- can get expected index of highest and 
    // lowest member of block output is in
    double x = ring[i];
    int expected_index_in_ring = get_index_in_ring(x);

    // The NON_MATCHING_RING_MEMBER_BUFFER provides a margin for error for whatever reason, such as a floating point corner case
    if ((i + NON_MATCHING_RING_MEMBER_BUFFER) < expected_index_in_ring || (i - NON_MATCHING_RING_MEMBER_BUFFER) > expected_index_in_ring)
    {
      std::cout << "Ring is bad... member " << i + 1 << " is " << (expected_index_in_ring < i ? "too young" : "too old" ) << "\n\n";
      return false;
    }
  }

  std::cout << "Ring is good!\n\n";
  return true;
}

void write_csv_for_analysis()
{
  std::ofstream myfile;
  myfile.open("special_selection_results.csv");

  myfile << "Specially Selected, Pure Gamma\n";

  int NUM_SIMULATED_RINGS = 100000;
  for (int i = 0; i < NUM_SIMULATED_RINGS; i++)
  {
    std::vector<double> special_ring = select_decoys(distribution(gen));

    for (int j = 0; j < RING_SIZE; j++)
      myfile << special_ring[j] << ", " << distribution(gen) << "\n";
  }
  
  myfile.close();
}

int main()
{
  // in actual code, would work backwards from real output index to derive x
  double real_x = distribution(gen);

  std::vector<double> good_ring = select_decoys(real_x);
  validate_ring_member_distribution(good_ring);

  // member 2 young enough to be member 1
  std::vector<double> bad_ring = {1, 5, 10, 10.5, 11.4, 11.8, 12.3, 13.0, 13.8, 14.8, 16.5};
  validate_ring_member_distribution(bad_ring);

  // member 9 old enough to be member 10
  std::vector<double> bad_ring2 = {1, 9.1, 10, 10.5, 11.4, 11.8, 12.3, 13.0, 14.7, 14.8, 16.5};
  validate_ring_member_distribution(bad_ring2);
    
  // member 3 young enough to be member 1
  std::vector<double> bad_ring3 = {1, 2, 3, 10.5, 11.4, 11.8, 12.3, 13.0, 13.8, 14.8, 16.5};
  validate_ring_member_distribution(bad_ring3);
    
  // member 8 old enough to be member 10
  std::vector<double> bad_ring4 = {1, 9.1, 10, 10.5, 11.4, 11.8, 12.3, 14.8, 14.9, 15.0, 16.5};
  validate_ring_member_distribution(bad_ring4);

  write_csv_for_analysis();  

  return 0;
}
```

Outputs:
```
Ring member 1: 5.92086
Ring member 2: 9.06757
Ring member 3: 10.0064
Ring member 4: 10.5402
Ring member 5: 11.4414
Ring member 6: 11.8583
Ring member 7: 12.3191
Ring member 8: 13.0634
Ring member 9: 13.8989
Ring member 10: 14.7498
Ring member 11: 16.5421
Ring is good!

Ring member 1: 1
Ring member 2: 5
Ring member 3: 10
Ring member 4: 10.5
Ring member 5: 11.4
Ring member 6: 11.8
Ring member 7: 12.3
Ring member 8: 13
Ring member 9: 13.8
Ring member 10: 14.8
Ring member 11: 16.5
Ring is good!

Ring member 1: 1
Ring member 2: 9.1
Ring member 3: 10
Ring member 4: 10.5
Ring member 5: 11.4
Ring member 6: 11.8
Ring member 7: 12.3
Ring member 8: 13
Ring member 9: 14.7
Ring member 10: 14.8
Ring member 11: 16.5
Ring is good!

Ring member 1: 1
Ring member 2: 2
Ring member 3: 3
Ring member 4: 10.5
Ring member 5: 11.4
Ring member 6: 11.8
Ring member 7: 12.3
Ring member 8: 13
Ring member 9: 13.8
Ring member 10: 14.8
Ring member 11: 16.5
Ring is bad... member 3 is too young

Ring member 1: 1
Ring member 2: 9.1
Ring member 3: 10
Ring member 4: 10.5
Ring member 5: 11.4
Ring member 6: 11.8
Ring member 7: 12.3
Ring member 8: 14.8
Ring member 9: 14.9
Ring member 10: 15
Ring member 11: 16.5
Ring is bad... member 8 is too old
```

[special_selection_results.zip](https://github.com/monero-project/research-lab/files/7187532/special_selection_results.zip)

## Python to sanity check that it produces the same result as pure gamma selecting

```py
import csv
import matplotlib.pyplot as plt
import math

MAX_X = 25
x_axis = [0] * MAX_X

ax = plt.axes()

special_gamma_counts = [0] * MAX_X
pure_gamma_counts = [0] * MAX_X

special_gamma_total = 0
pure_gamma_total = 0

with open('special_selection_results.csv', 'r') as csvfile:
    rows = csv.reader(csvfile, delimiter = ',')

    idx = 0
    for row in rows:
        if idx > 0:
            special_gamma = float(row[0])
            pure_gamma = float(row[1])

            if special_gamma < MAX_X:
                special_gamma_counts[math.floor(special_gamma)] += 1
                special_gamma_total += 1

            if pure_gamma < MAX_X:
                pure_gamma_counts[math.floor(pure_gamma)] += 1
                pure_gamma_total += 1

        idx += 1

    print("x    | Special gamma | Pure gamma")
    print("-----------------------------------")
    i = 0
    for special_gamma in special_gamma_counts:
        x_axis[i] = i

        special_gamma_counts[i] = special_gamma_counts[i] / special_gamma_total
        pure_gamma_counts[i] = pure_gamma_counts[i] / pure_gamma_total

        print("%-4s |     %1.6f  |   %1.6f" % (i, special_gamma_counts[i], pure_gamma_counts[i]))

        i += 1

    ax.plot(x_axis, special_gamma_counts, label='Special gamma', linewidth=4)
    ax.plot(x_axis, pure_gamma_counts, label='Pure gamma', linewidth=2)
    plt.legend()
    plt.show()
```

Outputs:

```
x    | Special gamma | Pure gamma
-----------------------------------
0    |     0.000000  |   0.000000
1    |     0.000000  |   0.000000
2    |     0.000001  |   0.000002
3    |     0.000040  |   0.000038
4    |     0.000470  |   0.000491
5    |     0.003557  |   0.003478
6    |     0.014425  |   0.014501
7    |     0.038541  |   0.038397
8    |     0.074509  |   0.074248
9    |     0.113127  |   0.112969
10   |     0.141128  |   0.140615
11   |     0.148195  |   0.148473
12   |     0.136585  |   0.136906
13   |     0.111653  |   0.112190
14   |     0.082396  |   0.082201
15   |     0.056102  |   0.056303
16   |     0.035655  |   0.035546
17   |     0.020663  |   0.020713
18   |     0.011400  |   0.011307
19   |     0.006012  |   0.006047
20   |     0.003018  |   0.003066
21   |     0.001432  |   0.001431
22   |     0.000672  |   0.000656
23   |     0.000293  |   0.000284
24   |     0.000125  |   0.000141
```

![special_v_pure](https://user-images.githubusercontent.com/26468430/133911254-63cf05ee-150b-4ca5-8da9-f6c70dca6b3b.png)

## Plotting PDF & CDF with the help of numpy

```py
import csv
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes()

special_gamma = []
pure_gamma = []

BINS = 100

with open('special_selection_results.csv', 'r') as csvfile:
    rows = csv.reader(csvfile, delimiter = ',')

    idx = 0
    for row in rows:
        if idx > 0:
            special_gamma.append(float(row[0]))
            pure_gamma.append(float(row[1]))
        idx += 1

special_gamma_count, special_gamma_bins_count = np.histogram(special_gamma, bins=BINS)
special_gamma_pdf = special_gamma_count / sum(special_gamma_count)
special_gamma_cdf = np.cumsum(special_gamma_pdf)

pure_gamma_count, pure_gamma_bins_count = np.histogram(pure_gamma, bins=BINS)
pure_gamma_pdf = pure_gamma_count / sum(pure_gamma_count)
pure_gamma_cdf = np.cumsum(pure_gamma_pdf)
  
plt.plot(special_gamma_bins_count[1:], special_gamma_pdf, label="Special gamma", linewidth=4)
plt.plot(pure_gamma_bins_count[1:], pure_gamma_pdf, label="Pure gamma", linewidth=2)
plt.title('PDF')
plt.legend()
plt.show()

plt.plot(special_gamma_bins_count[1:], special_gamma_cdf, label="Special gamma", linewidth=4)
plt.plot(pure_gamma_bins_count[1:], pure_gamma_cdf, label="Pure gamma", linewidth=2)
plt.title('CDF')
plt.legend()
plt.show()
```

![PDF](https://user-images.githubusercontent.com/26468430/133911217-0982d40c-b037-4514-8110-9e921ddea6af.png)

![CDF](https://user-images.githubusercontent.com/26468430/133911218-b9cd9b94-8028-48bd-8263-4f73381b7abb.png)


EDIT: added sanity check against pure gamma selecting
EDIT2: added numpy helper PDF/CDF
EDIT3: removed divide by `RING_PROPORTION` in favor of multiplying by `RING_SIZE` for clarity

## vtnerd | 2021-09-17T16:33:27+00:00
@j-berman This will definitely be an improvement

## HoverHalver | 2021-09-21T14:36:45+00:00
Rereading the thread, I find that the discrepancy exhibited by @j-berman (muchos thanks to him) between 
the real output ages histogram and the one used by the official (and near-official) wallets, quite worrying.
What seems worrying imo is **the scale** at which the 2 histograms differ.

I'm turning this in my head and I see only one possible scenario :
- there is/are wild wallet(s)  [ok, this is not really a news !]
- those wallet(s) are used **intensively** (since they generate such a massive discrepancy with the official output algo)
- such intensive usage is not due to transactions created by legit users at hand, only a script (probably replicated as multiple processes) is able to generate the volume able to cause such a discrepancy.

I would be very happy to be pointed what is wrong in the above scenario.

## iamamyth | 2021-09-21T16:16:24+00:00
Enforcing the gamma distribution (or any distribution) in consensus code would prevent a future soft fork to a better algorithm (or possibly a soft fork to fix bugs in the existing algorithm). This type of consensus-enforced distribution seems naturally at odds with a continually slowing release cycle. One must also consider the possibility that bugs in the gamma validation code would necessitate bugs in the ring selection, which seems quite a troubling failure mode, versus the current scenario where privacy suffers slightly but can be fixed somewhat rapidly.

## SamsungGalaxyPlayer | 2021-09-21T17:55:44+00:00
@iamamyth that's a valid concern, but I can't foresee a situation where we would change the algorithm solely through a soft fork. You specifically want people to follow the same curve, not spend using arbitrary or old ones.

Edit: I suppose you could argue the recent .3 update did this, but I like to hope this is a one-off.

## Rucknium | 2021-09-21T17:57:06+00:00
@HoverHalver You _should_ be worried. I think you miss an even simpler explanation: The mixin selection algorithm of the reference wallet itself poorly fits the real spend distribution. It was [designed by top computer scientists](https://www.sciendo.com/article/10.1515/popets-2018-0025) who unfortunately did not know what they were doing with the statistics. You need a qualified statistician or similar person to fix the algorithm. As an empirical microeconomist I am working on such a fix. It will take a few months to fully research the problem and develop the solution, however.

@iamamyth I agree that the enforcement issue is quite tricky and will need to be studied for a long time to understand all of the implications.

>This type of consensus-enforced distribution seems naturally at odds with a continually slowing release cycle.

In fact I am kicking around the idea of a continually-updating distribution estimated by consensus rules themselves. Seems far-fetched, but it may be possible. Statistics is a vast discipline.

## vtnerd | 2021-09-22T02:40:14+00:00
> I would be very happy to be pointed what is wrong in the above scenario.

There was a spike in transactions but the density calculation is averaged over a year. There should be a discrepancy between the "real" and computed density during certain timeframes. I don't recall seeing this mentioned anywhere (publicly), and might be a major contributor to the differences.

This is slightly different than the gamma distribution being poor overall, because a better model with an equally slow reaction should have similar issues.

> @HoverHalver You should be worried. I think you miss an even simpler explanation: The mixin selection algorithm of the reference wallet itself poorly fits the real spend distribution. It was designed by top computer scientists who unfortunately did not know what they were doing with the statistics. You need a qualified statistician or similar person to fix the algorithm. As an empirical microeconomist I am working on such a fix. It will take a few months to fully research the problem and develop the solution, however.

A person with a math background also looked at the design, and primarily criticized the density calculation (at least to me personally). This person may have been spot-on (about 2.5 years ago). My only rebuttal was/is that it was better than what we were doing previously, and improving upon probably wasn't going to be easy.

## HoverHalver | 2021-09-22T07:10:34+00:00
@vtnerd wrote 
> There was a spike in transactions but the density calculation is averaged over a year. There should be a discrepancy between the "real" and computed density during certain timeframes. I don't recall seeing this mentioned anywhere (publicly), and might be a major contributor to the differences.

Thanks for your answer.
Would it be possible to elaborate a bit more concerning the above point you mentioned ?
Could the concerned timeframes be the timeframes containing the mining txs (coinbase txs) ? That would concern ~24x30x365 = 262800 txs per year. Enough to explain (at least partly) the discrepancy ?

## j-berman | 2021-10-04T01:03:22+00:00
On the PoC to [select outputs in chunks of the PDF](https://github.com/monero-project/research-lab/issues/86#issuecomment-921805298) (or ["quantiles"](https://en.wikipedia.org/wiki/Quantile)), even if validating at consensus using that approach doesn't move forward, I think it would be sensible to do in the client anyway. It avoids the circumstance where a ring may be constructed of only recent members, revealing that the output is recent, and aiding in timing analysis.

In a PoC for wallet-side "binning" I'm working on, I'm thinking of combining the quantile approach with binning.

To see why it would be beneficial, a ring like this is possible (with low probability) with the current approach:

```
- 00: 2021-09-23
- 01: 2021-09-27
- 02: 2021-09-28
- 03: 2021-09-28
- 04: 2021-09-29
- 05: 2021-10-01
- 06: 2021-10-02
- 07: 2021-10-03
- 08: 2021-10-03
- 09: 2021-10-03
- 10: 2021-10-03
```

Notice how the oldest member of the ring is from 2021-09-23. That in and of itself is useful information ("this person received Monero at some point in the last 10 days"), and also gives some reason to guess eliminate outputs older than 2021-09-23 in other rings in the tx depending on context.

With the quantile method, the oldest output is guaranteed to come from the oldest quantile. The youngest possible "oldest" output right now would be from 2021-07-28 (assuming no bins, or 11 bins/2 members per bin, i.e. 10 quantiles).

EDIT: created a new comment for the downside below.

## j-berman | 2021-10-04T01:13:33+00:00
Potential downside with the quantile approach: assume you have a 2-input (or more) tx with real outputs that are recent or close in age. The quantile approach (and no binning) may land you with 2 rings where a single output in a quantile from both rings is very close in age, but the rest of the quantile outputs are further apart. This could possibly aid in analysis as well. Binning (and higher ring sizes) would mitigate it, however, it's worth continuing to weigh this downside, also weighed against how well the current algorithm protects against this (which also is known to have weak protection here).

Example:

```
Ring member 1:   5.92086    7.9321 
Ring member 2:   9.06757    8.86757
Ring member 3:   10.0064    10.2064
Ring member 4:   10.5402    10.7402
Ring member 5:   11.4414    11.4514   // very close, suspect?
Ring member 6:   11.8583    11.9583
Ring member 7:   12.3191    12.7191
Ring member 8:   13.0634    12.9634
Ring member 9:   13.8989    14.0002
Ring member 10: 14.7498    15.3133
Ring member 11: 16.5421    17.8421
```

EDIT: I think binning + larger ring sizes are the real mitigation to this, and it should just be assumed the current implementation is prone to the same thing as well.

## j-berman | 2021-12-26T01:35:32+00:00
I took a stab at further gauging the usefulness of binning compared to the current approach in protecting a user who spends multiple inputs in a transaction, where the inputs spent are from old transactions that are close in age (e.g. the user collects change outputs from 2 tx's over 2 days, then spends those change outputs in 1 tx >2 months later).

**I found that users seem to be decently well protected in this scenario** (even though the decoy selection algorithm isn't specifically designed to protect this). The decoy selection algorithm appears to select older decoys that are close in age at a frequency roughly close to the observed chain data.

This suggests to me binning would not necessarily be a highly useful upgrade to protect users for this scenario.

Some plausible explanations for why users have been fairly well protected:
- [wallets bias away from picking inputs that are very close in age](https://github.com/monero-project/monero/blob/319b831e65437f1c8e5ff4b4cb9be03f091f6fc6/src/wallet/wallet2.cpp#L6480)
- the warning in the wallet when a user tries to spend older outputs or close in age outputs has been effective
- it's just very rare for users to spend multiple older inputs that are close in age

Perhaps the most effective strategy to protect users for this scenario is for all wallets to use the biasing standard when picking inputs.

## The numbers

I looked at the 2-input RingCT tx's from various slices of the chain, and counted the number of tx's where there is an output in ring 1 that is at least X blocks old, and an output in ring 2 that is within Y blocks of that output. For every ring member, I also selected a new decoy running the decoy selection algorithm at the transaction's height. I did the same X->Y age check on the pure decoy selected rings as well, then compared the results. Here is [my code](https://github.com/j-berman/monero/commit/4baf4c99b002583905b4389402d9a5081d168059).

### Since v17.3.0 released (blocks 2508000 - 2522940)

|          | X: 2 months, Y: 2 days | X: 3 days, Y: 2 hours |
|------------|:-----:|:-----:|
| Count of 2 input txes total |  226216 |        226216 |
| Count of 2 input txes where there exists an output **X** old in ring 1, and an output in ring 2 that is less than **Y** away from that output      |  1.86% |     10.37% |
| pre v17.2.3 expected |  1.58% |        10.74% |
| v17.2.3 expected |  1.57% |   10.67% |
| MyMonero + monero-lws expected |  1.06% |   9.40% |
| v17.3.0 expected|  1.03% |   8.85% |

The `X: 2 months, Y: 2 days` results appear to reflect the most significant difference (1.03% -> 1.86% is a significant discrepancy. Just to explain the intuition, if 1.03% were closer to 0% and v17.3.0 were the only decoy selection algorithm in use, then it would suggest the outputs identified in the 1.86% of transactions were the real outputs spent in the transaction). However, it's difficult to draw a substantial conclusion considering many users likely have not updated to the latest version, and considering 1.57/1.58% is not far off from 1.86%, it would seem users are still decently well protected.

### v17.2.3 - v17.3.0 (blocks 2439000 - 2508000)

|          | X: 2 months, Y: 2 days | X: 3 days, Y: 2 hours |
|------------|:-----:|:-----:|
| Count of 2 input txes total |  1017478 |        1017478 |
| Count of 2 input txes where there exists an output **X** old in ring 1, and an output in ring 2 that is less than **Y** away from that output      |  2.00% |     9.67% |
| pre v17.2.3 expected |  1.80% |        10.17% |
| v17.2.3 expected |  1.77% |   10.12% |
| MyMonero + monero-lws expected |  1.20% |   8.72% |

### v14 up until anomalous volume spike (blocks 2210720 - 2409000)


|          | X: 2 months, Y: 2 days | X: 3 days, Y: 2 hours |
|------------|:-----:|:-----:|
| Count of 2 input txes total |  2209514 |        2209514 |
| Count of 2 input txes where there exists an output **X** old in ring 1, and an output in ring 2 that is less than **Y** away from that output      |  1.45% |     8.86% |
| pre v17.2.3 expected |  1.15% |        8.67% |
| MyMonero + monero-lws expected |  0.96% |   8.39% |

## Further research

It may be useful to see the numbers for outputs from the same transaction, or transactions from the same block. Also would be useful to know if other wallet implementers are implementing the bias standard and/or warning users about spending older outputs or close in age outputs.


## j-berman | 2022-01-30T04:41:45+00:00
Going to close this issue since each task is in a state where this issue is no longer necessary in my view. Happy to reopen if anyone disagrees.

### 1. Safely fix integer truncation in the wallet.

- released in [v0.17.3.0](https://www.getmonero.org/2021/12/04/monero-0.17.3.0-released.html)
- /monero-project/monero/pull/7798
____
### 2. Get "binning" to a production-ready implementation.

- #84
    - continued research into deterministic binning is on hold at the moment while Seraphis is still in its current stage of development. Deterministic binning will make more sense on the switch to larger ring sizes.
- #88
    - doesn't seem there is much support to move forward on this, and wallet-side binning in my view is not a hugely necessary upgrade that is convincing enough for me to push much further on, especially in light of [this finding that users seem to be well protected when spending old outputs close in age](https://github.com/monero-project/research-lab/issues/86#issuecomment-1001091949). The implementation in #88 is review-able in the event research proves its necessity.
___
### 3. Improve the distribution criteria used to select decoys (possibly move beyond the gamma).

- #93
    - @Rucknium is on it.
____
### 4. Implement validation at the consensus level that ensures constructed rings use the expected distribution.

- #87 
    - Seems there is not too much support to move forward on this as well at this point due to shortcomings of tying down consensus to something that perhaps will need to be modified in the future, when it may be more challenging to get the network to agree. However, very large rings + deterministic binning may necessitate this anyway. Research ongoing.
    - EDIT: also adding [this code snippet](https://github.com/monero-project/research-lab/issues/86#issuecomment-921805298) on how this could potentially be done in a way that leaves minimal risk for floating point corner cases.

# Action History
- Created by: j-berman | 2021-08-25T18:57:37+00:00
- Closed at: 2022-01-30T04:41:45+00:00
