---
title: 'v0.13.0.4: stacktrace on official build/CentOS7'
source_url: https://github.com/monero-project/monero/issues/4913
author: KrzysztofHajdamowicz
assignees: []
labels:
- duplicate
created_at: '2018-11-29T11:21:18+00:00'
updated_at: '2019-01-19T00:41:06+00:00'
type: issue
status: closed
closed_at: '2019-01-19T00:41:06+00:00'
---

# Original Description
Monerod starts, syncs itself to a network and dumps stacks every new block.

```
2018-11-28 11:07:47.521 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1594 ESC[1;34m----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1714864
id:     <c7fdccd17192a5f5ff22a86c3769d521c9b288d83a49d777e8e5cb5011ffc655>
PoW:    <23b2ee9bf2a551e55b92691c6d84065e129f8ecf7a57ad3d2539941200000000>
difficulty:     50230259074ESC[0m
2018-11-28 13:30:29.789 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:310     [78.192.13.98:38828 INC] Sync data returned a new top block candidate: 1714934 -> 1548046 [Your node is 166888 blocks (231 day
s) ahead] 
SYNCHRONIZATION started
2018-11-28 16:24:13.041 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
2018-11-28 16:24:13.041 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /data/ssd1/monerod/monerod:__wrap___cxa_throw+0x10a [0x561701cd54ea]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /data/ssd1/monerod/monerod:void boost::throw_exception<boost::bad_weak_ptr>(boost::bad_weak_ptr const&)+0x12d [0x5617019c127d]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /data/ssd1/monerod/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryp
tonote_connection_context> > >::safe_shared_from_this()+0x8a [0x561701b90daa]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /data/ssd1/monerod/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryp
tonote_connection_context> > >::close()+0x35 [0x561701ba37e5]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /data/ssd1/monerod/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_con
text> >::close(boost::uuids::uuid)+0x3a2 [0x561701b80c32]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /data/ssd1/monerod/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigne
d long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x48c [0x561701bcb60c]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /data/ssd1/monerod/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::check_connection_and_handshake
_with_peer(epee::net_utils::network_address const&, unsigned long)+0x623 [0x561701bde923]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /data/ssd1/monerod/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::gray_peerlist_housekeeping()+0
x148 [0x561701bdf268]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /data/ssd1/monerod/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0xb8 [0x561701b7
4698]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /data/ssd1/monerod/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<crypton
ote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idl
e_callback_conext_base>)+0x27 [0x561701b8d937]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /data/ssd1/monerod/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_ser
ver<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_
context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<crypton
ote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle
_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x109 [0x561701b74d99]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /data/ssd1/monerod/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x844 [0x561701b8b754]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /data/ssd1/monerod/monerod+0x9ff64d [0x5617020b564d]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /lib64/libpthread.so.0+0x7e25 [0x7ff90e731e25]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /lib64/libc.so.6:clone+0x6d [0x7ff90e45bbad]
2018-11-28 16:24:13.068 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:172  
```

Official release build, CentOS7 with packages:
```
# rpm -qa | grep libc
glibc-common-2.17-222.el7.x86_64
glibc-devel-2.17-222.el7.x86_64
glibc-headers-2.17-222.el7.x86_64
glibc-2.17-222.el7.x86_64

```


# Discussion History
## moneromooo-monero | 2018-11-29T14:17:35+00:00
These can be ignored, it's just failing to connect to new peers. It's only a problem if it does this on *all* new peers.

## moneromooo-monero | 2019-01-19T00:25:36+00:00
Duplicate of #4365

+duplicate


# Action History
- Created by: KrzysztofHajdamowicz | 2018-11-29T11:21:18+00:00
- Closed at: 2019-01-19T00:41:06+00:00
