---
title: daemon is busy or daemon is not connected
source_url: https://github.com/monero-project/monero/issues/1769
author: gituser
assignees: []
labels: []
created_at: '2017-02-21T23:45:06+00:00'
updated_at: '2017-12-23T13:36:03+00:00'
type: issue
status: closed
closed_at: '2017-12-23T13:36:03+00:00'
---

# Original Description
Trying to test new  `Monero 'Wolfram Warptangent' (v0.10.1.0-e960be5)` and it seems I'm either getting via RPC:

```
{
  "error": {
    "code": -3,
    "message": "daemon is busy"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
``` 

or:

```
{
  "error": {
    "code": -4,
    "message": "no connection to daemon"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```

~/.monero_testnet/monerod_dev.log:
```
2017-02-22 02:34:32.864	    7fb5c3a16740	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-02-22 02:34:32.864	    7fb5c3a16740	INFO 	global	contrib/epee/src/mlog.cpp:153	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-02-22 02:34:32.864	    7fb5c3a16740	INFO 	global	src/daemon/main.cpp:280	Monero 'Wolfram Warptangent' (v0.10.1.0-e960be5)
2017-02-22 02:34:32.864	    7fb5c3a16740	WARN 	daemon	src/daemon/executor.cpp:62	Monero 'Wolfram Warptangent' (v0.10.1.0-e960be5) Daemonised
2017-02-22 02:34:32.864	    7fb5c3a16740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-02-22 02:34:32.864	    7fb5c3a16740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-02-22 02:34:32.865	    7fb5c3a16740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-02-22 02:34:32.865	    7fb5c3a16740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-02-22 02:34:32.865	    7fb5c3a16740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-02-22 02:34:32.865	    7fb5c3a16740	WARN 	net.http	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:28081
2017-02-22 02:34:32.865	    7fb5c3a16740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 28081
2017-02-22 02:34:32.865	    7fb5c3a16740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-02-22 02:34:32.865	    7fb5c3a16740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:314	Loading blockchain from folder /home/monero/.bitmonero/testnet/lmdb ...
2017-02-22 02:34:32.890	    7fb5c3a16740	INFO 	global	src/daemon/core.h:78	Core initialized OK
2017-02-22 02:34:32.890	    7fb5c3a16740	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2017-02-22 02:34:32.890	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-02-22 02:34:32.890	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2017-02-22 02:34:33.890	[P2P0]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1055	
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2017-02-22 02:34:33.900	[P2P0]	WARN 	net.dns	src/common/dns_utils.cpp:529	WARNING: no two valid MoneroPulse DNS checkpoint records were received
```


