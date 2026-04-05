---
title: Ghostrider ignores Environmnent Variables in config.json
source_url: https://github.com/xmrig/xmrig/issues/2771
author: becgm
assignees: []
labels:
- bug
created_at: '2021-12-02T02:16:49+00:00'
updated_at: '2021-12-19T15:04:56+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:04:56+00:00'
---

# Original Description
When ghostrider algorithm is used the enviroment variables in config.json are not expanded.

When running randomx the correct worker ID is showed at pool's interface but when running ghostrider the worker is showed as ${HOSTNAME}.

The worker ID is configured at user's variable:
     "user": "XxXxXxXxXxXxXx.${HOSTNAME}"


# Discussion History
## Spudz76 | 2021-12-02T05:08:22+00:00
Wasn't aware that ever worked.

## Spudz76 | 2021-12-02T05:12:53+00:00
Okay, definitely works, and is wired globally in `setPool()` which is called regardless of algorithm.

## becgm | 2021-12-02T12:09:01+00:00
Pool still shows ${HOSTNAME} and it cannot be a bug at pool's interface since this string is sent by the xmrig client.


## xmrig | 2021-12-02T12:38:05+00:00
Fixed in dev branch.
Thank you.

## Spudz76 | 2021-12-02T15:41:27+00:00
Oops I forgot GR hides under the EthStratum umbrella.

# Action History
- Created by: becgm | 2021-12-02T02:16:49+00:00
- Closed at: 2021-12-19T15:04:56+00:00
