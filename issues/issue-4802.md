---
title: Phantom Transfers
source_url: https://github.com/monero-project/monero/issues/4802
author: oliverw
assignees: []
labels: []
created_at: '2018-11-05T10:07:39+00:00'
updated_at: '2018-11-06T11:45:09+00:00'
type: issue
status: closed
closed_at: '2018-11-06T11:45:09+00:00'
---

# Original Description
This morning I've sent 2.5 XMR to a wallet. Shortly after the entire amount transferred out of the wallet without showing any destinations (I did **not** issue a <code>rescan_bc</code>):

```
[wallet 42DBnE]: show_transfers
1698286     in       2018-11-05 08:05:08       2.500000000000 da88fdbb44c75c54531cf9030f97cfedf270437e64bb3df5b3b6f348632e01f2 0000000000000000 0 -
1698298    out       2018-11-05 08:26:14       2.499954660000 bb7e57667a2f3f7afb85947d08aedb52cda477fb1aa1f1efccf1562e47ec5617 0000000000000000 0.000045340000  0 -

[wallet 42DBnE]: show_transfer da88fdbb44c75c54531cf9030f97cfedf270437e64bb3df5b3b6f348632e01f2
Incoming transaction found
txid: <da88fdbb44c75c54531cf9030f97cfedf270437e64bb3df5b3b6f348632e01f2>
Height: 1698286
Timestamp: 2018-11-05 08:05:08
Amount: 2.500000000000
Payment ID: 0000000000000000
4 confirmations (1 suggested threshold)
Address index: 0
Note:

[wallet 42DBnE]: show_transfer bb7e57667a2f3f7afb85947d08aedb52cda477fb1aa1f1efccf1562e47ec5617
Outgoing transaction found
txid: <bb7e57667a2f3f7afb85947d08aedb52cda477fb1aa1f1efccf1562e47ec5617>
Height: 1698298
Timestamp: 2018-11-05 08:26:14
Amount: 2.499954660000
Payment ID: 0000000000000000
Change: 0.000000000000
Fee: 0.000045340000
Destinations:
Note:
```

First part of the monero-wallet-rpc - up until the incoming transfer was received. The exception in likely caused by the pool attempting to send a transfer over 1.922271205134 XMR to 28 addresses. Which obviously fails because there are not enough funds in the wallet.

```
2018-11-05 08:05:02.767 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <4b927c7bfbd98a95ed8e0e4a9b45b86c9a706d261edf6b5baf413cf4c7ed8829>
2018-11-05 08:05:02.767 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <48d149469d4c85b5e593334cc54a1d61c41bc865d12d70cb8d9816143432adc9>
2018-11-05 08:05:02.768 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2432     Already saw that one, it's for us
2018-11-05 08:05:02.839 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2788     Refresh done, blocks received: 0, balance (all accounts): 0.000000000000, unlocked: 0.000000000000
2018-11-05 08:05:23.039 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2432     Already saw that one, it's for us
2018-11-05 08:05:23.114 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2788     Refresh done, blocks received: 0, balance (all accounts): 0.000000000000, unlocked: 0.000000000000
2018-11-05 08:05:43.173 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1625     Received money: 2.500000000000, with tx: <da88fdbb44c75c54531cf9030f97cfedf270437e64bb3df5b3b6f348632e01f2>
2018-11-05 08:05:43.295 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2788     Refresh done, blocks received: 1, balance (all accounts): 2.500000000000, unlocked: 0.000000000000
2018-11-05 08:06:03.487 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2788     Refresh done, blocks received: 0, balance (all accounts): 2.500000000000, unlocked: 0.000000000000
2018-11-05 08:06:23.667 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <6df89de3a9db56c44fb7fea6132163709b07e43d460ac8359c23595888205d57>
2018-11-05 08:06:23.667 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <e9bc21be993f4b3ea01754f5e1cf687894d890466ce6d3b163eabd26484dfcd5>
2018-11-05 08:06:23.716 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2788     Refresh done, blocks received: 0, balance (all accounts): 2.500000000000, unlocked: 0.000000000000
2018-11-05 08:06:24.563 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:6216     Requested ring size 5 too low, using 11
2018-11-05 08:06:24.785 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6287     The last 10 blocks fill roughly 9% of the full reward zone.
2018-11-05 08:06:24.785 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6293     We'll use the low priority because probably it's safe to do so.
2018-11-05 08:06:24.785 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:8787     unlocked_balance(subaddr_account) == 0. THROW EXCEPTION: error::wallet_internal_error
2018-11-05 08:06:24.785 [RPC0]  WARN    net.http        src/wallet/wallet_errors.h:814  /DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:8787:N5tools5error21wallet_internal_errorE: No unlocked balance in the entire wallet
2018-11-05 08:06:24.785 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: tools::error::wallet_internal_error
2018-11-05 08:06:24.785 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2018-11-05 08:06:24.792 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] monero-wallet-rpc:__wrap___cxa_throw+0x10a [0x5644bbb06eda]
2018-11-05 08:06:24.793 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] monero-wallet-rpc:void tools::error::throw_wallet_ex<tools::error::wallet_internal_error, char [41]>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, char const (&) [41])+0x18e [0x5644bba0085e]
2018-11-05 08:06:24.793 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] monero-wallet-rpc:tools::wallet2::create_transactions_all(unsigned long, cryptonote::account_public_address const&, bool, unsigned long, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::allocator<unsigned char> > const&, unsigned int, std::set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int> >)+0x77a [0x5644bb9b7f9a]
2018-11-05 08:04:52.428 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] monero-wallet-rpc:tools::wallet_rpc_server::on_sweep_all(tools::wallet_rpc::COMMAND_RPC_SWEEP_ALL::request const&, tools::wallet_rpc::COMMAND_RPC_SWEEP_ALL::response&, epee::json_rpc::error&)+0x286 [0x5644bb823b06]
2018-11-05 08:04:52.428 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] monero-wallet-rpc:bool tools::wallet_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x7837 [0x5644bb90fdc7]
2018-11-05 08:04:52.428 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] monero-wallet-rpc:tools::wallet_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x179 [0x5644bb9239f9]
2018-11-05 08:04:52.428 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] monero-wallet-rpc:epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&)+0xaa [0x5644bb8f277a]
2018-11-05 08:04:52.428 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&)+0x13e [0x5644bb89216e]
2018-11-05 08:04:52.428 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body()+0x182 [0x5644bb892592]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&)+0x1a0 [0x5644bb925370]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long)+0x3b [0x5644bb925a2b]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] monero-wallet-rpc:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x228 [0x5644bb925cb8]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x7a [0x5644bb8d62ba]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] monero-wallet-rpc:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custext_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&)+0x1a0 [0x5644bb925370]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long)+0x3b [0x5644bb925a2b]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] monero-wallet-rpc:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x228 [0x5644bb925cb8]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x7a [0x5644bb8d62ba]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] monero-wallet-rpc:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1bd [0x5644bb8d675d]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x226 [0x5644bb8d6af6]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [16] monero-wallet-rpc:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x250 [0x5644bb8d6dd0]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [17] monero-wallet-rpc:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x8c4 [0x5644bb863a94]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [18] monero-wallet-rpc+0x7eeafd [0x5644bbb4cafd]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [19] /lib/x86_64-linux-gnu/libpthread.so.0+0x76db [0x7f4d727fe6db]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172      [20] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7f4d7252788f]
2018-11-05 08:04:52.441 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:172
2018-11-05 08:05:02.767 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <4b927c7bfbd98a95ed8e0e4a9b45b86c9a706d261edf6b5baf413cf4c7ed8829>
2018-11-05 08:05:02.767 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <48d149469d4c85b5e593334cc54a1d61c41bc865d12d70cb8d9816143432adc9>
```    

