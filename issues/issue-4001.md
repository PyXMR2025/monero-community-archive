---
title: variant 2
source_url: https://github.com/monero-project/monero/issues/4001
author: KlausT
assignees: []
labels:
- invalid
created_at: '2018-06-14T23:02:07+00:00'
updated_at: '2018-08-28T20:56:54+00:00'
type: issue
status: closed
closed_at: '2018-08-28T20:56:54+00:00'
---

# Original Description
Take a look at this code from Stellite:
https://github.com/stellitecoin/Stellite/blob/894ba4036069682d190f2282c2df08fd45177f9d/src/crypto/slow-hash.c#L56
I guess when Monero will be using variant 2 then it will not be the same as Stellite variant 2, right?

# Discussion History
## moneromooo-monero | 2018-06-15T07:53:49+00:00
No, it won't.

## moneromooo-monero | 2018-06-15T08:10:11+00:00
It will very likely be based upon https://github.com/SChernykh/xmr-stak-cpu/commit/9169ef624250e8ab73ec362d7905abcb00ba91a4

Then a couple other small tweaks will be made closer to release to keep the "ASIC design" period short.


## moneromooo-monero | 2018-08-28T20:43:44+00:00
See #4218 

Not a bug, closing.

+invalid


# Action History
- Created by: KlausT | 2018-06-14T23:02:07+00:00
- Closed at: 2018-08-28T20:56:54+00:00
