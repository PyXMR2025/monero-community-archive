---
title: light mode for opencl ?
source_url: https://github.com/xmrig/xmrig/issues/1361
author: thagrisu
assignees: []
labels:
- question
- opencl
created_at: '2019-12-01T23:17:33+00:00'
updated_at: '2019-12-02T00:13:30+00:00'
type: issue
status: closed
closed_at: '2019-12-02T00:13:30+00:00'
---

# Original Description
Hey is there something like a light mode for opencl machines ? 
Even when its slow .. maybe interesting for dualmining options ? 

thanks

# Discussion History
## xmrig | 2019-12-01T23:24:13+00:00
Miner can use dataset from system memory, `dataset_host` option, it save 2080 MB of GPU memory with performance impact as well.
Thank you.

## thagrisu | 2019-12-01T23:36:00+00:00
thanks .. does this create one 2080 file for every gpu in host memory then, or do they share one dataset file ?

Is it possible to run a light version in gpu memory ? ( with 256 MB like light version for cpu ? ) since my gpus only have 600 MB free space.

## xmrig | 2019-12-01T23:41:44+00:00
One dataset shared across all GPUs and CPU, but true light mode for GPUs not supported and will not be supported.
Thank you.

## thagrisu | 2019-12-02T00:13:30+00:00
ok thanks. 

# Action History
- Created by: thagrisu | 2019-12-01T23:17:33+00:00
- Closed at: 2019-12-02T00:13:30+00:00
