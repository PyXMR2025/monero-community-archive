---
title: boost::wrapexcept<boost::system::system_error> during startup.
source_url: https://github.com/monero-project/monero/issues/7378
author: crocket
assignees: []
labels: []
created_at: '2021-02-12T01:19:42+00:00'
updated_at: '2022-02-19T00:30:39+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:30:38+00:00'
---

# Original Description
Monero 0.17.1.9

```
2021-02-12 01:17:41.619     7f43b93bee00        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-02-12 01:17:41.619     7f43b93bee00        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-02-12 01:17:41.619     7f43b93bee00        INFO    global  src/daemon/main.cpp:294 Monero 'Oxygen Orion' (v0.17.1.9-unknown)
2021-02-12 01:17:41.619     7f43b93bee00        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2021-02-12 01:17:41.620     7f43b93bee00        WARNING daemon  src/daemon/executor.cpp:61      Monero 'Oxygen Orion' (v0.17.1.9-unknown) Daemonised
2021-02-12 01:17:41.620     7f43b93bee00        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2021-02-12 01:17:41.620     7f43b93bee00        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2021-02-12 01:17:41.620     7f43b93bee00        INFO    global  src/daemon/core.h:63    Initializing core...
2021-02-12 01:17:41.620     7f43b93bee00        INFO    global  src/cryptonote_core/cryptonote_core.cpp:515     Loading blockchain from folder /data/monero/lmdb ...
2021-02-12 01:17:41.655     7f43b93bee00        INFO    global  src/cryptonote_core/cryptonote_core.cpp:690     Loading checkpoints
2021-02-12 01:17:41.656     7f43b93bee00        INFO    global  src/daemon/core.h:73    Core initialized OK
2021-02-12 01:17:41.656     7f43b93bee00        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2021-02-12 01:17:41.659     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::wrapexcept<boost::system::system_error>
2021-02-12 01:17:41.659     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x113) [0x55d6b777b8ea]:__cxa_throw+0x113) [0x55d6b777b8ea]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [2]  0x87) [0x55d6b774eda1]:_ZN5boost15throw_exceptionINS_6system12system_errorEEEvRKT_+0x87) [0x55d6b774eda1]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x73) [0x55d6b780c203]:_ZN5boost4asio6detail14do_throw_errorERKNS_6system10error_codeEPKc+0x73) [0x55d6b780c203]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0x1bb9) [0x55d6b7b6b439]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11init_serverEjRKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEjSI_bbNS0_13ssl_options_tE+0x1bb9) [0x55d6b7b6b439]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x1bb) [0x55d6b7b6ef5b]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11init_serverENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERKSG_SG_SG_bbNS0_13ssl_options_tE+0x1bb) [0x55d6b7b6ef5b]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0x669) [0x55d6b7b6fc89]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE4initERKN5boost15program_options13variables_mapE+0x669) [0x55d6b7b6fc89]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [7]  0x362) [0x55d6b78a3212]:_ZN9daemonize11t_internalsC1ERKN5boost15program_options13variables_mapE+0x362) [0x55d6b78a3212]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [8]  0x2f) [0x55d6b77fa6bf]:_ZN9daemonize8t_daemonC2ERKN5boost15program_options13variables_mapEt+0x2f) [0x55d6b77fa6bf]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [9]  0x1bb) [0x55d6b78a452b]:_ZN9daemonize10t_executor13create_daemonERKN5boost15program_options13variables_mapE+0x1bb) [0x55d6b78a452b]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [10]  0x2f5) [0x55d6b78ade75]:_ZN10daemonizer9daemonizeIN9daemonize10t_executorEEEbiPPKcOT_RKN5boost15program_options13variables_mapE+0x2f5) [0x55d6b78ade75]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/bin/monerod(main+0x1361) [0x55d6b77c5ca1]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0xeb) [0x7f43b94c9e6b]:__libc_start_main+0xeb) [0x7f43b94c9e6b]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172      [13]  0x2a) [0x55d6b77d3bfa]:_start+0x2a) [0x55d6b77d3bfa]
2021-02-12 01:17:41.660     7f43b93bee00        INFO    stacktrace      src/common/stack_trace.cpp:172
2021-02-12 01:17:41.660     7f43b93bee00        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2021-02-12 01:17:41.660     7f43b93bee00        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2021-02-12 01:17:41.660     7f43b93bee00        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 127.0.0.1 (IPv4):18081
2021-02-12 01:17:41.660     7f43b93bee00        INFO    global  contrib/epee/include/net/http_server_impl_base.h:82     Binding on ::1 (IPv6):18081
2021-02-12 01:17:41.961     7f43b93bee00        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2021-02-12 01:17:41.961     7f43b93bee00        INFO    global  src/daemon/rpc.h:63     Initializing restricted RPC server...
2021-02-12 01:17:41.961     7f43b93bee00        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 0.0.0.0 (IPv4):18089
2021-02-12 01:17:41.961     7f43b93bee00        INFO    global  contrib/epee/include/net/http_server_impl_base.h:82     Binding on :: (IPv6):18089
2021-02-12 01:17:42.143     7f43b93bee00        INFO    global  src/daemon/rpc.h:69     restricted RPC server initialized OK on port: 18089
2021-02-12 01:17:42.143     7f43b93bee00        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2021-02-12 01:17:42.143 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2021-02-12 01:17:42.143 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:74     Starting restricted RPC server...
2021-02-12 01:17:42.143 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     restricted RPC server started ok
2021-02-12 01:17:42.143 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:213       Public RPC port 18089 will be advertised to other peers over P2P
2021-02-12 01:17:42.143 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2021-02-12 01:17:43.143 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1726
2021-02-12 01:17:43.143 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1726    **********************************************************************
2021-02-12 01:17:43.143 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1726    The daemon will start synchronizing with the network. This may take a long time to complete.
2021-02-12 01:17:43.143 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1726
2021-02-12 01:17:43.143 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1726    You can set the level of process detailization through "set_log <level|categories>" command,
2021-02-12 01:17:43.143 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1726    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2021-02-12 01:17:43.143 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1726
2021-02-12 01:17:43.143 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1726    Use the "help" command to see the list of available commands.
2021-02-12 01:17:43.143 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1726    Use "help <command>" to see a command's documentation.
2021-02-12 01:17:43.143 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1726    **********************************************************************
2021-02-12 01:17:43.647 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2446
2021-02-12 01:17:43.647 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2446    **********************************************************************
2021-02-12 01:17:43.647 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2446    You are now synchronized with the network. You may now start monero-wallet-cli.
2021-02-12 01:17:43.647 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2446
2021-02-12 01:17:43.647 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2446    Use the "help" command to see the list of available commands.
2021-02-12 01:17:43.647 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2446    **********************************************************************
```

# Discussion History
## selsta | 2022-02-19T00:30:38+00:00
This appears to be just an uncaught exception. You didn't report any other issues and the daemon seems to start correctly from your logs so I'll close this.

# Action History
- Created by: crocket | 2021-02-12T01:19:42+00:00
- Closed at: 2022-02-19T00:30:38+00:00
