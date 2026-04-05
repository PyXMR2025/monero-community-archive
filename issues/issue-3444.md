---
title: XMRig runs AMD 9B14 CPU and an error occurs. It seems that AMD CPU is not supported
source_url: https://github.com/xmrig/xmrig/issues/3444
author: robandfender
assignees: []
labels: []
created_at: '2024-03-14T04:19:58+00:00'
updated_at: '2025-06-16T19:45:17+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:45:17+00:00'
---

# Original Description
XMRig runs AMD 9B14 CPU and an error occurs. It seems that AMD CPU is not supported.But works fine with INTEL E5 CPU.
**Configuration:**

AMD 9B14（96 core）
32*4 DDR 4800 memory

**Error message：**
FAILED TO APPLY MSR MOD,HASHRATE WILL BE LOW

CPU #210 can't bind memor
more...like this

# Discussion History
## SChernykh | 2024-03-14T07:49:38+00:00
It is supported, and it can get 90+ kh/s: https://xmrig.com/benchmark/3EpAqp
Please show a screenshot of XMRig window right after startup so that I can see all errors.

# Action History
- Created by: robandfender | 2024-03-14T04:19:58+00:00
- Closed at: 2025-06-16T19:45:17+00:00