~/.monero_testnet/simplewallet_testnet_dev.log:
```
2017-02-22 02:26:36.739	    7fbd4bb3a740	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-02-22 02:26:36.739	    7fbd4bb3a740	INFO 	global	contrib/epee/src/mlog.cpp:153	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-02-22 02:26:36.739	    7fbd4bb3a740	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1414	Loading wallet...
2017-02-22 02:26:36.759	    7fbd4bb3a740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2337	Loaded wallet keys file, with public address: XXXXXX
2017-02-22 02:30:07.054	    7fbd4bb3a740	ERROR	net.http	contrib/epee/include/net/http_client.h:436	Unexpected recv fail
2017-02-22 02:30:07.055	    7fbd4bb3a740	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1192	!r. THROW EXCEPTION: error::no_connection_to_daemon
2017-02-22 02:30:07.055	    7fbd4bb3a740	WARN 	net.http	src/wallet/wallet_errors.h:697	/home/build/monero/source/src/wallet/wallet2.cpp:1192:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
2017-02-22 02:30:07.055	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:119	Exception: tools::error::no_connection_to_daemon
2017-02-22 02:30:07.055	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:120	Unwound call stack:
2017-02-22 02:30:07.057	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [1] /home/monero/current/monero-wallet-rpc:__wrap___cxa_throw+0x78 [0x814da8]
2017-02-22 02:30:07.057	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [2] /home/monero/current/monero-wallet-rpc:void tools::error::throw_wallet_ex<tools::error::no_connection_to_daemon, char [14]>(std::string&&, char const (&) [14])+0x189 [0x760179]
2017-02-22 02:30:07.057	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [3] /home/monero/current/monero-wallet-rpc:tools::wallet2::pull_blocks(unsigned long, unsigned long&, std::list<crypto::hash, std::allocator<crypto::hash> > const&, std::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> >&, std::vector<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices, std::allocator<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices> >&)+0x2d9 [0x712109]
2017-02-22 02:30:07.057	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [4] /home/monero/current/monero-wallet-rpc:tools::wallet2::refresh(unsigned long, unsigned long&, bool&)+0x191 [0x720911]
2017-02-22 02:30:07.057	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [5] /home/monero/current/monero-wallet-rpc:tools::wallet2::refresh()+0x23 [0x721773]
2017-02-22 02:30:07.057	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [6] /home/monero/current/monero-wallet-rpc:main+0x6b7 [0x664237]
2017-02-22 02:30:07.057	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [7] /lib/x86_64-linux-gnu/libc.so.6:__libc_start_main+0xf5 [0x7fbd4ae78b45]
2017-02-22 02:30:07.057	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [8] /home/monero/current/monero-wallet-rpc() [0x66f0cc]
2017-02-22 02:30:07.057	    7fbd4bb3a740	INFO 	stacktrace	src/common/stack_trace.cpp:158	
2017-02-22 02:30:07.057	    7fbd4bb3a740	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1448	Wallet initialization failed: no connection to daemon
2017-02-22 02:35:05.908	    7f64e2a88740	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-02-22 02:35:05.908	    7f64e2a88740	INFO 	global	contrib/epee/src/mlog.cpp:153	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-02-22 02:35:05.909	    7f64e2a88740	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1414	Loading wallet...
2017-02-22 02:35:05.925	    7f64e2a88740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2337	Loaded wallet keys file, with public address: MYWALLET_ADDRESS
2017-02-22 02:35:06.467	    7f64e2a88740	WARN 	net.http	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 192.168.70.9:28081
2017-02-22 02:35:06.468	    7f64e2a88740	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1457	Starting wallet rpc server
2017-02-22 02:35:20.790	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:35:21.869	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 51777 84198 91029 101462 
2017-02-22 02:35:21.903	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:35:21.903	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 51777 84198 91029 101462 
2017-02-22 02:35:21.937	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:35:22.977	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 56010 77940 88624 98682 
2017-02-22 02:35:22.977	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=0.000190000000, real_output=0, real_output_in_tx_index=0, indexes: 81157 90579 96426 100030 101314 
2017-02-22 02:35:23.013	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:35:23.013	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 56010 77940 88624 98682 
2017-02-22 02:35:23.013	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=0.000190000000, real_output=0, real_output_in_tx_index=0, indexes: 81157 90579 96426 100030 101314 
2017-02-22 02:35:23.062	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2998	daemon_send_resp.status == CORE_RPC_STATUS_BUSY. THROW EXCEPTION: error::daemon_busy
2017-02-22 02:35:23.062	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:697	/home/build/monero/source/src/wallet/wallet2.cpp:2998:N5tools5error11daemon_busyE: daemon is busy, request = sendrawtransaction
2017-02-22 02:35:23.062	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:119	Exception: tools::error::daemon_busy
2017-02-22 02:35:23.062	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:120	Unwound call stack:
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [1] /home/monero/current/monero-wallet-rpc:__wrap___cxa_throw+0x78 [0x814da8]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [2] /home/monero/current/monero-wallet-rpc:void tools::error::throw_wallet_ex<tools::error::daemon_busy, char [19]>(std::string&&, char const (&) [19])+0x189 [0x7618a9]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [3] /home/monero/current/monero-wallet-rpc:tools::wallet2::commit_tx(tools::wallet2::pending_tx&)+0x305 [0x7231b5]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [4] /home/monero/current/monero-wallet-rpc:tools::wallet2::commit_tx(std::vector<tools::wallet2::pending_tx, std::allocator<tools::wallet2::pending_tx> >&)+0x2a [0x72401a]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [5] /home/monero/current/monero-wallet-rpc:tools::wallet_rpc_server::on_transfer(tools::wallet_rpc::COMMAND_RPC_TRANSFER::request const&, tools::wallet_rpc::COMMAND_RPC_TRANSFER::response&, epee::json_rpc::error&)+0x55d [0x67762d]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [6] /home/monero/current/monero-wallet-rpc:bool tools::wallet_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x1052 [0x6daec2]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [7] /home/monero/current/monero-wallet-rpc:tools::wallet_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x139 [0x6e29b9]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [8] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&)+0x91 [0x6e3fc1]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [9] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&)+0xde [0x6b42ae]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [10] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_query_measure()+0xb0 [0x6b4530]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [11] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body()+0xd5 [0x6b4795]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [12] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::string&)+0x1c8 [0x6b4ee8]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [13] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long)+0x24 [0x6b5354]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [14] /home/monero/current/monero-wallet-rpc:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x24a [0x6ea75a]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [15] /home/monero/current/monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x69 [0x6d1829]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [16] /home/monero/current/monero-wallet-rpc:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x237 [0x6d1dc7]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [17] /home/monero/current/monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x467 [0x6d2347]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [18] /home/monero/current/monero-wallet-rpc:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x24b [0x6d267b]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [19] /home/monero/current/monero-wallet-rpc:boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&)+0x2f3 [0x6819c3]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [20] /home/monero/current/monero-wallet-rpc:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x210 [0x69f150]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [21] /home/monero/current/monero-wallet-rpc() [0x84713a]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [22] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7f64e2459064]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [23] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f64e1e8d62d]
2017-02-22 02:35:23.080	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	
2017-02-22 02:35:29.629	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:35:30.287	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 63079 70281 71837 101189 
2017-02-22 02:35:30.322	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:35:30.322	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 63079 70281 71837 101189 
2017-02-22 02:35:30.356	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:35:31.381	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 92913 98610 99412 101302 
2017-02-22 02:35:31.381	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=0.000190000000, real_output=1, real_output_in_tx_index=0, indexes: 52433 81157 85151 99406 100278 
2017-02-22 02:35:31.418	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:35:31.418	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 92913 98610 99412 101302 
2017-02-22 02:35:31.418	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=0.000190000000, real_output=1, real_output_in_tx_index=0, indexes: 52433 81157 85151 99406 100278 
2017-02-22 02:35:31.455	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2998	daemon_send_resp.status == CORE_RPC_STATUS_BUSY. THROW EXCEPTION: error::daemon_busy
2017-02-22 02:35:31.455	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:697	/home/build/monero/source/src/wallet/wallet2.cpp:2998:N5tools5error11daemon_busyE: daemon is busy, request = sendrawtransaction
2017-02-22 02:35:31.455	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:119	Exception: tools::error::daemon_busy
2017-02-22 02:35:31.455	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:120	Unwound call stack:
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [1] /home/monero/current/monero-wallet-rpc:__wrap___cxa_throw+0x78 [0x814da8]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [2] /home/monero/current/monero-wallet-rpc:void tools::error::throw_wallet_ex<tools::error::daemon_busy, char [19]>(std::string&&, char const (&) [19])+0x189 [0x7618a9]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [3] /home/monero/current/monero-wallet-rpc:tools::wallet2::commit_tx(tools::wallet2::pending_tx&)+0x305 [0x7231b5]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [4] /home/monero/current/monero-wallet-rpc:tools::wallet2::commit_tx(std::vector<tools::wallet2::pending_tx, std::allocator<tools::wallet2::pending_tx> >&)+0x2a [0x72401a]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [5] /home/monero/current/monero-wallet-rpc:tools::wallet_rpc_server::on_transfer(tools::wallet_rpc::COMMAND_RPC_TRANSFER::request const&, tools::wallet_rpc::COMMAND_RPC_TRANSFER::response&, epee::json_rpc::error&)+0x55d [0x67762d]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [6] /home/monero/current/monero-wallet-rpc:bool tools::wallet_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x1052 [0x6daec2]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [7] /home/monero/current/monero-wallet-rpc:tools::wallet_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x139 [0x6e29b9]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [8] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&)+0x91 [0x6e3fc1]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [9] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&)+0xde [0x6b42ae]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [10] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_query_measure()+0xb0 [0x6b4530]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [11] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body()+0xd5 [0x6b4795]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [12] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::string&)+0x1c8 [0x6b4ee8]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [13] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long)+0x24 [0x6b5354]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [14] /home/monero/current/monero-wallet-rpc:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x24a [0x6ea75a]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [15] /home/monero/current/monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x69 [0x6d1829]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [16] /home/monero/current/monero-wallet-rpc:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x237 [0x6d1dc7]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [17] /home/monero/current/monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x467 [0x6d2347]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [18] /home/monero/current/monero-wallet-rpc:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x24b [0x6d267b]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [19] /home/monero/current/monero-wallet-rpc:boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&)+0x2f3 [0x6819c3]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [20] /home/monero/current/monero-wallet-rpc:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x210 [0x69f150]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [21] /home/monero/current/monero-wallet-rpc() [0x84713a]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [22] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7f64e2459064]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [23] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f64e1e8d62d]
2017-02-22 02:35:31.458	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	
2017-02-22 02:37:03.803	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:37:04.490	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 63615 94246 98134 100809 
2017-02-22 02:37:04.524	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:37:04.525	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 63615 94246 98134 100809 
2017-02-22 02:37:04.559	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:37:05.359	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 48371 64370 76466 100823 
2017-02-22 02:37:05.359	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=0.000190000000, real_output=2, real_output_in_tx_index=0, indexes: 52895 77674 81157 94372 98778 
2017-02-22 02:37:05.396	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:37:05.396	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 48371 64370 76466 100823 
2017-02-22 02:37:05.396	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=0.000190000000, real_output=2, real_output_in_tx_index=0, indexes: 52895 77674 81157 94372 98778 
2017-02-22 02:37:05.433	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2998	daemon_send_resp.status == CORE_RPC_STATUS_BUSY. THROW EXCEPTION: error::daemon_busy
2017-02-22 02:37:05.433	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:697	/home/build/monero/source/src/wallet/wallet2.cpp:2998:N5tools5error11daemon_busyE: daemon is busy, request = sendrawtransaction
2017-02-22 02:37:05.433	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:119	Exception: tools::error::daemon_busy
2017-02-22 02:37:05.433	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:120	Unwound call stack:
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [1] /home/monero/current/monero-wallet-rpc:__wrap___cxa_throw+0x78 [0x814da8]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [2] /home/monero/current/monero-wallet-rpc:void tools::error::throw_wallet_ex<tools::error::daemon_busy, char [19]>(std::string&&, char const (&) [19])+0x189 [0x7618a9]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [3] /home/monero/current/monero-wallet-rpc:tools::wallet2::commit_tx(tools::wallet2::pending_tx&)+0x305 [0x7231b5]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [4] /home/monero/current/monero-wallet-rpc:tools::wallet2::commit_tx(std::vector<tools::wallet2::pending_tx, std::allocator<tools::wallet2::pending_tx> >&)+0x2a [0x72401a]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [5] /home/monero/current/monero-wallet-rpc:tools::wallet_rpc_server::on_transfer(tools::wallet_rpc::COMMAND_RPC_TRANSFER::request const&, tools::wallet_rpc::COMMAND_RPC_TRANSFER::response&, epee::json_rpc::error&)+0x55d [0x67762d]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [6] /home/monero/current/monero-wallet-rpc:bool tools::wallet_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x1052 [0x6daec2]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [7] /home/monero/current/monero-wallet-rpc:tools::wallet_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x139 [0x6e29b9]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [8] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&)+0x91 [0x6e3fc1]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [9] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&)+0xde [0x6b42ae]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [10] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_query_measure()+0xb0 [0x6b4530]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [11] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body()+0xd5 [0x6b4795]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [12] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::string&)+0x1c8 [0x6b4ee8]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [13] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long)+0x24 [0x6b5354]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [14] /home/monero/current/monero-wallet-rpc:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x24a [0x6ea75a]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [15] /home/monero/current/monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x69 [0x6d1829]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [16] /home/monero/current/monero-wallet-rpc:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x237 [0x6d1dc7]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [17] /home/monero/current/monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x467 [0x6d2347]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [18] /home/monero/current/monero-wallet-rpc:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x24b [0x6d267b]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [19] /home/monero/current/monero-wallet-rpc:boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&)+0x2f3 [0x6819c3]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [20] /home/monero/current/monero-wallet-rpc:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x210 [0x69f150]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [21] /home/monero/current/monero-wallet-rpc() [0x84713a]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [22] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7f64e2459064]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [23] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f64e1e8d62d]
2017-02-22 02:37:05.436	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	
2017-02-22 02:40:05.128	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:40:05.637	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 97093 98708 98775 100097 
2017-02-22 02:40:05.673	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:40:05.673	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 97093 98708 98775 100097 
2017-02-22 02:40:05.710	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:40:06.704	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 48521 85469 98659 101366 
2017-02-22 02:40:06.705	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=0.000190000000, real_output=2, real_output_in_tx_index=0, indexes: 45657 77916 81157 99933 101360 
2017-02-22 02:40:06.741	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3825	selected transfers: 
2017-02-22 02:40:06.742	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 34827 48521 85469 98659 101366 
2017-02-22 02:40:06.742	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.h:970	amount=0.000190000000, real_output=2, real_output_in_tx_index=0, indexes: 45657 77916 81157 99933 101360 
2017-02-22 02:40:06.780	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2998	daemon_send_resp.status == CORE_RPC_STATUS_BUSY. THROW EXCEPTION: error::daemon_busy
2017-02-22 02:40:06.780	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:697	/home/build/monero/source/src/wallet/wallet2.cpp:2998:N5tools5error11daemon_busyE: daemon is busy, request = sendrawtransaction
2017-02-22 02:40:06.780	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:119	Exception: tools::error::daemon_busy
2017-02-22 02:40:06.780	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:120	Unwound call stack:
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [1] /home/monero/current/monero-wallet-rpc:__wrap___cxa_throw+0x78 [0x814da8]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [2] /home/monero/current/monero-wallet-rpc:void tools::error::throw_wallet_ex<tools::error::daemon_busy, char [19]>(std::string&&, char const (&) [19])+0x189 [0x7618a9]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [3] /home/monero/current/monero-wallet-rpc:tools::wallet2::commit_tx(tools::wallet2::pending_tx&)+0x305 [0x7231b5]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [4] /home/monero/current/monero-wallet-rpc:tools::wallet2::commit_tx(std::vector<tools::wallet2::pending_tx, std::allocator<tools::wallet2::pending_tx> >&)+0x2a [0x72401a]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [5] /home/monero/current/monero-wallet-rpc:tools::wallet_rpc_server::on_transfer(tools::wallet_rpc::COMMAND_RPC_TRANSFER::request const&, tools::wallet_rpc::COMMAND_RPC_TRANSFER::response&, epee::json_rpc::error&)+0x55d [0x67762d]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [6] /home/monero/current/monero-wallet-rpc:bool tools::wallet_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x1052 [0x6daec2]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [7] /home/monero/current/monero-wallet-rpc:tools::wallet_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x139 [0x6e29b9]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [8] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&)+0x91 [0x6e3fc1]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [9] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&)+0xde [0x6b42ae]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [10] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_query_measure()+0xb0 [0x6b4530]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [11] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body()+0xd5 [0x6b4795]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [12] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::string&)+0x1c8 [0x6b4ee8]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [13] /home/monero/current/monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long)+0x24 [0x6b5354]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [14] /home/monero/current/monero-wallet-rpc:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x24a [0x6ea75a]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [15] /home/monero/current/monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x69 [0x6d1829]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [16] /home/monero/current/monero-wallet-rpc:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x237 [0x6d1dc7]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [17] /home/monero/current/monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x467 [0x6d2347]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [18] /home/monero/current/monero-wallet-rpc:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x24b [0x6d267b]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [19] /home/monero/current/monero-wallet-rpc:boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&)+0x2f3 [0x6819c3]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [20] /home/monero/current/monero-wallet-rpc:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x210 [0x69f150]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [21] /home/monero/current/monero-wallet-rpc() [0x84713a]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [22] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7f64e2459064]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158	    [23] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f64e1e8d62d]
2017-02-22 02:40:06.784	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:158
```

