---
title: monerod sync stuck sometimes.
source_url: https://github.com/monero-project/monero/issues/2649
author: miningpoolhub
assignees: []
labels: []
created_at: '2017-10-14T01:34:37+00:00'
updated_at: '2017-11-10T23:01:22+00:00'
type: issue
status: closed
closed_at: '2017-10-22T10:00:21+00:00'
---

# Original Description
monerod sync stopped. rpc calls were working well. only block height didn't move forward.

I found this issue happening before the hardfork too. I thought it was fixed after the hardfork and forgot about it until today. It's happening still.
As soon as I found the daemon was stuck at some height, I killed and restarted. Now it synced to latest block height. Here's the log.


```
2017-10-12 13:02:55.544 [P2P4]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-12 14:05:15.199 [P2P7]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-12 14:49:52.604 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419127/1419127^[[0m
2017-10-12 14:49:52.604 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-12 15:00:47.400 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419132/1419132^[[0m
2017-10-12 15:00:47.400 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-12 15:05:50.162 [P2P4]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-12 15:48:33.124 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419149/1419149^[[0m
2017-10-12 15:48:33.124 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-12 15:53:49.535 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419155/1419155^[[0m
2017-10-12 15:53:49.535 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-12 16:09:51.746 [P2P3]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-12 16:27:23.833 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419175/1419175^[[0m
2017-10-12 16:27:23.833 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-12 17:13:29.524 [P2P9]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-12 18:14:37.456 [P2P3]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-12 19:00:02.581 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419246/1419246^[[0m
2017-10-12 19:00:02.582 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-12 19:15:32.260 [P2P7]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-12 19:26:46.269 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419259/1419259^[[0m
2017-10-12 19:26:46.269 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-12 20:15:57.991 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-12 21:16:07.882 [P2P6]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-12 22:17:06.365 [P2P5]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-12 23:20:02.840 [P2P7]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 00:22:13.635 [P2P3]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 00:52:08.617 [P2P2]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 01:24:54.288 [P2P7]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 01:56:54.531 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419435/1419435^[[0m
2017-10-13 01:56:54.531 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 02:13:43.656 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419446/1419446^[[0m
2017-10-13 02:13:43.656 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 02:26:26.167 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 03:08:39.602 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419474/1419474^[[0m
2017-10-13 03:08:39.602 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 03:27:20.378 [P2P3]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 04:30:54.401 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 05:13:21.276 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419530/1419530^[[0m
2017-10-13 05:13:21.276 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 05:30:57.452 [P2P2]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 06:32:28.173 [P2P2]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 07:38:33.750 [P2P3]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 07:39:13.730 [P2P7]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:578  [batch] DB resize needed
2017-10-13 07:39:13.769 [P2P7]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:494  LMDB Mapsize increased.  Old: 49813MiB, New: 50837MiB
2017-10-13 07:57:50.863 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419610/1419610^[[0m
2017-10-13 07:57:50.863 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 08:39:40.921 [P2P5]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 09:41:26.411 [P2P2]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 10:41:37.424 [P2P9]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 11:42:15.346 [P2P9]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 12:38:14.094 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419761/1419761^[[0m
2017-10-13 12:38:14.094 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 12:43:00.836 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 12:52:09.843 [P2P8]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 13:43:17.580 [P2P5]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 14:44:22.376 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 15:32:37.810 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419854/1419854^[[0m
2017-10-13 15:32:37.811 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 15:45:46.107 [P2P6]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 15:45:46.956 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419863/1419863^[[0m
2017-10-13 15:45:46.956 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 15:59:18.900 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419869/1419869^[[0m
2017-10-13 15:59:18.901 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 16:03:22.701 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419870/1419870^[[0m
2017-10-13 16:03:22.702 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 16:13:28.203 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419873/1419873^[[0m
2017-10-13 16:13:28.203 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 16:47:13.479 [P2P9]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 17:47:24.040 [P2P5]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 18:33:28.823 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419950/1419950^[[0m
2017-10-13 18:33:28.824 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 18:48:15.418 [P2P3]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 19:28:25.609 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[91.121.87.10:18080 OUT]  Synced 1419985/1419985^[[0m
2017-10-13 19:28:25.609 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-13 19:49:15.560 [P2P3]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-13 20:49:30.074 [P2P3]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-14 00:52:10.483 [P2P7]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-14 01:17:08.596 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped
2017-10-14 01:17:08.596 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:78     Stopping core rpc server...
2017-10-14 01:17:08.599 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:145       Node stopped.
2017-10-14 01:17:08.599 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-10-14 01:17:08.603 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-10-14 01:17:09.439 [SRV_MAIN]      INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-10-14 01:17:09.474 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-10-14 01:17:09.474 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
2017-10-14 01:17:11.733     7fce488fa740        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-14 01:17:11.734     7fce488fa740        INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.0.0-release)
2017-10-14 01:17:11.734     7fce488fa740        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2017-10-14 01:17:11.736     7fce488fa740        WARN    daemon  src/daemon/executor.cpp:62      Monero 'Helium Hydra' (v0.11.0.0-release) Daemonised
2017-10-14 01:17:11.736     7fce488fa740        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-10-14 01:17:11.736     7fce488fa740        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-10-14 01:17:11.738     7fce488fa740        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-10-14 01:17:15.941     7fce488fa740        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-10-14 01:17:15.941     7fce488fa740        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-10-14 01:17:15.942     7fce488fa740        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:51811
2017-10-14 01:17:15.942     7fce488fa740        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 51811
2017-10-14 01:17:15.942     7fce488fa740        INFO    global  src/daemon/core.h:73    Initializing core...
2017-10-14 01:17:15.944     7fce488fa740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /home/xxxxx/.bitmonero/lmdb ...
2017-10-14 01:17:17.278     7fce488fa740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:421     Loading checkpoints
2017-10-14 01:17:17.463     7fce488fa740        WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-14 01:17:17.464     7fce488fa740        INFO    global  src/daemon/core.h:78    Core initialized OK
2017-10-14 01:17:17.464     7fce488fa740        INFO    global  src/daemon/rpc.h:68     Starting core rpc server...
2017-10-14 01:17:17.464 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:73     Core rpc server started ok
2017-10-14 01:17:17.464 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2017-10-14 01:17:18.464 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1231    ^[[1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************
^[[0m
2017-10-14 01:17:18.650 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-14 01:17:18.899 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [164.132.166.19:18080 OUT] Sync data returned a new top block candidate: 1420034 -> 1420139 [Your node is 105 blocks (0 days) behind]
SYNCHRONIZATION started
2017-10-14 01:17:20.982 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[164.132.166.19:18080 OUT]  Synced 1420054/1420139^[[0m
2017-10-14 01:17:24.768 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[164.132.166.19:18080 OUT]  Synced 1420074/1420139^[[0m
2017-10-14 01:17:29.581 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[164.132.166.19:18080 OUT]  Synced 1420094/1420139^[[0m
2017-10-14 01:17:34.555 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[164.132.166.19:18080 OUT]  Synced 1420114/1420139^[[0m
2017-10-14 01:17:39.202 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[164.132.166.19:18080 OUT]  Synced 1420134/1420139^[[0m
2017-10-14 01:17:39.609 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ^[[1;33m[164.132.166.19:18080 OUT]  Synced 1420139/1420139^[[0m
2017-10-14 01:17:39.609 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1521    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-10-14 01:17:39.609 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1543    ^[[1;33m
```

# Discussion History
## moneromooo-monero | 2017-10-14T08:10:43+00:00
This log shows no problems. You need to run with `--log-level 1` in order for any errors adding blocks to show up.

## moneromooo-monero | 2017-10-15T10:56:42+00:00
And it's probably fixed anyway. Varous sync fixes are PR'd somewhere, can't bring myself to search for them yet again. They'll be merged soon hopefully.

## miningpoolhub | 2017-10-16T01:29:34+00:00
@moneromooo-monero Thanks!

## moneromooo-monero | 2017-10-16T08:23:27+00:00
And they're all merged now. master may be a bit dangerous to use  now though, as loads of complicated things went in at once.

## moneromooo-monero | 2017-10-22T09:50:25+00:00
+resolved

## miningpoolhub | 2017-11-10T23:00:00+00:00
It stuck again. I'm running 0.11.1.0 Helium Hydra Point Release 1.
I did not run with --log-level 1, so there's no log data to show currently.

I just want to reopen this case. (well I can't because I didn't close it)

# Action History
- Created by: miningpoolhub | 2017-10-14T01:34:37+00:00
- Closed at: 2017-10-22T10:00:21+00:00
