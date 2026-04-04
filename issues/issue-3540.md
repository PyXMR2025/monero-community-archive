---
title: 'Assertion failed: Connection reset by peer (../zeromq-4.2.3/src/signaler.cpp:357)'
source_url: https://github.com/monero-project/monero/issues/3540
author: mmortal03
assignees: []
labels: []
created_at: '2018-04-02T16:58:49+00:00'
updated_at: '2021-12-08T23:40:27+00:00'
type: issue
status: closed
closed_at: '2021-10-25T23:59:03+00:00'
---

# Original Description
Trying out the 0.12.0.0 official binaries from monero-win-x64-v0.12.0.0.zip on GitHub. After some syncing, I got the following messages and then the monerod process crashed, on Windows 10 64-bit:

> Assertion failed: Connection reset by peer (../zeromq-4.2.3/src/signaler.cpp:357)
> Assertion failed: Connection reset by peer (../zeromq-4.2.3/src/signaler.cpp:357)
> Assertion failed: Connection reset by peer (../zeromq-4.2.3/src/signaler.cpp:357)

I wasn't logging anything, so I've got nothing else to report on this at the present. Might be something with ZeroMQ, but might be coincidental. I'll report back if I continue to see it.

# Discussion History
## mmortal03 | 2018-04-03T18:45:51+00:00
The same thing just happened again. Time to turn on logging.

## mmortal03 | 2018-04-04T12:29:46+00:00
I'm working on trying to reproduce this issue while logging at higher levels of granularity. At the default level of logging, the assertion failed errors don't even make it into the log file, for whatever reason. We've had some power outages in the area lately (but I'm running with a battery backup), so I thought it might be caused by the Internet connection dropping while the daemon is running. So, I tried yanking the Ethernet cable, but no immediate crash following that, so, still trying to determine what specifically is causing it AND get enough granularity on the log.

## mmortal03 | 2018-04-04T15:46:17+00:00
Just crashed again, here's a snippet of log level 2 just before the crash, but nothing about ZeroMQ in the console this time, so that could be a coincidence, and nothing obviously wrong here: 

`2018-04-04 15:28:49.226	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-04-04 15:28:49.226	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     60427042816
2018-04-04 15:28:49.226	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      48611799040
2018-04-04 15:28:49.226	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 11815243776
2018-04-04 15:28:49.226	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-04-04 15:28:49.226	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.8045  Percent threshold: 0.8000
2018-04-04 15:28:49.226	[P2P8]	DEBUG	cn.block_queue	src/cryptonote_protocol/cryptonote_protocol_handler.h:164	[76.102.30.200:18080 OUT] post relay N10cryptonote23NOTIFY_NEW_TRANSACTIONSE -->
2018-04-04 15:28:49.226	[P2P8]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:521	do_send() NOW just queues: packet=33 B, is added to queue-size=28
2018-04-04 15:28:49.226	[P2P8]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:521	do_send() NOW just queues: packet=13077 B, is added to queue-size=29
2018-04-04 15:28:49.242	[P2P8]	DEBUG	net	contrib/epee/include/net/levin_protocol_handler_async.h:717	[138.197.218.239:18080 OUT] LEVIN_PACKET_SENT. [len=13077, f=1, r?=0, cmd = 2002, ver=1
2018-04-04 15:28:49.242	[P2P8]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:536	do_send() NOW SENSD: packet=33 B
2018-04-04 15:28:49.242	[P2P8]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:521	do_send() NOW just queues: packet=13077 B, is added to queue-size=2
2018-04-04 15:28:49.242	[P2P8]	DEBUG	net	contrib/epee/include/net/levin_protocol_handler_async.h:717	[138.68.62.133:18080 OUT] LEVIN_PACKET_SENT. [len=13077, f=1, r?=0, cmd = 2002, ver=1
2018-04-04 15:28:49.242	[P2P8]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:521	do_send() NOW just queues: packet=33 B, is added to queue-size=44
2018-04-04 15:28:49.242	[P2P8]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:521	do_send() NOW just queues: packet=13077 B, is added to queue-size=45
2018-04-04 15:28:49.242	[P2P8]	DEBUG	net	contrib/epee/include/net/levin_protocol_handler_async.h:717	[37.59.97.202:18080 OUT] LEVIN_PACKET_SENT. [len=13077, f=1, r?=0, cmd = 2002, ver=1
2018-04-04 15:28:49.242	[P2P8]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:521	do_send() NOW just queues: packet=33 B, is added to queue-size=38
2018-04-04 15:28:49.242	[P2P8]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:521	do_send() NOW just queues: packet=13077 B, is added to queue-size=39
2018-04-04 15:28:49.242	[P2P8]	DEBUG	net	contrib/epee/include/net/levin_protocol_handler_async.h:717	[63.225.95.170:18080 OUT] LEVIN_PACKET_SENT. [len=13077, f=1, r?=0, cmd = 2002, ver=1
2018-04-04 15:28:49.305	[P2P8]	DEBUG	net	contrib/epee/include/net/levin_protocol_handler_async.h:414	[138.68.62.133:18080 OUT] LEVIN_PACKET_RECIEVED. [len=13077, flags1, r?=0, cmd = 2002, v=1
2018-04-04 15:28:49.305	[P2P8]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[138.68.62.133:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-04 15:28:49.305	[P2P8]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:738	tx <74851fabfe151b605d4421f25e2a1800c17e1750fa41c3d3d1a662c057a753ce>already have transaction in tx_pool
2018-04-04 15:28:49.305	[P2P8]	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:1032	tx <74851fabfe151b605d4421f25e2a1800c17e1750fa41c3d3d1a662c057a753ce>already have transaction in tx_pool`

