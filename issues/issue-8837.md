---
title: Monerod crashes without any visible errors in its logs
source_url: https://github.com/monero-project/monero/issues/8837
author: k4r4b3y
assignees: []
labels:
- bug
- more info needed
created_at: '2023-05-05T08:33:23+00:00'
updated_at: '2023-12-09T06:18:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am running monerod on odroid hc1 with latest dietpiOS (bookworm). Hardware has 2 GB RAM available, and I have created 4 GB of swap space. 
I am running the monerod binaries that I compiled from source, following the raspberry pi zero guide that comes with the monero repo's readme file.

Here are the logs that show the crashing behavior:
```
2023-05-04 18:19:28.365         b6975a60        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-05-04 18:19:28.365         b6975a60        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-04 18:19:28.366         b6975a60        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2023-05-04 18:19:28.376         b6975a60        WARNING daemon  src/daemon/executor.cpp:61      Monero 'Fluorine Fermi' (v0.18.2.2-release) Daemonised
2023-05-04 18:19:28.377         b6975a60        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2023-05-04 18:19:28.377         b6975a60        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2023-05-04 18:19:28.386         b6975a60        INFO    global  src/daemon/core.h:64    Initializing core...
2023-05-04 18:19:28.387         b6975a60        INFO    global  src/cryptonote_core/cryptonote_core.cpp:523     Loading blockchain from folder /mnt/external-hdd/bitmonero/lmdb ...
2023-05-04 18:19:28.389         b6975a60        WARNING global  src/blockchain_db/lmdb/db_lmdb.cpp:1354 The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2023-05-04 18:19:29.071         b6975a60        INFO    global  src/cryptonote_core/cryptonote_core.cpp:698     Loading checkpoints
2023-05-04 18:19:29.072         9198f180        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::bad_alloc
2023-05-04 18:19:29.072         9198f180        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2023-05-04 18:19:29.072         b6975a60        INFO    global  src/daemon/core.h:81    Core initialized OK
2023-05-04 18:19:29.072         b6975a60        INFO    global  src/daemon/p2p.h:64     Initializing p2p server...
2023-05-04 18:19:29.073         9198f180        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0xa5) [0x481d36]:__cxa_throw+0xa5) [0x481d36]
2023-05-04 18:19:29.073         9198f180        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/local/bin/monerod(+0x4da4a2) [0x92b4a2]
2023-05-04 18:19:29.073         9198f180        INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/local/bin/monerod(+0x4d3586) [0x924586]
2023-05-04 18:19:29.073         9198f180        INFO    stacktrace      src/common/stack_trace.cpp:172
2023-05-04 18:19:29.121         b6975a60        INFO    global  src/daemon/p2p.h:69     p2p server initialized OK
2023-05-04 18:19:29.122         b6975a60        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2023-05-04 18:19:29.123         b6975a60        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 127.0.0.1 (IPv4):18081
2023-05-04 18:19:29.303         b6975a60        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2023-05-04 18:19:29.304         b6975a60        INFO    global  src/daemon/rpc.h:63     Initializing restricted RPC server...
2023-05-04 18:19:29.304         b6975a60        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 0.0.0.0 (IPv4):18089
2023-05-04 18:19:33.832         b6975a60        INFO    global  src/daemon/rpc.h:69     restricted RPC server initialized OK on port: 18089
2023-05-04 18:19:33.851         b6975a60        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2023-05-04 18:19:33.853 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2023-05-04 18:19:33.853 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:74     Starting restricted RPC server...
2023-05-04 18:19:33.853 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     restricted RPC server started ok
2023-05-04 18:19:33.853 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:214       Public RPC port 18089 will be advertised to other peers over P2P
2023-05-04 18:19:33.854 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:79     Starting p2p net loop...
2023-05-04 18:19:34.857 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2023-05-04 18:19:34.860 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    **********************************************************************
2023-05-04 18:19:34.862 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    The daemon will start synchronizing with the network. This may take a long time to complete.
2023-05-04 18:19:34.862 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2023-05-04 18:19:34.862 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    You can set the level of process detailization through "set_log <level|categories>" command,
2023-05-04 18:19:34.862 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-05-04 18:19:34.863 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2023-05-04 18:19:34.863 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    Use the "help" command to see the list of available commands.
2023-05-04 18:19:34.863 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    Use "help <command>" to see a command's documentation.
2023-05-04 18:19:34.863 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    **********************************************************************
2023-05-04 18:19:40.160 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2023-05-04 18:19:40.161 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2023-05-04 18:19:40.164 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0xa5) [0x481d36]:__cxa_throw+0xa5) [0x481d36]
2023-05-04 18:19:40.166 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/local/bin/monerod(+0x2ff1e) [0x480f1e]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/local/bin/monerod(+0x23e734) [0x68f734]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/local/bin/monerod(+0x24dd0a) [0x69ed0a]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/local/bin/monerod(+0x252662) [0x6a3662]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/local/bin/monerod(+0x28e0a2) [0x6df0a2]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/local/bin/monerod(+0x28fffc) [0x6e0ffc]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/local/bin/monerod(+0x290f3a) [0x6e1f3a]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/local/bin/monerod(+0x236156) [0x687156]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/local/bin/monerod(+0x26109e) [0x6b209e]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/local/bin/monerod(+0x26143a) [0x6b243a]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/local/bin/monerod(+0x6ee32) [0x4bfe32]
2023-05-04 18:19:40.167 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/local/bin/monerod(+0x223b32) [0x674b32]
2023-05-04 18:19:40.168 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /usr/local/bin/monerod(+0x250f24) [0x6a1f24]
2023-05-04 18:19:40.168 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15]  0x6a7c) [0xb69b5a7c]:_thread.so.1.74.0(+0x6a7c) [0xb69b5a7c]
2023-05-04 18:19:40.168 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172
2023-05-04 18:19:41.711 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     [73.46.171.87:18080 OUT] Sync data returned a new top block candidate: 2826357 -> 2878665 [Your node is 52308 blocks (2.4 months) behind]
2023-05-04 18:19:41.713 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     SYNCHRONIZATION started
2023-05-04 18:21:57.839         b69daa60        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-05-04 18:21:57.839         b69daa60        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-04 18:21:57.840         b69daa60        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2023-05-04 18:21:57.850         b69daa60        WARNING daemon  src/daemon/executor.cpp:61      Monero 'Fluorine Fermi' (v0.18.2.2-release) Daemonised
2023-05-04 18:21:57.851         b69daa60        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2023-05-04 18:21:57.851         b69daa60        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2023-05-04 18:21:57.860         b69daa60        INFO    global  src/daemon/core.h:64    Initializing core...
2023-05-04 18:21:57.861         b69daa60        INFO    global  src/cryptonote_core/cryptonote_core.cpp:523     Loading blockchain from folder /mnt/external-hdd/bitmonero/lmdb ...
2023-05-04 18:21:57.863         b69daa60        WARNING global  src/blockchain_db/lmdb/db_lmdb.cpp:1354 The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2023-05-04 18:21:58.796         b69daa60        INFO    global  src/cryptonote_core/cryptonote_core.cpp:698     Loading checkpoints
2023-05-04 18:21:58.797         919ef180        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::bad_alloc
2023-05-04 18:21:58.797         919ef180        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2023-05-04 18:21:58.798         b69daa60        INFO    global  src/daemon/core.h:81    Core initialized OK
2023-05-04 18:21:58.798         b69daa60        INFO    global  src/daemon/p2p.h:64     Initializing p2p server...
2023-05-04 18:21:58.798         919ef180        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0xa5) [0x470d36]:__cxa_throw+0xa5) [0x470d36]
2023-05-04 18:21:58.798         919ef180        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/local/bin/monerod(+0x4da4a2) [0x91a4a2]
2023-05-04 18:21:58.799         919ef180        INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/local/bin/monerod(+0x4d3586) [0x913586]
2023-05-04 18:21:58.799         919ef180        INFO    stacktrace      src/common/stack_trace.cpp:172
2023-05-04 18:21:58.851         b69daa60        INFO    global  src/daemon/p2p.h:69     p2p server initialized OK
2023-05-04 18:21:58.854         b69daa60        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2023-05-04 18:21:58.857         b69daa60        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 127.0.0.1 (IPv4):18081
2023-05-04 18:21:59.039         b69daa60        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2023-05-04 18:21:59.041         b69daa60        INFO    global  src/daemon/rpc.h:63     Initializing restricted RPC server...
2023-05-04 18:21:59.041         b69daa60        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 0.0.0.0 (IPv4):18089
2023-05-04 18:22:05.925         b69daa60        INFO    global  src/daemon/rpc.h:69     restricted RPC server initialized OK on port: 18089
2023-05-04 18:22:05.937         b69daa60        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2023-05-04 18:22:05.938 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2023-05-04 18:22:05.939 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:74     Starting restricted RPC server...
2023-05-04 18:22:05.939 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     restricted RPC server started ok
2023-05-04 18:22:05.940 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:214       Public RPC port 18089 will be advertised to other peers over P2P
2023-05-04 18:22:05.940 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:79     Starting p2p net loop...
2023-05-04 18:22:06.942 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2023-05-04 18:22:06.946 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    **********************************************************************
2023-05-04 18:22:06.947 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    The daemon will start synchronizing with the network. This may take a long time to complete.
2023-05-04 18:22:06.949 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2023-05-04 18:22:06.949 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    You can set the level of process detailization through "set_log <level|categories>" command,
2023-05-04 18:22:06.949 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-05-04 18:22:06.949 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2023-05-04 18:22:06.949 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    Use the "help" command to see the list of available commands.
2023-05-04 18:22:06.949 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    Use "help <command>" to see a command's documentation.
2023-05-04 18:22:06.949 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    **********************************************************************
2023-05-04 18:22:12.753 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     [73.46.171.87:18080 OUT] Sync data returned a new top block candidate: 2826357 -> 2878666 [Your node is 52309 blocks (2.4 months) behind]
2023-05-04 18:22:12.753 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     SYNCHRONIZATION started
2023-05-04 18:24:36.357         b6d98a60        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-05-04 18:24:36.358         b6d98a60        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-04 18:24:36.359         b6d98a60        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2023-05-04 18:24:36.369         b6d98a60        WARNING daemon  src/daemon/executor.cpp:61      Monero 'Fluorine Fermi' (v0.18.2.2-release) Daemonised
2023-05-04 18:24:36.370         b6d98a60        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2023-05-04 18:24:36.370         b6d98a60        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2023-05-04 18:24:36.377         b6d98a60        INFO    global  src/daemon/core.h:64    Initializing core...
2023-05-04 18:24:36.378         b6d98a60        INFO    global  src/cryptonote_core/cryptonote_core.cpp:523     Loading blockchain from folder /mnt/external-hdd/bitmonero/lmdb ...
2023-05-04 18:24:36.379         b6d98a60        WARNING global  src/blockchain_db/lmdb/db_lmdb.cpp:1354 The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2023-05-04 18:24:37.633         b6d98a60        INFO    global  src/cryptonote_core/cryptonote_core.cpp:698     Loading checkpoints
2023-05-04 18:24:37.633         9198f180        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::bad_alloc
2023-05-04 18:24:37.633         9198f180        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2023-05-04 18:24:37.634         b6d98a60        INFO    global  src/daemon/core.h:81    Core initialized OK
2023-05-04 18:26:45.872         b6985a60        WARNING daemon  src/daemon/executor.cpp:61      Monero 'Fluorine Fermi' (v0.18.2.2-release) Daemonised
2023-05-04 18:26:45.873         b6985a60        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2023-05-04 18:26:45.873         b6985a60        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2023-05-04 18:26:45.880         b6985a60        INFO    global  src/daemon/core.h:64    Initializing core...
2023-05-04 18:26:45.880         b6985a60        INFO    global  src/cryptonote_core/cryptonote_core.cpp:523     Loading blockchain from folder /mnt/external-hdd/bitmonero/lmdb ...
2023-05-04 18:26:45.882         b6985a60        WARNING global  src/blockchain_db/lmdb/db_lmdb.cpp:1354 The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2023-05-04 18:26:48.194         b6985a60        INFO    global  src/cryptonote_core/cryptonote_core.cpp:698     Loading checkpoints
2023-05-04 18:26:48.194         9199f180        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::bad_alloc
2023-05-04 18:26:48.194         9199f180        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2023-05-04 18:26:48.194         b6985a60        INFO    global  src/daemon/core.h:81    Core initialized OK
2023-05-04 18:26:48.195         b6985a60        INFO    global  src/daemon/p2p.h:64     Initializing p2p server...
2023-05-04 18:26:48.195         9199f180        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0xa5) [0x438d36]:__cxa_throw+0xa5) [0x438d36]
2023-05-04 18:26:48.195         9199f180        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/local/bin/monerod(+0x4da4a2) [0x8e24a2]
2023-05-04 18:26:48.195         9199f180        INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/local/bin/monerod(+0x4d3586) [0x8db586]
2023-05-04 18:26:48.195         9199f180        INFO    stacktrace      src/common/stack_trace.cpp:172
2023-05-04 18:26:48.251         b6985a60        INFO    global  src/daemon/p2p.h:69     p2p server initialized OK
2023-05-04 18:26:48.253         b6985a60        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2023-05-04 18:26:48.253         b6985a60        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 127.0.0.1 (IPv4):18081
2023-05-04 18:26:48.449         b6985a60        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2023-05-04 18:26:48.451         b6985a60        INFO    global  src/daemon/rpc.h:63     Initializing restricted RPC server...
2023-05-04 18:26:48.451         b6985a60        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 0.0.0.0 (IPv4):18089
2023-05-04 18:27:03.591         b6985a60        INFO    global  src/daemon/rpc.h:69     restricted RPC server initialized OK on port: 18089
2023-05-04 18:27:03.600         b6985a60        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2023-05-04 18:27:03.601 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2023-05-04 18:27:03.601 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:74     Starting restricted RPC server...
2023-05-04 18:27:03.602 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     restricted RPC server started ok
2023-05-04 18:27:03.602 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:214       Public RPC port 18089 will be advertised to other peers over P2P
2023-05-04 18:27:03.602 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:79     Starting p2p net loop...
2023-05-04 18:27:04.605 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2023-05-04 18:27:04.605 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    **********************************************************************
2023-05-04 18:27:04.605 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    The daemon will start synchronizing with the network. This may take a long time to complete.
2023-05-04 18:27:04.605 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2023-05-04 18:27:04.605 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    You can set the level of process detailization through "set_log <level|categories>" command,
2023-05-04 18:27:04.605 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-05-04 18:27:04.605 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2023-05-04 18:27:04.605 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    Use the "help" command to see the list of available commands.
2023-05-04 18:27:04.605 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    Use "help <command>" to see a command's documentation.
2023-05-04 18:27:04.605 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    **********************************************************************
2023-05-04 18:27:10.575 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     [73.46.171.87:18080 OUT] Sync data returned a new top block candidate: 2826357 -> 2878673 [Your node is 52316 blocks (2.4 months) behind]
2023-05-04 18:27:10.575 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     SYNCHRONIZATION started
(END)
```

