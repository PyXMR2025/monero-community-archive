---
title: wallet2 decoy selection algorithm ignores very recent outputs
source_url: https://github.com/monero-project/monero/issues/7807
author: j-berman
assignees: []
labels: []
created_at: '2021-07-27T01:33:28+00:00'
updated_at: '2021-09-15T22:37:13+00:00'
type: issue
status: closed
closed_at: '2021-09-15T22:36:41+00:00'
---

# Original Description
UPDATE: it was discovered that MyMonero has been using a [separate implementation](https://github.com/vtnerd/monero-lws/blob/faa51780f3f8e6c5c0c4235499b95c246e074f29/src/util/gamma_picker.cpp) of the decoy selection algorithm that *did not have the bug*. Therefore, MyMonero users could have feasibly constructed transactions that selected newly spendable outputs as decoys, which means newly spent outputs observed on chain are not guaranteed identifiable as real outputs.

## Overview

The decoy selection algorithm in wallet2 has next to 0 chance of selecting extremely recent outputs as decoys. Today, if a user spends an output right in the block that it unlocks, and the output was originally created in a block that has fewer than 100 outputs total in it, their real output would be (edit: more) clearly identifiable in the ring (edit: outputs are not guaranteed identifiable primarily because of MyMonero's existing popular alternative algorithm in use). For reference, the trailing yearly average is around 63 outputs per block. ~Therefore, outputs that are spent immediately when they unlock are likely identifiable in rings today.~

To be clear, I have run this by core devs before sharing publicly.

## Technical explanation

It helps to explain the entire intuition behind the decoy selection algorithm, and provide some charts to explain the bug. Apologies if some of this is rudimentary, and also apologies if I got some of this wrong.

The decoy selection algorithm selects 10 decoys to include in a ring, and hides the real output among them using a criteria that best hides the real output. It does this by selecting decoys based on the expected time of when outputs are spent.

In the paper by [Miller et al](https://arxiv.org/pdf/1704.04299/) (section 6.1), they recommended using a particular distribution known as a gamma distribution to select decoys that correctly mirrors real world spending patterns observed on Monero back when Monero outputs could be linked on-chain. Here is what the gamma distribution recommended in the paper looks like:

![exp(x)](https://user-images.githubusercontent.com/26468430/127079746-4060a09f-2a7f-4cfc-9675-39f8e0913e0a.png)


The intuition behind the above chart: today, `exp(x)` is roughly equivalent to the age of outputs when they are spent (in seconds). For example, if `exp(x)` is 120, it means an output was 120 seconds old when it was spent. When you zoom into a particular point on that chart, the y-value is the expected probability of an output that is `exp(x)` seconds OR younger being spent. For example, when exp(x) is ~133,000, the y-value is ~0.50. This means that ~50% of outputs are expected to be spent in ~133,000 seconds or less.

Now, the above chart does not take into consideration that rings use 10 decoys. The probability that among 10 outputs, there is at least one output with an `exp(x)` of ~133,000 seconds or less is actually much higher than the probability of observing a single exp(x) of ~133,000 or less. After factoring in the fact that there are 10 decoys in rings, here is what the chart looks like showing the expected probability of a ring including at least one output that is exp(x) seconds or less as you move right along the x-axis: 

![exp(x) included in ring](https://user-images.githubusercontent.com/26468430/127080470-e20231d1-b971-4768-9b28-8be9a58485f1.png)

Squaring the above with the implementation of the decoy selection algorithm, upon arriving at an exp(x), it divides exp(x) by `average_output_time`, and then uses this value to subtract from the total number of outputs **starting from 10 blocks prior to the current height**. This is the English version of what [this code is doing](https://github.com/monero-project/monero/blob/de3456e1275836725291ba71036b7ef0e2cda91f/src/wallet/wallet2.cpp#L1018-L1034):

```
gamma_picker::gamma_picker(const std::vector<uint64_t> &rct_offsets, double shape, double scale):
    rct_offsets(rct_offsets)
{
  gamma = std::gamma_distribution<double>(shape, scale);
  
...

  begin = rct_offsets.data();
  end = rct_offsets.data() + rct_offsets.size() - CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE;
  num_rct_outputs = *(end - 1);
  THROW_WALLET_EXCEPTION_IF(num_rct_outputs == 0, error::wallet_internal_error, "No rct outputs");
  average_output_time = DIFFICULTY_TARGET_V2 * blocks_to_consider / outputs_to_consider; // this assumes constant target over the whole rct range
};

gamma_picker::gamma_picker(const std::vector<uint64_t> &rct_offsets): gamma_picker(rct_offsets, GAMMA_SHAPE, GAMMA_SCALE) {}

uint64_t gamma_picker::pick()
{
  double x = gamma(engine);
  x = exp(x);
  uint64_t output_index = x / average_output_time;
  if (output_index >= num_rct_outputs)
    return std::numeric_limits<uint64_t>::max(); // bad pick
  output_index = num_rct_outputs - 1 - output_index;

...
```

 Note that today, as highlighted in PR #7798, `average_output_time` is equal to 1. Therefore, exp(x) is equivalent to seconds *today*.

Now, observe on the second chart from above that among 10 decoys, the probability of there being at least one exp(x) of ~100 or lower is effectively 0. This means that the decoy selection algorithm in the reference wallet code will practically never select an exp(x) of 100 or lower. This means that unless an output_index that is 100 or more recent is included in a block that has MORE than 100 outputs, there is practically 0 chance the decoy selection algorithm will select it. The fact that there is still a chance to select a decoy with output index <100 is thanks to [this part of the algorithm](https://github.com/monero-project/monero/blob/de3456e1275836725291ba71036b7ef0e2cda91f/src/wallet/wallet2.cpp#L1036-L1045) which takes the output_index determined by exp(x), finds the block it's in, and then randomly selects an output from that block. So outputs from blocks that have >100 outputs have a chance at being selected as decoys. But a block that has 10 outputs in in it for example has 0 chance to have any of its outputs selected as a decoy.

## Observing the practical impact

At block height 2412231, there were 35746773 total outputs. Therefore, when users constructed transactions at block height 2412241, any outputs below 35746773 *should* have been fair game for inclusion in rings. However, there was practically 0 chance a ring would include outputs 35746772 to 35746672, which you can see in this chart:

![Expected inclusion of output_index in ring](https://user-images.githubusercontent.com/26468430/127079865-1c38aece-5e4b-468d-83e7-3a94e58cf0de.png)

I also ran get_outs 100k times (i.e. constructed 100k rings) at height 2412241 using [this code](https://github.com/j-berman/monero/pull/2), and not a single output from either blocks 2412231 or 2412230 was selected as decoys in any of the 100k rings.

[Here is another way to observe the impact of this bug](https://github.com/neptuneresearch/monero-ringmember-age-distribution/blob/main/png/v14rct_peakzoom.png). That chart is the observed on-chain distribution of outputs over the block range 2210720 to 2402699 (since Monero v14). Notice all the way at the left, there is a step-up to the peak. The peak is at 11 or 12, but there are observed outputs at 10. I believe this odd step-up is explained by the algorithm's tendency to ignore very early recent outputs. I discovered this bug while investigating this odd step-up. I went down the list of plausible explanations for the odd step-up, and landed on this bug as the most likely explanation.

## The fix

Still working through it. I believe we'll need to re-assess the paper's observed spend-time distribution to be certain the fix is correct. But, the fix would almost certainly require a change to decoy selection and would have some impact on tx uniformity similar to #7798, where clients that don't update would construct rings in a marginally different way than clients that do.

My first thought for the fix was that the decoy selection algorithm was essentially off by 10 blocks, meaning the gamma distribution recommended in the paper was *already* factoring in unlock time. Thus, my expectation was that the decoy selection algorithm is incorrectly applying the gamma distribution to the set of spendable outputs starting from 10 blocks prior, rather than applying it toward the set of ALL outputs, and then removing outputs from the ring that are not spendable. However, this does not appear to be correct, since the probability of an output spent between 120 and 1200 seconds ago is not negligible in the gamma distribution.

The fix I'm leaning toward at the moment is that the algorithm is off by 1 block, meaning that the paper's observed gamma distribution simply plotted observed spents. At a block time of 120 seconds, you would expect next to 0 outputs to be spent in less than 120 seconds, which the paper's recommended gamma distribution seems to corroborate.

More knowledge on the history of the 10 block unlock time and squaring that with the paper's observed gamma distribution would likely explain the above, and make the correct fix very clear.

Finally, once the fix is known, I can assess its impact on transaction uniformity assuming a percentage of clients don't update, and so we can decide if the change should be made as part of a hard fork or not alongside the fix in #7798.

# Discussion History
## j-berman | 2021-07-27T05:12:33+00:00
From [freddieraynolds on Twitter](https://twitter.com/FreddieRaynolds/status/1419881860247793665):

> If outputs can be identified as true spend this impacts privacy of all other XMR txs even those who do wait to spend since now their rings contain decoys that can be excluded. Any idea what the scope of impact here is?

This likely would only affect a tiny fraction of Monero transactions. The absolute maximum number of rings affected is probably < 1% (since block 2300000, only ~1% of outputs used in rings were between 10 and 12 blocks old, and a percentage of those were  likely decoys). Thus, all else equal, it would be next to impossible for this bug to compromise other transactions on the network (1% ^ 10 = 0.000000000000000001%).


## j-berman | 2021-09-15T22:36:41+00:00
Patched in #7821 

# Action History
- Created by: j-berman | 2021-07-27T01:33:28+00:00
- Closed at: 2021-09-15T22:36:41+00:00
