---
title: tx template fee sorting appears reversed
source_url: https://github.com/monero-project/monero/issues/1630
author: iamsmooth
assignees: []
labels: []
created_at: '2017-01-25T09:04:37+00:00'
updated_at: '2017-07-20T01:02:19+00:00'
type: issue
status: closed
closed_at: '2017-07-20T01:02:19+00:00'
---

# Original Description
https://github.com/monero-project/monero/blob/master/src/cryptonote_core/tx_pool.cpp#L256
https://github.com/monero-project/monero/blob/master/src/cryptonote_core/tx_pool.h#L65

^ Looking at this code it appears to me that transactions with the higher number of bytes per fee paid (i.e. lower fee per byte) would be sorted before (and added to the template before) those with lower bytes per fee.

I see several blocks mined which appear to confirm this behavior:

https://xmrchain.net/block/1231370
https://xmrchain.net/block/1231373

Suggested fix: either invert the current bytes/fee calculation or reverse the sort order for the std::set

# Discussion History
## iamsmooth | 2017-01-25T09:24:36+00:00
There's a fix over here: https://github.com/xnbya/monero/commit/56499f57a6f3cd65f66c33f976b4512388ba83ad

## iamsmooth | 2017-01-25T22:50:20+00:00
#1631 

## iamsmooth | 2017-07-20T01:02:19+00:00
has been fixed

# Action History
- Created by: iamsmooth | 2017-01-25T09:04:37+00:00
- Closed at: 2017-07-20T01:02:19+00:00
