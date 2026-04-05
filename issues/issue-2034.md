---
title: How can I play xmrig processing on AMD's dedicated GPU?
source_url: https://github.com/xmrig/xmrig/issues/2034
author: wallisonfgt
assignees: []
labels: []
created_at: '2021-01-11T17:06:44+00:00'
updated_at: '2021-04-12T14:24:27+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:24:27+00:00'
---

# Original Description
How can I play xmrig processing on AMD's dedicated GPU?

Processing is only recognized on my integrated GPU, my dedicated GPU is an AMD Radeon R8 M445DX.

Thank you!

# Discussion History
## Spudz76 | 2021-01-13T20:30:58+00:00
If it supports OpenCL and all the stuff is installed, it should work.
Linux, or Windows?  On Linux you'd install AMDGPU-Pro but it might not support OpenCL on some embedded graphics.  On Windows, I know nothing.

## ghost | 2021-02-08T09:26:47+00:00
On Windows should be enought enable OpenCL flag (or use --opencl if you run from cmd)

# Action History
- Created by: wallisonfgt | 2021-01-11T17:06:44+00:00
- Closed at: 2021-04-12T14:24:27+00:00
