---
title: 'print_coinbase_tx_sum 0 100 gives Error: Unsuccessful --'
source_url: https://github.com/monero-project/monero/issues/1722
author: KhojaHoldingCorp
assignees: []
labels: []
created_at: '2017-02-13T06:32:57+00:00'
updated_at: '2017-08-07T23:24:13+00:00'
type: issue
status: closed
closed_at: '2017-08-07T23:24:13+00:00'
---

# Original Description
monero@monerod:/tmp$ sudo ./monerod --version

Creating the logger system

Monero 'Wolfram Warptangent' (v0.10.1.0-release)

monero@monerod:/tmp$ sudo ./monerod print_coinbase_tx_sum 0 10

Creating the logger system

Error: Unsuccessful --

Help!

# Discussion History
## ghost | 2017-02-13T08:23:09+00:00
I'm getting the same error with current master no matter what block I start from (1, 100, 10000) or the number of blocks (1, 10, 100).

## JollyMort | 2017-02-13T11:53:11+00:00
It works for me on Win 7 x64 0.10.1, but if I run it from 0 to current height, it never finishes (left it overnight) and `monerod` uses 2GB RAM

## KhojaHoldingCorp | 2017-02-13T15:44:26+00:00
I used the precompiled linux binaries, I also compiled on Ubuntu 16.04 right after the fork, both have the error.

I will try to recompile later today with the most up to date source 

## moneromooo-monero | 2017-02-13T17:00:55+00:00
Precompiled binaries were buggy for this function.

## KhojaHoldingCorp | 2017-02-13T19:10:23+00:00
I recompiled with the "Bleeding Edge" source code. Still not working. Although there is a different error now!

monero@monerod:/tmp/monero/build/release/bin$ sudo /opt/monero/bin/monerod print_coinbase_tx_sum 0 10

2017-02-13 11:02:08.327     7f4fabc51740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO

2017-02-13 11:02:08.329     7f4fabc51740        ERROR   msgwriter       src/common/scoped_message_writer.h:94    Error: Unsuccessful --

Error: Unsuccessful --

Monero 'Wolfram Warptangent' (v0.10.1.0-3f171b9)

Compiled on Ubuntu 16.04
The daemon and wallet rpc's seem to work fine apart from that 

It seems that there is an issue with the logger and an issue with the print_coinbase_tx_sum  command

## moneromooo-monero | 2017-02-13T19:33:59+00:00
Add --log-level 1 and try the command again. It works for me with your example parameters.

As for the logger issue, file another bug for it.

## KhojaHoldingCorp | 2017-02-13T19:36:38+00:00
monero@monerod:/tmp/monero/build/release/bin$ sudo /opt/monero/bin/monerod print_coinbase_tx_sum 1 10 --log-level 1

2017-02-13 11:35:22.520     7f54c9c02740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO

2017-02-13 11:35:22.520     7f54c9c02740        INFO    global  contrib/epee/src/mlog.cpp:153   New log categories: *:WARNING,global:INFO,stacktrace:INFO

2017-02-13 11:35:22.524     7f54c9c02740        ERROR   msgwriter       src/common/scoped_message_writer.h:94   Error: Unsuccessful --

Error: Unsuccessful --

It seems to work on the windows binaries. ( from what I have been told ) 

Should I be providing other information?


## KhojaHoldingCorp | 2017-02-13T19:55:41+00:00
In my monerod log files I have 

2017-02-13 11:53:14.817 [P2P6]  ERROR   net.p2p src/p2p/net_node.inl:1455       [72.53.129.124:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)


## moneromooo-monero | 2017-02-13T19:57:57+00:00
Unrelated. If you don't see anything more interesting, try log level 2. If still nothing, then I'll have a look at the code to see if I can see anything weird without more info.

## KhojaHoldingCorp | 2017-02-13T19:59:20+00:00
monero@monerod:/var/log/monero$ sudo /opt/monero/bin/monerod print_coinbase_tx_sum 1 10 --log-level 2

2017-02-13 11:58:53.656     7fbf99b9d740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO

2017-02-13 11:58:53.656     7fbf99b9d740        INFO    global  contrib/epee/src/mlog.cpp:153   New log categories: *:DEBUG

2017-02-13 11:58:53.657     7fbf99b9d740        ERROR   msgwriter       src/common/scoped_message_writer.h:94   Error: Unsuccessful --

