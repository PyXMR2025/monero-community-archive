---
title: Hashrate sometimes drops to near 0 while mining RandomX on CPU
source_url: https://github.com/xmrig/xmrig/issues/1721
author: maxime506
assignees: []
labels:
- stability
created_at: '2020-06-07T20:51:43+00:00'
updated_at: '2020-08-31T05:47:08+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:47:08+00:00'
---

# Original Description
Think this has been bugging me for awhile. This happens on either a Ryzen 1st Gen CPU or on a Intel 3rd/4th Gen CPU when mining XMR on XMrig

Even though I have another CMD window to restart miner every 3 hour or so, nonetheless there's a chance that the miner is hashing RandomX at close to 0 (and still load the CPU!) and I will have to restart it to gain full speed. Is there a way the dev can implement a command, such as restart if miner hash at lower than a certain value?

# Discussion History
## downystreet | 2020-06-08T17:35:20+00:00
What does your config.json file look like?

## implodnik | 2020-06-30T12:11:05+00:00
This issue is old and probably related to the thread manager in Windows builds 19xx and higher (see #1393, for example). The only more or less reliable way to overcome this I found is to use an external watchdog (in my case it's a simple Powershell script that runs every 10 minutes, checks the 60s hashrate and restarts the process if necessary).

Also, using "-1"s as core number specifiers instead of exact core numbers significantly reduces probability of sudden hashrate drops.

## xmrig | 2020-08-31T05:47:08+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: maxime506 | 2020-06-07T20:51:43+00:00
- Closed at: 2020-08-31T05:47:08+00:00
