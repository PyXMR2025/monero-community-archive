---
title: FreeBSD and wrmsr
source_url: https://github.com/xmrig/xmrig/issues/2405
author: skrech
assignees: []
labels: []
created_at: '2021-05-23T06:53:51+00:00'
updated_at: '2021-05-24T02:42:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,

Today I decided to give MSR tweaks a try but it appears that they are not supported on FreeBSD.
I'm using xmrig 6.11.2 on FreeBSD 13.0 and sporting Ryzen 5600X.

I have loaded `cpuctl` kernel module needed for operating the MSR, and statring xmrig as root, but it doesn't show the expected message in the console. 

# Discussion History
## Spudz76 | 2021-05-24T02:42:33+00:00
I looked and don't see any support code for FreeBSD although it seems possible.

# Action History
- Created by: skrech | 2021-05-23T06:53:51+00:00
