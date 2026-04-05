---
title: No Active Pools, Stopped Mining.
source_url: https://github.com/xmrig/xmrig/issues/173
author: cmarshall108
assignees: []
labels: []
created_at: '2017-10-24T22:36:41+00:00'
updated_at: '2017-11-27T00:38:14+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:38:14+00:00'
---

# Original Description
I tried to setup the miner and even set the values in the config JSON file, verified the miner is connected to NiceHash; but i'm not getting any stats and no calculations are being submitted. The console will eventually say, "no active pools, stop mining" and disconnects from NiceHash's pool.

# Discussion History
## cmarshall108 | 2017-10-24T22:37:32+00:00
![screen shot 2017-10-24 at 6 37 05 pm](https://user-images.githubusercontent.com/22750553/31971576-63741dec-b8ea-11e7-877b-d3664098cf0d.png)


## xmrig | 2017-10-25T11:03:39+00:00
10 minutes timeout happen, can not avoid this, but it will successfully reconnect after that.
Diff 80000 to high for your hashrate, so it ok if you not submit shares in 10 minutes.

# Action History
- Created by: cmarshall108 | 2017-10-24T22:36:41+00:00
- Closed at: 2017-11-27T00:38:14+00:00