As you can see from the following log lines, monerod crashes without a visible error in the logs, and my systemd service brings it back up within 30secs of it crashing:
```
2023-05-04 18:22:12.753 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     SYNCHRONIZATION started
2023-05-04 18:24:36.357         b6d98a60        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-05-04 18:24:36.358         b6d98a60        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)
```

I noticed that this behavior occurs when I enable the `anonymous-incoming` and `tx-proxy` directives for tor on my monerod.config.

Here's my monerod.config:
```
# /etc/monero/monerod.conf

# Data directory (blockchain db and indices)
data-dir=/mnt/external-hdd/bitmonero

# Log file
log-file=/var/log/monero/monerod.log

# P2P configuration
p2p-bind-ip=0.0.0.0            # Bind to all interfaces (the default)
p2p-bind-port=18080            # Bind to default port

# RPC restricted public node configuration
# this will restrict the RPC capabilities of
# the remote clients connecting to our node
public-node=1                   # Advertise to other users they can use this node as a remote one for connecting their wallets
rpc-restricted-bind-ip=0.0.0.0  # Bind restricted RPC to all interfaces
rpc-restricted-bind-port=18089  # Bind restricted RPC on custom port to differentiate from default unrestricted RPC (18081)

# RPC unrestricted local node configuration
# this will allow us to run some RPC commands
# such as `print_cn` on our own node
rpc-bind-ip=127.0.0.1           # Bind unrestricted RPC to localhost
rpc-bind-port=18081             # Bind unrestricted RPC to its default port

no-igd=1                        # Disable UPnP port mapping

# Block known-malicious nodes from a DNSBL
enable-dns-blocklist=1

# Tor: broadcast transactions originating from connected wallets over Tor (does not concern relayed transactions)
tx-proxy=tor,127.0.0.1:9050,16

# I2P: broadcast transactions originating from connected wallets over I2P (does not concern relayed transactions)
#tx-proxy=i2p,127.0.0.1:48085,16

# Note: add-peer= and add-priority-node= directives aren't needed since monerod v0.18

# Tor: tell monerod your onion address so it can be advertised on P2P network
# don't forget to remove the comment from /etc/tor/torrc file enabling
# the port 18083!
anonymous-inbound=<REDACTED>.onion:18083,127.0.0.1:18083,16

# I2P: tell monerod your b32 address so it can be advertised on P2P network
#anonymous-inbound=<yourownb32i2paddress>.b32.i2p,127.0.0.1:48083,16
```

