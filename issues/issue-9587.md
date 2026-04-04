---
title: no mining
source_url: https://github.com/monero-project/monero/issues/9587
author: luckytalk
assignees: []
labels:
- question
created_at: '2024-11-22T04:01:15+00:00'
updated_at: '2024-11-28T16:12:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
My Monero status has always been 'not mining'. Where did I go wrong? My p2pool and xmrig have been running normally all along?

# Discussion History
## moneromooo-monero | 2024-11-25T13:46:29+00:00
I assume you mean "mining_status" in monerod ?
If so, is it mining ? I assume not. If other software is mining, it cannot know about it.
If monerod is indeed mining, then please supply more details.


## luckytalk | 2024-11-27T03:25:06+00:00
I got the following when running the status command:Height: 3290208/3290208 (100.0%) on mainnet, not mining, net hash 3.15 GH/s, v16, 32(out)+0(in) connections, uptime 0d 0h 23m 25s
I guess the running status of my Monero is abnormal.

## selsta | 2024-11-27T03:26:23+00:00
If you are mining with p2pool or xmrig then monerod does not know about it, since you use external software.

## luckytalk | 2024-11-27T05:12:49+00:00
I use p2pool，and xmrig mining

## selsta | 2024-11-27T16:10:46+00:00
If you are mining with xmrig and p2pool then monerod does not know about it, thus its status will say "not mining". Does that answer your question?

## luckytalk | 2024-11-28T01:08:13+00:00
So, is this a normal phenomenon? Will Monero report mining unless they are mining themselves?

## luckytalk | 2024-11-28T01:11:18+00:00
I report every hour when using Monero CLI: no incoming connections - check firewall/routers allow port 18080. Can we also ignore it? Because I have confirmed that both my firewall and router have enabled forwarding on port 18080.

## selsta | 2024-11-28T16:12:31+00:00
monerod can only know about mining if you mine with monerod itself, if you use external programs it does not know about it.

> Can we also ignore it

Yes it can be ignored if you are ok without incoming connections. It's not an issue unless you want to contribute to the network more.

# Action History
- Created by: luckytalk | 2024-11-22T04:01:15+00:00
