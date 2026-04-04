---
title: Mining jobs all running on a single core
source_url: https://github.com/monero-project/monero/issues/7941
author: BigassJohnny
assignees: []
labels: []
created_at: '2021-09-14T16:03:25+00:00'
updated_at: '2021-09-15T02:29:01+00:00'
type: issue
status: closed
closed_at: '2021-09-14T16:08:49+00:00'
---

# Original Description
I'm trying to get a mining benchmark on a Dell R900 with 4 Xeon X7460.  Build/installation went ok, blockchain sync at 100%.  When I start mining, every thread gets scheduled on a single core.  The output from 'top' shows one CPU at 2500% load and the other 23 idle.  Running one miner thread per core would probably work better but I can't find the right config options.  I'd rather not deal with installing a GUI and the requisite X overhead; looking for a command line/config file solution.  Monerod version is 0.17.2.0-release; OS is FreeBSD 13.0-RELEASE.

Any suggestions would be appreciated.


# Discussion History
## hyc | 2021-09-14T16:08:49+00:00
You're misinterpreting the "top" output. One CPU core can only yield 100% usage, max. If you're seeing 2500% CPU usage that means it's using at least 25 cores.

## BigassJohnny | 2021-09-14T16:19:38+00:00
Then how is it that running one thread produces the same 1.3kH/s as running 24?

## selsta | 2021-09-15T02:29:01+00:00
Try XMRig and check if you have the same issue there.

# Action History
- Created by: BigassJohnny | 2021-09-14T16:03:25+00:00
- Closed at: 2021-09-14T16:08:49+00:00
