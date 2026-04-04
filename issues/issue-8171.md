---
title: '"Export_Transfers All" contains a duplicate attribute'
source_url: https://github.com/monero-project/monero/issues/8171
author: ACK-J
assignees: []
labels: []
created_at: '2022-02-09T05:04:27+00:00'
updated_at: '2022-12-02T22:00:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After running `export_transfers all` within the `monero-wallet-cli`, a csv is written that contains the following header:

block, direction, unlocked, timestamp, **amount**, running balance, hash, payment ID, fee, destination, **amount**, index, note

Notice that the attribute **amount** is accidentally used twice ( 5th and 11th), I have confirmed that the two columns contain redundant data and is simply a duplicate

# Discussion History
## mranostay | 2022-12-02T22:00:40+00:00
I've noticed a failed transaction does this.. would be nice if the comments added "Failed" so one could filter those out for tax reporting.

# Action History
- Created by: ACK-J | 2022-02-09T05:04:27+00:00
