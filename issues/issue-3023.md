---
title: Suddenly get "Transaction not found in pool" in log file (running a pool)
source_url: https://github.com/monero-project/monero/issues/3023
author: sleever
assignees: []
labels:
- invalid
created_at: '2017-12-28T22:11:02+00:00'
updated_at: '2017-12-29T19:56:24+00:00'
type: issue
status: closed
closed_at: '2017-12-29T19:56:24+00:00'
---

# Original Description
Hello everybody,

Back again. We're currently mining away at a block for 4 days now and haven't had any luck regarding finding a block as you might have guessed.

The issue exists in the Electroneum wallet daemon log and i'm also posting this here as the electroneum wallet is a direct fork of this wallet.

The scenario:

Before the 4 days we've mined a few blocks succesfully but as of the 24th/25th we have no luck in finding a block anymore. By plowing through the blocks on the 25th I found errors regarding "runtime_errors" which I solved by restarting the daemon on the pool which resulted in the error to be gone for a period of time.

However, currently i'm looking in the logs again and see that the runtime_error has returned again with the message "Transaction not found in pool".

My questions:

1. What does this error mean?
2. How can this error suddenly appear?
3. Can this error cause my pool not to find any blocks?
4. How can I solve this error?

The error log:

`2017-12-28 16:40:08.911 [P2P1]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2674 WARNING: batch transaction mode already enabled, but asked to enable batch mode
2017-12-28 16:40:08.967 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:893  ^[[1;32mREORGANIZE SUCCESS! on height: 87570, new blockchain size: 87572^[[0m
2017-12-28 16:40:09.251 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1151    ^[[1;33m[52.224.181.117:26967 OUT]  Synced 87572/87572^[[0m
2017-12-28 16:40:09.265 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1518    ^[[1;32mSYNCHRONIZED OK^[[0m
2017-12-28 16:44:56.077 [RPC1]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:1015    Transaction not found in pool
2017-12-28 16:44:56.077 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:120  Exception: std::runtime_error
2017-12-28 16:44:56.077 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:121  Unwound call stack:
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [1] ./electroneumd:__cxa_throw+0x106 [0x7d96e6]
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [2] ./electroneumd:cryptonote::get_block_complete_entry(cryptonote::block&, cryptonote::tx_memory_pool&)+0x2ab [0x776b9b]
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [3] ./electroneumd:cryptonote::core::handle_block_found(cryptonote::block&)+0x7e [0x778dee]
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [4] ./electroneumd:cryptonote::core_rpc_server::on_submitblock(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [5] ./electroneumd:bool cryptonote::core_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [6] ./electroneumd:cryptonote::core_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [7] ./electroneumd:epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [8] ./electroneumd:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_r$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [9] ./electroneumd:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body()+0x158 [0x5e4508]
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [10] ./electroneumd:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_tra$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [11] ./electroneumd:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long)+0x37 [0x68a357]
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [12] ./electroneumd:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code cons$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [13] ./electroneumd:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<ep$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [14] ./electroneumd:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [15] ./electroneumd:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<bo$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [16] ./electroneumd:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi:$
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [17] ./electroneumd:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x807 [0x5b1d87]
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [18] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0+0x115d5 [0x7f6a535db5d5]
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [19] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7f6a5276f6ba]
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159      [20] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f6a524a53dd]
2017-12-28 16:44:56.086 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:159
`

Thank you very much in advance for helping me out!

Best regards,

# Discussion History
## sleever | 2017-12-29T19:15:30+00:00
Update 1:

Today I've investigated the issue further as you can read in issue #3030. Specifically regarding the error "transaction not found in pool" I have determined that the error originates from the following location in the code:

![image](https://user-images.githubusercontent.com/11486220/34445550-a3816002-ecd4-11e7-817f-a0f095011ab3.png)

This gives me the assumption that it does seem to do something to a found block that I don't like, which could mean why we're not finding a block. When we were still finding blocks this error message didn't appear.

Next to the investigation I have imported a fresh copy of a fully synced blockchain which is running at the pool now. However, still without success. 

Does anyone have any pointers regarding these messages or am I creating a storm in a glass of water here?

## moneromooo-monero | 2017-12-29T19:55:44+00:00
This does not seem to be a bug. You found a block, but one of the txes in the block you found was removed the txpool (probably because it was just included in another block).

+invalid

# Action History
- Created by: sleever | 2017-12-28T22:11:02+00:00
- Closed at: 2017-12-29T19:56:24+00:00
