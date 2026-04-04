---
title: URGENT! Continuesly new chainforks with version v0.10.2.2
source_url: https://github.com/monero-project/monero/issues/1876
author: Atrides
assignees: []
labels: []
created_at: '2017-03-17T17:07:52+00:00'
updated_at: '2017-03-21T16:30:25+00:00'
type: issue
status: closed
closed_at: '2017-03-19T21:02:43+00:00'
---

# Original Description
On all my nodes where v0.10.2.1 installed I saw such issue already 3 times. Nodes with 0.10.1.1 works normally.

Problem: sometimes node (still connected) hangs on some block and mines always it. Then they got own chain If I restart the node, shows following issues. Restart doesn't help! Needs full redownload of blockchain, in my case I take just backup from day before.

```
2017-03-17 10:06:31.366 [P2P9]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-03-17 11:00:27.857 [RPC1]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:71   Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-03-17 11:00:27.857 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: cryptonote::DB_ERROR
2017-03-17 11:00:27.857 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod() [0x74c46f]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod:cryptonote::BlockchainLMDB::add_transaction_data(crypto::hash const&, cryptonote::transaction const&, crypto::hash const&)+0x433 [0x721793]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod:cryptonote::BlockchainDB::add_transaction(crypto::hash const&, cryptonote::transaction const&, crypto::hash const*)+0x144 [0x6af1c4]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [4] ./monerod:cryptonote::BlockchainDB::add_block(cryptonote::block const&, unsigned long const&, unsigned long const&, unsigned long const&, std::vector<cryptonote::transaction, std::allocator<cryptonote::transaction> > const&)+0x11e [0x6af89e]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [5] ./monerod:cryptonote::BlockchainLMDB::add_block(cryptonote::block const&, unsigned long const&, unsigned long const&, unsigned long const&, std::vector<cryptonote::transaction, std::allocator<cryptonote::transaction> > const&)+0x12f [0x6fe18f]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [6] ./monerod:cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&)+0x1b43 [0x664a33]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [7] ./monerod:cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&)+0x312 [0x6661c2]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [8] ./monerod:cryptonote::core::handle_block_found(cryptonote::block&)+0x5a [0x67b3aa]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [9] ./monerod:cryptonote::core_rpc_server::on_submitblock(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, cryptonote::COMMAND_RPC_SUBMITBLOCK::response&, epee::json_rpc::error&)+0x1c4 [0x696484]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [10] ./monerod() [0x5f03b1]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [11] ./monerod() [0x5b1c93]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [12] ./monerod() [0x63d5f2]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [13] ./monerod() [0x60d23a]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [14] ./monerod() [0x60ecd3]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [15] ./monerod() [0x610837]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [16] ./monerod:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x1ae [0x610a2e]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [17] ./monerod() [0x624135]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [18] ./monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x118 [0x625548]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [19] ./monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x4b4 [0x60c9b4]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [20] ./monerod() [0x752194]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [21] ./monerod:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x14f [0x5d354f]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [22] ./monerod() [0x8635b5]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [23] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fbebe6d96ba]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158      [24] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fbebe40f82d]
2017-03-17 11:00:27.861 [RPC1]  INFO    stacktrace      src/common/stack_trace.cpp:158
2017-03-17 11:00:27.861 [RPC1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3360 Error adding block with hash: <8ec46bd7c32da82db83ea5e61b876916127120db693ea1e1da68c32c8fcf40ec> to blockchain, what = Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-03-17 11:07:23.356 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <76a817598de7ed21b70e741f18bc4ba37e92640738839c1a2549c8972d99d21b> attempting to add transaction already in blockchain with id: <aeef13013a2e52f71b72b7ca4065db1f01749a49defbdecd323e7d823fa012bc>
2017-03-17 11:07:23.456 [P2P4]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [178.254.12.114:35440 INC] Block verification failed, dropping connection
2017-03-17 11:07:23.632 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <76a817598de7ed21b70e741f18bc4ba37e92640738839c1a2549c8972d99d21b> attempting to add transaction already in blockchain with id: <aeef13013a2e52f71b72b7ca4065db1f01749a49defbdecd323e7d823fa012bc>
2017-03-17 11:07:23.729 [P2P2]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [163.172.76.47:43360 INC] Block verification failed, dropping connection
2017-03-17 11:07:23.904 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <76a817598de7ed21b70e741f18bc4ba37e92640738839c1a2549c8972d99d21b> attempting to add transaction already in blockchain with id: <aeef13013a2e52f71b72b7ca4065db1f01749a49defbdecd323e7d823fa012bc>
2017-03-17 11:07:24.005 [P2P7]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [195.154.169.129:59052 INC] Block verification failed, dropping connection
2017-03-17 11:07:24.137 [P2P6]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <76a817598de7ed21b70e741f18bc4ba37e92640738839c1a2549c8972d99d21b> attempting to add transaction already in blockchain with id: <aeef13013a2e52f71b72b7ca4065db1f01749a49defbdecd323e7d823fa012bc>
2017-03-17 11:07:24.225 [P2P6]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [198.27.67.63:36162 INC] Block verification failed, dropping connection
2017-03-17 11:07:24.336 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <76a817598de7ed21b70e741f18bc4ba37e92640738839c1a2549c8972d99d21b> attempting to add transaction already in blockchain with id: <aeef13013a2e52f71b72b7ca4065db1f01749a49defbdecd323e7d823fa012bc>
2017-03-17 11:07:24.420 [P2P2]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:352     [5.9.78.35:37178 INC] Block verification failed, dropping connection
2017-03-17 11:07:24.569 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3224 Block with id: <76a817598de7ed21b70e741f18bc4ba37e92640738839c1a2549c8972d99d21b> attempting to add transaction already in blockchain with id: <aeef13013a2e52f71b72b7ca4065db1f01749a49defbdecd323e7d823fa012bc>
[SKIP]
```

