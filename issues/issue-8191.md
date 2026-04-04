---
title: Support for subaddress private view key
source_url: https://github.com/monero-project/monero/issues/8191
author: crocket
assignees: []
labels: []
created_at: '2022-02-23T06:43:34+00:00'
updated_at: '2022-05-25T10:25:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
For now, the private view key allows anyone to view all addresses under a monero seed.
This is bad since there are cases where people collect money for group purchase. People who fund a group purchase require transparency for group purchase, and the group purchase organizer can't just provide the private view key for one single subaddress that collects the fund for group purchase.

This is also suboptimal for thorchain integration. Thorchain is going to require a private view key for withdrawing staked monero to wallets. Rather than giving the private view key for a monero seed, a private view key for a single subaddress is desired. I don't want to create a new monero seed just for withdrawing monero staked on thorchain monero liquidity pool.

# Discussion History
## selsta | 2022-02-23T19:49:37+00:00
The point of subaddresses is that there is a single global view key. Even if a per subaddress view key would be possible, I don't think it's planned currently.

## crocket | 2022-02-23T22:58:06+00:00
> The point of subaddresses is that there is a single global view key.

A single global view key doesn't give people granular control over which subaddresses to reveal to others.

## trasherdk | 2022-02-24T07:30:29+00:00
It could make sense for accounts, or what?

## crocket | 2022-02-24T08:25:25+00:00
An account view key sounds fine since it is easier to manage than subaddress view key.

# Action History
- Created by: crocket | 2022-02-23T06:43:34+00:00
