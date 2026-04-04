---
title: monerod log-file spamming by <boost::bad_weak_ptr>
source_url: https://github.com/monero-project/monero/issues/4365
author: trasherdk
assignees: []
labels: []
created_at: '2018-09-12T10:44:41+00:00'
updated_at: '2020-05-02T18:08:42+00:00'
type: issue
status: closed
closed_at: '2020-05-02T18:08:42+00:00'
---

# Original Description
I'm currently running 3 nodes and 2 wallets (cli). Both wallets connected to a separate node,
with mining running on their respective nodes. No problem, nothing in the log-file.
Issuing stop_mining in one wallet, triggered the following log entries, that keeps repeating.
The node is still syncing, and functioning, but only the excessive logging, roughly 10-15 min. apart.


	
	 [miner 0] INFO global  src/cryptonote_basic/miner.cpp:508  Miner thread stopped [0]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:124  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:125  Unwound call stack:
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [1] ${HOME}/bin/monerod:tools::log_stack_trace(char const*)+0x9e2 [0x565036352842]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [2] ${HOME}/bin/monerod:__cxa_throw+0x14b [0x5650363543eb]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [3] ${HOME}/bin/monerod+0x62cc95 [0x5650360c5c95]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [4] ${HOME}/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::safe_shared_from_this()+0xd9 [0x565036110ff9]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [5] ${HOME}/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0x95 [0x565036139585]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [6] ${HOME}/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x358 [0x5650360ef758]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [7] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x622 [0x5650361773e2]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [8] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0xa1c [0x56503619939c]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [9] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connect_to_seed()+0x30b [0x56503619d8fb]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [10] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x523 [0x56503619ea83]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [11] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x15e [0x5650360d5aae]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [12] ${HOME}/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x67 [0x56503610b8e7]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [13] ${HOME}/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x265 [0x5650360d6865]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [14] ${HOME}/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x10ee [0x56503610685e]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [15] /usr/lib64/libboost_thread.so.1.59.0+0x115a5 [0x7fc0ddb675a5]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [16] /lib64/libpthread.so.0+0x7684 [0x7fc0dd0a4684]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163  [17] /lib64/libc.so.6:clone+0x6d [0x7fc0dcddaeed]
	 [P2P4] INFO stacktrace src/common/stack_trace.cpp:163
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:124  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:125  Unwound call stack:
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [1] ${HOME}/bin/monerod:tools::log_stack_trace(char const*)+0x9e2 [0x565036352842]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [2] ${HOME}/bin/monerod:__cxa_throw+0x14b [0x5650363543eb]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [3] ${HOME}/bin/monerod+0x62cc95 [0x5650360c5c95]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [4] ${HOME}/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::safe_shared_from_this()+0xd9 [0x565036110ff9]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [5] ${HOME}/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0x95 [0x565036139585]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [6] ${HOME}/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x358 [0x5650360ef758]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [7] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x622 [0x5650361773e2]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [8] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0xa1c [0x56503619939c]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [9] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connect_to_seed()+0x30b [0x56503619d8fb]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [10] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x523 [0x56503619ea83]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [11] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x15e [0x5650360d5aae]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [12] ${HOME}/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x67 [0x56503610b8e7]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [13] ${HOME}/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x265 [0x5650360d6865]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [14] ${HOME}/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x10ee [0x56503610685e]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [15] /usr/lib64/libboost_thread.so.1.59.0+0x115a5 [0x7fc0ddb675a5]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [16] /lib64/libpthread.so.0+0x7684 [0x7fc0dd0a4684]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163  [17] /lib64/libc.so.6:clone+0x6d [0x7fc0dcddaeed]
	 [P2P8] INFO stacktrace src/common/stack_trace.cpp:163
	


# Discussion History
## moneromooo-monero | 2018-09-12T11:09:52+00:00
Do you have 979105b ?

## trasherdk | 2018-09-12T11:20:48+00:00
Yes, I have applied (979105b) patch. 
The second wallet, when issuing stop_mining, did not do anything to the second node, other than stopping mining. Repeated start/stop mining with no extra logging ??? Something else is triggering this.

