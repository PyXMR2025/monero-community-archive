---
title: bitmonerod runs out of file descriptors
source_url: https://github.com/monero-project/monero/issues/389
author: laanwj
assignees: []
labels: []
created_at: '2015-08-26T07:16:10+00:00'
updated_at: '2015-08-30T15:32:17+00:00'
type: issue
status: closed
closed_at: '2015-08-30T14:36:56+00:00'
---

# Original Description
I've noticed that bitmonerod runs out of file descriptors after a few days. This has happened twice now, so I thought it may be worth reporting.

Git version: 776b4fc91a821be152f0f23e6873aabb78a72029

Output:

```
ERROR   {5} {p1} 2015-08-26 06:58:20.582113 [abstract_tcp_server2.inl+489 ::do_send_chunk] send que size is more than ABSTRACT_SERVER_SEND_QUE_MAX_COUNT(1000), shutting down connection
ERROR   {5} {p1} 2015-08-26 06:58:26.357828 [abstract_tcp_server2.inl+489 ::do_send_chunk] send que size is more than ABSTRACT_SERVER_SEND_QUE_MAX_COUNT(1000), shutting down connection
[1440565113] libunbound[7241:0] error: can't create socket: Too many open files
[1440565113] libunbound[7241:0] error: can't create socket: Too many open files
[1440565113] libunbound[7241:0] error: can't create socket: Too many open files
[1440565113] libunbound[7241:0] error: can't create socket: Too many open files
[1440565113] libunbound[7241:0] error: can't create socket: Too many open files
[warn] epoll_create: Too many open files
[err] evsig_init: socketpair: Too many open files
2015-Aug-26 06:58:33.243670 [P2P2]Height: 711393 blob: 292 cumm: 292 p/t: 83 (1/79/0/0/0/0/0/0/0/2/457)ms
2015-Aug-26 06:58:33.290555 [P2P2]Blockchain stored OK, took: 45 ms
./start.sh: line 2:  7241 Segmentation fault      (core dumped) bitmonero/build/release/bin/bitmonerod --no-igd
```


# Discussion History
## fluffypony | 2015-08-26T07:32:28+00:00
It's a known issue we're trying to resolve - I've had it happen on mainchain on OS X, but not reproducibly on Linux (probably because of higher ulimits). What platform are you on?


## laanwj | 2015-08-26T08:40:22+00:00
This is on stock Ubuntu 14.04.3 LTS (no changed ulimits). ulimit shows:

```
open files                      (-n) 1024
```


## iamsmooth | 2015-08-26T22:30:54+00:00
suggest setting it much lower for testing. 50 should be more than sufficient if incoming connections are firewalled off.


## fluffypony | 2015-08-26T22:32:59+00:00
@iamsmooth my playing-around-with-testing environment is a production Linux box that has a high limit, but for reproducing this issue I agree.

This is mainnet only as far as I can tell, which definitely points to the MoneroPulse DNS checkpointing, so that's where I'm focused on atm


## laanwj | 2015-08-29T14:53:20+00:00
Happened again. This time it segfaulted while processing the error.

```
[err] evsig_init: socketpair: Too many open files
2015-Aug-29 12:31:52.344473 [P2P7]Blockchain stored OK, took: 231 ms
./start.sh: line 2:  1020 Segmentation fault      (core dumped) bitmonero/build/release/bin/bitmonerod --no-igd
```

dmesg:

```
[955438.165523] bitmonerod[1040]: segfault at 0 ip 00000000006c1ac1 sp 00007f2d5c7f3660 error 4 in bitmonerod[400000+4c7000]
```

addr2line (not a debug build, so just symbol info): 

```
ubuntu@monero:~$ addr2line -e bitmonero/build/release/bin/bitmonerod -fCi 0x6c1ac1                                                                
epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)
??:?
```

Is there anything that I can disable (eg `MoneroPulse DNS checkpointing`) to isolate the problem?


## fluffypony | 2015-08-29T14:57:44+00:00
This is what we're busy testing as a fix, if you want to try it:

```
diff --git a/external/unbound/libunbound/libworker.c b/external/unbound/libunbound/libworker.c
index 72b6153..c4e04ce 100644
--- a/external/unbound/libunbound/libworker.c
+++ b/external/unbound/libunbound/libworker.c
@@ -617,6 +617,7 @@ int libworker_fg(struct ub_ctx* ctx, struct ctx_query* q)
        /* process new query */
        if(!mesh_new_callback(w->env->mesh, &qinfo, qflags, &edns, 
                w->back->udp_buff, qid, libworker_fg_done_cb, q)) {
+               libworker_delete(w);
                free(qinfo.qname);
                return UB_NOMEM;
        }
```


## laanwj | 2015-08-29T15:48:33+00:00
Trying with that


## moneromooo-monero | 2015-08-30T09:21:54+00:00
Are you running a static build ? If so, try with dynamic. I get the problem only with static builds here, even when using the same unbound tree for both (the in-tree one). It seems weird so I want to know if you can get it to happen with dynamic builds.


## moneromooo-monero | 2015-08-30T09:22:47+00:00
Also, this makes it happen a lot quicker when testing:

Hmm, doesn't display correctly here, so.... 
Replace 3600 with 60 on src/cryptonote_core/cryptonote_core.cpp:104.

diff --git a/src/cryptonote_core/cryptonote_core.cpp b/src/cryptonote_core/cryptonote_core.cpp
index 6d2cc35..2ad3be2 100644
--- a/src/cryptonote_core/cryptonote_core.cpp
+++ b/src/cryptonote_core/cryptonote_core.cpp
@@ -101,7 +101,7 @@ namespace cryptonote
     if (m_checkpoints_updating.test_and_set()) return true;

```
 bool res = true;
```
-    if (time(NULL) - m_last_dns_checkpoints_update >= 3600)
-    if (time(NULL) - m_last_dns_checkpoints_update >= 60)
   {
     res = m_blockchain_storage.update_checkpoints(m_checkpoints_path, true, m_testnet);
     m_last_dns_checkpoints_update = time(NULL);


## moneromooo-monero | 2015-08-30T14:35:58+00:00
Fixed:
https://github.com/monero-project/bitmonero/commit/3c10239327b7495550c091d0789d9019c7bdf5b8

Seems to run well here with a very low ulimit -n, but please report if it still borks after a long time.


## fluffypony | 2015-08-30T14:36:56+00:00
Also I'm closing as we've merged this into master, please reopen if it occurs again


## laanwj | 2015-08-30T15:32:17+00:00
This is just the default `make` in the root, which results in a build in `build/release`. Looking at the ldd output libraries such as boost and icuuc are linked dynamically.


# Action History
- Created by: laanwj | 2015-08-26T07:16:10+00:00
- Closed at: 2015-08-30T14:36:56+00:00
