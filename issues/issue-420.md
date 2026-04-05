---
title: unauthenticated Error
source_url: https://github.com/xmrig/xmrig/issues/420
author: FoadRamezani
assignees: []
labels: []
created_at: '2018-02-28T20:21:59+00:00'
updated_at: '2018-03-01T03:25:16+00:00'
type: issue
status: closed
closed_at: '2018-03-01T03:25:16+00:00'
---

# Original Description
Hi dear , i have a problem, in mining ETN from spacepools i get a unauthenticated error and show this message “ rejected , unauthenticated,no active pools stop mining, this error show on programs every about 7 minutes, how can i resolve it?

# Discussion History
## FoadRamezani | 2018-02-28T20:23:46+00:00
I checked from two PCs with separate Rig ID and with diffrence difficulty

## xmrig | 2018-03-01T03:10:32+00:00
`Unauthenticated` it's error message from pool, happens when pool forgot about miner after some time without shares, but usually timeout for this is more than 1 hour. Probably some pool issue.
Thank you.

## FoadRamezani | 2018-03-01T03:25:16+00:00
I checked with 2 or 3 pools and get this error in all,thank you , i will check from another pool

# Action History
- Created by: FoadRamezani | 2018-02-28T20:21:59+00:00
- Closed at: 2018-03-01T03:25:16+00:00
