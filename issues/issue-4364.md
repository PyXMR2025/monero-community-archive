---
title: 'build error on ubuntu 14 -" undefined reference to `boost" '
source_url: https://github.com/monero-project/monero/issues/4364
author: jackieWhn
assignees: []
labels:
- invalid
created_at: '2018-09-12T10:21:13+00:00'
updated_at: '2019-06-15T17:33:36+00:00'
type: issue
status: closed
closed_at: '2019-06-15T17:33:27+00:00'
---

# Original Description
Errors:
```
[ 29%] Linking CXX static library libdevice.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 29%] Built target device
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_ringct
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 29%] Building CXX object src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 29%] Built target obj_ringct
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_checkpoints
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 29%] Building CXX object src/checkpoints/CMakeFiles/obj_checkpoints.dir/checkpoints.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 29%] Built target obj_checkpoints
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target checkpoints
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 29%] Linking CXX static library libcheckpoints.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 29%] Built target checkpoints
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_cryptonote_basic
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 30%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/account.cpp.o
[ 30%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_basic_impl.cpp.o
[ 30%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/cryptonote_format_utils.cpp.o
[ 31%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/difficulty.cpp.o
[ 31%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/hardfork.cpp.o
[ 31%] Building CXX object src/cryptonote_basic/CMakeFiles/obj_cryptonote_basic.dir/miner.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 31%] Built target obj_cryptonote_basic
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target cryptonote_basic
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 31%] Linking CXX static library libcryptonote_basic.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 31%] Built target cryptonote_basic
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target ringct
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 32%] Linking CXX static library libringct.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 32%] Built target ringct
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_cryptonote_core
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 34%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/blockchain.cpp.o
[ 34%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_core.cpp.o
[ 34%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/tx_pool.cpp.o
[ 35%] Building CXX object src/cryptonote_core/CMakeFiles/obj_cryptonote_core.dir/cryptonote_tx_utils.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 35%] Built target obj_cryptonote_core
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_multisig
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 36%] Building CXX object src/multisig/CMakeFiles/obj_multisig.dir/multisig.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 36%] Built target obj_multisig
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target multisig
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 36%] Linking CXX static library libmultisig.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 36%] Built target multisig
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_blockchain_db
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 37%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/blockchain_db.cpp.o
[ 37%] Building CXX object src/blockchain_db/CMakeFiles/obj_blockchain_db.dir/lmdb/db_lmdb.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 37%] Built target obj_blockchain_db
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target blockchain_db
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 37%] Linking CXX static library libblockchain_db.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 37%] Built target blockchain_db
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target cryptonote_core
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 38%] Linking CXX static library libcryptonote_core.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 38%] Built target cryptonote_core
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_mnemonics
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 38%] Building CXX object src/mnemonics/CMakeFiles/obj_mnemonics.dir/electrum-words.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 38%] Built target obj_mnemonics
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target mnemonics
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 39%] Linking CXX static library libmnemonics.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 39%] Built target mnemonics
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_rpc
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 39%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/core_rpc_server.cpp.o
[ 39%] Building CXX object src/rpc/CMakeFiles/obj_rpc.dir/instanciations.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 39%] Built target obj_rpc
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_rpc_base
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 40%] Building CXX object src/rpc/CMakeFiles/obj_rpc_base.dir/rpc_args.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 40%] Built target obj_rpc_base
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target rpc_base
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 41%] Linking CXX static library librpc_base.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 41%] Built target rpc_base
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_p2p
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 41%] Building CXX object src/p2p/CMakeFiles/obj_p2p.dir/net_node.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 41%] Built target obj_p2p
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target p2p
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 42%] Linking CXX static library libp2p.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 42%] Built target p2p
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_cryptonote_protocol
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 42%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o
[ 42%] Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/cryptonote_protocol_handler-base.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 42%] Built target obj_cryptonote_protocol
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target cryptonote_protocol
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 42%] Linking CXX static library libcryptonote_protocol.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 42%] Built target cryptonote_protocol
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target rpc
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 42%] Linking CXX static library librpc.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 42%] Built target rpc
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_daemon_messages
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 43%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o
[ 43%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/daemon_messages.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 43%] Built target obj_daemon_messages
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_serialization
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 43%] Building CXX object src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 43%] Built target obj_serialization
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target serialization
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 43%] Linking CXX static library libserialization.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 43%] Built target serialization
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target daemon_messages
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 43%] Linking CXX static library libdaemon_messages.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 43%] Built target daemon_messages
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_daemon_rpc_server
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 43%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/daemon_handler.cpp.o
[ 43%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 43%] Built target obj_daemon_rpc_server
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target daemon_rpc_server
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 43%] Linking CXX static library libdaemon_rpc_server.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 43%] Built target daemon_rpc_server
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target obj_wallet
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 43%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
[ 43%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.o
[ 44%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/ringdb.cpp.o
[ 44%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/node_rpc_proxy.cpp.o
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 44%] Built target obj_wallet
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target wallet
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 45%] Linking CXX static library ../../lib/libwallet.a
make[3]: Leaving directory `/usr/local/monero/build/release'
[ 45%] Built target wallet
make[3]: Entering directory `/usr/local/monero/build/release'
Scanning dependencies of target wallet_rpc_server
make[3]: Leaving directory `/usr/local/monero/build/release'
make[3]: Entering directory `/usr/local/monero/build/release'
[ 45%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
[ 46%] Linking CXX executable ../../bin/monero-wallet-rpc
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `bool command_line::get_arg<bool, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<bool, false, false, 1> const&) [clone .isra.1563]':
wallet_rpc_server.cpp:(.text+0x60fb): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `std::string command_line::get_arg<std::string, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<std::string, false, false, 1> const&) [clone .isra.1562]':
wallet_rpc_server.cpp:(.text+0x9023): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `tools::wallet_rpc_server::on_open_wallet(tools::wallet_rpc::COMMAND_RPC_OPEN_WALLET::request const&, tools::wallet_rpc::COMMAND_RPC_OPEN_WALLET::response&, epee::json_rpc::error&)':
wallet_rpc_server.cpp:(.text+0xb4af): undefined reference to `boost::program_options::options_description::options_description(std::string const&, unsigned int, unsigned int)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `tools::wallet_rpc_server::on_create_wallet(tools::wallet_rpc::COMMAND_RPC_CREATE_WALLET::request const&, tools::wallet_rpc::COMMAND_RPC_CREATE_WALLET::response&, epee::json_rpc::error&)':
wallet_rpc_server.cpp:(.text+0x1412d): undefined reference to `boost::program_options::options_description::options_description(std::string const&, unsigned int, unsigned int)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `tools::wallet_rpc_server::init(boost::program_options::variables_map const*)':
wallet_rpc_server.cpp:(.text+0x15819): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
wallet_rpc_server.cpp:(.text+0x1590b): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::program_options::typed_value<std::string, char>::xparse(boost::any&, std::vector<std::string, std::allocator<std::string> > const&) const':
wallet_rpc_server.cpp:(.text._ZNK5boost15program_options11typed_valueISscE6xparseERNS_3anyERKSt6vectorISsSaISsEE[_ZNK5boost15program_options11typed_valueISscE6xparseERNS_3anyERKSt6vectorISsSaISsEE]+0x19): undefined reference to `boost::program_options::validate(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, std::string*, int)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void command_line::add_arg<bool, false, false, 1>(boost::program_options::options_description&, command_line::arg_descriptor<bool, false, false, 1> const&, bool)':
wallet_rpc_server.cpp:(.text._ZN12command_line7add_argIbLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb[_ZN12command_line7add_argIbLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb]+0x44): undefined reference to `boost::program_options::options_description::find_nothrow(std::string const&, bool, bool, bool) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::program_options::typed_value<std::string, char>::name() const':
wallet_rpc_server.cpp:(.text._ZNK5boost15program_options11typed_valueISscE4nameEv[_ZNK5boost15program_options11typed_valueISscE4nameEv]+0x2f): undefined reference to `boost::program_options::arg'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void command_line::add_arg<std::string, true, false, 1>(boost::program_options::options_description&, command_line::arg_descriptor<std::string, true, false, 1> const&, bool)':
wallet_rpc_server.cpp:(.text._ZN12command_line7add_argISsLb1ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb[_ZN12command_line7add_argISsLb1ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb]+0x44): undefined reference to `boost::program_options::options_description::find_nothrow(std::string const&, bool, bool, bool) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void command_line::add_arg<std::string, false, false, 1>(boost::program_options::options_description&, command_line::arg_descriptor<std::string, false, false, 1> const&, bool)':
wallet_rpc_server.cpp:(.text._ZN12command_line7add_argISsLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb[_ZN12command_line7add_argISsLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb]+0x44): undefined reference to `boost::program_options::options_description::find_nothrow(std::string const&, bool, bool, bool) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::program_options::basic_command_line_parser<char>::basic_command_line_parser(int, char const* const*)':
wallet_rpc_server.cpp:(.text._ZN5boost15program_options25basic_command_line_parserIcEC2EiPKPKc[_ZN5boost15program_options25basic_command_line_parserIcEC5EiPKPKc]+0xe8): undefined reference to `boost::program_options::to_internal(std::string const&)'
wallet_rpc_server.cpp:(.text._ZN5boost15program_options25basic_command_line_parserIcEC2EiPKPKc[_ZN5boost15program_options25basic_command_line_parserIcEC5EiPKPKc]+0x131): undefined reference to `boost::program_options::detail::cmdline::cmdline(std::vector<std::string, std::allocator<std::string> > const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::program_options::basic_parsed_options<char> boost::program_options::parse_command_line<char>(int, char const* const*, boost::program_options::options_description const&, int, boost::function1<std::pair<std::string, std::string>, std::string const&>)':
wallet_rpc_server.cpp:(.text._ZN5boost15program_options18parse_command_lineIcEENS0_20basic_parsed_optionsIT_EEiPKPKS3_RKNS0_19options_descriptionEiNS_9function1ISt4pairISsSsERKSsEE[_ZN5boost15program_options18parse_command_lineIcEENS0_20basic_parsed_optionsIT_EEiPKPKS3_RKNS0_19options_descriptionEiNS_9function1ISt4pairISsSsERKSsEE]+0xfb): undefined reference to `boost::program_options::detail::cmdline::set_additional_parser(boost::function1<std::pair<std::string, std::string>, std::string const&>)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::parse_uri(std::string, epee::net_utils::http::uri_content&)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils9parse_uriESsRNS0_4http11uri_contentE[_ZN4epee9net_utils9parse_uriESsRNS0_4http11uri_contentE]+0x362): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::string> boost::re_detail_106700::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::string>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, boost::re_detail_106700::re_set_long<unsigned int> const*, boost::re_detail_106700::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x1a5): undefined reference to `boost::re_detail_106700::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10670016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x519): undefined reference to `boost::re_detail_106700::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_prefix()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12match_prefixEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12match_prefixEv]+0x14c): undefined reference to `boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > >::maybe_assign(boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > > const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::serialization::convert_to_integral<std::string, unsigned long, false>::convert(std::string const&, unsigned long&)':
wallet_rpc_server.cpp:(.text._ZN4epee13serialization19convert_to_integralISsmLb0EE7convertERKSsRm[_ZN4epee13serialization19convert_to_integralISsmLb0EE7convertERKSsRm]+0x399): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::set_reply_content_encoder()':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25set_reply_content_encoderEv[_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25set_reply_content_encoderEv]+0x26e): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::is_connection_close_field(std::string const&)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25is_connection_close_fieldERKSs[_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25is_connection_close_fieldERKSs]+0x204): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::is_multipart_body(epee::net_utils::http::http_header_info const&, std::string&)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE17is_multipart_bodyERKNS1_16http_header_infoERSs[_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE17is_multipart_bodyERKNS1_16http_header_infoERSs]+0x23b): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_invoke_query_line()':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE24handle_invoke_query_lineEv[_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE24handle_invoke_query_lineEv]+0x330): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_match()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE11match_matchEv[_ZN5boost16re_detail_10670012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE11match_matchEv]+0x240): undefined reference to `boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > >::maybe_assign(boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > > const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::parse_cached_header(epee::net_utils::http::http_header_info&, std::string const&, unsigned long)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE19parse_cached_headerERNS1_16http_header_infoERKSsm[_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE19parse_cached_headerERNS1_16http_header_infoERKSsm]+0x251): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::get_len_from_content_lenght(std::string const&, unsigned long&)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE27get_len_from_content_lenghtERKSsRm[_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE27get_len_from_content_lenghtERKSsRm]+0x245): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `main':
wallet_rpc_server.cpp:(.text.startup+0x3e41): undefined reference to `boost::program_options::options_description::options_description(std::string const&, unsigned int, unsigned int)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o:(.data.rel.ro._ZTVN5boost15program_options11typed_valueISscEE[_ZTVN5boost15program_options11typed_valueISscEE]+0x38): undefined reference to `boost::program_options::value_semantic_codecvt_helper<char>::parse(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool) const'
../../lib/libwallet.a(wallet2.cpp.o): In function `std::enable_if<!std::is_same<std::string, bool>::value, bool>::type command_line::has_arg<std::string, false, false, 1>(boost::program_options::variables_map const&, command_line::arg_descriptor<std::string, false, false, 1> const&) [clone .isra.672]':
wallet2.cpp:(.text+0x31ad): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../../lib/libwallet.a(wallet2.cpp.o): In function `bool command_line::get_arg<bool, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<bool, false, false, 1> const&) [clone .isra.2931]':
wallet2.cpp:(.text+0xd60b): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../../lib/libwallet.a(wallet2.cpp.o): In function `std::string command_line::get_arg<std::string, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<std::string, false, false, 1> const&) [clone .isra.2932]':
wallet2.cpp:(.text+0xd833): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../../lib/libwallet.a(wallet2.cpp.o): In function `(anonymous namespace)::make_basic(boost::program_options::variables_map const&, (anonymous namespace)::options const&, std::function<boost::optional<tools::password_container> (char const*, bool)> const&)':
wallet2.cpp:(.text+0x21deb): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../../lib/libwallet.a(wallet2.cpp.o): In function `boost::program_options::validation_error::validation_error(boost::program_options::validation_error::kind_t, std::string const&, std::string const&, int)':
wallet2.cpp:(.text._ZN5boost15program_options16validation_errorC2ENS1_6kind_tERKSsS4_i[_ZN5boost15program_options16validation_errorC5ENS1_6kind_tERKSsS4_i]+0x2f): undefined reference to `boost::program_options::validation_error::get_template(boost::program_options::validation_error::kind_t)'
wallet2.cpp:(.text._ZN5boost15program_options16validation_errorC2ENS1_6kind_tERKSsS4_i[_ZN5boost15program_options16validation_errorC5ENS1_6kind_tERKSsS4_i]+0x45): undefined reference to `boost::program_options::error_with_option_name::error_with_option_name(std::string const&, std::string const&, std::string const&, int)'
../../lib/libwallet.a(wallet2.cpp.o): In function `boost::program_options::typed_value<int, char>::name() const':
wallet2.cpp:(.text._ZNK5boost15program_options11typed_valueIicE4nameEv[_ZNK5boost15program_options11typed_valueIicE4nameEv]+0x2f): undefined reference to `boost::program_options::arg'
../../lib/libwallet.a(wallet2.cpp.o): In function `void command_line::add_arg<std::string, false, true, 1>(boost::program_options::options_description&, command_line::arg_descriptor<std::string, false, true, 1> const&, bool)':
wallet2.cpp:(.text._ZN12command_line7add_argISsLb0ELb1ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb[_ZN12command_line7add_argISsLb0ELb1ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb]+0x44): undefined reference to `boost::program_options::options_description::find_nothrow(std::string const&, bool, bool, bool) const'
../../lib/libwallet.a(wallet2.cpp.o): In function `void command_line::add_arg<int, false, false, 1>(boost::program_options::options_description&, command_line::arg_descriptor<int, false, false, 1> const&, bool)':
wallet2.cpp:(.text._ZN12command_line7add_argIiLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb[_ZN12command_line7add_argIiLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb]+0x44): undefined reference to `boost::program_options::options_description::find_nothrow(std::string const&, bool, bool, bool) const'
../../lib/libwallet.a(wallet2.cpp.o): In function `std::string command_line::get_arg<std::string>(boost::program_options::variables_map const&, command_line::arg_descriptor<std::string, false, true, 1> const&)':
wallet2.cpp:(.text._ZN12command_line7get_argISsEET_RKN5boost15program_options13variables_mapERKNS_14arg_descriptorIS1_Lb0ELb1ELi1EEE[_ZN12command_line7get_argISsEET_RKN5boost15program_options13variables_mapERKNS_14arg_descriptorIS1_Lb0ELb1ELi1EEE]+0x3b): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
wallet2.cpp:(.text._ZN12command_line7get_argISsEET_RKN5boost15program_options13variables_mapERKNS_14arg_descriptorIS1_Lb0ELb1ELi1EEE[_ZN12command_line7get_argISsEET_RKN5boost15program_options13variables_mapERKNS_14arg_descriptorIS1_Lb0ELb1ELi1EEE]+0x74): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../../lib/libwallet.a(wallet2.cpp.o): In function `bool boost::regex_search<std::char_traits<char>, std::allocator<char>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(std::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::match_results<std::basic_string<char, std::char_traits<char>, std::allocator<char> >::const_iterator, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)':
wallet2.cpp:(.text._ZN5boost12regex_searchISt11char_traitsIcESaIcESaINS_9sub_matchIN9__gnu_cxx17__normal_iteratorIPKcSsEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbRKSbIT2_T_T0_ERNS_13match_resultsINSJ_14const_iteratorET1_EERKNS_11basic_regexISG_T3_EENS_15regex_constants12_match_flagsE[_ZN5boost12regex_searchISt11char_traitsIcESaIcESaINS_9sub_matchIN9__gnu_cxx17__normal_iteratorIPKcSsEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbRKSbIT2_T_T0_ERNS_13match_resultsINSJ_14const_iteratorET1_EERKNS_11basic_regexISG_T3_EENS_15regex_constants12_match_flagsE]+0x127): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
../../lib/libwallet.a(wallet2.cpp.o): In function `void boost::program_options::validate<int, char>(boost::any&, std::vector<std::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, int*, long)':
wallet2.cpp:(.text._ZN5boost15program_options8validateIicEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l[_ZN5boost15program_options8validateIicEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l]+0x5a6): undefined reference to `boost::program_options::invalid_option_value::invalid_option_value(std::string const&)'
../../lib/libwallet.a(wallet2.cpp.o):(.data.rel.ro._ZTVN5boost16exception_detail19error_info_injectorINS_15program_options20invalid_option_valueEEE[_ZTVN5boost16exception_detail19error_info_injectorINS_15program_options20invalid_option_valueEEE]+0x30): undefined reference to `boost::program_options::error_with_option_name::substitute_placeholders(std::string const&) const'
../../lib/libwallet.a(wallet2.cpp.o):(.data.rel.ro._ZTVN5boost16exception_detail10clone_implINS0_19error_info_injectorINS_15program_options20invalid_option_valueEEEEE[_ZTVN5boost16exception_detail10clone_implINS0_19error_info_injectorINS_15program_options20invalid_option_valueEEEEE]+0x38): undefined reference to `boost::program_options::error_with_option_name::substitute_placeholders(std::string const&) const'
../../lib/libwallet.a(wallet2.cpp.o):(.data.rel.ro._ZTVN5boost16exception_detail19error_info_injectorINS_15program_options16validation_errorEEE[_ZTVN5boost16exception_detail19error_info_injectorINS_15program_options16validation_errorEEE]+0x30): undefined reference to `boost::program_options::error_with_option_name::substitute_placeholders(std::string const&) const'
../../lib/libwallet.a(wallet2.cpp.o):(.data.rel.ro._ZTVN5boost16exception_detail10clone_implINS0_19error_info_injectorINS_15program_options16validation_errorEEEEE[_ZTVN5boost16exception_detail10clone_implINS0_19error_info_injectorINS_15program_options16validation_errorEEEEE]+0x38): undefined reference to `boost::program_options::error_with_option_name::substitute_placeholders(std::string const&) const'
../../lib/libwallet.a(wallet2.cpp.o):(.data.rel.ro._ZTVN5boost15program_options16validation_errorE[_ZTVN5boost15program_options16validation_errorE]+0x30): undefined reference to `boost::program_options::error_with_option_name::substitute_placeholders(std::string const&) const'
../../lib/libwallet.a(wallet2.cpp.o):(.data.rel.ro._ZTVN5boost15program_options20invalid_option_valueE[_ZTVN5boost15program_options20invalid_option_valueE]+0x30): more undefined references to `boost::program_options::error_with_option_name::substitute_placeholders(std::string const&) const' follow
../../lib/libwallet.a(wallet2.cpp.o):(.data.rel.ro._ZTVN5boost15program_options11typed_valueIicEE[_ZTVN5boost15program_options11typed_valueIicEE]+0x38): undefined reference to `boost::program_options::value_semantic_codecvt_helper<char>::parse(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool) const'
../rpc/librpc_base.a(rpc_args.cpp.o): In function `std::string command_line::get_arg<std::string, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<std::string, false, false, 1> const&) [clone .isra.192]':
rpc_args.cpp:(.text+0x403): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../rpc/librpc_base.a(rpc_args.cpp.o): In function `cryptonote::rpc_args::init_options(boost::program_options::options_description&)':
rpc_args.cpp:(.text+0x57c): undefined reference to `boost::program_options::options_description::find_nothrow(std::string const&, bool, bool, bool) const'
../rpc/librpc_base.a(rpc_args.cpp.o): In function `cryptonote::rpc_args::process(boost::program_options::variables_map const&)':
rpc_args.cpp:(.text+0xc6e): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
rpc_args.cpp:(.text+0xd06): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../common/libcommon.a(util.cpp.o): In function `bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::string>)':
util.cpp:(.text._ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESD_[_ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESD_]+0x115): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `std::enable_if<!std::is_same<std::string, bool>::value, bool>::type command_line::has_arg<std::string, false, false, 1>(boost::program_options::variables_map const&, command_line::arg_descriptor<std::string, false, false, 1> const&) [clone .isra.145]':
miner.cpp:(.text+0x3fd): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `std::enable_if<!std::is_same<unsigned short, bool>::value, bool>::type command_line::has_arg<unsigned short, false, false, 1>(boost::program_options::variables_map const&, command_line::arg_descriptor<unsigned short, false, false, 1> const&) [clone .isra.148]':
miner.cpp:(.text+0x4dd): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `std::string command_line::get_arg<std::string, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<std::string, false, false, 1> const&) [clone .isra.742]':
miner.cpp:(.text+0x1f63): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `bool command_line::get_arg<bool, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<bool, false, false, 1> const&) [clone .isra.745]':
miner.cpp:(.text+0x205b): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `unsigned short command_line::get_arg<unsigned short, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<unsigned short, false, false, 1> const&) [clone .isra.747]':
miner.cpp:(.text+0x215b): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o):miner.cpp:(.text+0x70a6): more undefined references to `boost::program_options::abstract_variables_map::operator[](std::string const&) const' follow
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `void command_line::add_arg<unsigned short, false, false, 1>(boost::program_options::options_description&, command_line::arg_descriptor<unsigned short, false, false, 1> const&, bool)':
miner.cpp:(.text._ZN12command_line7add_argItLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb[_ZN12command_line7add_argItLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb]+0x44): undefined reference to `boost::program_options::options_description::find_nothrow(std::string const&, bool, bool, bool) const'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `bool boost::regex_match<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)':
miner.cpp:(.text._ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE[_ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE]+0xf0): undefined reference to `boost::re_detail_106700::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `boost::program_options::typed_value<unsigned short, char>::name() const':
miner.cpp:(.text._ZNK5boost15program_options11typed_valueItcE4nameEv[_ZNK5boost15program_options11typed_valueItcE4nameEv]+0x2f): undefined reference to `boost::program_options::arg'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `void boost::program_options::validate<unsigned short, char>(boost::any&, std::vector<std::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, unsigned short*, long)':
miner.cpp:(.text._ZN5boost15program_options8validateItcEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l[_ZN5boost15program_options8validateItcEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l]+0x1ba): undefined reference to `boost::program_options::invalid_option_value::invalid_option_value(std::string const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o):(.data.rel.ro._ZTVN5boost15program_options11typed_valueItcEE[_ZTVN5boost15program_options11typed_valueItcEE]+0x38): undefined reference to `boost::program_options::value_semantic_codecvt_helper<char>::parse(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool) const'
../../lib/libwallet.a(wallet_args.cpp.o): In function `bool command_line::is_arg_defaulted<std::string, false, false, 1>(boost::program_options::variables_map const&, command_line::arg_descriptor<std::string, false, false, 1> const&) [clone .isra.77]':
wallet_args.cpp:(.text+0x5b): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../../lib/libwallet.a(wallet_args.cpp.o): In function `bool command_line::get_arg<bool, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<bool, false, false, 1> const&) [clone .isra.275]':
wallet_args.cpp:(.text+0x36b): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../../lib/libwallet.a(wallet_args.cpp.o): In function `std::string command_line::get_arg<std::string, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<std::string, false, false, 1> const&) [clone .isra.276]':
wallet_args.cpp:(.text+0x463): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../../lib/libwallet.a(wallet_args.cpp.o): In function `void command_line::add_arg<unsigned long, false, false, 1>(boost::program_options::options_description&, command_line::arg_descriptor<unsigned long, false, false, 1> const&, bool)':
wallet_args.cpp:(.text._ZN12command_line7add_argImLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb[_ZN12command_line7add_argImLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb]+0x44): undefined reference to `boost::program_options::options_description::find_nothrow(std::string const&, bool, bool, bool) const'
../../lib/libwallet.a(wallet_args.cpp.o): In function `void command_line::add_arg<unsigned int, false, false, 1>(boost::program_options::options_description&, command_line::arg_descriptor<unsigned int, false, false, 1> const&, bool)':
wallet_args.cpp:(.text._ZN12command_line7add_argIjLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb[_ZN12command_line7add_argIjLb0ELb0ELi1EEEvRN5boost15program_options19options_descriptionERKNS_14arg_descriptorIT_XT0_EXT1_EXT2_EEEb]+0x44): undefined reference to `boost::program_options::options_description::find_nothrow(std::string const&, bool, bool, bool) const'
../../lib/libwallet.a(wallet_args.cpp.o): In function `wallet_args::main(int, char**, char const*, char const*, boost::program_options::options_description, boost::program_options::positional_options_description const&, std::function<void (std::string const&, bool)> const&, char const*, bool)':
wallet_args.cpp:(.text.startup+0x2cb): undefined reference to `boost::program_options::options_description::options_description(std::string const&, unsigned int, unsigned int)'
wallet_args.cpp:(.text.startup+0x7b0): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
wallet_args.cpp:(.text.startup+0x9c3): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
wallet_args.cpp:(.text.startup+0xb33): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
wallet_args.cpp:(.text.startup+0xb7b): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../../lib/libwallet.a(wallet_args.cpp.o): In function `boost::program_options::typed_value<unsigned int, char>::name() const':
wallet_args.cpp:(.text._ZNK5boost15program_options11typed_valueIjcE4nameEv[_ZNK5boost15program_options11typed_valueIjcE4nameEv]+0x2f): undefined reference to `boost::program_options::arg'
../../lib/libwallet.a(wallet_args.cpp.o): In function `boost::program_options::typed_value<unsigned long, char>::name() const':
wallet_args.cpp:(.text._ZNK5boost15program_options11typed_valueImcE4nameEv[_ZNK5boost15program_options11typed_valueImcE4nameEv]+0x2f): undefined reference to `boost::program_options::arg'
../../lib/libwallet.a(wallet_args.cpp.o): In function `void boost::program_options::validate<unsigned int, char>(boost::any&, std::vector<std::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, unsigned int*, long)':
wallet_args.cpp:(.text._ZN5boost15program_options8validateIjcEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l[_ZN5boost15program_options8validateIjcEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l]+0x566): undefined reference to `boost::program_options::invalid_option_value::invalid_option_value(std::string const&)'
../../lib/libwallet.a(wallet_args.cpp.o): In function `void boost::program_options::validate<unsigned long, char>(boost::any&, std::vector<std::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, unsigned long*, long)':
wallet_args.cpp:(.text._ZN5boost15program_options8validateImcEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l[_ZN5boost15program_options8validateImcEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l]+0x5a1): undefined reference to `boost::program_options::invalid_option_value::invalid_option_value(std::string const&)'
../../lib/libwallet.a(wallet_args.cpp.o):(.data.rel.ro._ZTVN5boost15program_options11typed_valueImcEE[_ZTVN5boost15program_options11typed_valueImcEE]+0x38): undefined reference to `boost::program_options::value_semantic_codecvt_helper<char>::parse(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool) const'
../../lib/libwallet.a(wallet_args.cpp.o):(.data.rel.ro._ZTVN5boost15program_options11typed_valueIjcEE[_ZTVN5boost15program_options11typed_valueIjcEE]+0x38): undefined reference to `boost::program_options::value_semantic_codecvt_helper<char>::parse(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool) const'
collect2: error: ld returned 1 exit status
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory `/usr/local/monero/build/release'
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory `/usr/local/monero/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory `/usr/local/monero/build/release'
make: *** [release-all] Error 2
```


I built  bependencies  as following.
```
RUN apt-get update && \
    apt-get --no-install-recommends --yes install \
        ca-certificates \
        cmake \
        g++ \
        make \
        pkg-config \
        graphviz \
        doxygen \
        git \
        curl \
        libtool-bin \
        autoconf \
        automake \
        bzip2

