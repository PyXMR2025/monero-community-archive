---
title: Enforce minimum of 2 outputs per transaction at the consensus level
source_url: https://github.com/monero-project/monero/issues/5399
author: Mitchellpkt
assignees: []
labels: []
created_at: '2019-04-04T21:44:35+00:00'
updated_at: '2019-08-27T16:09:53+00:00'
type: issue
status: closed
closed_at: '2019-08-27T16:09:53+00:00'
---

# Original Description
Typical transactions have at least 2 outputs: change + recipient(s). This is already implemented in the core software.

Thus, any transaction with a single output leaks two pieces of information:
1) The transaction is probably churn or a sweep
2) The user is employing non-standard software.

As far as I know, enforcing >= 2 outputs per transaction at the consensus level will not impact any entities using correctly-designed software. This will be a forcing function to ensure that *all wallets* generate transactions that are indistinguishable (in this respect) from transactions constructed by the core software.

Thoughts?

-:- Isthmus

# Discussion History
## SamsungGalaxyPlayer | 2019-04-04T21:49:32+00:00
Unless there is some strong reason to support 1-output transactions, I think this should be enforced on the protocol level as soon as possible. Sending 1-output transactions is already not possible in official wallets, and doing so reveals that the entire value of the input(s) is/are spent.

## jtgrassie | 2019-04-08T22:51:18+00:00
This prevents someone sending their entire wallet balance to someone though (which seems like a fair use case).

It also prevents someone sweeping their unspendable (dust) outputs. Another valid use case.

## hyc | 2019-04-09T01:01:05+00:00
They can do a sweep_all and specify 2 outputs. (or we can just make 2 outputs the default, if this change is accepted.)

## dEBRUYNE-1 | 2019-04-09T06:29:20+00:00
@jtgrassie & @hyc: A `sweep_all` will result in two outputs, namely one for the recipient and one output that is destined for a random address. Enforcing a minimum of two outputs per transaction at the consensus level would thus not prevent someone from sending their entire wallet balance to a recipient. 

## Mitchellpkt | 2019-04-17T05:06:41+00:00
[Neptune Research](https://www.github.com/NeptuneResearch) and I took glance at single-output transactions (1OTXs) from the last few years. You can check out the analysis in [this Jupyter Notebook](https://github.com/noncesense-research-lab/tx_in_out_distribution/blob/master/tx_ringct_1_out/single_output_txns_XMR_5399.ipynb). Plot showing key result below:

![image](https://user-images.githubusercontent.com/21246742/56262390-512eee80-6093-11e9-893c-f0b4a92293eb.png)

## Observations:
-  There have been over 2500+ single-output transactions since 2017
-  Single-output transactions (1OTXs) are a persistent intermittent phenomena
-  There was a surge of 1OTXs around height 1562000
-  1OTXs are observed to this day (data includes 2019)




## SarangNoether | 2019-04-22T17:50:15+00:00
I am in support of this. The issue has been brought up before without any movement, but it's certainly well worth it to make this a consensus requirement.

## moneromooo-monero | 2019-08-27T15:15:20+00:00
+resolved


# Action History
- Created by: Mitchellpkt | 2019-04-04T21:44:35+00:00
- Closed at: 2019-08-27T16:09:53+00:00
