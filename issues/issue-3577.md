---
title: Transaction was rejected by daemon
source_url: https://github.com/monero-project/monero/issues/3577
author: got3nks
assignees: []
labels: []
created_at: '2018-04-07T11:07:00+00:00'
updated_at: '2018-04-07T11:18:43+00:00'
type: issue
status: closed
closed_at: '2018-04-07T11:18:43+00:00'
---

# Original Description
Since we upgraded our client to v0.12.0.0 and the hardfork activated, we are unable to send transactions:

`transaction was rejected by daemon`

Any idea on how to fix this?

# Discussion History
## fluffypony | 2018-04-07T11:08:32+00:00
The daemon will give you the actual reason. Could be that the ring size (mixin) is too low, or you’re using a pre-0.12 wallet?

## got3nks | 2018-04-07T11:09:45+00:00
The daemon log shows `tx verification failed: ring size too small, invalid input`

We are using "mixin" => 0 in RPC requests, which used to work fine until now.

After replacing mixin = 0 with mixin = 6, now it is fixed.

# Action History
- Created by: got3nks | 2018-04-07T11:07:00+00:00
- Closed at: 2018-04-07T11:18:43+00:00
