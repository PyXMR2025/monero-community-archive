---
title: 'Qt wallet can''t synch up with monerod: GET blocks.bin request never completes'
source_url: https://github.com/monero-project/monero/issues/2545
author: radfish
assignees: []
labels: []
created_at: '2017-09-28T03:00:06+00:00'
updated_at: '2017-10-17T21:34:09+00:00'
type: issue
status: closed
closed_at: '2017-10-17T21:16:15+00:00'
---

# Original Description
On wallet open, it first waits for daemon to synchronize, then it waits to get blocks, then it issues some kind of request, which results in the following exception at the daemon. The sequence keeps repeating.

```
2017-09-28 02:55:03.651 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:120  Exception: cryptonote::TX_DNE
2017-09-28 02:55:03.652 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:121  Unwound call stack:
2017-09-28 02:55:03.660 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [1] /usr/bin/monerod:__cxa_throw+0xac [0x7d52a8]
2017-09-28 02:55:03.660 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [2] /usr/bin/monerod+0x2c6220 [0x71d220]
2017-09-28 02:55:03.661 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [3] /usr/bin/monerod:cryptonote::BlockchainLMDB::get_tx_block_height(crypto::hash const&) const+0x3a4 [0x728b6c]
2017-09-28 02:55:03.661 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [4] /usr/bin/monerod:cryptonote::core_rpc_server::on_get_transactions(cryptonote::COMMAND_RPC_GET_TRANSACTIONS::request const&, cryptonote::COMMAND_RPC_GET_TRANSACTIONS::response&)+0xb98 [0x6cfe38]
2017-09-28 02:55:03.661 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [5] /usr/bin/monerod:bool cryptonote::core_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x38dc [0x6fc274]
2017-09-28 02:55:03.661 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [6] /usr/bin/monerod:cryptonote::core_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x178 [0x70bf10]
2017-09-28 02:55:03.661 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [7] /usr/bin/monerod:epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&)+0xa4 [0x70ca58]
2017-09-28 02:55:03.661 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [8] /usr/bin/monerod:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&)+0x124 [0x6e1bf8]
2017-09-28 02:55:03.662 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [9] /usr/bin/monerod:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body()+0x18c [0x6e1f5c]
2017-09-28 02:55:03.662 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [10] /usr/bin/monerod:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&)+0x248 [0x714d80]
2017-09-28 02:55:03.662 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [11] /usr/bin/monerod:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned int)+0x48 [0x715190]
2017-09-28 02:55:03.662 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [12] /usr/bin/monerod:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned int)+0x1cc [0x7153bc]
2017-09-28 02:55:03.662 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [13] /usr/bin/monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned int> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned int>&)+0x8c [0x6f70a4]
2017-09-28 02:55:03.663 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [14] /usr/bin/monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned int)+0x15c [0x6f73b0]
2017-09-28 02:55:03.663 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [15] /usr/bin/monerod:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x274 [0x6f7728]
2017-09-28 02:55:03.663 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [16] /usr/bin/monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned int)+0x1a0 [0x6f79cc]
2017-09-28 02:55:03.664 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [17] /usr/bin/monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned int)+0x1d4 [0x5bb948]
2017-09-28 02:55:03.664 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [18] /usr/bin/monerod:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x734 [0x5dc790]
2017-09-28 02:55:03.664 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [19] /usr/lib/libboost_thread.so.1.65.1+0x1096c [0xb69cd96c]
2017-09-28 02:55:03.664 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159  

```

wallet log:

```
qml: >>> wallet refreshed
Checking connection status
qml: >>> wallet updated
NEW STATUS  Wallet::ConnectionStatus(ConnectionStatus_Connected)
qml: Wallet connection status changed 1
2017-09-28 03:00:08.228     7fffc5c53700        WARN    wallet.wallet2  src/wallet/wallet2.cpp:1554    Error calling gettransactions daemon RPC: r 0, status 
refreshed
qml: >>> wallet refreshed
Checking connection status
qml: >>> wallet updated
NEW STATUS  Wallet::ConnectionStatus(ConnectionStatus_Disconnected)
qml: Wallet connection status changed 0
2017-09-28 03:00:18.228     7fffc5c53700        ERROR   net.http        contrib/epee/include/net/http_client.h:390     HTTP_CLIENT: Failed to SEND
refreshed
```

