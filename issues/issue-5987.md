---
title: cryptonote_protocol_handler.inl build issues
source_url: https://github.com/monero-project/monero/issues/5987
author: moneroexamples
assignees: []
labels: []
created_at: '2019-10-15T12:30:03+00:00'
updated_at: '2019-10-15T22:14:48+00:00'
type: issue
status: closed
closed_at: '2019-10-15T22:14:48+00:00'
---

# Original Description
arch liunx, gcc 9.2
latest monero master

```
n file included from /home/mwo2/monero/tests/unit_tests/node_server.cpp:36:
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘int cryptonote::t_cryptonote_protocol_handler<t_core>::handle_notify_new_block(int, cryptonote::NOTIFY_NEW_BLOCK::request&, cryptonote::cryptonote_connection_context&) [with t_core = test_core; cryptonote::NOTIFY_NEW_BLOCK::request = epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t>]’:
/home/mwo2/monero/tests/unit_tests/node_server.cpp:299:39:   required from here
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:457:7: error: cannot convert ‘cryptonote::tx_blob_entry’ to ‘const blobdata&’ {aka ‘const std::__cxx11::basic_string<char>&’}
  457 |       m_core.handle_incoming_tx(*tx_blob_it, tvc, true, true, false);
      |       ^~~~~~
/home/mwo2/monero/tests/unit_tests/node_server.cpp:59:55: note:   initializing argument 1 of ‘bool test_core::handle_incoming_tx(const blobdata&, cryptonote::tx_verification_context&, bool, bool, bool)’
   59 |   bool handle_incoming_tx(const cryptonote::blobdata& tx_blob, cryptonote::tx_verification_context& tvc, bool keeped_by_block, bool relayed, bool do_not_relay) { return true; }
      |                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
In file included from /home/mwo2/monero/tests/unit_tests/node_server.cpp:36:
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘int cryptonote::t_cryptonote_protocol_handler<t_core>::handle_notify_new_transactions(int, cryptonote::NOTIFY_NEW_TRANSACTIONS::request&, cryptonote::cryptonote_connection_context&) [with t_core = test_core; cryptonote::NOTIFY_NEW_TRANSACTIONS::request = epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_TRANSACTIONS::request_t>]’:
/home/mwo2/monero/tests/unit_tests/node_server.cpp:299:39:   required from here
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:912:7: error: cannot convert ‘<brace-enclosed initializer list>’ to ‘const blobdata&’ {aka ‘const std::__cxx11::basic_string<char>&’}
  912 |       m_core.handle_incoming_tx({arg.txs[i], crypto::null_hash}, tvc, false, true, false);
      |       ^~~~~~
/home/mwo2/monero/tests/unit_tests/node_server.cpp:59:55: note:   initializing argument 1 of ‘bool test_core::handle_incoming_tx(const blobdata&, cryptonote::tx_verification_context&, bool, bool, bool)’
   59 |   bool handle_incoming_tx(const cryptonote::blobdata& tx_blob, cryptonote::tx_verification_context& tvc, bool keeped_by_block, bool relayed, bool do_not_relay) { return true; }
      |                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
In file included from /home/mwo2/monero/tests/unit_tests/node_server.cpp:36:
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘int cryptonote::t_cryptonote_protocol_handler<t_core>::handle_request_chain(int, cryptonote::NOTIFY_REQUEST_CHAIN::request&, cryptonote::cryptonote_connection_context&) [with t_core = test_core; cryptonote::NOTIFY_REQUEST_CHAIN::request = epee::misc_utils::struct_init<cryptonote::NOTIFY_REQUEST_CHAIN::request_t>]’:
/home/mwo2/monero/tests/unit_tests/node_server.cpp:299:39:   required from here
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:1606:8: error: no matching function for call to ‘test_core::find_blockchain_supplement(std::__cxx11::list<crypto::hash>&, bool, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&)’
 1606 |     if(!m_core.find_blockchain_supplement(arg.block_ids, !arg.prune, r))
/home/mwo2/monero/tests/unit_tests/node_server.cpp:65:8: note: candidate: ‘bool test_core::find_blockchain_supplement(const std::__cxx11::list<crypto::hash>&, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&)’
   65 |   bool find_blockchain_supplement(const std::list<crypto::hash>& qblock_ids, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request& resp){return true;}
      |        ^~~~~~~~~~~~~~~~~~~~~~~~~~
/home/mwo2/monero/tests/unit_tests/node_server.cpp:65:8: note:   candidate expects 2 arguments, 3 provided
In file included from /home/mwo2/monero/tests/unit_tests/node_server.cpp:36:
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘int cryptonote::t_cryptonote_protocol_handler<t_core>::handle_response_chain_entry(int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&) [with t_core = test_core; cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request = epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request_t>]’:
/home/mwo2/monero/tests/unit_tests/node_server.cpp:299:39:   required from here
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:2267:14: error: no matching function for call to ‘test_core::prevalidate_block_hashes(uint64_t&, std::vector<crypto::hash>&, std::vector<long unsigned int>&)’
 2267 |     uint64_t n_use_blocks = m_core.prevalidate_block_hashes(arg.start_height, arg.m_block_ids, arg.m_block_weights);
      |              ^~~~~~~~~~~~
/home/mwo2/monero/tests/unit_tests/node_server.cpp:87:12: note: candidate: ‘uint64_t test_core::prevalidate_block_hashes(uint64_t, const std::vector<crypto::hash>&)’
   87 |   uint64_t prevalidate_block_hashes(uint64_t height, const std::vector<crypto::hash> &hashes) { return 0; }
      |            ^~~~~~~~~~~~~~~~~~~~~~~~
/home/mwo2/monero/tests/unit_tests/node_server.cpp:87:12: note:   candidate expects 2 arguments, 3 provided
In file included from /home/mwo2/monero/tests/unit_tests/node_server.cpp:36:
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘int cryptonote::t_cryptonote_protocol_handler<t_core>::handle_notify_new_fluffy_block(int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&) [with t_core = test_core; cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request = epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request_t>]’:
/home/mwo2/monero/tests/unit_tests/node_server.cpp:299:39:   required from here
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:621:16: error: cannot convert ‘cryptonote::tx_blob_entry’ to ‘const blobdata&’ {aka ‘const std::__cxx11::basic_string<char>&’}
  621 |             if(!m_core.handle_incoming_tx(tx_blob, tvc, true, true, false) || tvc.m_verifivation_failed)
/home/mwo2/monero/tests/unit_tests/node_server.cpp:59:55: note:   initializing argument 1 of ‘bool test_core::handle_incoming_tx(const blobdata&, cryptonote::tx_verification_context&, bool, bool, bool)’
   59 |   bool handle_incoming_tx(const cryptonote::blobdata& tx_blob, cryptonote::tx_verification_context& tvc, bool keeped_by_block, bool relayed, bool do_not_relay) { return true; }
      |                           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
In file included from /home/mwo2/monero/tests/unit_tests/node_server.cpp:36:
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘bool cryptonote::t_cryptonote_protocol_handler<t_core>::on_connection_synchronized() [with t_core = test_core]’:
/home/mwo2/monero/tests/unit_tests/node_server.cpp:299:39:   required from here
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:2178:16: error: ‘class test_core’ has no member named ‘is_within_compiled_block_hash_area’
 2178 |     if(!m_core.is_within_compiled_block_hash_area(m_core.get_current_blockchain_height()) && m_synchronized.compare_exchange_strong(val_expected, true))
      |         ~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘bool cryptonote::t_cryptonote_protocol_handler<t_core>::should_ask_for_pruned_data(cryptonote::cryptonote_connection_context&, uint64_t, uint64_t, bool) const [with t_core = test_core; uint64_t = long unsigned int]’:
/home/mwo2/monero/tests/unit_tests/node_server.cpp:299:39:   required from here
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:1790:17: error: ‘class test_core’ has no member named ‘is_within_compiled_block_hash_area’
 1790 |     if (!m_core.is_within_compiled_block_hash_area(first_block_height + nblocks - 1))
      |          ~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:1800:40: error: ‘class test_core’ has no member named ‘has_block_weights’
 1800 |     if (check_block_weights && !m_core.has_block_weights(first_block_height, nblocks))
      |                                 ~~~~~~~^~~~~~~~~~~~~~~~~
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘int cryptonote::t_cryptonote_protocol_handler<t_core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) [with t_core = test_core]’:
/home/mwo2/monero/tests/unit_tests/node_server.cpp:299:39:   required from here
/home/mwo2/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:1318:52: error: cannot convert ‘const std::vector<cryptonote::tx_blob_entry>’ to ‘const std::vector<std::__cxx11::basic_string<char> >&’
 1318 |             m_core.handle_incoming_txs(block_entry.txs, tvc, true, true, false);
      |                                        ~~~~~~~~~~~~^~~
      |                                                    |
      |                                                    const std::vector<cryptonote::tx_blob_entry>
/home/mwo2/monero/tests/unit_tests/node_server.cpp:60:69: note:   initializing argument 1 of ‘bool test_core::handle_incoming_txs(const std::vector<std::__cxx11::basic_string<char> >&, std::vector<cryptonote::tx_verification_context>&, bool, bool, bool)’
   60 |   bool handle_incoming_txs(const std::vector<cryptonote::blobdata>& tx_blob, std::vector<cryptonote::tx_verification_context>& tvc, bool keeped_by_block, bool relayed, bool do_not_relay) { return true; }
      |                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
[ 94%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/notify.cpp.o
In file included from /usr/include/c++/9.2.0/functional:59,
                 from /usr/include/boost/config/no_tr1/functional.hpp:21,
                 from /usr/include/boost/function/detail/prologue.hpp:14,
                 from /usr/include/boost/function/function_template.hpp:13,
                 from /usr/include/boost/function/detail/maybe_include.hpp:22,
                 from /usr/include/boost/function/function1.hpp:11,
                 from /usr/include/boost/program_options/value_semantic.hpp:13,
                 from /usr/include/boost/program_options/options_description.hpp:13,
                 from /home/mwo2/monero/src/cryptonote_core/cryptonote_core.h:35,
                 from /home/mwo2/monero/tests/unit_tests/node_server.cpp:32:
/usr/include/c++/9.2.0/bits/std_function.h:669:7: error: ‘std::function<_Res(_ArgTypes ...)>::function(_Functor) [with _Functor = cryptonote::t_cryptonote_protocol_handler<t_core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) [with t_core = test_core]::<lambda(cryptonote::cryptonote_connection_context&, nodetool::peerid_type, uint32_t)>; <template-parameter-2-2> = void; <template-parameter-2-3> = void; _Res = bool; _ArgTypes = {cryptonote::cryptonote_connection_context&, long unsigned int, unsigned int}]’, declared using local type ‘cryptonote::t_cryptonote_protocol_handler<t_core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) [with t_core = test_core]::<lambda(cryptonote::cryptonote_connection_context&, nodetool::peerid_type, uint32_t)>’, is used but never defined [-fpermissive]
  669 |       function<_Res(_ArgTypes...)>::
      |       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/include/c++/9.2.0/bits/std_function.h:669:7: error: ‘std::function<_Res(_ArgTypes ...)>::function(_Functor) [with _Functor = cryptonote::t_cryptonote_protocol_handler<t_core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) [with t_core = test_core]::<lambda(cryptonote::cryptonote_connection_context&, nodetool::peerid_type, uint32_t)>; <template-parameter-2-2> = void; <template-parameter-2-3> = void; _Res = bool; _ArgTypes = {cryptonote::cryptonote_connection_context&, long unsigned int, unsigned int}]’, declared using local type ‘cryptonote::t_cryptonote_protocol_handler<t_core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) [with t_core = test_core]::<lambda(cryptonote::cryptonote_connection_context&, nodetool::peerid_type, uint32_t)>’, is used but never defined [-fpermissive]
/usr/include/c++/9.2.0/bits/std_function.h:669:7: error: ‘std::function<_Res(_ArgTypes ...)>::function(_Functor) [with _Functor = cryptonote::t_cryptonote_protocol_handler<t_core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) [with t_core = test_core]::<lambda(cryptonote::cryptonote_connection_context&, nodetool::peerid_type, uint32_t)>; <template-parameter-2-2> = void; <template-parameter-2-3> = void; _Res = bool; _ArgTypes = {cryptonote::cryptonote_connection_context&, long unsigned int, unsigned int}]’, declared using local type ‘cryptonote::t_cryptonote_protocol_handler<t_core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) [with t_core = test_core]::<lambda(cryptonote::cryptonote_connection_context&, nodetool::peerid_type, uint32_t)>’, is used but never defined [-fpermissive]
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:583: tests/unit_tests/CMakeFiles/unit_tests.dir/node_server.cpp.o] Error 1
make[3]: *** Waiting for unfinished jobs....
make[3]: Leaving directory '/home/mwo2/monero/build/Linux/master/release'
make[2]: *** [CMakeFiles/Makefile2:5011: tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/home/mwo2/monero/build/Linux/master/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/home/mwo2/monero/build/Linux/master/release'
make: *** [Makefile:103: release-all] Error 2
```
Thought that maybe https://github.com/monero-project/monero/pull/5984 solves this, but it does not. 




# Discussion History
## moneromooo-monero | 2019-10-15T13:19:10+00:00
https://github.com/monero-project/monero/pull/5988

## moneroexamples | 2019-10-15T22:14:48+00:00
Works. Thank you!

# Action History
- Created by: moneroexamples | 2019-10-15T12:30:03+00:00
- Closed at: 2019-10-15T22:14:48+00:00