Error: Unsuccessful --


## moneromooo-monero | 2017-02-13T20:00:48+00:00
You're giving an instruction to the detached daemon here. The actual logs will be in the log file, ~/.bitmonero/bitmonerod.log

## KhojaHoldingCorp | 2017-02-13T20:16:31+00:00
monero@monerod:~/.bitmonero$ cat bitmonero.log

2017-02-13 10:54:23.499     7f8ce0d60740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO

2017-02-13 10:54:23.698     7f8ce0d60740        ERROR   msgwriter       src/common/scoped_message_writer.h:94   Error: Unsuccessful --

2017-02-13 11:02:08.327     7f4fabc51740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO

2017-02-13 11:02:08.329     7f4fabc51740        ERROR   msgwriter       src/common/scoped_message_writer.h:94   Error: Unsuccessful --

2017-02-13 11:02:16.456     7fda22908740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO

2017-02-13 11:02:16.457     7fda22908740        ERROR   msgwriter       src/common/scoped_message_writer.h:94   Error: Unsuccessful --

2017-02-13 11:35:22.520     7f54c9c02740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO

2017-02-13 11:35:22.520     7f54c9c02740        INFO    global  contrib/epee/src/mlog.cpp:153   New log categories: *:WARNING,global:INFO,stacktrace:INFO

2017-02-13 11:35:22.524     7f54c9c02740        ERROR   msgwriter       src/common/scoped_message_writer.h:94   Error: Unsuccessful --

2017-02-13 11:58:53.656     7fbf99b9d740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO

2017-02-13 11:58:53.656     7fbf99b9d740        INFO    global  contrib/epee/src/mlog.cpp:153   New log categories: *:DEBUG

2017-02-13 11:58:53.657     7fbf99b9d740        ERROR   msgwriter       src/common/scoped_message_writer.h:94   Error: Unsuccessful --


## moneromooo-monero | 2017-02-13T20:26:05+00:00
You've started the original without the log level 1 or 2, then.