At this point the pool retries the payment:

```
2018-11-05 08:21:34.170 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2788     Refresh done, blocks received: 0, balance (all accounts): 2.500000000000, unlocked: 2.500000000000
2018-11-05 08:21:48.123 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:6216     Requested ring size 5 too low, using 11
2018-11-05 08:21:48.346 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6287     The last 10 blocks fill roughly 6% of the full reward zone.
2018-11-05 08:21:48.346 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6293     We'll use the low priority because probably it's safe to do so.
2018-11-05 08:21:48.349     7f4d691aa700        INFO    net.dns src/common/dns_utils.cpp:252    adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2018-11-05 08:21:48.349     7f4d691aa700        INFO    net.dns src/common/dns_utils.cpp:252    adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2018-11-05 08:21:48.420 [RPC0]  WARN    net.dns src/common/dns_utils.cpp:519    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-11-05 08:21:48.841 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6901     7769980 unlocked rct outputs
2018-11-05 08:21:48.841 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6926     Fake output makeup: 67 requested: 0 recent, 0 pre-fork, 0 post-fork, 67 full-chain
2018-11-05 08:21:48.841 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6987     Selecting real output: 7769946 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 6504008 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7478574 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7543701 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7566149 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7581592 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7582405 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7599058 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7603092 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7607877 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7612599 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7679507 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7682458 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7685447 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7688385 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7700563 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7702054 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7707242 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7709687 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7724814 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7729754 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7732180 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7734093 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7734594 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7736382 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7738615 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7738941 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7742434 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7746567 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7750094 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7750662 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7754209 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7754609 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7755037 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7755537 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7756361 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7756678 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7758408 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7758823 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7759508 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7759634 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7760489 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7761233 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7761327 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7761642 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7762335 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7762433 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7762495 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7762593 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7762920 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7763158 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7763428 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7764895 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7765019 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7766127 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7766563 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7767033 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7767083 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7767832 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7767851 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7768539 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7768638 for 0.000000000000
2018-11-05 08:21:48.845 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7768751 for 0.000000000000
2018-11-05 08:21:48.846 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7768861 for 0.000000000000
2018-11-05 08:21:48.846 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7769412 for 0.000000000000
2018-11-05 08:21:48.846 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7769439 for 0.000000000000
2018-11-05 08:21:48.846 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7769768 for 0.000000000000
2018-11-05 08:21:48.846 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7109     asking for output 7769946 for 0.000000000000
2018-11-05 08:21:48.915 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1847       amount=2.500000000000, real_output=10, real_output_in_tx_index=1, indexes: 7607877 7612599 7688385 7707242 7750662 7761327 7762433 7763428 7767083 7769439 7769946
2018-11-05 08:21:48.917 [RPC0]  INFO    perf    src/common/perf_timer.cpp:111   PERF             ----------
2018-11-05 08:21:48.917 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF      202    PROVE_v
2018-11-05 08:21:49.030 [RPC0]  INFO    bulletproofs    src/ringct/bulletproofs.cc:170  Hi/Gi cache size: 64 kB
2018-11-05 08:21:49.030 [RPC0]  INFO    bulletproofs    src/ringct/bulletproofs.cc:171  Hi_p3/Gi_p3 cache size: 320 kB
2018-11-05 08:21:49.030 [RPC0]  INFO    bulletproofs    src/ringct/bulletproofs.cc:172  Straus cache size: 300 kB
2018-11-05 08:21:49.030 [RPC0]  INFO    bulletproofs    src/ringct/bulletproofs.cc:173  Pippenger cache size: 320 kB
2018-11-05 08:21:49.030 [RPC0]  INFO    bulletproofs    src/ringct/bulletproofs.cc:175  Total cache size: 1004kB
2018-11-05 08:21:49.031 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF      679      PROVE_v
2018-11-05 08:21:49.031 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF       14      PROVE_aLaR
2018-11-05 08:21:49.043 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF    11921      PROVE_step1
2018-11-05 08:21:49.044 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF     1035      PROVE_step2
2018-11-05 08:21:49.064 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF    19741      PROVE_step3
2018-11-05 08:21:49.182 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF   118238      PROVE_step4
2018-11-05 08:21:49.188 [RPC0]  INFO    construct_tx    src/cryptonote_core/cryptonote_tx_utils.cpp:599 transaction_created: <1148f2b0cbc6313f1361d1b9cbd8c2cad0a3c3e1ecda72bff548bdf906e0ec7b>
{
  "version": 2,
  "unlock_time": 0,
  "vin": [ {
      "key": {
        "amount": 0,
        "key_offsets": [ 7607877, 4722, 75786, 18857, 43420, 10665, 1106, 995, 3655, 2356, 507
        ],
        "k_image": "a0a37c53d0d6d556d3a19e8682b83b7576453fd2a9743e1f2175627ebaa6ee4e"
      }
    }
  ],
  "vout": [ {
      "amount": 0,
      "target": {
        "key": "d15b8b962ccf0cc557694b54340bafb334f53f0e8849d93202dc923973428a6b"
      }
    }, {
      "amount": 0,
      "target": {
        "key": "984ebf136e03c11525b457f44404df4ca02db62e36c5c0617b20019f2a5233e3"
      }
    }
  ],
  "extra": [ 1, 254, 51, 186, 91, 82, 236, 186, 34, 133, 146, 134, 23, 112, 79, 114, 134, 32, 3, 124, 248, 133, 178, 87, 182, 115, 217, 219, 166, 201, 68, 69, 203
  ],
  "rct_signatures": {
    "type": 3,
    "txnFee": 39900000,
    "ecdhInfo": [ {
        "mask": "aac014c2e564c5e937a4c8e1218bbf8a549e25a9ebbe7132a9063e5bd159790c",
        "amount": "8eb7a854d435b52224880bffbd9ba048956b293a3606aa2a339d3b7d2160700c"
      }, {
        "mask": "05823ce90026cf024c5d55df9d052bbeb90db75d1cce1901fe2809551d54ef01",
        "amount": "f2d6405cb169b48a52677eb3d7ef10ae77973ba30efbad673e474b20f4ee1f0c"
      }],
    "outPk": [ "c535e203a3811ca726acf9865bf66a9b1e5b38dff39c3267216b556c30d75d96", "6ffbd5f05fd98ebce878242139a581252fa398988ba317250e5e60920339fa1e"]
  },
  "rctsig_prunable": {
    "nbp": 1,
    "bp": [ {
        "A": "42c859fddc9e84edf79b82b1f7c1ca200e437691c697dea5d2c6f82be1babbd7",
        "S": "01ab18cf3d51d54451e849cf858477aa4fccb2f0cf2e008aedc73001aa6f54a8",
        "T1": "85ccdb3106530bb9fbece7e8932d9fbc80aa91195b30ca96c267bc75a847252d",
        "T2": "5a3d2fb5c633a0ebc64d91084b6f3b8ee3958aa1c29b67327479b1a68c06f42b",
        "taux": "8e8cbb719f37e790089de3e60fdb2b53a59fa16c99ff0f75e3c7eccbc6807c05",
        "mu": "5233f45d7cc7c5352fece94e5d8aa2d480dada41683ea56972e5bd7299f94e08",
        "L": [ "5d8a73b3ce89694f61bd8ab44591539128718bc5d97509d22b8741c0e4d54e8e", "f0be8ea0390e4096d415209bf1bdb655100ab1018144b8a92b44868c9f9f923b", "3f8839e4f79914ebeb2d936cfa0e62b08078deeb539c80e81c6abb68aa6444d7", "ecdce780e14fba516042cb8c7e4402ee8e22d23d91188f868697a13b4dd8d598", "547f14e01d150ec2c2e3a6fb1243e09cc4d7e637495c4781ad7ce07c37c65f14", "0893704432d0533535e2ac106f12982fec76fc522297f40070c33689a7b1bb00", "0a41a8515dbbd5dcaa35b0d680566d982c7272043e9e836719437482f5925e6e"
        ],
        "R": [ "f3599b87c093813a9567d95f7477ddd585dc5e228934e0bc43558a0a2cef6e0d", "1b6d501cd5030d14cd6f9d036d9242d07ba612492402c8f1925cf9e6cbebc168", "af1a0b4ac4f7606f3b9124815d0f4355961bc6c241c9d4c492d9db2ab7381287", "5bffc6be2efc2d9a0edeb697c86783f6da349a3e41bed60b12a7ee4638b50498", "136e124cb55d26892e5e0c427f512e95b361845e4c9c03a3f51a543eb05965ad", "6b433569bfc2c01090e4ab1c6801c3795033c518aa43356f4f97dc6e0870815f", "cdb9f9502c671ab8a5c6e72cbc96802337290573d7fc0ee51497ec5b410c344b"
        ],
        "a": "2c13963637a3b839ee3352e0724003b94bf3e18f7e5d75cfcea0a43667530509",
        "b": "0367588955834375cffe6420aeb3b2a978e169da1577f66728836a4c1a78dc0e",
        "t": "264692e7a326a8d43c5d444e5b2add39f851c5fa1681f43c504bad77a91c2a0f"
      }
    ],
    "MGs": [ {
        "ss": [ [ "9ea5705e4e9d61a58065d6e12a2efff47f90ddcddb80bf2c8aeef623dc597a04", "4a43f84a09c8f11b096b5f54729fd7a4dfde8b4945824a21a2155b84ea160a09"], [ "a2d5aa2e96de58575593ffdcddc1ee60dbc123ea768023f1584fd9fb344ba107", "bc4304f8a0ddbfaa2139be9ab59619ff067dd2a504500c10ee2fc5da17b2290e"], [ "cbf8edd5e6e230f0e5053e4e20934abc84d05b1186bd7525cf29ca80a0d2530a", "fd4267b469ee42197c132fe261702666e0419bf17f285c5a074df9f894431e07"], [ "ab745c8491f91a2ceba93761e4529893a4b82f4bd51f62358cd0827961454709", "3f786638e46c8444db92077fdcd7bdd718996a10cc0f3205e5d78bc0b21c4706"], [ "ed217387d4f1c1f422373a295a2746d79943ea7d7cf525f9c7802cc8b0ed1300", "589682ae1c35ef869f7f6b4a419a19c37536117bd6eee80fbca1b8413d06db05"], [ "3b3731d2f7c431fb0602949c847a69bc799b97a469f6dbeeafd1e85ae25f130f", "a2f3c12398c311b1c9219f034b2416a916a47b72a624319b30143f540ef3750d"], [ "7ad416031d08faa0eaea545b800977d23d4ffdaa1f1f13a015023ae55558e50d", "efd5e15755bcf04999963ece1fe6312d0f8c60141fe7088bd1d10405bd495406"], [ "478041d536753fca1c15a128ac9d3355990bc90729545e7c89d86b4e9bdde30b", "9ea132f351bbf08827b040588cb7982c1696eed67e1e8a755cbaf2c17e12f707"], [ "caccff2c249831759dcc2fc8352a69442a8c13f0a78f71de0486cb043905fc04", "d0d727d81344cab60c3cd60921762b47de719687c326f0e9f94cd0a9729f2405"], [ "436aedf2e5844ea36ebdce51deb9e4764e85f5c8e9edabe9d188f4a2b010940f", "418d7446c9cf41797149fbe82795b0c85920605dd5ac4e2c03b045dd5bf4b208"], [ "02f22acd1397ab2a1a4b7f86c9826acb929ed94c7ed5067aa53ce7fa0f1e5707", "1c1ae2c70e07b11959ea9c42b7fa0f08f32932686736ed5da47c401b33d1c80a"]],
        "cc": "422cde9e9129159eb1298d55fbc75f1d05e58ba7802eb15d03cb84763757fa08"
      }],
    "pseudoOuts": [ "83095611beb86589f517a01c295d23086e5efbdd9de9c4a6f2f067245cf9db70"]
  }
}

2018-11-05 08:21:49.189 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1847       amount=2.500000000000, real_output=10, real_output_in_tx_index=1, indexes: 7607877 7612599 7688385 7707242 7750662 7761327 7762433 7763428 7767083 7769439 7769946
2018-11-05 08:21:49.190 [RPC0]  INFO    perf    src/common/perf_timer.cpp:111   PERF             ----------
2018-11-05 08:21:49.190 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF       32    PROVE_v
2018-11-05 08:21:49.190 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF      559      PROVE_v
2018-11-05 08:21:49.190 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF       10      PROVE_aLaR
2018-11-05 08:21:49.200 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF     9922      PROVE_step1
2018-11-05 08:21:49.201 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF      844      PROVE_step2
2018-11-05 08:21:49.220 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF    18590      PROVE_step3
2018-11-05 08:21:49.339 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF   119092      PROVE_step4
2018-11-05 08:21:49.345 [RPC0]  INFO    construct_tx    src/cryptonote_core/cryptonote_tx_utils.cpp:599 transaction_created: <00e7ccc0e8f899eee9d95f31ee6ffcbc9a367e82edfce5357ea3d3117c12e405>
{
  "version": 2,
  "unlock_time": 0,
  "vin": [ {
      "key": {
        "amount": 0,
        "key_offsets": [ 7607877, 4722, 75786, 18857, 43420, 10665, 1106, 995, 3655, 2356, 507
        ],
        "k_image": "a0a37c53d0d6d556d3a19e8682b83b7576453fd2a9743e1f2175627ebaa6ee4e"
      }
    }
  ],
  "vout": [ {
      "amount": 0,
      "target": {
        "key": "3bc2e8a4c1d0edb0d04ae291f80d6734c25d1a70121c37656107baeb609d6b66"
      }
    }, {
      "amount": 0,
      "target": {
        "key": "07c36b50c1e3659ec543bcd0acbd9f4225fb21afe2dca0f05f56f78be904a789"
      }
    }
  ],
  "extra": [ 1, 38, 82, 87, 222, 250, 89, 133, 49, 2, 64, 108, 179, 186, 119, 113, 9, 143, 113, 171, 57, 210, 57, 85, 236, 199, 173, 0, 211, 101, 144, 115, 219
  ],
  "rct_signatures": {
    "type": 3,
    "txnFee": 45340000,
    "ecdhInfo": [ {
        "mask": "b9d4e61cf94b80c753f16cd22854db123ed8d23ec610cd9d5c4bfff407be8d04",
        "amount": "9e51e5e51752c6a1f6bd1cd23b41a2fb403eafe9fa01375b5fdcf8187db8900b"
      }, {
        "mask": "3e2e3f77287e525bd565308cd48c9ddda72df84b9b439c9ee1e765a1b6cf4c0a",
        "amount": "418462e083e739231f6933ff25e8523a7ed9b3809112fe3b80a97d402107d50e"
      }],
    "outPk": [ "e02f0a735c25bbab355b48f3906a235ade10293fd1a861ed955ad6e0ade74610", "6b80be9d1b0142d446d506e3e72f923418b3cbbd8bb823b08fce185443925584"]
  },
  "rctsig_prunable": {
    "nbp": 1,
    "bp": [ {
        "A": "71e29822baee572177217c742e296f0bfadad81752e2ad950cbd4225a7667053",
        "S": "23f49bac0159bf10004f25ec7b996ce2100efb577a24ba03755468b7356f3e75",
        "T1": "576218bbf8075b2fe981f1e631e83ad4e46bcb531889c23d8fe046d4de50c291",
        "T2": "bebc82fa10d0c8f94652b856af928edb035e1b3ad7e8ee7471923576219481b9",
        "taux": "ac34e0d792887cf4972b3376663e38bc44f2dc5c42fbfa2184ec846ab1bd020e",
        "mu": "15fca8e580bd0b6b325389082812273b01f8813ee7dc29aabad2928f6b10c901",
        "L": [ "7acdf90722d6398d71cdeed0dd9e189fa5b1a16fd7d606135a783c960416ff81", "da9a5185f7b10ee31b3347396507309afb4c783fea13315bfe709c999141f9c4", "6d9ed42ca2e631eaf6a16c7eccefcaafb11099dac712ed702cc3ba042078b143", "64115b1a9eb58397153b6891df1016d2a86847c75ea54beca98982cc08cefb0a", "237c21f3e0ad14ee139df9b32abc2170fc388e34db1d75f91cc3473767a88b0e", "fa797e95caf3a432ea339300df5adfb3f3bfc8141f9894e50bfdf46bf6dc1830", "d0225d399ef6ee0657937fb52f5d261166cdc1a912843253ac080e743e26cb86"
        ],
        "R": [ "d7a6f052392120b7d9f37c393b564d5f5de608d8a268c0a57aa4593d56809ff9", "0b7e7759c76849f2ff53f137e130b02a5b1d4a01b2a41db62595c01724d22c08", "8677f06dc9d695aa8ef39a5fda4e7a375e60ff603ecf6079e9a30e8065e52f42", "bac755db78547112e156095fac5b8a3c9df10ad34d7728d03e2aecc3e9b5ef5f", "3cbf7ffaccbd1c1ecd71517a51f9d26cfd31c211d1b1a758b203e97ac8cb5427", "e7015e9d598f05844d5772f6b03baedb9adaab52cc3b0f98981c29a99e61d17b", "c9b60d84cdad7f0e81975226a015cc47e412e2ed7c740cef238708726a84ac30"
        ],
        "a": "d44d16d5cfbf781e9215883b9aeeb4e5f761ca7ef75fb90c350984eaee23b30e",
        "b": "930061491ea4ef8eaa3f38560ab812f1616b5d7af32caee80cc99bca94f44803",
        "t": "a28705990eaa3db4679467fb15e2d2ac14d88822fb44ead23827dbe6b5a47209"
      }
    ],
    "MGs": [ {
        "ss": [ [ "08a0629a0361b7152f79f517861c204f73cea2c5c3c92a7657555b00db818a08", "1ec6098dfbc868b660689b100ab7580d081af1d02666276e02a4783ed5c80503"], [ "9dbf0ebcec7202470d4c32fd02244ad697690554dd5eb7195a2b95d1860e5c05", "0bf261232e58229d43a477b17de560e7a5fe4521c6d695b0d641c10f142f2a08"], [ "d359be32d1dda946929b4bf6fd753a52c62bd7f541fc635d37edda4d4e8a8000", "851e35f11487d981ab98de350096ce6683cd5dc0c02e8f019c913c2a4fe99c0e"], [ "09ac8e83e77804da0a6067ef54ffe4e1d71f76ebd8fe3981546dc2c36ddafc03", "773e69ece1d63b67bf3091e4bc09482f1720b1ce15c60d6bdfdccc6252af290c"], [ "6c57af0303b831468c3a93b405ab5cca9741fda662ad2c7e1d571bfef7b39a05", "5a73a781e6d5151d72a5260ee2bebe8015e4bef649b4fb73490e68083bdfdc06"], [ "fc11c57cb4d8528c2f8087aa66bb4f04f7bc13487e7368c229c6959ac1464007", "df522477053018f0135a3019d51e0d8c6592c70005aba6aa8d092366c85fd705"], [ "d637a2ee1c6b978817c3c6731ae218b23eef1a950bb8e9bacfc191530a07ff02", "1d4de1e982fd7e20ca6fcade9ea916d5251b13b0544e84bae884bc966d6f2609"], [ "b1c1fee22429f9680867a175161751fa0c9d97a53d0dd5da3d8b46319bd4340d", "9215cf200e85b5f5a2766fa20a3b99472349582f54d203c511fdd3f60b10890b"], [ "879c8f28569dae45bb3b1d59c584b58dad6f631fb1f3ba0dff50ea16a246e205", "3b490e6534c6be8d580996d08278c016c7f1a5344837b431cf9928865776cc0c"], [ "18ffe5ea4054771858c8be3eaab9c98c275b8266a7e44ea53d780066b9b91204", "35dde94c6ffd7b536c35c1ec1d512da4d6c2eeb656599134dcfb0f6f2c6a3d00"], [ "c960859a20b8ee3cd48210123f34d37045daaec05a2b92562d20d0d737484e0f", "3c3ac30ffdf4532350b833a809ce9bfa8021637f7f7bf05ff2480c3d024f6301"]],
        "cc": "0e26643584503277fa4cf4978f5ce7decb769ead7c01b48a923db975f8bfed09"
      }],
    "pseudoOuts": [ "54afd178d3ad09e13497f79bcafd6c4d5d5af945f943a6060446f15c8981b8e0"]
  }
}

2018-11-05 08:21:49.345 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:9025     Done creating 1 transactions, 0.000045340000 total fee, 0.000000000000 total change
2018-11-05 08:21:49.345 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1847       amount=2.500000000000, real_output=10, real_output_in_tx_index=1, indexes: 7607877 7612599 7688385 7707242 7750662 7761327 7762433 7763428 7767083 7769439 7769946
2018-11-05 08:21:49.346 [RPC0]  INFO    perf    src/common/perf_timer.cpp:111   PERF             ----------
2018-11-05 08:21:49.346 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF       19    PROVE_v
2018-11-05 08:21:49.347 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF      575      PROVE_v
2018-11-05 08:21:49.347 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF       10      PROVE_aLaR
2018-11-05 08:21:49.357 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF     9895      PROVE_step1
2018-11-05 08:21:49.358 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF      828      PROVE_step2
2018-11-05 08:21:49.376 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF    18511      PROVE_step3
2018-11-05 08:21:49.492 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF   115981      PROVE_step4
2018-11-05 08:21:49.498 [RPC0]  INFO    construct_tx    src/cryptonote_core/cryptonote_tx_utils.cpp:599 transaction_created: <bb7e57667a2f3f7afb85947d08aedb52cda477fb1aa1f1efccf1562e47ec5617>
{
  "version": 2,
  "unlock_time": 0,
  "vin": [ {
      "key": {
        "amount": 0,
        "key_offsets": [ 7607877, 4722, 75786, 18857, 43420, 10665, 1106, 995, 3655, 2356, 507
        ],
        "k_image": "a0a37c53d0d6d556d3a19e8682b83b7576453fd2a9743e1f2175627ebaa6ee4e"
      }
    }
  ],
  "vout": [ {
      "amount": 0,
      "target": {
        "key": "2abe29db078c34245614fec542f15055e0054b2cd405b51f4ffa3c2ccd7751c9"
      }
    }, {
      "amount": 0,
      "target": {
        "key": "0b15b22afe4beae55d2f9b268f90163a41cafe920202326d505d93bb83f98ed8"
      }
    }
  ],
  "extra": [ 1, 175, 239, 163, 201, 137, 178, 31, 57, 36, 203, 248, 212, 170, 37, 157, 80, 200, 75, 5, 65, 29, 118, 242, 32, 53, 162, 174, 20, 123, 60, 30, 235
  ],
  "rct_signatures": {
    "type": 3,
    "txnFee": 45340000,
    "ecdhInfo": [ {
        "mask": "0166f2e23819102cd10743b0649d3e1d2a9fd2e1a1297af9cd0f9dbdf2de980c",
        "amount": "23db0ca8948916fc1dbda31fce5898803a8351f55782e0467eb676477ddc190f"
      }, {
        "mask": "2716e8fd01e1ee59bdba6ff1233312af3796d6a18583da87864fe457de840e04",
        "amount": "914e0cf1ef080285f7815979a4f6da5afef564da9fc4229b7c5d87e686540406"
      }],
    "outPk": [ "d0178bd5a6bdc3d0d3f49695f28c78ba4ccd67f3f040275c86e4456feb5d3694", "dc2444dc1d3dac0821c47d34372c334fa8395b82e75fd452223332ef92aa47c8"]
  },
  "rctsig_prunable": {
    "nbp": 1,
    "bp": [ {
        "A": "88c21a7dc1c00dba195d04137caeabb718cdb86bf1c216df45fbf1df12c55a13",
        "S": "4958e5b12ae49b5164a7b8d005edfd94544e3728af9845b27ad11442d42e496d",
        "T1": "ab8fda4581a8596146c267eb105365ab3c65527751abc9fc4b77a1bc7f4da7e9",
        "T2": "1015bdd199b66a5c5f2537c676c64e257bbb1b3804dcc834258d314a48c9e3e7",
        "taux": "964257e9b8aa73fe3466a43ca11946ffdd74ecda812aab34bb0463c281feab0c",
        "mu": "541cab5253dc35cf8f13839b0701c9dcd6b57f5d5e0433d2bd04b60a17c0c007",
        "L": [ "5c64cddb1f8a7917e46cdc64bd47453cbc5bbc16656f640abfd0fbd429b6f600", "8ffd53bea972f8eac3eecef105a1350b1ba5c0e8cf7e62aeaac7382bb5598af8", "a42082a9bee810c5089c7bed37186f52be135e229047325251c23d6cc04a3f9e", "d4cb1aeaebfbad389b14ff0d7cca6a3e07100ff4ae7a22feb1b2f85523de231d", "e92aa6484d4f838e858dfe4924ff1c8c7179888f09ebc3863cc06f5647bc67e4", "2d31e91f44b30e140e2bca80a8a08da3754d7d77c1cd749a270c71ecb709794a", "43aa7b007419923c82c513e33626b3b7329390eba4318bda76959448ca05cd2b"
        ],
        "R": [ "46d56b2144c5349a8cd7e9613d260fe735bf4890786f10dad662a91f88995d9d", "a1e99afe2f0a72fa15bd321a2b62fecd168f54bba7efde8ab8e31a3798760103", "86e4014ba7208835042aa3e0ef10ecd8f37cbcfca0b9325b186967636ef9b82c", "1ef1406e45fe402bea70a636e56c1a38337a6db584395d488ae3b610b481fd9a", "162f565cbd4cc6a715368071a9289866be647a94ea8e112ffaddfe5bb9a4eef5", "a12b3a06b922c2c8f3a1d3b2f1e51f661c530ad393d3de1b5d17ebecd1a12309", "eecda854dc8fd41426818dffeef5db1eb43e0617c3e3dd11d4be9602966a7b64"
        ],
        "a": "7ab91007040af6b34f5558543aa1cb3eab4ef7e43dd3e7e50e22e996f9d5e609",
        "b": "ed5b20bae27aa3a6044f5f44397675a45fc1c36dd099cbbc80459ba100d2df02",
        "t": "4e539b8743687264a8569a3a6784b0b41d45402dd6e9fbe2f542be52dbe51503"
      }
    ],
    "MGs": [ {
        "ss": [ [ "b50a477c36f29dc73416899cc4bba3d102f6191531e21febd122f219e929810e", "d7ee65535a8513a6a901a87c69d94d6c1d45343bcbeca93c227563b743b6b407"], [ "98d55919d1eb5dae81533737cd4e9f4f153143caaccb164c414a976fe62d2b09", "406cd740caffd348d261c0d135e45c58488651006354e7f0d9ba3472b9d90508"], [ "6d54ee3a07905b40f344eee6cad0bb30c414cb3d3340bbde61bf5da3d088c60c", "b01d67d717672b8af4b83dda1936a908088ca1046d4df6a2d0bb74339e15450f"], [ "9583289d8ff85221c6581845b4299cb80a00abb8298936d8ce8066d48345a00e", "5e1948a56e732b831dd761df2c2889f08cf71d8618ba360894fe371fb0af920b"], [ "d368d2f86396a91201abcdd0c4989e782b508138428604477f87bd0a800e1300", "90baeba77fe2fe9d9361ae6dff7f98137aca9dbccc99831fab614bf1283cf10c"], [ "8b8b753c6a54fbe87907b4e197917813c550ed0ef6fd117e79a523345be8db01", "efa1e05af6f32a984d7e785ed18eacbe962af000f84d385eaefe06c5f0360104"], [ "825538f9cd4c4954e97da84100292048e100d705a94066eb718d15e91eb2cb06", "392f78b0b5927249c641396034babdb7ce24f8138cb06213ece652502b897e0f"], [ "7645b303e2fb03a49feb7632ed60e562efc75cc7f48d0e64d0d9d65a74997b02", "730809d04666cc91d8fa8a8980dcc06fefc0502b02cd8f340df550bd599b200b"], [ "5400b6056e230b11c675c365f143d3c7463e6c10cb3e699cababc2076084ac07", "c17d416e4ea49543fdfba45c687718469a25f2cd0a1cd00b05777864a7f9660c"], [ "d2e7ce871d2386579bcf0fab442edbe9d3870efc33e5750fb48a7da3e0974b0c", "0459eb504528bc85d895b1f318149a13785902f7bddd18fbe0c4661753062900"], [ "ef50c4d27458c970ef862fb3898743be6777a4b7f8ebd8865a4a789fb4b81d06", "015f3033005c4b0cd4999804f865b84bdd257fe6b83e2114f07548a8d2705a0e"]],
        "cc": "25d71e6b554dd7eba2c9e18780866ae5931a93040100adfd442c3a13afb2b10c"
      }],
    "pseudoOuts": [ "3c65f020fc6c7cd96f1f375a7ca27a2c32790ba69d871cc6eae9c324b48c8ee1"]
  }
}

2018-11-05 08:21:49.498 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:9056       Transaction 1/1 <bb7e57667a2f3f7afb85947d08aedb52cda477fb1aa1f1efccf1562e47ec5617>: 1875 weight, sending 2.500000000000 in 1 outputs to 1 destination(s), including 0.000045340000 fee, 0.000000000000 change
2018-11-05 08:21:49.568 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5413     Transaction successfully sent. <<bb7e57667a2f3f7afb85947d08aedb52cda477fb1aa1f1efccf1562e47ec5617>>
Commission: 0.000045340000 (dust sent to dust addr: 0.000000000000)
Balance: 0.000000000000
Unlocked: 0.000000000000
Please, wait for confirmation for your balance to be unlocked.
2018-11-05 08:21:54.383 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <bb7e57667a2f3f7afb85947d08aedb52cda477fb1aa1f1efccf1562e47ec5617>
2018-11-05 08:21:54.383 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2427     We sent that one
2018-11-05 08:21:54.384 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <22467b94577370f00ea6d1667e62f71dcdc7a20080a5581d724a386a1ae4e14f>
2018-11-05 08:21:54.384 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <24baa355c1a8fe03ffed7d203431c137a1fa1c80a0cb22e15760938e8a72eaa3>
2018-11-05 08:21:54.384 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <14f2cad6928b42e8fecbdceb2f82251301b5b8f72674122fe3f783cdd84dc6b4>
2018-11-05 08:21:54.384 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2398     Found new pool tx: <7e21b389be85e20fca9f131e1930f7ffac7f2f83e983912b7307181e3c2893de>
2018-11-05 08:21:54.449 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2788     Refresh done, blocks received: 0, balance (all accounts): 0.000000000000, unlocked: 0.000000000000
```

