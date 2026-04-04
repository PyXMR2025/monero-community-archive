---
title: 'Incorrect warning when blockchain on LUKS encrypted SSD volume => "W The blockchain
  is on a rotating drive: this will be very slow, use an SSD if possible"'
source_url: https://github.com/monero-project/monero/issues/7865
author: xanoni
assignees: []
labels: []
created_at: '2021-08-16T05:16:29+00:00'
updated_at: '2021-08-16T08:15:17+00:00'
type: issue
status: closed
closed_at: '2021-08-16T08:15:16+00:00'
---

# Original Description
`monerod` shows the message `W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible` when the blockchain is indeed stored on a LUKS-encrypted SSD volume, which uses more CPU but still has great random read/write performance.

# Discussion History
## selsta | 2021-08-16T05:20:10+00:00
It's what the OS returns. Not much we can do here.

https://github.com/monero-project/monero/blob/89664fcee58688b7e439fb8fcdce0c3792195dd3/src/common/util.cpp#L813

## xanoni | 2021-08-16T08:15:16+00:00
K. Well. Guess I can live with it. 

# Action History
- Created by: xanoni | 2021-08-16T05:16:29+00:00
- Closed at: 2021-08-16T08:15:16+00:00
