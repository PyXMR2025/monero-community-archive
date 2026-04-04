---
title: Transfer back to same wallet shows up only in outgoing transfers
source_url: https://github.com/monero-project/monero/issues/6909
author: emesik
assignees: []
labels: []
created_at: '2020-10-18T12:16:10+00:00'
updated_at: '2022-02-19T01:07:49+00:00'
type: issue
status: closed
closed_at: '2022-02-19T01:07:49+00:00'
---

# Original Description
- net: `stagenet`
- address: `56eDKfprZtQGfB4y6gVLZx5naKVHw6KEKLDoq2WWtLng9ANuBvsw67wfqyhQECoLmjQN4cKAdvMp2WsC5fnw9seKLcCSfjj`
- secret spend key: `fee3132a9b6744c3b5e724477ffc75ea61baeb81da443ba41095fe460cb64007`

I sent a transfer of 1.0 XMR to `79QBvrVQGvYdaQauHUBBdxJqGapkMzoQJP31sLXmMYZuHjTJFEariB9gQ2dgYvVtfK8FdJ7covNFJNjSx9PDMPQNFUpBeVU` which is subaddress (0,263).

It created tx `1a75f3aa57f7912313e90ab1188b7a102dbb619a324c3db51bb856a2f40503f1` which has been mined in block 689015.

Now, in the wallet I'd expect the tx to show up both in incoming and outgoing transfers, however it shows up only among outgoing:

```
[wallet 56eDKf]: show_transfers
(...)
  602561     in unlocked       2020-06-15 12:16:13       0.180000000000 645cf24e3b07b16b2e35b8d6ff6219d3231ae9bdb4d973697d8ba731f67ff259 0000000000000000 0.000000000000 76Suu6:0.180000000000 6 - 
  689015    out        -       2020-10-18 11:18:31       0.000000000000 1a75f3aa57f7912313e90ab1188b7a102dbb619a324c3db51bb856a2f40503f1 0000000000000000 0.000094240000 79QBvrVQGvYdaQauHUBBdxJqGapkMzoQJP31sLXmMYZuHjTJFEariB9gQ2dgYvVtfK8FdJ7covNFJNjSx9PDMPQNFUpBeVU:1.000000000000 145 - 
```

Similar result occurs in RPC, the transfer is visible only as outgoing when querying by `get_transfers`.

The expected behavior would be to see the transfer both as outgoing and incoming.

# Discussion History
## moneromooo-monero | 2020-10-18T15:52:28+00:00
By design. If the design is to change, people who want the change should make a well tested patch. Such a patch has potential for confusing existing accounting code.

# Action History
- Created by: emesik | 2020-10-18T12:16:10+00:00
- Closed at: 2022-02-19T01:07:49+00:00