## KhojaHoldingCorp | 2017-02-13T20:27:33+00:00
2017-Feb-13 12:32:06.462270 [RPC1]PERF       37        verRange
2017-Feb-13 12:32:06.464770 PERF       39    verRange
2017-Feb-13 12:32:06.468148 [RPC1]PERF        3        verRctMG
2017-Feb-13 12:32:06.468231 [RPC1]PERF       43      verRct
2017-Feb-13 12:32:06.468253 [RPC1]PERF       44    check_tx_inputs
2017-Feb-13 12:32:06.469303 [RPC1]/json_rpc[getblocktemplate] processed with 0/46/0ms
2017-Feb-13 12:32:06.639845 [RPC1]HTTP [172.16.254.81] POST /json_rpc
2017-Feb-13 12:32:06.641125 [RPC1]PERF             ----------
2017-Feb-13 12:32:06.641316 [RPC1]PERF             check_tx_inputs
2017-Feb-13 12:32:06.641340 [RPC1]PERF        0      expand_transaction_2
2017-Feb-13 12:32:06.641375 [RPC1]PERF               verRct
2017-Feb-13 12:32:06.641592 PERF             ----------
2017-Feb-13 12:32:06.677157 [RPC1]PERF       36        verRange
2017-Feb-13 12:32:06.677567 PERF       36    verRange
2017-Feb-13 12:32:06.680875 [RPC1]PERF        3        verRctMG
2017-Feb-13 12:32:06.680939 [RPC1]PERF       40      verRct
2017-Feb-13 12:32:06.680959 [RPC1]PERF       40    check_tx_inputs
2017-Feb-13 12:32:06.681956 [RPC1]/json_rpc[getblocktemplate] processed with 0/42/0ms
2017-Feb-13 12:32:07.472248 [RPC0]HTTP [172.16.254.81] POST /json_rpc
2017-Feb-13 12:32:07.473743 [RPC0]PERF             ----------
2017-Feb-13 12:32:07.473995 [RPC0]PERF             check_tx_inputs
2017-Feb-13 12:32:07.474032 [RPC0]PERF        0      expand_transaction_2
2017-Feb-13 12:32:07.474117 [RPC0]PERF               verRct
2017-Feb-13 12:32:07.474160 PERF             ----------
2017-Feb-13 12:32:07.510145 [RPC0]PERF       36        verRange
2017-Feb-13 12:32:07.510170 PERF       36    verRange
2017-Feb-13 12:32:07.513494 [RPC0]PERF        3        verRctMG
2017-Feb-13 12:32:07.513558 [RPC0]PERF       39      verRct
2017-Feb-13 12:32:07.513580 [RPC0]PERF       40    check_tx_inputs
2017-Feb-13 12:32:07.514594 [RPC0]/json_rpc[getblocktemplate] processed with 0/42/0ms
2017-Feb-13 12:32:07.685759 [RPC0]HTTP [172.16.254.81] POST /json_rpc
2017-Feb-13 12:32:07.687021 [RPC0]PERF             ----------
2017-Feb-13 12:32:07.687246 [RPC0]PERF             check_tx_inputs
2017-Feb-13 12:32:07.687268 [RPC0]PERF        0      expand_transaction_2
2017-Feb-13 12:32:07.687300 [RPC0]PERF               verRct
2017-Feb-13 12:32:07.687311 PERF             ----------
2017-Feb-13 12:32:07.723072 [RPC0]PERF       36        verRange
2017-Feb-13 12:32:07.723347 PERF       36    verRange
2017-Feb-13 12:32:07.726656 [RPC0]PERF        2        verRctMG
2017-Feb-13 12:32:07.726720 [RPC0]PERF       39      verRct
2017-Feb-13 12:32:07.726740 [RPC0]PERF       39    check_tx_inputs
2017-Feb-13 12:32:07.727733 [RPC0]/json_rpc[getblocktemplate] processed with 1/41/0ms
2017-Feb-13 12:32:08.057637 [P2P8][88.99.83.196:18080 OUT]NOTIFY_NEW_TRANSACTIONS
2017-Feb-13 12:32:08.518061 [RPC0]HTTP [172.16.254.81] POST /json_rpc
2017-Feb-13 12:32:08.520022 [RPC0]PERF             ----------
2017-Feb-13 12:32:08.520395 [RPC0]PERF             check_tx_inputs
2017-Feb-13 12:32:08.520429 [RPC0]PERF        0      expand_transaction_2
2017-Feb-13 12:32:08.520514 [RPC0]PERF               verRct
2017-Feb-13 12:32:08.520532 PERF             ----------
2017-Feb-13 12:32:08.556720 PERF       36    verRange
2017-Feb-13 12:32:08.556755 [RPC0]PERF       36        verRange
2017-Feb-13 12:32:08.560043 [RPC0]PERF        3        verRctMG
2017-Feb-13 12:32:08.560118 [RPC0]PERF       40      verRct
2017-Feb-13 12:32:08.560146 [RPC0]PERF       40    check_tx_inputs
2017-Feb-13 12:32:08.561213 [RPC0]/json_rpc[getblocktemplate] processed with 0/43/0ms
2017-Feb-13 12:32:08.731001 [RPC1]HTTP [172.16.254.81] POST /json_rpc
2017-Feb-13 12:32:08.732896 [RPC1]PERF             ----------
2017-Feb-13 12:32:08.733244 [RPC1]PERF             check_tx_inputs
2017-Feb-13 12:32:08.733279 [RPC1]PERF        0      expand_transaction_2
2017-Feb-13 12:32:08.733328 [RPC1]PERF               verRct
2017-Feb-13 12:32:08.733342 PERF             ----------
2017-Feb-13 12:32:08.769718 [RPC1]PERF       36        verRange
2017-Feb-13 12:32:08.769798 PERF       37    verRange
2017-Feb-13 12:32:08.773117 [RPC1]PERF        3        verRctMG
2017-Feb-13 12:32:08.773181 [RPC1]PERF       40      verRct
2017-Feb-13 12:32:08.773201 [RPC1]PERF       40    check_tx_inputs
2017-Feb-13 12:32:08.774195 [RPC1]/json_rpc[getblocktemplate] processed with 0/43/0ms
2017-Feb-13 12:32:09.565126 [RPC0]HTTP [172.16.254.81] POST /json_rpc
2017-Feb-13 12:32:09.566421 [RPC0]PERF             ----------
2017-Feb-13 12:32:09.566653 [RPC0]PERF             check_tx_inputs
2017-Feb-13 12:32:09.566683 [RPC0]PERF        0      expand_transaction_2
2017-Feb-13 12:32:09.566771 [RPC0]PERF               verRct
2017-Feb-13 12:32:09.566793 PERF             ----------
2017-Feb-13 12:32:09.602632 [RPC0]PERF       36        verRange
2017-Feb-13 12:32:09.602733 PERF       35    verRange
2017-Feb-13 12:32:09.606053 [RPC0]PERF        3        verRctMG
2017-Feb-13 12:32:09.606119 [RPC0]PERF       40      verRct
2017-Feb-13 12:32:09.606140 [RPC0]PERF       40    check_tx_inputs
2017-Feb-13 12:32:09.607154 [RPC0]/json_rpc[getblocktemplate] processed with 0/42/0ms
2017-Feb-13 12:32:09.777904 [RPC0]HTTP [172.16.254.81] POST /json_rpc
2017-Feb-13 12:32:09.779311 [RPC0]PERF             ----------
2017-Feb-13 12:32:09.779566 [RPC0]PERF             check_tx_inputs
2017-Feb-13 12:32:09.779595 [RPC0]PERF        0      expand_transaction_2
2017-Feb-13 12:32:09.779651 [RPC0]PERF               verRct
2017-Feb-13 12:32:09.779662 PERF             ----------
2017-Feb-13 12:32:09.815876 [RPC0]PERF       37        verRange
2017-Feb-13 12:32:09.816165 PERF       37    verRange
2017-Feb-13 12:32:09.819475 [RPC0]PERF        3        verRctMG
2017-Feb-13 12:32:09.819539 [RPC0]PERF       40      verRct
2017-Feb-13 12:32:09.819559 [RPC0]PERF       40    check_tx_inputs
2017-Feb-13 12:32:09.820552 [RPC0]/json_rpc[getblocktemplate] processed with 0/42/0ms
2017-Feb-13 12:32:10.362968 [RPC0]HTTP [172.16.254.81] POST /json_rpc
2017-Feb-13 12:32:10.363213 [RPC0]/json_rpc[getlastblockheader] processed with 0/0/0ms


