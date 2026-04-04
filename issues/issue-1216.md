---
title: 'Dark theme: sync progress not correct when using bootstrap node'
source_url: https://github.com/monero-project/monero-gui/issues/1216
author: qubenix
assignees: []
labels:
- enhancement
created_at: '2018-03-30T21:40:48+00:00'
updated_at: '2018-04-04T16:49:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Sync progress shows normal without bootstrap node.

![image](https://user-images.githubusercontent.com/15707061/38154654-7b408cf0-3430-11e8-836d-eb87d83f7385.png)

With bootstrap node shows fully sync'd when not.

![image](https://user-images.githubusercontent.com/15707061/38154679-9f755a9c-3430-11e8-8859-293943b7694d.png)


# Discussion History
## dEBRUYNE-1 | 2018-03-31T08:10:41+00:00
This is somewhat expected as the wallet is, at first, connects to a remote node and thus uses the status of the remote node as daemon status. It'd probably be best to either add another status bar for the local node or let the daemon status bar indicate whether it is connected to a remote node or a local node. 

## qubenix | 2018-03-31T14:43:48+00:00
Got it. Not sure if you want to leave this open, or open a new issue at a later date. I think it's worth thinking about some way to give the user progress of their local sync without having to click `Show status`. Either of your suggestions sounds good.

## sanderfoobar | 2018-04-04T05:54:21+00:00
+enhancement

## SamsungGalaxyPlayer | 2018-04-04T16:49:08+00:00
Should the wallet use terminology such as "remote is synchronized" when it is connected to a remote node (including bootstrap) and "daemon is synchronized" when the local node is synchronized? As a side benefit, this would inform the advanced user when it is safe to send transactions with a local node.

# Action History
- Created by: qubenix | 2018-03-30T21:40:48+00:00
