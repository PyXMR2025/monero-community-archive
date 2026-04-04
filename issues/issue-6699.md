---
title: Internal wallet error, casting problem
source_url: https://github.com/monero-project/monero/issues/6699
author: OxMarco
assignees: []
labels: []
created_at: '2020-07-06T14:37:33+00:00'
updated_at: '2020-07-06T15:22:47+00:00'
type: issue
status: closed
closed_at: '2020-07-06T15:22:47+00:00'
---

# Original Description
Compiled _monero_ project on Mac OSX, started the daemon and the wallet roc, as soon as I run "open wallet" I get:
_E static_cast<uint8_t>(m_nettype) != field_nettype. THROW EXCEPTION: error::wallet_internal_error_

The wallet exists and can be opened on another computer, what's wrong with this newer install?

# Discussion History
## sumogr | 2020-07-06T15:06:55+00:00
You are trying to run a wallet created on testnet on mainnet or vice versa.

## OxMarco | 2020-07-06T15:13:18+00:00
no I'm running both the daemon and the wallet rpc on testnet, I think it has something to do with boost libraries being updated a few days ago

## sumogr | 2020-07-06T15:16:20+00:00
both daemon and rpc are run with the --testnet flag on right? what boost libraries?

## OxMarco | 2020-07-06T15:22:47+00:00
Yes flag on both. I solved with reinstalling boost, apparently brew didn't fetch dependencies correctly. 

# Action History
- Created by: OxMarco | 2020-07-06T14:37:33+00:00
- Closed at: 2020-07-06T15:22:47+00:00
