---
title: tx-proxy I2P / Tor, no outbound connections (only inbound)
source_url: https://github.com/monero-project/monero/issues/6938
author: selsta
assignees: []
labels: []
created_at: '2020-10-26T20:51:06+00:00'
updated_at: '2022-07-20T22:57:50+00:00'
type: issue
status: closed
closed_at: '2022-07-20T22:57:49+00:00'
---

# Original Description
I host I2P / Tor monero nodes with --tx-proxy and --anonymous-inbound, that works quite well but on both nodes I don’t have any outbound peers.

It looks like this on both nodes.

```
INC :                         I2P     no    xxx    0                   160847(9)/6408(81)            normal                   1898                0           0             0         0            
INC :                         I2P     no    xxx    0                   21417(14)/15039(14)           normal                   2510                0           0             0         0            
INC :                         I2P     no    xxx    0                   414479(69)/15491(69)          normal                   2778                0           0             0         0            
INC :                         Tor     no    xxx    0                   23893(9)/1916(17)             normal                   92                  0           0             0         0            
INC :                         Tor     no    xxx    0                   9428(20)/6631(20)             normal                   1014                0           0             0         0            
INC :                         Tor     no    xxx    0                   57781(6)/7451(39)             normal                   1036                0           0             0         0            
INC :                         Tor     no    xxx    0                   10015(50)/7246(50)            normal                   1032                0           0             0         0            
INC :                         Tor     no    xxx    0                   11440(24)/7451(24)            normal                   1038                0           0             0         0            
INC :                         Tor     no    xxx    0                   86729(69)/6426(69)            normal                   956                 0           0             0         0            
INC :                         Tor     no    xxx    0                   89972(16)/7451(16)            normal                   1038                0           0             0         0            
INC :                         Tor     no    xxx    0                   18702(81)/10342(81)           normal                   3423                0           0             0         0            
INC :                         Tor     no    xxx    0                   448998(0)/16082(2)            normal                   3451                0           0             0         0            
INC :                         Tor     no    xxx    0                   261783(40)/20408(40)          normal                   3531                0           0             0         0            
```

The missing outbound peers results in constant messages like this:

```
Lost all outbound connections to anonymity network - currently unable to send transaction(s)
```

Why do I have plenty inbound peers but not outbound ones? Should this get better once we have more I2P / Tor peers?

Sometimes I get outbound ones after restarting, but they drop pretty quickly and I stay at only inbound ones.

# Discussion History
## selsta | 2020-10-26T21:16:27+00:00
Most likely related https://github.com/monero-project/monero/issues/6631

## MoneroArbo | 2020-11-04T23:58:15+00:00
My server rebooted today because of a power failure and ever since then my outbound i2p connections have been much more stable, lasting upwards of 90 minutes, versus only 3 - 5 minutes previously. I'm not sure what would have changed, except this may have been the first time the i2p-zero daemon was reset since upgrading monerod to 0.17.x

Seems like maybe this issue only affects certain users / only happens under certain conditions, conditions that may or may not have to do with i2p-zero.

Another piece of evidence for it only affecting some users / only happening under some circumstances is that, like selsta, I've been able to maintain stable inbound connections even when outbound connections were failing. Those stable "inbound" connections are, I would think, seen as stable outbound connections by another daemon.

## selsta | 2020-11-05T00:02:27+00:00
On my 24/7 server where I have both Tor and I2P I just did a test and had:

- Tor: 3 outbound, 12 inbound
- I2P: 1 outbound, 6 inbound

on my second server:

- Tor: 3 outbound, 12 inbound
- I2P: 3 outbound, 3 inbound

It seems to me once we get even more Tor / I2P nodes it should get more and more stable. I still do get the "no outbound connections" message sometimes.

## MoneroArbo | 2020-11-05T00:26:42+00:00
I feel like the litmus test isn't how many connections you have at any given time, but how long they persist and, even more importantly, how often and for how long you have zero outbound connections. For example, on November 3rd my daemon printed the message

