---
title: Archlinuxarm SYNCHRONIZATION issue
source_url: https://github.com/monero-project/monero/issues/330
author: ghost
assignees: []
labels: []
created_at: '2015-06-24T15:37:55+00:00'
updated_at: '2016-12-15T18:11:08+00:00'
type: issue
status: closed
closed_at: '2016-12-15T18:11:08+00:00'
---

# Original Description
I have built monero using the following code

```
pacman -S git boost doxygen db libevent gtest unbound miniupnpc 
git clone https://github.com/monero-project/bitmonero.git
cd bitmonero
nano Makefile
'
in the “release-all” section add this code: -D NO_AES=ON
'
make release-all
#cd build/release/bin
strip ~/tmp/bitmonero/build/release/bin/./bitmonerod 
```

but the daemon will not sync past block 345 ?

```
SYNCHRONIZATION started
2015-Jun-24 17:35:59.730853 [P2P5][198.27.64.122:18080 OUT]Got NEW BLOCKS inside of handle_response_get_objects: size: 200
2015-Jun-24 17:36:00.343320 [P2P9][62.210.245.87:18082 OUT]Sync data returned unknown top block: 345 -> 622159 [621814 blocks (431 days) behind] 
SYNCHRONIZATION started
2015-Jun-24 17:36:00.530173 [P2P2][62.210.245.83:18083 OUT]Got NEW BLOCKS inside of handle_response_get_objects: size: 200
2015-Jun-24 17:36:01.357110 [P2P6][121.42.26.133:18080 OUT]-->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=200, txs.size()=0requested blocks count=200 / 200
2015-Jun-24 17:36:04.129319 [P2P5][121.42.26.133:18080 OUT]Got NEW BLOCKS inside of handle_response_get_objects: size: 200
2015-Jun-24 17:36:04.571033 [P2P4][62.210.245.87:18082 OUT]-->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=200, txs.size()=0requested blocks count=200 / 200
2015-Jun-24 17:36:04.693876 [P2P2][75.49.210.245:18080 OUT]Sync data returned unknown top block: 345 -> 622159 [621814 blocks (431 days) behind] 
SYNCHRONIZATION started
2015-Jun-24 17:36:05.368759 [P2P7][198.27.64.122:18080 OUT]Sync data returned unknown top block: 345 -> 622159 [621814 blocks (431 days) behind] 
SYNCHRONIZATION started
2015-Jun-24 17:36:05.469479 [P2P9][62.210.245.87:18082 OUT]Got NEW BLOCKS inside of handle_response_get_objects: size: 200
2015-Jun-24 17:36:05.677069 [P2P4][62.210.245.83:18083 OUT]Sync data returned unknown top block: 345 -> 622159 [621814 blocks (431 days) behind] 
SYNCHRONIZATION started
2015-Jun-24 17:36:06.282644 [P2P5][188.134.79.203:18080 OUT]Sync data returned unknown top block: 345 -> 622159 [621814 blocks (431 days) behind] 
SYNCHRONIZATION started
2015-Jun-24 17:36:06.981137 [P2P8][178.137.1.9:18080 OUT]Sync data returned unknown top block: 345 -> 622159 [621814 blocks (431 days) behind] 
SYNCHRONIZATION started
```

What have I missed?


# Discussion History
## moneromooo-monero | 2016-03-20T12:38:27+00:00
Run with --set-log 1 and see if you get more info about why it's not syncing.


## ghost | 2016-09-17T21:24:06+00:00
Hi @iPerky, is this still an issue for you or can it be closed?


## luigi1111 | 2016-12-15T18:11:08+00:00
@iPerky Please reopen with more details if this still exists.

# Action History
- Created by: ghost | 2015-06-24T15:37:55+00:00
- Closed at: 2016-12-15T18:11:08+00:00