Also I see in console followings. May be other nodes make the same and mine own chains.
```
[SKIP]
2017-03-17 17:12:26.254 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257043
id:     <d56b12388ae802411d235681c63e02d30414dbb34f80dcc20d5eaa01aef67883>
PoW:    <f96b422fb5886c1aeb720bb7a6261d610a489590f06d9acaeeead73a00000000>
difficulty:     6530702856
2017-03-17 17:12:26.279 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257044
id:     <cd939c1a64b7859c8d5196a2ac49d19a767f424c1cbe087ee1af7480616b7477>
PoW:    <b9e235455043680359c3098779c304f4cb5b164bd63b60b18ad75b6a00000000>
difficulty:     6542402137
2017-03-17 17:12:26.305 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257045
id:     <9407a980d8a9eeb1c05241b9b232f469d0c8149eff825f520a31bb9bd2ec7506>
PoW:    <97f529ab6efa4edd2e96595c87ca62e5ab0c245e78191fc960dbd45400000000>
difficulty:     6537388021
2017-03-17 17:12:26.330 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257046
id:     <3d079b6ff697b61ba77162a4a478ebabf3d4d7cf0d2658f62ec0713ad12dddec>
PoW:    <93b6f91867959a66f4b0f5170ae2e1894a70e99a453894d7e8fa997b00000000>
difficulty:     6535222949
2017-03-17 17:12:26.356 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257047
id:     <029a675105954afe1f8e4d611d90a732ce5d1c70234aaca72686bea13e65c2b9>
PoW:    <6158a7a83bc77b1f54a86ea380ed9dda2d193adc030f7c8a5d3da48c00000000>
difficulty:     6538632564
2017-03-17 17:12:26.381 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257048
id:     <7848524257c87440fb477f32b3ac975c1a3b067539da106977a8c9e11d79a807>
PoW:    <d785ead084e8ee27b4184cefce357ee5592b0172f8a2a3fff5579f0200000000>
difficulty:     6546121124
2017-03-17 17:12:26.405 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257049
id:     <51df2417ca47af2b1503b89a3330272f41f3a5ee4c5f1186558918641f22acf8>
PoW:    <e11babf1cb6e217a8476f2bd8166ff441ace27d18b2f8a0133c4f81e00000000>
difficulty:     6543332317
2017-03-17 17:12:26.429 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257050
id:     <f5c4396bb11b827afbc45435c62daa2ec0de31105d5f632ed8fed2b4fb2b3a78>
PoW:    <ce06162b6ba0381d6b147a0b61e8dcfc1838caf9dd42c0df17b0797a00000000>
difficulty:     6553854522
2017-03-17 17:12:26.453 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257051
id:     <2620e2ea79fba2bb015933310f44c89f9624f21bae766380d6f9658073758b32>
PoW:    <f483b6450ec638d4ea06cadaaef4346fb260531f93621d9ef662130d00000000>
difficulty:     6539039710
2017-03-17 17:12:26.477 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257052
id:     <a4feccfc0960623d58c8cb2f5540d8f9041ba80eec35020fffb429d3d39f99f2>
PoW:    <84a8a117d780a20708f7e229a58b884cc13769ef14bb5f9be4d0c40e00000000>
difficulty:     6542683190
2017-03-17 17:12:26.502 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257053
id:     <bf6e9cfb800598ef33982d8a4159970e29eec135c1ccbd3f5481bdedce94fc2f>
PoW:    <a6c877da76207073ab70c72936476820d78706326713fcc8563e5d7b00000000>
difficulty:     6538112490
2017-03-17 17:12:26.523 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257054
id:     <3adc4d3de4cb885009490e9ee927316555ac6363a4189d8690a803b6a915a8a4>
PoW:    <fcb7ef373f907f5a4632bf3da4305eea856d3f1131e4fa9094631b5f00000000>
difficulty:     6537308152
2017-03-17 17:12:26.545 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257055
id:     <98cbc975e499d7b9d8112f89d0b6f34d4609f571f2cea06aad78da6ae2d9037d>
PoW:    <bd53465d1499d9d62e0ede8ce4c27f85527451029d9b4e6d03f9278500000000>
difficulty:     6546962379
2017-03-17 17:12:26.568 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257056
id:     <0482b07a688c52c00dcd89bfea07703666307963eed208700074abf903e39134>
PoW:    <915ab8bc87cf0f8f2e8d59ff0dbd766a5baf43c2b85797f9e8add62a00000000>
difficulty:     6551433800
2017-03-17 17:12:26.595 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1257057
id:     <295c8f3dd0f08c93bc400d07d688811515f53c0d716cfb9285175c53673f6a91>
PoW:    <6f9311ffab4dc60ff11255f5e5f6ece2fe452cf11a9549e7ea9dbf3300000000>
difficulty:     6547495084

```


