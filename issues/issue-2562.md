---
title: 'Improvement: astrobwt speedup'
source_url: https://github.com/xmrig/xmrig/issues/2562
author: 8lecramm
assignees: []
labels: []
created_at: '2021-08-26T18:16:37+00:00'
updated_at: '2021-08-29T08:36:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,
the astrobwt algorithm uses a salsa20 implementation by ZeroTier.
"libsodium" offers a faster salsa20 implementation.
I did some tests and hashrate increases by 2.5% on all machines.

Setup:
OS: Linux (Ubuntu, Debian)
Processors: Intel Core i5 7th Gen, Core i5 8th Gen, Xeon E3-1241

# Discussion History
## SChernykh | 2021-08-29T08:36:38+00:00
#2565 

# Action History
- Created by: 8lecramm | 2021-08-26T18:16:37+00:00
