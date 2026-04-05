---
title: 'Is it possible access Mac2020/Intel GPU '
source_url: https://github.com/xmrig/xmrig/issues/2611
author: FINDKEEF
assignees: []
labels: []
created_at: '2021-10-01T01:06:33+00:00'
updated_at: '2021-10-02T04:47:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi I'm using a imac 2020 (the last intel model) .
My Ram 128GB
AMD Radeon Pro 5700XT 16GB.

Looking for a way to use my gpu for mining..

Any Advise would be Appreciated!!
Thanks

# Discussion History
## Spudz76 | 2021-10-01T19:22:16+00:00
Submitted my fixes branch for inclusion, you could build from that set of patches and it should almost "just work".

Definitely won't work without the patches, when xmrig sees "AMD" anywhere in the board name, it assumes it's a full AMDGPU-Pro OpenCL stack with all the extensions (not stripped generic standard only Apple OpenCL 1.2 with an AMD card behind it).  And then some other issues with code syntax the Apple OpenCL runtime compiler didn't like.

The CPU should already "just work" similar to a Win/Lin PC, from Terminal shell (there is no GUI).

## FINDKEEF | 2021-10-02T04:47:23+00:00
thanks


# Action History
- Created by: FINDKEEF | 2021-10-01T01:06:33+00:00