WORKDIR /usr/local

#Cmake
ARG CMAKE_VERSION=3.11.2
ARG CMAKE_VERSION_DOT=v3.11
ARG CMAKE_HASH=5ebc22bbcf2b4c7a20c4190d42c084cf38680a85b1a7980a2f1d5b4a52bf5248
RUN curl -s -O https://cmake.org/files/${CMAKE_VERSION_DOT}/cmake-${CMAKE_VERSION}.tar.gz \
    && echo "${CMAKE_HASH} cmake-${CMAKE_VERSION}.tar.gz" | sha256sum -c \
    && tar -xzf cmake-${CMAKE_VERSION}.tar.gz \
    && cd cmake-${CMAKE_VERSION} \
    && ./configure \
    && make \
    && make install

## Boost
ARG BOOST_VERSION=1_67_0
ARG BOOST_VERSION_DOT=1.67.0
ARG BOOST_HASH=2684c972994ee57fc5632e03bf044746f6eb45d4920c343937a465fd67a5adba
RUN curl -s -L -o  boost_${BOOST_VERSION}.tar.bz2 https://dl.bintray.com/boostorg/release/${BOOST_VERSION_DOT}/source/boost_${BOOST_VERSION}.tar.bz2 \
    && echo "${BOOST_HASH} boost_${BOOST_VERSION}.tar.bz2" | sha256sum -c \
    && tar -xvf boost_${BOOST_VERSION}.tar.bz2 \
    && cd boost_${BOOST_VERSION} \
    && ./bootstrap.sh \
    && ./b2 --build-type=minimal link=static runtime-link=static --with-chrono --with-date_time --with-filesystem --with-program_options --with-regex --with-serialization --with-system --with-thread --with-locale threading=multi threadapi=pthread cflags="-fPIC" cxxflags="-fPIC" stage
