---
title: Failed to insert key images from txpool tx
source_url: https://github.com/monero-project/monero/issues/3778
author: joelstahre
assignees: []
labels:
- invalid
created_at: '2018-05-07T20:43:48+00:00'
updated_at: '2018-05-09T09:06:49+00:00'
type: issue
status: closed
closed_at: '2018-05-07T21:24:51+00:00'
---

# Original Description
Ubuntu 18.

can not start monerod

output:

```
./monerod
2018-05-07 20:42:36.068     7f2f0a589bc0        INFO    global  src/daemon/main.cpp:280 Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-05-07 20:42:36.068     7f2f0a589bc0        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-05-07 20:42:36.068     7f2f0a589bc0        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-05-07 20:42:36.069     7f2f0a589bc0        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-05-07 20:42:37.123     7f2f0a589bc0        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-05-07 20:42:37.124     7f2f0a589bc0        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-05-07 20:42:37.125     7f2f0a589bc0        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:18081
2018-05-07 20:42:37.125     7f2f0a589bc0        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2018-05-07 20:42:37.125     7f2f0a589bc0        INFO    global  src/daemon/core.h:86    Initializing core...
2018-05-07 20:42:37.126     7f2f0a589bc0        INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder /home/joelstahre/.bitmonero/lmdb ...
2018-05-07 20:42:38.246     7f2f0a589bc0        ERROR   txpool  src/cryptonote_core/tx_pool.cpp:398     internal error: kept_by_block=0,  kei_image_set.size()=1
txin.k_image=<6e8266eabb607c99850a283dfa0b2213273a184922a4b76b5fbde551b8d4eaa6>
tx_id=<2c85cc54304f572829a2180290337fb762b5ec4e0b5026a44a9500cce2d94c25>
2018-05-07 20:42:38.246     7f2f0a589bc0        FATAL   txpool  src/cryptonote_core/tx_pool.cpp:1280    Failed to insert key images from txpool tx
2018-05-07 20:42:38.246     7f2f0a589bc0        ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:513     Failed to initialize memory pool
2018-05-07 20:42:38.246     7f2f0a589bc0        INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2018-05-07 20:42:38.247     7f2f0a589bc0        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2018-05-07 20:42:39.288     7f2f0a589bc0        INFO    global  src/daemon/core.h:103   Deinitializing core...
2018-05-07 20:42:39.297     7f2f0a589bc0        INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2018-05-07 20:42:39.297     7f2f0a589bc0        INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully
```



# Discussion History
## moneromooo-monero | 2018-05-07T21:16:19+00:00
That was fixed, use current code. There'll be a 0.12.1.0 soonish if you don't want to build your own.

+invalid


## joelstahre | 2018-05-07T21:21:22+00:00
What do you mean by fixed? Any instructions on how to do it?

## moneromooo-monero | 2018-05-07T21:28:34+00:00
I mean made to work. If you pull the current code (either master or release-0.12 branch), you have the fix and should be able to start normally.

## rnhmjoj | 2018-05-09T08:57:13+00:00
@moneromooo-monero can you link the commit?

EDIT:
It looks like this is the one: https://github.com/monero-project/monero/commit/08343abaf432c56124651a20099d0e5b029aa62e

# Action History
- Created by: joelstahre | 2018-05-07T20:43:48+00:00
- Closed at: 2018-05-07T21:24:51+00:00
