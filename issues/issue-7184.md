---
title: 7.1.7 banning nodes added to config as "add-priority-node" when building new
  pruned nodes
source_url: https://github.com/monero-project/monero/issues/7184
author: MoneroNodeHoster
assignees: []
labels: []
created_at: '2020-12-23T22:57:01+00:00'
updated_at: '2020-12-26T15:38:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am setting my new pruned nodes on Ubuntu 20.04 using the CLI daemon. The existing full nodes are also running the CLI daemon on Ubuntu 20.04.

I am currently running a few full nodes and thought I would help the network by adding a few additional pruned nodes in remote locations. I successfully added my existing full nodes to the config of the new pruned nodes as priority-nodes to decrease the strain on the overall monero network and to speed up the building of the new pruned nodes.

After tailing the logs of the new pruned nodes, I realized the new nodes are banning my full nodes, despite the full nodes being added as "add-priority-node."

The only remedy I have found thus far is to repeatedly keep restarting the new pruned nodes as they build themselves, to allow them to continue downloading from my full nodes.

If a whitelisting function could be added for IPs set for "add-priority-node" that would be a great help.

# Discussion History
## moneromooo-monero | 2020-12-23T23:05:29+00:00
Post a level 2 log of this (--log-level 2)

## MoneroNodeHoster | 2020-12-23T23:22:59+00:00
All existing logs are level 0. I will try to recreate the issue using level 2.

To make a correction, the new nodes are "blocking" the priority nodes, not banning them.

## MoneroNodeHoster | 2020-12-24T04:16:07+00:00
51.79.71.134 is the priority node, another node of mine.
I did increase the out-going connections on 51.79.71.134 from the default of 8 to 2048, as it's a dedicated monero node on it's own VPS. I read in a white paper how 93%+ of all nodes at the time had under 250 connections and I thought increasing out-going connections would help to add more obscurity to the network and help the network in general.
I am not sure if that is what is causing the flagging.

