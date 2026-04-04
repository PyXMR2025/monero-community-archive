---
title: balance 0 after updating monero
source_url: https://github.com/monero-project/monero-gui/issues/2042
author: dradlidr
assignees: []
labels:
- resolved
created_at: '2019-03-29T07:23:02+00:00'
updated_at: '2019-03-31T14:45:32+00:00'
type: issue
status: closed
closed_at: '2019-03-31T14:45:32+00:00'
---

# Original Description
Wallet update field on monero-gui v.0.14.0.0 I do not see the coins that I had before the update. Tell me how to fix this?

# Discussion History
## dEBRUYNE-1 | 2019-03-29T07:33:49+00:00
Did you create a transaction with GUI v0.13.0.4 while it was outdated? 

## dradlidr | 2019-03-30T09:19:45+00:00
Yes, now I do not see the transactions and coins that I had before the update

## dradlidr | 2019-03-30T09:38:14+00:00
I lost the coins that I had v0.13.0.4, the transactions that were missing, they were made before hard forks

## dradlidr | 2019-03-30T09:40:27+00:00
after I updated my wallet to v0.14.0.0, I don’t see old monens and transactions

## dEBRUYNE-1 | 2019-03-30T14:25:39+00:00
Can you try this guide? 

https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-created-pe

## dradlidr | 2019-03-30T14:27:54+00:00
I already did it, it did not help

## selsta | 2019-03-30T15:14:07+00:00
Did you make sure the correct account is selected?

You can change account under the `Account` tab.

## dradlidr | 2019-03-30T16:04:49+00:00
yes correct. I have one account

## dradlidr | 2019-03-30T16:16:19+00:00
Maybe coins can be seen in the old wallet in v0.13.0.4 it does not sync

## dEBRUYNE-1 | 2019-03-30T16:40:16+00:00
Do you see any unauthorized outgoing transactions on the history page?

## dradlidr | 2019-03-30T16:57:14+00:00
No transactions at all. which I did before hard forks. their wallet does not see them

## dradlidr | 2019-03-30T16:58:44+00:00
wallet sees transactions that were after hard forks


## dEBRUYNE-1 | 2019-03-31T07:17:06+00:00
Is your balance correct? Also, do you remember when you first created this particular wallet? 

## dradlidr | 2019-03-31T11:00:50+00:00
decidedly. Coins appeared after recovering a purse from a mnemonic phrase. on a new computer. thank you for your response

## dEBRUYNE-1 | 2019-03-31T14:43:56+00:00
All right, good to hear you managed to resolve your issue. 

## dEBRUYNE-1 | 2019-03-31T14:44:00+00:00
+resolved

# Action History
- Created by: dradlidr | 2019-03-29T07:23:02+00:00
- Closed at: 2019-03-31T14:45:32+00:00