When I comment out `anonymous-inbound` and `tx-proxy=tor,` directives, my node runs without this kind of crash and it maintians a stable set of peers and syncs th blockchain.

How can I get my monerod working with anonymous inbound and tx proxy settings for tor?

# Discussion History
## selsta | 2023-05-05T12:14:02+00:00
The logs unfortunately aren't useful. Do you run Tor and I2P manually?

## k4r4b3y | 2023-05-05T12:20:41+00:00
I run Tor as the systemd service that comes by default with debian.

>The logs unfortunately aren't useful.

What else can I provide?

## selsta | 2023-05-05T13:10:32+00:00
> What else can I provide?

It would be important to know if monerod gets killed for being out of memory or crashes.

If you start monerod manually from the command line (no systemd), does it say "Killed" when it stops running?

## k4r4b3y | 2023-05-05T17:02:24+00:00
>If you start monerod manually from the command line (no systemd), does it say "Killed" when it stops running?

It gave "Bus error"


```
user@DietPi:~$ sudo -u monero bash
monero@DietPi:/home/user$ /usr/local/bin/monerod --config-file=/etc/monero/monerod.conf --pidfile /var/run/monero/monerod.pid
2023-05-05 16:55:48.565 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-05 16:55:48.565 I Initializing cryptonote protocol...
2023-05-05 16:55:48.565 I Cryptonote protocol initialized OK
2023-05-05 16:55:48.569 I Initializing core...
2023-05-05 16:55:48.569 I Loading blockchain from folder /mnt/external-hdd/bitmonero/lmdb ...
2023-05-05 16:55:48.570 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2023-05-05 16:58:00.456 I Loading checkpoints
2023-05-05 16:58:00.459 I Core initialized OK
2023-05-05 16:58:00.459 I Initializing p2p server...
2023-05-05 16:58:00.526 I p2p server initialized OK
2023-05-05 16:58:00.528 I Initializing core RPC server...
2023-05-05 16:58:00.529 I Binding on 127.0.0.1 (IPv4):18081
2023-05-05 16:58:00.722 I core RPC server initialized OK on port: 18081
2023-05-05 16:58:00.723 I Initializing restricted RPC server...
2023-05-05 16:58:00.724 I Binding on 0.0.0.0 (IPv4):18089
2023-05-05 16:58:17.535 I restricted RPC server initialized OK on port: 18089
2023-05-05 16:58:17.547 I Starting core RPC server...
2023-05-05 16:58:17.548 I core RPC server started ok
2023-05-05 16:58:17.554 I Starting restricted RPC server...
2023-05-05 16:58:17.557 I restricted RPC server started ok
2023-05-05 16:58:17.567 I Starting p2p net loop...
2023-05-05 16:58:18.573 I
2023-05-05 16:58:18.573 I **********************************************************************
2023-05-05 16:58:18.574 I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-05-05 16:58:18.574 I
2023-05-05 16:58:18.574 I You can set the level of process detailization through "set_log <level|categories>" command,
2023-05-05 16:58:18.575 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-05-05 16:58:18.575 I
2023-05-05 16:58:18.575 I Use the "help" command to see the list of available commands.
2023-05-05 16:58:18.575 I Use "help <command>" to see a command's documentation.
2023-05-05 16:58:18.576 I **********************************************************************
2023-05-05 16:58:19.302 I [66.42.102.130:18080 OUT] Sync data returned a new top block candidate: 2830977 -> 2879332 [Your node is 48355 blocks (2.2 months) behind]
2023-05-05 16:58:19.303 I SYNCHRONIZATION started
2023-05-05 16:59:26.076 I Synced 2830997/2879332 (98%, 48335 left)
2023-05-05 17:00:03.500 I Synced 2831017/2879332 (98%, 48315 left)
Bus error
monero@DietPi:/home/user$
```

