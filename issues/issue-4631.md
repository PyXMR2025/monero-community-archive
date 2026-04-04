---
title: Syncing issues with the new v0.13.0.x-release
source_url: https://github.com/monero-project/monero/issues/4631
author: mmitech
assignees: []
labels: []
created_at: '2018-10-16T18:32:40+00:00'
updated_at: '2018-10-23T11:17:01+00:00'
type: issue
status: closed
closed_at: '2018-10-23T11:17:01+00:00'
---

# Original Description
After the upgrade monerod can't connect to the network! bellow are the logs (with a restart issued once)

System: Ubuntu Server 16.04.5/amd64
ufw 18080


```
2018-10-16 12:15:07.454     7f4462a6e780        INFO    global  src/daemon/main.cpp:287 Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-16 12:15:07.454     7f4462a6e780        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2018-10-16 12:15:07.455     7f4462a6e780        WARN    daemon  src/daemon/executor.cpp:61      Monero 'Beryllium Bullet' (v0.13.0.2-release) Daemonised
2018-10-16 12:15:07.455     7f4462a6e780        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-10-16 12:15:07.455     7f4462a6e780        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-10-16 12:15:07.455     7f4462a6e780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-10-16 12:15:11.523     7f4462a6e780        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-10-16 12:15:11.524     7f4462a6e780        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-10-16 12:15:11.524     7f4462a6e780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:6666
2018-10-16 12:15:11.524     7f4462a6e780        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 6666
2018-10-16 12:15:11.524     7f4462a6e780        INFO    global  src/daemon/core.h:86    Initializing core...
2018-10-16 12:15:11.524     7f4462a6e780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:447     Loading blockchain from folder /home/monero/.bitmonero/lmdb ...
2018-10-16 12:15:11.525     7f4462a6e780        INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:4071 Migrating blockchain from DB version 1 to 2 - this may take a while:
2018-10-16 14:20:02.075     7f4462a6e780        INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:4213 Migrating blockchain from DB version 2 to 3 - this may take a while:
2018-10-16 14:21:41.925     7f4462a6e780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:585     Loading checkpoints
2018-10-16 14:21:41.954     7f4462a6e780        WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-10-16 14:21:41.954     7f4462a6e780        INFO    global  src/daemon/core.h:92    Core initialized OK
2018-10-16 14:21:41.954     7f4462a6e780        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2018-10-16 14:21:41.955 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2018-10-16 14:21:41.957 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2018-10-16 14:21:42.961 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1484
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************

2018-10-16 14:21:42.989 [P2P2]  WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-10-16 14:21:43.519 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [69.47.19.85:18080 OUT] Sync data returned a new top block candidate: 1684133 -> 1684192 [Your node is 59 blocks (0 days) behind]
SYNCHRONIZATION started
2018-10-16 14:21:52.817 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182    [69.47.19.85:18080 OUT]  Synced 1684153/1684192
2018-10-16 14:21:59.644 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182    [69.47.19.85:18080 OUT]  Synced 1684173/1684192
2018-10-16 14:22:10.138 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182    [69.47.19.85:18080 OUT]  Synced 1684192/1684192
2018-10-16 14:22:10.139 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1576    SYNCHRONIZED OK
2018-10-16 14:22:10.139 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1598
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-10-16 14:22:38.470 [P2P1]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 14:37:39.204 [P2P4]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 14:46:34.406 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped
2018-10-16 14:46:34.543     7f445f177700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::thread_interrupted
2018-10-16 14:46:34.543     7f445f177700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2018-10-16 14:46:34.556     7f445f177700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod:__wrap___cxa_throw+0x10a [0x5631338b81aa]
2018-10-16 14:46:34.556     7f445f177700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod:boost::this_thread::interruption_point()+0x76 [0x563133c981a6]
2018-10-16 14:46:34.556     7f445f177700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod:cryptonote::rpc::ZmqServer::serve()+0x935 [0x5631338cacf5]
2018-10-16 14:46:34.556     7f445f177700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod+0x9ff34d [0x563133c9834d]
2018-10-16 14:46:34.556     7f445f177700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7f44621576ba]
2018-10-16 14:46:34.556     7f445f177700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f4461e8d41d]
2018-10-16 14:46:34.556     7f445f177700        INFO    stacktrace      src/common/stack_trace.cpp:172
2018-10-16 14:46:34.560 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:84     Stopping core RPC server...
2018-10-16 14:46:34.560 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:190       Node stopped.
2018-10-16 14:46:34.560 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2018-10-16 14:46:34.564 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2018-10-16 14:46:39.169 [SRV_MAIN]      INFO    global  src/daemon/core.h:103   Deinitializing core...
2018-10-16 14:46:39.903 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2018-10-16 14:46:39.903 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully
2018-10-16 14:46:40.976     7fcd0283c780        INFO    logging contrib/epee/src/mlog.cpp:242   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-16 14:46:40.976     7fcd0283c780        INFO    global  src/daemon/main.cpp:287 Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-16 14:46:40.976     7fcd0283c780        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2018-10-16 14:46:40.977     7fcd0283c780        WARN    daemon  src/daemon/executor.cpp:61      Monero 'Beryllium Bullet' (v0.13.0.2-release) Daemonised
2018-10-16 14:46:40.977     7fcd0283c780        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-10-16 14:46:40.977     7fcd0283c780        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-10-16 14:46:40.977     7fcd0283c780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-10-16 14:46:45.043     7fcd0283c780        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-10-16 14:46:45.044     7fcd0283c780        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-10-16 14:46:45.046     7fcd0283c780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:6666
2018-10-16 14:46:45.046     7fcd0283c780        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 6666
2018-10-16 14:46:45.046     7fcd0283c780        INFO    global  src/daemon/core.h:86    Initializing core...
2018-10-16 14:46:45.046     7fcd0283c780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:447     Loading blockchain from folder /home/monero/.bitmonero/lmdb ...
2018-10-16 14:46:45.094     7fcd0283c780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:585     Loading checkpoints
2018-10-16 14:46:45.103     7fcd0283c780        WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-10-16 14:46:45.104     7fcd0283c780        INFO    global  src/daemon/core.h:92    Core initialized OK
2018-10-16 14:46:45.104     7fcd0283c780        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2018-10-16 14:46:45.104 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2018-10-16 14:46:45.104 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2018-10-16 14:46:46.105 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1484
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************

2018-10-16 14:46:46.121 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-10-16 14:46:46.675 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1598
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-10-16 15:01:41.173 [P2P2]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 15:16:42.057 [P2P1]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 15:31:43.587 [P2P8]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 15:46:44.454 [P2P2]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 15:48:08.978 [P2P0]  WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-10-16 16:01:45.530 [P2P9]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 16:16:46.637 [P2P5]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 16:31:47.713 [P2P2]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 16:46:48.952 [P2P3]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 16:49:53.550 [P2P8]  WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-10-16 17:01:49.758 [P2P9]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 17:16:50.747 [P2P7]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 17:31:51.741 [P2P4]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 17:46:52.883 [P2P9]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 17:50:45.714 [P2P2]  WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-10-16 18:01:53.834 [P2P2]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
2018-10-16 18:05:01.107 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
2018-10-16 18:05:01.107 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/bin/monerod:__wrap___cxa_throw+0x10a [0x558d4cd8e1aa]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod:void boost::throw_exception<boost::bad_weak_ptr>(boost::bad_weak_ptr const&)+0x12d [0x558d4ca7987d]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::safe_shared_from_this()+0x8a [0x558d4cc49afa]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0x35 [0x558d4cc5c565]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3a2 [0x558d4cc398c2]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x48c [0x558d4cc8438c]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::check_connection_and_handshake_with_peer(epee::net_utils::network_address const&, unsigned long)+0x663 [0x558d4cc97773]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::gray_peerlist_housekeeping()+0x148 [0x558d4cc980b8]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0xb8 [0x558d4cc2d328]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x27 [0x558d4cc46687]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x109 [0x558d4cc2da29]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x844 [0x558d4cc444a4]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/bin/monerod+0x9ff34d [0x558d4d16e34d]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fcd01f256ba]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fcd01c5b41d]
2018-10-16 18:05:01.118 [P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:172
2018-10-16 18:16:54.698 [P2P1]  WARN    global  src/p2p/net_node.inl:1338       No incoming connections - check firewalls/routers allow port 18080
```

