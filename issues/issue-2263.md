---
title: CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2986344448
source_url: https://github.com/xmrig/xmrig/issues/2263
author: KMKAR
assignees: []
labels: []
created_at: '2021-04-13T21:45:02+00:00'
updated_at: '2021-04-13T22:45:15+00:00'
type: issue
status: closed
closed_at: '2021-04-13T22:45:15+00:00'
---

# Original Description
Hi.
I'm getting CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 2986344448 using the following environment:
xmrig 6.11.2
AMD Radeon r7 250 (1gb ddr5) / Drivers: 21.2.3 / OpenGL 4.6 / OpenCL 1.2
Windows 10 (10.0.18363.476)

Information from clinfo, extract from application console with the error and json config file below:
[clinfo.txt](https://github.com/xmrig/xmrig/files/6306852/clinfo.txt)
[xmrig_error.txt](https://github.com/xmrig/xmrig/files/6306857/xmrig_error.txt)
[config_secure.txt](https://github.com/xmrig/xmrig/files/6306885/config_secure.txt)

I looked a lot about how to solve this one but no luck..
Thanks!

# Discussion History
## SChernykh | 2021-04-13T22:15:04+00:00
Because GPU with 1 GB memory can't allocate 2.8 GB buffer.

## KMKAR | 2021-04-13T22:33:53+00:00
Hi @SChernykh
Yes, I assumed that. But how can I edit (if possible) the buffer? I couldn't find that anywhere.
Thanks

## SChernykh | 2021-04-13T22:36:23+00:00
I assume this is KawPow DAG and you can't edit it. The size of DAG is defined in the algorithm itself.

## KMKAR | 2021-04-13T22:45:15+00:00
You're right. I'm trying to use kawpow and the current DAG size is 2,8 gb. Thanks for the answers and input.

# Action History
- Created by: KMKAR | 2021-04-13T21:45:02+00:00
- Closed at: 2021-04-13T22:45:15+00:00
