---
title: 'recipe for target ''bin/monero-wallet-rpc'' failed , undefined reference to
  `boost::'
source_url: https://github.com/monero-project/monero/issues/4051
author: minzak
assignees: []
labels: []
created_at: '2018-06-25T14:23:54+00:00'
updated_at: '2018-06-26T10:44:40+00:00'
type: issue
status: closed
closed_at: '2018-06-26T10:44:40+00:00'
---

# Original Description
Debian 8 x64
**apt install libbz2-dev build-essential cmake pkg-config libboost-all-dev libssl-dev libzmq3-dev libunbound-dev libsodium-dev libminiupnpc-dev libunwind8-dev liblzma-dev libreadline6-dev libldns-dev libexpat1-dev libgtest-dev doxygen graphviz**

with boost 1.66
```
cd /usr/src
https://dl.bintray.com/boostorg/release/1.66.0/source/boost_1_66_0.tar.bz2
tar -xvf boost_1_66_0.tar
cd boost_1_66_0
./bootstrap.sh --prefix=/usr/local --with-libraries=all
./bjam install
```

And run it:
```
cd /usr/src
git clone --recursive https://github.com/monero-project/monero
cd monero && git submodule init && git submodule update
git checkout v0.12.2.0
make build && cd build
cmake
make
```

I got:

```
root@monero:/usr/src/monero/build# make
[  5%] Built target generate_translations_header
[ 15%] Built target libminiupnpc-static
[ 17%] Built target lmdb
[ 18%] Built target easylogging
[ 25%] Built target epee
[ 26%] Built target epee_readline
[ 27%] Built target genversion
[ 29%] Built target obj_version
[ 29%] Built target version
[ 43%] Built target obj_cncrypto
[ 43%] Built target cncrypto
[ 51%] Built target obj_common
[ 51%] Built target common
[ 52%] Built target obj_ringct
[ 55%] Built target obj_ringct_basic
[ 58%] Built target obj_device
[ 58%] Built target ringct_basic
[ 61%] Built target blocks
[ 61%] Built target device
[ 62%] Built target obj_checkpoints
[ 62%] Built target checkpoints
[ 66%] Built target obj_cryptonote_basic
[ 66%] Built target cryptonote_basic
[ 66%] Built target ringct
[ 69%] Built target obj_cryptonote_core
[ 70%] Built target obj_multisig
[ 70%] Built target multisig
[ 72%] Built target obj_blockchain_db
[ 72%] Built target blockchain_db
[ 72%] Built target cryptonote_core
[ 73%] Built target obj_mnemonics
[ 73%] Built target mnemonics
[ 74%] Built target obj_daemon_messages
[ 75%] Built target obj_serialization
[ 75%] Built target obj_p2p
[ 75%] Built target p2p
[ 77%] Built target obj_cryptonote_protocol
[ 77%] Built target cryptonote_protocol
[ 77%] Built target serialization
[ 77%] Built target daemon_messages
[ 78%] Built target obj_rpc_base
[ 78%] Built target rpc_base
[ 79%] Built target obj_rpc
[ 79%] Built target rpc
[ 80%] Built target obj_daemon_rpc_server
[ 80%] Built target daemon_rpc_server
[ 83%] Built target obj_wallet
[ 83%] Built target wallet
Linking CXX executable ../../bin/monero-wallet-rpc
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&) [clone .part.800]':
wallet_rpc_server.cpp:(.text+0xebb): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb]+0x2c): undefined reference to `boost::re_detail_106000::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::call_run_once_service_io()':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE24call_run_once_service_ioEv[_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE24call_run_once_service_ioEv]+0x39f): undefined reference to `boost::this_thread::hiden::sleep_until(timespec const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x1a): undefined reference to `boost::re_detail_106000::get_mem_block()'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x17b): undefined reference to `boost::re_detail_106000::verify_options(unsigned int, boost::regex_constants::_match_flags)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x1ba): undefined reference to `boost::re_detail_106000::put_mem_block(void*)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x341): undefined reference to `boost::re_detail_106000::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::parse_uri(std::string, epee::net_utils::http::uri_content&)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils9parse_uriESsRNS0_4http11uri_contentE[_ZN4epee9net_utils9parse_uriESsRNS0_4http11uri_contentE]+0x347): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::re_detail_106000::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0x95): undefined reference to `boost::re_detail_106000::get_default_error_string(boost::regex_constants::error_type)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xc8): undefined reference to `boost::re_detail_106000::raise_runtime_error(std::runtime_error const&)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xf3): undefined reference to `boost::re_detail_106000::get_default_error_string(boost::regex_constants::error_type)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::string> boost::re_detail_106000::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::string>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, boost::re_detail_106000::re_set_long<unsigned int> const*, boost::re_detail_106000::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x190): undefined reference to `boost::re_detail_106000::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x325): undefined reference to `boost::re_detail_106000::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::extend_stack()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv]+0x18): undefined reference to `boost::re_detail_106000::get_mem_block()'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x1a): undefined reference to `boost::re_detail_106000::get_mem_block()'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x13c): undefined reference to `boost::re_detail_106000::verify_options(unsigned int, boost::regex_constants::_match_flags)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x16a): undefined reference to `boost::re_detail_106000::put_mem_block(void*)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x22c): undefined reference to `boost::re_detail_106000::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::serialization::convert_to_integral<std::string, unsigned long, false>::convert(std::string const&, unsigned long&)':
wallet_rpc_server.cpp:(.text._ZN4epee13serialization19convert_to_integralISsmLb0EE7convertERKSsRm[_ZN4epee13serialization19convert_to_integralISsmLb0EE7convertERKSsRm]+0x2c2): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::set_reply_content_encoder()':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25set_reply_content_encoderEv[_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25set_reply_content_encoderEv]+0x2e4): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::is_connection_close_field(std::string const&)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25is_connection_close_fieldERKSs[_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25is_connection_close_fieldERKSs]+0x208): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::is_multipart_body(epee::net_utils::http::http_header_info const&, std::string&)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE17is_multipart_bodyERKNS1_16http_header_infoERSs[_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE17is_multipart_bodyERKNS1_16http_header_infoERSs]+0x224): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_invoke_query_line()':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE24handle_invoke_query_lineEv[_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE24handle_invoke_query_lineEv]+0x33d): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o:wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE19parse_cached_headerERNS1_16http_header_infoERKSsm[_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE19parse_cached_headerERNS1_16http_header_infoERKSsm]+0x270): more undefined references to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)' follow
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::do_send_chunk(void const*, unsigned long)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE13do_send_chunkEPKvm[_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE13do_send_chunkEPKvm]+0x3b4): undefined reference to `boost::this_thread::hiden::sleep_until(timespec const&)'
../../lib/libwallet.a(wallet2.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&) [clone .part.913]':
wallet2.cpp:(.text+0x1bdb): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
../../lib/libwallet.a(wallet2.cpp.o): In function `epee::net_utils::parse_url(std::string, epee::net_utils::http::url_content&)':
wallet2.cpp:(.text._ZN4epee9net_utils9parse_urlESsRNS0_4http11url_contentE[_ZN4epee9net_utils9parse_urlESsRNS0_4http11url_contentE]+0x34d): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
../../lib/libwallet.a(node_rpc_proxy.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&) [clone .part.383]':
node_rpc_proxy.cpp:(.text+0x1fb): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
../../contrib/epee/src/libepee.a(connection_basic.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&) [clone .part.122]':
connection_basic.cpp:(.text+0xeb): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
../../contrib/epee/src/libepee.a(connection_basic.cpp.o): In function `epee::net_utils::connection_basic::sleep_before_packet(unsigned long, int, int)':
connection_basic.cpp:(.text+0x1096): undefined reference to `boost::this_thread::hiden::sleep_until(timespec const&)'
../common/libcommon.a(util.cpp.o): In function `bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::string>)':
util.cpp:(.text._ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESD_[_ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESD_]+0x123): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&) [clone .part.154]':
miner.cpp:(.text+0x1db): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1l> >(boost::chrono::duration<long, boost::ratio<1l, 1l> > const&) [clone .part.155]':
miner.cpp:(.text+0x28b): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `boost::this_thread::sleep(boost::posix_time::ptime const&)':
miner.cpp:(.text._ZN5boost11this_thread5sleepERKNS_10posix_time5ptimeE[_ZN5boost11this_thread5sleepERKNS_10posix_time5ptimeE]+0xf4): undefined reference to `boost::this_thread::hiden::sleep_until(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `bool boost::regex_match<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)':
miner.cpp:(.text._ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE[_ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE]+0xe4): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:124: recipe for target 'bin/monero-wallet-rpc' failed
make[2]: *** [bin/monero-wallet-rpc] Error 1
CMakeFiles/Makefile2:2141: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[1]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
Makefile:127: recipe for target 'all' failed
make: *** [all] Error 2
root@monero:/usr/src/monero/build#
```
What is wrong?

Or same error if i use make in root without cmake

```
[ 48%] Built target wallet
make[3]: Entering directory '/usr/src/monero/build/release'
Scanning dependencies of target wallet_rpc_server
make[3]: Leaving directory '/usr/src/monero/build/release'
make[3]: Entering directory '/usr/src/monero/build/release'
[ 49%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
Linking CXX executable ../../bin/monero-wallet-rpc
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&) [clone .part.800]':
wallet_rpc_server.cpp:(.text+0xebb): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::unwind_extra_block(bool)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE18unwind_extra_blockEb]+0x2c): undefined reference to `boost::re_detail_106000::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::call_run_once_service_io()':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE24call_run_once_service_ioEv[_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE24call_run_once_service_ioEv]+0x39f): undefined reference to `boost::this_thread::hiden::sleep_until(timespec const&)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::find_imp()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x1a): undefined reference to `boost::re_detail_106000::get_mem_block()'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x17b): undefined reference to `boost::re_detail_106000::verify_options(unsigned int, boost::regex_constants::_match_flags)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x1ba): undefined reference to `boost::re_detail_106000::put_mem_block(void*)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x341): undefined reference to `boost::re_detail_106000::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::parse_uri(std::string, epee::net_utils::http::uri_content&)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils9parse_uriESsRNS0_4http11uri_contentE[_ZN4epee9net_utils9parse_uriESsRNS0_4http11uri_contentE]+0x347): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `void boost::re_detail_106000::raise_error<boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > >(boost::regex_traits_wrapper<boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::error_type)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0x95): undefined reference to `boost::re_detail_106000::get_default_error_string(boost::regex_constants::error_type)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xc8): undefined reference to `boost::re_detail_106000::raise_runtime_error(std::runtime_error const&)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE[_ZN5boost16re_detail_10600011raise_errorINS_20regex_traits_wrapperINS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEEEvRKT_NS_15regex_constants10error_typeE]+0xf3): undefined reference to `boost::re_detail_106000::get_default_error_string(boost::regex_constants::error_type)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `__gnu_cxx::__normal_iterator<char const*, std::string> boost::re_detail_106000::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::string>, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, boost::re_detail_106000::re_set_long<unsigned int> const*, boost::re_detail_106000::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x190): undefined reference to `boost::re_detail_106000::cpp_regex_traits_implementation<char>::transform_primary(char const*, char const*) const'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcSsEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SB_SB_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x325): undefined reference to `boost::re_detail_106000::cpp_regex_traits_implementation<char>::transform(char const*, char const*) const'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::extend_stack()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE12extend_stackEv]+0x18): undefined reference to `boost::re_detail_106000::get_mem_block()'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::match_imp()':
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x1a): undefined reference to `boost::re_detail_106000::get_mem_block()'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x13c): undefined reference to `boost::re_detail_106000::verify_options(unsigned int, boost::regex_constants::_match_flags)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x16a): undefined reference to `boost::re_detail_106000::put_mem_block(void*)'
wallet_rpc_server.cpp:(.text._ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv[_ZN5boost16re_detail_10600012perl_matcherIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS6_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE9match_impEv]+0x22c): undefined reference to `boost::re_detail_106000::put_mem_block(void*)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::serialization::convert_to_integral<std::string, unsigned long, false>::convert(std::string const&, unsigned long&)':
wallet_rpc_server.cpp:(.text._ZN4epee13serialization19convert_to_integralISsmLb0EE7convertERKSsRm[_ZN4epee13serialization19convert_to_integralISsmLb0EE7convertERKSsRm]+0x2c2): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::set_reply_content_encoder()':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25set_reply_content_encoderEv[_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25set_reply_content_encoderEv]+0x2e4): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::is_connection_close_field(std::string const&)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25is_connection_close_fieldERKSs[_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE25is_connection_close_fieldERKSs]+0x208): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::is_multipart_body(epee::net_utils::http::http_header_info const&, std::string&)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE17is_multipart_bodyERKNS1_16http_header_infoERSs[_ZN4epee9net_utils4http27http_simple_client_templateINS0_19blocked_mode_clientEE17is_multipart_bodyERKNS1_16http_header_infoERSs]+0x224): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_invoke_query_line()':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE24handle_invoke_query_lineEv[_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE24handle_invoke_query_lineEv]+0x33d): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o:wallet_rpc_server.cpp:(.text._ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE19parse_cached_headerERNS1_16http_header_infoERKSsm[_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE19parse_cached_headerERNS1_16http_header_infoERKSsm]+0x270): more undefined references to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)' follow
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::do_send_chunk(void const*, unsigned long)':
wallet_rpc_server.cpp:(.text._ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE13do_send_chunkEPKvm[_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE13do_send_chunkEPKvm]+0x3b4): undefined reference to `boost::this_thread::hiden::sleep_until(timespec const&)'
../../lib/libwallet.a(wallet2.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&) [clone .part.913]':
wallet2.cpp:(.text+0x1bdb): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
../../lib/libwallet.a(wallet2.cpp.o): In function `epee::net_utils::parse_url(std::string, epee::net_utils::http::url_content&)':
wallet2.cpp:(.text._ZN4epee9net_utils9parse_urlESsRNS0_4http11url_contentE[_ZN4epee9net_utils9parse_urlESsRNS0_4http11url_contentE]+0x34d): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
../../lib/libwallet.a(node_rpc_proxy.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&) [clone .part.383]':
node_rpc_proxy.cpp:(.text+0x1fb): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
../../contrib/epee/src/libepee.a(connection_basic.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&) [clone .part.122]':
connection_basic.cpp:(.text+0xeb): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
../../contrib/epee/src/libepee.a(connection_basic.cpp.o): In function `epee::net_utils::connection_basic::sleep_before_packet(unsigned long, int, int)':
connection_basic.cpp:(.text+0x1096): undefined reference to `boost::this_thread::hiden::sleep_until(timespec const&)'
../common/libcommon.a(util.cpp.o): In function `bool boost::regex_search<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::string>)':
util.cpp:(.text._ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESD_[_ZN5boost12regex_searchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsESD_]+0x123): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1000l> >(boost::chrono::duration<long, boost::ratio<1l, 1000l> > const&) [clone .part.154]':
miner.cpp:(.text+0x1db): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `void boost::this_thread::sleep_for<long, boost::ratio<1l, 1l> >(boost::chrono::duration<long, boost::ratio<1l, 1l> > const&) [clone .part.155]':
miner.cpp:(.text+0x28b): undefined reference to `boost::this_thread::hiden::sleep_for(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `boost::this_thread::sleep(boost::posix_time::ptime const&)':
miner.cpp:(.text._ZN5boost11this_thread5sleepERKNS_10posix_time5ptimeE[_ZN5boost11this_thread5sleepERKNS_10posix_time5ptimeE]+0xf4): undefined reference to `boost::this_thread::hiden::sleep_until(timespec const&)'
../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `bool boost::regex_match<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> > >(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)':
miner.cpp:(.text._ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE[_ZN5boost11regex_matchIN9__gnu_cxx17__normal_iteratorIPKcSsEESaINS_9sub_matchIS5_EEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEEEbT_SD_RNS_13match_resultsISD_T0_EERKNS_11basic_regexIT1_T2_EENS_15regex_constants12_match_flagsE]+0xe4): undefined reference to `boost::re_detail_106000::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::string>, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::string> > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::construct_init(boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags)'
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:124: recipe for target 'bin/monero-wallet-rpc' failed
make[3]: *** [bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/usr/src/monero/build/release'
CMakeFiles/Makefile2:2141: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[2]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/usr/src/monero/build/release'
Makefile:127: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/usr/src/monero/build/release'
Makefile:72: recipe for target 'release-all' failed
make: *** [release-all] Error 2

root@monero:/usr/src/monero#

``` 

# Discussion History
## moneromooo-monero | 2018-06-25T15:04:03+00:00
Did you set up the BOOST_ROOT env var properly ?

## minzak | 2018-06-25T15:42:35+00:00
As many other project, i run only this:
```
cd /usr/src
https://dl.bintray.com/boostorg/release/1.66.0/source/boost_1_66_0.tar.bz2
tar -xvf boost_1_66_0.tar
cd boost_1_66_0
./bootstrap.sh --prefix=/usr/local --with-libraries=all
./bjam install
```

And all is available at /usr/local

Can i use cmake in monero with some prefix to boost & boost source to build binary?

## moneromooo-monero | 2018-06-25T17:20:00+00:00
As I said above, BOOST_ROOT.
Or check the FindBoost.cmake file for hint variables, might be others I forget.


## minzak | 2018-06-26T10:44:40+00:00
At last.
i use: 
```
cmake -DBOOST_ROOT=/usr/local/include/boost -DBOOST_LIBRARYDIR=/usr/local/lib ..
make

```
And after it all is fine!
Also https://github.com/monero-project/monero/issues/4052 no trouble more!


# Action History
- Created by: minzak | 2018-06-25T14:23:54+00:00
- Closed at: 2018-06-26T10:44:40+00:00
