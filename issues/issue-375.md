---
title: One node's pool not catching up to another
source_url: https://github.com/seraphis-migration/monero/issues/375
author: j-berman
assignees: []
labels: []
created_at: '2026-05-12T20:36:24+00:00'
updated_at: '2026-05-12T20:45:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
@Rucknium reports one node's pool isn't catching up to the other's pool size. For context, both nodes have a configured max pool size of 3gb.

Node 1:

```
print_pool_stats
50757 tx(es), 417541654 bytes total (min 7650, max 177528, avg 8226, median 7650)
fees 25.118512797000 (avg 0.000494877805 per tx, 0.000000060158 per byte)
4218 double spends, 0 not relayed, 0 failing, 47749 older than 10 minutes (oldest 2 days ago), estimated 84 block (168 minutes) backlog
   Age      Txes       Bytes
00:00:00   36185   276877342
05:59:17       0           0
11:58:35       0           0
17:57:53       0           0
23:57:11       0           0
29:56:28       0           0
35:55:46       0           0
41:55:04       0           0
47:54:22   13552   132857893
71:33:07    1020     7806419
```

Node 2:

```
print_pool_stats
99416 tx(es), 789427904 bytes total (min 7650, max 177528, avg 7940, median 7650)
fees 32.487779678000 (avg 0.000326786228 per tx, 0.000000041153 per byte)
8037 double spends, 0 not relayed, 0 failing, 95362 older than 10 minutes (oldest 2 days ago), estimated 158 block (316 minutes) backlog
   Age      Txes       Bytes
00:00:00   84976   650321943
05:56:07       0           0
11:52:14       0           0
17:48:21       0           0
23:44:28       0           0
29:40:35       0           0
35:36:42       0           0
41:32:49       0           0
47:28:56   12450   123879042
71:34:25    1990    15226919
```

Node1 log file sample: [bitmonero.log](https://github.com/user-attachments/files/27656835/bitmonero.log)

# Discussion History
## nahuhh | 2026-05-12T20:40:14+00:00
I would assume that this is from flushing the txpool (and it not refilling)

the age of tx grouping is really poorly done, but the big difference that is relevant seems to be the "older than 10mins" number. 
at first glance, it would appear that the >24hr txa are the reorged ones, but i think there are a huge chunk of the 00:00 txs that are reorg/invalid txs as well

# Action History
- Created by: j-berman | 2026-05-12T20:36:24+00:00
