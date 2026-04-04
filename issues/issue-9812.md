---
title: Wrong block blob
source_url: https://github.com/monero-project/monero/issues/9812
author: batterhour
assignees: []
labels:
- invalid
created_at: '2025-02-22T18:33:59+00:00'
updated_at: '2025-02-22T18:42:30+00:00'
type: issue
status: closed
closed_at: '2025-02-22T18:42:18+00:00'
---

# Original Description
I forked Monero and customized it for my needs. I came up with a name for the new coin, generated unique address prefixes, and created the genesis block. After that, I launched three nodes on different servers and set up P2Pool on each of them. At first glance, everything seemed to work fine, but as soon as I started mining, problems arose.

The miner submits thousands of shares per second, but in the logs of P2Pool and the nodes, I found errors related to the blob (block). Here’s what the logs show:

Node logs:
`2025-02-22 16:24:57.799 E Failed to parse block from blob`

P2Pool logs:
`2025-02-22 16:24:46.5915 P2Pool submit_block: height = 1, template id = 1, nonce = 65536, extra_nonce = 947920331, mm_root = c263c283c740204a4ad22ed10d7117e9384792770b09b3c8ea88c616ef181d55
2025-02-22 16:24:46.5917 P2Pool submit_block: height = 1, template id = 1, nonce = 229376, extra_nonce = 947920331, mm_root = c263c283c740204a4ad22ed10d7117e9384792770b09b3c8ea88c616ef181d55
2025-02-22 16:24:46.5925 P2Pool submit_block: daemon returned error: 'Wrong block blob', template id = 1, nonce = 65536, extra_nonce = 947920331, mm_root = c263c283c740204a4ad22ed10d7117e9384792770b09b3c8ea88c616ef181d55
2025-02-22 16:24:46.5925 P2Pool submit_block: daemon returned error: 'Wrong block blob', template id = 1, nonce = 229376, extra_nonce = 947920331, mm_root = c263c283c740204a4ad22ed10d7117e9384792770b09b3c8ea88c616ef181d55`

I have no idea what the system doesn’t like, and I’d like to ask for help from the community. Why is there a blob error? Could I have missed something during the setup or genesis block generation? I’d appreciate any advice or suggestions!


# Discussion History
## selsta | 2025-02-22T18:42:18+00:00
I would recommend to try mining without P2Pool first to narrow down the issue.

Either way, this is the wrong place to ask about forking monero so I'm closing this.

# Action History
- Created by: batterhour | 2025-02-22T18:33:59+00:00
- Closed at: 2025-02-22T18:42:18+00:00
