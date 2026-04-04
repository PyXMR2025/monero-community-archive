---
title: Can wallet-rpc serve multiple requests in parallel
source_url: https://github.com/monero-project/monero/issues/5077
author: kim0
assignees: []
labels:
- invalid
created_at: '2019-01-17T00:57:35+00:00'
updated_at: '2019-05-01T08:09:10+00:00'
type: issue
status: closed
closed_at: '2019-01-17T01:09:06+00:00'
---

# Original Description
Say I have 10 different accounts. Is it possible to initiate 5 transfers (each between a pair of accounts) such that they are done in parallel (i.e. NOT waiting till transfer 1 is done, to start transfer 2 ...etc). Thanks


# Discussion History
## hyc | 2019-01-17T01:00:46+00:00
No.

This tracker is for actual bug reports, not usage questions. Use IRC #monero or reddit.

+invalid

## kim0 | 2019-01-17T01:04:17+00:00
well, I was building an API that interacts with wallet-rpc. The API should handle more than one request at a time. Not sure what my options are now? Thanks for helping


## webzorg | 2019-05-01T08:08:41+00:00
Pitty, I have problems with multi threaded access too, seems like wallet-rpc cannot accomodate parallel requests.

# Action History
- Created by: kim0 | 2019-01-17T00:57:35+00:00
- Closed at: 2019-01-17T01:09:06+00:00
