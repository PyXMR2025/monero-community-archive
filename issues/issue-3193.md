---
title: Cant run monerod for testnet and mainnet at the same time.
source_url: https://github.com/monero-project/monero/issues/3193
author: moneroexamples
assignees: []
labels: []
created_at: '2018-01-28T02:55:29+00:00'
updated_at: '2018-02-18T19:27:57+00:00'
type: issue
status: closed
closed_at: '2018-02-18T19:27:57+00:00'
---

# Original Description
Monero master at:

commit 6ed314854cf87a7eb5810ef8a5dd707b4b9295e7

trying to run monerod for mainet and testnet at the same computer, results now in:

```
018-01-28 02:53:10.965     7f0f3bc58bc0        FATAL   net     contrib/epee/include/net/abstract_tcp_server2.inl:741 Error starting server: bind: Address already in use
2018-01-28 02:53:10.967     7f0f3bc58bc0        INFO    global  src/daemon/core.h:101 Deinitializing core...
2018-01-28 02:53:10.969     7f0f3bc58bc0        ERROR   daemon  src/daemon/core.h:106 Failed to deinitialize core...
2018-01-28 02:53:10.969     7f0f3bc58bc0        INFO    global  src/daemon/protocol.h:75      Stopping cryptonote protocol...
2018-01-28 02:53:10.969     7f0f3bc58bc0        INFO    global  src/daemon/protocol.h:79      Cryptonote protocol stopped successfully
2018-01-28 02:53:10.970     7f0f3bc58bc0        ERROR   daemon  src/daemon/main.cpp:294       Exception in main! Failed to initialize p2p server.
```

only one can be run (either mainnet or testnet).



# Discussion History
## stoffu | 2018-01-28T05:10:48+00:00
I don't observe this issue on macOS Sierra 10.12.6.

## leonklingele | 2018-01-28T06:22:01+00:00
Reproducible on Debian. However testnet daemon starts up fine when specifying a log level (e.g. `--log-level 1`). Strange.

## leonklingele | 2018-01-28T06:37:10+00:00
OK, something fishy is going on.

When starting the testnet daemon via a systemd unit, for whatever reason it tries to bind to `0.0.0.0:18080`:

```
Jan 28 06:25:57 service-monerod systemd[1]: Started Monero node deamon (testnet).
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.907            7f056a92b780        INFO         global        src/daemon/main.cpp:286        Monero 'Helium Hydra' (v0.11.1.0-master-6ed31485)
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.908            7f056a92b780        INFO         daemon        src/daemon/main.cpp:288        Moving from main() into the daemonize now.
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.908            7f056a92b780        INFO         global        src/daemon/protocol.h:53        Initializing cryptonote protocol...
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.908            7f056a92b780        INFO         global        src/daemon/protocol.h:58        Cryptonote protocol initialized OK
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.908            7f056a92b780        INFO         global        src/daemon/p2p.h:63        Initializing p2p server...
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.908            7f056a92b780        INFO         net.throttle        contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 2048 kbps
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.908            7f056a92b780        INFO         net.p2p        src/p2p/net_node.inl:1817        Set limit-up to 2048 kB/s
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.908            7f056a92b780        INFO         net.throttle        contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.908            7f056a92b780        INFO         net.p2p        src/p2p/net_node.inl:1830        Set limit-down to 8192 kB/s
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.908            7f056a92b780        INFO         net.throttle        contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 2048 kbps
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.909            7f056a92b780        INFO         net.p2p        src/p2p/net_node.inl:1852        Set limit-up to 2048 kB/s
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.909            7f056a92b780        INFO         net.throttle        contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.909            7f056a92b780        INFO         net.p2p        src/p2p/net_node.inl:1856        Set limit-down to 8192 kB/s
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.909            7f056a92b780        INFO         net.p2p        src/p2p/net_node.inl:360        Added seed node: 163.172.182.165:28080
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.909            7f056a92b780        INFO         net.p2p        src/p2p/net_node.inl:360        Added seed node: 195.154.123.123:28080
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.909            7f056a92b780        INFO         net.p2p        src/p2p/net_node.inl:360        Added seed node: 212.83.172.165:28080
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.909            7f056a92b780        INFO         net.p2p        src/p2p/net_node.inl:360        Added seed node: 212.83.175.67:28080
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.909            7f056a92b780        INFO         net.p2p        src/p2p/net_node.inl:360        Added seed node: 5.9.100.248:28080
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.909            7f056a92b780        INFO         net        contrib/epee/include/net/abstract_tcp_server2.inl:802        Set server type to: 2 from name: P2P, prefix_name = P2P
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.909            7f056a92b780        INFO         net.p2p        src/p2p/net_node.inl:536        Binding on 0.0.0.0:18080
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.911            7f056a92b780        FATAL        net        contrib/epee/include/net/abstract_tcp_server2.inl:741        Error starting server: bind: Address already in use
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.911            7f056a92b780        ERROR        net.p2p        src/p2p/net_node.inl:538        Failed to bind server
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.912            7f056a92b780        INFO         global        src/daemon/core.h:101        Deinitializing core...
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.913            7f056a92b780        ERROR        daemon        src/daemon/core.h:106        Failed to deinitialize core...
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.913            7f056a92b780        INFO         global        src/daemon/protocol.h:75        Stopping cryptonote protocol...
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.913            7f056a92b780        INFO         global        src/daemon/protocol.h:79        Cryptonote protocol stopped successfully
Jan 28 06:25:58 service-monerod monerod[9484]: 2018-01-28 06:25:58.913            7f056a92b780        ERROR        daemon        src/daemon/main.cpp:294        Exception in main! Failed to initialize p2p server.
Jan 28 06:25:58 service-monerod systemd[1]: monerod-testnet.service: Main process exited, code=exited, status=1/FAILURE
Jan 28 06:25:58 service-monerod systemd[1]: monerod-testnet.service: Unit entered failed state.
Jan 28 06:25:58 service-monerod systemd[1]: monerod-testnet.service: Failed with result 'exit-code'.
Jan 28 06:25:59 service-monerod systemd[1]: monerod-testnet.service: Service hold-off time over, scheduling restart.
Jan 28 06:25:59 service-monerod systemd[1]: Stopped Monero node deamon (testnet).
Jan 28 06:25:59 service-monerod systemd[1]: monerod-testnet.service: Start request repeated too quickly.
Jan 28 06:25:59 service-monerod systemd[1]: Failed to start Monero node deamon (testnet).
```

