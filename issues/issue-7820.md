---
title: Errors in monero full node
source_url: https://github.com/monero-project/monero/issues/7820
author: wpbloger
assignees: []
labels: []
created_at: '2021-07-29T17:48:22+00:00'
updated_at: '2021-07-30T10:41:45+00:00'
type: issue
status: closed
closed_at: '2021-07-30T10:41:44+00:00'
---

# Original Description
Recently I decided to mine Monero on my own and for this I installed a Full node with all blockchain.
To install the node, I used a local computer with os: Ubuntu 20.04.2 LTS with an xeon e5 2678 v3 processor and a 1 TB SSD NVME.
I have fast Internet and synchronization was successful in a day, the full node was ready with the daemon.
In addition, I downloaded and installed GUI Wallet on the same computer, which started quite successfully and synchronized with the daemon. The block height matches.
The node was compiled and installed as described in the instructions in the Monero repository. 
After that, I installed xmrig-proxy for myself in order to be able to reduce the complexity of the ball for work machines, and on work machines I installed xmrig, where I inserted the wallet obtained in my GUI Wallet and started mining.
The time on the computer where the node is installed is set to the UTC time zone.
xmrig-proxy receives valid shares and does not display errors. 
I start the monerod daemon with the following config file(bitmonero.conf): 
```
add-priority-node=opennode.xmr-tw.org:18080
add-priority-node=node.moneroworld.com:18080
add-priority-node=uwillrunanodesoon.moneroworld.com:18080
add-priority-node=nodes.hashvault.pro:18080
add-priority-node=node.supportxmr.com:18080
out-peers=512
in-peers=512
public-node=1
rpc-restricted-bind-ip=0.0.0.0
rpc-restricted-bind-port=18089
confirm-external-bind=1
rpc-bind-ip=127.0.0.1
rpc-bind-port=18081
prune-blockchain=false
limit-rate-up=20970
limit-rate-down=20970
enable-dns-blocklist=true
```

However, after a few days, the following errors began to appear in the console: 
```
2021-07-28 13:03:49.344	W ge_frombytes_vartime failed at 380
2021-07-28 13:03:49.354	E Exception at [core::handle_incoming_txs()], what=ge_frombytes_vartime failed at 380

2021-07-20 08:30:53.042	E Verification failure
```
Same errors on log:
```
WARNING	ringct	src/ringct/rctOps.cpp:415	ge_frombytes_vartime failed at 415
2021-07-17 01:50:02.712	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2021-07-17 01:50:02.712	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2021-07-17 01:50:02.720	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x113) [0x55ce2977aa4a]:__cxa_throw+0x113) [0x55ce2977aa4a]
2021-07-17 01:50:02.720	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x353eb4) [0x55ce297b3eb4] 
2021-07-17 01:50:02.720	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x2681) [0x55ce29df6221]:_ZN3rct18bulletproof_VERIFYERKSt6vectorIPKNS_11BulletproofESaIS3_EE+0x2681) [0x55ce29df6221]
2021-07-17 01:50:02.720	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0xd) [0x55ce29d6533d]:_ZN3rct14verBulletproofERKSt6vectorIPKNS_11BulletproofESaIS3_EE+0xd) [0x55ce29d6533d]
2021-07-17 01:50:02.720	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xed4) [0x55ce29d79bb4]:_ZN3rct21verRctSemanticsSimpleERKSt6vectorIPKNS_6rctSigESaIS3_EE+0xed4) [0x55ce29d79bb4]
2021-07-17 01:50:02.720	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x6a2) 


WARNING	ringct	src/ringct/rctOps.cpp:380	ge_frombytes_vartime failed at 380
2021-07-28 13:03:49.345	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2021-07-28 13:03:49.345	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2021-07-28 13:03:49.352	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x113) [0x560e27da5a4a]:__cxa_throw+0x113) [0x560e27da5a4a]
2021-07-28 13:03:49.352	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x353bca) [0x560e27ddebca] 
2021-07-28 13:03:49.352	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x247) [0x560e28227997]:_ZNK10cryptonote4core32check_tx_inputs_keyimages_domainERKNS_11transactionE+0x247) [0x560e28227997]
2021-07-28 13:03:49.352	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0xd63) [0x560e2822c153]:_ZNK10cryptonote4core17check_tx_semanticERKNS_11transactionEb+0xd63) [0x560e2822c153]
2021-07-28 13:03:49.352	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xbd) 

2021-07-20 08:30:53.042	[P2P8]	ERROR	bulletproofs	src/ringct/bulletproofs.cc:1075	Verification failure
2021-07-20 08:32:43.056	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2021-07-20 08:32:43.056	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2021-07-20 08:32:43.061	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x113) [0x55ce2977aa4a]:__cxa_throw+0x113) [0x55ce2977aa4a]
2021-07-20 08:32:43.061	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x16c) 
```
I also started receiving messages like this: 
`There were 0 blocks in the last 20 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.`
But I have everything in order with the Internet connection, and there is a peers connections.

