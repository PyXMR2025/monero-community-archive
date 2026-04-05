---
title: Can I use cpu & gpu at the same time?
source_url: https://github.com/xmrig/xmrig/issues/1442
author: DEADSEC-SECURITY
assignees: []
labels:
- question
created_at: '2019-12-18T15:58:38+00:00'
updated_at: '2019-12-21T20:03:44+00:00'
type: issue
status: closed
closed_at: '2019-12-21T20:03:44+00:00'
---

# Original Description
So I was wondering if it's possible to use GPU and CPU mining at the same time and if it's possible how can I do it

# Discussion History
## Spudz76 | 2019-12-18T20:44:53+00:00
Enable both backends (see [here](https://github.com/xmrig/xmrig/blob/master/src/config.json) for a basic default config file).  The `"cpu"` and either `"opencl"` or `"cuda"` backend should have `"enabled": true` - note for CUDA you also need [xmrig-cuda](https://github.com/xmrig/xmrig-cuda/releases) built to `libxmrig-cuda.so` or `libxmrig-cuda.dll` and placed in your run location.

They will be locked to the same algo (which probably sucks, GPU can't do RandomX very well).  But works if you are mining some algo that is useful on both.

I run it in two instances, one set for cpu only, and the other with cpu off and whichever gpu on.  That way they can join the pool under different algos (using MoneroOcean).

## jacksonkr | 2019-12-20T16:12:59+00:00
Doing this on windows is easy. Update your config to have both cpu:true and opencl:true (for amd) or cuda:true (for nvidia).

If you have an nvidia card you may need to install the cuda driver separately
https://developer.nvidia.com/cuda-downloads

NOTE! this does not work with 5.3.0 - I personally use 5.1.0

# Action History
- Created by: DEADSEC-SECURITY | 2019-12-18T15:58:38+00:00
- Closed at: 2019-12-21T20:03:44+00:00
