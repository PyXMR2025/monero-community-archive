---
title: 'Feature request: Ability to use a different pool for CPU and GPU'
source_url: https://github.com/xmrig/xmrig/issues/3084
author: benthetechguy
assignees: []
labels: []
created_at: '2022-07-07T07:18:19+00:00'
updated_at: '2022-07-08T17:30:14+00:00'
type: issue
status: closed
closed_at: '2022-07-07T20:36:52+00:00'
---

# Original Description
**Describe the bug**
I'd like to use XMRig to mine with both my CPU and GPU at the same time. For GPU mining I'm using the KawPow algorithm which doesn't support CPU, so I can't do both with one pool. I can add two pools with different algorithms in config.json, but XMRig only ever uses the first one specified unless it fails to connect.

**Expected behavior**
XMRig should have an extra config option that tells it to use certain pools only on certain backends (e.g. CPU, OpenCL, CUDA).
Alternatively, XMRig could detect that a pool/algorithm doesn't support a certain backend (e.g. KawPow not supporting CPU) and switch to the next pool (e.g. RandomX) for just that backend, while continuing to use the first pool for the other supported backends (e.g. CUDA).

# Discussion History
## SChernykh | 2022-07-07T07:24:10+00:00
The whole XMRig UI and internal code logic assume one pool connection at a time. Hashrate display, number of accepted shares, new jobs from pool and so on. Just run two XMRig instances, one for CPU and one for GPU.

## benthetechguy | 2022-07-07T20:36:52+00:00
Okay. I assumed that running two instances of XMRig would lead to decreased performance, but I guess not.

## benthetechguy | 2022-07-08T02:58:20+00:00
I was right. While GPU performance was unharmed, I could only get 10-50 H/s on RandomX CPU mining. I think it's because they're fighting for RAM and the GPU process won because it was started first.
I'm mining on an M1 Mac Mini with 8 GB RAM and the GPU shares that RAM with the CPU.

## SChernykh | 2022-07-08T08:33:33+00:00
Oh, it's M1. No, you can't run efficiently on both CPU and GPU there because they share the same memory. No matter if it's single XMRig or two instances. The only thing that might work is if you mined KawPow with GPU and GhostRider with CPU (GhostRider fits into CPU cache).

## benthetechguy | 2022-07-08T17:30:14+00:00
Would it be beneficial to mine GhostRider on both CPU and GPU, or is that not a very good algo for GPU, like RandomX?


# Action History
- Created by: benthetechguy | 2022-07-07T07:18:19+00:00
- Closed at: 2022-07-07T20:36:52+00:00
