---
title: Can I manually set xmrig difficulty?
source_url: https://github.com/xmrig/xmrig/issues/390
author: xberg
assignees: []
labels:
- question
created_at: '2018-02-07T13:26:37+00:00'
updated_at: '2018-03-14T22:48:06+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:48:06+00:00'
---

# Original Description
Hi,
Is it possible to change cryptonight's default difficulty? 

Mining Cryptonight algo thru xmrig at 800 H /s. Current difficulty is 200,007.
My miner is finding very few results at such difficulty. Is there no way to start at a lower difficulty?

# Discussion History
## xmrig | 2018-02-07T13:32:39+00:00
It depends of pool, you need check your pool help page. Usually it `+DIFF` or `.DIFF` added to wallet address, but not all pools support this feature.
Thank you.

## korishan | 2018-02-07T19:14:30+00:00
It can also be the pool address port can change the difficulty. Check to see which ports your pool is using. It's possible the there are different ports available.

# Action History
- Created by: xberg | 2018-02-07T13:26:37+00:00
- Closed at: 2018-03-14T22:48:06+00:00
