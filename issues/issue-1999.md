---
title: Option to save signed transaction to file from full wallet
source_url: https://github.com/monero-project/monero/issues/1999
author: mochaccinuh
assignees: []
labels:
- invalid
created_at: '2017-04-23T21:59:47+00:00'
updated_at: '2017-09-20T20:48:28+00:00'
type: issue
status: closed
closed_at: '2017-09-20T20:48:28+00:00'
---

# Original Description
When doing "transfer" in a view only wallet an unsigned transaction is stored to a file. It would be nice if full wallet (with spend key) also could save transaction to file and in addition sign the transaction. This enables a full cold wallet to easily create transactions that are ready to be broadcast to the network via a hot wallet with submit_transfer.

# Discussion History
## moneromooo-monero | 2017-07-24T12:30:45+00:00
The cold wallet already saves the signed transaction to a file. Can you elaborate on what you are asking exactly ?

## hyc | 2017-09-20T20:47:48+00:00
+invalid


# Action History
- Created by: mochaccinuh | 2017-04-23T21:59:47+00:00
- Closed at: 2017-09-20T20:48:28+00:00