## trasherdk | 2018-09-12T12:08:12+00:00
My setup:
xmr-stak (win 10) -> monero-stratum -> node-1 -> node-2 (node-2 <-> node-3)
wallet-1 -> node-2
wallet-2 -> node-3
Does that make any sense?

Stopping/Starting "node-2", caused "node-3" to freak out. Same log output as above.
Seems like node-3 didn't like to be alone, without any peers.


## moneromooo-monero | 2018-09-12T12:13:23+00:00
Looking at the code, it seems to behave as expected.


## trasherdk | 2018-09-12T12:16:16+00:00
What is the right method to shut down a detached monerod?
So far I've been using SIGHUP.

## moneromooo-monero | 2018-09-12T12:44:31+00:00
monerod exit

## moneromooo-monero | 2018-10-05T10:14:14+00:00
I've looked and this is all fine.

## anronin | 2018-10-11T05:23:03+00:00
Hi, I have the same issue, monerod 0.13.0.2, I think on 0.12.3 it was much more such exceptions but still it has this [bitmonero.log](https://github.com/monero-project/monero/files/2467448/bitmonero.log)

<details>
<summary>Exception: boost::exception_detail</summary>

2018-10-10 10:10:07.245     7ffa9ca61780        INFO    logging contrib/epee/src/mlog.cpp:242   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-10 10:10:07.245     7ffa9ca61780        INFO    global  src/daemon/main.cpp:287 Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-10 10:10:07.246     7ffa9ca61780        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2018-10-10 10:10:07.271     7ffa9ca61780        WARN    daemon  src/daemon/executor.cpp:61      Monero 'Beryllium Bullet' (v0.13.0.2-release) Daemonised
2018-10-10 10:10:07.271     7ffa9ca61780        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-10-10 10:10:07.271     7ffa9ca61780        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-10-10 10:10:07.272     7ffa9ca61780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-10-10 10:10:07.817     7ffa9ca61780        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-10-10 10:10:07.818     7ffa9ca61780        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-10-10 10:10:07.840     7ffa9ca61780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:18087
2018-10-10 10:10:07.840     7ffa9ca61780        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18087
2018-10-10 10:10:07.840     7ffa9ca61780        INFO    global  src/daemon/core.h:86    Initializing core...
2018-10-10 10:10:07.841     7ffa9ca61780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:447     Loading blockchain from folder /home/projects/monero/lmdb ...
2018-10-10 10:10:07.841     7ffa9ca61780        WARN    global  src/blockchain_db/lmdb/db_lmdb.cpp:1211 The blockchain is on a rotating drive: this will be very slow, use a SSD if possible
2018-10-10 10:10:07.904     7ffa9ca61780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:585     Loading checkpoints
2018-10-10 10:10:08.046     7ffa9ca61780        INFO    global  src/daemon/core.h:92    Core initialized OK
2018-10-10 10:10:08.046     7ffa9ca61780        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2018-10-10 10:10:08.046 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2018-10-10 10:10:08.046 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2018-10-10 10:10:09.047 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1484
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************

2018-10-10 10:10:09.346 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [93.158.203.80:18080 OUT] Sync data returned a new top block candidate: 1679745 -> 1679748 [Your node is 3 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-10-10 10:10:12.409 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1182    [93.158.203.80:18080 OUT]  Synced 1679748/1679748
2018-10-10 10:10:12.410 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1576    SYNCHRONIZED OK
2018-10-10 10:10:12.410 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1598
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-10-10 10:15:34.525 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
2018-10-10 10:15:34.525 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /home/projects/monero/src/monero/build/release/bin/monerod:__cxa_throw+0x10e [0x55a2f559e88e]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /home/projects/monero/src/monero/build/release/bin/monerod:void boost::throw_exception<boost::bad_weak_ptr>(boost::bad_weak_ptr const&)+0x12d [0x55a2f528a42d]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /home/projects/monero/src/monero/build/release/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::safe_shared_from_this()+0x8a [0x55a2f545abea]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /home/projects/monero/src/monero/build/release/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0x35 [0x55a2f546d805]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /home/projects/monero/src/monero/build/release/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3a6 [0x55a2f544a676]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /home/projects/monero/src/monero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x48c [0x55a2f549545c]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /home/projects/monero/src/monero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x727 [0x55a2f54a4dc7]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /home/projects/monero/src/monero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool)+0xa49 [0x55a2f54a6c79]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /home/projects/monero/src/monero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x1a9 [0x55a2f54a7499]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /home/projects/monero/src/monero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x346 [0x55a2f54a8256]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /home/projects/monero/src/monero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x80 [0x55a2f543dfa0]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /home/projects/monero/src/monero/build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x27 [0x55a2f5457767]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /home/projects/monero/src/monero/build/release/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x109 [0x55a2f543e6d9]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /home/projects/monero/src/monero/build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x844 [0x55a2f5455584]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7ffa9a6775d5]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [16] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7ffa99eb86ba]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172      [17] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7ffa99bee41d]
2018-10-10 10:15:34.567 [P2P1]  INFO    stacktrace      src/common/stack_trace.cpp:172
2018-10-11 03:24:55.939 [P2P8]  INFO    global  src/cryptonote_core/blockchain.cpp:1594 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1680265
id:     <879784dc0aa750e05d82d70c4801b72a31249ba9c456931e2ddb45fd143a317c>
PoW:    <6c1d347ae5abeb6240965f33821d358bfd2f952e4d2bb1e43c66130300000000>
difficulty:     63052669066
2018-10-11 03:51:04.270 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
2018-10-11 03:51:04.270 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2018-10-11 03:51:04.336 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /home/projects/monero/src/monero/build/release/bin/monerod:__cxa_throw+0x10e [0x55a2f559e88e]
2018-10-11 03:51:04.336 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /home/projects/monero/src/monero/build/release/bin/monerod:void boost::throw_exception<boost::bad_weak_ptr>(boost::bad_weak_ptr const&)+0x12d [0x55a2f528a42d]
2018-10-11 03:51:04.336 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /home/projects/monero/src/monero/build/release/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::safe_shared_from_this()+0x8a [0x55a2f545abea]
2018-10-11 03:51:04.336 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /home/projects/monero/src/monero/build/release/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0x35 [0x55a2f546d805]
2018-10-11 03:51:04.336 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /home/projects/monero/src/monero/build/release/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3a6 [0x55a2f544a676]
2018-10-11 03:51:04.336 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /home/projects/monero/src/monero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x48c [0x55a2f549545c]
2018-10-11 03:51:04.336 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /home/projects/monero/src/monero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::check_connection_and_handshake_with_peer(epee::net_utils::network_address const&, unsigned long)+0x663 [0x55a2f54a8913]
2018-10-11 03:51:04.336 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /home/projects/monero/src/monero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::gray_peerlist_housekeeping()+0x148 [0x55a2f54a9258]
2018-10-11 03:51:04.337 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /home/projects/monero/src/monero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0xb8 [0x55a2f543dfd8]
2018-10-11 03:51:04.337 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /home/projects/monero/src/monero/build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x27 [0x55a2f5457767]
2018-10-11 03:51:04.337 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /home/projects/monero/src/monero/build/release/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x109 [0x55a2f543e6d9]
2018-10-11 03:51:04.337 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /home/projects/monero/src/monero/build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x844 [0x55a2f5455584]
2018-10-11 03:51:04.337 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7ffa9a6775d5]
2018-10-11 03:51:04.337 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7ffa99eb86ba]
2018-10-11 03:51:04.337 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7ffa99bee41d]
2018-10-11 03:51:04.337 [P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:172
</details>

but i don't see any problems with this, seems all work normal

## moneromooo-monero | 2018-10-11T08:31:50+00:00
Those are fine.

## moneromooo-monero | 2020-05-02T18:08:42+00:00
Fixed in #6269

# Action History
- Created by: trasherdk | 2018-09-12T10:44:41+00:00
- Closed at: 2020-05-02T18:08:42+00:00
