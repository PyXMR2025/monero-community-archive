---
title: 'Linux 12.0 daemon was working now will not restart: internal error: kept_by_block=0,'
source_url: https://github.com/monero-project/monero/issues/3770
author: ronohara
assignees: []
labels: []
created_at: '2018-05-07T04:52:09+00:00'
updated_at: '2018-05-16T10:32:56+00:00'
type: issue
status: closed
closed_at: '2018-05-16T10:32:56+00:00'
---

# Original Description
monero@m4 ~ $ monerod --config-file /etc/monero/monerod.conf
2018-05-07 04:46:12.110	    7fe47fc570c0	WARN 	global	src/common/util.cpp:569	Running with glibc 2.25, hangs may occur - change glibc version if possible
2018-05-07 04:46:12.112	    7fe47fc570c0	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-05-07 04:46:12.112	    7fe47fc570c0	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-05-07 04:46:12.112	    7fe47fc570c0	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-05-07 04:46:12.112	    7fe47fc570c0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-05-07 04:46:16.381	    7fe47fc570c0	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-05-07 04:46:16.381	    7fe47fc570c0	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-05-07 04:46:16.381	    7fe47fc570c0	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 192.168.77.184:18081
2018-05-07 04:46:16.381	    7fe47fc570c0	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-05-07 04:46:16.381	    7fe47fc570c0	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-05-07 04:46:16.381	    7fe47fc570c0	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /var/lib/monero/lmdb ...
2018-05-07 04:46:16.754	    7fe47fc570c0	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:398	internal error: kept_by_block=0,  kei_image_set.size()=1
txin.k_image=<fc919121b0300d9309242abfa2280b95738cc2d90309c98632376b8c8254a523>
tx_id=<5d8028a8e2163435675e5b0f8344bdfd5f464ccda34556ea642ecbb2c994f466>
2018-05-07 04:46:16.754	    7fe47fc570c0	FATAL	txpool	src/cryptonote_core/tx_pool.cpp:1280	Failed to insert key images from txpool tx
2018-05-07 04:46:16.754	    7fe47fc570c0	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:513	Failed to initialize memory pool
2018-05-07 04:46:16.754	    7fe47fc570c0	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-05-07 04:46:16.754	    7fe47fc570c0	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-05-07 04:46:20.761	    7fe47fc570c0	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-05-07 04:46:20.797	    7fe47fc570c0	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-05-07 04:46:20.797	    7fe47fc570c0	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
m

# Discussion History
## Kukunin | 2018-05-07T07:24:59+00:00
Affects me as well. It seems that there is a wrong transaction appeared in txpool, that crashes the daemon

## moneromooo-monero | 2018-05-07T10:34:42+00:00
That load problem fixed already.
For the crash, post a stack trace of that crash.


## buyongji | 2018-05-07T11:42:58+00:00
I also have the same problem, how to solve?

## kirichenko | 2018-05-07T12:17:43+00:00
Me too:

```
monerod@Ubuntu-1604-xenial-64-minimal:~/monero-v0.12.0.0$ ./monerod --rpc-bind-ip 0.0.0.0 --confirm-external-bind --restricted-rpc
2018-05-07 12:04:23.800     7f95a4507740        INFO    global  src/daemon/main.cpp:280 Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-05-07 12:04:23.800     7f95a4507740        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-05-07 12:04:23.800     7f95a4507740        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-05-07 12:04:23.800     7f95a4507740        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-05-07 12:04:27.825     7f95a4507740        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-05-07 12:04:27.825     7f95a4507740        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-05-07 12:04:27.826     7f95a4507740        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 0.0.0.0:18081
2018-05-07 12:04:27.826     7f95a4507740        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2018-05-07 12:04:27.826     7f95a4507740        INFO    global  src/daemon/core.h:86    Initializing core...
2018-05-07 12:04:27.826     7f95a4507740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder /home/monerod/.bitmonero/lmdb ...
2018-05-07 12:04:28.168     7f95a4507740        ERROR   txpool  src/cryptonote_core/tx_pool.cpp:398     internal error: kept_by_block=0,  kei_image_set.size()=1
txin.k_image=<6e8266eabb607c99850a283dfa0b2213273a184922a4b76b5fbde551b8d4eaa6>
tx_id=<2c85cc54304f572829a2180290337fb762b5ec4e0b5026a44a9500cce2d94c25>
2018-05-07 12:04:28.168     7f95a4507740        FATAL   txpool  src/cryptonote_core/tx_pool.cpp:1280    Failed to insert key images from txpool tx
2018-05-07 12:04:28.169     7f95a4507740        ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:513     Failed to initialize memory pool
2018-05-07 12:04:28.169     7f95a4507740        INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2018-05-07 12:04:28.169     7f95a4507740        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2018-05-07 12:04:32.178     7f95a4507740        INFO    global  src/daemon/core.h:103   Deinitializing core...
2018-05-07 12:04:32.189     7f95a4507740        INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2018-05-07 12:04:32.189     7f95a4507740        INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully
```