# Discussion History
## Atrides | 2017-03-17T17:13:36+00:00
Additional info

```
2017-03-16 08:20:48.902 [P2P9]  INFO    global  src/cryptonote_core/blockchain.cpp:1409 ###### REORGANIZE on height: 1267367 of 1267367 with cum_difficulty 1764072489331929
 alternative blockchain size: 2 with cum_difficulty 1764080446593701
2017-03-16 08:20:49.583 [P2P9]  INFO    global  src/cryptonote_core/blockchain.cpp:1420 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1267367
id:     <c209106962ffcf53d20502d19ef8bf4c5945d6b9f2d2af45c9f345ffc3d3f9ed>
PoW:    <c08dcb4b8021f0106503243c5beaacf7beb7302354ec630d24ea734700000000>
difficulty:     7958637891
2017-03-16 08:20:49.583 [P2P9]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2423 WARNING: batch transaction mode already enabled, but asked to enable batch mode
2017-03-16 08:20:49.622 [P2P9]  INFO    global  src/cryptonote_core/blockchain.cpp:884  REORGANIZE SUCCESS! on height: 1267367, new blockchain size: 1267369
2017-03-16 08:20:49.622 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: cryptonote::DB_ERROR
2017-03-16 08:20:49.622 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod() [0x76374f]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod:cryptonote::BlockchainLMDB::batch_stop()+0x400 [0x7048a0]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod:cryptonote::Blockchain::cleanup_handle_incoming_blocks(bool)+0xec [0x65179c]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [4] ./monerod:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_block(int, cryptonote::NOTIFY_NEW_BLOCK::request&, cryptonote::cryptonote_connection_context&)+0x3e6 [0x637cb6]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [5] ./monerod() [0x7e257d]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [6] ./monerod() [0x6270d0]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [7] ./monerod() [0x607ba9]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [8] ./monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1ae [0x5d24ae]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [9] ./monerod() [0x624415]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [10] ./monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x118 [0x5ffc08]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [11] ./monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x4b4 [0x60cf44]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [12] ./monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1e9 [0x5926f9]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [13] ./monerod() [0x752194]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [14] ./monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x14f [0x5d3d2f]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [15] ./monerod() [0x8635b5]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [16] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7fbebe6d96ba]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158      [17] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fbebe40f82d]
2017-03-16 08:20:49.624 [P2P9]  INFO    stacktrace      src/common/stack_trace.cpp:158
2017-03-16 09:39:26.803 [P2P5]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-03-16 09:39:48.637 [P2P5]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-03-16 09:39:49.356 [P2P0]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-03-16 09:40:54.641 [P2P1]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
2017-03-16 09:44:38.671 [P2P7]  WARN    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler-base.cpp:125        RATE LIMIT NOT IMPLEMENTED HERE YET (download at unlimited speed?)
```

