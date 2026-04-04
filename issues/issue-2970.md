---
title: Daemon stops syncing after sometime running
source_url: https://github.com/monero-project/monero/issues/2970
author: vdo
assignees: []
labels:
- bug
created_at: '2017-12-20T08:53:16+00:00'
updated_at: '2018-06-10T09:40:55+00:00'
type: issue
status: closed
closed_at: '2018-06-10T09:40:55+00:00'
---

# Original Description
The daemon stops syncing just after this block:

`2017-12-20 00:16:39.304 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154    ESC[1;33m[163.172.255.56:57526 INC]  Synced 1121073/1468507ESC[0m
`
Then after some time, like 2 hours , it reports this stacktrace:
```
2017-12-20 01:51:21.972 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:120  Exception: cryptonote::BLOCK_DNE
2017-12-20 01:51:21.972 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:121  Unwound call stack:
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [1] /opt/monero-v0.11.1.0/monerod:__wrap___cxa_throw+0x102 [0x8914e2]
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [2] /opt/monero-v0.11.1.0/monerod() [0x7c8184]
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [3] /opt/monero-v0.11.1.0/monerod:cryptonote::BlockchainLMDB::get_block_height(crypto::hash const&) const+0x461 [0x7d39d1]
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [4] /opt/monero-v0.11.1.0/monerod:cryptonote::BlockchainLMDB::get_block_blob[abi:cxx11](crypto::hash const&) const+0x12b [0x7c97fb]
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [5] /opt/monero-v0.11.1.0/monerod:bool cryptonote::Blockchain::get_blocks<std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >, std::_
_cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, crypton
ote::block> > >, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > >(std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<cha
r>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >&, std::__cxx11::list<crypto::hash, std::allocator<crypto::ha
sh> >&) const+0x1ac [0x82941c]
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [6] /opt/monero-v0.11.1.0/monerod:cryptonote::Blockchain::handle_get_objects(cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::NOTIFY
_RESPONSE_GET_OBJECTS::request&)+0x1b2 [0x80ec22]
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [7] /opt/monero-v0.11.1.0/monerod:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_request_get_objects(int, cryptonote::NOTIFY
_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&)+0x16c [0x70b3fc]
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [8] /opt/monero-v0.11.1.0/monerod:int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote:
:NOTIFY_REQUEST_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::requ
est&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_han
dler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, crypton
ote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, c
ryptonote::cryptonote_connection_context&)+0x227 [0x7068f7]
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [9] /opt/monero-v0.11.1.0/monerod:int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_conne
ction_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context
&, bool&)+0x2ab [0x70c55b]
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [10] /opt/monero-v0.11.1.0/monerod:int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nod
etool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std:
:allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&)+0xbe [0x70c7ce]
2017-12-20 01:51:21.979 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [11] /opt/monero-v0.11.1.0/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11:
:basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)+0x4f [0x70cbdf]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [12] /opt/monero-v0.11.1.0/monerod:epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_conte
xt> >::handle_recv(void const*, unsigned long)+0x470 [0x70d0b0]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [13] /opt/monero-v0.11.1.0/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote:
:cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1ba [0x724cea]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [14] /opt/monero-v0.11.1.0/monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost
::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boos
t::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::sy
stem::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool:
:p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_han
dler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x71 [0x6cc391]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [15] /opt/monero-v0.11.1.0/monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x179 [0x6cc7c9]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [16] /opt/monero-v0.11.1.0/monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x20a [0x6ccb8a]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [17] /opt/monero-v0.11.1.0/monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x233 [0x6cce43]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [18] /opt/monero-v0.11.1.0/monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x15c [0x649d1c]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [19] /opt/monero-v0.11.1.0/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x807 [0x66a7f7]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [20] /opt/monero-v0.11.1.0/monerod() [0x988fa5]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x7494 [0x7f5cdea24494]
2017-12-20 01:51:21.980 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7f5cde766aff]
```

But then, if I stop the daemon manually and I start it again, it continues the sync just where it stopped. 
I had to do this a couple of times.



# Discussion History
## moneromooo-monero | 2017-12-20T10:25:09+00:00
Next time you restart, add --log-level 1, and post the log where it starts complaining about verification.

## jredwine2857 | 2018-01-01T02:36:24+00:00
Yep, same here on 5 nodes running on ubuntu 16.04 running 0.11.1.0. Happens daily some days then other times it will go several before it stops synching.  Have a cron job to bounce it daily and it helps some.  Still have it every few days even with that.  

I'll run with the log level 1 and see what it shows and post back.

## jredwine2857 | 2018-01-01T02:40:22+00:00
Ok, next question....where does it put the log file when you run it with --detach?


## moneromooo-monero | 2018-01-01T11:57:15+00:00
~/.bitmonero/bitmonero.log

## dEBRUYNE-1 | 2018-01-08T12:32:22+00:00
+bug

## moneromooo-monero | 2018-06-10T09:27:46+00:00
AFAIK, all such bugs are now fixed in 0.12.2.0.

+resolved


# Action History
- Created by: vdo | 2017-12-20T08:53:16+00:00
- Closed at: 2018-06-10T09:40:55+00:00
