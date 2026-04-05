---
title: OpenCL fails with Intel GPU
source_url: https://github.com/xmrig/xmrig/issues/1176
author: turtleminor13
assignees: []
labels:
- bug
- opencl
created_at: '2019-09-18T07:53:24+00:00'
updated_at: '2020-08-19T01:27:12+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:27:12+00:00'
---

# Original Description
With beta version 4.0.0 on Ubuntu 18.04, the opencl module fails to initialize with the Intel beignet gpu driver.
![image](https://user-images.githubusercontent.com/49797136/65128214-e4a37d00-d9ad-11e9-9ae4-fe87c151b376.png)
![image](https://user-images.githubusercontent.com/49797136/65128236-eec57b80-d9ad-11e9-8ce5-cfc9da0b1618.png)

FYI - Opencl does work on my Odroid-N2 with ARM Mali-G52 gpu, mining cn-pico on Ubuntu 18.04.  Great step forward with this version 4.0.0 unifying CPU+GPU mining!

# Discussion History
## xmrig | 2019-09-18T08:19:42+00:00
I will check later I did't check Intel platform yet seems it regression also autoconfig choice 2 threads it not right too.

About `CL_INVALID_HOST_PTR` error, not possible to fix it (only make error more cleaner), OpenCL code can't work in slow mode, it require full dataset (2080 MB).
Thank you.

## wll1rah | 2019-09-20T17:29:28+00:00
What OpenCL versions will the miner be supporting?

## xmrig | 2019-09-20T17:46:55+00:00
Intel OpenCL is not high priority, CPU in CPU mode is better, currently it broken anyway, on Windows OpenCL code compiled, but produce invalid shares.
Thank you.

# Action History
- Created by: turtleminor13 | 2019-09-18T07:53:24+00:00
- Closed at: 2020-08-19T01:27:12+00:00
