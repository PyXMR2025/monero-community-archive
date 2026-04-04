---
title: Testnet issue, random stacktrace in log
source_url: https://github.com/monero-project/monero/issues/3285
author: Sheastesx
assignees: []
labels: []
created_at: '2018-02-18T06:06:02+00:00'
updated_at: '2018-10-09T11:49:02+00:00'
type: issue
status: closed
closed_at: '2018-10-09T11:49:02+00:00'
---

# Original Description
I am with master 4f80c50730447fa0dabb795c63b45ed27851725d and this just showed up in my testnet log file:

```
2018-02-18 01:54:56.895	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
2018-02-18 01:54:56.895	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /testmonero/build/release/bin/monerod:__cxa_throw+0x10e [0x555a83fd4dce]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /testmonero/build/release/bin/monerod+0x352a5e [0x555a83e83a5e]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /testmonero/build/release/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::safe_shared_from_this()+0x7c [0x555a83ea747c]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /testmonero/build/release/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::add_ref()+0x35 [0x555a83ea87a5]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /testmonero/build/release/bin/monerod:epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::start_outer_call()+0x110 [0x555a83ea6750]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /testmonero/build/release/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::find_and_lock_connection(boost::uuids::uuid, epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >*&)+0x3c4 [0x555a83ea6ce4]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] /testmonero/build/release/bin/monerod:bool epee::net_utils::async_invoke_remote_command2<nodetool::COMMAND_REQUEST_SUPPORT_FLAGS::response, nodetool::COMMAND_REQUEST_SUPPORT_FLAGS::request, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_get_support_flags(nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> const&, std::function<void (nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, unsigned int const&)>)::{lambda(int, nodetool::COMMAND_REQUEST_SUPPORT_FLAGS::response const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1}, epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >(boost::uuids::uuid, int, nodetool::COMMAND_REQUEST_SUPPORT_FLAGS::request const&, epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >&, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_get_support_flags(nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> const&, std::function<void (nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, unsigned int const&)>)::{lambda(int, nodetool::COMMAND_REQUEST_SUPPORT_FLAGS::response const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1} const&, unsigned long)+0xda [0x555a83ed09ba]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] /testmonero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_get_support_flags(nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> const&, std::function<void (nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, unsigned int const&)>)+0x5a [0x555a83ed0cba]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] /testmonero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x548 [0x555a83edfe28]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] /testmonero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x70f [0x555a83eef09f]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] /testmonero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool)+0xc17 [0x555a83ef11b7]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [12] /testmonero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x228 [0x555a83ef1898]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [13] /testmonero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x211 [0x555a83ef21c1]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [14] /testmonero/build/release/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x80 [0x555a83e8b700]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [15] /testmonero/build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x27 [0x555a83ea57a7]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [16] /testmonero/build/release/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0xf5 [0x555a83e8c6d5]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [17] /testmonero/build/release/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x864 [0x555a83ea33c4]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [18] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.62.0+0x12116 [0x7f02eb0bc116]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [19] /lib/x86_64-linux-gnu/libpthread.so.0+0x7494 [0x7f02ea5f7494]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [20] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7f02ea339aff]
2018-02-18 01:54:56.898	[P2P2]	INFO 	stacktrace	src/common/stack_trace.cpp:163
```

# Discussion History
## moneroexamples | 2018-02-20T23:59:44+00:00
if you write `status` in daemon, what testnet hf version it shows? v8 or v7? Just curious. 

## Sheastesx | 2018-02-22T00:09:49+00:00
@moneroexamples v8

## moneroexamples | 2018-02-22T01:11:35+00:00
What does status says? 

I also have issues with tesnet v8. Maybe its connected:

https://github.com/monero-project/monero/issues/3267

## moneromooo-monero | 2018-07-19T21:50:53+00:00
I believe this is fixed by #4130.


## moneromooo-monero | 2018-10-09T11:45:32+00:00
There are other instances of that exception, but those are all fine AFAICT.
The one in this bug is now fixed.

+resolved

# Action History
- Created by: Sheastesx | 2018-02-18T06:06:02+00:00
- Closed at: 2018-10-09T11:49:02+00:00
