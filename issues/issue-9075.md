---
title: Fast Sync checkpoints for stagenet
source_url: https://github.com/monero-project/monero/issues/9075
author: duggavo
assignees: []
labels:
- proposal
- discussion
created_at: '2023-11-22T22:04:05+00:00'
updated_at: '2023-12-07T20:35:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Synchronizing on stagenet and testnet is very slow, especially syncing before RandomX, since Cryptonight verification is very slow,

Fast Synchronization check points should be added for stagenet and possibly testnet too, to reduce synchronization time.

# Discussion History
## selsta | 2023-11-24T15:26:23+00:00
Enabling fast sync causes some verification code to get skipped. For the sake of testing alone we shouldn't enable this on all 3 networks.

I guess enabling it on stagenet only is ok.

# Action History
- Created by: duggavo | 2023-11-22T22:04:05+00:00