Could anyone provide some insight what's going on here and where the transfer went?

# Discussion History
## moneromooo-monero | 2018-11-05T10:16:14+00:00
That log does not show where the tx is going. Your pool probably has logs of it.

## oliverw | 2018-11-05T10:18:14+00:00
@moneromooo-monero Yes it does. Is the monero-wallet-rpc *supposed* to show the destination addresses? Any why does show_transfer not display any destinations?

## moneromooo-monero | 2018-11-05T10:26:06+00:00
It displays those at the wallet.wallet2:DEBUG level.

About show_transfer, did you save monero-wallet-rpc, then load moneor-wallet-cli, or did you load monero-wallet-cli on the state before the transfer ?

## oliverw | 2018-11-05T10:40:08+00:00
I stopped the docker container running monero-wallet-rpc and ran monero-wallet-cli manually with the current directory being the datadir of monero-wallet-rpc.

A couple things that are especially confusing to me here is. Where is that transfer over the full wallet-amount being coming from. The pool is asking to transfer 1.922271205134, not 2.5. Any why is the log showing all those lines containing _asking for output xxxx for 0.000000000000_?

The server in question is not accessible from anywhere except from one trusted host, that's again several jump boxes away from the public internet.

## moneromooo-monero | 2018-11-05T11:02:29+00:00
I am not familiar with the details of docker. Did you load monero-wallet-cli on the state before the transfer ?

