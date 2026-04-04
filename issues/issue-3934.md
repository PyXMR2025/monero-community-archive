---
title: monero-wallet-rpc  get error when using "method":"transfer". v0.12.2.0
source_url: https://github.com/monero-project/monero/issues/3934
author: zhangdaoling
assignees: []
labels: []
created_at: '2018-06-05T13:14:28+00:00'
updated_at: '2018-06-25T22:09:00+00:00'
type: issue
status: closed
closed_at: '2018-06-25T22:09:00+00:00'
---

# Original Description
the error {
  "error": {
    "code": -38,
    "message": "no connection to daemon"
  },
  "id": "0",
  "jsonrpc": "2.0"
}

getheight ,get tranfers is ok.

the rpc.log is:
2018-06-05 10:11:01.021   0x7fffe67b33c0    INFO    logging contrib/epee/src/mlog.cpp:185   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-05 10:11:01.053   0x7fffe67b33c0    INFO    global  contrib/epee/include/net/http_server_impl_base.h:76 Binding on 0.0.0.0:18082
2018-06-05 10:11:01.054   0x7fffe67b33c0    WARN    wallet.rpc  src/wallet/wallet_rpc_server.cpp:3001   Starting wallet RPC server
2018-06-05 10:11:05.449 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:3762 Loaded wallet keys file, with public address: 4354iETEVskdUJ1cqLtBziaMKrEDNeMAdUUJPBQ6aJr3aJG4NJY4TWnJk9268QdBEu3XjPYwiijS5LbsYnDH6WzcNCsUKKV
2018-06-05 10:11:05.449 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:3768 file not found: /Users/zhangdaoling/work/chain_work/2-monero/wallet_main/MoneroTestWallet, starting with empty blockchain
2018-06-05 10:13:17.842 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1297 Received money: 0.099999990000, with tx: <e9e4227ff6b322773ea89eaad368ffe6300d99fc7ebcf87f9eb1215e6e7ce447>
2018-06-05 10:13:47.958 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1297 Received money: 0.097434120000, with tx: <dd6b1809b413d31372387c2d748d8e0e9027602408b48efc68df62d6c92500ea>
2018-06-05 10:13:47.958 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1403 Spent money: 0.099999990000, with tx: <dd6b1809b413d31372387c2d748d8e0e9027602408b48efc68df62d6c92500ea>
2018-06-05 10:13:48.095 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1297 Received money: 0.087770640000, with tx: <65e02cc8bd1aa01382353344ec35b17a085a520b9c5bd7a6292c9ed4f835279d>
2018-06-05 10:13:48.095 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1403 Spent money: 0.097434120000, with tx: <65e02cc8bd1aa01382353344ec35b17a085a520b9c5bd7a6292c9ed4f835279d>
2018-06-05 10:14:06.703 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1297 Received money: 0.075441040000, with tx: <d0c99695782ad20051220bf9e8d4ebf71e53d3c8c584993ab0392e27254c1c68>
2018-06-05 10:14:06.703 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1403 Spent money: 0.087770640000, with tx: <d0c99695782ad20051220bf9e8d4ebf71e53d3c8c584993ab0392e27254c1c68>
2018-06-05 10:14:08.318 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1297 Received money: 0.041114300000, with tx: <d9ebfc1064e409f00e00ee0a19a7c7f1218145724c4c569d6c9e0be019717e94>
2018-06-05 10:14:08.318 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1403 Spent money: 0.075441040000, with tx: <d9ebfc1064e409f00e00ee0a19a7c7f1218145724c4c569d6c9e0be019717e94>
2018-06-05 10:14:29.731 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1684 !r. THROW EXCEPTION: error::no_connection_to_daemon
2018-06-05 10:14:29.732 [RPC0]  WARN    net.http    src/wallet/wallet_errors.h:794  /DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1684:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
2018-06-05 10:14:29.732 [RPC0]  ERROR   wallet.rpc  src/wallet/wallet_rpc_server.cpp:109    Exception at while refreshing, what=no connection to daemon
2018-06-05 10:14:49.737 [RPC0]  ERROR   net.http    contrib/epee/include/net/http_client.h:394  HTTP_CLIENT: Failed to SEND
2018-06-05 10:14:49.737 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1684 !r. THROW EXCEPTION: error::no_connection_to_daemon
2018-06-05 10:14:49.737 [RPC0]  WARN    net.http    src/wallet/wallet_errors.h:794  /DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1684:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
2018-06-05 10:14:49.737 [RPC0]  ERROR   wallet.rpc  src/wallet/wallet_rpc_server.cpp:109    Exception at while refreshing, what=no connection to daemon
2018-06-05 10:15:34.107 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1684 !r. THROW EXCEPTION: error::no_connection_to_daemon
@

# Discussion History
## zhangdaoling | 2018-06-06T08:17:55+00:00
diff v0.12.2 v0.12.1 contrib/epee/include/net/abstract_tcp_server2.inl
#define DEFAULT_TIMEOUT_MS_LOCAL boost::posix_time::milliseconds(120000) // 2 minutes
#define DEFAULT_TIMEOUT_MS_REMOTE boost::posix_time::milliseconds(10000) // 10 seconds

