---
title: Garbled payment proof right after sending payment (bug?)
source_url: https://github.com/monero-project/monero-gui/issues/2270
author: MoneroChan
assignees: []
labels: []
created_at: '2019-07-05T03:19:57+00:00'
updated_at: '2019-09-01T01:16:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I noticed that the payment proof generated is sometimes glitched right after sending a payment.
(as in "0 confirmations" waiting for Tx to leave pool)
This can cause new users to be confused or panic or 'submit incorrect proofs' to merchants, which may cause problems.

GUI Version: 
monero-gui-win-x64-v0.14.1.0.

Steps to replicate:
1. After sending transaction, go to transactions screen "immediately"
2. Click the square orange ' P ' button box to generate a payment proof.
3. The payment proof that appears is sometimes excessively long on screen, almost 2x to 3x as many bytes and characters as a normal payment proof and cannot be used to prove a Tx in the prove/verify screen.

I noticed the situation auto corrects itself once at least 1 confirmation is received, however the initial glitched payment proof may cause new users to be confused or panic or submit incorrect proofs to merchants, which may be a serious issue.

Possible solution: Disable Payment proof till at least 1 confirmation received. or display message to wait, etc..

Can someone check if this exists at the end as well?

Cheers
MC

# Discussion History
## rating89us | 2019-07-07T18:27:19+00:00
Are you using a hardware wallet together with GUI?

## MoneroChan | 2019-07-09T10:10:51+00:00
This issue was tested using a Normal GUI wallet on the newest release 

## selsta | 2019-09-01T01:16:08+00:00
I can’t reproduce this, the size of the payment proof is normal and it verifies correctly.

# Action History
- Created by: MoneroChan | 2019-07-05T03:19:57+00:00
