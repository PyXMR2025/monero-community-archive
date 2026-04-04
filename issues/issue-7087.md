---
title: Monerod and GUI monero not synced?
source_url: https://github.com/monero-project/monero/issues/7087
author: IndustrialOne
assignees: []
labels: []
created_at: '2020-12-06T11:51:11+00:00'
updated_at: '2022-07-19T19:59:03+00:00'
type: issue
status: closed
closed_at: '2022-07-19T19:59:03+00:00'
---

# Original Description
Apologies if this is a dumb question but I just FINALLY finished syncing the blockchain and notice GUI Monero says I am disconnected from the network even though I'm not. Monerod is operational, GUI Monero started it after all and the log page confirms it is working.

Mining doesn't work because it thinks I am disconnected. What am I doing wrong? Should I turn the prune off from the custom commandline or something now that I'm done syncing?

# Discussion History
## moneromooo-monero | 2020-12-07T01:09:28+00:00
Does monero-wallet-cli think you're disconnected also ?

## IndustrialOne | 2020-12-07T13:12:13+00:00
It doesn't appear so, it just asked me if I wanted to turn background mining on so I did and it said it did a network refresh of all the blocks.

________________________________
From: moneromooo-monero <notifications@github.com>
Sent: Sunday, December 6, 2020 6:09 PM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


Does monero-wallet-cli think you're disconnected also ?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-739606517>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4S3NSD4LTAR2ME57XTSTQTNJANCNFSM4UPIOBYQ>.


## IndustrialOne | 2020-12-07T13:21:49+00:00
Wait a minute, the log says mining is turned on but not started. monero-wallet-cli also says my wallet is out of sync with the network despite monerod saying I'm perfectly synced. I am so confused.

________________________________
From: moneromooo-monero <notifications@github.com>
Sent: Sunday, December 6, 2020 6:09 PM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


Does monero-wallet-cli think you're disconnected also ?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-739606517>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4S3NSD4LTAR2ME57XTSTQTNJANCNFSM4UPIOBYQ>.


## moneromooo-monero | 2020-12-08T15:34:35+00:00
Post the actual message.

## IndustrialOne | 2020-12-08T17:53:36+00:00
https://pasteboard.co/JE0lBmw.png

Daemon log:
2020-12-08 17:44:19.848 [miner 0] INFO global src/cryptonote_basic/miner.cpp:548 background mining is enabled, but not started, waiting until start triggers
2020-12-08 17:44:30.365 [P2P2] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:1600 Synced 2247822/2247822
2020-12-08 17:44:30.366 [P2P2] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318 SYNCHRONIZED OK
2020-12-08 17:45:05.048 [P2P3] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318 SYNCHRONIZED OK
2020-12-08 17:45:05.302 [P2P3] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318 SYNCHRONIZED OK
2020-12-08 17:45:05.347 [P2P8] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318 SYNCHRONIZED OK

These contradict each other. I have no actual idea if monero cli and monerod are synced with each other.


________________________________
From: moneromooo-monero <notifications@github.com>
Sent: Tuesday, December 8, 2020 8:34 AM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


Post the actual message.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-740693250>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4S5SWU5PPCYXYZPLGDSTZBRVANCNFSM4UPIOBYQ>.


## moneromooo-monero | 2020-12-08T18:08:41+00:00
Can't see, requires JS, direct link in the source is permission denied.
I thikn you can upload images to github comments. i.ibb.co would also work. imgur hasn't been working in a few months.

