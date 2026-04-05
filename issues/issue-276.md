---
title: Can not connect to pool on ipv6 network
source_url: https://github.com/xmrig/xmrig/issues/276
author: sh17156
assignees: []
labels:
- bug
created_at: '2017-12-19T19:39:38+00:00'
updated_at: '2018-03-14T23:42:39+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:42:39+00:00'
---

# Original Description
Hi,

I am currently on ipv6 network. I check the command ping6 monerohash.com which returns valid packets. I am using the same pool  in config.json file i.e. "url" : stratum+tcp://monerohash.com:3333 and run xmrig. This time, I could not connect to the pool.  xmrig supports ipv6 connections? Is there a way I can connect over my ipv6 network?

Thanks  

# Discussion History
## sh17156 | 2017-12-19T19:42:12+00:00
P.S. I am running ubuntu 16.04

## xmrig | 2018-03-14T23:42:39+00:00
IPv6 support was added in v2.5.
Thank you.

# Action History
- Created by: sh17156 | 2017-12-19T19:39:38+00:00
- Closed at: 2018-03-14T23:42:39+00:00
