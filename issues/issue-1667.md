---
title: monero-wallet-rpc segfault
source_url: https://github.com/monero-project/monero/issues/1667
author: Snipa22
assignees: []
labels: []
created_at: '2017-02-03T17:09:31+00:00'
updated_at: '2017-02-04T20:22:02+00:00'
type: issue
status: closed
closed_at: '2017-02-04T20:22:02+00:00'
---

# Original Description
Built from commit: 15eb2bcf6f2132c5410e937186b6a3121147d628
System: Ubuntu 16.04 LTS, x86_64

Symptom: monero-wallet-rpc crashes if it's unable to get a response from /getblocks.bin. 

I have confirmed that the monero daemon is still responding to the RPC request at the time of the crash.

Logs:
```
2017-02-03 15:40:44.000	[RPC0]	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:1709	Refresh done, blocks received: 0, balance: 18.959937936764, unlocked: 18.959937936764
2017-02-03 15:41:04.000	[RPC0]	ERROR	net.http	contrib/epee/include/net/http_client.h:354	HTTP_CLIENT: Failed to SEND
2017-02-03 15:41:04.000	[RPC0]	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:78	Failed to invoke http request to  http://localhost:18081/getblocks.bin
2017-02-03 15:41:04.000	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1174	!r. THROW EXCEPTION: error::no_connection_to_daemon
2017-02-03 15:41:04.000	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:697	/usr/local/src/monero/src/wallet/wallet2.cpp:1174:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
2017-02-03 15:41:04.001	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:111	Exception: tools::error::no_connection_to_daemon
2017-02-03 15:41:04.001	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:112	Unwound call stack:
2017-02-03 15:41:04.001	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     1                  0x683550 __cxa_throw + 0x70
2017-02-03 15:41:04.001	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     2                  0x613cbd void tools::error::throw_wallet_ex<tools::error::no_connection_to_daemon, char [14]>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, char const (&) [14]) [clone .constprop.1349] + 0x16d
2017-02-03 15:41:04.002	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     3                  0x519231 tools::wallet2::pull_blocks(unsigned long, unsigned long&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> >&, std::vector<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices, std::allocator<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::block_output_indices> >&) + 0x5d1
2017-02-03 15:41:04.002	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     4                  0x546e56 tools::wallet2::refresh(unsigned long, unsigned long&, bool&) + 0x1a6
2017-02-03 15:41:04.002	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     5                  0x4f54d2 epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::idle_callback_conext<tools::wallet_rpc_server::run()::{lambda()#1}>::call_handler() [clone .lto_priv.4076] + 0x32
2017-02-03 15:41:04.002	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     6                  0x4df275 epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::idle_callback_conext_base>) + 0x15
2017-02-03 15:41:04.003	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     7                  0x4dbe7c boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0xec
2017-02-03 15:41:04.003	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     8                  0x6396a4 boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1873] + 0x404
2017-02-03 15:41:04.003	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     9                  0x4e4d5f epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() + 0x14f
2017-02-03 15:41:04.004	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     a                  0x7fbe812915d5 boost::this_thread::interruption_point() + 0x145
2017-02-03 15:41:04.004	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     b                  0x7fbe800576ba start_thread + 0xca
2017-02-03 15:41:04.004	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     c                  0x7fbe81e4e82d clone + 0x6d
2017-02-03 15:41:04.004	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:134	     d                  0x0
```
pooldaemon@iof758c:~/logs2$ 

# Discussion History
## moneromooo-monero | 2017-02-03T19:03:23+00:00
This is not a crash.
Does it really crash ? If so, stack trace *of the crash* needed.

## Snipa22 | 2017-02-03T19:12:55+00:00
It does indeed crash, and this is the stack trace from the XMR wallet logs, there are no additional logs, just a note on the console Aborted(Stack Dumped)

## moneromooo-monero | 2017-02-03T20:30:08+00:00
You should get a core, let its name be $CORE:
gdb /path/to/monerod /path/to/$CORE
bt