ENV BOOST_ROOT /usr/local/boost_${BOOST_VERSION}

# OpenSSL
ARG OPENSSL_VERSION=1.1.0h
ARG OPENSSL_HASH=5835626cde9e99656585fc7aaa2302a73a7e1340bf8c14fd635a62c66802a517
RUN curl -s -O https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \
    && echo "${OPENSSL_HASH} openssl-${OPENSSL_VERSION}.tar.gz" | sha256sum -c \
    && tar -xzf openssl-${OPENSSL_VERSION}.tar.gz \
    && cd openssl-${OPENSSL_VERSION} \
    && ./Configure linux-x86_64 no-shared --static -fPIC \
    && make build_generated \
    && make libcrypto.a \
    && make install
ENV OPENSSL_ROOT_DIR=/usr/local/openssl-${OPENSSL_VERSION}

# ZMQ
ARG ZMQ_VERSION=v4.2.5
ARG ZMQ_HASH=d062edd8c142384792955796329baf1e5a3377cd
RUN git clone https://github.com/zeromq/libzmq.git -b ${ZMQ_VERSION} \
    && cd libzmq \
    && test `git rev-parse HEAD` = ${ZMQ_HASH} || exit 1 \
    && ./autogen.sh \
    && CFLAGS="-fPIC" CXXFLAGS="-fPIC" ./configure --enable-static --disable-shared \
    && make \
    && make install \
    && ldconfig

