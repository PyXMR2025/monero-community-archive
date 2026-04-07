---
title: MSR - WinRing0x64.sys Dependencies
source_url: https://github.com/xmrig/xmrig/issues/1420
author: yesilcimenahmet
assignees: []
labels:
- question
created_at: '2019-12-15T11:43:55+00:00'
updated_at: '2019-12-15T20:39:41+00:00'
type: issue
status: closed
closed_at: '2019-12-15T20:39:41+00:00'
---

# Original Description
Hi,

I'm using a 64-bit version of XMRig compiled with GCC to avoid MSVCR dependencies. Is there any dependency of the WinRing0x64.sys file? or specific operating system version?


# Discussion History
## xmrig | 2019-12-15T11:50:32+00:00
This driver added to support write to MSR registers on Windows https://xmrig.com/docs/miner/randomx-optimization-guide/msr however miner can work without this file.
Thank you.

## SChernykh | 2019-12-15T11:53:49+00:00
We tested WinRing0x64.sys in Windows 7 (64-bit) and Windows 10 (64-bit). There are no additional dependencies.

## yesilcimenahmet | 2019-12-15T12:04:11+00:00
Thanks a lot.

I mean, if the WinRing0x64.sys file cannot be loaded due to dependencies or some other reason, will the application crash? The application should continue to run against each scenario.

## SChernykh | 2019-12-15T12:06:50+00:00
If it fails to load, MSR mod will not be applied, but XMRig will continue to run.

## yesilcimenahmet | 2019-12-15T20:39:41+00:00
Thanks.

# Action History
- Created by: yesilcimenahmet | 2019-12-15T11:43:55+00:00
- Closed at: 2019-12-15T20:39:41+00:00