Are you claiming you did not make that tx ? Typically, monero will send more than what you ask, and get you the remainder as change. Are you sure this is not the case ?


## oliverw | 2018-11-05T11:11:25+00:00
Well, docker just sends a SIGTERM to monero-wallet-rpc when stopping the container. I'm not sure at which state that left the wallet.

Regarding your second question, I'm 100% sure that the pool did not request a transfer for 2.5 XMR but  1.922271205134 to 28 addresses issued through a <code>transfer</code> RPC. It did that repeatedly until is the RPC succeeded when the incoming transfer arrived. Is some of that information decipherable from the log?

## moneromooo-monero | 2018-11-05T11:17:38+00:00
That *should* have saved it then.
Did monero-wallet-cli print out the "Received..." line when you loaded it ?

## oliverw | 2018-11-05T11:51:11+00:00
```
2018-11-05 08:29:20,052 INFO  [default] Page size: 4096
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Beryllium Bullet' (v0.13.0.2-release)
Logging to /home/oliver/monero-v0.13.0.2/monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): wallet
Wallet and key files found, loading...
Wallet password:
Opened wallet: 42DBnE5RfiEDtHyY9S2pWHZ9Xz864ruVrC9nfscB9whRdn7mNDEaH7s5bys9nGDQy1hQa8rZDcujTfcbBVvy64Fr1nyfFGp
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Error: Failed to initialize ring database: privacy enhancing features will be inactive
Starting refresh...
Enter password (output received):
Height 1698286, txid <da88fdbb44c75c54531cf9030f97cfedf270437e64bb3df5b3b6f348632e01f2>, 2.500000000000, idx 0/0
Height 1698298, txid <bb7e57667a2f3f7afb85947d08aedb52cda477fb1aa1f1efccf1562e47ec5617>, spent 2.500000000000, idx 0/0
Refresh done, blocks received: 31
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0 42DBnE        0.000000000000        0.000000000000       Primary account
----------------------------------------------------------------------------------
          Total        0.000000000000        0.000000000000
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000
Background refresh thread started
```