is this the reason that monero-wallet-rpc always  get error “error::no_connection_to_daemon”.
Why REMOTE is 10 seconds but LOCAL is 2 minutes.
anyone here, please

## moneromooo-monero | 2018-06-06T09:47:20+00:00
This was done to avoid DoS. Does it work if you set these to, say, 10 minutes ? 
boost::posix_time::milliseconds(600000)

## zhangdaoling | 2018-06-06T10:06:42+00:00
@moneromooo-monero ,can i simply use v12.0, is there any effect for v12.2?

## moneromooo-monero | 2018-06-06T10:34:09+00:00
0.12.0.0 has a known bug which can cause the dameon to stop syncing until you restart it.

## zhangdaoling | 2018-06-06T10:38:55+00:00
@moneromooo-monero any other effect for v12.2？syncing is not a problem because we have common moniter for node

## moneromooo-monero | 2018-06-06T10:40:02+00:00
If syncing is not a problem, then I think you should be OK with 0.12.0.0.

## zhangdaoling | 2018-06-06T10:40:35+00:00
@moneromooo-monero what about 0.12.1.0

## moneromooo-monero | 2018-06-06T10:53:37+00:00
<s>It is pretty much the same as 0.12.2.0. In particular, it does have the timeout change.</s>

Wait, I'm wrong. 0.12.1.0 does not have the timeout change, use it as its sync is fixed :)

## zhangdaoling | 2018-06-06T11:08:10+00:00
@moneromooo-monero ，this error just happen when v12.2.  v12.1 is ok 

## zhangdaoling | 2018-06-06T11:15:21+00:00
@moneromooo-monero  its ok if we change #define DEFAULT_TIMEOUT_MS_REMOTE boost::posix_time::milliseconds(100000) // 100 seconds

this is detail：

git diff contrib/epee/include/net/abstract_tcp_server2.inl
diff --git a/contrib/epee/include/net/abstract_tcp_server2.inl b/contrib/epee/include/net/abstract_tcp_server2.inl
index 91a94c2..c419906 100644
--- a/contrib/epee/include/net/abstract_tcp_server2.inl
+++ b/contrib/epee/include/net/abstract_tcp_server2.inl
@@ -57,7 +57,7 @@
 #define MONERO_DEFAULT_LOG_CATEGORY "net"

 #define DEFAULT_TIMEOUT_MS_LOCAL boost::posix_time::milliseconds(120000) // 2 minutes
-#define DEFAULT_TIMEOUT_MS_REMOTE boost::posix_time::milliseconds(10000) // 10 seconds
+#define DEFAULT_TIMEOUT_MS_REMOTE boost::posix_time::milliseconds(120000) // 10 seconds
 #define TIMEOUT_EXTRA_MS_PER_BYTE 0.2

 PRAGMA_WARNING_PUSH
@@ -583,7 +583,7 @@ PRAGMA_WARNING_DISABLE_VS(4355)
   {
     boost::posix_time::milliseconds ms = (boost::posix_time::milliseconds)(unsigned)(bytes * TIMEOUT_EXTRA_MS_PER_BYTE);
     ms += m_timer.expires_from_now();
-    if (ms > get_default_time())
+    if (ms < get_default_time())
       ms = get_default_time();
     return ms;
   }

## moneromooo-monero | 2018-06-06T11:58:36+00:00
OK, thanks for confirming.

## Lafudoci | 2018-06-06T12:14:58+00:00
I have the same "no connection to daemon" errors a lot since v0.12.2. Maybe they're the same timeout issue?
Here is my rpc log.
https://paste.fedoraproject.org/paste/-b~ckQCApbF-inYp2FncSA


## moneromooo-monero | 2018-06-08T20:22:02+00:00
https://github.com/monero-project/monero/pull/3962 fixes this.

## Lafudoci | 2018-06-10T06:09:47+00:00
#3962 resolved my issue mentioned above.

## Zarkoob | 2018-06-11T05:02:24+00:00
@moneromooo-monero any notes when this goes live? I'm having problems when trying sending from ledger now on a public node. I can't at all it seems unless it's my own node. The time it takes to make a transaction if even hurrying is more than ~7 seconds. 

## moneromooo-monero | 2018-06-11T09:04:11+00:00
You'll see it go to "merged" state on github when it gets merged.
But if you have your own node, why would you want to use a stranger's in the first place ?

## Zarkoob | 2018-06-11T13:29:40+00:00
@moneromooo-monero the ledger machine doesn’t run the node just the ledger. 

Same house - two computers 

## moneromooo-monero | 2018-06-25T21:57:52+00:00
+resolved

# Action History
- Created by: zhangdaoling | 2018-06-05T13:14:28+00:00
- Closed at: 2018-06-25T22:09:00+00:00
