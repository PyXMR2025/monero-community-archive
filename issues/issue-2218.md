---
title: gcc win32-64 speeds
source_url: https://github.com/xmrig/xmrig/issues/2218
author: jvds123
assignees: []
labels:
- question
created_at: '2021-03-29T07:53:58+00:00'
updated_at: '2021-04-12T13:40:08+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:40:08+00:00'
---

# Original Description
got the xmrig (gcc ) installed on 3 pc, 2 are 64bits, and one 32bits, all 3 have intel q6600 processor, and ram are 8 and 4 gb for the 64bits ones and 3gb for the 32bits, the 64bits run 6 times faster at 750~780 hs, vs 120~130 hs on the 32 bits, is that normal? 


# Discussion History
## SChernykh | 2021-03-29T08:42:04+00:00
Yes, it is expected. 32-bit version is very slow on all algorithms because they were all created for 64-bit CPUs.

## snipeTR | 2021-03-29T09:39:10+00:00
is there any way to optimize it?

## Lonnegan | 2021-03-29T09:59:18+00:00
In addition, please check whether the miner is running in fast mode at all. The miner uses 2 GB of RAM for this purpose. Since the system only has a total of 3 GB RAM (and 32 bit Win can't address more also), it may be running in slow light mode with reduced RAM consumption.

## Spudz76 | 2021-03-29T20:44:04+00:00
Much of the crypto is based on using 64-bit natively, so to process with a 32-bit miner many operations have to be done twice and eat many transfer cycles and cause worse effective bandwidth to memory and cache.  Also pieces that are 32-bit usually have two pieces of data combined into a 64-bit and then operated on quickly (using alignment being sequential to an advantage).

The algorithms need to be able to "see" and process data with 64bits, no way around that, and 32-bit is of course always slower at 64-bit math.  There are 64-bit opcodes that do things at least twice a fast when available.  Some CPU features may not be available in 32-bit mode.  Does the 32-bit one still show AES support and etc?

# Action History
- Created by: jvds123 | 2021-03-29T07:53:58+00:00
- Closed at: 2021-04-12T13:40:08+00:00