# Discussion History
## moneromooo-monero | 2017-09-28T21:07:35+00:00
That looks like the txpool claims to have a tx which is in fact not found. Any errors before that in the monerod log ?

## moneromooo-monero | 2017-10-02T15:34:57+00:00
In fact, this looks like a bug which was fixed in https://github.com/monero-project/monero/pull/2552

## moneromooo-monero | 2017-10-03T08:41:33+00:00
And by #2552 I mean #2548.

## radfish | 2017-10-07T20:38:43+00:00
Rebuilt master (with #2548 now). Exception went away, but Qt wallet doesn't ever connect.
The cycle was due to a 3min 30sec timeout in wallet2.h. I increased that to 3 hours to prevent it from triggering. What seems to be happening is:
1. monerod is synchronized with low load on the disk,
2. wallet sends a GET blocks.bin request, disk load goes up and monerod log freezes completely for ~20mins (one thread in D state),
3. due to stalling, monerod unsynchronizes
4. monerod resynchronizes, and issues 'SYNCHRONIZED OK'
5. nothing happens in the wallet log

There is never a 'processed' from the core_rpc_server in the monerod log. So, either the request takes more than several hours to process, or it gets aborted by the daemon (due to losing synchronization or for some other reason). Also, it is unclear if wallet rpc connection is still alive (I don't see any messages with the relevant IP address after the initial connection is made, so I assume the connection is indeed alive).

So, what is this blocks.bin request have to do (scan all 28GB of blockchain?) and, whatever it may be, why can it block the whole daemon (something not right with the asynch logic)?

PS. Yes, my disk is NFS and it is very very slow.

## moneromooo-monero | 2017-10-07T21:31:09+00:00
getblocks.bin will do a binary search on the block hash table, then read a segment of the block blob table, and a segment of the tx blob table. Probably also a few smaller bits. This takes the blockchain lock, for obvious reasons. It is plausible that a reader/writer system be possible, which would allow the blockchain to continue updating.

## radfish | 2017-10-07T22:23:45+00:00
Ok. Thanks a lot for the explanation. Ok, so the async logic is fine then, it needs exclusive access, so be it. Maybe I should try to track the processing of the request to see if daemon eventually finishes it, and if so, why doesn't the wallet get a response (even if after a very long time, and even if the daemon falls out of sync after finishing the request.

## moneromooo-monero | 2017-10-07T22:30:32+00:00
This is possible a TCP timeout (lower level).

## radfish | 2017-10-17T21:16:15+00:00
This is no longer happening after (1) deleting LMDB (which we know was corrupt due to kernel crash with dbsync-fast) and re-importing blockchain.raw from scratch, (2) moving the daemon to SSD via NBD, and (3) with latest master merges.

I'm closing this bug report, but this issue raises some things to consider:
(1) error reporting in the wallet-daemon communication could be improved, specifically, have daemon report progress on potentially long-running requests, and have the wallet report the state of the connection and of current request.
(2) Change default to dbsync-safe. Users who want to trade speed for risk can change it -- as opposed to the other way around.
(3) Detect potential corruption of DB somehow (periodic concurrent scan? feedback from other nodes?). My daemon has been running with a corrupt DB for months. And, I'm probably not alone. This probably creates noise in the network.
(3a) Before any automatic checks, perhaps implement user-triggerable online DB verification to improve the current alternative of having to export and re-import the blockchain to check your DB.
(4) support concurrent access the DB while processing requests from the wallet.

## hyc | 2017-10-17T21:33:15+00:00
(2) the daemon now automatically switches to dbsync-safe after it catches up to the network.
(4) what do you mean? the DB supports arbitrary concurrency. [edit] Oh I see, the blockchain lock.

# Action History
- Created by: radfish | 2017-09-28T03:00:06+00:00
- Closed at: 2017-10-17T21:16:15+00:00
