---
title: 'Mutiple Monero Wallet RPC connections to Monero Daemon '
source_url: https://github.com/monero-project/monero/issues/5044
author: TylerTheFox
assignees: []
labels: []
created_at: '2019-01-07T04:07:55+00:00'
updated_at: '2019-01-08T03:44:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If 5 (or more) Monero Wallet RPCs connect to the same Monero Daemon with open wallets the RPCs will start throwing connection errors. 

With around 10 RPCs connected to the daemon all the RPCs start complaining after about 30 seconds.
```
2019-01-07 04:07:29.838 20844   ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2020     !r. THROW EXCEPTION: error::no_connection_to_daemon
2019-01-07 04:07:29.838 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2020     !r. THROW EXCEPTION: error::no_connection_to_daemon
2019-01-07 04:07:29.838 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2020     !r. THROW EXCEPTION: error::no_connection_to_daemon
2019-01-07 04:07:29.839 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2020     !r. THROW EXCEPTION: error::no_connection_to_daemon
2019-01-07 04:07:29.839 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2767     pull_blocks failed, try_count=3
2019-01-07 04:07:29.839 [RPC0]  ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:125    Exception at while refreshing, what=proxy exception in refresh thread
2019-01-07 04:07:31.827 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2020     !r. THROW EXCEPTION: error::no_connection_to_daemon
2019-01-07 04:07:31.828 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2020     !r. THROW EXCEPTION: error::no_connection_to_daemon
2019-01-07 04:07:33.887 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2020     !r. THROW EXCEPTION: error::no_connection_to_daemon
2019-01-07 04:07:33.888 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2020     !r. THROW EXCEPTION: error::no_connection_to_daemon
```

Was a connection limit for RPCs introduced recently? This did not occur in the past.

# Discussion History
## moneromooo-monero | 2019-01-07T13:51:37+00:00
Yes, it's a primitive mitigation against DoS. IIRC if the addresses are local, the timeouts are a lot more generous.

## TylerTheFox | 2019-01-07T20:43:43+00:00
This was tested on local host, perhaps a launch paramater setting is needed for this? 

## moneromooo-monero | 2019-01-07T20:49:52+00:00
The timeounts are N divided by 2 for every extra connection from the same host. N is 30 minutes for local hosts, 5 minutes otherwise. 5 connections should yield 112 second timeouts, which should be more than enough. What RPC are you calling ?

## TylerTheFox | 2019-01-07T20:53:39+00:00
Monero wallet rpc with launch flags --wallet-dir Wallets/ --rpc-bind-port 12198 --daemon-address 127.0.0.1:19472 --disable-rpc-login --trusted-daemon.

After about running 5 of those they all start timing out with different port binds ofc.

## moneromooo-monero | 2019-01-07T21:25:22+00:00
This should print out the timeout settings it's using.

<pre>
diff --git a/contrib/epee/include/net/abstract_tcp_server2.inl b/contrib/epee/include/net/abstract_tcp_server2.inl
index d8779f372..50ae34187 100644
--- a/contrib/epee/include/net/abstract_tcp_server2.inl
+++ b/contrib/epee/include/net/abstract_tcp_server2.inl
@@ -586,6 +586,7 @@ PRAGMA_WARNING_DISABLE_VS(4355)
     try { count = host_count(m_host); } catch (...) { count = 0; }
     const unsigned shift = std::min(std::max(count, 1u) - 1, 8u);
     boost::posix_time::milliseconds timeout(0);
+MGINFO("timeout: local " << m_local << ", shift " << sfift);
     if (m_local)
       timeout = boost::posix_time::milliseconds(DEFAULT_TIMEOUT_MS_LOCAL >> shift);
     else
</pre>

## TylerTheFox | 2019-01-08T03:33:47+00:00
I was testing it on the standard monero win32/linux build on the release page https://github.com/monero-project/monero/releases v0.13.0.4

This is the code that launches the RPC, but the issue occurs when launched manually as well (this was written before accounts were a thing with the RPC api).
https://github.com/Brandantl/Monero-TipBot/blob/develop/src/Core/RPCManager.cpp#L517

Works fine on the older Monero code bases such as https://github.com/LetheanMovement/lethean but not the newer Monero code base with the timeout issue.

monerod is being launched with default parameters. 

# Action History
- Created by: TylerTheFox | 2019-01-07T04:07:55+00:00