## moneromooo-monero | 2018-11-05T11:58:54+00:00
You got the line, that means the tx wasn't received in a block by monero-wallet-rpc. That probably explains why the destination address(es) aren't available, if the cache wasn't saved.

That tx has two outputs, so it's not a multi recipient transfer like what you mentioned earlier. No change coming back to the sending wallet, so it's likely a sweep_all with a dummy 0 change. If you did not do a sweep_all, any chance you might have some malware, or that your keys could be known ?


## oliverw | 2018-11-05T12:24:18+00:00
I have to investigate.

## oliverw | 2018-11-05T13:27:46+00:00
@moneromooo-monero Just making sure I understood you correctly, you think the transaction was initiated locally and not received from the blockchain, right? 

Additionally, I presume there's nothing in the logs that would reveil the userid or remote address of the creator of the tx?

## moneromooo-monero | 2018-11-05T13:50:17+00:00
Since monero-wallet-cli printed that line:
Height 1698298, txid <bb7e57667a2f3f7afb85947d08aedb52cda477fb1aa1f1efccf1562e47ec5617>, spent 2.500000000000, idx 0/0
It means the wallet cache it loaded did not have that transaction recorded yet.
This means either:
- monero-wallet-rpc never saw a block that tx
- monero-wallet-rpc did see a block with that tx but did not save the wallet cache before monero-wallet-cli loaded it

