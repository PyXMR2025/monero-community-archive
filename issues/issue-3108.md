---
title: Transaction was not constructed
source_url: https://github.com/monero-project/monero/issues/3108
author: oliverw
assignees: []
labels: []
created_at: '2018-01-12T12:02:01+00:00'
updated_at: '2018-01-12T13:35:21+00:00'
type: issue
status: closed
closed_at: '2018-01-12T13:35:21+00:00'
---

# Original Description
Our node runs into an error when attempting to create a transaction to multiple recipients (miner payout), even though the node has enough confirmed balance:

```
2018-01-12 11:43:21.069 [RPC0]  WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:233    Requested ring size 1 too low for hard fork 6, using 5
2018-01-12 11:43:21.112 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:4023     selected transfers:
2018-01-12 11:43:21.303 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.h:1022       amount=10.025345063792, real_output=3, real_output_in_tx_index=0, indexes: 2821794 3625665 4263621 4275952 4277036
2018-01-12 11:43:21.303 [RPC0]  ERROR   default src/cryptonote_core/cryptonote_tx_utils.cpp:188 Destinations have to have exactly one output to support encrypted payment ids
2018-01-12 11:43:21.303 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:4121     !r. THROW EXCEPTION: error::tx_not_constructed
2018-01-12 11:43:21.303 [RPC0]  WARN    net.http        src/wallet/wallet_errors.h:707  /DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:4121:N5tools5error18tx_not_constructedE: transaction was not constructed
Sources:
  source 0:
    amount: 10.025345063792
Destinations:
  0: 49fpniWnSQLFGC9EuTnaYNP8e1kxM4kDAWb8GzGxLJQxdaS94VCUtAMipvLPXfbDUeRrKQbK3dbBzVcBpT3baXHZGszcbyC 0.182500770708
  1: 4Ao2w7yY3TceF4uexxbnaVAacmEZtxXbD82nMS6XVvWbgVLLvqJkjBYTNFzcaph6mQENAqHNrHsrFTJbjk7D6SYxNYbE96W 0.109828222973
  2: 47e4GxMeK735SYo1PMs18R6Qag1QTz3jaHPcpAhYXyHaEov28YLxAk58MP84UjFyh63RqyHP1pDw6Ks5wSTbjYXGLwRkm8S 0.111406810921
  3: 428fxbeXbEvEFdZ2Yf7rHMJrFj9NNhyxL6fWeABJFASsXvqZU1Qvpbrb2wMGqMidr517cCgU6SEbbXGY8RtqR17BMrV9mgg 0.173521979374
  4: 475YVJbPHPedudkhrcNp1wDcLMTGYusGPF5fqE7XjnragVLPdqbCHBdZg3dF4dN9hXMjjvGbykS6a77dTAQvGrpiQqHp2eH 0.109211588330
  5: 42w79cwuAHzEixv4315BWuXWyD78FbfyPVzPCsfr9ZLBT4Q74WGaNoPUrGcmjZP7PgVknn6Xj5mEBde1X7xqLdNBJPw3Wj8 0.127029407733
  6: 46uWjHX79va3HfAz67yv8kGXDs97rme2rc3oUFMtVcdtSYzPFTeK4ZXL5jESEoWxvogUb7dvgmEaSTaqK3FfYNvs1GMFCs7 0.113283574466
  7: 46aqxGqZgs85xVrMRQondgMiacrfjU91PNXz7VtCe6m92mwgSdaFFEueictMMCJYiuSKRoM9ZcMAcFNRHcnEsuRpCk7oEpK 0.103865225171
  8: 494QkvFQz8NTX54GdHWkc9Jxoa1rJtfTm1s9bvfeoaerN7TK9617EKcfK3SmVwjHzWVZ1dVqJYyvLF4psAG1kopFMZk3uFF 0.115511125672
  9: 432nV1f1rFG8oitLKS7qBoJ5P3AJY6176E4sGWMVg7xpho18sYodLTpbd6cRRFs3XueGKHvsJRZZtXSQRGuC1Be76xpNqqe 0.145160180661
  10: 49ue3U661D3iUcm4p3xErAEEGxvPZmsMj21KAa5sMDGc2uhH1RrV4SD3tx6q7ukKpwTPxJtqwMLQ1S9eSm3ySDPkJbnBrYx 0.101798775739
  11: 46B4cycVcucAW5w5fXinzFYa4qpSdVgHeQDv6TkFnYHQZNdsJiDSehqKTnMYhH791WVk2zpnghjM25mS4wfkduYuSpdfm42 0.417586508541
  12: 44CAiHC7QvW8Vdo9iBzNXH9RPbf5o8ANMV2ZaSxUr47t2txKkMbHrnZR1F4zvuvnnC2jDAzhdCDm3hRcVPU25aUF2mmTjo2 0.138384206550
  13: 42LXacHmDrH69dEqUTi1GLZntDBgZ4MhDC27iGnMUYihY2qGvQRgxbA2MsXeCG14DK4gisrkjErf53Xs2s3wzSpjKFLkZDf 0.145640976193
  14: 42RJmGDJbvieFySMDukDbmcK6ygACDb8TCKcT6i6b8K2NQmrsYBokyGQsfDmL9PmpvXFhbFxFNoD77xXMTM9Dhz15wqxPvW 0.137261921110
unlock_time: 0
2018-01-12 11:43:21.303 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:120  Exception: tools::error::tx_not_constructed
2018-01-12 11:43:21.303 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:121  Unwound call stack:
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [1] monero-wallet-rpc:__wrap___cxa_throw+0x102 [0x87f762]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [2] monero-wallet-rpc:void tools::error::throw_wallet_ex<tools::error::tx_not_constructed, std::vector<cryptonote::tx_source_entry, std::allocator<cryptonote::tx_source_entry> >, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, bool>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, std::vector<cryptonote::tx_source_entry, std::allocator<cryptonote::tx_source_entry> > const&, std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> > const&, unsigned long const&, bool const&)+0x4c4 [0x7bb6a4]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [3] monero-wallet-rpc:tools::wallet2::transfer_selected_rct(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, std::__cxx11::list<unsigned long, std::allocator<unsigned long> >, unsigned long, std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, unsigned long, unsigned long, std::vector<unsigned char, std::allocator<unsigned char> > const&, cryptonote::transaction&, tools::wallet2::pending_tx&)+0x1aa8 [0x7891c8]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [4] monero-wallet-rpc:tools::wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::allocator<unsigned char> >, bool)+0x299d [0x78f97d]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [5] monero-wallet-rpc:tools::wallet_rpc_server::on_transfer_split(tools::wallet_rpc::COMMAND_RPC_TRANSFER_SPLIT::request const&, tools::wallet_rpc::COMMAND_RPC_TRANSFER_SPLIT::response&, epee::json_rpc::error&)+0x330 [0x6b3470]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [6] monero-wallet-rpc:bool tools::wallet_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x1562 [0x735972]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [7] monero-wallet-rpc:tools::wallet_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&)+0x15c [0x73f67c]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [8] monero-wallet-rpc:epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&)+0xa2 [0x722742]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [9] monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&)+0x22e [0x6f65ae]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [10] monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body()+0x152 [0x6f68e2]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [11] monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&)+0x1c0 [0x740940]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [12] monero-wallet-rpc:epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned long)+0x37 [0x740d67]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [13] monero-wallet-rpc:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x1ca [0x740f9a]
2018-01-12 11:43:21.310 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:159      [14] monero-wallet-rpc:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x71 [0x71c7c1]

```

Any recommendations?

# Discussion History
## stoffu | 2018-01-12T12:13:48+00:00
As the error log says:
```
2018-01-12 11:43:21.303 [RPC0]  ERROR   default src/cryptonote_core/cryptonote_tx_utils.cpp:188 Destinations have to have exactly one output to support encrypted payment ids
```

You tried to use an encrypted payment ID (either by having one integrated address among the destinations or by separately specifying a 16-char payment ID), which isn't allowed for multi-destination transfer.

## oliverw | 2018-01-12T12:21:38+00:00
@stoffu So that would mean that one of those addresses listed in the log dump is actually an integrated address or one missing its payment id?

## stoffu | 2018-01-12T13:03:50+00:00
Yes, it could be that one destination was an integrated address, whose address part gets displayed in the log.

Another possibility is that all the destinations are normal addresses, and a short 16-char pID was given separately.

## oliverw | 2018-01-12T13:35:21+00:00
Ok I've located the problem in our code. Closing this.

# Action History
- Created by: oliverw | 2018-01-12T12:02:01+00:00
- Closed at: 2018-01-12T13:35:21+00:00