```
~$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
18080                       ALLOW      Anywhere
```



# Discussion History
## dEBRUYNE-1 | 2018-10-16T18:45:43+00:00
Bit of an obvious question, but have you tried restarting the daemon (monerod)?

## mmitech | 2018-10-16T18:54:09+00:00
> Bit of an obvious question, but have you tried restarting the daemon (monerod)?

yes, see in the logs it include a restart.

## dEBRUYNE-1 | 2018-10-16T19:55:16+00:00
Missed that, apologies. 

## moneromooo-monero | 2018-10-16T20:12:36+00:00
If you mean the warning messages, did you configure your router to forward port 18080 to your computer running monerod ?

## mmitech | 2018-10-16T20:23:29+00:00
> If you mean the warning messages, did you configure your router to forward port 18080 to your computer running monerod ?

No, this is on AWS and the security group allows the P2P port, it worked just fine before, as you can see from the logs it was syncing ( Synced 1684192/1684192) up until I updated.



## moneromooo-monero | 2018-10-16T20:31:51+00:00
Well, it's done syncing, and it doesn't print such messages when it's just keeping up.
What does "status" show ?

## myaeon-ru | 2018-10-18T22:23:29+00:00
is it normal? this after update daemon from v12 to v13 version

2018-10-18 22:22:53.371	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] [priority]Connect failed to 184.59.137.43:18081
2018-10-18 22:22:53.371	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 176.197.0.214:18080
2018-10-18 22:22:53.371	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 173.31.196.23:18080
2018-10-18 22:22:53.372	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 91.195.42.135:18080
2018-10-18 22:22:53.372	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 47.75.113.228:18080
2018-10-18 22:22:53.372	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 82.200.204.118:18080
2018-10-18 22:22:53.372	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 128.173.236.119:18080
2018-10-18 22:22:53.372	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 128.199.179.100:18080
2018-10-18 22:22:53.372	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 118.171.13.210:18080
2018-10-18 22:22:53.372	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 188.233.12.226:18080
2018-10-18 22:22:53.373	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 147.175.187.111:18080
2018-10-18 22:22:53.373	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 71.218.154.32:18080
2018-10-18 22:22:53.373	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 76.174.86.132:18080
2018-10-18 22:22:53.374	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 68.37.27.79:18080
2018-10-18 22:22:53.374	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 5.251.218.89:18080
2018-10-18 22:22:53.374	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 202.112.0.100:18080
2018-10-18 22:22:53.374	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 71.212.75.94:18080
2018-10-18 22:22:53.375	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 222.210.23.148:18080
2018-10-18 22:22:53.375	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 192.227.232.22:18080
2018-10-18 22:22:53.375	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 94.112.87.155:18080
2018-10-18 22:22:53.376	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:946	[0.0.0.0:0 OUT] Connect failed to 188.234.245.186:18080
2018-10-18 22:22:53.376	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1246	Failed to connect to any, trying seeds