2020-12-24 03:09:52.248 [P2P1]  DEBUG   net     contrib/epee/include/net/levin_protocol_handler_async.h:477     [51.79.71.134:18080 OUT] LEVIN_PACKET_RECEIVED. [len=171918, flags1, r?=0, cmd = 2007, v=1
2020-12-24 03:09:52.248 [P2P1]  INFO    net.p2p.traffic contrib/epee/include/storages/levin_abstract_invoke2.h:44       [51.79.71.134:18080 OUT] 171918 bytes received for category command-2007 initiated by peer
2020-12-24 03:09:52.248 [P2P1]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:2501    [51.79.71.134:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=4216, m_start_height=2254690, m_total_height=2258906
2020-12-24 03:09:52.248 [P2P1]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2502    [51.79.71.134:18080 OUT] [0] state: received chain in state standby
2020-12-24 03:09:52.248 [P2P1]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2506    [51.79.71.134:18080 OUT] Got NOTIFY_RESPONSE_CHAIN_ENTRY out of the blue, dropping connection
2020-12-24 03:09:52.248 [P2P1]  DEBUG   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2778    [51.79.71.134:18080 OUT] dropping connection id 831bc318-be03-4452-870c-4bd8d574790b (pruning seed 0), score 1, flush_all_spans 0
2020-12-24 03:09:52.248 [P2P1]  DEBUG   net.p2p src/p2p/net_node.inl:346        Host 51.79.71.134 fail score=11
2020-12-24 03:09:52.248 [P2P1]  INFO    net     contrib/epee/include/storages/levin_abstract_invoke2.h:150      Failed to invoke command 1002 return code -3
2020-12-24 03:09:52.248 [P2P1]  WARNING net.p2p src/p2p/net_node.inl:1197       [51.79.71.134:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-12-24 03:09:52.248 [P2P1]  INFO    global  src/p2p/net_node.inl:270        Host 51.79.71.134 blocked.
2020-12-24 03:09:52.248 [P2P1]  ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:765   Setting timer on a shut down object
2020-12-24 03:09:52.249 [P2P1]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2839    [51.79.71.134:18080 OUT] [0] state: closed in state standby
2020-12-24 03:09:52.249 [P2P1]  INFO    net.p2p src/p2p/net_node.inl:2592       [51.79.71.134:18080 831bc318-be03-4452-870c-4bd8d574790b OUT] CLOSE CONNECTION
2020-12-24 03:09:52.249 [P2P1]  DEBUG   net.conn        contrib/epee/src/connection_basic.cpp:184       Destructing connection #14228 to 51.79.71.134

## moneromooo-monero | 2020-12-24T12:35:52+00:00
That''s a millisecond's worth or logs. Send a bit more.

## moneromooo-monero | 2020-12-24T12:36:22+00:00
(from before, at least from 30 seconds before that)

## MoneroNodeHoster | 2020-12-24T13:22:32+00:00
Sorry, it's an open node so I was trying to be a minimalist with sharing node log info.
[monero.log-2020-12-24-03-11-42.zip](https://github.com/monero-project/monero/files/5739673/monero.log-2020-12-24-03-11-42.zip)


## MoneroNodeHoster | 2020-12-24T14:06:41+00:00
A second instance of the same issue, using a different priority-node, connecting from another node.
IP 51.222.106.129 is the priority-node that was banned on this VPS.

[monero.log-2020-12-24-10-51-16.zip](https://github.com/monero-project/monero/files/5739800/monero.log-2020-12-24-10-51-16.zip)

## MoneroArbo | 2020-12-24T14:25:48+00:00
> I did increase the out-going connections on 51.79.71.134 from the default of 8 to 2048

That's like a lot. Possible more than the system / daemon can handle?

## MoneroNodeHoster | 2020-12-24T14:49:07+00:00
Both 51.79.71.134 and 51.222.106.129 are on "OVH Comfort" 4v core VPS. The node software is the only thing running on the VPS other than fail2ban and the UFW.

When I bring up sync_info, I have not seen either VPS exceed 1100 connections, despite setting a 2048 connections cap.

When I look at OVH's system monitoring software, both VPS are performing well below their maximums with the exception of system memory. Since Ubuntu caches the blockchain, the both VPS usually hovers around 90% memory utilization. I don't think either VPS has hit more than 50% cpu utilization, even once.

## moneromooo-monero | 2020-12-24T15:52:39+00:00
Do you have the log from 51.79.71.134 for the same time range ?

## moneromooo-monero | 2020-12-24T15:56:14+00:00
ie, 3:09 to 3:10

## MoneroNodeHoster | 2020-12-24T16:58:32+00:00
Sorry, I lost the applicable logs from 51.79.71.134 already.

I do have the corresponding level 1 logs from 51.222.106.129 during that same time period that VPS was blocked. The "new" pruned node that was connecting to 51.222.106.129, is 51.222.87.128.

I am resetting my logs to level 2 on all of the servers and increasing logging and will rebuild the new nodes from scratch, to see if I can recreate the issue again, with much more logging.
[monero.log-2020-12-24-11-03-00.zip](https://github.com/monero-project/monero/files/5740189/monero.log-2020-12-24-11-03-00.zip)


## moneromooo-monero | 2020-12-24T17:06:49+00:00
I don't see 51.222.106.129 being blocked in the log I have, so that won't do. AFAICT the node banning receives a response from a query it never sent, so I need to see what the other side thinks it got.

## moneromooo-monero | 2020-12-24T17:07:21+00:00
Alternatively, it could be some really long delay from a query made long ago, and some intervening timeout.

## MoneroNodeHoster | 2020-12-24T17:19:55+00:00
Sorry, I believe I am creating confusion, because I did not have adequate logging set initially and I am trying to piece logs together from 2 priority nodes and 2 newly build nodes. Thus, 4 servers total, leading to confusion.

I wiped the blockchain from the 2 newly built nodes, and am rebuilding identically to what I did initially, this time with extensive level 2 logging, in an attempt to recreate the problem.

## erciccione | 2020-12-26T15:31:49+00:00
I too had this problem recently. Syncing a pruned node from another node using `--add-priority-node` caused the prioritary node to be banned multiple times. The problem seem to have solved itself after multiple restarts and now that the node is fully synced i'm not seeing no problem (the two nodes are connected, but no bans). When i started to get more verbose logs the problem stopped, so i have no details.

## moneromooo-monero | 2020-12-26T15:38:28+00:00
It's quite possibly that a pruned node will not reply to an attempt to get a set of block hashes for a range it has no full data for. I think the peer will now drop for this, and eventually drop since the same peer will be queried repeatedly. If this is the case, then a fix would be to not request this data if we know the peer is pruned for that range. Which it's supposed to do already IIRC, but there's at least one case where it does, so it'd  make sense for this bug to be due to it too.

# Action History
- Created by: MoneroNodeHoster | 2020-12-23T22:57:01+00:00
