---
title: Failed to connect to any of seed peers, continuing without seed
source_url: https://github.com/monero-project/monero/issues/3209
author: lukaszmatczak
assignees: []
labels:
- invalid
created_at: '2018-01-30T13:13:21+00:00'
updated_at: '2018-09-02T13:00:51+00:00'
type: issue
status: closed
closed_at: '2018-09-02T13:00:51+00:00'
---

# Original Description
Since 23rd January I see in log a lot of messages like:
```
2018-01-30 11:52:14.217 [P2P3]  WARN    net.p2p src/p2p/net_node.inl:1195       Failed to connect to any of seed peers, trying fallback seeds
2018-01-30 11:52:14.217 [P2P3]  WARN    net.p2p src/p2p/net_node.inl:1206       Failed to connect to any of seed peers, continuing without seeds
```
and also:
```
2018-01-30 11:43:59.370 [P2P8]  WARN    net.p2p src/p2p/net_node.inl:1629       [188.165.214.76:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2018-01-30 11:45:08.111 [P2P9]  WARN    net.p2p src/p2p/net_node.inl:834        [189.163.95.195:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2018-01-30 11:45:29.972 [P2P4]  WARN    net.p2p src/p2p/net_node.inl:759        [45.6.216.30:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2018-01-30 11:45:29.972 [P2P7]  WARN    net.p2p src/p2p/net_node.inl:808        [45.6.216.30:18080 OUT] COMMAND_HANDSHAKE Failed
```

In addition my pool is getting orphaned block much more often than before.

I didn't change anything so I think it's problem with Monero network.

# Discussion History
## moneromooo-monero | 2018-01-30T13:26:26+00:00
What version are you running ? Is this testnet or mainnet ?

## lukaszmatczak | 2018-01-30T14:11:22+00:00
v0.11.1.0, mainnet

## moneromooo-monero | 2018-01-30T15:06:56+00:00
Can you restart monerod with --log-level 0,net.p2p:DEBUG (or add net.p2p:DEBUG to your current log level, if non default). Then exit once it's warned about continuing without seeds, and paste the resulting log on fpaste.org or pastebin.mozilla.org or github paste.

## someniatko | 2018-01-30T17:39:31+00:00
Hi there, i had similar problem. Here is log from monerod while syncing, and running like @moneromooo-monero suggested:
https://gist.github.com/someniatko/f9792527ff57584039ffdb2cf2c4c09d

## moneromooo-monero | 2018-01-30T17:50:20+00:00
> DNS seed node lookup either timed out or failed

Looks like you have broken DNS. Either fix it, or you can run with DNS_PUBLIC=tcp://a.b.c.d with an IP of your choice.

## moneromooo-monero | 2018-01-30T17:50:56+00:00
Or --seed-node a.b.c.d if you have an IP.

## moneromooo-monero | 2018-06-10T19:06:31+00:00
I'll close as invalid if there's no followup soon.

## moneromooo-monero | 2018-09-02T12:57:24+00:00
+invalid

# Action History
- Created by: lukaszmatczak | 2018-01-30T13:13:21+00:00
- Closed at: 2018-09-02T13:00:51+00:00