Fixed with https://github.com/monero-project/monero/issues/2834#issuecomment-345331178

## emesik | 2018-05-07T13:25:20+00:00
I had the same problem. The fix mentioned in the linked comment helped to start the daemon again.

However... Wasn't that a successful mempool spamming attack?

My [pool stat website](https://pooldata.xmrlab.com/) stopped gathering data on 2018-05-05 3:38 UTC when the pool reached 415 txns of 10.75MiB. Since that moment the daemon was offline wit the error mentioned above.

Are we sure it's not a vulnerability?

## metamirror | 2018-05-07T22:22:39+00:00
I have the same problem on Linux (Ubuntu 16.04.4 LTS). Daemon was working but then froze and won't restart. 

During the startup sequence, this appears in red:
```
2018-05-07 22:12:50.825	    7ff87f864740	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:398	internal error: kept_by_block=0,  kei_image_set.size()=1
txin.k_image=<6e8266eabb607c99850a283dfa0b2213273a184922a4b76b5fbde551b8d4eaa6>
tx_id=<2c85cc54304f572829a2180290337fb762b5ec4e0b5026a44a9500cce2d94c25>
2018-05-07 22:12:50.825	    7ff87f864740	FATAL	txpool	src/cryptonote_core/tx_pool.cpp:1280	Failed to insert key images from txpool tx
2018-05-07 22:12:50.825	    7ff87f864740	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:513	Failed to initialize memory pool
```


## moneromooo-monero | 2018-05-07T22:31:49+00:00
Just use current code, it's been fixed already as I said above.

## vmsplice | 2018-05-08T01:06:36+00:00
I am having the same problem, Debian stable and monerod v0.12.0.0.

@moneromooo-monero, sorry, I'm a newbie, by current code do you mean the current master branch only available on GitHub? We're already using the latest official point release (0.12.0.0).

As far as I'm concerned, the daemon just stopped working out of nowhere. Do we really need to compile monerod ourselves or use external tools (mdb_drop.c) to make it work again? If that's the case, fine. But I would like to at least have an official announcement about this kind of thing. 

What caused this to happen, was this some sort of an attack? I would presume it's not a good thing if lots of Monero nodes can be crashed like this. Is there something we could have done to prevent this? Is the official recommendation to fix the database ourselves or wait for a fix from the dev team? Any idea when we can expect to have working pre-built binaries available again?

## vmsplice | 2018-05-08T07:29:43+00:00
Answering to myself, @moneromooo-monero's comments from another issue (#3778):
> If you pull the current code (either master or release-0.12 branch), you have the fix and should be able to start normally.
> There'll be a 0.12.1.0 soonish if you don't want to build your own.

Sounds good. Still curious for an explanation, this isn't supposed to happen, right?

## ronohara | 2018-05-12T10:04:12+00:00
FYI - I was unable to build from source - zmq.hpp missing on a Gentoo system.

In addition to the zeromq package requirement, it turns out you need the cppzmq package - c++ bindings.

The build instructions may need a refresh.

For me, it was .... emerge cppzmq
then update my local git repository 
then make


EDIT - just to confirm.  Compiling from the latest source has fixed the crash.

## arnuschky | 2018-05-13T06:34:59+00:00
Summary of workaround mentioned by @kirichenko for Ubuntu:

```bash
apt-get install liblmdb-dev
wget http://highlandsun.com/hyc/mdb_drop.c
gcc mdb_drop.c /usr/lib/x86_64-linux-gnu/liblmdb.a -lpthread -o mdb_drop
./mdb_drop -d -s txpool_meta ~/.bitmonero/lmdb/
./mdb_drop -d -s txpool_blob ~/.bitmonero/lmdb/
```

## moneromooo-monero | 2018-05-16T10:24:14+00:00
The loading was fixed a while ago, and there does not seem to be a crash. Reopen if there is actually a crash.

+resolved

# Action History
- Created by: ronohara | 2018-05-07T04:52:09+00:00
- Closed at: 2018-05-16T10:32:56+00:00