The tx was definitely made locally, since:
2018-11-05 08:21:49.568 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5413     Transaction successfully sent. <<bb7e57667a2f3f7afb85947d08aedb52cda477fb1aa1f1efccf1562e47ec5617>>

So that means two possibilities:
- the wallet cache was not saved
- the wallet cache was saved, but before the tx got into a block

The tx was made at :21:49. It was mined at tx :26:14. You started monero-wallet-cli at :29:20. Maybe you stopped monero-wallet-rpc between :21:49 and :26:14, waited three minutes, then started monero-wallet-cli.

As I said above, destination addresses are logged at wallet.wallet2:DEBUG level, which you don't seem to have enabled.

## oliverw | 2018-11-05T13:57:59+00:00
@moneromooo-monero I was referring to IP Addresses in my previous comment. :)

## moneromooo-monero | 2018-11-05T14:04:49+00:00
If you think someone connected to your host to send that tx ? You'd have to look at the ssh logs, or if which IP the RPC call is from, I don't think that's logged, but presumably monero-wallet-rpc listens to 127.0.0.1 only, unless you changed that.

## oliverw | 2018-11-05T14:24:41+00:00
@moneromooo-monero That's not even possible since the server only accepts SSH connections from a single white-listed trusted host. The only possibility I see would be an insider at the hosting provider. I'm currently going through all logs, and trying to correlate the chain of events.

