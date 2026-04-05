---
title: How to mine with nvidia NVIDIA A100 80G?
source_url: https://github.com/xmrig/xmrig/issues/2894
author: AhrimanSefid
assignees: []
labels: []
created_at: '2022-01-25T01:11:42+00:00'
updated_at: '2022-01-25T18:59:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi All.
can help me mine with nvidia NVIDIA A100 80G?
64 core cpu
1tb ram
3 vga A100 80G

# Discussion History
## Spudz76 | 2022-01-25T10:03:52+00:00
That is a CUDA Capability 8.0 which is pretty good, plus it has HBM2e which is ridiculously good.

Build or download [`xmrig-cuda`](https://github.com/xmrig/xmrig-cuda) the release is only available for Windows, match the CUDA version in your driver which is shown in `nvidia-smi` output top right corner.  If you build it you can pass `-DCUDA_ARCH=80` in the cmake step to save compile time (only build what's needed for your specific card).

Place the dll (or so) library plugin in the same directory as main xmrig executable.  Find the `cuda` section of the `config.json` and set `"enabled": true,` instead of default which is `false`.  Launch xmrig and it should detect GPU and set up thread profiles.

## AhrimanSefid | 2022-01-25T14:09:24+00:00
Linux support?
ubuntu

## Spudz76 | 2022-01-25T18:59:01+00:00
Build doc, bottom section

https://xmrig.com/docs/miner/build/ubuntu

# Action History
- Created by: AhrimanSefid | 2022-01-25T01:11:42+00:00
