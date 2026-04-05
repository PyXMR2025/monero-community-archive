---
title: About idle mining
source_url: https://github.com/xmrig/xmrig/issues/2429
author: Fleettelematicssystem
assignees: []
labels: []
created_at: '2021-06-07T13:51:48+00:00'
updated_at: '2021-06-07T15:09:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, is there any way to make the miner use **30%** of all processing and when idle, use more? I saw that there is a "pause-on-active" feature, but that would completely stop mining while it's not active, right?

# Discussion History
## SChernykh | 2021-06-07T14:28:07+00:00
You can run two copies of xmrig with different configs: first copy will always run at 30%, the second copy will use remaining CPU cores and have `pause-on-active` on.

## Fleettelematicssystem | 2021-06-07T14:53:56+00:00
I was studying at this link: https://xmrig.com/docs/miner/config/cpu

but I still don't understand, can you give me an example to use for example 20% of the CPU while it's normal and 80% when it's idle?

## SChernykh | 2021-06-07T15:09:07+00:00
You have to edit config.json, find there `"rx":[0,1,2,3,4,5,6,7],` and remove some threads from it to reduce CPU usage.

# Action History
- Created by: Fleettelematicssystem | 2021-06-07T13:51:48+00:00
