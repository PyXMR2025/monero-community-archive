---
title: Failed to compile on ppc64le
source_url: https://github.com/xmrig/xmrig/issues/143
author: '0x006E'
assignees: []
labels: []
created_at: '2017-10-08T16:19:50+00:00'
updated_at: '2017-10-25T14:55:21+00:00'
type: issue
status: closed
closed_at: '2017-10-25T14:55:21+00:00'
---

# Original Description
I am using OpenPower PC's for mining. But I can't get xmrig to compile on it. It just says there is some error on sysinfos.c
impossible register constraint in 'asm'. Please help me compile. To reproduce the error compile on ppc64le. 


# Discussion History
## xmrig | 2017-10-08T16:42:39+00:00
Only x86(64) architectures supported.
Thank you.

## 0x006E | 2017-10-09T13:45:49+00:00
Is there anyway to port this on ppc64le. I searched for cpuid opcode on ppc64le platform but found nothing on it. 

## atarate | 2017-10-09T14:01:42+00:00
Intrinsics of the code are X86 and AES-NI Specific. You will have to rewrite the code as such mate.

# Action History
- Created by: 0x006E | 2017-10-08T16:19:50+00:00
- Closed at: 2017-10-25T14:55:21+00:00
