---
title: Don't corrupt database on unsafe shutdown
source_url: https://github.com/monero-project/monero/issues/7320
author: sonatagreen
assignees: []
labels: []
created_at: '2021-01-17T06:20:33+00:00'
updated_at: '2021-01-17T08:28:42+00:00'
type: issue
status: closed
closed_at: '2021-01-17T08:28:42+00:00'
---

# Original Description
It should be possible to structure writes in such a way that the data on disk is never in a state corresponding to a corrupted database.

Temporary workaround: periodically do the following:
1. (at daemon console) `save`
2. (at daemon console) `exit`
3. (at OS shell) `$ cp /path/to/lmdb/data.mdb /path/to/lmdb/data.mdb.bak`
4. re-start daemon

# Discussion History
## trasherdk | 2021-01-17T07:16:05+00:00
How about 
```bash
monerod --rpc-bind-port 18083 save     
2021-01-17 07:14:49.511 I Monero 'Oxygen Orion' (v0.17.1.9-release)
Blockchain saved
```

## selsta | 2021-01-17T08:23:17+00:00
```
--db-sync-mode safe
```

## sonatagreen | 2021-01-17T08:28:42+00:00
> ```
> --db-sync-mode safe
> ```
\>_< Thanks.

# Action History
- Created by: sonatagreen | 2021-01-17T06:20:33+00:00
- Closed at: 2021-01-17T08:28:42+00:00
