---
title: wallet rpc outgoing transfers always return subaddress index 0
source_url: https://github.com/monero-project/monero/issues/5171
author: woodser
assignees: []
labels: []
created_at: '2019-02-20T16:44:00+00:00'
updated_at: '2019-04-01T16:09:44+00:00'
type: issue
status: closed
closed_at: '2019-04-01T16:09:44+00:00'
---

# Original Description
Querying wallet rpc `get_transfers` with a subaddress index > 0 will return outgoing transfers, presumably from that subaddress, but their subaddresses are always indicated as 0.

This issue is to return the correct subaddress index for outgoing transfers.  Given that they are returned when querying with specific subaddress indices, this should be possible.

# Discussion History
## moneromooo-monero | 2019-03-13T13:54:47+00:00
That is because a transfer can be made with many subaddress indices as inputs.
In that case, there should be a list rather than a single number.

## moneromooo-monero | 2019-03-13T14:15:37+00:00
https://github.com/monero-project/monero/pull/5282

## moneromooo-monero | 2019-03-13T14:16:26+00:00
There's also an address field. There could be an additional addresses field too to match. Not sure that's needed though, since I'm not even sure what address is doing here.

## moneromooo-monero | 2019-04-01T15:58:19+00:00
+resolved

# Action History
- Created by: woodser | 2019-02-20T16:44:00+00:00
- Closed at: 2019-04-01T16:09:44+00:00
