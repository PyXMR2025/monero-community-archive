---
title: 'monerod crashes after "Exception: std::bad_alloc"'
source_url: https://github.com/monero-project/monero/issues/4135
author: arnuschky
assignees: []
labels: []
created_at: '2018-07-14T20:10:20+00:00'
updated_at: '2018-07-16T21:10:02+00:00'
type: issue
status: closed
closed_at: '2018-07-16T21:09:45+00:00'
---

# Original Description
monerod crashes after a while, log shows several `std::bad_alloc` exceptions (stack trace below).

Running 0.12.3.0 (a486cae) on Ubuntu 14.04 x64.

Any ideas where this comes from?

```
2018-07-14 20:04:12.533	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: std::bad_alloc
2018-07-14 20:04:12.533	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-07-14 20:04:12.535	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /usr/local/bin/monerod:__cxa_throw+0x90 [0x7f40594196e0]
2018-07-14 20:04:12.535	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /usr/lib/x86_64-linux-gnu/libstdc++.so.6:operator new(unsigned long)+0x7d [0x7f405671de0d]
2018-07-14 20:04:12.535	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /usr/lib/x86_64-linux-gnu/libstdc++.so.6:std::string::_Rep::_S_create(unsigned long, unsigned long, std::allocator<char> const&)+0x59 [0x7f4056779249]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /usr/lib/x86_64-linux-gnu/libstdc++.so.6:std::string::_Rep::_M_clone(std::allocator<char> const&, unsigned long)+0x1b [0x7f4056779e0b]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /usr/lib/x86_64-linux-gnu/libstdc++.so.6:std::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(std::string const&)+0x3c [0x7f405677a48c]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /usr/local/bin/monerod:std::_Rb_tree_iterator<std::pair<std::string const, unsigned int> > std::_Rb_tree<std::string, std::pair<std::string const, unsigned int>, std::_Select1st<std::pair<std::string const, unsigned int> >, std::less<std::string>, std::allocator<std::pair<std::string const, unsigned int> > >::_M_emplace_hint_unique<std::piecewise_construct_t const&, std::tuple<std::string const&>, std::tuple<> >(std::_Rb_tree_const_iterator<std::pair<std::string const, unsigned int> >, std::piecewise_construct_t const&, std::tuple<std::string const&>&&, std::tuple<>&&)+0x5c [0x7f405917240c]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::host_count(std::string const&, int)+0x3df [0x7f405930ec5f]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::shutdown()+0x167 [0x7f405930f327]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0xeb [0x7f405930f46b]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] /usr/local/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3d5 [0x7f40592ec6b5]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x237 [0x7f4059331c07]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [12] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x6fc [0x7f405934341c]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [13] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connect_to_seed()+0x10d [0x7f4059345b1d]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [14] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x318 [0x7f40593462c8]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [15] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x79 [0x7f40592e1ec9]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [16] /usr/local/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x23 [0x7f40592fb263]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [17] /usr/local/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x106 [0x7f40592e26c6]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [18] /usr/local/bin/monerod:boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&)+0x2fd [0x7f4059145b8d]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [19] /usr/local/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x289 [0x7f40592f9849]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [20] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0xf77f [0x7f40569d277f]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x8184 [0x7f4056293184]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f4055fc003d]
2018-07-14 20:04:12.536	[P2P9]	INFO 	stacktrace	src/common/stack_trace.cpp:163	
```

# Discussion History
## arnuschky | 2018-07-14T20:11:27+00:00
I also found this exception:

```
2018-07-14 20:06:49.068	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: std::runtime_error
2018-07-14 20:06:49.068	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /usr/local/bin/monerod:__cxa_throw+0x90 [0x7ff39df836e0]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::host_count(std::string const&, int)+0x770 [0x7ff39de78ff0]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::shutdown()+0x167 [0x7ff39de79327]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0xeb [0x7ff39de7946b]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /usr/local/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3d5 [0x7ff39de566b5]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x237 [0x7ff39de9bc07]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x6fc [0x7ff39dead41c]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool)+0x9be [0x7ff39deaf13e]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x14a [0x7ff39deaf93a]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x216 [0x7ff39deb01c6]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x79 [0x7ff39de4bec9]
2018-07-14 20:06:49.070	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [12] /usr/local/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x23 [0x7ff39de65263]
2018-07-14 20:06:49.071	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [13] /usr/local/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x106 [0x7ff39de4c6c6]
2018-07-14 20:06:49.071	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [14] /usr/local/bin/monerod:boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&)+0x2fd [0x7ff39dcafb8d]
2018-07-14 20:06:49.071	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [15] /usr/local/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x289 [0x7ff39de63849]
2018-07-14 20:06:49.071	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [16] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0xf77f [0x7ff39b53c77f]
2018-07-14 20:06:49.071	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [17] /lib/x86_64-linux-gnu/libpthread.so.0+0x8184 [0x7ff39adfd184]
2018-07-14 20:06:49.071	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [18] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7ff39ab2a03d]
2018-07-14 20:06:49.071	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	
```

