---
title: inconsistency in reported block height
source_url: https://github.com/monero-project/monero/issues/130
author: iamsmooth
assignees: []
labels: []
created_at: '2014-09-12T05:04:49+00:00'
updated_at: '2016-03-20T18:58:02+00:00'
type: issue
status: closed
closed_at: '2016-03-20T18:58:02+00:00'
---

# Original Description
2014-Sep-11 22:00:47.482087 [P2P8][121.40.157.40:18080 OUT]Sync data returned unknown top block: 214132 -> 214133 [1 blocks (0 days) behind] 
SYNCHRONIZATION started
2014-Sep-11 22:00:47.482393 [P2P8]Remote top block height: **214133**, id: <**7b37dc73f030b0cf9dae82162fcb41ce306d585994aba8aced6a0961b8316de8**>
2014-Sep-11 22:00:47.850375 [P2P3]+++++ BLOCK SUCCESSFULLY ADDED
id:     <**7b37dc73f030b0cf9dae82162fcb41ce306d585994aba8aced6a0961b8316de8**>
PoW:    <47b03c4f44588505660263214bc7cb308c171ca8faa04090e515fb8d02000000>
HEIGHT **214132**, difficulty:      1209222503


# Discussion History
## fluffypony | 2016-01-25T18:31:22+00:00
This is still happening, assigning to @moneromooo-monero 


## moneromooo-monero | 2016-03-20T12:37:05+00:00
https://github.com/monero-project/bitmonero/pull/737


# Action History
- Created by: iamsmooth | 2014-09-12T05:04:49+00:00
- Closed at: 2016-03-20T18:58:02+00:00