## moneromooo-monero | 2023-05-05T17:11:12+00:00
Assuming you're on x86_64, this'll be an attempt to derefence unmapped memory. This typically points to your database being shot. 

## k4r4b3y | 2023-05-05T17:14:07+00:00
>Assuming you're on x86_64

I am on 32-bit dietpiOS (debian bookworm based).

## selsta | 2023-05-05T17:16:27+00:00
So you can 100% fix the issue by removing `anonymous-inbound` and `tx-proxy` ? What if you just add `tx-proxy`, still same issue?

## k4r4b3y | 2023-05-05T17:17:27+00:00
>So you can 100% fix the issue by removing anonymous-inbound and tx-proxy ?

That's right. When I remove only those 2 lines, the monerod runs stable, without reboots.

> What if you just add tx-proxy, still same issue?

Let me try that.

## k4r4b3y | 2023-05-05T17:28:07+00:00
>What if you just add tx-proxy, still same issue?

With this, monerod is running without giving the "Bus error" as before. So, the problem is with `anonymous-inbound` directive? How can I resolve it?

## selsta | 2023-05-05T17:29:16+00:00
Do you know how to run monerod in gdb and get a backtrace?

## k4r4b3y | 2023-05-05T17:29:58+00:00
>Do you know how to run monerod in gdb and get a backtrace?

Unfortunately not. But if you have a guide for me, I can try and figure it out.

## selsta | 2023-05-05T17:31:19+00:00
https://github.com/monero-project/monero/issues/8821#issuecomment-1503373610

Start it with your starting arguments.

## k4r4b3y | 2023-05-05T17:31:44+00:00
thanks, I am checking it out.

## k4r4b3y | 2023-05-05T17:39:15+00:00
I have been running `monerod` with a system user called "monero." I started a bash shell with that user and tried running gdb with "monero" user. However, when I issue "run", gdb says "This account is currently not available".

Is it not possible to run gdb with a system user? If not I might have to quickly run the monerod from my normal user account and start the blockchain from scratch. 

## k4r4b3y | 2023-05-05T17:50:00+00:00
OK. I managed to run it with the monero user by using:
```
monero@DietPi:/home/user$ export SHELL=/bin/sh ; gdb --args /usr/local/bin/monerod --config-file=/etc/monero/monerod.conf --pidfile /var/run/monero/monerod.pid
```

I will report back the remaining part of the debugging.

## k4r4b3y | 2023-05-05T17:54:39+00:00
Here's the output of `thread apply all bt`:

