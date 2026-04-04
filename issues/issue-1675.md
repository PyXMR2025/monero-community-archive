---
title: monero-wallet-rpc Unable to make payments
source_url: https://github.com/monero-project/monero/issues/1675
author: Snipa22
assignees: []
labels: []
created_at: '2017-02-04T20:21:04+00:00'
updated_at: '2017-10-03T10:00:26+00:00'
type: issue
status: closed
closed_at: '2017-10-03T10:00:26+00:00'
---

# Original Description
No crashes this time around, but it's reporting that it's unable to connect to the daemon, however, on both sides of this process, it's getting new blocks from the daemon safely and successfully.
```
2017-02-04 20:14:55.106 [RPC0]  TRACE   net.throttle    src/p2p/network_throttle-detail.cpp:189 Moving counter buffer by 1 second 650623 < 650646 (last time 650624)
2017-02-04 20:14:55.106 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:527   [127.0.0.1:59954 INC] [sock 12] Async send requested 178
2017-02-04 20:14:55.106 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:601   [127.0.0.1:59954 INC] [sock 12] Async send calledback 178
2017-02-04 20:14:55.107 [RPC0]  INFO    net.p2p src/p2p/connection_basic.cpp:164        Spawned connection p2p#13 to 0.0.0.0 currently we have sockets count:3
2017-02-04 20:14:55.107 [RPC0]  INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:85    test, connection constructor set m_connection_type=1
2017-02-04 20:14:55.107 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:151   [sock 13] new connection from 127.0.0.1:59956 INC to 127.0.0.1:37458, total sockets objects 3
2017-02-04 20:14:55.107 [RPC0]  INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:270    connection type RPC 127.0.0.1:37458 <--> 127.0.0.1:59956
2017-02-04 20:14:55.107 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:601   [127.0.0.1:59954 INC] [sock 12] Async send calledback 59
2017-02-04 20:14:55.107 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:98    [sock 12] Socket destroyed
2017-02-04 20:14:55.107 [RPC0]  INFO    net.p2p src/p2p/connection_basic.cpp:172        Destructing connection p2p#11 to 127.0.0.1
2017-02-04 20:14:55.107 [RPC0]  TRACE   net.throttle    src/p2p/network_throttle-detail.cpp:189 Moving counter buffer by 1 second 1.55495e+104 < 650646 (last time 1.55495e+104)
2017-02-04 20:14:55.107 [RPC0]  TRACE   net.throttle    src/p2p/network_throttle-detail.cpp:189 Moving counter buffer by 1 second 650645 < 650646 (last time 650645)
2017-02-04 20:14:55.107 [RPC0]  TRACE   wallet.rpc      src/wallet/wallet_rpc_server.cpp:399    on_transfer_split starts
2017-02-04 20:14:55.145 [RPC0]  TRACE   net     contrib/epee/include/net/net_helper.h:397       READ ENDS: Success. bytes_tr: 203
2017-02-04 20:14:55.145 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_client.h:690      http_stream_filter::parse_cached_header(*)
2017-02-04 20:15:00.145 [RPC0]  TRACE   net     contrib/epee/include/net/net_helper.h:538       Timed out socket
2017-02-04 20:15:00.145 [RPC0]  TRACE   net     contrib/epee/include/net/net_helper.h:384       READ ENDS: Connection err_code 125
2017-02-04 20:15:00.145 [RPC0]  ERROR   net.http        contrib/epee/include/net/http_client.h:401      Unexpected recv fail
2017-02-04 20:15:00.145 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_client.h:447      Returning false because of wrong state machine. state: 5
2017-02-04 20:15:00.145 [RPC0]  INFO    net.http        contrib/epee/include/storages/http_abstract_invoke.h:47 Failed to invoke http request to  /json_rpc
2017-02-04 20:15:00.145 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:4641     !r. THROW EXCEPTION: error::no_connection_to_daemon
2017-02-04 20:15:00.145 [RPC0]  WARN    net.http        src/wallet/wallet_errors.h:697  /usr/local/src/monero/src/wallet/wallet2.cpp:4641:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = select_available_unmixable_outputs
2017-02-04 20:15:00.145 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: tools::error::no_connection_to_daemon
2017-02-04 20:15:00.146 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [1] /usr/local/src/monero/build/release/bin/monero-wallet-rpc:tools::wallet2::select_available_outputs_from_histogram(unsigned long, bool, bool, bool)+0x494 [0x5c59a4]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [2] /usr/local/src/monero/build/release/bin/monero-wallet-rpc:tools::wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::allocator<unsigned char> >, bool)+0x22d [0x5c64ed]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [3] /usr/local/src/monero/build/release/bin/monero-wallet-rpc:tools::wallet_rpc_server::on_transfer(tools::wallet_rpc::COMMAND_RPC_TRANSFER::request const&, tools::wallet_rpc::COMMAND_RPC_TRANSFER::response&, epee::json_rpc::error&)+0x35d [0x4d3c5d]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [4] /usr/local/src/monero/build/release/bin/monero-wallet-rpc() [0x65e279]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [5] /usr/local/src/monero/build/release/bin/monero-wallet-rpc() [0x512aa1]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [6] /usr/local/src/monero/build/release/bin/monero-wallet-rpc() [0x4ff27a]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [7] /usr/local/src/monero/build/release/bin/monero-wallet-rpc() [0x4e9e75]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [8] /usr/local/src/monero/build/release/bin/monero-wallet-rpc() [0x4ebbb7]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [9] /usr/local/src/monero/build/release/bin/monero-wallet-rpc:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x1ce [0x4ebdce]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [10] /usr/local/src/monero/build/release/bin/monero-wallet-rpc() [0x4f3005]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [11] /usr/local/src/monero/build/release/bin/monero-wallet-rpc:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x118 [0x4f3468]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [12] /usr/local/src/monero/build/release/bin/monero-wallet-rpc:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x660 [0x4f3bd0]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [13] /usr/local/src/monero/build/release/bin/monero-wallet-rpc() [0x5ebfa4]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [14] /usr/local/src/monero/build/release/bin/monero-wallet-rpc:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x14f [0x4e7bef]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [15] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7fb99c6145d5]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [16] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fb99b1446ba]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [17] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fb99d1d182d]
2017-02-04 20:15:00.147 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158  
2017-02-04 20:15:00.147 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:554  HTTP_RESPONSE_HEAD: << 
HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 117
Content-Type: text/plain
Last-Modified: Sat, 04 Feb 2017 20:15:00 GMT
Accept-Ranges: bytes
Connection: close

```

