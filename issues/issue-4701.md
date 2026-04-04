---
title: Abnormal high rate of tx mixins are mining rewards with ringsize 0
source_url: https://github.com/monero-project/monero/issues/4701
author: lacksfish
assignees: []
labels: []
created_at: '2018-10-22T22:49:30+00:00'
updated_at: '2019-06-15T17:27:49+00:00'
type: issue
status: closed
closed_at: '2019-06-15T17:27:49+00:00'
---

# Original Description
Many Monero transactions post fork include an alarming high rate of 0 mixin inputs. I am linking below 3 random TXOs with ringsize 0, and they all are used in [this transaction here](https://xmrchain.net/tx/34036eff0f6041f6865ea5702b9fc662ac806e8e6240e33de8adf1edbf824099). You'll find this is the case for a lot of recently issued transactions!

https://xmrchain.net/tx/fb18757b748c5cc8ccdc482860eab478c62a41695b21c6aca6f15b215509803e

https://xmrchain.net/tx/7fea47e43b946cd474f1524754143b1869f819696d512704f8f61c714fcd822a

https://xmrchain.net/tx/c53b07be71ef98b9a99abf084e27e0628f8f3c1145104077572ef95d8ac9acf7


Just from a gut feeling it seems like the random decoy input selection is at first picking random blocks... and then a random tx form the block. WHAT IF THAT BLOCK IS EMTPY?!


Monero has a block every minute, and many blocks are empty, so that's why we see so many new transactions mixing with a lot of coinbase transactions from blocks, as - most of the time - this is the only tx available after a random block number select.


I think this needs to be fixed/addressed, but I'm happy to hear why this behavior changed recently.

# Discussion History
## lacksfish | 2018-10-22T23:15:04+00:00
To go into a bit of detail, normal tx inputs are way more common than the rare once-per-block coinbase transaction. Although, as the current "decoy" selection algorithm was changed, it would pick random blocks and then a random transaction from it for mixing. But many blocks are empty, so the coinbase transaction is the only one to choose from. So since they are more rare, but now get selected heavily as decoys, you can simply exclude them if you want to track Monero users, simplifying your problem. :) It is a side effect from a hastily changed and not well tested new approach to input selection, which is now potentially costing Monero users their privacy.

## lacksfish | 2018-10-22T23:30:12+00:00
I'm literally flabbergasted on how this could have made it into release branches/versions with no further discussions and testing of the privacy implications.

## xiphon | 2018-10-22T23:55:35+00:00
#4697 

## moneromooo-monero | 2018-10-23T08:08:44+00:00
Those aren't ring size 0 outputs, they're coinbases. You can spot then by the "gen" type in vin.

## iamsmooth | 2018-10-24T00:28:07+00:00
The correct characterization of the issue is not coinbases specifically it is outputs from smaller blocks being more likely to be picked (due to the algorithm of picking a block first, and then picking 1/n from the outputs in that block), at least to the extent that such blocks don't also have a smaller time interval for picking them (there is, I believe, some correlation).

## lacksfish | 2018-10-24T11:34:57+00:00
It's transactions [such as this one](https://xmrchain.net/tx/6dedf8ac37d83e486b74abb619d2f261d64edfaa18cb9cacefc8a67d3e55e13c) that especially stick out

## lacksfish | 2018-10-24T11:37:18+00:00
[This transaction](https://xmrchain.net/tx/15390ed3831ea491c7e55f3c876f9e5ddd8e56572f63b1354456d4bca2b04766) includes 6 coinbase transactions out of 10 decoys for the second input provided. I'm also just grabbing these txid's from the mempool as they flow through.

## moneromooo-monero | 2019-06-15T10:45:24+00:00
+resolved

# Action History
- Created by: lacksfish | 2018-10-22T22:49:30+00:00
- Closed at: 2019-06-15T17:27:49+00:00