```
[New Thread 0xa79fb180 (LWP 5676)]
[New Thread 0xa733a180 (LWP 5677)]
[New Thread 0xa6e39180 (LWP 5678)]

Thread 16 "monerod" received signal SIGBUS, Bus error.
[Switching to Thread 0x79dfd180 (LWP 5655)]
0x00465740 in bool nodetool::peerlist_entry_base<epee::net_utils::network_address>::serialize_map<true, epee::serialization::portable_storage>(epee::serialization::portable_storage&, epee::serialization::portable_storage::hsection) [clone .isra.0] ()
(gdb) thread apply all bt

Thread 38 (Thread 0xa6e39180 (LWP 5678) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 37 (Thread 0xa733a180 (LWP 5677) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 36 (Thread 0xa79fb180 (LWP 5676) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 35 (Thread 0xa7efc180 (LWP 5675) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 34 (Thread 0xa83fd180 (LWP 5674) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
--Type <RET> for more, q to quit, c to continue without paging--
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 33 (Thread 0xa88fe180 (LWP 5673) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 32 (Thread 0xa8dff180 (LWP 5672) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 31 (Thread 0x748f7180 (LWP 5670) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 30 (Thread 0x74df8180 (LWP 5669) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 29 (Thread 0x752f9180 (LWP 5668) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
--Type <RET> for more, q to quit, c to continue without paging--
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 28 (Thread 0x757fa180 (LWP 5667) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 27 (Thread 0x75cfb180 (LWP 5666) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 26 (Thread 0x761fc180 (LWP 5665) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 25 (Thread 0x766fd180 (LWP 5664) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0074887e in tools::threadpool::run(bool) ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 24 (Thread 0x76bfe180 (LWP 5663) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674369a in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
--Type <RET> for more, q to quit, c to continue without paging--c

Thread 23 (Thread 0x770ff180 (LWP 5662) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674369a in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 22 (Thread 0x777fd180 (LWP 5661) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674369a in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 21 (Thread 0x77cfe180 (LWP 5660) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674369a in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 20 (Thread 0x781ff180 (LWP 5659) "monerod"):
#0  0xb6707616 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb679cafc in epoll_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0x0046dca2 in boost::asio::detail::epoll_reactor::run(long, boost::asio::detail::op_queue<boost::asio::detail::scheduler_operation>&) ()
#3  0x0046ec8a in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#4  0x00623b32 in boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .isra.0] ()
#5  0x00650f24 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 19 (Thread 0x78cfe180 (LWP 5658) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674369a in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 18 (Thread 0x791ff180 (LWP 5657) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674589c in __pthread_cond_timedwait64 () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0xb674595a in pthread_cond_timedwait () from /lib/arm-linux-gnueabihf/libc.so.6
#5  0x0074ec32 in nodetool::socks_connect_internal(std::atomic<bool> const&, boost::asio::io_context&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp> const&, epee::net_utils::network_address const&) ()
#6  0x0067bd06 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::socks_connect(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::network_zone&, epee::net_utils::network_address const&, epee::net_utils::ssl_support_t) ()
#7  0x0068d2be in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long long) ()
#8  0x0068ec3c in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::network_zone&, bool) ()
#9  0x0068ff6a in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::network_zone&, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned int) ()
#10 0x00690f26 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() ()
#11 0x00636156 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() ()
#12 0x0066109e in bool epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > >(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > >) ()
#13 0x0066143a in boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::asio::execution::any_executor<boost::asio::execution::context_as_t<boost::asio::execution_context&>, boost::asio::execution::detail::blocking::never_t<0>, boost::asio::execution::prefer_only<boost::asio::execution::detail::blocking::possibly_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::outstanding_work::tracked_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::outstanding_work::untracked_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::relationship::fork_t<0> >, boost::asio::execution::prefer_only<boost::asio::execution::detail::relationship::continuation_t<0> > > >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#14 0x0046ee32 in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#15 0x00623b32 in boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .isra.0] ()
#16 0x00650f24 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#17 0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#18 0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 17 (Thread 0x798fc180 (LWP 5656) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674369a in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 16 (Thread 0x79dfd180 (LWP 5655) "monerod"):
#0  0x00465740 in bool nodetool::peerlist_entry_base<epee::net_utils::network_address>::serialize_map<true, epee::serialization::portable_storage>(epee::serialization::portable_storage&, epee::serialization::portable_storage::hsection) [clone .isra.0] ()
#1  0x00465f26 in bool epee::serialization::serialize_stl_container_t_obj<std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > >, epee::serialization::portable_storage>(std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > > const&, epee::serialization::portable_storage&, epee::serialization::portable_storage::hsection, char const*) [clone .constprop.0] [clone .isra.0] ()
#2  0x0048fb1a in int epee::net_utils::buff_to_t_adapter<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::request_t>, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::response_t>, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>, std::_Bind<int (nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::*(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>, std::_Placeholder<4>))(int, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::request_t>&, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::response_t>&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)> >(int, epee::span<unsigned char const>, epee::byte_stream&, std::_Bind<int (nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::*(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>, std::_Placeholder<4>))(int, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::request_t>&, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::response_t>&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)>, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#3  0x00491a16 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, epee::span<unsigned char const>, epee::byte_stream&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#4  0x0067e716 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned int) ()
#5  0x0067f152 in boost::asio::detail::completion_handler<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned int)#3}::operator()(boost::system::error_code const&, unsigned int) const::{lambda()#1}, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0u> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#6  0x00541efe in boost::asio::detail::strand_service::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#7  0x0046ee32 in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#8  0x00623b32 in boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .isra.0] ()
#9  0x00650f24 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#10 0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#11 0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 15 (Thread 0x7a2fe180 (LWP 5654) "monerod"):
#0  0x007f35d8 in mdb_page_get.isra ()
#1  0x007f5a20 in mdb_page_search_root ()
#2  0x007f6000 in mdb_cursor_set ()
#3  0x007f6206 in mdb_cursor_set ()
#4  0x007f4e94 in mdb_cursor_get ()
#5  0x007cbe68 in cryptonote::BlockchainLMDB::block_exists(crypto::hash const&, unsigned long long*) const ()
#6  0x006bb792 in cryptonote::Blockchain::have_block_unlocked(crypto::hash const&, int*) const ()
#7  0x006bbdf6 in cryptonote::Blockchain::have_block(crypto::hash const&, int*) const ()
#8  0x00644db4 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::skip_unneeded_hashes(cryptonote::cryptonote_connection_context&, bool) const ()
#9  0x00693534 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::request_missing_objects(cryptonote::cryptonote_connection_context&, bool, bool) ()
#10 0x006994dc in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) ()
#11 0x0069c9ce in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t>&, cryptonote::cryptonote_connection_context&) ()
#12 0x00492920 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, epee::span<unsigned char const>, epee::byte_stream&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#13 0x0067e394 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned int) ()
#14 0x0067f152 in boost::asio::detail::completion_handler<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned int)#3}::operator()(boost::system::error_code const&, unsigned int) const::{lambda()#1}, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0u> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#15 0x00541efe in boost::asio::detail::strand_service::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#16 0x0046ee32 in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#17 0x00623b32 in boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .isra.0] ()
#18 0x00650f24 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#19 0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#20 0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 14 (Thread 0x7aaff180 (LWP 5653) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674589c in __pthread_cond_timedwait64 () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0xb674595a in pthread_cond_timedwait () from /lib/arm-linux-gnueabihf/libc.so.6
#5  0x00648e98 in void boost::this_thread::sleep_for<long long, boost::ratio<1ll, 1ll> >(boost::chrono::duration<long long, boost::ratio<1ll, 1ll> > const&) ()
#6  0x00651c6e in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run()::{lambda()#1}::operator()() const ()
#7  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#8  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 13 (Thread 0x7b683180 (LWP 5652) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb6792db4 in poll () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb6eb8916 in ?? () from /lib/arm-linux-gnueabihf/libzmq.so.5
#3  0xb6e9c46a in ?? () from /lib/arm-linux-gnueabihf/libzmq.so.5
#4  0xb6ebb0a6 in ?? () from /lib/arm-linux-gnueabihf/libzmq.so.5
#5  0xb6ebbc88 in ?? () from /lib/arm-linux-gnueabihf/libzmq.so.5
#6  0xb6ed1c10 in zmq_msg_recv () from /lib/arm-linux-gnueabihf/libzmq.so.5
#7  0x00822dcc in net::zmq::receive[abi:cxx11](void*, int) ()
#8  0x0078ba90 in cryptonote::rpc::ZmqServer::serve() ()
#9  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#10 0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 12 (Thread 0x7be84180 (LWP 5651) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x00454d48 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
#5  0x0045749c in bool epee::async_console_handler::run<epee::async_console_handler::run<std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)> >(std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)>, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)#1}>(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::async_console_handler::run<std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)> >(std::_Bind<bool (epee::command_handler::*(epee::console_handlers_binder*, std::_Placeholder<1>))(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)>, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>)::{lambda(boost::optional<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&)#1} const&, std::function<void ()>) ()
#6  0x00457c48 in epee::console_handlers_binder::run_handling(std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()>) ()
#7  0x004559b8 in boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf3<bool, epee::console_handlers_binder, std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<void ()> >, boost::_bi::list4<boost::_bi::value<epee::console_handlers_binder*>, boost::_bi::value<std::function<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > ()> >, boost::_bi::value<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::_bi::value<std::function<void ()> > > > >::run() ()
#8  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#9  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 11 (Thread 0x7c685180 (LWP 5650) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb679752a in __select64 () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb6797698 in select () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0x00455138 in epee::async_stdin_reader::reader_thread_func() ()
#4  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#5  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 10 (Thread 0x7d4fe180 (LWP 5649) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x0046ed1e in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#5  0x0047175a in boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .isra.0] ()
#6  0x004735fe in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#7  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#8  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 9 (Thread 0x7dcff180 (LWP 5648) "monerod"):
#0  0xb6707616 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb679cafc in epoll_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0x0046dca2 in boost::asio::detail::epoll_reactor::run(long, boost::asio::detail::op_queue<boost::asio::detail::scheduler_operation>&) ()
#3  0x0046ec8a in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#4  0x0047175a in boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .isra.0] ()
#5  0x004735fe in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 8 (Thread 0x7e8fa180 (LWP 5647) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x0046ed1e in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#5  0x0047175a in boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .isra.0] ()
#6  0x004735fe in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#7  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#8  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 7 (Thread 0x7f0fb180 (LWP 5646) "monerod"):
#0  0xb6707616 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb679cafc in epoll_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0x0046dca2 in boost::asio::detail::epoll_reactor::run(long, boost::asio::detail::op_queue<boost::asio::detail::scheduler_operation>&) ()
#3  0x0046ec8a in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#4  0x0047175a in boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .isra.0] ()
#5  0x004735fe in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#6  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#7  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 6 (Thread 0x7f8fc180 (LWP 5645) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674589c in __pthread_cond_timedwait64 () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0xb674595a in pthread_cond_timedwait () from /lib/arm-linux-gnueabihf/libc.so.6
#5  0x008cd632 in epee::misc_utils::sleep_no_w(long) ()
#6  0x0045a766 in boost::detail::thread_data<daemonize::t_daemon::run(bool)::{lambda()#1}>::run() ()
#7  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#8  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 5 (Thread 0x800fd180 (LWP 5644) "ZMQbg/IO/0"):
#0  0xb6707616 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb679cafc in epoll_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb6e95f04 in ?? () from /lib/arm-linux-gnueabihf/libzmq.so.5
#3  0xb6ec8e24 in ?? () from /lib/arm-linux-gnueabihf/libzmq.so.5
#4  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 4 (Thread 0x808fe180 (LWP 5643) "ZMQbg/Reaper"):
#0  0xb6707616 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb679cafc in epoll_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb6e95f04 in ?? () from /lib/arm-linux-gnueabihf/libzmq.so.5
#3  0xb6ec8e24 in ?? () from /lib/arm-linux-gnueabihf/libzmq.so.5
#4  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 2 (Thread 0xa255a180 (LWP 5640) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0x0046ed1e in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#5  0x006d6bb0 in boost::asio::detail::scheduler::run(boost::system::error_code&) ()
#6  0x006d6fac in boost::asio::io_context::run() ()
#7  0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#8  0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)

Thread 1 (Thread 0xb69faa60 (LWP 5636) "monerod"):
#0  0xb6707614 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#1  0xb674339e in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#2  0xb674347c in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
#3  0xb674562a in pthread_cond_wait () from /lib/arm-linux-gnueabihf/libc.so.6
#4  0xb6a36512 in boost::thread::join_noexcept() () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#5  0x0067890e in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned int, bool, boost::thread_attributes const&) ()
#6  0x00679882 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
#7  0x0046fe8a in daemonize::t_p2p::run() ()
#8  0x00463ee0 in daemonize::t_daemon::run(bool) ()
#9  0x004949ec in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#10 0x00437ee4 in main ()
(gdb)
```