Why are these errors and how can I fix them?
Maybe because of them I can't find the block for a long time or am I just unlucky? 

# Discussion History
## selsta | 2021-07-29T17:51:40+00:00
These errors show up from time to time. It means a transaction didn't verify. It isn't related to mining.

> Maybe because of them I can't find the block for a long time or am I just unlucky?

What's your hashrate?

> There were 0 blocks in the last 20 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.

It means, as it says in the message that there were no blocks for 20 minutes. It can happen from time to time. If you are on the same height as e.g. xmrchain.net then everything is okay. See also: https://melo.tools/blocks/frequencies/

## wpbloger | 2021-07-29T17:58:08+00:00
> These errors show up from time to time. It means a transaction didn't verify. It isn't related to mining.

Are such mistakes in the nature of things?
I thought they might be the reason for my bad luck, especially verification failure

> What's your hashrate?

In general, my hashrate is 100-120 kH / s and about 30-40 days I'm trying to get a block, the console writes about alternative blocks every day, but there are no solutions ( 

## selsta | 2021-07-29T18:06:40+00:00
> Are such mistakes in the nature of things?

My daemon shows this also occasionally and I don't mine. It isn't related.

> In general, my hashrate is 100-120 kH / s and about 30-40 days I'm trying to get a block

`At 100000 h/s with network diff of 3.10e+11 your expected time for find a block is 3.10e+06 s or 35.88 days.`

You are still within the average time to find a block.

## moneromooo-monero | 2021-07-29T18:35:24+00:00
100 kH/s is one hell of a high hash rate. Are you sure ?

## wpbloger | 2021-07-29T18:48:52+00:00
> 100 kH/s is one hell of a high hash rate. Are you sure ?

Yes, of course, I have 12 cpu 2678v3 and 3 cpu 5900, but apparently this is not enough to get a block in a month.
Now I'm trying to find out if everything is in order in the node and if it is working properly. 

## moneromooo-monero | 2021-07-29T19:27:17+00:00
If your chain is increasing at an average of a block every two minutes, you're almost certainly all good.

## wpbloger | 2021-07-29T19:35:08+00:00
> If your chain is increasing at an average of a block every two minutes, you're almost certainly all good.

Yes, the chain grows, alternative blocks are added, the reorganization takes place.
But I am worried about the errors that appear, I posted them in the thread, @selsta writes that they are not important for mining, can anyone else come across specific errors who is the miner?

## moneromooo-monero | 2021-07-29T20:13:28+00:00
Are these errors showing up on default log settings ?

## wpbloger | 2021-07-29T20:22:05+00:00
> Are these errors showing up on default log settings ?

Yes, I have not changed the log level settings.
Output of the command set_log:
`Log categories are now *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO`

## moneromooo-monero | 2021-07-29T20:25:24+00:00
After checking, core::handle_incoming_txs means a tx you received was invalid wrt your chain. Not a tx you mined. So ignore.

## moneromooo-monero | 2021-07-29T20:26:36+00:00
Oh, if you want to double check:
Restart monerod with --fixed-difficulty 1. Mine again. You'll find lots of blocks fast.
Then restart without that option, and those fake blocks will get dumped and you'll get back on the correct chain.
If you can't find blocks with  --fixed-difficulty 1 then something is indeed wrong somewhere.


## wpbloger | 2021-07-30T10:41:44+00:00
I tried to set a fixed difficulty, at first there were many errors about not found transactions, then a lot of messages about finding alternative blocks went, and even the balance in the goo wallet was updated, it became equal to 2.7 XMR, which means the blocks were found.
After restarting the node without a fixed complexity, the node reorganized the chain and the balance on the wallet became correct.
It looks like the node is working, it seems that I just had no luck yet, thanks to everyone for taking part in solving my problem. 

# Action History
- Created by: wpbloger | 2021-07-29T17:48:22+00:00
- Closed at: 2021-07-30T10:41:44+00:00
