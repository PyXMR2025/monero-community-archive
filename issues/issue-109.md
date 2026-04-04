---
title: Avoid selecting coinbase outputs as decoys
source_url: https://github.com/monero-project/research-lab/issues/109
author: Rucknium
assignees: []
labels: []
created_at: '2023-01-04T20:20:44+00:00'
updated_at: '2023-01-29T01:12:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Summary

This issue is for discussing a potentially privacy-improving decoy selection rule for ring signatures that would entirely avoid using any coinbase outputs as decoys.

## p2pool Coinbase Transactions

Most, if not all, coinbase transactions produced by centralized mining pools or solo miners have a single output. Therefore, these outputs occur once per block. The probability that they would be included in any given transaction's ring is low.

p2pool coinbase transactions split the block reward among dozens and sometimes hundred of miners, producing dozens or hundreds of outputs in each p2pool block that are small in value. I wrote an [R script](https://github.com/Rucknium/misc-research/tree/main/Monero-p2pool-Output-Stats) that calculates the number of p2pool outputs for any interval of time.

The numbers for Sept. 28 2022 to December 27, 2022 (block heights 2721396 to 2786779) are:
```
Total number of blocks: 65384
Number of blocks found by p2pool: 4540 (6.94% of total)
Summary statistics on number of payout outputs per block found by p2pool:
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
   66.0   104.0   113.0   128.4   122.0   615.0 
Total number of transaction outputs: 4,123,336
Number of p2pool payout transaction outputs: 582,919 (14.14% of total)
```

## Privacy Risk of Status Quo

Given that 14 percent of all outputs are p2pool payouts, we can approximate the probability of any given ring selecting a certain number of p2pool outputs as decoys by computing the probability density function of a Binomial(15, 0.14) distribution (under some mild simplifying assumptions).

A simple R script to calculate:

```R
for (i in 0:15) {
cat("Probability that a ring has ",
  formatC(i, width = 2),
  " p2pool coinbase outputs as decoys: ",
  formatC(round(dbinom(i, size = 15, prob = 0.14) * 100, 3), digits = 3, width = 6, format = "f"),
  " % \n", sep = "")
}
```
which produces:
```
Probability that a ring has  0 p2pool coinbase outputs as decoys: 10.411 % 
Probability that a ring has  1 p2pool coinbase outputs as decoys: 25.421 % 
Probability that a ring has  2 p2pool coinbase outputs as decoys: 28.968 % 
Probability that a ring has  3 p2pool coinbase outputs as decoys: 20.435 % 
Probability that a ring has  4 p2pool coinbase outputs as decoys:  9.980 % 
Probability that a ring has  5 p2pool coinbase outputs as decoys:  3.574 % 
Probability that a ring has  6 p2pool coinbase outputs as decoys:  0.970 % 
Probability that a ring has  7 p2pool coinbase outputs as decoys:  0.203 % 
Probability that a ring has  8 p2pool coinbase outputs as decoys:  0.033 % 
Probability that a ring has  9 p2pool coinbase outputs as decoys:  0.004 % 
Probability that a ring has 10 p2pool coinbase outputs as decoys:  0.000 % 
Probability that a ring has 11 p2pool coinbase outputs as decoys:  0.000 % 
Probability that a ring has 12 p2pool coinbase outputs as decoys:  0.000 % 
Probability that a ring has 13 p2pool coinbase outputs as decoys:  0.000 % 
Probability that a ring has 14 p2pool coinbase outputs as decoys:  0.000 % 
Probability that a ring has 15 p2pool coinbase outputs as decoys:  0.000 % 
```

Between one and three decoys are usually wasted on p2pool coinbase outputs. This means that effective ring size is usually 15 - 13 rather than the intended 16.

In most transactions, p2pool outputs can be ruled out as the real spend because p2pool miners need to consolidate their payouts in transactions with a large number of inputs. Furthermore, the miners' addresses are in plaintext on the p2pool side chain, observable by Monero privacy adversaries. @SChernykh can discuss the issue in greater detail.

## Implementation

This change would not require a network upgrade (hard fork) because decoy selection is not enforced by any blockchain consensus rules. This would be a change at the wallet software level.

It would make the most sense to implement this in production code at the same time that the decoy selection changes of [OSPEAD](https://github.com/monero-project/research-lab/issues/93) are implemented, assuming that OSPEAD passes review. Simultaneous implementation would avoid creating yet another "anonymity puddle" where users who are slow to update their software are transacting with diverse versions of the decoy selection algorithm.

With this wallet-level change, when a miner spends a coinbase output, the coinbase output would still be included in the ring. It would be obvious to observers that the miner's coinbase output is the real spend in that ring. The behavior could be changed by #108 

## Further Reading

[Wijaya, Liu, Steinfeld, & Liu (2021) "Transparency or anonymity leak: Monero mining pools data publication."](https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=37)

[Ehrenhofer (2019) "Let’s Stop Using Coinbase Outputs."](https://medium.com/@JEhrenhofer/lets-stop-using-coinbase-outputs-da672ca75d43)

[Monero issue 6688: Separate coinbase and non-coinbase rings](https://github.com/monero-project/monero/issues/6688)

[January 04, 2023 MRL meeting log](https://github.com/monero-project/meta/issues/776)

[December 28, 2022 MRL meeting log](https://github.com/monero-project/meta/issues/773)

[December 20, 2022 MRL meeting log](https://github.com/monero-project/meta/issues/772)


# Discussion History
## Rucknium | 2023-01-18T18:14:35+00:00
@SChernykh has [announced](https://www.reddit.com/r/MoneroMining/comments/1095730/psa_p2pool_network_upgrade_aka_hardfork_on_march/) an [upgrade](https://github.com/SChernykh/p2pool/issues/221) to P2Pool that will reduce the number of P2Pool payout outputs by 50 to 67 percent. That's a big accomplishment, but user privacy can still be improved by this proposal to avoid selecting coinbase outputs as decoys.

I did some historical analysis of P2Pool payout outputs and how they affect privacy of non-mining users.

Below is a plot of the share of blocks mined by P2Pool. It has risen slowly over time to about 9 percent today, with some spikes and dips.

![p2pool-mined-blocks](https://user-images.githubusercontent.com/86333515/213260724-36f57398-17aa-45f8-9d8e-274d8aa0a350.png)

The total number of Monero transaction outputs per week fell after the hard fork because of the crash in Monero transaction volume.

![outputs-total](https://user-images.githubusercontent.com/86333515/213260807-8d1c7755-c147-4860-b5ae-9817308f1f51.png)

The post-fork crash after the hard fork plus the stable P2Pool share of mined blocks caused the share of P2Pool outputs to increase from about 5 percent to 15 percent.

![p2pool-outputs-share](https://user-images.githubusercontent.com/86333515/213260874-7db63d0e-a4de-4533-9977-11f28d433209.png)

The low share of P2Pool outputs before the hard fork is good news. It means that the negative privacy effect was low at a time when the ring size was lower. The pre-fork ring size was 11. Now it is 16.

We can approximate the effective ring size for each week using the theoretical Binomial distribution again. Effective ring size is the number of ring members that are not P2Pool outputs. The median effective ring size is plotted below. The median value of X means that 50 percent of all rings have an effective ring size of X or below.

![median-effective-ring-size](https://user-images.githubusercontent.com/86333515/213260933-67472c57-c4f9-4172-aa65-15ecd9e1dda2.png)

The plot shows that median effective ring size still increased after the hard fork despite the larger P2Pool share of outputs.

The median is "typical luck". We also want to be aware of what can happen when an unusually high number of P2Pool outputs are selected as decoys. These are "unlucky" rings. Below is a plot of the 5th percentile of effective ring size. That's the 5 percent unluckiest rings. The unluckiest rings have almost the same effective ring size before and after the hard fork.

![unlucky-5-percent-effective-ring-size](https://user-images.githubusercontent.com/86333515/213260975-ed7966b6-3fbb-4c6d-8c50-6bc8f0a702d1.png)

The code to reproduce this analysis is at https://github.com/Rucknium/misc-research/tree/main/Monero-p2pool-Output-Stats/analysis



## WojasKrk | 2023-01-29T01:12:15+00:00
W #78 #78 

# Action History
- Created by: Rucknium | 2023-01-04T20:20:44+00:00