This doesn't appear to be the case when starting it directly from bash using the exact same arguments.

## leonklingele | 2018-01-28T07:38:27+00:00
I am left clueless but still want to share my findings so far.

Starting `monerod` as follows works fine (no `Address already in use` error):
```bash
$ pwd
/root
$ /root/monero/build/release/bin/monerod --testnet-data-dir /srv/share/testnet/ \
    --rpc-bind-ip 127.0.0.1 --restricted-rpc --p2p-bind-ip 0.0.0.0 --fluffy-blocks \
    --log-level 1 --testnet
```

----

The `Address already in use` error appears in all of the following scenarios:

1. When changing the order of arguments, e.g. `--log-level 1 --testnet --fluffy-blocks` (fails) instead of `--fluffy-blocks --log-level 1 --testnet` (works, see above)
2. When removing `--fluffy-blocks` or `--log-level 1`
3. When starting `monerod` directly from the `bin` directory:

```bash
$ pwd
/root/monero/build/release/bin
$ ./monerod --testnet-data-dir /srv/share/testnet/ --rpc-bind-ip 127.0.0.1 \
    --restricted-rpc --p2p-bind-ip 0.0.0.0 --fluffy-blocks --log-level 1 --testnet
..
2018-01-28 07:32:52.166	    7fe58a4ba780	FATAL	net	contrib/epee/include/net/abstract_tcp_server2.inl:741	Error starting server: bind: Address already in use
..
```

WTF❓

## moneromooo-monero | 2018-01-28T08:52:14+00:00
Please give the exact command lines of a failing case (the two commands) since it's hit and miss. Works with a couple days old daemon at least.

## leonklingele | 2018-01-28T09:02:06+00:00
@moneromooo-monero reproducible with:

mainnet:
`$ /root/monero/build/release/bin/monerod --data-dir /srv/share/ --rpc-bind-ip 127.0.0.1 --restricted-rpc --p2p-bind-ip 0.0.0.0 --db-sync-mode safe --fluffy-blocks`

testnet (fails with `Address already in use` as illustrated before):
`$ /root/monero/build/release/bin/monerod --testnet-data-dir /srv/share/testnet/ --rpc-bind-ip 127.0.0.1 --restricted-rpc --p2p-bind-ip 0.0.0.0 --db-sync-mode safe --fluffy-blocks --testnet`

## moneromooo-monero | 2018-01-28T09:45:05+00:00
https://github.com/monero-project/monero/pull/3196

## moneroexamples | 2018-01-28T11:02:20+00:00
@moneromooo-monero 

Thx. The PR https://github.com/monero-project/monero/pull/3196 fixes the issue for me. I will leave the issue open for few days, for visibility, as it seams not only me have this problem.

## moneromooo-monero | 2018-01-28T15:36:20+00:00
We usually keep bugs open till the patch is merged.

## moneromooo-monero | 2018-02-18T19:20:51+00:00
+resolved

# Action History
- Created by: moneroexamples | 2018-01-28T02:55:29+00:00
- Closed at: 2018-02-18T19:27:57+00:00
