---
title: Monero GUI cannot communicate with Ledger on macOS
source_url: https://github.com/monero-project/monero-gui/issues/3494
author: t-anon
assignees: []
labels: []
created_at: '2021-05-22T00:42:28+00:00'
updated_at: '2021-06-03T05:14:25+00:00'
type: issue
status: closed
closed_at: '2021-06-03T05:14:24+00:00'
---

# Original Description
- GUI 0.17.2 
- Ledger 1.3.0 w/ Monero 1.7.7
- macOS 11.3.1 (M1 chip)

The Monero application on the Ledger immediately quits if the Monero GUI wallet attempts to communicate with it.

The issue began after updating the GUI to 0.17.2  and the Ledger to 1.3.0.


# Discussion History
## selsta | 2021-05-25T03:31:47+00:00
Is this a Ledger Nano X?

## selsta | 2021-05-25T03:39:35+00:00
There does not seem to exit a Monero 1.7.7 version according to https://github.com/LedgerHQ/app-monero/releases

## t-anon | 2021-06-03T05:13:07+00:00
@selsta The issue kind of fixed itself after I cleaned out monero-wallet-gui from my laptop and re-installed. Not sure what the root cause was. 

Monero 1.7.7 definitely exists. From Ledger Manager:

<img width="263" alt="Screen Shot 2021-06-03 at 1 12 30 AM" src="https://user-images.githubusercontent.com/82717986/120590630-d4913280-c408-11eb-85b9-435f611d859d.png">




## selsta | 2021-06-03T05:14:24+00:00
Thanks for the update. Closing as the issue is resolved.

# Action History
- Created by: t-anon | 2021-05-22T00:42:28+00:00
- Closed at: 2021-06-03T05:14:24+00:00
