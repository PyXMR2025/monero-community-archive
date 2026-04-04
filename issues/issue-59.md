---
title: Treat pre-RingCT outputs like coinbase outputs
source_url: https://github.com/monero-project/research-lab/issues/59
author: UkoeHB
assignees: []
labels: []
created_at: '2020-01-30T04:07:02+00:00'
updated_at: '2023-10-27T17:04:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In the modern implementation of Monero (protocol v12, core software release 0.15.x.x) the outputs from ancient pre-RingCT transactions are treated quite differently from RingCT outputs. This seems uncontroversial at first glance, since such large-scale changes to the transaction structure imply a need to migrate between versions. However, the treatment of coinbase outputs reveals a much more straightforward and harmonious migration process than is currently used.

A brief summary of the situation right now (as I understand it). In protocol v1 output amounts were communicated in clear text, much like the class of Bitcoin-esque currencies. Such an output amount might say `1938892901222`. Then in v2-v3 these output amounts were split into denominations with a separate output for each chunk, say for example `1000000000000` + `900000000000` + `30000000000` + .... And, of course, in v4-onwards nearly all new outputs have had hidden amounts thanks to RingCT.

It is not clear to me how original ring signatures were constructed, given the strict limitation that amounts balance (the CryptonoteV2 whitepaper does not explain this, although they do claim to use ring signatures). In v2-v3, ring signature members all had the same amount denomination, which has fairly obvious functionality since there were likely to be at least a few multiples of each denomination floating around. In any case, now those early outputs are referred to as 'unmixable' since they can't be included in a ring with anything, and can only be spent in a pre-RingCT transaction (since RingCT transactions *require* a ring signature for inputs), where the outputs are denominated as in the v2-v3 style. The v2-v3 outputs are 'mixable' but can only be combined with other v2-v3 denomination outputs in a ring, and can be spent in a RingCT transaction. So, to get a hidden amount output when starting with an early v1 unmixable output, first create a transaction with v2-v3 outputs to make it mixable, then spend those in a normal RingCT tx.

The unusual thing is coinbase outputs, which CAN be spent in modern RingCT transactions *despite* having amounts in clear text. My proposal is merely to apply the same technique used on coinbase outputs to all pre-RingCT outputs. This would allow wallets to mostly deprecate those old transaction details, and only nodes would have to maintain backward compatibility. It means, going forward, that _all_ decoy selection for ring membership would be performed across the entire history of available outputs (from genesis to today, including all coinbase and non-coinbase outputs from any kind of transaction).

The technique is simple. Each person recording a copy of the blockchain creates a commitment to any output amount communicated in clear text. For amount `a`, the commitment is `C = 1G + aH`, where `H` is the secondary generator used in Monero commitments.

To spend it in a ring signature, add it to a ring with other clear text and hidden amount outputs (doesn't matter). Create a pseudo output commitment (following the`RCTTypeSimple` construction being used in today's protocol) to the same amount, and sign in the MLSAG with the commitment to zero created. Amounts balance correctly, and observers are none the wiser as to whether you spent a cleartext amount or hidden amount.

# Discussion History
## UkoeHB | 2020-02-01T15:37:15+00:00
Since it's usually obvious when ancient outputs are spent in a modern transaction, we can mess around with ring membership to better hide them. This technique actually facilitates that, by allowing size-11 ring sizes for every single ancient output, even if the members are from the same era (v1 or v2-v3).

## j-berman | 2023-10-25T05:57:55+00:00
Commenting for wider discussion:

With Seraphis, existing ("legacy") outputs in the chain would need to be migrated into Seraphis enotes in migration txs. Users won't need to know they're constructing these migration txs. Users just send Monero normally and these migration txs will look like normal txs in their wallet, they don't have to do anything special to migrate. This migration is necessary in order to construct Seraphis membership proofs, which can only be constructed using Seraphis enotes.

