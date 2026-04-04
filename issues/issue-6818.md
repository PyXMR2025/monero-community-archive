---
title: Rpc client id wrong syntax
source_url: https://github.com/monero-project/monero/issues/6818
author: Elektro8
assignees: []
labels: []
created_at: '2020-09-14T19:27:04+00:00'
updated_at: '2020-09-16T15:07:05+00:00'
type: issue
status: closed
closed_at: '2020-09-16T15:07:05+00:00'
---

# Original Description
In wallet-cli  in help set it is listed that to keep using the same client id for rpc payments " set persistent-client-id 1" must be used.
But that is not working, because it's actually  "set persistent-rpc-client-id 1".

# Discussion History
## moneromooo-monero | 2020-09-14T20:51:49+00:00
Thanks, https://github.com/monero-project/monero/pull/6819

# Action History
- Created by: Elektro8 | 2020-09-14T19:27:04+00:00
- Closed at: 2020-09-16T15:07:05+00:00
