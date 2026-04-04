---
title: 'Can''t create transaction: no connection to daemon. Please make sure daemon
  is running'
source_url: https://github.com/monero-project/monero-gui/issues/1412
author: Tendancy
assignees: []
labels:
- resolved
created_at: '2018-05-14T14:29:38+00:00'
updated_at: '2019-07-04T12:29:46+00:00'
type: issue
status: closed
closed_at: '2019-07-04T12:27:45+00:00'
---

# Original Description
I'm have been trying to send a payment but received  this message

"Can't create transaction: internal error: No unlocked balance in the specified subaddress(es)"

In the main send screen of my Monero GUI wallet for Mac it displays that I have both a balance and an identical unlocked balance. 

I have tried again to send again a few times since and now get a different message, "Can't create transaction: no connection to daemon. Please make sure daemon is running."

I can clearly see that the network status is connected, -  wallet is synchronised, daemon is synchronised. 

Below from Level 2 log as I try to make transaction... Thanks for your help

2018-05-14 14:26:19.937	  0x7fffc0bad3c0	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-14 14:26:51.997	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242002/1572621[0m
2018-05-14 14:26:56.026	  0x7fffc0bad3c0	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Height: 1572622/1572622 (100.0%) on mainnet, bootstrapping from node.moneroworld.com:18089, local height: 1242002 (79.0%), not mining, net hash 424.96 MH/s, v7, up to date, 168(out)+55(in) connections, uptime 3d 10h 59m 35s
2018-05-14 14:27:03.616	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242022/1572621[0m
2018-05-14 14:27:15.960	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242042/1572622[0m
2018-05-14 14:27:26.446	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242062/1572622[0m
2018-05-14 14:27:38.126	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242082/1572622[0m
2018-05-14 14:27:52.401	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242102/1572622[0m
2018-05-14 14:28:02.610	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242122/1572623[0m
2018-05-14 14:28:12.981	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242142/1572623[0m
2018-05-14 14:28:25.132	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242162/1572623[0m
2018-05-14 14:28:40.101	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242182/1572623[0m
2018-05-14 14:28:54.900	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242202/1572623[0m
2018-05-14 14:29:09.409	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242222/1572623[0m
2018-05-14 14:29:25.873	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[167.99.171.68:18080 OUT]  Synced 1242242/1572623[0m

# Discussion History
## pazos | 2018-05-15T15:48:05+00:00
```
Height: 1572622/1572622 (100.0%) on mainnet, bootstrapping from node.moneroworld.com:18089,
local height: 1242002 (79.0%), not mining, net hash 424.96 MH/s, v7, up to date, 168(out)+55(in)
connections, uptime 3d 10h 59m 35s
```

You are connected to a remote node while downloading the blockchain. Is that intended?

## Tendancy | 2018-05-16T18:38:14+00:00
Are you sure? When I check my monero GUI it says I am connected to a local node.
Is this liable to effect why I can't send a transaction? I have now received the same message several times, "Can't create transaction: no connection to daemon. Please make sure daemon is running."

Yet each time I can clearly see that the network status is connected, - wallet is synchronised, daemon is synchronised??? 

## stoffu | 2018-05-17T05:11:07+00:00
You're using a feature called "[daemon bootstrapping](https://github.com/monero-project/monero-gui/pull/1091)" where your local node acts as a pipe to a remote node while the synchronization is not finished. The wallet shows the status as "connected", but it doesn't mean that the local daemon is fully synced and ready to serve the wallet. Admittedly, this display is very confusing and needs to be improved in the future. I think the cause of your error is the remote node node.moneroworld.com:18089 being busy and not responding.

You can either specify a different remote node as the bootstrap node or stop using the bootstrapping feature and simply wait for the local daemon to finish syncing.


## Tendancy | 2018-05-17T20:12:51+00:00
Thanks stoffu... I've read your link to daemon bootstraping, a few  further questions,
 1 - can you recommend a different and safe/reliable remote node that I could use?
2 - how long do local daemons typically take to sync? wallet downloaded nearly 2 weeks ago!
3 - any idea about the original message I got which was "Can't create transaction: internal error: No unlocked balance in the specified subaddress(es)"?

I appreciate your help 

## stoffu | 2018-05-17T21:46:01+00:00
1. No.

2. Depends on many factors. It’s a lot slower if your storage is a spinning disk.

3. Not sure, but probably because your node isn’t fully synced.

## dEBRUYNE-1 | 2019-07-04T06:39:29+00:00
@Tendancy - Do you still incur similar issues with GUI v0.14.1.0? 



## Tendancy | 2019-07-04T12:10:56+00:00
 Sorry bud, haven't used for a while
    On Thursday, 4 July 2019, 07:39:35 BST, dEBRUYNE-1 <notifications@github.com> wrote:  
 
 
@Tendancy - Do you still incur similar issues with GUI v0.14.1.0?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub, or mute the thread.
  

## dEBRUYNE-1 | 2019-07-04T12:24:44+00:00
@Tendancy - I am going to close this issue then. In case you'd like to try GUI v0.14.1.0, you can find it here:

https://www.reddit.com/r/Monero/comments/c8eg6k/gui_v01410_boron_butterfly_with_ledger_nano_x_and/

## dEBRUYNE-1 | 2019-07-04T12:24:48+00:00
+resolved

## Tendancy | 2019-07-04T12:29:46+00:00
 Ok thanks for your efforts
    On Thursday, 4 July 2019, 13:24:52 BST, dEBRUYNE-1 <notifications@github.com> wrote:  
 
 
@Tendancy - I am going to close this issue then. In case you'd like to try GUI v0.14.1.0, you can find it here:

https://www.reddit.com/r/Monero/comments/c8eg6k/gui_v01410_boron_butterfly_with_ledger_nano_x_and/

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub, or mute the thread.
  

# Action History
- Created by: Tendancy | 2018-05-14T14:29:38+00:00
- Closed at: 2019-07-04T12:27:45+00:00