## arnuschky | 2018-07-15T06:05:47+00:00
I ran this with log level 2, here's the last section of the log (after this, the daemon crashed):

I forgot to say: this is on stagenet.

```
2018-07-15 00:35:07.124	[P2P1]	INFO 	net	contrib/epee/include/net/levin_protocol_handler_async.h:174	[xxx.xxx.xxx.xxx:38080 OUT] Timeout on invoke operation happened, command: 1001 timeout: 5000
2018-07-15 00:35:07.124	[P2P1]	INFO 	net	contrib/epee/include/storages/levin_abstract_invoke2.h:122	Failed to invoke command 1001 return code -4
2018-07-15 00:35:07.125	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:708	[162.210.173.150:38080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2018-07-15 00:35:07.125	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:757	[162.210.173.150:38080 OUT] COMMAND_HANDSHAKE Failed
2018-07-15 00:35:07.125	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: std::bad_alloc
2018-07-15 00:35:07.125	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /usr/local/bin/monerod:__cxa_throw+0x90 [0x7f6e388206e0]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /usr/lib/x86_64-linux-gnu/libstdc++.so.6:operator new(unsigned long)+0x7d [0x7f6e35b24e0d]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /usr/lib/x86_64-linux-gnu/libstdc++.so.6:std::string::_Rep::_S_create(unsigned long, unsigned long, std::allocator<char> const&)+0x59 [0x7f6e35b80249]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /usr/lib/x86_64-linux-gnu/libstdc++.so.6:std::string::_Rep::_M_clone(std::allocator<char> const&, unsigned long)+0x1b [0x7f6e35b80e0b]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /usr/lib/x86_64-linux-gnu/libstdc++.so.6:std::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(std::string const&)+0x3c [0x7f6e35b8148c]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /usr/local/bin/monerod:std::_Rb_tree_iterator<std::pair<std::string const, unsigned int> > std::_Rb_tree<std::string, std::pair<std::string const, unsigned int>, std::_Select1st<std::pair<std::string const, unsigned int> >, std::less<std::string>, std::allocator<std::pair<std::string const, unsigned int> > >::_M_emplace_hint_unique<std::piecewise_construct_t const&, std::tuple<std::string const&>, std::tuple<> >(std::_Rb_tree_const_iterator<std::pair<std::string const, unsigned int> >, std::piecewise_construct_t const&, std::tuple<std::string const&>&&, std::tuple<>&&)+0x5c [0x7f6e3857940c]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::host_count(std::string const&, int)+0x3df [0x7f6e38715c5f]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::shutdown()+0x167 [0x7f6e38716327]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0xeb [0x7f6e3871646b]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] /usr/local/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3d5 [0x7f6e386f36b5]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x237 [0x7f6e38738c07]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [12] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x6fc [0x7f6e3874a41c]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [13] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connect_to_seed()+0x10d [0x7f6e3874cb1d]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [14] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x318 [0x7f6e3874d2c8]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [15] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x79 [0x7f6e386e8ec9]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [16] /usr/local/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x23 [0x7f6e38702263]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [17] /usr/local/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x106 [0x7f6e386e96c6]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [18] /usr/local/bin/monerod:boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&)+0x2fd [0x7f6e3854cb8d]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [19] /usr/local/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x289 [0x7f6e38700849]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [20] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0xf77f [0x7f6e35dd977f]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x8184 [0x7f6e3569a184]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f6e353c703d]
2018-07-15 00:35:07.128	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:163	
2018-07-15 00:35:07.128	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1776	[162.210.173.150:38080 3ea667cb-f7de-4b86-da3a-5b704f3da033 OUT] CLOSE CONNECTION
2018-07-15 00:35:07.128	[P2P1]	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:171	Destructing connection p2p#2900 to xxx.xxx.xxx.xxx
```

## arnuschky | 2018-07-15T08:01:27+00:00
More info:

 - After downgrading to 0.12.2.0 the problem seems to be gone.
 - Problem was also present on mainnet
 - Several exceptions usually occur until daemon finally crashes
 - Therefore crashes take sometimes 20-30mins to happen
 - I failed to reproduce this on Ubuntu 16.04


## moneromooo-monero | 2018-07-15T10:08:33+00:00
The second one is fixed by 4130.
I'm surprised the first and third one crash. What compiler ?

## arnuschky | 2018-07-15T11:14:51+00:00
First and third are the same, no? As I said, these don't crash the daemon immediately but seem to occur for a while and at some point the daemon crashes. So I am not even 100% certain that those exceptions are the cause.