## anonimal | 2017-03-17T17:26:16+00:00
I was also getting **alot** of `attempting to add transaction already in blockchain with id` for days. Screen flooded with red.

Working solution for me: backup the data directory (`mv .bitmonero/ .bitmonero.bak/`) and start a fresh sync. Maybe there are less drastic measures; I'm curious to know what they are.

## moneromooo-monero | 2017-03-17T17:28:13+00:00
Fixed by 296641e047fa79d2651045f12f79738fd8668c46 (most likely). Let us know, in case there really is another bug there.

## vtnerd | 2017-03-17T19:20:09+00:00
> Working solution for me: backup the data directory (mv .bitmonero/ .bitmonero.bak/) and start a fresh sync. Maybe there are less drastic measures; I'm curious to know what they are.

Reverting back to 10.1 also works.

## anonimal | 2017-03-17T19:26:40+00:00
>Nodes with 0.10.1.1 works normally
>Maybe there are less drastic measures
>Reverting back to 10.1 also works.

Still too drastic for my taste! 😄 

## moneromooo-monero | 2017-03-17T19:36:20+00:00
Well, export and import (with verify off) also works. Easier on the network.

## Atrides | 2017-03-19T08:17:45+00:00
Updated to version from source (Mar 17, 2017), problem still not solved.

```

2017-03-18 20:40:50.505 [RPC0]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:71   Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-03-18 20:40:50.505 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: cryptonote::DB_ERROR
2017-03-18 20:40:50.505 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod() [0x74e87f]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod:cryptonote::BlockchainLMDB::add_transaction_data(crypto::hash const&, cryptonote::transaction const&, crypto::hash const&)+0x433 [0x70c283]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod:cryptonote::BlockchainDB::add_transaction(crypto::hash const&, cryptonote::transaction const&, crypto::hash const*)+0x144 [0x714924]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [4] ./monerod:cryptonote::BlockchainDB::add_block(cryptonote::block const&, unsigned long const&, unsigned long const&, unsigned long const&, std::vector<cryptonote::transaction, std::allocator<cryptonote::transaction> > const&)+0x11e [0x714ffe]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [5] ./monerod:cryptonote::BlockchainLMDB::add_block(cryptonote::block const&, unsigned long const&, unsigned long const&, unsigned long const&, std::vector<cryptonote::transaction, std::allocator<cryptonote::transaction> > const&)+0x12f [0x6d8fef]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [6] ./monerod:cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&)+0x1b43 [0x77d923]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [7] ./monerod:cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&)+0x312 [0x77f0b2]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [8] ./monerod:cryptonote::core::handle_block_found(cryptonote::block&)+0x5a [0x69440a]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [9] ./monerod:cryptonote::core_rpc_server::on_submitblock(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, cryptonote::COMMAND_RPC_SUBMITBLOCK::response&, epee::json_rpc::error&)+0x1c4 [0x679ba4]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [10] ./monerod() [0x5da707]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [11] ./monerod() [0x5b1dd3]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [12] ./monerod() [0x62b382]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [13] ./monerod() [0x60dcea]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [14] ./monerod() [0x60fe23]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [15] ./monerod() [0x611987]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [16] ./monerod:epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned long)+0x1ae [0x611b7e]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [17] ./monerod() [0x63ed85]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [18] ./monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x118 [0x640198]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [19] ./monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x4b4 [0x60d464]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [20] ./monerod() [0x7620f4]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [21] ./monerod:epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread()+0x14f [0x5f37ef]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [22] ./monerod() [0x86a2b5]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [23] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7f3eab18d6ba]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158      [24] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f3eaaec382d]
2017-03-18 20:40:50.508 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:158
2017-03-18 20:40:50.508 [RPC0]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3383 Error adding block with hash: <f5122ace8e7029fae35b4f14df286061dc1a7c20184286415dd1f00d9140f0de> to blockchain, what = Failed to add tx blob to db transaction: MDB_KEYEXIST: Key/data pair already exists
2017-03-18 20:41:27.982 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 20:41:28.231 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 20:41:28.265 [P2P9]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 20:41:28.880 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 20:41:28.972 [P2P0]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 20:41:29.175 [P2P6]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 20:41:29.211 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 20:41:29.801 [P2P1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 20:41:29.990 [P2P3]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>

```
[SKIP THE SAME]

