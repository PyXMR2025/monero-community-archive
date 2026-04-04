---
title: connection error when trying to sync block
source_url: https://github.com/monero-project/monero/issues/4836
author: Seriy-A
assignees: []
labels:
- invalid
created_at: '2018-11-11T14:16:52+00:00'
updated_at: '2018-11-12T00:01:00+00:00'
type: issue
status: closed
closed_at: '2018-11-12T00:01:00+00:00'
---

# Original Description
i got new block from p2p node, and failed to sync it
then, got this block from another node, and all ok :\
```
2018-11-11 11:56:13.549 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [64.46.4.218:37555 INC] Sync data returned a new top block candidate: 1702687 -> 1702688 [Your node is 1 blocks (0 days) behind]

SYNCHRONIZATION started
2018-11-11 11:57:33.864 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
2018-11-11 11:57:33.866 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2018-11-11 11:57:33.897 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] monerod:__wrap___cxa_throw+0x10a [0x55765aaea4ea]
2018-11-11 11:57:33.898 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] monerod:void boost::throw_exception<boost::bad_weak_ptr>(boost::bad_weak_ptr const&)+0x12d [0x55765a7d627d]
2018-11-11 11:57:33.899 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::safe_shared_from_this()+0x8a [0x55765a9a5daa]
2018-11-11 11:57:33.899 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0x35 [0x55765a9b87e5]
2018-11-11 11:57:33.900 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3a2 [0x55765a995c32]
2018-11-11 11:57:33.901 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x48c [0x55765a9e060c]
2018-11-11 11:57:33.902 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::check_connection_and_handshake_with_peer(epee::net_utils::network_address const&, unsigned long)+0x623 [0x55765a9f3923]
2018-11-11 11:57:33.903 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::gray_peerlist_housekeeping()+0x148 [0x55765a9f4268]

2018-11-11 11:57:33.904 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0xb8 [0x55765a989698]
2018-11-11 11:57:33.905 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x27 [0x55765a9a2937]
2018-11-11 11:57:33.906 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x109 [0x55765a989d99]
2018-11-11 11:57:33.907 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x844 [0x55765a9a0754]
2018-11-11 11:57:33.907 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] monerod+0x9ff64d [0x55765aeca64d]
2018-11-11 11:57:33.908 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /lib/x86_64-linux-gnu/libpthread.so.0+0x8164 [0x7f5096a52164]
2018-11-11 11:57:33.910 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7f509697adef]
2018-11-11 11:57:33.910 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:172
2018-11-11 11:57:54.997 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [65.130.225.167:58982 INC] Sync data returned a new top block candidate: 1702687 -> 1702688 [Your node is 1 blocks (0 days) behind]
SYNCHRONIZATION started
```

# Discussion History
## moneromooo-monero | 2018-11-11T14:21:30+00:00
There doesn't seem to be a problem here, unless it can't catch up.
Did it catch up ?

## Seriy-A | 2018-11-11T15:39:23+00:00
seems my english excess bad to read your post correctly :(
or what you mean, any advices for catching?

## moneromooo-monero | 2018-11-11T16:33:59+00:00
The log you posted is OK.
Is your node currently stuck ?
If it is not stuck, then nothing is wrong.

## Seriy-A | 2018-11-11T17:47:49+00:00
node OK, got block from 64.46.4.218:37555, got error
got same block (1702688) from 65.130.225.167:58982, all ok

_maybe it happens because epee::net_utils::connection got bad packet?_

## Seriy-A | 2018-11-11T22:17:42+00:00
catched again w/ same adressess, but not after sync attempt

```
2018-11-11 20:28:48.203 [P2P7]  WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-11-11 20:30:02.440 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
2018-11-11 20:30:02.442 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2018-11-11 20:30:02.556 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] monerod:__wrap___cxa_throw+0x10a [0x55765aaea4ea]
2018-11-11 20:30:02.557 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] monerod:void boost::throw_exception<boost::bad_weak_ptr>(boost::bad_weak_ptr const&)+0x12d [0x55765a7d627d]
2018-11-11 20:30:02.558 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::safe_shared_from_this()+0x8a [0x55765a9a5daa]
2018-11-11 20:30:02.560 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0x35 [0x55765a9b87e5]
2018-11-11 20:30:02.561 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3a2 [0x55765a995c32]
2018-11-11 20:30:02.562 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x48c [0x55765a9e060c]
2018-11-11 20:30:02.562 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::check_connection_and_handshake_with_peer(epee::net_utils::network_address const&, unsigned long)+0x623 [0x55765a9f3923]
2018-11-11 20:30:02.563 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::gray_peerlist_housekeeping()+0x148 [0x55765a9f4268]

2018-11-11 20:30:02.565 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0xb8 [0x55765a989698]
2018-11-11 20:30:02.566 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x27 [0x55765a9a2937]
2018-11-11 20:30:02.566 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x109 [0x55765a989d99]
2018-11-11 20:30:02.568 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x844 [0x55765a9a0754]
2018-11-11 20:30:02.569 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] monerod+0x9ff64d [0x55765aeca64d]
2018-11-11 20:30:02.570 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /lib/x86_64-linux-gnu/libpthread.so.0+0x8164 [0x7f5096a52164]
2018-11-11 20:30:02.572 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7f509697adef]
2018-11-11 20:30:02.573 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172
2018-11-11 21:18:08.897 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [184.146.4.132:51038 INC] Sync data returned a new top block candidate: 1702973 -> 1702976 [Your node is 3 blocks (0 days) behind]
```

## moneromooo-monero | 2018-11-11T23:56:05+00:00
OK, then all is good. You can ignore those messages.

+invalid


# Action History
- Created by: Seriy-A | 2018-11-11T14:16:52+00:00
- Closed at: 2018-11-12T00:01:00+00:00
