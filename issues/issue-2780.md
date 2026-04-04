---
title: Synchronization error
source_url: https://github.com/monero-project/monero/issues/2780
author: OlegFisher
assignees: []
labels:
- invalid
created_at: '2017-11-08T20:40:51+00:00'
updated_at: '2017-11-23T11:54:28+00:00'
type: issue
status: closed
closed_at: '2017-11-09T21:32:24+00:00'
---

# Original Description
Hey,
I'm developing new NodeJS wallet for Monero. And I'm totally stuck on this issue.

I've forked from Monero an I'm trying to launch using my own seed nodes and my own network(I've deleted checkpoints as well). I've launched two seed servers and they have synchronized to each other.  Even after mining they were synchronized on height 785.

I've erased data-folder .bytemonero on one server and next time I tried to launch I've got this message:

**set_log 2**
```
2017-11-08 15:39:19.337	[P2P7]	DEBUG	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#2089 to 52.0.46.102
2017-11-08 15:39:19.394	[P2P0]	DEBUG	net	contrib/epee/include/net/levin_protocol_handler_async.h:401	[52.0.46.102:19236 OUT] LEVIN_PACKET_RECIEVED. [len=29, flags2, r?=0, cmd = 1007, v=1
2017-11-08 15:39:19.499	[P2P2]	DEBUG	net	contrib/epee/include/net/levin_protocol_handler_async.h:401	[52.0.46.102:19236 OUT] LEVIN_PACKET_RECIEVED. [len=25222, flags1, r?=0, cmd = 2007, v=1
2017-11-08 15:39:19.499	[P2P2]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1569	[52.0.46.102:19236 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=785, m_start_height=0, m_total_height=785
2017-11-08 15:39:19.499	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3770	Blocks 0 - 784 start at 0 and end at 3
2017-11-08 15:39:19.500	[P2P2]	WARN 	blockchain	src/cryptonote_core/blockchain.cpp:3824	invalid hash for blocks 0 - 255
2017-11-08 15:39:19.500	[P2P2]	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:3845	usable: 0 / 785
2017-11-08 15:39:19.500	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1592	[52.0.46.102:19236 OUT] Peer yielded no usable blocks, dropping connection
```

**sync_info from main server**
```
Height: 785, target: 785 (100%)
Downloading at 0 kB/s
0 peers
0 spans, 0 MB
```
**sync_info from second one**

```
Height: 1, target: 1 (100%)
Downloading at 0 kB/s
0 peers
0 spans, 0 MB
```

I tried to copy data from original data folder and it worked. But after I launch new not  peer it shows the same error. 

When I try to mine on synchronized peer, it works on the main server I got

```
2017-11-08 16:02:05.057	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1452	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1
id:	<c1068f4309e9e8bc7475d46175c67b773dfd4e7fc15775d8decb3f99975cfd31>
PoW:	<a57646c3831085c376dbb34f3750c3d5fc1e484361e090c1c83b404dda1a37a2>
difficulty:	1
2017-11-08 16:02:05.082	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1452	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2
id:	<37a0a02866b9228a61ea98decdb4eec0d2833eddf863b083123b2469e6532cdb>
PoW:	<d3348f15a7c2d9e634ffabccb6cb2c3c428bd25bfed6cccfab3f1f643887341a>
difficulty:	1
2017-11-08 16:02:05.106	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1452	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3
id:	<553a9c36ac484372c04300a044ee674f633c9ade29832416bb10d4fad4c38cb8>
PoW:	<c7df560e4a5c57895b50ca88f7fa2ab19bde023dd4bd16825358e92334788302>
difficulty:	60
2017-11-08 16:02:05.131	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1452	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 4
id:	<2183c048875dfc450c1cfc2b7c8233cb3a5032f4ee47eb4fd5568b8c55a8b961>
PoW:	<1ee575214278dd97461579d19e3c39d4cc683a7d33e476d359132aa06fce0d00>
difficulty:	3660
2017-11-08 16:02:05.156	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1452	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 5
id:	<ef22d4d621bd7952969f796b9ca5c7c3be998f1aab65b55cf9daef63079bb68b>
PoW:	<5647b655e9dfaf02f46558e66a569df96f9bd444207ca2391a0b6524ccd40400>
```
 

Best,
Oleg.


# Discussion History
## moneromooo-monero | 2017-11-08T20:58:22+00:00
That sounds like a really complicated to do things and waste your time. Syncing the whole chain should not take that much time. And in any case, using testnet will only get a 3.5 GB blockchain (as opposed to something like 30 GB).


## HalykCoin | 2017-11-09T18:29:40+00:00
> That sounds like a really complicated to do things
Thank you for the answer, I really happy to get at least some information. 

Actually I found the reason of this exception. Monero stores cache of all checkpoints in **checkpoints.dat**, so it checks hash of hashes of blocks during synchronization in step of every 255 blocks.

I would be very happy if you disclose me practical or philosophical background of this implementation. Because I haven's seen such things in other crypto-currencies like bitcoin.

Thank you in advance,
Best Regards,
Oleg.

## moneromooo-monero | 2017-11-09T20:41:54+00:00
It's just a way to speedup verification.

## moneromooo-monero | 2017-11-09T21:29:40+00:00
This doesn't appear to be a bug, since you mined new blocks, so closing.

+invalid


## OlegFisher | 2017-11-23T11:54:28+00:00
Thank you for the answer! 

# Action History
- Created by: OlegFisher | 2017-11-08T20:40:51+00:00
- Closed at: 2017-11-09T21:32:24+00:00
