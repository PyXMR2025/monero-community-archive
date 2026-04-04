---
title: Sending a tx with Mac GUI Ledger not showing address on Ledger
source_url: https://github.com/monero-project/monero/issues/7148
author: songproducer
assignees: []
labels: []
created_at: '2020-12-14T08:17:50+00:00'
updated_at: '2020-12-14T17:11:57+00:00'
type: issue
status: closed
closed_at: '2020-12-14T17:11:57+00:00'
---

# Original Description
No way to confirm address using Ledger screen

# Discussion History
## jonathancross | 2020-12-14T13:14:51+00:00
If this is specific to the GUI, it should be submitted to the [monero-gui](https://github.com/monero-project/monero-gui/issues) repo.

## selsta | 2020-12-14T13:16:16+00:00
@songproducer are you using the latest firmware, Ledger live version and ledger monero version?

## songproducer | 2020-12-14T14:20:21+00:00
I believe so
Ledger Live 1.2.4-5
Leder Monero App 1.7.5
Monero GUI 0.17.1.6-cc352e4 (Qt 5.12.8)
Embedded Monero version: 0.17.1.6-cc352e491

## selsta | 2020-12-14T14:21:18+00:00
So the only problem is that you can't verify the receiving address? Or can't you send at all?

## songproducer | 2020-12-14T14:50:28+00:00
The only issue is I can't verify the address. I don't want to send without verifying the address first.

## selsta | 2020-12-14T15:08:49+00:00
Works as expected here.

You first accept the fee, then change and then the amount and destination address.

# Action History
- Created by: songproducer | 2020-12-14T08:17:50+00:00
- Closed at: 2020-12-14T17:11:57+00:00
