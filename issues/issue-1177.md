---
title: CL_BUILD_PROGRAM_FAILURE
source_url: https://github.com/xmrig/xmrig/issues/1177
author: Wacholek
assignees: []
labels:
- bug
- opencl
created_at: '2019-09-18T09:37:49+00:00'
updated_at: '2021-04-12T15:54:50+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:54:50+00:00'
---

# Original Description
Any hint about what is wrong?
[CL_BUILD_PROGRAM_FAILURE](https://github.com/xmrig/xmrig/files/3625614/ERROR.txt)

2x HD6990 Windows 7 Catalyst 14.4
RandomX algo. 




# Discussion History
## xmrig | 2019-09-18T16:47:57+00:00
Fixed in evo branch, but this GPU will be very slow, JIT mode not implemented.
Thank you.

## Wacholek | 2019-09-19T14:04:06+00:00
> Fixed in evo branch, but this GPU will be very slow, JIT mode not implemented.
> Thank you.
I am aware of the low speed. I have several that kind of rigs. I will be more profitable to mine on CPU but those card are there and can mine something. 
I cannot test how slow it would because, I cannot run the miner. 


## Wacholek | 2019-11-03T16:57:03+00:00
Using xmrig v4.5.0 I get this:
[2019-11-03 17:46:45.371]  ocl  error CL_INVALID_KERNEL_NAME when calling clCrea
teKernel for kernel fillAes1Rx4_scratchpad
[2019-11-03 17:46:45.373]  ocl  thread #1 failed with error CL_INVALID_KERNEL_NAME

The same system and drivers as before. 

# Action History
- Created by: Wacholek | 2019-09-18T09:37:49+00:00
- Closed at: 2021-04-12T15:54:50+00:00