/usr/local/src/monero/build/release/bin/monero-wallet-rpc --wallet-file PoolWallet --rpc-bind-port 37458 --disable-rpc-login --log-level 4 --log-file /home/pooldaemon/wallet-rpc.log

Running git: e56bf442c394bc5977cb7931d78b4cfca5e3a0b2

# Discussion History
## Snipa22 | 2017-02-04T21:18:17+00:00
I have rolled back to: 15eb2bcf6f2132c5410e937186b6a3121147d628 and verified that this is working as intended. The command is a transfer_multi command being sent in over RPC with the standard formatting as available in the documentation.

## moneromooo-monero | 2017-02-05T11:07:09+00:00
It's probably 2bf029be172a47ace8134143e1320fdb10d3ea44. If your daemon is trusted, add "trusted_daemon: true" to your JSON. This speeds up the histogram a lot.

## moneromooo-monero | 2017-02-11T20:01:22+00:00
I got this to happen, and it was just due to the long run time of the histogram RPC for untrusted daemons.

## Snipa22 | 2017-02-12T01:05:11+00:00
Good to know, might be worth documenting somewhere, but I'll make sure to track that flag for future RPC code related stuff.

## moneromooo-monero | 2017-03-25T16:53:31+00:00
Does this now work in the same conditions for you with current master ?

## arnuschky | 2017-03-25T20:12:29+00:00
This works for me now with 0.10.3 and `trusted-daemon=true`. (I encountered the same problem with 0.10.2)

## moneromooo-monero | 2017-10-03T09:56:40+00:00
+resolved

# Action History
- Created by: Snipa22 | 2017-02-04T20:21:04+00:00
- Closed at: 2017-10-03T10:00:26+00:00