## selsta | 2023-05-05T18:58:33+00:00
Thank you, this might be useful.

## motogon | 2023-05-06T06:30:31+00:00
demon stops working 

2023-05-06 06:11:29.041	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-06 06:11:29.042	I Initializing cryptonote protocol...
2023-05-06 06:11:29.042	I Cryptonote protocol initialized OK
2023-05-06 06:11:29.042	I Initializing core...
2023-05-06 06:11:29.043	I Loading blockchain from folder /Users/dend1/.bitmonero/lmdb ...
2023-05-06 06:11:29.254	I Loading checkpoints
2023-05-06 06:11:31.706	I Core initialized OK
2023-05-06 06:11:31.999	I Initializing p2p server...
2023-05-06 06:11:32.011	I p2p server initialized OK
2023-05-06 06:11:32.012	I Initializing core RPC server...
2023-05-06 06:11:32.012	I Binding on 127.0.0.1 (IPv4):18081
2023-05-06 06:11:32.473	I core RPC server initialized OK on port: 18081
2023-05-06 06:11:32.534	I Starting core RPC server...
2023-05-06 06:11:32.534	I core RPC server started ok
2023-05-06 06:11:33.148	I Starting p2p net loop...
2023-05-06 06:11:34.150	I 
2023-05-06 06:11:34.150	I **********************************************************************
2023-05-06 06:11:34.150	I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-05-06 06:11:34.150	I 
2023-05-06 06:11:34.150	I You can set the level of process detailization through "set_log <level|categories>" command,
2023-05-06 06:11:34.151	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-05-06 06:11:34.151	I 
2023-05-06 06:11:34.151	I Use the "help" command to see the list of available commands.
2023-05-06 06:11:34.151	I Use "help <command>" to see a command's documentation.
2023-05-06 06:11:34.151	I **********************************************************************
2023-05-06 06:11:34.664	I [162.218.65.25:18180 OUT] Sync data returned a new top block candidate: 2850808 -> 2879708 [Your node is 28900 blocks (1.3 months) behind] 
2023-05-06 06:11:34.664	I SYNCHRONIZATION started
zsh: killed     ./monerod


