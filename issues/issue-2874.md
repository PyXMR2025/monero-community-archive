---
title: xmrig fails to mine Ghostrider on FX-8320E
source_url: https://github.com/xmrig/xmrig/issues/2874
author: eboye69
assignees: []
labels: []
created_at: '2022-01-18T11:13:08+00:00'
updated_at: '2022-07-06T21:33:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
With FX-8320E (CPU L2:8M L3:8M 8C/8T NUMA:1)
during xmrig lauch "invalid mining.notify notification: params array has wrong size"

**To Reproduce**
During Xmrig lauch

**Additional context**
the automatic ghostrider array is
[ [8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7] ]
I try to modify it with no result


# Discussion History
## SChernykh | 2022-01-18T12:10:10+00:00
It's either an invalid config, or some pool problem. Paste your full config.json (and xmrig command line) here.

## eboye69 | 2022-01-18T12:51:28+00:00
Sorry and thanks for your help, it was a pool config error.

# Action History
- Created by: eboye69 | 2022-01-18T11:13:08+00:00