## moneromooo-monero | 2017-02-03T20:30:40+00:00
Before that, check cores are enabled:
ulimit -c
if it says 0:
ulimit -c unlimited

## Snipa22 | 2017-02-03T20:58:33+00:00
Fresh logs and backtraces, hot off the presses.

```
2017-02-03 20:53:12.570	[RPC0]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-02-03 20:53:12.570	[RPC0]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type RPC 127.0.0.1:37458 <--> 127.0.0.1:60714
2017-02-03 20:53:12.570	[RPC0]	ERROR	net	contrib/epee/include/storages/portable_storage_from_json.h:104	Wrong JSON character at: 300000000000000,"address":"422sqocg7bvjUtpxGX6EHWFAYZPAi5MJujKdSYinNvHNR3DkCDsz7uFWbwaVe4vUMveKAzAiA4j8xgUi29TpKXpm41kvtLD"}],"fee":150000000000,"mixin":3,"unlock_time":0,"get_tx_key":true}}
2017-02-03 20:53:12.570	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:111	Exception: std::runtime_error
2017-02-03 20:53:12.570	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:112	Unwound call stack:
2017-02-03 20:53:12.571	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     1                  0x683550 __cxa_throw + 0x70
2017-02-03 20:53:12.571	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     2                  0x62880b void epee::serialization::json::run_handler<epee::serialization::portable_storage>(epee::serialization::portable_storage::hsection, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, epee::serialization::portable_storage&) [clone .constprop.1492] + 0x24db
2017-02-03 20:53:12.571	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     3                  0x626f33 void epee::serialization::json::run_handler<epee::serialization::portable_storage>(epee::serialization::portable_storage::hsection, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, epee::serialization::portable_storage&) [clone .constprop.1492] + 0xc03
2017-02-03 20:53:12.572	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     4                  0x628273 void epee::serialization::json::run_handler<epee::serialization::portable_storage>(epee::serialization::portable_storage::hsection, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, epee::serialization::portable_storage&) [clone .constprop.1492] + 0x1f43
2017-02-03 20:53:12.572	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     5                  0x62cb15 epee::serialization::portable_storage::load_from_json(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1490] + 0x25
2017-02-03 20:53:12.572	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     6                  0x5dce70 bool tools::wallet_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&) [clone .constprop.651] + 0xb0
2017-02-03 20:53:12.573	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     7                  0x4fc6b1 epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&) + 0xf1
2017-02-03 20:53:12.573	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     8                  0x510e5a epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&) + 0x21a
2017-02-03 20:53:12.573	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     9                  0x4e7625 epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) + 0xae5
2017-02-03 20:53:12.573	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     a                  0x4e9367 epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long) + 0x27
2017-02-03 20:53:12.574	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     b                  0x4e957e epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long) + 0x1ce
2017-02-03 20:53:12.574	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     c                  0x505665 void boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>::operator()<boost::system::error_code, unsigned long>(boost::system::error_code const&, unsigned long const&) + 0xc5
2017-02-03 20:53:12.574	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     d                  0x505a93 boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0xe3
2017-02-03 20:53:12.575	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     e                  0x506240 boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0x650
2017-02-03 20:53:12.575	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	     f                  0x6396a4 boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1873] + 0x404
2017-02-03 20:53:12.575	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	    10                  0x4e4d5f epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() + 0x14f
2017-02-03 20:53:12.575	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	    11                  0x7fb472eeb5d5 boost::this_thread::interruption_point() + 0x145
2017-02-03 20:53:12.576	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	    12                  0x7fb471cb16ba start_thread + 0xca
2017-02-03 20:53:12.576	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:138	    13                  0x7fb473aa882d clone + 0x6d
2017-02-03 20:53:12.576	[RPC0]	INFO 	stacktrace	src/common/stack_trace.cpp:134	    14                  0x0
pooldaemon@iof758c:~$ gdb /usr/local/src/monero/build/release/bin/monero-wallet-rpc core
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.04) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /usr/local/src/monero/build/release/bin/monero-wallet-rpc...done.

warning: core file may not match specified executable file.
[New LWP 29700]
[New LWP 26180]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Core was generated by `/usr/local/src/monero/build/release/bin/monero-wallet-rpc --wallet-file PoolWal'.
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x00000000006a3028 in read_encoded_value_with_base ()
[Current thread is 1 (Thread 0x7fb45effd700 (LWP 29700))]
(gdb) bt
#0  0x00000000006a3028 in read_encoded_value_with_base ()
#1  0x00000000006a31af in __gcc_personality_v0 ()
#2  0x00007fb472759a9f in __libunwind_Unwind_RaiseException () from /usr/lib/x86_64-linux-gnu/libunwind.so.8
#3  0x00007fb47225d90c in __cxa_throw () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#4  0x000000000068359c in __cxa_throw ()
#5  0x000000000062880b in void epee::serialization::json::run_handler<epee::serialization::portable_storage>(epee::serialization::portable_storage::hsection, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, epee::serialization::portable_storage&) [clone .constprop.1492] ()
#6  0x0000000000626f33 in void epee::serialization::json::run_handler<epee::serialization::portable_storage>(epee::serialization::portable_storage::hsection, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, epee::serialization::portable_storage&) [clone .constprop.1492] ()
#7  0x0000000000628273 in void epee::serialization::json::run_handler<epee::serialization::portable_storage>(epee::serialization::portable_storage::hsection, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, epee::serialization::portable_storage&) [clone .constprop.1492] ()
#8  0x000000000062cb15 in epee::serialization::portable_storage::load_from_json(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1490] ()
#9  0x00000000005dce70 in bool tools::wallet_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&) [clone .constprop.651] ()
#10 0x00000000004fc6b1 in epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&) ()
#11 0x0000000000510e5a in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&) ()
#12 0x00000000004e7625 in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) ()
#13 0x00000000004e9367 in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long) ()
#14 0x00000000004e957e in epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long) ()
#15 0x0000000000505665 in void boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>::operator()<boost::system::error_code, unsigned long>(boost::system::error_code const&, unsigned long const&) ()
#16 0x0000000000505a93 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#17 0x0000000000506240 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) ()
#18 0x00000000006396a4 in boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1873] ()
#19 0x00000000004e4d5f in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
#20 0x00007fb472eeb5d5 in ?? () from /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.58.0
#21 0x00007fb471cb16ba in start_thread (arg=0x7fb45effd700) at pthread_create.c:333
#22 0x00007fb473aa882d in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109
(gdb) 