## moneromooo-monero | 2018-10-19T08:46:08+00:00
Any particular things you should tell us about your network/connection ?

## myaeon-ru | 2018-10-19T13:50:35+00:00
> Any particular things you should tell us about your network/connection ?
Direct connection without any firewall's or any other things that can be blocked input / output traffic.
I told before, only compiled from source new v13, replaced binary's that was before and that's all.

i repeat again - i have pool and on v12 binary's all was fine.

/usr/local/bin/monerod --config-file /etc/monerod.conf --pidfile /run/monerod.pid
```
cat monerod.conf 
data-dir=/home/monero/.bitmonero
log-file=/var/log/monero.log
log-level=0
no-igd=1
hide-my-port=1
db-salvage=1
p2p-bind-ip=127.0.0.1
rpc-bind-ip=127.0.0.1
restricted-rpc=1

```


## moneromooo-monero | 2018-10-19T14:03:18+00:00
p2p-bind-ip=127.0.0.1

That's for loopback interface only (local machine connections).


## moneromooo-monero | 2018-10-19T14:03:52+00:00
db-salvage=1

And that's weird, it'll take out the last db transaction at every startup. It *should* work though.

## myaeon-ru | 2018-10-19T14:15:23+00:00
> p2p-bind-ip=127.0.0.1
> That's for loopback interface only (local machine connections).

