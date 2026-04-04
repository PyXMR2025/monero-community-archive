---
title: Known ring does not include the spent output
source_url: https://github.com/monero-project/monero/issues/3771
author: Atrides
assignees: []
labels: []
created_at: '2018-05-07T15:37:18+00:00'
updated_at: '2018-05-17T23:17:17+00:00'
type: issue
status: closed
closed_at: '2018-05-17T23:17:17+00:00'
---

# Original Description
I tried to send coins from the pool, but since some two days I get such error from wallet:
"Known ring does not include the spent output: 5598899"

I rescanned wallet-address from scratch. The daemon node is synced with other daemons, has the same height. Monero 12.0


```
2018-05-07 15:12:59.485 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:6019     !own_found. THROW EXCEPTION: error::wallet_internal_error
2018-05-07 15:12:59.485 [RPC0]  WARN    net.http        src/wallet/wallet_errors.h:794  /DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:6019:N5tools5error21wallet_internal_errorE: Known ring does not include the spent output: 5598899
2018-05-07 15:12:59.486 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: tools::error::wallet_internal_error
2018-05-07 15:12:59.486 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
2018-05-07 15:12:59.498 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [1] ./monero-wallet-rpc:__wrap___cxa_throw+0x10a [0x7f62d357225a]
2018-05-07 15:12:59.498 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [2] ./monero-wallet-rpc:void tools::error::throw_wallet_ex<tools::error::wallet_internal_error, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)+0x170 [0x7f62d3456320]
2018-05-07 15:12:59.498 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [3] ./monero-wallet-rpc:tools::wallet2::get_outs(std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long)+0x62d7 [0x7f62d33f5de7]
2018-05-07 15:12:59.498 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [4] ./monero-wallet-rpc:tools::wallet2::transfer_selected_rct(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, std::vector<unsigned long, std::allocator<unsigned long> > const&, unsigned long, std::vector<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > >, std::allocator<std::vector<std::tuple<unsigned long, crypto::public_key, rct::key>, std::allocator<std::tuple<unsigned long, crypto::public_key, rct::key> > > > >&, unsigned long, unsigned long, std::vector<unsigned char, std::allocator<unsigned char> > const&, cryptonote::transaction&, tools::wallet2::pending_tx&, bool)+0x2f6b [0x7f62d3424e3b]
2018-05-07 15:12:59.498 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [5] ./monero-wallet-rpc:tools::wallet2::create_transactions_2(std::vector<cryptonote::tx_destination_entry, std::allocator<cryptonote::tx_destination_entry> >, unsigned long, unsigned long, unsigned int, std::vector<unsigned char, std::allocator<unsigned char> > const&, unsigned int, std::set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int> >, bool)+0x3320 [0x7f62d342e750]
2018-05-07 15:12:59.498 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] ./monero-wallet-rpc:tools::wallet_rpc_server::on_transfer(tools::wallet_rpc::COMMAND_RPC_TRANSFER::request const&, tools

```

incoming_transfers available with this index:
```
spent    unlocked  ringct    global index                                                               tx id      addr index
    F    unlocked  RingCT         5598899  <d86031292154142f7c51c7b528a042c170fac6a7bd33a3e3cd5cdb9ae6410e27>               0


```

# Discussion History
## moneromooo-monero | 2018-05-07T16:47:11+00:00
Do you have https://github.com/monero-project/monero/pull/3615 in ?

## Atrides | 2018-05-07T16:53:13+00:00
No, used official 0.12.0. Because since this version "make" doesn't works anymore

## moneromooo-monero | 2018-05-07T17:23:02+00:00
Then confirm whenever you've tried it, it fixes earlier occurences of this. For make, check README.md.

