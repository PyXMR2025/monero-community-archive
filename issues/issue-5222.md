---
title: '[Discussion] Add different public wallet selection algorithm'
source_url: https://github.com/monero-project/monero/issues/5222
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2019-03-04T04:36:14+00:00'
updated_at: '2020-07-10T17:05:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Update: this proposal now focuses more broadly on public wallets, though public mining pool wallets remain the most relevant application. Related to #6688 in terms of reducing the impact of mining pool data.

I recommend that Monero implements a new input selection algorithm for public wallets that share their view keys (such as the Monero CCS) or a list of transactions publicly (such as mining pools). Doing so will limit the information leaked by transactions from public wallets.

The diagrams were made with ringsize 7, but the same situation applies to other ringsizes.

# The Problem

![image](https://user-images.githubusercontent.com/12520755/53710113-51379f80-3e01-11e9-94ff-ad5186209f27.png)

Suppose a pool controls the left yellow Monero output. It would like to make a payment to two miners and would like to receive the change back. It creates a single transaction with two outputs for the miners and the yellow output as change back.

In the future, the pool sends the change output. Unfortunately, observers could be keeping a list of outputs that the pool controls. They suspect that the pool received at least one change output. Observers can thus deduce that only the yellow output in the second transaction could be the real spend. The ring signature is compromised since the output is known to be spent in the transaction. Any other transactions that reference this output will have effective ringsizes reduced by 1. This can have a chain reaction effect on the network if this happens often enough, potentially in combination with other attacks.

Since pools often publish lists of mined blocks and sent transactions, observers can typically see the real output spent in each transaction. While there are a few exceptions (including multiple controlled outputs in the same ring, including miner payout outputs in same ring, unexpected no change output), these are rare and only slightly complicate analyses.

# The Goal

Monero should provide pools (and other public wallets) with tools to protect the integrity of these change outputs. Monero should strive to make it ambiguous when these funds are spent. Thus, users who select these change outputs sent to a public wallet as decoys will no longer have them heuristically dead. Of course, in many cases this only improves the situation; it does not remove ALL possible heuristics.

# Recommended Changes

Monero has several options on the table, but most include burden to the miners (less visible info) or more network resource requirements (churning). There is a better solution though with no downside from what I can tell: adjusting the input selection algorithm to select only outputs in a ring that were created in the same transaction.

Here is one example where the two miner payout outputs are included in the same ring signature. These three outputs appear identical; observers no longer know which one of these the pool controls and which two belong to the paid miners.

![image](https://user-images.githubusercontent.com/12520755/53709956-9f986e80-3e00-11e9-8d64-4c3a91d81dee.png)

We thus protect the integrity of these public pool change outputs. If these change outputs are spent in other transactions, they serve as effective decoys. The paid miners could be making these transactions. In the below example, another user creates a ring signature with the change output. The output is still a plausible spend.

![image](https://user-images.githubusercontent.com/12520755/53710755-5b0ed200-3e04-11e9-9a01-af28cd341cef.png)

The monero-wallet-cli should have a special `--public-wallet` flag that triggers this selection behavior. For it to work, the tool needs to:

1. Keep a list of change outputs and other outputs created during the same transaction (one list per transaction sent)
2. When spending these change outputs, use these related outputs in a single ring

If large batched transactions are created where the outputs > ringsize, the selection algorithm should select other outputs created in the same transaction at random until the necessary ringsize is met. This still protects the integrity of the change outputs, but it offers slightly less plausible deniability to the receiver outputs (usually a miner payout) that are not selected. The non-selected outputs are known to NOT be controlled by the public wallet. This is ultimately minor and certainly not a reason to be against this proposal, but it's perhaps an argument for why the ringsize should be at least as large as the maximum number of outputs in a single transaction. I do not make that recommendation here.

# Discussion History
## moneromooo-monero | 2019-03-04T10:23:32+00:00
That seems like a good idea at first glance.

# Action History
- Created by: SamsungGalaxyPlayer | 2019-03-04T04:36:14+00:00
