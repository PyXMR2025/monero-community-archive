---
title: '[SUGGESTION] Idle time percent'
source_url: https://github.com/xmrig/xmrig/issues/2465
author: XfedeX
assignees: []
labels:
- question
created_at: '2021-06-30T06:25:52+00:00'
updated_at: '2022-04-03T14:56:04+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:56:04+00:00'
---

# Original Description
**What do you mean?**
You should add a setting that sets the idle time in percent, similar to [crypto-webminer](https://www.crypto-webminer.com/integrate.html?).
E.G. : If it is set to 10 then the miner will "sleep" for 1ms and then work for 9ms.
This would allow to limit CPU usage and using all cores, thus avoiding cores overheating.

# Discussion History
## Spudz76 | 2021-06-30T18:04:11+00:00
There is a `bsleep` for the CUDA backend and I agree it would be nice to have similar in the OpenCL backend (which might as well also then be adapted into the CPU backend).  OpenCL really chokes out GUI when mining even with lowered intensities due to no "breathing room" sleep setting.  I can see how a bsleep for CPU would help in some setups.

# Action History
- Created by: XfedeX | 2021-06-30T06:25:52+00:00
- Closed at: 2022-04-03T14:56:04+00:00
