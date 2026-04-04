---
title: 'gettransactions: unconfirmed tx (in mempool) show very high block_height'
source_url: https://github.com/monero-project/monero/issues/4916
author: got3nks
assignees: []
labels:
- invalid
created_at: '2018-11-29T18:38:09+00:00'
updated_at: '2018-12-13T01:41:05+00:00'
type: issue
status: closed
closed_at: '2018-12-13T01:41:05+00:00'
---

# Original Description
When a tx is not confirmed yet and you retrieve it through the monerod's RPC `/gettransactions` call, `block_height` and `block_timestamp` are very large number.

```
      'block_height' => '18446744073709551615',
      'block_timestamp' => '18446744073709551615',
```

I wonder how they are calculated? I guess the documentation should be updated: https://www.getmonero.org/resources/developer-guides/daemon-rpc.html

# Discussion History
## hyc | 2018-11-29T18:47:48+00:00
That's MAX_ULONG. Doesn't mean anything.

## got3nks | 2018-11-29T18:51:45+00:00
I would rather expect it to be a null value for an unconfirmed tx.
Or update the documentation, I guess?

## xiphon | 2018-11-29T22:14:54+00:00
1. Check `in_pool` field first.
2. The code explicitly sets `block_height` and `block_timestamp` to `MAX_ULONG` if a tx is not mined yet (in the daemon's memory pool).

## moneromooo-monero | 2018-12-13T01:16:11+00:00
Not a bug.

+invalid

# Action History
- Created by: got3nks | 2018-11-29T18:38:09+00:00
- Closed at: 2018-12-13T01:41:05+00:00