# zmq.hpp
ARG CPPZMQ_VERSION=v4.2.3
ARG CPPZMQ_HASH=6aa3ab686e916cb0e62df7fa7d12e0b13ae9fae6
RUN git clone https://github.com/zeromq/cppzmq.git -b ${CPPZMQ_VERSION} \
    && cd cppzmq \
    && test `git rev-parse HEAD` = ${CPPZMQ_HASH} || exit 1 \
    && mv *.hpp /usr/local/include

# Readline
ARG READLINE_VERSION=7.0
ARG READLINE_HASH=750d437185286f40a369e1e4f4764eda932b9459b5ec9a731628393dd3d32334
RUN curl -s -O https://ftp.gnu.org/gnu/readline/readline-${READLINE_VERSION}.tar.gz \
    && echo "${READLINE_HASH} readline-${READLINE_VERSION}.tar.gz" | sha256sum -c \
    && tar -xzf readline-${READLINE_VERSION}.tar.gz \
    && cd readline-${READLINE_VERSION} \
    && CFLAGS="-fPIC" CXXFLAGS="-fPIC" ./configure \
    && make \
    && make install

# Sodium
ARG SODIUM_VERSION=1.0.16
ARG SODIUM_HASH=675149b9b8b66ff44152553fb3ebf9858128363d
RUN git clone https://github.com/jedisct1/libsodium.git -b ${SODIUM_VERSION} \
    && cd libsodium \
    && test `git rev-parse HEAD` = ${SODIUM_HASH} || exit 1 \
    && ./autogen.sh \
    && CFLAGS="-fPIC" CXXFLAGS="-fPIC" ./configure \
    && make \
    && make check \
    && make install
