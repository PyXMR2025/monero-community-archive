---
title: 'Question: how to get hashes'
source_url: https://github.com/xmrig/xmrig/issues/2632
author: LinuxHeki
assignees: []
labels: []
created_at: '2021-10-16T17:34:49+00:00'
updated_at: '2021-10-18T19:48:32+00:00'
type: issue
status: closed
closed_at: '2021-10-18T19:48:32+00:00'
---

# Original Description
I want to build Xmrig into my GUI app. I want to show how many hashes I get. Is this possible? If is how can I get number of hashes?

# Discussion History
## Spudz76 | 2021-10-16T20:35:49+00:00
Use the API endpoints `/2/summary` and `/2/backends`

## LinuxHeki | 2021-10-17T09:10:49+00:00
Thanks! Where can I find documentation?

## Spudz76 | 2021-10-17T11:19:38+00:00
Well, [incomplete ones are here](https://xmrig.com/docs/miner/api)

Or, [this out of date one here](https://github.com/xmrig/xmrig/blob/master/doc/API.md)

So pretty much just load `http://miner:10080/2/summary` or `http://miner:10080/2/backends` where `miner` is your miner's host/ip and `10080` is whatever you configured for the API port.  It returns JSON.

## LinuxHeki | 2021-10-18T19:48:05+00:00
Thanks

# Action History
- Created by: LinuxHeki | 2021-10-16T17:34:49+00:00
- Closed at: 2021-10-18T19:48:32+00:00
