---
title: How can I change the % of CPU load via src code in say miner.cpp if I have
  a particular processor or video card on my pc?
source_url: https://github.com/xmrig/xmrig/issues/3687
author: Toxenskiy
assignees: []
labels: []
created_at: '2025-07-20T11:02:08+00:00'
updated_at: '2025-07-27T00:04:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
How can I change the % of CPU load via src code in say miner.cpp if I have a particular processor or video card on my pc?

# Discussion History
## Spudz76 | 2025-07-27T00:04:00+00:00
Throttling doesn't work like that, miner will only be able to "PWM" the load by doing less time at 100%, but it will still be pulses of 100% load on any core it is told to use.  Basically a delay between cycles, so it rests more between sprints.

# Action History
- Created by: Toxenskiy | 2025-07-20T11:02:08+00:00
