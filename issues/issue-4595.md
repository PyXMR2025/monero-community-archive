---
title: code not used?
source_url: https://github.com/monero-project/monero/issues/4595
author: calidion
assignees: []
labels:
- invalid
created_at: '2018-10-15T09:55:31+00:00'
updated_at: '2018-10-16T18:24:58+00:00'
type: issue
status: closed
closed_at: '2018-10-16T18:24:58+00:00'
---

# Original Description
by
```
grep crypto_ops_builder -Rn .
```
gets no file using files in that directory.

It seems directory `src/crypto/crypto_ops_builder` is not used?

# Discussion History
## moneromooo-monero | 2018-10-15T11:34:23+00:00
Indeed, it is the reference code from djb.

## calidion | 2018-10-15T12:05:46+00:00
what is djb?

## iDunk5400 | 2018-10-15T12:16:04+00:00
https://en.wikipedia.org/wiki/Daniel_J._Bernstein

## moneromooo-monero | 2018-10-16T18:18:44+00:00
+invalid

# Action History
- Created by: calidion | 2018-10-15T09:55:31+00:00
- Closed at: 2018-10-16T18:24:58+00:00
