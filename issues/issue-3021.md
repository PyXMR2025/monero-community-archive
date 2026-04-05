---
title: opencl issue
source_url: https://github.com/xmrig/xmrig/issues/3021
author: bitmastercoin
assignees: []
labels: []
created_at: '2022-04-16T05:25:19+00:00'
updated_at: '2022-04-17T03:47:54+00:00'
type: issue
status: closed
closed_at: '2022-04-17T03:47:54+00:00'
---

# Original Description
  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2181038080
[2022-04-16 00:24:26.907]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2181038080



# Discussion History
## Spudz76 | 2022-04-16T08:26:10+00:00
You don't have >2GB of VRAM free?

## bitmastercoin | 2022-04-17T03:47:54+00:00
had to align my VRAM it was all mucked up.

# Action History
- Created by: bitmastercoin | 2022-04-16T05:25:19+00:00
- Closed at: 2022-04-17T03:47:54+00:00
