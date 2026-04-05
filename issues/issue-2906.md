---
title: '32 bit version of XMrig '
source_url: https://github.com/xmrig/xmrig/issues/2906
author: hammadmallick
assignees: []
labels:
- question
- wontfix
created_at: '2022-01-27T11:46:28+00:00'
updated_at: '2025-06-16T19:25:52+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:25:52+00:00'
---

# Original Description
XMrig doesnt have a 32 bit download version but i want to know is there a way to run it on a 32bit windows. 

# Discussion History
## UnixCro | 2022-01-28T12:33:53+00:00
It is not valuable to mine with 32-bit system.  That's why XMRig doesn't offer a download.  You have to compile it yourself with cmake and make.

## deutz81 | 2023-09-21T01:11:11+00:00
[XMrig have a 32 bit version](removed)


## SChernykh | 2023-09-21T08:38:26+00:00
I don't recommend clicking on this kind of links, it's better to download directly from Github: https://github.com/xmrig/xmrig/releases/download/v5.5.0/xmrig-5.5.0-gcc-win32.zip

## Alosck | 2024-02-27T10:43:08+00:00
> It is not valuable to mine with 32-bit system.  That's why XMRig doesn't offer a download.  You have to compile it yourself with cmake and make.

How do you do this?

## xmrig | 2024-02-27T12:07:22+00:00
Technically 32 bit version still available even for latest release https://download.xmrig.com/xmrig/6.21.1/a5aa2c90425c0baaf7bfdd118bbedb13e9267c26/xmrig-6.21.1-gcc-win64.zip username: `xmrig`, password `download`, but it absolutely useless for mining with modern algorithms and maybe not working at all. Support status for 32 bit version: it compiles.
Thank you.

# Action History
- Created by: hammadmallick | 2022-01-27T11:46:28+00:00
- Closed at: 2025-06-16T19:25:52+00:00
