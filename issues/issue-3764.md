---
title: 'Exception: cryptonote::BLOCK_DNE'
source_url: https://github.com/monero-project/monero/issues/3764
author: tdiesler
assignees: []
labels:
- invalid
created_at: '2018-05-06T17:32:57+00:00'
updated_at: '2018-05-27T17:27:46+00:00'
type: issue
status: closed
closed_at: '2018-05-06T22:00:46+00:00'
---

# Original Description
Shows during sync with v0.12.0.0-master-release on Fedora x64 

```
monerod --detach

[xmrusr@monero-01 ~]$ cat .bitmonero/bitmonero.conf 
# Configuration for monerod
# Syntax: any command line option may be specified as 'clioptionname=value'.
# See 'monerod --help' for all available options.

rpc-bind-ip=some.ip
confirm-external-bind=true

rpc-login=myname:mypasswd
```
```
2018-05-06 16:35:19.404	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[196.52.2.104:61352 INC] Sync data returned a new top block candidate: 1564504 -> 1566954 [Your node is 2450 blocks (3 days) behind] 
SYNCHRONIZATION started
2018-05-06 16:35:24.043	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[163.172.20.17:18080 OUT]  Synced 1564524/1566953
2018-05-06 16:35:32.668	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: cryptonote::BLOCK_DNE
2018-05-06 16:35:32.668	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-05-06 16:35:32.684	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] monerod:__wrap___cxa_throw+0x10a [0x5592eb65d1ba]
2018-05-06 16:35:32.688	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] monerod+0x51b0c9 [0x5592eb5880c9]
2018-05-06 16:35:32.688	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] monerod:cryptonote::BlockchainLMDB::get_block_height(crypto::hash const&) const+0x437 [0x5592eb596137]
2018-05-06 16:35:32.689	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] monerod:cryptonote::BlockchainLMDB::get_block_blob[abi:cxx11](crypto::hash const&) const+0x144 [0x5592eb588ea4]
2018-05-06 16:35:32.689	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] monerod:bool cryptonote::Blockchain::get_blocks<std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > >(std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >&) const+0x1f1 [0x5592eb5eb511]
2018-05-06 16:35:32.689	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] monerod:cryptonote::Blockchain::handle_get_objects(cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&)+0x1de [0x5592eb5d269e]
2018-05-06 16:35:32.689	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] monerod:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_request_get_objects(int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&)+0x18f [0x5592eb54cdbf]
2018-05-06 16:35:32.689	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] monerod:int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&)+0x24f [0x5592eb3d913f]
2018-05-06 16:35:32.689	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] monerod:int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&)+0x2aa [0x5592eb3e883a]
2018-05-06 16:35:32.689	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] monerod:int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&)+0xc2 [0x5592eb3e8ac2]
2018-05-06 16:35:32.690	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)+0x50 [0x5592eb3e8e90]
2018-05-06 16:35:32.690	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [12] monerod:epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long)+0x4ad [0x5592eb5690ad]
2018-05-06 16:35:32.690	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [13] monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1f8 [0x5592eb580ea8]
2018-05-06 16:35:32.690	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [14] monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x7a [0x5592eb549dfa]
2018-05-06 16:35:32.690	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [15] monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x188 [0x5592eb54a268]
2018-05-06 16:35:32.690	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [16] monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x226 [0x5592eb54a656]
2018-05-06 16:35:32.690	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [17] monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x250 [0x5592eb54a930]
2018-05-06 16:35:32.690	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [18] monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1f4 [0x5592eb3682e4]
2018-05-06 16:35:32.691	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [19] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x854 [0x5592eb52eb54]
2018-05-06 16:35:32.691	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [20] monerod+0x9870c5 [0x5592eb9f40c5]
2018-05-06 16:35:32.691	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [21] /lib64/libpthread.so.0+0x7564 [0x7fa5c52b7564]
2018-05-06 16:35:32.691	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [22] /lib64/libc.so.6:clone+0x3f [0x7fa5c4feb31f]
```

# Discussion History
## moneromooo-monero | 2018-05-06T21:57:52+00:00
It's innocuous. It's actually silenced in current code. You can ignore it.

+invalid


## jtgrassie | 2018-05-24T12:36:02+00:00
@moneromooo-monero 
> It's actually silenced in current code. You can ignore it.

Sorry but I still see these exceptions in current code. Whilst they can be ignored, they pollute the logs considerably.

## jtgrassie | 2018-05-24T12:36:26+00:00
This needs reopening.

## allenwalker3 | 2018-05-27T17:27:46+00:00
+1

# Action History
- Created by: tdiesler | 2018-05-06T17:32:57+00:00
- Closed at: 2018-05-06T22:00:46+00:00