`gcc (Ubuntu 4.8.5-4ubuntu8~14.04.2) 4.8.5`



## moneromooo-monero | 2018-07-15T11:52:22+00:00
Then get a stack trace of the crash, if it still happens with the patch above.


## arnuschky | 2018-07-15T12:03:01+00:00
Sorry I was unclear. The exception with log level 2 (last one) is the log just before the crash. So it's the stack trace of the crash. What I meant is that the exact same trace appears multiple times in the log without crashing the daemon. Haven't tested with 4130 yet, though.

## moneromooo-monero | 2018-07-15T13:55:39+00:00
Doubt it. Make sure with gdb.

## moneromooo-monero | 2018-07-15T18:02:38+00:00
4130 is in fact not enough, I'll have another patch soon.

## arnuschky | 2018-07-16T06:42:01+00:00
Ok, great. I'll wait for it so that I can test everything in one go.

## arnuschky | 2018-07-16T06:46:54+00:00
BTW, I found these in my kernel log:

```
[15949850.460861] monerod[4069]: segfault at 18 ip 00007f188e0e7f8b sp 00007f176f0fa830 error 4 in libc-2.19.so[7f188e067000+1be000]
[15952516.590350] monerod[4661]: segfault at 18 ip 00007f132e88781b sp 00007f1218df6c50 error 4 in libc-2.19.so[7f132e809000+1be000]
[15959189.598311] monerod[6818]: segfault at 7fe300000018 ip 00007fe508e6881b sp 00007fe3ea8f9c50 error 4 in libc-2.19.so[7fe508dea000+1be000]
[15961372.231970] monerod[26441]: segfault at 7f0a00000018 ip 00007f0bffa5075e sp 00007f0adbffdc50 error 4 in libc-2.19.so[7f0bff9d2000+1be000]
[15965649.412872] monerod[26805]: segfault at 7f2600000018 ip 00007f28177b975e sp 00007f27009f4c50 error 4 in libc-2.19.so[7f281773b000+1be000]
[15966098.799892] monerod[26839]: segfault at 18 ip 00007f363a88af8b sp 00007f351bafc7a0 error 4 in libc-2.19.so[7f363a80a000+1be000]
[15969634.424800] monerod[27056]: segfault at 18 ip 00007f20a551581b sp 00007f1f87ffdc50 error 4 in libc-2.19.so[7f20a5497000+1be000]
[15970276.187282] monerod[27165]: segfault at 7fa200000018 ip 00007fa4230cf75e sp 00007fa30f9d4c50 error 4 in libc-2.19.so[7fa423051000+1be000]
[15974866.788846] monerod[27465]: segfault at 7fa300000018 ip 00007fa4e7f0275e sp 00007fa3d2afac50 error 4 in libc-2.19.so[7fa4e7e84000+1be000]
[15979193.393161] monerod[27678]: segfault at 18 ip 00007f249419175e sp 00007f2347ffd5c0 error 4 in libc-2.19.so[7f2494113000+1be000]
[15980781.401867] monerod[27765]: segfault at 7ff500000018 ip 00007ff712aac81b sp 00007ff5fd7f8c50 error 4 in libc-2.19.so[7ff712a2e000+1be000]
[15982392.146438] monerod[27907]: segfault at 7fc300000018 ip 00007fc50760981b sp 00007fc3e9ff9c50 error 4 in libc-2.19.so[7fc50758b000+1be000]
[15991097.828717] monerod[28495]: segfault at 7fd600000018 ip 00007fd80428081b sp 00007fd6ed1f5c50 error 4 in libc-2.19.so[7fd804202000+1be000]
[15997528.597332] monerod[9676]: segfault at 18 ip 00007f4055f4075e sp 00007f3f361f7c50 error 4 in libc-2.19.so[7f4055ec2000+1be000]
[15997859.078061] monerod[9746]: segfault at 18 ip 00007ff39aaacf8b sp 00007ff272bf9b40 error 4 in libc-2.19.so[7ff39aa2c000+1be000]
```

Note that build system != test system, but software levels are the same.

## moneromooo-monero | 2018-07-16T08:03:24+00:00
4130 is now updated with a better patch.


## arnuschky | 2018-07-16T11:26:05+00:00
Seems that this was the problem, not crashing anymore. I'll keep an eye on it for a few more hours/deploy to more systems before closing the issue.

## arnuschky | 2018-07-16T21:09:45+00:00
Daemon is still up, seems fixed. Thanks for the prompt help!

## arnuschky | 2018-07-16T21:10:02+00:00
Fixed by #4130 

# Action History
- Created by: arnuschky | 2018-07-14T20:10:20+00:00
- Closed at: 2018-07-16T21:09:45+00:00
