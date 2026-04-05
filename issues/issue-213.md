---
title: Failed to verify input FCMP++ signatures for tx
source_url: https://github.com/seraphis-migration/monero/issues/213
author: nahuhh
assignees: []
labels: []
created_at: '2025-11-02T17:31:58+00:00'
updated_at: '2025-12-09T18:06:24+00:00'
type: issue
status: closed
closed_at: '2025-12-09T18:06:24+00:00'
---

# Original Description
this spams for a while
```
2025-11-02 17:25:10.252 D Considering <dfe2da26b141ec06d10e77dd9a6592425c5a1672ad7f8f5a6638cfa260b10e67>, weight 11904, current block weight 0/1912936, current coinbase 0.600000000000, relay method 4                                                                                                                                                                         
2025-11-02 17:25:10.258 D No previously valid verID provided for tx <dfe2da26b141ec06d10e77dd9a6592425c5a1672ad7f8f5a6638cfa260b10e67>, continuing to input verification as normal...
2025-11-02 17:25:10.316 E Failed to verify input FCMP++ signatures for tx <dfe2da26b141ec06d10e77dd9a6592425c5a1672ad7f8f5a6638cfa260b10e67>                                            
2025-11-02 17:25:10.316 D   not ready to go                                                                                                                                             
2025-11-02 17:25:10.316 D Considering <c326d080460149dbc608d113677a8ee45780a791883b05933201a197b8a373ea>, weight 17507, current block weight 0/1912936, current coinbase 0.600000000000, relay method 4                                                                                                                                                                         
2025-11-02 17:25:10.320 D No previously valid verID provided for tx <c326d080460149dbc608d113677a8ee45780a791883b05933201a197b8a373ea>, continuing to input verification as normal...
2025-11-02 17:25:10.375 E Failed to verify input FCMP++ signatures for tx <c326d080460149dbc608d113677a8ee45780a791883b05933201a197b8a373ea>
2025-11-02 17:25:10.375 D   not ready to go
```

disclaimer:
- I'm running various PRs on top of the latest branch: 209, 208, 207, 198, 195, 184
- I'm only seeing this on 1 node. I have 3 nodes running these PRs.
- I'm not submitting txs directly to this node, just p2p traffic.


# Discussion History
## j-berman | 2025-11-03T02:15:13+00:00
Possibly a tx that was deep reorged out that can no longer be valid?

## j-berman | 2025-11-03T02:19:14+00:00
Or a tx that made it into your pool before a deep reorg that then rendered the tx invalid

## j-berman | 2025-12-09T18:06:24+00:00
Closing since this is an expected error message during normal operation. Perhaps the message could be downgraded from an error message and/or again... logic improved when dealing with txs rendered invalid by a reorg.

# Action History
- Created by: nahuhh | 2025-11-02T17:31:58+00:00
- Closed at: 2025-12-09T18:06:24+00:00
