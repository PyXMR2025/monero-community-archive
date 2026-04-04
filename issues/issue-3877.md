---
title: Wallet 1GB file size limit problem.
source_url: https://github.com/monero-project/monero/issues/3877
author: miningpoolhub
assignees: []
labels: []
created_at: '2018-05-28T12:40:49+00:00'
updated_at: '2018-05-28T16:26:34+00:00'
type: issue
status: closed
closed_at: '2018-05-28T16:26:34+00:00'
---

# Original Description
This code blocks wallet file loading when file is bigger than 1GB
https://github.com/monero-project/monero/blob/master/contrib/epee/include/file_io_utils.h#L162

I can't launch wallet-rpc program as it exceeded 1GB already.
I just changed this numbers, compiled and working well but worried a bit with this issue.

Any idea for improving this part?
Maybe not using simple file read operation in one large buffer, but use file mapping would be better.

I think pool, exchange service will reach 1GB sooner or later.

# Discussion History
## moneromooo-monero | 2018-05-28T13:33:23+00:00
AFAIK this is safe, at least two others have done this, and no reports of anything falling over :)

In the future, the wallet cache will be a LMDB database, so this will be mooted.

## moneromooo-monero | 2018-05-28T13:45:12+00:00
I'll fix this for now just for wallet caches.

## moneromooo-monero | 2018-05-28T13:59:27+00:00
https://github.com/monero-project/monero/pull/3878 should do it (still building).

## miningpoolhub | 2018-05-28T16:26:34+00:00
Great!

# Action History
- Created by: miningpoolhub | 2018-05-28T12:40:49+00:00
- Closed at: 2018-05-28T16:26:34+00:00