I've gone back to my the release binaries. This is the contents of the detached monerod

I get no new entries in ~/bitmonero/bitmonero.log

monero@monerod:~/.bitmonero$ sudo /opt/monero/bin/monerod print_coinbase_tx_sum 1 10 --log-level 2
Creating the logger system
Error: Unsuccessful --
monero@monerod:~/.bitmonero$



## ghost | 2017-02-13T22:14:29+00:00
Afraid I'm seeing this with current master `Monero 'Wolfram Warptangent' (v0.10.1.0-3f171b9)`

No matter which block I choose to start from or how many I want to count over.

Sadly nothing I can see of much use in the logs at level 1 or 2.

```
nodey@odroidc2:~/.bitmonero$ monerod print_coinbase_tx_sum 10000 10000
2017-02-13 22:11:06.970	      7f7f712000	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-02-13 22:11:06.970	      7f7f712000	INFO 	global	contrib/epee/src/mlog.cpp:153	New log categories: *:DEBUG
2017-02-13 22:11:09.347	      7f7f712000	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Unsuccessful --
```

## moneromooo-monero | 2017-02-13T22:43:07+00:00
Nothing seems wrong indeed. I guess I'll have a look to see if I can spot something, just in case.

## moneromooo-monero | 2017-02-13T22:56:04+00:00
Actually, I can get the same problem when I use a detached daemon too. Will fix.

## moneromooo-monero | 2017-02-13T23:07:06+00:00
https://github.com/monero-project/monero/pull/1729 should fix it, I can't test till I'm synced though, and that won't be till tomorrow.

## KhojaHoldingCorp | 2017-02-13T23:14:27+00:00
Awesome.. Thanks for the fast work!

## moneromooo-monero | 2017-02-13T23:33:10+00:00
Actually it synced already, a lot faster than I expected. And the fix doesn't work :) Debugging...

## moneromooo-monero | 2017-02-13T23:51:13+00:00
Fixed :)

## ghost | 2017-02-14T00:24:32+00:00
Thanks!

## KhojaHoldingCorp | 2017-02-14T00:28:06+00:00
Awesome..

## moneromooo-monero | 2017-08-07T23:23:36+00:00
+resolved

# Action History
- Created by: KhojaHoldingCorp | 2017-02-13T06:32:57+00:00
- Closed at: 2017-08-07T23:24:13+00:00
