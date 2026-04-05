---
title: how to limit gpu usage?
source_url: https://github.com/xmrig/xmrig/issues/2603
author: nicholasvg
assignees: []
labels: []
created_at: '2021-09-24T11:27:04+00:00'
updated_at: '2021-09-24T12:49:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
i have old card ( 2 GB ) cuda 
I want to limit GPU usage to use 50% only
how I can?

# Discussion History
## Spudz76 | 2021-09-24T12:49:27+00:00
Set bsleep 500, then it will spend 500ms every round sleeping.  Usually 125 or 250 work okay for GUI response if using same GPU for that (best not to).

Or edit config.json and reduce blocks+threads by half, that may not help depending why you only want 50% of an already slow GPU.

# Action History
- Created by: nicholasvg | 2021-09-24T11:27:04+00:00
