---
title: Exception on OUTPUT_DNE
source_url: https://github.com/monero-project/monero/issues/1705
author: ghost
assignees: []
labels: []
created_at: '2017-02-09T23:35:36+00:00'
updated_at: '2017-08-08T11:42:16+00:00'
type: issue
status: closed
closed_at: '2017-08-08T11:42:16+00:00'
---

# Original Description
Is this expected behaviour and the logging is just unnecessarily verbose, or is this actually a problem?
Latest master (`99ee3fd`), Ubuntu 16.04, ARMv8, GCC 5.4.1

```
2017-02-09 23:33:34.140	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[203.177.142.37:18080 OUT] Sync data returned a new top block candidate: 1241941 -> 1242655 [Your node is 714 blocks (0 days) behind] 
SYNCHRONIZATION started
2017-02-09 23:33:40.594	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:119	Exception: cryptonote::OUTPUT_DNE
2017-02-09 23:33:40.594	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:120	Unwound call stack:
2017-02-09 23:33:40.599	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [1] monerod() [0x6257e4]
2017-02-09 23:33:40.600	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [2] monerod:cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&)+0x530 [0x5932f8]
2017-02-09 23:33:40.600	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [3] monerod:cryptonote::Blockchain::output_scan_worker(unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&) const+0x30 [0x55d298]
2017-02-09 23:33:40.600	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [4] monerod:cryptonote::Blockchain::prepare_handle_incoming_blocks(std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> > const&)+0xf30 [0x56db48]
2017-02-09 23:33:40.600	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [5] monerod:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&)+0xe1c [0x4f328c]
2017-02-09 23:33:40.600	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [6] monerod() [0x665df8]
2017-02-09 23:33:40.600	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [7] monerod() [0x676150]
2017-02-09 23:33:40.600	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [8] monerod() [0x4e7c28]
2017-02-09 23:33:40.600	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [9] monerod() [0x513168]
2017-02-09 23:33:40.601	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [10] monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1ec [0x5347ac]
2017-02-09 23:33:40.601	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [11] monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x188 [0x50cc00]
2017-02-09 23:33:40.601	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [12] monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x58c [0x50d37c]
2017-02-09 23:33:40.601	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [13] monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x19c [0x4ca3dc]
2017-02-09 23:33:40.601	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [14] monerod() [0x622248]
2017-02-09 23:33:40.601	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [15] monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x158 [0x5361e0]
2017-02-09 23:33:40.601	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [16] /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0+0x11cf8 [0x7f7e8c0cf8]
2017-02-09 23:33:40.602	[P2P3]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [17] /lib/aarch64-linux-gnu/libpthread.so.0+0x6fc4 [0x7f7ed56fc4]
```

# Discussion History
## anonimal | 2017-02-09T23:38:33+00:00
Duplicate of https://github.com/monero-project/monero/issues/1355?

## moneromooo-monero | 2017-02-09T23:47:27+00:00
We'd need to change the function to not throw when it's known the outputs may not be found for expected reasons. Then we'll know that when an exception happens, it is really unexpected :)

## ghost | 2017-02-10T08:27:18+00:00
@anonimal Yes I believe you're correct. @moneromooo-monero Should I close, or is the new easylogging++ info useful?

## moneromooo-monero | 2017-03-25T16:52:21+00:00
I think I fixed that.

## moneromooo-monero | 2017-08-08T11:28:42+00:00
+resolved

# Action History
- Created by: ghost | 2017-02-09T23:35:36+00:00
- Closed at: 2017-08-08T11:42:16+00:00