`Lost all outbound connections to anonymity network - currently unable to send transaction(s)`

no less than 11 times throughout the day. For comparison, I have seen that error zero times in the ~7 hours since my server rebooted. These numbers are with all six i2p mipseeds added as priority nodes, btw, which really shouldn't even be necessary.

Anyway I'm not sure exactly what that translates to in "uptime" but if there's a tor / i2p out peer even 90% of the time, that's still 10% of the time that tor / i2p users can't send transactions.

It may well be that the issue improves as we get more tor / i2p peers. I suspect you're right about that, but I also still suspect some sort of underlying implementation issue and don't know if the problem will entirely go away just from adding more peers.

But that's just my uneducated take.

**edit:** ~24 hours later and my server is back to its previous behavior of OUT i2p connections lasting only ~5 minutes and regularly printing the " Lost all outbound connections..." error

## maogo | 2020-11-13T13:03:53+00:00
I usually get 4-6 i2p inbound connections, but no outbound ,Sometimes see one i2p outbound in "print_cn" and Peer id is "0000000000000000" , and then it will be lost soon.

## moneromooo-monero | 2020-12-23T03:15:39+00:00
You can try changing 8 with, say, 5 on this line:
> const unsigned shift = get_state().sock_count > AGGRESSIVE_TIMEOUT_THRESHOLD ? std::min(std::max(count, 1u) - 1, 8u) : 0;
in contrib/epee/include/net/abstract_tcp_server2.inl

This will give Tor peers a more generous timeout. If this causes Tor peers to not cycle so often, it can be adjusted.

## vtnerd | 2020-12-23T21:16:21+00:00
> I usually get 4-6 i2p inbound connections, but no outbound ,Sometimes see one i2p outbound in "print_cn" and Peer id is "0000000000000000" , and then it will be lost soon.

The incoming `peer_id` over I2P/Tor should always be zeroed (after a recent release) for privacy purposes.

> You can try changing 8 with, say, 5 on this line:

I doubt this timeout is going to make much of a difference. Unless there are more than 120 I2P/Tor connections, this should be a 5 minute timeout, and 2.5 minute timeout otherwise?

## MoneroArbo | 2020-12-23T21:55:22+00:00
Minor point, but Peer ID is 0000000000000000 while handshaking and 0000000000000001 when connected.

Anyway, as noted in #6631, you can temporarily work around this by using --add-priority-node on several i2p peers.

> Unless there are more than 120 I2P/Tor connections, this should be a 5 minute timeout, and 2.5 minute timeout otherwise?