```

2017-03-18 21:32:27.081 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 21:32:31.606 [P2P3]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 21:33:17.521 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:119  Exception: cryptonote::OUTPUT_DNE
2017-03-18 21:33:17.521 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:120  Unwound call stack:
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [1] ./monerod() [0x752f9f]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [2] ./monerod:cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, bool)+0xc6c [0x6dd9ac]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [3] ./monerod:cryptonote::Blockchain::check_tx_input(unsigned long, cryptonote::txin_to_key const&, crypto::hash const&, std::vector<crypto::signature, std::allocator<crypto::signature> > const&, rct::rctSig const&, std::vector<rct::ctkey, std::allocator<rct::ctkey> >&, unsigned long*)+0x407 [0x7763e7]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [4] ./monerod:cryptonote::Blockchain::check_tx_inputs(cryptonote::transaction&, cryptonote::tx_verification_context&, unsigned long*)+0xbd9 [0x666009]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [5] ./monerod:cryptonote::Blockchain::check_tx_inputs(cryptonote::transaction&, unsigned long&, crypto::hash&, cryptonote::tx_verification_context&, bool)+0x27e [0x669dee]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [6] ./monerod:cryptonote::tx_memory_pool::add_tx(cryptonote::transaction const&, crypto::hash const&, unsigned long, cryptonote::tx_verification_context&, bool, bool, bool, unsigned char)+0x753 [0x68fe63]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [7] ./monerod:cryptonote::core::add_new_tx(cryptonote::transaction const&, crypto::hash const&, crypto::hash const&, unsigned long, cryptonote::tx_verification_context&, bool, bool, bool)+0x24d [0x6916cd]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [8] ./monerod:cryptonote::core::handle_incoming_tx(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::tx_verification_context&, bool, bool, bool)+0xb97 [0x779e87]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [9] ./monerod:cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_transactions(int, cryptonote::NOTIFY_NEW_TRANSACTIONS::request&, cryptonote::cryptonote_connection_context&)+0x142 [0x618bd2]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [10] ./monerod() [0x7e936b]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [11] ./monerod() [0x6142e0]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [12] ./monerod() [0x608549]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [13] ./monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1ae [0x5f274e]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [14] ./monerod() [0x63f065]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [15] ./monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x118 [0x6009f8]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [16] ./monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x4b4 [0x60d9f4]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [17] ./monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1e9 [0x5921e9]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [18] ./monerod() [0x7620f4]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [19] ./monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x14f [0x5f3fcf]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [20] ./monerod() [0x86a2b5]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7f3eab18d6ba]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158      [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f3eaaec382d]
2017-03-18 21:33:17.524 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:158
2017-03-18 21:33:18.720 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 21:33:19.853 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 21:33:20.913 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 21:33:34.703 [P2P1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 21:34:19.417 [P2P3]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>


```

[SKIP THE SAME]

```

2017-03-18 22:47:24.136 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:47:52.399 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [82.238.80.97:52602 INC] Sync data returned a new top block candidate: 1269297 -> 1269351 [Your node is 54 blocks (0 days) behind] 
SYNCHRONIZATION started
2017-03-18 22:48:03.040 [P2P0]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:48:07.011 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:49:14.882 [P2P1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:49:15.500 [P2P9]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:49:23.207 [P2P8]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:49:25.379 [P2P9]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:49:38.048 [P2P3]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:49:50.369 [P2P5]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:50:02.649 [P2P6]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:50:25.610 [P2P7]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:50:52.914 [RPC1]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <5e50523d37204296be5e5cb0104f4c974e70a0f230cd41fa009df6999246df18> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>
2017-03-18 22:50:52.914 [RPC1]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:900     mined block failed verification
2017-03-18 22:51:06.874 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [85.194.238.2:18080 OUT] Sync data returned a new top block candidate: 1269297 -> 1269352 [Your node is 55 blocks (0 days) behind] 
SYNCHRONIZATION started
2017-03-18 22:51:08.606 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3247 Block with id: <903acc10453e46325a994eb5715658d1b4465453a394c9a529543877981c6483> attempting to add transaction already in blockchain with id: <5770cfd71b2217dabd492e7a088f81745fb3910e5eaf7f5524dfe1f253fa99b9>

```