In line with the proposal spelled out in this issue, the Seraphis wallet lib constructs these migration txs with ring signatures that include combined {pre-RingCT, post-RingCT, coinbase} legacy outputs (see this [comment](https://github.com/seraphis-migration/wallet3/issues/25#issuecomment-1297000494)).

This is at odds with the general push to separate spending coinbase outputs from normal RingCT outputs:
- https://github.com/monero-project/research-lab/issues/109
- https://github.com/monero-project/monero/pull/8815

Pre-RingCT txs also didn't have that great of privacy historically (https://www.getmonero.org/2018/03/29/response-to-an-empirical-analysis-of-traceability.html), so including them could potentially reduce the efficacy of ring sigs for post-RingCT outputs.

Worth noting there's also a solid amount of additional work needed to implement support for this in addition to consensus changes:
- A database migration that stores total output counts not keyed by amount.
- The RPC used for legacy wallet scanning will need to include these counts in response.
- The RPC for selecting decoys will need to return the distribution according to this new rule.

Additionally, in order for the Seraphis wallet lib to support legacy scanning that can scan all necessary data [wallet2 needs to construct txs before the Seraphis fork](https://github.com/seraphis-migration/wallet3/issues/48), the Seraphis wallet lib would *also* need to keep track of global output ID's keyed by amount *anyway* in addition to the global count, so the wallet lib would need both.

## UkoeHB | 2023-10-25T18:41:22+00:00
> Worth noting there's also a solid amount of additional work needed to implement support for this in addition to consensus changes:

This is not a one-sided equation. Treating coinbase enotes differently in the seraphis code implies a non-trivial amount more wallet code and complexity.

## j-berman | 2023-10-25T18:43:06+00:00
Ya fair, I mentioned that that in the MRL meeting but should've mentioned that here too.

## j-berman | 2023-10-25T19:24:20+00:00
This was discussed in the most recent MRL meeting: https://github.com/monero-project/meta/issues/913

My summary of the discussion:

- There is still relatively solid support for spending coinbase outputs separately for the privacy benefit (https://github.com/monero-project/research-lab/issues/109)
- @Rucknium mentioned they plan to do some additional research on pre-RingCT output usage. This would help gauge the benefits of including them in rings alongside RingCT outputs.
- My take (piggybacking off @jeffro256): if the decoy selection algo treats all outputs the same, then when users spend >1 pre-RingCT outputs in a single tx (and rings are composed of both pre-RingCT and RingCT outputs), then pre-RingCT outputs would likely stick out as obvious real spends in each ring of the tx. This would negate the privacy benefit of including pre-RingCT outputs in the same ring as RingCT outputs.
	- This can be mitigated with some engineering of decoy selection to distinguish pre-RingCT from RingCT for the purposes of selecting decoys, which would seem to defeat the core point of this proposal.
- There seemed to be rough agreement in the meeting that wallets could warn users if they are spending pre-RingCT outputs in a tx (e.g. wallets could tell users to churn those outputs) to improve privacy when spending pre-RingCT outputs.
	- @rbrunner7 points out that probably only the CLI would end up doing this.
- @jeffro256 mentioned (and I support this fwiw) that he would like to see stronger evidence of a net privacy gain before continuing work supporting mixing pre-RingCT and post-RingCT in the same tx.

## Rucknium | 2023-10-27T17:04:13+00:00
I counted the number of non-RingCT rings and outputs created between block height 2689608 (v16 fork on 2022-08-14) and 3003871 (2023-10-25).

- 0.05% (10,024 of 18,712,969) rings were non-RingCT.

- 0.005% (468 of 8,536,690) of transactions had at least one non-RingCT ring. Since there are a higher share of non-RingCT rings than transactions with non-RingCT rings, transactions with non-RingCT rings must have a higher number of inputs than transactions with only RingCT rings, on average. In other words, transactions with non-RingCT rings are more likely to be consolidation transactions.

- 0.0005% (118 of 22,892,724) of transaction outputs were non-RingCT because of [this](https://github.com/monero-project/monero/pull/8178#issuecomment-1081307990) allowed edge case. If a user spends a non-RingCT output today, the real spend will likely be at least a year old, if not older, because there are so few non-RingCT outputs created recently.

We have a potential privacy gain for about 0.005% of transactions if we allow rings to have both RingCT and non-RingCT outputs. We can compare with other ways to improve privacy for subsets of transactions, such as transactions with nonstandard fees. Exodus released a fix to their nonstandard fee calculations in their Desktop wallet after my report to them. About 3% of transactions had the Exodus nonstandard fee. Two weeks after the fix release, the number of these transactions has been [cut in half](https://github.com/Rucknium/misc-research/blob/main/Monero-Nonstandard-Fees/images/Exodus-txs-after-fix-release.png) to about 1.5% of transaction volume. There are still at least 7% of transactions that [have nonstandard fees with unknown origin](https://github.com/Rucknium/misc-research/blob/main/Monero-Nonstandard-Fees/README.md). The current Seraphis proposal will implement fee discretization to reduce the nonstandard fee privacy problem.

The numbers on non-RingCT rings above can be produced by running [this R script](https://github.com/Rucknium/misc-research/blob/aa6c8d3409a291e394f74b0420bdab06ec1e0287/Monero-Effective-Ring-Size/xmr-ring-gathering.R) and then running:

```R
ringct.counts <- rings[, .(is.RingCT = input_amount[1] == 0),
  by = c("block_height_ring", "block_timestamp_ring", "tx_hash", "input_num")]

ringct.counts.by.tx <- ringct.counts[, .(any.non.RingCT = any(!is.RingCT)),
  by = c("block_height_ring", "tx_hash")]

v16.fork.height <- 2689608 # 2022-08-14

ringct.counts[block_height_ring >= v16.fork.height, table(is.RingCT), ]
ringct.counts[block_height_ring >= v16.fork.height, 100 * prop.table(table(is.RingCT)), ]

ringct.counts.by.tx[block_height_ring >= v16.fork.height, table(any.non.RingCT), ]
ringct.counts.by.tx[block_height_ring >= v16.fork.height, 100 * prop.table(table(any.non.RingCT)), ]

output.index[block_height >= v16.fork.height, table(output_amount > 0 & tx_num != 1)]
output.index[block_height >= v16.fork.height, 100 * prop.table(table(output_amount > 0 & tx_num != 1))]
# tx_num == 1 means that it is a coinbase output
```


# Action History
- Created by: UkoeHB | 2020-01-30T04:07:02+00:00