## moneromooo-monero | 2018-04-04T16:03:25+00:00
Those assertion failures don't get into the log because it's the 0mq code printing those.

## mmortal03 | 2018-04-04T17:17:47+00:00
Here's what the Windows application log says: 

Faulting application name: monerod.exe, version: 0.0.0.0, time stamp: 0x5aba638b
Faulting module name: KERNELBASE.dll, version: 10.0.16299.248, time stamp: 0x4414ec23
Exception code: 0x40000015
Fault offset: 0x0000000000014008
Faulting process id: 0x1d4c
Faulting application start time: 0x01d3cc18c50034de
Faulting application path: C:\Users\mmortal03\Desktop\Monero_new\monerod.exe
Faulting module path: C:\WINDOWS\System32\KERNELBASE.dll
Report Id: 0cfdd73c-c83c-4682-86bc-206ac925099a
Faulting package full name: 
Faulting package-relative application ID: 

## mmortal03 | 2018-04-26T02:19:01+00:00
I've been commenting about this issue over on another bug thread, but here's the latest info:

Using gdb, it looks like the issue starts at line 46 of daemon/main.cpp, which is the include for "blockchain_db/db_types.h". I don't know how helpful that is.

I tried to do a backtrace, but it says:
```
#0  0x00007ffc37984008 in RaiseException ()
   from C:\WINDOWS\System32\KernelBase.dll
#1  0x0000000000f3ed64 in ?? ()
Backtrace stopped: previous frame inner to this frame (corrupt stack?)
```

## dEBRUYNE-1 | 2018-04-28T14:42:47+00:00
For visibility purposes, someone else affected by the same issue:

https://www.reddit.com/r/Monero/comments/89nofd/monero_gui_01200_lithium_luna_megathread_download/dxhk89e/

## mmortal03 | 2018-04-28T19:09:30+00:00
@dEBRUYNE-1 , I'm able to consistently reproduce it on one machine, but haven't been able to reproduce it on a different machine, using the *same* source blockchain files, which could mean that it may not be anything corrupt in the copy of the blockchain, but something specific to the hardware of the machines. (I will continue to try to reproduce it on other machines in the next few days.)

Off the top of my head, specs that might matter are the differing processors -- the machine with the issue is an AMD E-350 (Windows 10 64-bit, 6GB RAM), whereas one that I haven't yet reproduced it on is an Intel i7-3635QM (Windows 10 64-bit, 8GB RAM).

## mmortal03 | 2018-05-01T09:41:05+00:00
The other user that's experiencing this that was on Reddit states that his CPU is an Intel Core 2 Quad Q9550, so that strikes down the idea that it's some sort of Intel versus AMD processor issue. It was a shot in the dark by me.

