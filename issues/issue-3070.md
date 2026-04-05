---
title: Miner software upgrade or not for Monero v15
source_url: https://github.com/xmrig/xmrig/issues/3070
author: Lonnegan
assignees: []
labels:
- question
created_at: '2022-06-14T22:17:25+00:00'
updated_at: '2025-06-16T19:25:35+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:25:35+00:00'
---

# Original Description
Hi,

I've just seen that you did updates to @xmrig due to the network upgrade to Monero v15
https://github.com/xmrig/xmrig/pull/3067
https://github.com/xmrig/xmrig/pull/3067/commits/45061f40d807d6ac7ff065eba468c7bb0dbb6e7e

The official Monero FAQ instead says:

> Q: Will there be any changes to the PoW algorithm?
> A: No. The PoW algorithm will not be affected. **Mining will work as before and miners won't need to update their software**.

So just to be sure, since I have a couple of Monero mining systems out there: will I have to update those all before 16th of July or not?

# Discussion History
## xmrig | 2022-06-14T22:24:41+00:00
This change is about daemon (solo) mine due changes on protocol level and not PoW, regular pool mining is not affected.
Thank you.

# Action History
- Created by: Lonnegan | 2022-06-14T22:17:25+00:00
- Closed at: 2025-06-16T19:25:35+00:00
