---
title: Unable to Bind Port to Monero-Wallet-Cli
source_url: https://github.com/monero-project/monero/issues/1062
author: devinjdawson
assignees: []
labels:
- invalid
created_at: '2016-09-10T09:27:06+00:00'
updated_at: '2017-09-02T15:42:19+00:00'
type: issue
status: closed
closed_at: '2017-09-02T15:42:19+00:00'
---

# Original Description
`Monero-Wallet-Cli` log:

```
2016-Sep-10 04:51:22.487349 Loaded ok
2016-Sep-10 04:51:22.487833 Binding on localhost:13333
2016-Sep-10 04:51:22.487966 Starting wallet rpc server
2016-Sep-10 04:51:22.487988 Run net_service loop( 1 threads)...
2016-Sep-10 04:54:30.513439 [SRV_MAIN]net_service loop stopped.
2016-Sep-10 04:54:30.513493 [SRV_MAIN]Stopped wallet rpc server
2016-Sep-10 04:54:30.513512 [SRV_MAIN]Storing wallet...
2016-Sep-10 04:54:30.866664 [SRV_MAIN]Stored ok
```

I think the error lies in `Monerod`'s RPC code. libboost seems to not function properly under Ubuntu 16.04. This is from the `monerod.log`.

```
2016-Sep-10 04:54:04.734641 [RPC1]Exception: cryptonote::TX_DNE
2016-Sep-10 04:54:04.734681 [RPC1]Unwinded call stack:
2016-Sep-10 04:54:04.734928 [RPC1]     1                  0x5d6d88 __cxa_throw + 0x70
2016-Sep-10 04:54:04.735097 [RPC1]     2                  0x73a7b7 void (anonymous namespace)::throw1<cryptonote::TX_DNE>(cryptonote::TX_DNE const&) [clone .constprop.1484] + 0xd7
2016-Sep-10 04:54:04.735248 [RPC1]     3                  0x61833e cryptonote::BlockchainLMDB::get_tx(crypto::hash const&) const + 0x23e
2016-Sep-10 04:54:04.735411 [RPC1]     4                  0x6fdd07 bool cryptonote::Blockchain::get_transactions<std::vector<crypto::hash, std::allocator<crypto::hash> >, std::__cxx11::list<cryptonote::transaction, std::allocator<cryptonote::transaction> >, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > >(std::vector<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<cryptonote::transaction, std::allocator<cryptonote::transaction> >&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >&) const + 0x97
2016-Sep-10 04:54:04.735560 [RPC1]     5                  0x66a112 cryptonote::core_rpc_server::on_get_transactions(cryptonote::COMMAND_RPC_GET_TRANSACTIONS::request const&, cryptonote::COMMAND_RPC_GET_TRANSACTIONS::response&) + 0x1da
2016-Sep-10 04:54:04.735721 [RPC1]     6                  0x626b75 bool cryptonote::core_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&) [clone .constprop.612] + 0x2d25
2016-Sep-10 04:54:04.735898 [RPC1]     7                  0x5067fe cryptonote::core_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&) + 0x17e
2016-Sep-10 04:54:04.736055 [RPC1]     8                  0x71ba3d epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&) + 0x8d
2016-Sep-10 04:54:04.736205 [RPC1]     9                  0x523756 epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&) + 0x1f6
2016-Sep-10 04:54:04.736353 [RPC1]    10                  0x530f75 epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) + 0xcb5
2016-Sep-10 04:54:04.736501 [RPC1]    11                  0x5330c7 epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long) + 0x27
2016-Sep-10 04:54:04.736646 [RPC1]    12                  0x5343ef epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long) + 0xc0f
2016-Sep-10 04:54:04.736801 [RPC1]    13                  0x550856 boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0x1d6
2016-Sep-10 04:54:04.736957 [RPC1]    14                  0x5518d7 boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0x7d7
2016-Sep-10 04:54:04.737107 [RPC1]    15                  0x4a58f9 boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0x1e9
2016-Sep-10 04:54:04.737264 [RPC1]    16                  0x73a214 boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1104] + 0x43c
2016-Sep-10 04:54:04.737414 [RPC1]    17                  0x4cd6bf epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() + 0x14f
2016-Sep-10 04:54:04.737616 [RPC1]    18                  0x7f5481bed5d5 boost::this_thread::interruption_point() + 0x145
2016-Sep-10 04:54:04.737831 [RPC1]    19                  0x7f5482f936fa start_thread + 0xca
2016-Sep-10 04:54:04.738040 [RPC1]    20                  0x7f5482cc2b5d clone + 0x6d
2016-Sep-10 04:54:04.738227 [RPC1]    21                  0x0
2016-Sep-10 04:54:25.014608 [RPC1]Exception: cryptonote::TX_DNE
2016-Sep-10 04:54:25.014642 [RPC1]Unwinded call stack:
2016-Sep-10 04:54:25.014891 [RPC1]     1                  0x5d6d88 __cxa_throw + 0x70
2016-Sep-10 04:54:25.015059 [RPC1]     2                  0x73a7b7 void (anonymous namespace)::throw1<cryptonote::TX_DNE>(cryptonote::TX_DNE const&) [clone .constprop.1484] + 0xd7
2016-Sep-10 04:54:25.015207 [RPC1]     3                  0x61833e cryptonote::BlockchainLMDB::get_tx(crypto::hash const&) const + 0x23e
2016-Sep-10 04:54:25.015370 [RPC1]     4                  0x6fdd07 bool cryptonote::Blockchain::get_transactions<std::vector<crypto::hash, std::allocator<crypto::hash> >, std::__cxx11::list<cryptonote::transaction, std::allocator<cryptonote::transaction> >, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > >(std::vector<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<cryptonote::transaction, std::allocator<cryptonote::transaction> >&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >&) const + 0x97
2016-Sep-10 04:54:25.015518 [RPC1]     5                  0x66a112 cryptonote::core_rpc_server::on_get_transactions(cryptonote::COMMAND_RPC_GET_TRANSACTIONS::request const&, cryptonote::COMMAND_RPC_GET_TRANSACTIONS::response&) + 0x1da
2016-Sep-10 04:54:25.015679 [RPC1]     6                  0x626b75 bool cryptonote::core_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&) [clone .constprop.612] + 0x2d25
2016-Sep-10 04:54:25.015848 [RPC1]     7                  0x5067fe cryptonote::core_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&) + 0x17e
2016-Sep-10 04:54:25.016004 [RPC1]     8                  0x71ba3d epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&) + 0x8d
2016-Sep-10 04:54:25.016153 [RPC1]     9                  0x523756 epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&) + 0x1f6
2016-Sep-10 04:54:25.016304 [RPC1]    10                  0x530f75 epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) + 0xcb5
2016-Sep-10 04:54:25.016451 [RPC1]    11                  0x5330c7 epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long) + 0x27
2016-Sep-10 04:54:25.016595 [RPC1]    12                  0x5343ef epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long) + 0xc0f
2016-Sep-10 04:54:25.016757 [RPC1]    13                  0x550856 boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0x1d6
2016-Sep-10 04:54:25.016914 [RPC1]    14                  0x5518d7 boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0x7d7
2016-Sep-10 04:54:25.017096 [RPC1]    15                  0x4a58f9 boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0x1e9
2016-Sep-10 04:54:25.017262 [RPC1]    16                  0x73a214 boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1104] + 0x43c
```

Don't hack me bro <3


# Discussion History
## moneromooo-monero | 2016-09-17T15:27:13+00:00
That shows the RPC server bound properly and got a request.
I'm not sure whether that exception is a red herring or not, since it used to throw an exception for not finding a tx hash, when this is sometimes expected.
Can you re-run with "--log-level 2" to see if there's anything else of interest ?


## moneromooo-monero | 2017-09-02T15:38:06+00:00
No reply, and binding port seems to have worked just fine.

+invalid

# Action History
- Created by: devinjdawson | 2016-09-10T09:27:06+00:00
- Closed at: 2017-09-02T15:42:19+00:00
