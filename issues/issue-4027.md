---
title: '[feature request] password method for wallet-rpc'
source_url: https://github.com/monero-project/monero/issues/4027
author: artyomsol
assignees: []
labels: []
created_at: '2018-06-19T17:51:49+00:00'
updated_at: '2018-10-03T17:40:25+00:00'
type: issue
status: closed
closed_at: '2018-10-03T17:40:25+00:00'
---

# Original Description
A possibility to change the  wallet  password is a "must have" feature of any wallet implementation. 
It is missed in the wallet-rpc API though implemented in [wallet-cli](https://github.com/monero-project/monero/blob/v0.12.2.0/src/simplewallet/simplewallet.cpp#L711).

# Discussion History
## moneromooo-monero | 2018-06-19T20:32:12+00:00
That seems dangerous, no ?

## artyomsol | 2018-06-19T21:18:29+00:00
I don't think it could be more dangerous than doing so with CLI or GUI.
Double checking of a new password is a duty of UI, but back end API should be able to handle the query to provide the same functionality as CLI.
IMHO, manual creation of the new one wallet (loosing the metadata collected in the previous one) just to change the password (regular operation to provide the securirty) is a bit overhead and anti pattern from the RPC point of view.

## Zarkoob | 2018-06-22T03:51:57+00:00
What kind of meta data would we be losing?

## artyomsol | 2018-06-22T12:27:45+00:00
@Zarkoob tx private keys and destinations of outgoing transfers

## moneromooo-monero | 2018-10-02T18:43:48+00:00
+hacktoberfest

# Action History
- Created by: artyomsol | 2018-06-19T17:51:49+00:00
- Closed at: 2018-10-03T17:40:25+00:00