```

I have been compiling Monero for 3days and trying to solve this problem. 
But failed. So i will very appreciate for your help, thanks

# Discussion History
## moneromooo-monero | 2018-09-12T10:27:30+00:00
How many boost do you have installed ?
Is this a build from a clean repo ?

## jackieWhn | 2018-09-12T10:35:39+00:00
1. How many boost do you have installed ?
boost 1.54, installed by "sudo apt-get install libboost-dev"
boost 1.66 and boost 1.67 installed from source

2. Is this a build from a clean repo ?
Do you mean monero? 

@moneromooo-monero 

## moneromooo-monero | 2018-09-12T10:41:27+00:00
1. Make sure headers and libs are both from the same boost tree/install, whether from cmake, compile, or link. You can use VERBOSE=1 on the make command line to see the command lines. In particular, check the last -L flag in the link line before the boost libs.

2. Yes


## jackieWhn | 2018-09-12T10:56:54+00:00
1. I compile monero by  "make VERBOSE=1" and got infos below. How can i konw that if boosts are same or not? 

```
[ 52%] Linking CXX executable ../../bin/monero-wallet-rpc
cd /usr/local/monero/build/release/src/wallet && /usr/local/bin/cmake -E cmake_link_script CMakeFiles/wallet_rpc_server.dir/link.txt --verbose=1
/usr/bin/c++   -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=native  -fPIC  -Wformat -Wformat-security -fstack-protector -fno-strict-aliasing -DNDEBUG -Ofast     -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -rdynamic CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  -o ../../bin/monero-wallet-rpc -Wl,-rpath,/usr/local/lib: -lrt -ldl ../../lib/libwallet.a ../../contrib/epee/src/libepee.a ../rpc/librpc_base.a ../cryptonote_core/libcryptonote_core.a ../crypto/libcncrypto.a ../common/libcommon.a ../libversion.a /usr/local/lib/libboost_chrono.so /usr/local/lib/libboost_program_options.so /usr/local/lib/libboost_filesystem.so /usr/local/lib/libboost_thread.so -pthread -lrt -ldl ../blockchain_db/libblockchain_db.a ../multisig/libmultisig.a ../ringct/libringct.a ../cryptonote_basic/libcryptonote_basic.a ../device/libdevice.a ../blocks/libblocks.a -lpcsclite ../ringct/libringct_basic.a ../checkpoints/libcheckpoints.a ../mnemonics/libmnemonics.a ../../external/db_drivers/liblmdb/liblmdb.a /usr/local/lib/libboost_serialization.so ../common/libcommon.a ../crypto/libcncrypto.a ../../contrib/epee/src/libepee.a ../../external/easylogging++/libeasylogging.a -pthread -lunb.....
```

2. i use "make clean" or  "git clone" again.  

@moneromooo-monero 

## moneromooo-monero | 2018-09-12T11:07:27+00:00
That link line is linking against boost in /usr/local/lib (/usr/local/lib/libboost_chrono.so).
Check what the compilation step uses.

## jackieWhn | 2018-09-13T03:07:17+00:00
i uninstall all the boost and reinstall boost_1_67 into the folder /usr/local.
I got this info after running make VERBOSE=1.


[ 46%] Linking CXX executable ../../bin/monero-wallet-rpc
cd /usr/local/monero/build/release/src/wallet && /usr/local/bin/cmake -E cmake_link_script CMakeFiles/wallet_rpc_server.dir/link.txt --verbose=1
/usr/bin/c++   -fno-strict-aliasing -maes -std=c++11 -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -march=native  -fPIC  -Wformat -Wformat-security -fstack-protector -fno-strict-aliasing -DNDEBUG -Ofast     -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -rdynamic CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o  -o ../../bin/monero-wallet-rpc -lrt -ldl ../../lib/libwallet.a ../../contrib/epee/src/libepee.a ../rpc/librpc_base.a ../cryptonote_core/libcryptonote_core.a ../crypto/libcncrypto.a ../common/libcommon.a ../libversion.a **/usr/local/boost_1_67_0/stage/lib/libboost_chrono.a /usr/local/boost_1_67_0/stage/lib/libboost_program_options.a /usr/local/boost_1_67_0/stage/lib/libboost_filesystem.a /usr/local/boost_1_67_0/stage/lib/libboost_thread.a -pthread** -lrt -ldl ../blockchain_db/libblockchain_db.a ../multisig/libmultisig.a ../ringct/libringct.a ../cryptonote_basic/libcryptonote_basic.a ../device/libdevice.a ../blocks/libblocks.a -lpcsclite ../ringct/libringct_basic.a ../checkpoints/libcheckpoints.a ../mnemonics/libmnemonics.a ../../external/db_drivers/liblmdb/liblmdb.a **/usr/local/boost_1_67_0/stage/lib/libboost_serialization.a** ../common/libcommon.a ../crypto/libcncrypto.a ../../contrib/epee/src/libepee.a ../../external/easylogging++/libeasylogging.a -pthread -lunbound **/usr/local/boost_1_67_0/stage/lib/libboost_chrono.a** /usr/local/openssl-1.1.0h/libssl.a /usr/local/openssl-1.1.0h/libcrypto.a **/usr/local/boost_1_67_0/stage/lib/libboost_date_time.a** **/usr/local/boost_1_67_0/stage/lib/libboost_filesystem.a /usr/local/boost_1_67_0/stage/lib/libboost_system.a /usr/local/boost_1_67_0/stage/lib/libboost_program_options.a /usr/local/boost_1_67_0/stage/lib/libboost_thread.a /usr/local/boost_1_67_0/stage/lib/libboost_regex.a** -lrt -ldl 
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `bool command_line::get_arg<bool, false>(boost::program_options::variables_map const&, command_line::arg_descriptor<bool, false, false, 1> const&) [clone .isra.1563]':.....
<void (std::string const&, bool)> const&, char const*, bool)':
wallet_args.cpp:(.text.startup+0x2cb): undefined reference to `boost::program_options::options_description::options_description(std::string const&, unsigned int, unsigned int)'
wallet_args.cpp:(.text.startup+0x7b0): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
wallet_args.cpp:(.text.startup+0x9c3): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
wallet_args.cpp:(.text.startup+0xb33): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
wallet_args.cpp:(.text.startup+0xb7b): undefined reference to `boost::program_options::abstract_variables_map::operator[](std::string const&) const'
../../lib/libwallet.a(wallet_args.cpp.o): In function `boost::program_options::typed_value<unsigned int, char>::name() const':
wallet_args.cpp:(.text._ZNK5boost15program_options11typed_valueIjcE4nameEv[_ZNK5boost15program_options11typed_valueIjcE4nameEv]+0x2f): undefined reference to `boost::program_options::arg'
../../lib/libwallet.a(wallet_args.cpp.o): In function `boost::program_options::typed_value<unsigned long, char>::name() const':
wallet_args.cpp:(.text._ZNK5boost15program_options11typed_valueImcE4nameEv[_ZNK5boost15program_options11typed_valueImcE4nameEv]+0x2f): undefined reference to `boost::program_options::arg'
../../lib/libwallet.a(wallet_args.cpp.o): In function `void boost::program_options::validate<unsigned int, char>(boost::any&, std::vector<std::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, unsigned int*, long)':
wallet_args.cpp:(.text._ZN5boost15program_options8validateIjcEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l[_ZN5boost15program_options8validateIjcEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l]+0x566): undefined reference to `boost::program_options::invalid_option_value::invalid_option_value(std::string const&)'
../../lib/libwallet.a(wallet_args.cpp.o): In function `void boost::program_options::validate<unsigned long, char>(boost::any&, std::vector<std::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, unsigned long*, long)':
wallet_args.cpp:(.text._ZN5boost15program_options8validateImcEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l[_ZN5boost15program_options8validateImcEEvRNS_3anyERKSt6vectorISbIT0_St11char_traitsIS5_ESaIS5_EESaIS9_EEPT_l]+0x5a1): undefined reference to `boost::program_options::invalid_option_value::invalid_option_value(std::string const&)'
../../lib/libwallet.a(wallet_args.cpp.o):(.data.rel.ro._ZTVN5boost15program_options11typed_valueImcEE[_ZTVN5boost15program_options11typed_valueImcEE]+0x38): undefined reference to `boost::program_options::value_semantic_codecvt_helper<char>::parse(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool) const'
../../lib/libwallet.a(wallet_args.cpp.o):(.data.rel.ro._ZTVN5boost15program_options11typed_valueIjcEE[_ZTVN5boost15program_options11typed_valueIjcEE]+0x38): undefined reference to `boost::program_options::value_semantic_codecvt_helper<char>::parse(boost::any&, std::vector<std::string, std::allocator<std::string> > const&, bool) const'
collect2: error: ld returned 1 exit status
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory `/usr/local/monero/build/release'
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory `/usr/local/monero/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory `/usr/local/monero/build/release'
make: *** [release-all] Error 2

@moneromooo-monero 
how to check what the compilation step uses ? thanks
And i think the main reason is "undefined reference to `boost::program_options"


