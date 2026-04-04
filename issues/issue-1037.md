---
title: '[Feature Request] Simplewallet upgrade_wallet'
source_url: https://github.com/monero-project/monero/issues/1037
author: ghost
assignees: []
labels: []
created_at: '2016-09-03T00:51:40+00:00'
updated_at: '2016-09-04T10:29:37+00:00'
type: issue
status: closed
closed_at: '2016-09-04T10:29:37+00:00'
---

# Original Description
Please consider adding a function `upgrade_wallet` to the next version of simple wallet to convert transactions to RingCT until the hard fork making RingCT compulsory for all transactions.

I'm happy to close this once one of the devs acknowledges they've read it.


# Discussion History
## moneromooo-monero | 2016-09-03T12:16:05+00:00
Can you describe what you mean by "convert transactions to RingCT" ?


## ghost | 2016-09-03T12:38:59+00:00
I guess moving my transactions in a piecemeal fashion to a new account through the blockchain. Now that could mean thousands of people trying to make transactions at the same time for a couple of days, but that pain would be worth it in the long run because of the massive increase in anonymity it creates.


## moneromooo-monero | 2016-09-03T18:17:49+00:00
You could use sweep_all, which... /me checks... yes, it will use rct txes. So that would use up all your (rct or not) outputs and make a rct output for you. I guess there could be a variant that only takes pre-rct outputs, that'd be easy to add.


## ghost | 2016-09-03T21:31:07+00:00
Thank you. Would be nice to make it as user-friendly as possible in the wallet itself, or provide a step-by-step writeup on stackexchange in time for release.

I'll close this tomorrow.


# Action History
- Created by: ghost | 2016-09-03T00:51:40+00:00
- Closed at: 2016-09-04T10:29:37+00:00
