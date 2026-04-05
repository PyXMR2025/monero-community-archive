---
title: ' ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram'
source_url: https://github.com/xmrig/xmrig/issues/1380
author: redmac68
assignees: []
labels: []
created_at: '2019-12-04T15:16:12+00:00'
updated_at: '2021-04-12T15:11:49+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:11:49+00:00'
---

# Original Description
Updated from 5.1.0 to 5.1.1 and now get " ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram". Was OK. GPUs are rx 470s

# Discussion History
## corgiRex | 2020-03-21T12:03:21+00:00
Hi, 
I have the same problem "ocl error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram".
I have HP ProBook 4530s with dGPU - AMD, 
Win 10, xmrig-5.9.0

![Snímka](https://user-images.githubusercontent.com/62467683/77225917-1c18ff00-6b74-11ea-94a7-2a96b2a9c722.PNG)

Full listing
[ocl_error.txt](https://github.com/xmrig/xmrig/files/4362822/ocl_error.txt)

What can I do ?



## SChernykh | 2020-03-21T19:26:15+00:00
@corgiRex Your GPU (Radeon HD 7400M) doesn't support 64-bit floating point, so it can't run RandomX.

## corgiRex | 2020-03-24T22:30:38+00:00
@SChernykh 
When i install Win 10  32-bit and run XMRig 5.5.0 32-bit,
will it work with my GPU ?

## minzak | 2020-06-14T19:39:02+00:00
similar issues - https://github.com/xmrig/xmrig/issues/1734

# Action History
- Created by: redmac68 | 2019-12-04T15:16:12+00:00
- Closed at: 2021-04-12T15:11:49+00:00