## IndustrialOne | 2020-12-09T14:34:12+00:00
https://i.ibb.co/QnMtkZK/untitled.png
[https://i.ibb.co/QnMtkZK/untitled.png]


________________________________
From: moneromooo-monero <notifications@github.com>
Sent: Tuesday, December 8, 2020 11:08 AM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


Can't see, requires JS, direct link in the source is permission denied.
I thikn you can upload images to github comments. i.ibb.co would also work. imgur hasn't been working in a few months.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-740809436>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4QATXYPHBGP56YYOL3STZTTVANCNFSM4UPIOBYQ>.


## moneromooo-monero | 2020-12-09T18:44:40+00:00
That "out of sync" in the prompt means the wallet is out of sync wrt the daemon. That's different from the daemon being out of sync with the network.

The daemon syncs the chain to your machine. Then the wallet parses that chain to see which txes are for/from you. So in your case the daemon has downloaded and verified all the blocks in the chain, but the wallet hasn't finished checking it for transactions to/from you.

## IndustrialOne | 2020-12-10T14:43:40+00:00
So how come the GUI says I'm disconnected and won't let me mine? The CLI won't let me mine either AFAIK.

________________________________
From: moneromooo-monero <notifications@github.com>
Sent: Wednesday, December 9, 2020 11:44 AM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


That "out of sync" in the prompt means the wallet is out of sync wrt the daemon. That's different from the daemon being out of sync with the network.

The daemon syncs the chain to your machine. Then the wallet parses that chain to see which txes are for/from you. So in your case the daemon has downloaded and verified all the blocks in the chain, but the wallet hasn't finished checking it for transactions to/from you.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-741972526>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4VJCUKCPA6RJAQTS4DST7ASTANCNFSM4UPIOBYQ>.


## moneromooo-monero | 2020-12-10T16:22:04+00:00
Post actual messages.

## IndustrialOne | 2020-12-11T14:26:30+00:00
2020-12-11 14:17:46.904 5872 INFO logging contrib/epee/src/mlog.cpp:273 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-12-11 14:17:46.905 5872 WARNING frontend src/wallet/api/wallet.cpp:412 Logging to "C:\\Users\\Admin\\AppData\\Roaming\\monero-wallet-gui\\monero-wallet-gui.log"
2020-12-11 14:17:46.905 5872 WARNING frontend src/wallet/api/wallet.cpp:412 qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2020-12-11 14:17:49.348 5872 INFO logging contrib/epee/src/mlog.cpp:273 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-12-11 14:17:49.479 4964 WARNING wallet.wallet2 src/wallet/wallet2.cpp:5601 Loaded wallet keys file, with public address: 42MMxxxxxxxxxxxxxxx
2020-12-11 14:17:49.814 4964 ERROR wallet.wallet2 src/wallet/wallet2.cpp:5501 !m_is_initialized. THROW EXCEPTION: error::wallet_not_initialized
2020-12-11 14:17:49.822 4964 WARNING frontend src/wallet/api/wallet.cpp:412 Exception thrown from async function:  wallet is not initialized
2020-12-11 14:18:24.709 1604 WARNING net.dns src/common/dns_utils.cpp:567 WARNING: no two valid DNS TXT records were received


________________________________
From: moneromooo-monero <notifications@github.com>
Sent: Thursday, December 10, 2020 9:22 AM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


Post actual messages.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-742626265>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4UZ5RJ5CPUCOABJDATSUDYT5ANCNFSM4UPIOBYQ>.


## xiphon | 2020-12-11T14:57:39+00:00
Don't see any related error in the GUI log above.

> The CLI won't let me mine either AFAIK.

Post the CLI wallet logs.

## moneromooo-monero | 2020-12-11T15:31:19+00:00
That " !m_is_initialized" looks like a bug.

## IndustrialOne | 2020-12-11T16:30:53+00:00
CLI log doesn't say anything, just this:
2020-12-08 17:43:44.328 6128 INFO logging contrib/epee/src/mlog.cpp:273 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO

Monerod log said this wrt mining:
2020-12-07 13:00:38.132 [RPC0] WARNING miner src/cryptonote_basic/miner.cpp:414 Background mining controller thread started
2020-12-07 13:00:38.533 [miner 0] INFO global src/cryptonote_basic/miner.cpp:548 background mining is enabled, but not started, waiting until start triggers
2020-12-07 13:01:33.006 [P2P7] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318 SYNCHRONIZED OK
2020-12-07 13:01:33.529 [P2P5] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318 SYNCHRONIZED OK
2020-12-07 13:01:33.529 [P2P7] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:2318 SYNCHRONIZED OK
2020-12-07 13:03:03.622 [miner 0] INFO global src/cryptonote_basic/miner.cpp:548 background mining is enabled, but not started, waiting until start triggers
2020-12-07 13:07:12.430 [miner 0] INFO global src/cryptonote_basic/miner.cpp:548 background mining is enabled, but not started, waiting until start triggers

Then the last line kept repeating.

________________________________
From: xiphon <notifications@github.com>
Sent: Friday, December 11, 2020 7:57 AM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


Don't see any related error in the GUI log above.

The CLI won't let me mine either AFAIK.

Post the CLI wallet logs.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-743240368>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4WVNDFLN3U3ZU3LT5TSUIXPHANCNFSM4UPIOBYQ>.


## moneromooo-monero | 2020-12-11T16:41:30+00:00
Run monero-wallet-cli with --log-level 1, it defaults to not logging.

## IndustrialOne | 2020-12-14T12:16:43+00:00
https://pastebin.com/mSVetp7r
So is everything working fine? I was able to get mining started with cli but I cannot see any progress.

________________________________
From: moneromooo-monero <notifications@github.com>
Sent: Friday, December 11, 2020 9:41 AM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


Run monero-wallet-cli with --log-level 1, it defaults to not logging.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-743299964>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4Q4VXOEXSDJRDKECQTSUJDUVANCNFSM4UPIOBYQ>.


## moneromooo-monero | 2020-12-14T13:34:43+00:00
It looks like some minor calls to the daemon are timing out.
Are you running monerod with --restricted-rpc ?
In any case, it's mostly working from this log, modulo the timeouts.

## IndustrialOne | 2020-12-14T15:52:56+00:00
No --restricted-rpc on my custom commandline, no. Are the minor calls important?

________________________________
From: moneromooo-monero <notifications@github.com>
Sent: Monday, December 14, 2020 6:34 AM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


It looks like some minor calls to the daemon are timing out.
Are you running monerod with --restricted-rpc ?
In any case, it's mostly working from this log, modulo the timeouts.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-744443722>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4UMDN2KVUCZXWQWUEDSUYIAFANCNFSM4UPIOBYQ>.


## moneromooo-monero | 2020-12-14T17:36:11+00:00
Not really, they're the mining_status call, which asks the daemon whether it is mining.

## IndustrialOne | 2020-12-15T15:08:39+00:00
Ok so is the CLI communicating properly with the daemon or not? My original issue is why the GUI says my wallet is not connected with the daemon when monerod is obviously running and working. You asked if the CLI is exhibiting the same issue. Is it?

________________________________
From: moneromooo-monero <notifications@github.com>
Sent: Monday, December 14, 2020 10:36 AM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


Not really, they're the mining_status call, which asks the daemon whether it is mining.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-744596479>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4V6KES5YPAZVVQNITLSUZEJXANCNFSM4UPIOBYQ>.


## moneromooo-monero | 2020-12-15T16:45:27+00:00
In the log you posted, it seems to be communicating properly with the daemon except for the mining calls. Otherwise you get the chain and txpool data just fine. So by and large it seems fine.

## IndustrialOne | 2020-12-16T15:36:08+00:00
So why does the GUI say I'm disconnected? All I can see on the gui-wallet.log is "wallet not initialized".

________________________________
From: moneromooo-monero <notifications@github.com>
Sent: Tuesday, December 15, 2020 9:45 AM
To: monero-project/monero <monero@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero] Monerod and GUI monero not synced? (#7087)


In the log you posted, it seems to be communicating properly with the daemon except for the mining calls. Otherwise you get the chain and txpool data just fine. So by and large it seems fine.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero/issues/7087#issuecomment-745416550>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4S2WMJB7M3F2PLDI3DSU6HDPANCNFSM4UPIOBYQ>.


## moneromooo-monero | 2020-12-16T17:33:21+00:00
Ask on https://github.com/monero-project/monero-gui. Maybe it does something different.


# Action History
- Created by: IndustrialOne | 2020-12-06T11:51:11+00:00
- Closed at: 2022-07-19T19:59:03+00:00
