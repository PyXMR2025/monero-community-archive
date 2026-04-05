---
title: Any change that XMRig Will support Intel ARC GPUs?
source_url: https://github.com/xmrig/xmrig/issues/3284
author: WZF888888
assignees: []
labels:
- review later
- opencl
created_at: '2023-06-06T12:21:49+00:00'
updated_at: '2025-06-18T22:37:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Any change that XMRig Will support Intel ARC GPUs?
I think Intel ARC GPUs just can use OpenCL to do mining so is it possible that you guys can add that in the next iteration?

# Discussion History
## WZF888888 | 2023-06-06T12:24:10+00:00
I try to change the platform in config to Intel and this show up.
![image](https://github.com/xmrig/xmrig/assets/100253117/146e69e7-27ad-495e-8c67-d2fa863201d7)
![image](https://github.com/xmrig/xmrig/assets/100253117/94dd6786-e084-4a77-86a0-cc682723be78)


## ahorek | 2023-06-06T23:47:11+00:00
randomx requires double precision and Arc has no hardware support for it. It's not a GPU minable algorithm anyway and emulation would make it even worse.

kawpow / cn algos could work out of the box, but I don't have an Arc to test with.

## agowa | 2025-04-16T07:47:37+00:00
That is no longer true, the new B580 and B570 do have both half and double precision floats as well.

https://en.wikipedia.org/wiki/List_of_Intel_graphics_processing_units#Battlemage_based

# Action History
- Created by: WZF888888 | 2023-06-06T12:21:49+00:00