## moneromooo-monero | 2017-03-19T09:47:42+00:00
Can you please include the output of:
mdb_stat -a ~/.bitmonero/lmdb/
on a bad db (and, just in case, also on the good backup db before you start again)


## moneromooo-monero | 2017-03-19T10:26:59+00:00
Patch ready.

Does this help ?
https://github.com/moneromooo-monero/bitmonero/tree/prep-block
(just the last patch)

## hyc | 2017-03-19T11:50:29+00:00
@Atrides Just installing the update doesn't fix your existing DB. You still must export and reimport (or simply delete and resync from network).

## moneromooo-monero | 2017-03-19T11:51:13+00:00
This patch isn't quite right wrt locking, there'll be a followup.

## Atrides | 2017-03-19T11:52:34+00:00
@hyc I just replace with DB saved day before issue

## moneromooo-monero | 2017-03-19T12:02:30+00:00
Actually, this patch is wrong.

## moneromooo-monero | 2017-03-19T12:28:07+00:00
New patch on the same branch. https://github.com/moneromooo-monero/bitmonero/tree/prep-block

## moneromooo-monero | 2017-03-19T12:43:22+00:00
Cleaned up and PR'd: https://github.com/monero-project/monero/pull/1896

Along with hyc's patch, it should hopefully fix it.

## Atrides | 2017-03-19T13:19:40+00:00
I compiled with both patches, will test it, thank you!

## moneromooo-monero | 2017-03-19T13:20:56+00:00
Make sure your starting db is ok ("mdb_stat -a ~/.bitmonero/lmdb" should show the last three tables (tx related) with the same number of entries).

## Atrides | 2017-03-19T13:35:30+00:00
mdb_stat shows nothing, hangs with 
`futex(0x7f0531e36008, FUTEX_WAIT_PRIVATE, 2, NULL) = -1 EAGAIN (Resource temporarily unavailable)
`
but in console status shows actually block and already mined one block


## moneromooo-monero | 2017-03-19T14:37:26+00:00
You'd have to either:
- run mdb_stat while monerod is not using the db
- recompile mdb_stat with recent changes to mutex placement in the lock file


## moneromooo-monero | 2017-03-19T17:56:00+00:00
Let us know when you've run enough that you think it's likely confirmed fixed, please.

## Atrides | 2017-03-19T20:09:20+00:00
7 hours from update, two blocks were not accepted:
```
2017-03-19 11:01:20.444 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1099    SYNCHRONIZED OK
2017-03-19 11:23:31.052 [RPC1]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:917     mined block failed verification
2017-03-19 12:14:54.051 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:293     [176.9.2.145:8180 OUT] Sync data returned a new top block candidate: 1269731 -> 1269732 [Your node is 1 blocks (0 days) behind] 
```

```
2017-03-19 14:08:48.660 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1099    SYNCHRONIZED OK
2017-03-19 15:14:50.598 [RPC1]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:897     Transaction not found in pool
2017-03-19 15:48:46.249 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1099    SYNCHRONIZED OK
```

Other ca. 40 blocks without problem.

But last time, between issues were more then 24 hours.


## moneromooo-monero | 2017-03-19T20:42:59+00:00
Great, thanks for confirming.

It's a bit odd that the first one doesn't have accompanying info. Log level 1 would shed some light.

The second one can happen if another block was just added which includes that tx. So your block is orphaned by not much time.


## moneromooo-monero | 2017-03-21T16:30:25+00:00
Atrides, more fixes are in master now (including a fix for lengthy RPC pauses when the txpool is large).

# Action History
- Created by: Atrides | 2017-03-17T17:07:52+00:00
- Closed at: 2017-03-19T21:02:43+00:00
