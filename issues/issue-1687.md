---
title: Argon2 when mining RandomX
source_url: https://github.com/xmrig/xmrig/issues/1687
author: Lonnegan
assignees: []
labels:
- question
created_at: '2020-05-24T00:00:36+00:00'
updated_at: '2020-08-19T01:17:46+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:17:46+00:00'
---

# Original Description
Hi,

when I start xmrig 5.11.2 for mining RandomX, it shows "use argon2 implementation AVX2". In 5.11.1 this imho senseless message isn't shown. I'm not mining Argon2 (Turtlecoin), but Monero (RandomX)
![xmrig_bug_argon2_rx](https://user-images.githubusercontent.com/60088495/82742764-59f7f680-9d62-11ea-86ff-aee20a00b3e0.png)


# Discussion History
## xmrig | 2020-05-24T03:35:23+00:00
It's OK, argon2 used in RandomX dataset initialization and AVX* make it about 300 ms or so faster, now dedicated argon2 implementation used for mining and part of RandomX is unified, so old option [argon2-impl](https://github.com/xmrig/xmrig/blob/master/doc/CPU.md#argon2-impl-since-v310) now works for RandomX too.
Thank you.

## Lonnegan | 2020-05-24T10:14:09+00:00
Ah, ok. thx 4 info :)

# Action History
- Created by: Lonnegan | 2020-05-24T00:00:36+00:00
- Closed at: 2020-08-19T01:17:46+00:00
