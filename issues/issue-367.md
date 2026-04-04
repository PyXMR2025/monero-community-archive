---
title: New unconfirmed sent transactions listed at bottom of History
source_url: https://github.com/monero-project/monero-gui/issues/367
author: bigreddmachine
assignees: []
labels: []
created_at: '2016-12-28T04:21:34+00:00'
updated_at: '2017-01-06T02:29:34+00:00'
type: issue
status: closed
closed_at: '2017-01-06T02:29:34+00:00'
---

# Original Description
When a new transaction is sent from the wallet, before it is accepted into a block, it is listed at the bottom of the chart. Presumably this is because it is listed as in "block 0". Once confirmed, it moved up to the top, which makes sense. I think it should be at the top from the start, and say "block n/a" rather than "0".

# Discussion History
## ghost | 2016-12-28T17:29:49+00:00
Great idea

## palexande | 2016-12-31T11:42:06+00:00
Agree, new transactions need to be at the top whether sending or receiving.

## Jaqueeee | 2016-12-31T13:59:36+00:00
fixed in #376 
unconfirmed shows as Block height: Pending

## bigreddmachine | 2017-01-06T02:29:34+00:00
Good work!

# Action History
- Created by: bigreddmachine | 2016-12-28T04:21:34+00:00
- Closed at: 2017-01-06T02:29:34+00:00
