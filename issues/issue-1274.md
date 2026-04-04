---
title: Couldn't start mining
source_url: https://github.com/monero-project/monero-gui/issues/1274
author: MaxXor
assignees: []
labels:
- resolved
created_at: '2018-04-05T14:23:09+00:00'
updated_at: '2018-04-20T20:45:18+00:00'
type: issue
status: closed
closed_at: '2018-04-20T20:45:18+00:00'
---

# Original Description
In latest GUI release the solo mining option does no longer work and only shows:
> Couldn't start mining

Also the mining status on the bottom is out of view and scrolling is required to view it. I had fixed this a while ago, but seems it's back again... https://github.com/monero-project/monero-gui/pull/844

# Discussion History
## dEBRUYNE-1 | 2018-04-05T15:14:28+00:00
Are you running `monerod` with `--restricted-rpc`?

## MaxXor | 2018-04-05T15:16:48+00:00
Does the GUI run `monerod` by default with `--restricted-rpc` ? I didn't change any setting.

## SamsungGalaxyPlayer | 2018-04-05T16:41:12+00:00
It does not run with `--restricted-rpc` by default.

Is it possible you are connected to a bootstrapped node if your local node is not fully synced yet?

## MaxXor | 2018-04-05T16:43:40+00:00
It's fully synced and mining worked fine in v0.11.

## MaxXor | 2018-04-06T12:42:02+00:00
Seems to be working again after fork.

## sanderfoobar | 2018-04-20T20:40:46+00:00
+resolved

# Action History
- Created by: MaxXor | 2018-04-05T14:23:09+00:00
- Closed at: 2018-04-20T20:45:18+00:00