It really seems like there either needs to be a much longer timeout for i2p / tor (after all, these peers aren't relaying blocks or clearnet transactions) or some sort of keep-alive to test for connectivity every so often.

Or, possibly in addition to, it might be good to have logic where monerod tries to always keep at least 1 - 2 active tor / i2p connections if --tx-relay is enabled. Something like if i2p connection count < x then attempt connection to random i2p peer.

Or, what if when monerod receives a transaction over RPC while --tx-relay is enabled, it were to trigger a tor / i2p connection, specifically for the purpose of relaying that transaction? Would add a little delay to i2p transaction propagation, but it seems better than just having the transaction sit in the local tx_pool until a connection happens to become available.

Idk, just spitballing

On related note, if I accidentally send a transaction while there are no i2p peers, I have to manually do relay_tx in monerod to get it to propagate. It doesn't seem to ever get broadcast otherwise. That probably needs to be a separate issue though.

## moneromooo-monero | 2020-12-23T22:56:21+00:00
5 minutes >> 8 is 1 second. They hit this because they're external and many from the same "fake" IP.

## vtnerd | 2020-12-24T22:53:55+00:00
> It really seems like there either needs to be a much longer timeout for i2p / tor (after all, these peers aren't relaying blocks or clearnet transactions) or some sort of keep-alive to test for connectivity every so often.

This assumes a timeout issue being the primary cause. I think some more information may still be needed.

> 5 minutes >> 8 is 1 second. They hit this because they're external and many from the same "fake" IP.

The "real host" (onion address) is used for outgoing, but inbound would be merged to the same host value. This only gets enabled when there are more than 120 connections in the relevant zone though. The timeout is 5 minutes when the zone has fewer than 120 connections. It seems unlikely that people are accepting that many inbound+outbound connections for these privacy networks.

The value should likely be changed anyway since the daemon can be configured into this behavior easily.

## ghost | 2020-12-28T04:40:00+00:00
This issue is especially pronounced in at least two cases:

1. sending time-sensitive transactions—e.g., transactions for XMR.to orders, and
2. remote wallet clients sending transactions through remote RPC nodes that are affected by this issue.

I run a node on a VPS as both my personal remote node and a public remote node. Sending a time-sensitive transaction becomes a nerve-racking affair for me because I do not know whether the transaction would be received by the other party in time. I generally do not have the time to connect to my VPS to check whether my node has made a "suitable outbound" onion connection before I send a transaction. And this outbound onion connection drought can last a long time. Here's a snippet of the log for a recent 12-hour period:

<details>
<summary>Expand</summary>

```
2020-12-27 12:08:09.161	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261300
2020-12-27 12:09:48.632	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261303
2020-12-27 12:11:26.949	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261304
2020-12-27 12:16:41.495	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261306
2020-12-27 12:18:14.644	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261307
2020-12-27 13:02:03.957	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261331
2020-12-27 13:09:02.237	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261334
2020-12-27 13:12:15.918	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261336
2020-12-27 13:22:30.266	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261342
2020-12-27 13:30:48.963	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261345
2020-12-27 13:40:57.786	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261350
2020-12-27 13:46:04.340	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261351
2020-12-27 13:57:49.245	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261355
2020-12-27 14:08:00.614	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261358
2020-12-27 14:50:05.186	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261379
2020-12-27 14:50:06.400	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261379
2020-12-27 14:51:43.508	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261381
2020-12-27 14:53:25.654	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261382
2020-12-27 14:55:07.550	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261383
2020-12-27 14:58:30.480	[P2P4]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261386
2020-12-27 15:00:09.778	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261386
2020-12-27 15:35:28.586	[P2P4]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261410
2020-12-27 15:45:41.098	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261415
2020-12-27 15:52:28.685	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261417
2020-12-27 16:00:55.966	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261418
2020-12-27 16:07:30.731	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261421
2020-12-27 16:24:31.000	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261430
2020-12-27 16:31:07.778	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261432
2020-12-27 16:45:41.126	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261439
2020-12-27 17:06:35.191	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261445
2020-12-27 17:08:11.335	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261447
2020-12-27 17:13:14.501	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261448
2020-12-27 17:16:39.488	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261450
2020-12-27 17:18:18.336	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261451
2020-12-27 17:33:28.238	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261459
2020-12-27 17:50:23.122	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261470
2020-12-27 17:57:15.380	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261473
2020-12-27 18:02:14.685	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261476
2020-12-27 18:10:35.252	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261481
2020-12-27 18:19:01.498	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261486
2020-12-27 18:34:09.219	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261496
2020-12-27 18:37:29.699	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261499
2020-12-27 18:40:59.551	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261500
2020-12-27 18:47:36.024	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261502
2020-12-27 18:54:31.020	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261504
2020-12-27 19:01:06.421	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261509
2020-12-27 19:04:33.641	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261509
2020-12-27 19:08:00.616	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261510
2020-12-27 19:11:21.447	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261513
2020-12-27 19:12:59.041	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261513
2020-12-27 19:14:42.994	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261513
2020-12-27 19:17:54.648	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261513
2020-12-27 19:19:46.472	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261514
2020-12-27 19:21:28.861	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261514
2020-12-27 19:23:02.638	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261514
2020-12-27 19:24:43.116	[P2P4]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261516
2020-12-27 19:26:21.709	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261517
2020-12-27 19:28:07.034	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261518
2020-12-27 19:29:54.507	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261519
2020-12-27 19:31:27.794	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261521
2020-12-27 19:33:16.768	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261522
2020-12-27 19:34:50.387	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261524
2020-12-27 19:38:09.683	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261527
2020-12-27 19:41:37.857	[P2P4]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261529
2020-12-27 19:45:02.161	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261532
2020-12-27 19:46:36.622	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261534
2020-12-27 19:49:55.506	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261539
2020-12-27 20:06:49.247	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261556
2020-12-27 20:33:44.799	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261573
2020-12-27 20:40:30.821	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261575
2020-12-27 20:50:56.676	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261581
2020-12-27 20:52:15.635	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261582
2020-12-27 20:54:03.108	[P2P4]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261582
2020-12-27 20:55:47.340	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261584
2020-12-27 20:57:30.425	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261584
2020-12-27 21:00:42.328	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261587
2020-12-27 21:02:26.270	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261588
2020-12-27 21:04:03.207	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261589
2020-12-27 21:04:05.201	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:343	Unable to send transaction(s) to tor - no available outbound connections
2020-12-27 21:07:30.276	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261591
2020-12-27 21:10:49.173	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261591
2020-12-27 21:12:30.015	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261593
2020-12-27 21:24:17.401	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261600
2020-12-27 21:25:57.959	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261601
2020-12-27 21:27:50.318	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261602
2020-12-27 21:31:02.730	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261606
2020-12-27 21:32:50.180	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261607
2020-12-27 21:34:28.218	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261609
2020-12-27 21:36:14.235	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261609
2020-12-27 21:37:58.141	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261610
2020-12-27 21:39:28.272	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261612
2020-12-27 21:42:55.374	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261613
2020-12-27 21:51:17.773	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261619
2020-12-27 21:52:59.347	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261620
2020-12-27 21:56:17.575	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261623
2020-12-27 21:58:07.187	[P2P4]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261623
2020-12-27 21:59:42.715	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261623
2020-12-27 22:01:19.454	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261624
2020-12-27 22:03:07.454	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261627
2020-12-27 22:04:41.340	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261628
2020-12-27 22:06:33.922	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261628
2020-12-27 22:11:34.448	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261629
2020-12-27 22:13:11.303	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261630
2020-12-27 22:14:54.473	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261632
2020-12-27 22:16:33.799	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261632
2020-12-27 22:18:11.569	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261632
2020-12-27 22:23:15.591	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261634
2020-12-27 22:28:18.464	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261636
2020-12-27 22:40:07.514	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261639
2020-12-27 22:43:29.732	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261641
2020-12-27 22:53:48.176	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261648
2020-12-27 22:55:16.633	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261648
2020-12-27 22:58:47.825	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261652
2020-12-27 23:00:20.224	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261655
2020-12-27 23:02:07.168	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261656
2020-12-27 23:03:42.564	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261656
2020-12-27 23:05:32.641	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261657
2020-12-27 23:08:50.330	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261657
2020-12-27 23:10:28.421	[P2P4]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261657
2020-12-27 23:12:09.818	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261657
2020-12-27 23:14:00.786	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261657
2020-12-27 23:15:32.479	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261657
2020-12-27 23:17:14.241	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261658
2020-12-27 23:20:43.481	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261661
2020-12-27 23:24:01.323	[P2P5]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261663
2020-12-27 23:27:23.079	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261665
2020-12-27 23:28:56.976	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261665
2020-12-27 23:30:39.714	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261666
2020-12-27 23:40:46.172	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261670
2020-12-27 23:54:20.343	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261673
2020-12-28 00:01:01.065	[P2P9]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261677
2020-12-28 00:29:43.874	[P2P3]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261698
2020-12-28 00:58:25.937	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261710
2020-12-28 01:00:06.084	[P2P6]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261711
2020-12-28 01:23:33.834	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261719
2020-12-28 01:25:24.576	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261719
2020-12-28 01:26:58.338	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261720
2020-12-28 01:28:51.425	[P2P8]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261721
2020-12-28 01:30:26.275	[P2P7]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261722
2020-12-28 01:37:13.018	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261725
2020-12-28 01:38:50.243	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261725
2020-12-28 01:40:30.824	[P2P0]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261725
2020-12-28 01:42:09.766	[P2P2]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261725
2020-12-28 01:58:58.653	[P2P1]	WARNING	net.p2p.tx	src/cryptonote_protocol/levin_notify.cpp:681	Unable to send transaction(s) to tor - no suitable outbound connections at height 2261734
```
</details>

I had hoped that #7076 would at least mitigate this issue. It appeared to allow `monerod` to make an outbound connection to an onion peer that already has an inbound connection to it, thereby preserving the number of available onion peers to make outbound connections to. I assume that before #7076, `monerod` would not make an outbound connection to an onion peer that already has an inbound connection to it. But #7076 does not seem to have mitigated or fixed this issue. The log snippet was taken from my `v0.17.1.7-release` node.

Remote wallet clients that send transactions through my node (or other nodes that experience this issue) have it worse. They have no visibility into the connection state of the node that they're connecting to, and are therefore unable to tell whether the node that they've connected to would be able to propagate their transactions or not. They also would be unaware that their transactions are not propagating not because of malicious behavior, but simply because that node could not establish a "suitable outbound" onion connection to propagate their transactions through. I wonder how many support requests concerning non-propagating transactions have this as the actual underlying issue instead of bona fide malicious behavior.

This issue could also be at least partly why there currently remains a lack of available P2P onion nodes. Node operators may be reluctant to set up their nodes as P2P onion nodes because of unreliable onion connection behavior. It is certainly causing me to reconsider whether this unreliability is worth enduring for the sake of added privacy.

Adding priority onion nodes using the `--add-priority-node` option does not mitigate this issue for me. My node would still drop outbound connections to priority onion nodes after five minutes.

I now wonder whether adding the `disable_noise` parameter to the `--tx-proxy` option would mitigate this issue. It seems to me that `monerod` is having trouble establishing outbound onion connections when cycling through the Noise protocol's five-minute windows. I'm currently reluctant to try it, because there may be broader privacy implications that I may not be aware of.

## selsta | 2020-12-28T12:46:21+00:00
#7076 fixed a privacy leak to allowed you to link connections by their peer ID. It did not address the issue with connections getting dropped.

FWIW I added 2 priority peers and also added disable_noise and I consistently had outbound peers in the past weeks. But yea, this issue still needs a proper fix.

## unamefailed | 2020-12-30T00:57:21+00:00
```
snbrpdeug2vuojer6ql6ozcbdzddxbdbi3yiv7avchwnzzocrlaq.b32.i2p:18080  f7d82bf178823abd  normal            0         2263155  0 kB/s, 0 blocks / 0 MB queued
snbrpdeug2vuojer6ql6ozcbdzddxbdbi3yiv7avchwnzzocrlaq.b32.i2p:28082  f7d82bf178823abd  normal            0         2263155  0 kB/s, 0 blocks / 0 MB queued
```
 Different port at the same address ,is this allowed? 

## ghost | 2021-01-04T00:04:00+00:00
My `v0.17.1.8-release` node has had stable outbound onion connections throughout the last four days of being run with the `disable_noise` option enabled. Each transaction sent to my node from my wallet was successfully broadcast to the Monero network within 30 seconds. I set the maximum number of outbound onion connections to `12` and did not add any priority peers, onion or otherwise.

## xanoni | 2021-08-16T03:36:24+00:00
> Different port at the same address ,is this allowed?

Bump, also curious. Doesn't look right to me.

> It really seems like there either needs to be a much longer timeout for i2p / tor (after all, these peers aren't relaying blocks or clearnet transactions) or some sort of keep-alive to test for connectivity every so often.

I assumed that most Tor / I2P nodes were also pushing out & receiving blocks to/from connected nodes via traditional IP ... is this not the case? Are you talking about nodes behind `torsocks`?

Related:[ Discussion around full SOCKS support (PR7616) ](https://github.com/monero-project/monero/pull/7616)

## xanoni | 2021-08-17T23:11:26+00:00
By the way, I have the opposite problem ... >100 outbound connections (mostly to clearnet nodes) but 0 inbound ... maybe someone could look at this ticket and let me know if I screwed up somewhere.

https://github.com/monero-project/monero/issues/7863#issuecomment-900024882

Also, if people could share their (sanitized) `.conf` file, that would be great. See the link above for my settings. Thank you.

## selsta | 2021-10-06T02:23:59+00:00
Closing this, while it still isn't perfect it certainly is less of a problem now that more people run tor / i2p nodes.

## MoneroArbo | 2021-10-06T15:38:35+00:00
Agreed it's better, rarely do I have to rebroadcast a transaction manually nowadays, but my logs still look like this even with four "priority nodes" added:
```

2021-10-05 17:16:54.190 [P2P7]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464467
2021-10-05 17:28:34.525 [P2P8]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464473
2021-10-05 17:36:19.354 [P2P1]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464475
2021-10-05 18:02:43.019 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464487
2021-10-05 18:04:28.403 [P2P5]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464489
2021-10-05 18:19:51.585 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464501
2021-10-05 18:30:05.494 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464503
2021-10-05 18:36:58.135 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464507
2021-10-05 18:52:03.077 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464519
2021-10-05 18:53:02.034 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464521
2021-10-05 18:53:52.617 [P2P3]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464521
2021-10-05 19:05:38.924 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464526
2021-10-05 19:31:25.089 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464541
2021-10-05 19:38:16.151 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464546
2021-10-05 19:41:17.595 [P2P8]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464547
2021-10-05 20:03:49.803 [P2P5]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464554
2021-10-05 20:07:25.531 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464556
2021-10-05 20:12:51.591 [P2P3]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464559
2021-10-05 20:23:31.236 [P2P8]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464568
2021-10-05 20:32:59.977 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464573
2021-10-05 20:58:52.606 [P2P8]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464585
2021-10-05 21:12:19.105 [P2P7]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464590
2021-10-05 21:18:36.876 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464596
2021-10-05 21:50:15.784 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:2074 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2464607
2021-10-05 21:50:15.786 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:2074 id:     <88f9a3fab49996dc5a971457979a05ed3fcebbd09490e707ecdace14d4e19fd0>
2021-10-05 21:50:15.786 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:2074 PoW:    <af5ff07086a0c5e467534754f38029c4f695cfc2fa92af1fdc91a90200000000>
2021-10-05 21:50:15.786 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:2074 difficulty:     343369452284
2021-10-05 22:15:39.475 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464618
2021-10-05 22:47:33.291 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464629
2021-10-05 23:40:05.498 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464651
2021-10-06 00:00:31.512 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464663
2021-10-06 00:10:39.671 [P2P7]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464671
2021-10-06 00:13:57.337 [P2P3]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464672
2021-10-06 00:27:38.767 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464679
2021-10-06 00:36:06.910 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464684
2021-10-06 00:49:41.987 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464690
2021-10-06 00:56:31.255 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464695
2021-10-06 01:19:55.009 [P2P3]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464705
2021-10-06 01:25:22.604 [P2P5]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464709
2021-10-06 01:29:00.337 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464713
2021-10-06 01:42:31.785 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464717
2021-10-06 02:14:35.787 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464733
2021-10-06 02:23:10.459 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464738
2021-10-06 02:44:19.777 [P2P5]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464748
2021-10-06 02:51:02.011 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464750
2021-10-06 03:04:29.181 [P2P5]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464757
2021-10-06 03:11:15.484 [P2P1]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464759
2021-10-06 03:24:50.232 [P2P1]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464765
2021-10-06 03:36:32.501 [P2P3]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464771
2021-10-06 03:46:46.448 [P2P3]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464778
2021-10-06 03:55:11.206 [P2P1]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464782
2021-10-06 04:07:01.581 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464787
2021-10-06 04:18:47.254 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464794
2021-10-06 05:09:38.483 [P2P7]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464812
2021-10-06 05:11:10.157 [P2P7]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464814
2021-10-06 05:14:27.953 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464816
2021-10-06 06:44:36.113 [P2P7]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464865
2021-10-06 06:58:04.166 [P2P1]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464871
2021-10-06 07:26:35.418 [P2P9]  INFO    global  src/cryptonote_core/blockchain.cpp:2074 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2464882
2021-10-06 07:26:35.420 [P2P9]  INFO    global  src/cryptonote_core/blockchain.cpp:2074 id:     <ae9437f15ce1a9692b09b49545f88c0a77451fa8073febdb306d663b0611d975>
2021-10-06 07:26:35.420 [P2P9]  INFO    global  src/cryptonote_core/blockchain.cpp:2074 PoW:    <57cd821170e08d6907768b186a2a82d499d5a56857cfd9719e7c240200000000>
2021-10-06 07:26:35.420 [P2P9]  INFO    global  src/cryptonote_core/blockchain.cpp:2074 difficulty:     334354727767
2021-10-06 07:26:43.367 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464883
2021-10-06 07:45:19.424 [P2P3]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464887
2021-10-06 07:55:28.207 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464890
2021-10-06 08:02:05.942 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464893
2021-10-06 08:17:28.408 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464903
2021-10-06 08:29:07.144 [P2P8]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464908
2021-10-06 08:52:54.371 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464921
2021-10-06 08:59:08.261 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464925
2021-10-06 09:01:27.126 [P2P3]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464925
2021-10-06 09:03:06.697 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464925
2021-10-06 09:06:22.248 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464925
2021-10-06 09:28:25.969 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464936
2021-10-06 09:33:39.122 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464939
2021-10-06 09:55:46.362 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464954
2021-10-06 09:57:22.365 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464955
2021-10-06 10:00:50.634 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464956
2021-10-06 10:10:47.545 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464961
2021-10-06 10:24:25.621 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464966
2021-10-06 10:39:38.168 [P2P7]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464969
2021-10-06 10:43:01.056 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464970
2021-10-06 10:49:48.795 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464971
2021-10-06 11:37:26.195 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464993
2021-10-06 11:52:58.914 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2464999
2021-10-06 12:09:58.810 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465013
2021-10-06 12:15:11.330 [P2P3]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465018
2021-10-06 12:28:32.434 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465025
2021-10-06 12:47:14.214 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465031
2021-10-06 12:55:38.411 [P2P1]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465032
2021-10-06 13:00:44.914 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465034
2021-10-06 13:04:06.391 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465037
2021-10-06 13:26:13.346 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465042
2021-10-06 13:31:10.232 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465045
2021-10-06 13:34:35.617 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465047
2021-10-06 14:08:34.785 [P2P1]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465063
2021-10-06 14:39:01.347 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465080
2021-10-06 14:45:56.282 [P2P9]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465086
2021-10-06 14:49:14.884 [P2P5]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465088
2021-10-06 15:16:21.531 [P2P8]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to i2p - no suitable outbound connections at height 2465096
```

## selsta | 2022-05-06T11:47:51+00:00
@vtnerd It seems that adding `disable_noise` solves this issue with dropping connections.

Someone on IRC reported that they constantly have messages like

```
2022-04-26 17:21:15.654 W Unable to send transaction(s) to tor - no suitable outbound connections at height 2610502
```

even with multiple Tor priority nodes. Adding `disable_noise` solved the issue. I also confirmed this locally, all my nodes with `disable_noise` work, the other ones complain about "no suitable outbound connections".

## trasherdk | 2022-05-08T03:07:36+00:00
And without Tor:
```
version 
0.17.3.2-release
2022-05-08 02:38:32.823   W Unable to send transaction(s), no available connections
2022-05-08 02:38:53.687        W Unable to send transaction(s), no available connections
2022-05-08 02:38:57.079        W Unable to send transaction(s), no available connections
2022-05-08 02:39:17.602        W Unable to send transaction(s), no available connections
2022-05-08 02:40:06.224        W Unable to send transaction(s), no available connections
2022-05-08 02:40:16.958        W Unable to send transaction(s), no available connections
status
Height: 1087915/1087915 (100.0%) on stagenet, not mining, net hash 3.92 kH/s, v14, 3(out)+1(in) connections, uptime 7d 2h 10m 21s
```

## j-berman | 2022-05-15T03:22:18+00:00
Both #8324 and #8330 keep outgoing tor connections alive much longer for me, and drastically reduce the frequency I see "Unable to send transaction(s) to X - no suitable outbound connections at height Y".

The reason I still see the warning at all is not because my node doesn't have any outgoing tor connections, but because every once in a while, all outgoing tor connections' [`m_remote_blockchain_height`](https://github.com/monero-project/monero/blob/9a124f681119855949f6406ecd69c2ad91da9770/src/cryptonote_protocol/levin_notify.cpp#L148) fall behind my node's height (i.e. my node sometimes doesn't know that other outgoing tor connections are fully sync'd at the time this value is checked in memory). However, those connections still seem to be "suitable" to me and are capable of accepting txs. Seems like a racy ordering issue expecting the remote heights to be up to date in that spot. Fully investigating/finding a good solution for how this line is handled I believe should fully solve this warning for tor/i2p daemons correctly. Fetching remote heights from the outgoing connections in that spot seems like one last resort way to handle it, but more investigation needed.

Re-relay logic is also fixed in #8326; I'm hoping needing to manually re-relay or flush & re-submit even on rare occasion will soon be a thing of the past.

Not sure what would be causing the non-tor/i2p `Unable to send transaction(s), no available connections` warning. Haven't dug into that

## deutrino | 2022-06-10T02:38:51+00:00
FWIW, I have found that vetting about 6 to 8 .onion nodes on various node lists for relatively good uptime and longevity, and using them with ```add-priority-node```, did vastly decrease the amount of ```Unable to send transaction(s), no available connections``` messages in the logs, without using ```disable-noise```. Adding 6 got the level down to a handful a day, and a couple more did reduce it further but not to zero.

## selsta | 2022-06-10T03:57:00+00:00
@deutrino Are you running master branch? That alone should vastly reduce the amount of times this message shows up, all without setting any priority nodes.

## deutrino | 2022-06-10T17:35:45+00:00
@selsta No, thank you for mentioning, I thought about this as I was going to sleep. I mostly just posted my experience in case people running stable find this thread before the next release is out - the ```add-priority-node``` works fairly well, you just have to add enough reliable nodes.

I'm running latest stable, have not yet built monerod from source, but I suppose this is as good a reason as any to start! I'm planning to try it this weekend. :smile: 

## selsta | 2022-07-20T22:57:49+00:00
v0.18.0.0 significantly improved Tor / I2P connectivity.

# Action History
- Created by: selsta | 2020-10-26T20:51:06+00:00
- Closed at: 2022-07-20T22:57:49+00:00