# Discussion History
## moneromooo-monero | 2017-02-23T21:01:19+00:00
What exact RPC call are you making ?

## gituser | 2017-02-23T21:30:11+00:00
Was trying to send a transaction via usual transfer call via RPC.

## moneromooo-monero | 2017-02-23T22:39:51+00:00
Do you use a local or remote daemon ?

## osensei | 2017-02-24T01:57:44+00:00
I just opened issue #1788 , maybe this is related?

## gituser | 2017-02-24T03:53:26+00:00
@moneromooo-monero daemon is remote.

## moneromooo-monero | 2017-02-24T09:05:33+00:00
Try https://github.com/monero-project/monero/pull/1786

## moneromooo-monero | 2017-02-26T23:56:15+00:00
Does it still happen with current master ? Some RPC timeout were just fixed.

## gituser | 2017-02-27T02:33:48+00:00
I'm sorry for the silence. I've tried before latest master didn't build at all. Trying now.

## gituser | 2017-02-27T03:22:08+00:00
Getting this on the commit beee286c7b08308f3193e7d2cb8d66f0e689da28:

```
/home/build/monero/source/src/blockchain_utilities/bootstrap_file.cpp: In member function 'seek_to_first_chunk':
/home/build/monero/source/src/blockchain_utilities/bootstrap_file.cpp:368:3: warning: 'MEM[(unsigned char &)&bfi + 1]' may be used uninitialized in this function [-Wmaybe-uninitialized]
   MINFO("bootstrap file v" << unsigned(bfi.major_version) << "." << unsigned(bfi.minor_version));
   ^
/home/build/monero/source/src/blockchain_utilities/bootstrap_file.cpp:365:24: note: 'MEM[(unsigned char &)&bfi + 1]' was declared here
   bootstrap::file_info bfi;
                        ^
/home/build/monero/source/external/easylogging++/easylogging++.h:5113:21: warning: 'MEM[(unsigned int &)&bfi + 4]' may be used uninitialized in this function [-Wmaybe-uninitialized]
                     m_messageBuilder << log;
                     ^
/home/build/monero/source/src/blockchain_utilities/bootstrap_file.cpp:365:24: note: 'MEM[(unsigned int &)&bfi + 4]' was declared here
   bootstrap::file_info bfi;
                        ^
/tmp/ccAS9lTf.ltrans24.ltrans.o:(.rodata._ZZN5boost9function2INS_14iterator_rangeIN9__gnu_cxx17__normal_iteratorIPcSsEEEES5_S5_E9assign_toINS_9algorithm6detail13token_finderFINSA_10is_any_ofFIcEEEEEEvT_E13stored_vtable[_ZZN5boost9function2INS_14iterator_rangeIN9__gnu_cxx17__normal_iteratorIPcSsEEEES5_S5_E9assign_toINS_9algorithm6detail13token_finderFINSA_10is_any_ofFIcEEEEEEvT_E13stored_vtable]+0x0): multiple definition of `void boost::function2<boost::iterator_range<__gnu_cxx::__normal_iterator<char*, std::string> >, __gnu_cxx::__normal_iterator<char*, std::string>, __gnu_cxx::__normal_iterator<char*, std::string> >::assign_to<boost::algorithm::detail::token_finderF<boost::algorithm::detail::is_any_ofF<char> > >(boost::algorithm::detail::token_finderF<boost::algorithm::detail::is_any_ofF<char> >)::stored_vtable'
/home/build/monero/boost/boost.build/lib/libboost_thread.a(thread.o):(.rodata._ZZN5boost9function2INS_14iterator_rangeIN9__gnu_cxx17__normal_iteratorIPcSsEEEES5_S5_E9assign_toINS_9algorithm6detail13token_finderFINSA_10is_any_ofFIcEEEEEEvT_E13stored_vtable[_ZZN5boost9function2INS_14iterator_rangeIN9__gnu_cxx17__normal_iteratorIPcSsEEEES5_S5_E9assign_toINS_9algorithm6detail13token_finderFINSA_10is_any_ofFIcEEEEEEvT_E13stored_vtable]+0x0): first defined here
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/blockchain_export.dir/build.make:164: recipe for target 'bin/monero-blockchain-export' failed
make[3]: *** [bin/monero-blockchain-export] Error 1
```

## hyc | 2017-02-27T06:38:38+00:00
That's caused by LTO. set USE_LTO=false in Cmake.

## gituser | 2017-02-27T07:11:08+00:00
@hyc can I pass it through environment variable?

e.g.
```
export USE_LTO=false
make release-static
 ```

## hyc | 2017-02-27T07:42:00+00:00
No. It's a CMake variable, not a make variable. I would have said "make" if I meant make. I said Cmake.

You can edit build/release/CMakeCache.txt and set it in there.

## moneromooo-monero | 2017-12-23T11:57:34+00:00
Are you still getting these or can this be closed ?

## gituser | 2017-12-23T13:36:03+00:00
this can be closed.

# Action History
- Created by: gituser | 2017-02-21T23:45:06+00:00
- Closed at: 2017-12-23T13:36:03+00:00
