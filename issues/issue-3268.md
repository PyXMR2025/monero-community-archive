---
title: Monero Snap Package Not Starting  wallet.rpc
source_url: https://github.com/monero-project/monero/issues/3268
author: TimeTravelersHackedMe
assignees: []
labels: []
created_at: '2018-02-15T05:56:28+00:00'
updated_at: '2021-08-13T04:26:39+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:26:39+00:00'
---

# Original Description
Hey, I installed the snap package on Ubuntu because the Dockerfile we have is erroring out during the build. When I installed the package I was given 2 new executables called monero.monero-wallet-rpc and monero.monero-wallet-cli. I used the Wallet CLI to generate my Monero addresses and such. I waited for it to sync and now when I login to it, it doesn't say (out of sync) or anything. Now, I'm trying to run the Wallet RPC client so I can connect to it with this pool I'm trying to set up. Here's my start parameters:

```
--log-level 4 --disable-rpc-login --daemon-address=127.0.0.1:18081 --rpc-bind-port 18085 --password x --wallet-file /home/xxx/x --trusted-daemon --confirm-external-bind
````

I run the process by executing:
```
pm2 run process.json
```
Here's the process.json file:
```
{
  apps: [{
    name: 'Monero RPC',
    script: 'monero.monero-wallet-rpc',
    watch: false,
    args: '--log-level 4 --disable-rpc-login --daemon-address=127.0.0.1:18081 --rpc-bind-port 18082 --password x --wallet-file /home/xxx/x --trusted-daemon'
  }]

}
```

When I look at the process with pm2 logs "Monero RPC" it looks like the Monero RPC hangs when trying to start the server... This is what I see in the logs, followed by a lot of stuff that's coming from wallet.wallet2:
```
0|Monero R | 2018-02-15 05:51:12.150        7f49f3476740        TRACE   net     contrib/epee/include/net/net_helper.h:397       READ ENDS: Success. bytes_tr: 2612
0|Monero R | 2018-02-15 05:51:12.150        7f49f3476740        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:1550Got 1 and OK
0|Monero R | 2018-02-15 05:51:12.152        7f49f3476740        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:1610update_pool_state end
0|Monero R | 2018-02-15 05:51:12.152        7f49f3476740        INFO    wallet.wallet2  src/wallet/wallet2.cpp:1793Refresh done, blocks received: 1, balance: 0.000000000000, unlocked: 0.000000000000
0|Monero R | 2018-02-15 05:51:12.152        7f49f3476740        INFO    wallet.rpc      src/wallet/wallet_rpc_server.cpp:1883   Loaded ok
0|Monero R | 2018-02-15 05:51:12.152        7f49f3476740        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:795   Set server type to: 1 from name: RPC, prefix_name = RPC
0|Monero R | 2018-02-15 05:51:12.152        7f49f3476740        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18082
0|Monero R | 2018-02-15 05:51:12.152        7f49f3476740        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:734   start accept
0|Monero R | 2018-02-15 05:51:12.153        7f49f3476740        INFO    net.p2p src/p2p/connection_basic.cpp:164Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
0|Monero R | 2018-02-15 05:51:12.153        7f49f3476740        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:85    test, connection constructor set m_connection_type=1
0|Monero R | 2018-02-15 05:51:12.153        7f49f3476740        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:1898   Starting wallet rpc server
0|Monero R | 2018-02-15 05:51:12.153        7f49f3476740        INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:83     Run net_service loop( 1 threads)...
0|Monero R | 2018-02-15 05:51:12.153    [SRV_MAIN]      INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:821   Run server thread name: RPC
0|Monero R | 2018-02-15 05:51:12.153    [SRV_MAIN]      INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:828   JOINING all threads
```
When running nodejs-pool, I'm getting an error from the Worker saying that it was unable to open the wallet.

Any body know how I can debug this?

Also, another question: how is the daemon running? Does it run when I run monero.monero-wallet-rpc? Also, with the Snap package I notice that I don't have access to the monerod command... am I missing something?

# Discussion History
## TimeTravelersHackedMe | 2018-02-15T19:42:15+00:00
I guess there's no monerod package in the snap installation that the README.md recommends?

## selsta | 2021-08-13T04:26:39+00:00
Snap package is no longer supported and has been removed.

# Action History
- Created by: TimeTravelersHackedMe | 2018-02-15T05:56:28+00:00
- Closed at: 2021-08-13T04:26:39+00:00
