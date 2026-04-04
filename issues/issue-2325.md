---
title: '[Idea] Flush stale tx from the mempool if any of its key images have been
  flagged as spent'
source_url: https://github.com/monero-project/monero/issues/2325
author: stoffu
assignees: []
labels: []
created_at: '2017-08-22T09:19:45+00:00'
updated_at: '2017-09-23T09:29:56+00:00'
type: issue
status: closed
closed_at: '2017-09-23T09:29:56+00:00'
---

# Original Description
A situation might occur where a user first sends a transaction with the lowest fee and then decides to re-send the same transaction with a higher fee (because the prior tx didn't get confirmed quickly). If the latter tx gets confirmed, the former tx will continue to exist in the mempool until it expires after 24hrs.

Perhaps it's a good idea to make the daemon automatically drop such txes to reduce the cost of relaying etc?

# Discussion History
## moneromooo-monero | 2017-08-22T09:31:53+00:00
It's not clear to me whether that would facilitate double spending attacks.

## ghost | 2017-09-03T23:39:21+00:00
@stoffu @moneromooo-monero it would prevent some mempool flooding attacks though

## moneromooo-monero | 2017-09-23T08:42:17+00:00
https://github.com/monero-project/monero/pull/2509

## stoffu | 2017-09-23T09:29:56+00:00
Thank you, @moneromooo-monero!

# Action History
- Created by: stoffu | 2017-08-22T09:19:45+00:00
- Closed at: 2017-09-23T09:29:56+00:00