## selsta | 2023-05-06T06:32:01+00:00
@motogon While this seems unrelated to this issue, how much RAM do you have? What hardware do you have?

## motogon | 2023-05-06T06:32:56+00:00
imac (intel i7) - ram 32

## selsta | 2023-05-06T06:35:18+00:00
@motogon which macOS version? How did you install monero?

Can you open Console.app, click on Crash and see if there's a monerod crash report?

## motogon | 2023-05-06T06:37:58+00:00
mac os 13.3 using monero-gui-mac-x64-v0.18.2.2.dmg


## motogon | 2023-05-06T06:40:46+00:00
[monerod-2023-05-06-092746.ips.zip](https://github.com/monero-project/monero/files/11411670/monerod-2023-05-06-092746.ips.zip)


## selsta | 2023-05-06T06:55:31+00:00
@motogon do you have some kind of anti virus installed?

## motogon | 2023-05-06T06:56:18+00:00
no 

## motogon | 2023-05-06T07:02:13+00:00
I deleted the file /.bitmonero/lmdb/data.mdb , then run monerod 
Synchronization went to the current level ( 99% ) and then the problem started. 

## selsta | 2023-05-06T07:03:10+00:00
macOS is killing monerod and I don't know why yet, I haven't seen this on other macOS systems before.

## motogon | 2023-05-06T07:07:17+00:00
> macOS is killing monerod

and the problem occurs at 99% synchronization 

## motogon | 2023-05-06T07:18:29+00:00
2023-05-05 19:46:14.516	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687	Synced 2850688/2879431 (99%, 28743 left)
2023-05-05 19:46:14.782	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687	Synced 2850708/2879431 (99%, 28723 left)
2023-05-05 19:46:15.720	[P2P0]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687	Synced 2850728/2879431 (99%, 28703 left)
2023-05-05 19:46:16.068	[P2P0]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687	Synced 2850748/2879431 (99%, 28683 left)
2023-05-05 19:46:16.431	[P2P0]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687	Synced 2850768/2879431 (99%, 28663 left)
2023-05-05 19:46:16.846	[P2P0]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687	Synced 2850788/2879431 (99%, 28643 left)
2023-05-05 19:46:17.269	[P2P0]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1687	Synced 2850808/2879431 (99%, 28623 left)
2023-05-06 05:46:46.703	  0x7ff84b4a65c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-05-06 05:46:46.705	  0x7ff84b4a65c0	INFO	global	src/daemon/main.cpp:296	Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-05-06 05:46:46.705	  0x7ff84b4a65c0	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2023-05-06 05:46:46.707	  0x7ff84b4a65c0	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Fluorine Fermi' (v0.18.2.2-release) Daemonised
2023-05-06 05:46:46.708	  0x7ff84b4a65c0	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2023-05-06 05:46:46.708	  0x7ff84b4a65c0	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2023-05-06 05:46:46.709	  0x7ff84b4a65c0	INFO	global	src/daemon/core.h:64	Initializing core...
2023-05-06 05:46:46.709	  0x7ff84b4a65c0	INFO	global	src/cryptonote_core/cryptonote_core.cpp:523	Loading blockchain from folder /Users/dend/.bitmonero/lmdb ...
2023-05-06 05:46:46.860	  0x7ff84b4a65c0	INFO	global	src/cryptonote_core/cryptonote_core.cpp:698	Loading checkpoints
2023-05-06 05:46:48.593	  0x7ff84b4a65c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-05-06 05:46:48.595	  0x7ff84b4a65c0	INFO	global	src/daemon/main.cpp:296	Monero 'Fluorine Fermi' (v0.18.2.2-release)


## k4r4b3y | 2023-05-06T09:01:04+00:00
@motogon I am not sure if your issue is related to mine.

## motogon | 2023-05-06T09:20:01+00:00
> I am not sure if your issue is related to mine.

I suppose it may be related. 
How can it be explained, up to 99% works, and at the last percentage " crashes ". 
Perhaps monerod is trying to do, which leads to a crash

## selsta | 2023-05-06T09:20:46+00:00
@motogon it's not related, can you open a separate issue?

## selsta | 2023-05-06T09:24:30+00:00
@k4r4b3y can you install a 64bit operating system?

## k4r4b3y | 2023-05-06T09:28:45+00:00
@selsta unfortunately not. My odroid hc1 hardware has 32-bit CPU, afaik.

Apart from that hardware, I also have a raspberry pi 4 that I can install a 64-bit CPU and try monerod there. However, I am more interested in learning & fixing the problem I am having on 32-bit monerod.

## selsta | 2023-05-06T09:31:23+00:00
@k4r4b3y my guess is that the `--anonymous-incoming` code is broken on 32bit and since we rarely see 32 bit nodes in combination with anonymous-incoming it wasn't noticed yet.

## k4r4b3y | 2023-05-06T09:31:58+00:00
>my guess is that the --anonymous-incoming code is broken on 32bit and since we rarely see 32 bit nodes in combination with anonymous-incoming it wasn't noticed yet.

Oh that's a bummer. So there is not much I can do to fix that..

## motogon | 2023-05-06T09:34:43+00:00
> @motogon it's not related, can you open a separate issue?

https://github.com/monero-project/monero/issues/8841

## selsta | 2023-05-08T18:02:51+00:00
@k4r4b3y

Can you run the following unit tests and check if they succeed?

```
make
cd build/<hostname>/<branch>/release/tests/unit_tests/
./unit_tests --gtest_filter='tor_address.*'
```

## k4r4b3y | 2023-05-11T13:14:09+00:00
@selsta sorry for late reply. I just saw your message. I will try your unit tests and return back this afternoon.

## k4r4b3y | 2023-05-13T05:45:18+00:00
@selsta here's the output:
```
user@DietPi:~/.local/src/monero$ cd build/Linux/_HEAD_detached_at_v0.18.2.2_/release/tests/unit_tests/
user@DietPi:~/.local/src/monero/build/Linux/_HEAD_detached_at_v0.18.2.2_/release/tests/unit_tests$ ./unit_tests --gtest_filter='tor_address.*'
Note: Google Test filter = tor_address.*
[==========] Running 11 tests from 1 test suite.
[----------] Global test environment set-up.
[----------] 11 tests from tor_address
[ RUN      ] tor_address.constants
[       OK ] tor_address.constants (0 ms)
[ RUN      ] tor_address.invalid
[       OK ] tor_address.invalid (18 ms)
[ RUN      ] tor_address.unblockable_types
[       OK ] tor_address.unblockable_types (0 ms)
[ RUN      ] tor_address.valid
[       OK ] tor_address.valid (0 ms)
[ RUN      ] tor_address.generic_network_address
[       OK ] tor_address.generic_network_address (1 ms)
[ RUN      ] tor_address.epee_serializev_v2
[       OK ] tor_address.epee_serializev_v2 (3 ms)
[ RUN      ] tor_address.epee_serializev_v3
[       OK ] tor_address.epee_serializev_v3 (0 ms)
[ RUN      ] tor_address.epee_serialize_unknown
[       OK ] tor_address.epee_serialize_unknown (0 ms)
[ RUN      ] tor_address.boost_serialize_v2
[       OK ] tor_address.boost_serialize_v2 (0 ms)
[ RUN      ] tor_address.boost_serialize_v3
[       OK ] tor_address.boost_serialize_v3 (0 ms)
[ RUN      ] tor_address.boost_serialize_unknown
[       OK ] tor_address.boost_serialize_unknown (0 ms)
[----------] 11 tests from tor_address (24 ms total)

[----------] Global test environment tear-down
[==========] 11 tests from 1 test suite ran. (26 ms total)
[  PASSED  ] 11 tests.
user@DietPi:~/.local/src/monero/build/Linux/_HEAD_detached_at_v0.18.2.2_/release/tests/unit_tests$
```

hope this helps.

## vtnerd | 2023-05-17T15:04:53+00:00
@selsta I think `--anonymous-inbound` is a (partially) red-herring, looking at the relevant stacktrace:
```
Thread 16 (Thread 0x79dfd180 (LWP 5655) "monerod"):
#0  0x00465740 in bool nodetool::peerlist_entry_base<epee::net_utils::network_address>::serialize_map<true, epee::serialization::portable_storage>(epee::serialization::portable_storage&, epee::serialization::portable_storage::hsection) [clone .isra.0] ()
#1  0x00465f26 in bool epee::serialization::serialize_stl_container_t_obj<std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > >, epee::serialization::portable_storage>(std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > > const&, epee::serialization::portable_storage&, epee::serialization::portable_storage::hsection, char const*) [clone .constprop.0] [clone .isra.0] ()
#2  0x0048fb1a in int epee::net_utils::buff_to_t_adapter<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::request_t>, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::response_t>, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>, std::_Bind<int (nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::*(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>, std::_Placeholder<4>))(int, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::request_t>&, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::response_t>&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)> >(int, epee::span<unsigned char const>, epee::byte_stream&, std::_Bind<int (nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::*(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>, std::_Placeholder<4>))(int, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::request_t>&, epee::misc_utils::struct_init<nodetool::COMMAND_TIMED_SYNC_T<cryptonote::CORE_SYNC_DATA>::response_t>&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)>, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#3  0x00491a16 in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, epee::span<unsigned char const>, epee::byte_stream&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#4  0x0067e716 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned int) ()
#5  0x0067f152 in boost::asio::detail::completion_handler<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned int)#3}::operator()(boost::system::error_code const&, unsigned int) const::{lambda()#1}, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0u> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#6  0x00541efe in boost::asio::detail::strand_service::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#7  0x0046ee32 in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#8  0x00623b32 in boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .isra.0] ()
#9  0x00650f24 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#10 0xb6a35a7c in ?? () from /lib/arm-linux-gnueabihf/libboost_thread.so.1.74.0
#11 0xb6745cf6 in ?? () from /lib/arm-linux-gnueabihf/libc.so.6
```
This is in the serialization code for peerlists somehow.

## vtnerd | 2023-05-17T15:06:10+00:00
EDIT: Above, nevermind looks like you dug into that a bit with the unit test thing. But yeah I don't have much to go on either, I have no 32-bit arm systems I can use for testing.

## k4r4b3y | 2023-05-23T09:50:19+00:00
In a week, that node should finish blockchain sync. Currently, it is doing the sync without `anonymous-inbound` directive in its config. After the sync completes, I will try re-enabling the tor anonymous-inbound directive and see if it can work that way.

Another thing I will try is using the binaries compiled by the monero-project, instead of using the ones I have compiled inside the 32-bit dietpiOS.

## k4r4b3y | 2023-05-29T19:08:14+00:00
The node has finished synchronizing with the network. I have re-enabled the tor anonymous-inbound directive. 

Sadly, the same issue as I reported in the OP continues.

# Action History
- Created by: k4r4b3y | 2023-05-05T08:33:23+00:00
