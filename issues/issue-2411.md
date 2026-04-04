---
title: Libunbound openssl error - 0.11.0.0 release version
source_url: https://github.com/monero-project/monero/issues/2411
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2017-09-08T10:00:39+00:00'
updated_at: '2018-07-21T10:00:50+00:00'
type: issue
status: closed
closed_at: '2018-07-21T10:00:50+00:00'
---

# Original Description
A few users have been reporting these "errors" on Linux 64-bit (using the latest release, Helium Hydra):

>[1504816717] libunbound[25519:0] info: warning: unsupported algorithm for trust anchor . DS IN

>[1504816717] libunbound[25519:0] warning: trust anchor . has no supported algorithms, the anchor is ignored (check if you need to upgrade unbound and openssl)

As far as I can tell, it doesn't inhibit them from syncing or using the daemon. 

Source:

https://www.reddit.com/r/Monero/comments/6yprar/mandatory_upgrade_monero_01100_helium_hydra/dmpa8ab/

# Discussion History
## moneromooo-monero | 2017-09-08T10:13:46+00:00
This prevents DNSSEC verification, but it's apparently not done well in the first place anyway. This looks like an OpenSSL which was compiled with SHA1 (or a cmake bug which causes USE_SHA1 to be undefined when building unbound).


## RichAyotte | 2017-09-08T19:47:39+00:00
Possibly some relevant information here.

> The format is a DNS resource record on one line, DS or DNSKEY.
> 
> If I call ub_ctx_add_ta() with the string you have there, the root
> anchor with a \n after it, it works fine.
> 
> The warning is printed if you try to load an unsupported trust anchor,
> this behaviour has changed in recent releases, dealing with loading
> trust anchors with unknown algorithms, to support root key rollover
> schemes more thoroughly.
> 
> However, the string you give has supported algorithms.  I do not
> understand either why you get this error.  Are you loading a different
> string?  (for instance with an ECDSA algorithm and the user has old
> OpenSSL with no ECDSA support).
> 
> Or have you compiled unbound without sha256 support?  Not even sure if
> that is possible and I think that needs configure options to do it,
> but then this message would appear.
> 
> Note the hard coded anchor will get you in trouble with the root key
> rollover that is talked about in public forums.  You need to have some
> sort of update process (f.e. using your software update).
> 
> Best regards, Wouter


https://www.unbound.net/pipermail/unbound-users/2016-January/004176.html

## anonimal | 2017-09-08T20:20:04+00:00
(referencing #2133 for housekeeping)

## MattTwinkleToes | 2017-09-18T23:12:00+00:00
I am afraid that it does see to stop us syncing or even accessing the wallet at all.  MY balance is 0.00000 at the moment.

```
./monerod 
2017-09-18 23:08:31.458	    7f7256275740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-release)
2017-09-18 23:08:31.458	    7f7256275740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-09-18 23:08:31.458	    7f7256275740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-09-18 23:08:31.458	    7f7256275740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
[1505776111] libunbound[2528:0] info: warning: unsupported algorithm for trust anchor . DS IN
[1505776111] libunbound[2528:0] warning: trust anchor . has no supported algorithms, the anchor is ignored (check if you need to upgrade unbound and openssl)
2017-09-18 23:08:33.208	    7f7256275740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-09-18 23:08:33.208	    7f7256275740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-09-18 23:08:33.208	    7f7256275740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-09-18 23:08:33.209	    7f7256275740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-09-18 23:08:33.209	    7f7256275740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-09-18 23:08:33.210	    7f7256275740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/matt/.bitmonero/lmdb ...
2017-09-18 23:08:33.406	    7f7256275740	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:102	Failed to parse transaction from blob
2017-09-18 23:08:33.406	    7f7256275740	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1020	Failed to parse tx from txpool
2017-09-18 23:08:33.406	    7f7256275740	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:409	Failed to initialize memory pool
2017-09-18 23:08:33.406	    7f7256275740	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-09-18 23:08:33.406	    7f7256275740	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-09-18 23:08:33.406	    7f7256275740	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-09-18 23:08:33.416	    7f7256275740	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-09-18 23:08:33.416	    7f7256275740	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
```




## moneromooo-monero | 2017-09-19T08:31:46+00:00
Can you file new bugs separately please, or this is going to be really confusing. One of the txes in the pool seems to be corrupt.

## moneromooo-monero | 2017-12-23T17:16:22+00:00
Might be fixed by https://github.com/monero-project/monero/pull/2996

## moneromooo-monero | 2018-07-19T22:01:32+00:00
Can someone who had that problem confirm whether this is fixed ?

## salim-b | 2018-07-19T22:14:43+00:00
it's fixed for me (Ubuntu 16.04 LTS) :slightly_smiling_face: 

## moneromooo-monero | 2018-07-21T09:57:20+00:00
Thanks

+resolved

# Action History
- Created by: dEBRUYNE-1 | 2017-09-08T10:00:39+00:00
- Closed at: 2018-07-21T10:00:50+00:00
