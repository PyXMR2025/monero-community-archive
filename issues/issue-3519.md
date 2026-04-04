---
title: We need RawImport for Testnet
source_url: https://github.com/monero-project/monero/issues/3519
author: krtschmr
assignees: []
labels: []
created_at: '2018-03-29T12:33:01+00:00'
updated_at: '2022-03-16T15:39:35+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:39:07+00:00'
---

# Original Description
currently the Testnet sync can take up to 8 hours.

Either we restart the testnet once a month (not a good idea tho) or we have an official testnet download

# Discussion History
## fluffypony | 2018-03-29T12:42:11+00:00
Testnet and stagenet aren't mainnet-critical components, so I'd suggest someone host an unofficial download. If they go rogue and attack testnet and stagenet it's not a big deal.

## raxbg | 2018-03-29T12:44:18+00:00
I vote for the testnet download

## krtschmr | 2018-03-29T12:44:20+00:00
That's true. Let me talk to moneroworld, maybe he can do :)

## digianarchist | 2018-03-30T02:34:49+00:00
http://www.mediafire.com/file/4rc78pb8ed21bk1/monero_testnet_v8_1070681.raw

## selsta | 2022-03-16T15:39:07+00:00
Closing as I think there aren't any plans for an official blockchain.raw file for testnet / stagenet. Syncing is recommended, even if it takes a bit. Maybe we can look into adding checkpoints for faster sync.

# Action History
- Created by: krtschmr | 2018-03-29T12:33:01+00:00
- Closed at: 2022-03-16T15:39:07+00:00