## Atrides | 2018-05-07T17:32:12+00:00
I reported other bug [https://github.com/monero-project/monero/issues/3773](#3773 ) with make command

## Atrides | 2018-05-08T15:30:16+00:00
Checked with last master source v0.12.0.0-master-d19255b. 
After **rescan_bc** now shows:
```
Warning: Some input keys being spent are from blocks that are temporally very close, which can break the anonymity of ring signature. Make sure this is intentional!

Is this okay?  (Y/Yes/N/No): Y
Error: transaction <3c582d5e89b8f2a1a82ab253bd25fa6a1a7a533176fc336c105edc05be8dbe81> was rejected by daemon with status: Failed
Error: Reason: double spend

```
Daemon shows in console:

```
2018-05-08 15:25:45.133 [RPC1]  WARN    daemon.rpc      src/rpc/core_rpc_server.cpp:801 [on_send_raw_tx]: tx verification failed: double spend

```

And 200k logs with repeated strings:

```
2018-05-08 15:24:09.721     7f3e85160700        INFO    msgwriter       src/common/scoped_message_writer.h:102  Height: 1568360/1568360 (100.0%) on mainnet, not mining, net hash 463.30 MH/s, v7, up to date, 6(out)+3(in) connections, uptime 0d 0h 1m 2s
2018-05-08 15:25:39.744 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: cryptonote::BLOCK_DNE
2018-05-08 15:25:39.744 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
2018-05-08 15:25:39.759 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [1] ./monerod112a:__wrap___cxa_throw+0x10a [0x55f85a34daea]
2018-05-08 15:25:39.759 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [2] ./monerod112a+0x51f2c9 [0x55f85a2782c9]
2018-05-08 15:25:39.759 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [3] ./monerod112a:cryptonote::BlockchainLMDB::get_block_height(crypto::hash const&) const+0x437 [0x55f85a286367]
2018-05-08 15:25:39.759 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [4] ./monerod112a:cryptonote::BlockchainLMDB::get_block_blob[abi:cxx11](crypto::hash const&) const+0x144 [0x55f85a2790a4]
2018-05-08 15:25:39.759 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [5] ./monerod112a:bool cryptonote::Blockchain::get_blocks<std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > >(std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> > const&, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block>, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, cryptonote::block> > >&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >&) const+0x1f1 [0x55f85a2db6c1]
2018-05-08 15:25:39.759 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] ./monerod112a:cryptonote::Blockchain::handle_get_objects(cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&)+0x1de [0x55f85a2c29ae]
2018-05-08 15:25:39.759 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [7] ./monerod112a:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_request_get_objects(int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&)+0x18f [0x55f85a23db0f]
2018-05-08 15:25:39.759 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [8] ./monerod112a:int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_REQUEST_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&)+0x24f [0x55f85a0c95af]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [9] ./monerod112a:int cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context>(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, cryptonote::cryptonote_connection_context&, bool&)+0x2aa [0x55f85a0d8caa]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [10] ./monerod112a:int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&)+0xc2 [0x55f85a0d8f32]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [11] ./monerod112a:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)+0x50 [0x55f85a0d9300]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [12] ./monerod112a:epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long)+0x4ad [0x55f85a259d1d]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [13] ./monerod112a:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1f8 [0x55f85a270ef8]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [14] ./monerod112a:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&)+0x7a [0x55f85a23ac1a]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [15] ./monerod112a:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x188 [0x55f85a23b088]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [16] ./monerod112a:void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&)+0x226 [0x55f85a23b476]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [17] ./monerod112a:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x250 [0x55f85a23b750]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [18] ./monerod112a:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1f4 [0x55f85a057e44]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [19] ./monerod112a:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x854 [0x55f85a21eca4]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [20] ./monerod112a+0x9970dd [0x55f85a6f00dd]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7f3e88d3c6ba]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163      [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f3e88a7241d]
2018-05-08 15:25:39.760 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:163

```

## moneromooo-monero | 2018-05-08T17:55:14+00:00
You probably have a pending (unmined) tx in your txpool.

## Atrides | 2018-05-09T02:57:01+00:00
You are right, I found some pending transactions in txpool that already older then 4 days, some of them belongs to my wallet.

## Atrides | 2018-05-17T14:49:06+00:00
The problem still exist.
This transaction is already 12 days in mempool:

```
print_tx 40277f035540a63de2e7fe664fb60b2147b5513a902f6b15d16e3794ed234945
Found in pool

```


## moneromooo-monero | 2018-05-17T15:02:12+00:00
A transaction being in the pool has nothing to with the the ringdb.
Are you saying you still have the ringdb problem ("known tring doesnot include...") with the current release-0.12 fixes ?

## Atrides | 2018-05-17T15:25:17+00:00
It's the same problem (same ring-inputs), but transformed to 
```
[wallet 4xxxx]: sweep_all 8 XXXXXXXXXXXXXXXXXX
Wallet password: 
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): Y

Transaction 1/1:
Spending from address index 0
Sweeping XXXXXX for a total fee of XXXXXXX.  Is this okay?  (Y/Yes/N/No): Y

Error: transaction <c6dad4c7f40853ede950d6151951b58582777fb00c5e19ff0f568cb183fc776c> was rejected by daemon with status: Failed
Error: Reason: double spend
```
This old wallet not used already 10 days, last successful transaction was 12 days ago.
And 5 transactions still in mempool in all monero-daemons, although monero has limit 7 days to remove transactions from mempool.


## moneromooo-monero | 2018-05-17T18:26:34+00:00
What makes you think it's the same problem ? If logs, please post the relevant part.

## moneromooo-monero | 2018-05-17T18:28:25+00:00
And make a new bug for the tx lifetime bug.

# Action History
- Created by: Atrides | 2018-05-07T15:37:18+00:00
- Closed at: 2018-05-17T23:17:17+00:00
