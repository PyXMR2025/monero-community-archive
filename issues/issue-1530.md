---
title: wallet rpc "not enough money" should be a different error from "not enough
  unlocked money"
source_url: https://github.com/monero-project/monero/issues/1530
author: iamsmooth
assignees: []
labels: []
created_at: '2017-01-05T20:47:06+00:00'
updated_at: '2017-11-05T23:53:55+00:00'
type: issue
status: closed
closed_at: '2017-11-05T23:53:55+00:00'
---

# Original Description
Apparently these two conditions return the same error, but they require different recovery processes from an rpc client: The former requires getting more money, and the latter only requires waiting for outputs to unlock.

# Discussion History
# Action History
- Created by: iamsmooth | 2017-01-05T20:47:06+00:00
- Closed at: 2017-11-05T23:53:55+00:00