```

Refrence command used:
```
curl -X POST http://127.0.0.1:37458/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"transfer","params":{"destinations":[{"amount"300000000000000,"address":"422sqocg7bvjUtpxGX6EHWFAYZPAi5MJujKdSYinNvHNR3DkCDsz7uFWbwaVe4vUMveKAzAiA4j8xgUi29TpKXpm41kvtLD"}],"fee":150000000000,"mixin":3,"unlock_time":0,"get_tx_key":true}}' -H 'Content-Type: application/json'
```

Command to launch RPC wallet:
```
/usr/local/src/monero/build/release/bin/monero-wallet-rpc --wallet-file PoolWallet --rpc-bind-port 37458 --disable-rpc-login --log-level 4 --log-file /home/pooldaemon/wallet-rpc.log
```

## moneromooo-monero | 2017-02-03T21:09:38+00:00
OK, that's libunwind and/or GCC being a *censored*.
I'll revive my replace-libunwind-with-easylogging patch I guess.

## moneromooo-monero | 2017-02-03T21:10:16+00:00
F..... github trying to parse my text....


## Snipa22 | 2017-02-04T20:22:02+00:00
Fixed in #1671  Thank you @moneromooo-monero <3

# Action History
- Created by: Snipa22 | 2017-02-03T17:09:31+00:00
- Closed at: 2017-02-04T20:22:02+00:00