## mmortal03 | 2018-05-02T21:29:14+00:00
I may have found the cause and a workaround. 

Last night, I coincidentally discovered that my network monitoring utility, NetWorx, was acting up and affecting another application, so I closed it, and thought to run the Monero daemon to see if it might've also been interfering with it. *It ran all night without crashing.* 

I've since come across the following, where someone mentions at the bottom of the thread that NetWorx was causing this same error in a different program, where it was also somehow interfering with ZeroMQ. I don't know why this would be, and it still isn't a fix, as I'd like to be able to continue to monitor my network bandwidth usage with NetWorx while using the latest version of monero, but at least this is an area for further investigation: 
https://stackoverflow.com/questions/46623548/jupyter-notebook-python-crash-on-windows-10

## mmortal03 | 2018-05-02T21:32:33+00:00
Also, see here, it may have to do with a TDI or WFP filter driver being used by NetWorx and other programs: https://github.com/Microsoft/WSL/issues/1554#issuecomment-339743927

They're saying that the Windows Insider preview build 17046 may contain a workaround for developers for the TDI driver, which would probably arrive in the Windows 10 April 2018 Update (already in the Insider preview), but I don't really see it as a fix, which may need to come in zeromq itself.

## mmortal03 | 2018-05-02T22:41:36+00:00
Also, see here: https://github.com/zeromq/libzmq/issues/1808

## mmortal03 | 2018-05-03T03:24:49+00:00
The other user on Reddit was also using NetWorx. This seems very likely to be the trigger. Hopefully, we can get some sort of fix in the zeromq libraries for this.

## moneromooo-monero | 2018-10-25T10:09:55+00:00
Since it seems to be due to some network software breaking connections, it seems unrelated to monero and I'll close this. Seems OK ?

## mmortal03 | 2018-10-26T00:03:24+00:00
Yeah, I'll close it. It's also going to take a while to get fixed on zeromq. I don't know that there's anything that Monero could do to work around it.

## mmortal03 | 2019-12-07T16:44:20+00:00
@moneromooo-monero, this is finally said to be fixed as of yesterday in zeromq: https://github.com/zeromq/libzmq/issues/1808

Is @luigi1111 the one handling Monero builds currently? Just wanted to give people a heads up. Whenever this fix gets into the zeromq release channel, I'll be interested to test it in Monero. I'll keep tabs on this and follow-up.

## mmortal03 | 2021-10-10T06:15:25+00:00
@luigi1111 , I thought I'd come back and test this issue, as it's been a few years, and I can still reproduce the crashing with the latest version of monero. The bug was supposedly fixed in zeromq, but I have no idea what version of the zeromq libraries is currently being used in monero to rule out old libraries.

## selsta | 2021-10-10T09:27:58+00:00
We still use v4.1.7 for zeromq for release binaries. I can update it to the latest version for the next release.

## mmortal03 | 2021-12-08T03:35:21+00:00
@selsta , did this make it into v0.17.3.0? I'm testing it, and, unfortunately, still seeing the associated crashing, so I just wanted to make sure.

## selsta | 2021-12-08T03:37:25+00:00
@mmortal03 Yes. Did you download the binary from getmonero.org?

## mmortal03 | 2021-12-08T03:47:34+00:00
Yep, monero-win-x64-v0.17.3.0.zip. I'll have to see if I can get a screen capture of the last screen output before it crashes, as I don't believe the log, at any granularity, has ever captured these errors. 
I don't believe this is technically a bug in Monero, it's a bug in zeromq, but it's frustrating that the supposed fix in zeromq has not resolved things here.

## selsta | 2021-12-08T15:42:36+00:00
I'm out of ideas regarding this issue, we definitely used 4.3.4 in v0.17.3.0: https://github.com/monero-project/monero/blob/v0.17.3.0/contrib/depends/packages/zeromq.mk#L2

## mmortal03 | 2021-12-08T23:40:27+00:00
Thanks, no worries. Once I have more evidence, I'm going to post to the zeromq thread about it.

# Action History
- Created by: mmortal03 | 2018-04-02T16:58:49+00:00
- Closed at: 2021-10-25T23:59:03+00:00