## oliverw | 2018-11-05T14:49:24+00:00
@moneromooo-monero 

> That tx has two outputs, so it's not a multi recipient transfer like what you mentioned earlier. 

Sifting through the logs I was unable to locate a single transaction to multiple recipients having more than two vouts. Are you 100% sure about that comment?

## moneromooo-monero | 2018-11-05T14:52:25+00:00
Not quite. It' possible that if you send a tx to two recipients, for X and Y monero respectively, and you have a fee F, and you have an output of value X+Y+F, then you'll get a multi recipient tx with only two outputs. Not super likely though.
It could be part of one though, but then it'd have to be huge enough to trigger the splitting code.

## oliverw | 2018-11-05T15:06:22+00:00
@moneromooo-monero That's strange because according to the logs all our historic payouts involved transfers to 20+x addresses with a total amount of 1-2 XMR. 100% of the generated transactions have just two vouts.

## moneromooo-monero | 2018-11-05T15:26:55+00:00
Maybe your software sends one at a time.

## oliverw | 2018-11-05T15:31:54+00:00
@moneromooo-monero Nope, it only does this for transfers to exchanges involing paymentids.

https://github.com/coinfoundry/miningcore/blob/dev/src/Miningcore/Blockchain/Cryptonote/CryptonotePayoutHandler.cs#L170

(I'm the author)

## moneromooo-monero | 2018-11-05T15:38:18+00:00
Then you gotta tell us how you do it, that's great for scalability ^_^
Alternatively, there's a bug somewhere and check the JSON you're actually sending.

## oliverw | 2018-11-05T15:43:01+00:00
We're both referring to this when talking about outputs, right?

```
  "vout": [ {
      "amount": 0,
      "target": {
        "key": "3a16dcc20b44cc4583fab60315943a330a5bb1dc80209e9b74d808a207e9b7c4"
      }
    }, {
      "amount": 0,
      "target": {
        "key": "9c226c649c2bd20144d792c8766cd9c79e31cc22aca377e722b3ee635e4ad7f3"
      }
    }
  ],

```

## moneromooo-monero | 2018-11-05T15:48:48+00:00
Yes.

# Action History
- Created by: oliverw | 2018-11-05T10:07:39+00:00
- Closed at: 2018-11-06T11:45:09+00:00
