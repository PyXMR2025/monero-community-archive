---
title: GUI 2beta on W7 64b claims double spend even after re-sync following a failed
  'pending' tx
source_url: https://github.com/monero-project/monero-gui/issues/691
author: Bits-of-Wisdom
assignees: []
labels:
- resolved
created_at: '2017-04-24T05:00:31+00:00'
updated_at: '2017-08-07T18:10:11+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:10:11+00:00'
---

# Original Description
GUI 2beta on W7 64b claims double spend even after re-sync following a failed 'pending' tx

I have GUI2beta installed on W7 64b and I tried to create a transaction for xmr.to, which stayed on 'pending'. I followed the SE guide, flushed the tx pool in the deamon and re-scanned from scratch the wallet, so now it shows my old balance. HOWEVER: trying to send Monero now results in an Error message: " Couldn't send the money: transaction <TX ID> was rejected by daemon with status: Failed. Reason: double spend"
Which is by the way after daemon is flushed tx and .key file only left on the wallet so it did a full blockchain sync from scratch.
How to be able to spend from my balance now?

Thank you in advance!

# Discussion History
## Jaqueeee | 2017-04-24T09:25:43+00:00
There is a "rescan spent" button in GUI that should fix this. 

## Jaqueeee | 2017-05-02T17:17:27+00:00
@Bits-of-Wisdom did "rescan spent" help? Please close issue in that case. 

## dEBRUYNE-1 | 2017-08-07T18:08:56+00:00
This is probably resolved by now.

+resolved

# Action History
- Created by: Bits-of-Wisdom | 2017-04-24T05:00:31+00:00
- Closed at: 2017-08-07T18:10:11+00:00