Exactly that, but why if i don't want open my p2p port for other's ?!
Ok i must support network - but it should be my wish!
Main problem was when share - upcomming traffic grow up to 50Mb/s it was terrible!
Also in case of sharing was many log's warning about "died" or "unsupported" pools - they try synchronize with many errors 


## myaeon-ru | 2018-10-19T14:20:30+00:00
> p2p-bind-ip=127.0.0.1
> 
> That's for loopback interface only (local machine connections).

```
root@root:~# netstat -nap | grep monerod
tcp        0      0 **0.0.0.0:18080**           0.0.0.0:*               LISTEN      24737/monerod   
tcp        0      0 127.0.0.1:18081         0.0.0.0:*               LISTEN      24737/monerod   
tcp        0      0 127.0.0.1:18082         0.0.0.0:*               LISTEN      24737/monerod
```
Look's not so good - 0.0.0.0 ! I don't want this!
What if i want manage incoming via firewall, what if want manage multiply adapter

## myaeon-ru | 2018-10-19T14:38:10+00:00
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-10-19 14:24:09.543	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1576	SYNCHRONIZED OK
*** Error in `/usr/local/bin/monerod': double free or corruption (!prev): 0x00007f82141d0470 ***
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x777e5)[0x7f8229b897e5]
/lib/x86_64-linux-gnu/libc.so.6(+0x8037a)[0x7f8229b9237a]
/lib/x86_64-linux-gnu/libc.so.6(cfree+0x4c)[0x7f8229b9653c]
/usr/local/bin/monerod(_ZNSt6vectorIN6crypto4hashESaIS1_EEaSERKS3_+0xeb)[0x564761d93b6b]
/usr/local/bin/monerod(_ZN10cryptonote5blockaSERKS0_+0x1d6)[0x564761ee6046]
/usr/local/bin/monerod(_ZN10cryptonote10Blockchain20cache_block_templateERKNS_5blockERKNS_22account_public_addressERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERKmmm+0x122)[0x564761eda4c2]
/usr/local/bin/monerod(_ZN10cryptonote10Blockchain21create_block_templateERNS_5blockERKNS_22account_public_addressERmS6_S6_RKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x1416)[0x564761edb9c6]
/usr/local/bin/monerod(_ZN10cryptonote15core_rpc_server19on_getblocktemplateERKNS_28COMMAND_RPC_GETBLOCKTEMPLATE7requestERNS1_8responseERN4epee8json_rpc5errorE+0x2ed)[0x564761d8e07d]
/usr/local/bin/monerod(_ZN10cryptonote15core_rpc_server23handle_http_request_mapIN4epee9net_utils23connection_context_baseEEEbRKNS3_4http17http_request_infoERNS5_18http_response_infoERT_+0x1213f)[0x564761cea6bf]
/usr/local/bin/monerod(_ZN10cryptonote15core_rpc_server19handle_http_requestERKN4epee9net_utils4http17http_request_infoERNS3_18http_response_infoERNS2_23connection_context_baseE+0x179)[0x564761cf62a9]
/usr/local/bin/monerod(_ZN4epee9net_utils4http19http_custom_handlerINS0_23connection_context_baseEE14handle_requestERKNS1_17http_request_infoERNS1_18http_response_infoE+0xaa)[0x564761cc04aa]
/usr/local/bin/monerod(_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE32handle_request_and_send_responseERKNS1_17http_request_infoE+0x13e)[0x564761c7f47e]
/usr/local/bin/monerod(_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE27handle_retriving_query_bodyEv+0x190)[0x564761c7f8b0]
/usr/local/bin/monerod(_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE14handle_buff_inERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x1a0)[0x564761cfa1d0]
/usr/local/bin/monerod(_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE11handle_recvEPKvm+0x3b)[0x564761cfa88b]
/usr/local/bin/monerod(_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE11handle_readERKN5boost6system10error_codeEm+0x228)[0x564761cfab18]
/usr/local/bin/monerod(_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSA_4http19http_custom_handlerINSA_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISG_EEEEPFNS_3argILi1EEEvEPFNSR_ILi2EEEvEEEEESI_mEEEEvRPNS2_11strand_implERT_+0x7a)[0x564761cb909a]


## moneromooo-monero | 2018-10-19T21:20:33+00:00
Are you able to run that with valgrind or ASAN ?

## moneromooo-monero | 2018-10-19T21:27:44+00:00
Anyway, the bind patch was reverted already, it had unexpected impact on some tor uses.

## lh1008 | 2018-10-20T17:06:52+00:00
Hi guys, I'm receiving the same message. I never had any problems with my connection, the message appears again and again during synchronization.

https://paste.fedoraproject.org/paste/7sS~Ct--ldrtfVO1Gm0gOg

## moneromooo-monero | 2018-10-20T17:28:43+00:00
Your log seems OK, except for no incoming connections.
Did you make sure your router is setup to route 18080 to your node to enable those ?

## myaeon-ru | 2018-10-21T12:58:57+00:00
> Anyway, the bind patch was reverted already, it had unexpected impact on some tor uses.

Can you give number of merged request or may be show in code - i will remove it from my sources manual. Asked only because many changes already was done in upstream and hard to find out where it.
Thank you.

## moneromooo-monero | 2018-10-21T13:34:52+00:00
76d6d832

## lh1008 | 2018-10-21T16:28:28+00:00
@moneromooo-monero I have never changed or done any configuration with my router so all of this is pretty new to me. Not sure how to setup a route for 18080 in my router. I will have to read about it. Btw, I have ubuntu 18.04 LTS xenial, and never changed any configuration to my pc (not that I'm aware of). I will be back once I enable 18080. If I'm not able to do it, I will still be sending a message asking for help. :)

## iDunk5400 | 2018-10-21T16:42:42+00:00
@lh1008 The message you are seeing is not an error. It's simply telling you that there are 0 incoming connections, which you can see if you type `status` in your daemon. It's about the `0(in)` bit in `8(out)+0(in) connections`.
You may want to route your port 18080 to your PC where you run the daemon, or you may not. How to do that is beyond the scope of this issue tracker.

## myaeon-ru | 2018-10-21T18:20:12+00:00
> [76d6d83](https://github.com/monero-project/monero/commit/76d6d832d2a43ff03acf9b4ce7b5f0f9e34231e2)

Can confirm - after revert, my error at config 
`p2p-bind-ip=127.0.0.1`
was gone, at now moment synchronization from localhost work fine as before.
Thank you. 

## moneromooo-monero | 2018-10-23T11:14:26+00:00
+resolved

# Action History
- Created by: mmitech | 2018-10-16T18:32:40+00:00
- Closed at: 2018-10-23T11:17:01+00:00