## moneromooo-monero | 2018-09-13T08:26:24+00:00
Look at an earlier step. It might have -I flags to boost directories. If not, it'll find the ones in /usr/include or whatever's in $C_INCLUDE_PATH (assuming cmake uses that, not sure it does, it can be annoying with its defaults). Also check the output of cmake when it configures, it tells you which boost version it found.

## iDunk5400 | 2018-09-14T08:36:52+00:00
That one could be the classic issue where a dependency (boost in this case) was built with a different GCC than the program itself.

Note that if you decide to rebuild boost with your current compiler, you might (will) need to rebuild all your other software using that particular boost installation.

## moneromooo-monero | 2018-10-09T11:03:38+00:00
Did you try the suggestion above ? If so, did it work ?

## Ulmo | 2018-10-19T18:32:16+00:00
The heck.  Nvidia drivers require GCC6, but GCC7 is latest.  This will cause problems.  Can't you package maintainers properly select the right compiler for building at build time?

For instance, I have GCC6 set as default in my PATH.  But, if your package is picky about which compiler to build, it can find the GCC's it likes for what it wants and do that, rather than telling me I did something wrong.  Yes, I think NVIDIA should do the same thing.  But fact is, both GCC's should work fine for most things, so I don't think it should matter that I have GCC6 as default, and if your build requires a certain GCC for something, it should build as such rather than blaming me for its failures.  Yes, I'm saying that if your build process finds a library it needs that has been built with GCC7 that your build requires GCC7 to link against that library with that your build then find GCC7 and use GCC7 for that build portion, and/or at the least enforce that in a legible error message that we understand.  Even though you are not NVIDIA.  After all, this is YOUR failure due to YOU linking wrongly based upon YOUR bad selection of compiler that YOU tried to use, just because that's what happened to be in the PATH and system library build history.

## fluffypony | 2018-10-19T18:54:09+00:00
@Ulmo you can have multiple versions of gcc installed and switch between them using update-alternatives. See: https://codeyarns.com/2015/02/26/how-to-switch-gcc-version-using-update-alternatives/

## Ulmo | 2018-10-20T05:31:01+00:00
Thank you for reminding me and telling me it still exists; I can look into that when I open up a little bit of spacetime.

## moneromooo-monero | 2018-10-23T11:18:06+00:00
Did you whether check those -I flags match the libs directory ?

## moneromooo-monero | 2018-12-13T13:04:34+00:00
I'll close this later if no more info is given, as it looks like user error.


## BigslimVdub | 2019-01-04T04:12:38+00:00
I am getting same this issue building Aeon v0.12.8.0 right now on 16.04, looking into it. 


## moneromooo-monero | 2019-04-14T10:15:39+00:00
Did you find anything, or did you just have two boost versions around ?

## moneromooo-monero | 2019-06-15T10:50:32+00:00
Very likely user config error and no reply. Reopen if you are *sure* it's not user error and it still happens with 0.14.1.0.

+invalid


# Action History
- Created by: jackieWhn | 2018-09-12T10:21:13+00:00
- Closed at: 2019-06-15T17:33:27+00:00
