---
title: Incorrect report of "No incoming connections" in high latency environment
source_url: https://github.com/monero-project/monero/issues/4654
author: qubenix
assignees: []
labels: []
created_at: '2018-10-18T23:47:28+00:00'
updated_at: '2018-10-19T00:18:01+00:00'
type: issue
status: closed
closed_at: '2018-10-19T00:18:01+00:00'
---

# Original Description
OS: Qubes 4 & Whonix 14

I have this reoccurring issue where the debug log will continuously print that there are no incoming connection even when there are. It seems that I'm hitting a handshake timeout with my peers. This is happening since testing out the v0.13.0.1-rc2 and continuing to at least commit 5638b07d9faa0ceb6c88c17e873256ec2569ce5a.

Here's some log, near the bottom I set log level to `1` and then you can see the timeouts: https://paste.debian.net/plainh/d9ecad37.

# Discussion History
## xiphon | 2018-10-18T23:54:27+00:00
There ain't any incoming connections in the logs. The log message is correct.

## qubenix | 2018-10-19T00:15:08+00:00
Then why do I continue to get blocks, `netstat` shows connections, and monerod's `status` show connections? You can see that in the logs I pasted, here is one such example:

```
2018-10-18 21:44:38.946 [P2P4]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-18 21:48:27.107     7353b538c780        INFO    logging contrib/epee/src/mlog.cpp:242New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-18 21:48:27.109     7353b538c780        INFO    msgwriter       src/common/scoped_message_writer.h:102        Height: 1685674/1685674 (100.0%) on mainnet, not mining, net hash 461.62 MH/s, v8 (next fork in 0.8 days), up to date, 8(out)+0(in) connections, uptime 0d 8h 32m 59s
```

## qubenix | 2018-10-19T00:17:57+00:00
Oh, my mistake it's just about incoming connections. 

# Action History
- Created by: qubenix | 2018-10-18T23:47:28+00:00
- Closed at: 2018-10-19T00:18:01+00:00
