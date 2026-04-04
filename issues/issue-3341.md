---
title: Accelerated graphics cause crash on Windows 10 20H2
source_url: https://github.com/monero-project/monero-gui/issues/3341
author: tidux
assignees: []
labels: []
created_at: '2021-02-23T03:54:40+00:00'
updated_at: '2024-07-31T16:23:49+00:00'
type: issue
status: closed
closed_at: '2024-07-31T16:23:49+00:00'
---

# Original Description
AMD RX580, latest drivers.  Starting in low graphics mode works normally, but the accelerated graphics mode reproducibly causes a hard lockup on my system.  Driver issue reported to AMD, but it might be related to something application side, since other GPU accelerated things work on this card, both games and miners.

# Discussion History
## hbroer | 2021-04-12T13:40:26+00:00
Had the same issue. Switched back GPU Mode from compute to graphics and it worked again. 

I hope this will be fixed. I have running another miner on my RX 590 and it does only half the hashrate without compute mode. 

## selsta | 2022-04-26T18:41:06+00:00
An application should never result in a hard system lockup. That's definitely a driver bug.

Is this still an issue with AMD?

## selsta | 2024-07-31T16:23:49+00:00
Closing due to inactivity.

# Action History
- Created by: tidux | 2021-02-23T03:54:40+00:00
- Closed at: 2024-07-31T16:23:49+00:00
