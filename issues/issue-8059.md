---
title: Encounter a know virus running OS X version of Monero GUI
source_url: https://github.com/monero-project/monero/issues/8059
author: jpitz31
assignees: []
labels: []
created_at: '2021-11-13T17:42:33+00:00'
updated_at: '2021-11-13T17:57:04+00:00'
type: issue
status: closed
closed_at: '2021-11-13T17:44:02+00:00'
---

# Original Description
Just installed Monero GUI, on a Mac running MacOS Big Sur version 11.6.

Avast virus protection indicates that the Monero GUI is infected with MacOS:Miner-DL

Refer to the below link for details on this threat:

https://www.bleepingcomputer.com/news/security/cs-go-cheat-delivers-cryptocurrency-miner-on-macos/

"SentinelOne security researcher Arnaud Abbati says the Monero miner uses the user's resources to mine funds for two email addresses registered with the MinerGate service."

Thanks

# Discussion History
## selsta | 2021-11-13T17:44:02+00:00
The GUI contains a miner, that's why it gets flagged by your anti virus.

Add an exception, there isn't anything we can do on our side.

## jpitz31 | 2021-11-13T17:49:53+00:00
Read the virus report, someone modified the source to to include a threat to mine in the background to several email addresses, one owned by a past developer.  The account is held by someone on minergate.  They are stealing resources to mine Monero into their account.

## selsta | 2021-11-13T17:52:36+00:00
That's an unrelated report from 2017.

## selsta | 2021-11-13T17:57:04+00:00
You can use these steps to confirm the binary has the correct hash: https://www.getmonero.org/resources/user-guides/verification-allos-advanced.html

# Action History
- Created by: jpitz31 | 2021-11-13T17:42:33+00:00
- Closed at: 2021-11-13T17:44:02+00:00
