---
title: Cannot Syncing, seized at 1768663
source_url: https://github.com/monero-project/monero/issues/5212
author: eastredn
assignees: []
labels: []
created_at: '2019-03-01T08:28:37+00:00'
updated_at: '2019-03-05T13:49:37+00:00'
type: issue
status: closed
closed_at: '2019-03-05T13:49:37+00:00'
---

# Original Description
version：monero-v0.14.0.0
desc:   Cannot Syncing to newest block,it seized at 1768663, i try restart monerod, the same wrong.

logs:
2019-03-01 08:02:30.760     7fd276aee780        INFO    global  src/daemon/main.cpp:287 Monero 'Boron Butterfly' (v0.14.0.0-release)
2019-03-01 08:02:30.760     7fd276aee780        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2019-03-01 08:02:30.777     7fd276aee780        WARN    daemon  src/daemon/executor.cpp:61      Monero 'Boron Butterfly' (v0.14.0.0-release) Daemonised
2019-03-01 08:02:30.777     7fd276aee780        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2019-03-01 08:02:30.777     7fd276aee780        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2019-03-01 08:02:30.777     7fd276aee780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2019-03-01 08:02:54.789     7fd276aee780        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2019-03-01 08:02:54.789     7fd276aee780        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2019-03-01 08:02:54.789     7fd276aee780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:17071
2019-03-01 08:02:54.789     7fd276aee780        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 17071
2019-03-01 08:02:54.789     7fd276aee780        INFO    global  src/daemon/core.h:86    Initializing core...
2019-03-01 08:02:54.821     7fd276aee780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:469     Loading blockchain from folder /root/work/xmr/xmrdata/lmdb ...
2019-03-01 08:02:54.821     7fd276aee780        WARN    global  src/blockchain_db/lmdb/db_lmdb.cpp:1227 The blockchain is on a rotating drive: this will be very slow, use a SSD if possible
2019-03-01 08:03:28.024     7fd276aee780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:628     Loading checkpoints
2019-03-01 08:03:56.039     7fd276aee780        WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2019-03-01 08:03:56.040     7fd276aee780        INFO    global  src/daemon/core.h:92    Core initialized OK
2019-03-01 08:03:56.040     7fd276aee780        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2019-03-01 08:03:56.040 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2019-03-01 08:03:56.040 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2019-03-01 08:03:57.040 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1533
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************

2019-03-01 08:04:02.494 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1598
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2019-03-01 08:04:14.220 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [178.74.211.229:18080 OUT] Sync data returned a new top block candidate: 1768663 -> 1781946 [Your node is 13283 blocks (18 days) behind] 
SYNCHRONIZATION started
2019-03-01 08:04:44.513 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [84.85.102.113:18080 OUT] Sync data returned a new top block candidate: 1768663 -> 1781946 [Your node is 13283 blocks (18 days) behind] 
SYNCHRONIZATION started
2019-03-01 08:05:01.212     7fd2755e3700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::thread_interrupted
2019-03-01 08:05:01.212     7fd2755e3700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2019-03-01 08:05:01.239     7fd2755e3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /root/work/xmr/monero-v0.14.0.0/monerod:__wrap___cxa_throw+0x10a [0x55a7edb9d6ca]
2019-03-01 08:05:01.239     7fd2755e3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /root/work/xmr/monero-v0.14.0.0/monerod:boost::this_thread::interruption_point()+0x76 [0x55a7edf7bba6]
2019-03-01 08:05:01.239     7fd2755e3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /root/work/xmr/monero-v0.14.0.0/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)::{lambda()#1}::operator()() const+0x2b8 [0x55a7eda3eb08]
2019-03-01 08:05:01.239     7fd2755e3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /root/work/xmr/monero-v0.14.0.0/monerod+0xa11d4d [0x55a7edf7bd4d]
2019-03-01 08:05:01.239     7fd2755e3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fd2761b66ba]
2019-03-01 08:05:01.239     7fd2755e3700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fd275eec41d]
2019-03-01 08:05:01.239     7fd2755e3700        INFO    stacktrace      src/common/stack_trace.cpp:172
2019-03-01 08:05:18.634 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [95.216.74.172:44792 INC] Sync data returned a new top block candidate: 1768663 -> 1779351 [Your node is 10688 blocks (14 days) behind] 
SYNCHRONIZATION started
2019-03-01 08:05:30.736 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [62.210.104.31:47792 INC] Sync data returned a new top block candidate: 1768663 -> 1781946 [Your node is 13283 blocks (18 days) behind] 
SYNCHRONIZATION started
2019-03-01 08:06:38.334 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [94.22.226.45:34118 INC] Sync data returned a new top block candidate: 1768663 -> 1781947 [Your node is 13284 blocks (18 days) behind] 
SYNCHRONIZATION started
 2019-03-01 08:10:37.034        [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [13.229.227.42:18080 OUT] Sync data returned a new top block candidate: 1768663 -> 1781950 [Your node is 13287 blocks (18 days) behind] 
SYNCHRONIZATION started

# Discussion History
## moneromooo-monero | 2019-03-01T11:58:39+00:00
Restart with --log-level 1. This will show why new blocks are not added.

## eastredn | 2019-03-01T21:54:49+00:00
run with --log-level 1 logs:
[monerod-sync.txt](https://github.com/monero-project/monero/files/2921164/monerod-sync.txt)
pls help to view, thx

## moneromooo-monero | 2019-03-01T22:08:02+00:00
That looks like something that's fixed in https://github.com/monero-project/monero/pull/5193, which is on current release-v0.13 branch (but not in the tagged release yet).

## eastredn | 2019-03-02T02:53:59+00:00
How can i do? 

## eastredn | 2019-03-02T04:58:44+00:00
Thanks @moneromooo-monero  .  I clone v0.14.0.0 and  fixed with #5193 's code,  rebuild  it,      it works!

## moneromooo-monero | 2019-03-05T13:39:21+00:00
+resolved

# Action History
- Created by: eastredn | 2019-03-01T08:28:37+00:00
- Closed at: 2019-03-05T13:49:37+00:00
