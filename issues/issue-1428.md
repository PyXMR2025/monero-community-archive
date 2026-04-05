---
title: error 1061 and error 1072
source_url: https://github.com/xmrig/xmrig/issues/1428
author: EicHub
assignees: []
labels:
- duplicate
created_at: '2019-12-16T01:15:22+00:00'
updated_at: '2019-12-18T02:54:58+00:00'
type: issue
status: closed
closed_at: '2019-12-18T02:54:58+00:00'
---

# Original Description
[2019-12-16 09:06:08.131]  msr  failed to stop WinRing0 driver, error 1061
[2019-12-16 09:06:08.131]  msr  failed to remove WinRing0 driver, error 1072

-----

Windows 2016 and Windows 2019,EPYC 7451 and EPYC 7601,admin privileges


# Discussion History
## EicHub | 2019-12-16T05:21:35+00:00
Find the cause of the problem
I used the process tracking query to find that ZenStatesAll uses WinRing0x64.sys, but when I close the Zenstates program, xmrig still reports 1061 and 1072;
ZenStatesAll, which is a tool to overclock the epyc processor.


## xmrig | 2019-12-16T06:37:53+00:00
Duplicate #1423 can you check dev branch?
Thank you.

## EicHub | 2019-12-18T02:54:52+00:00
It has worked for me. https://github.com/xmrig/xmrig/issues/1425#issuecomment-566664690
Use dev and "wrmsr": ["0xc0011020:0x0", "0xc0011021:0x60", "0xc0011022:0x510000","0xc001102b:0x1808cc16"]
It not only solves the 1061 1072 problem, but also resolves the xmrig crash of the EPYC ES CPU.


# Action History
- Created by: EicHub | 2019-12-16T01:15:22+00:00
- Closed at: 2019-12-18T02:54:58+00:00
