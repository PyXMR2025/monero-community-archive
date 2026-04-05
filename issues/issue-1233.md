---
title: Drop hashrate on amd with multiple threads
source_url: https://github.com/xmrig/xmrig/issues/1233
author: Amf1k
assignees: []
labels:
- opencl
created_at: '2019-10-11T08:49:59+00:00'
updated_at: '2021-04-12T15:53:36+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:53:36+00:00'
---

# Original Description
A config with 2 threads is generated on my RX580 and the total hash is about 400 h/s, when I leave one thread the hash is about 650 h/s. Is it a calculation error or is it faster mined with one thread? this is repeated on all versions with opencl xmrig-beta or xmrig-amd

[config and screens](https://mega.nz/#F!zpUzgQQD!dpMXlYVcsm27k2PfzsiaoA)

# Discussion History
## xmrig | 2019-10-11T14:43:21+00:00
Please show Sensors tab from GPU-Z before and after start mining, it might be memory issue, OpenCL API not provide information about free memory, in case if your GPU is not dedicated for mining, Windows can take over 500 MB of GPU memory, `864 * 2 * 2 + 500 = 3956` it very close to memory limit, solution is use less intensity for double threads mode.

Also don't need change `strided_index`, second value in array is option was known as `mem_chunk`.
Thank you.

## Amf1k | 2019-10-14T04:48:19+00:00
[screens](https://mega.nz/#F!GhlQgCLQ!wUDMrSvOwV8DE5cUeUMUNw)

Some kind of bug in GPU-Z, shows loading 100% always. Or maybe the problem is in my RX580. Memory seems to allocate correctly.

## Amf1k | 2019-11-21T09:59:14+00:00
@xmrig  hi! is there any news?


# Action History
- Created by: Amf1k | 2019-10-11T08:49:59+00:00
- Closed at: 2021-04-12T15:53:36+00:00
