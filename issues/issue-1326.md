---
title: wrong binary format, packet size = 0 less than expected sizeof(storage_block_header)=9
source_url: https://github.com/monero-project/monero/issues/1326
author: medusadigital
assignees: []
labels: []
created_at: '2016-11-11T23:54:09+00:00'
updated_at: '2016-11-21T16:24:50+00:00'
type: issue
status: closed
closed_at: '2016-11-21T16:24:50+00:00'
---

# Original Description
```
2016-Nov-12 00:46:17.604288 [P2P5]ERROR C:/msys64/home/ququ/monero/contrib/epee/include/storages/portable_storage.h:153 portable_storage: wrong binary format, packet size = 0 less than expected sizeof(storage_block_header)=9
2016-Nov-12 00:46:17.604288 [P2P5]ERROR C:/msys64/home/ququ/monero/contrib/epee/include/storages/levin_abstract_invoke2.h:129 Failed to load_from_binary on command 1007

```

![wrongbinaryformat](https://cloud.githubusercontent.com/assets/17108301/20233657/30e67fe8-a872-11e6-9abf-4aeb37f6217f.png)


`Monero 'Wolfram Warptangent' (v0.10.0.0-6a2bb62)`

Setup: win7 x64 




# Discussion History
## medusadigital | 2016-11-12T00:02:22+00:00
```
-12 00:58:11.617543 [P2P6][68.52.96.191:46310 1f6e1deb-e86a-0d64-83ab-ceb4279b94e2 INC] NEW CONNECTION
2016-Nov-12 00:58:12.319544 [P2P9][155.94.209.23:18080 OUT]NOTIFY_NEW_BLOCK (hop 2)
2016-Nov-12 00:58:14.051147 [P2P5]PEER DOESN'T SUPPORT FLUFFY BLOCKS - RELAYING FULL BLOCK
2016-Nov-12 00:58:14.051147 [P2P7]connections_ size now 9
2016-Nov-12 00:58:14.051147 [P2P5][68.52.96.191:46310 INC] post N10cryptonote16NOTIFY_NEW_BLOCKE -->
2016-Nov-12 00:58:14.051147 [P2P5]PEER DOESN'T SUPPORT FLUFFY BLOCKS - RELAYING FULL BLOCK
2016-Nov-12 00:58:14.051147 [P2P5][107.170.217.146:18080 OUT] post N10cryptonote16NOTIFY_NEW_BLOCKE -->
2016-Nov-12 00:58:14.238347 [P2P9]tx <137d01fb8ffd9650f89beb530eaabec04cc355c50376c15df48706be38f34240> already have transaction in blockchain
2016-Nov-12 00:58:14.238347 [P2P7][68.52.96.191:46310 INC]COMMAND_HANDSHAKE
2016-Nov-12 00:58:14.238347 [P2P9]tx <c0c06ff77b80cbf9bbd84388ba71f2d43273db8b9cfd9b259e98704f77665741> already have transaction in blockchain
2016-Nov-12 00:58:14.238347 [P2P9]tx <45b5c18fbb6fec356d246f042e3061cda764bebd04817460734e83b90a881261> already have transaction in blockchain
2016-Nov-12 00:58:14.238347 [P2P7][155.94.209.23:18080 OUT]COMMAND_TIMED_SYNC
2016-Nov-12 00:58:14.799948 [P2P7][104.131.173.147:18080 OUT]NOTIFY_NEW_TRANSACTIONS
2016-Nov-12 00:58:14.862348 [P2P6][111.202.148.34:46875 2302fdc2-2e71-75e3-4ee2-1362f59ad597 INC] NEW CONNECTION
2016-Nov-12 00:58:14.909148 [P2P6]ERROR C:/msys64/home/ququ/monero/contrib/epee/include/storages/portable_storage.h:153 portable_storage: wrong binary format, packet size = 0 less than expected sizeof(storage_block_header)=9
2016-Nov-12 00:58:14.909148 [P2P6]ERROR C:/msys64/home/ququ/monero/contrib/epee/include/storages/levin_abstract_invoke2.h:129 Failed to load_from_binary on command 1007
2016-Nov-12 00:58:14.909148 [P2P6][68.52.96.191:46310 INC]COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-7, LEVIN_ERROR_FORMAT)
2016-Nov-12 00:58:15.267949 [P2P7][68.52.96.191:46310 INC]NOTIFY_REQUEST_CHAIN: m_block_ids.size()=30
2016-Nov-12 00:58:15.299149 [P2P7][68.52.96.191:46310 INC]-->>NOTIFY_RESPONSE_CHAIN_ENTRY: m_start_height=532662, m_total_height=1177692, m_block_ids.size()=10000
2016-Nov-12 00:58:15.299149 [P2P7][68.52.96.191:46310 INC] post N10cryptonote27NOTIFY_RESPONSE_CHAIN_ENTRYE -->
2016-Nov-12 00:58:15.345949 [P2P7]connections_ size now 10
2016-Nov-12 00:58:15.361549 [P2P7][111.202.148.34:46875 INC]COMMAND_HANDSHAKE
2016-Nov-12 00:58:15.642350 [P2P6]ERROR C:/msys64/home/ququ/monero/contrib/epee/include/storages/portable_storage.h:153 portable_storage: wrong binary format, packet size = 0 less than expected sizeof(storage_block_header)=9
2016-Nov-12 00:58:15.642350 [P2P6]ERROR C:/msys64/home/ququ/monero/contrib/epee/include/storages/levin_abstract_invoke2.h:129 Failed to load_from_binary on command 1007
2016-Nov-12 00:58:15.642350 [P2P6][111.202.148.34:46875 INC]COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-7, LEVIN_ERROR_FORMAT)
2016-Nov-12 00:58:16.063550 [P2P6][0.0.0.0:0 OUT]back ping connect failed to 68.52.96.191:18080
2016-Nov-12 00:58:16.125951 [P2P8][0.0.0.0:0 OUT]Connect failed to 93.126.127.160:18080
2016-Nov-12 00:58:16.125951 [P2P8]Selected peer: 13713611575471650532 106.69.214.120:18080[white=0] last_seen: d0.h0.m49.s38
2016-Nov-12 00:58:16.125951 [P2P8]Connecting to 106.69.214.120:18080(white=0, last_seen: d0.h0.m49.s38)...
2016-Nov-12 00:58:16.125951 [P2P8]connections_ size now 11
2016-Nov-12 00:58:16.235151 [P2P7][68.52.96.191:46310 INC]NOTIFY_REQUEST_GET_OBJECTS
```


## voidzero | 2016-11-12T08:50:55+00:00
Getting this too on Gentoo GNU/Linux amd64.


## ghost | 2016-11-12T09:17:45+00:00
Me too


## moneromooo-monero | 2016-11-12T10:19:45+00:00
https://github.com/monero-project/monero/pull/1329


## iDunk5400 | 2016-11-12T11:49:11+00:00
#1329 fixes the issue.


## ghost | 2016-11-14T16:01:18+00:00
Hi @medusadigital, if #1329 has fixed the issue for you, would you mind closing the issue or reporting back if not?


## medusadigital | 2016-11-21T16:24:50+00:00
hei sorry, guys, reading email is not my strength. 

fixed --> closed

# Action History
- Created by: medusadigital | 2016-11-11T23:54:09+00:00
- Closed at: 2016-11-21T16:24:50+00:00
