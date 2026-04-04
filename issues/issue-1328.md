---
title: Master doesn't compile for me
source_url: https://github.com/monero-project/monero/issues/1328
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-11-12T05:05:53+00:00'
updated_at: '2016-11-13T13:53:47+00:00'
type: issue
status: closed
closed_at: '2016-11-13T13:53:47+00:00'
---

# Original Description
~/monero_head$ git log
commit 6a2bb62827d778b299e5bd34e4d33670b33d63cf
Merge: 524ff61 358e068



[ 72%] Building CXX object tests/core_proxy/CMakeFiles/core_proxy.dir/core_proxy.cpp.o
In file included from /home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.h:169:0,
                 from /home/user/monero_head/tests/core_proxy/core_proxy.cpp:50:
/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘cryptonote::t_cryptonote_protocol_handl
er<t_core>::relay_block(cryptonote::NOTIFY_NEW_BLOCK::request&, cryptonote::cryptonote_connection_context&)::<lambda(cryptonote::t_cryptonote_p
rotocol_handler<t_core>::connection_context&, nodetool::peerid_type, uint32_t)> [with t_core = tests::proxy_core; cryptonote::t_cryptonote_prot
ocol_handler<t_core>::connection_context = cryptonote::cryptonote_connection_context; nodetool::peerid_type = long unsigned int; uint32_t = uns
igned int]’:
/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.inl:1096:46:   required from ‘struct cryptonote::t_cryptonote_pro
tocol_handler<t_core>::relay_block(cryptonote::NOTIFY_NEW_BLOCK::request&, cryptonote::cryptonote_connection_context&) [with t_core = tests::pr
oxy_core]::<lambda(cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>::connection_context&, nodetool::peerid_type, uint32_t)>’
/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.inl:1096:5:   required from ‘bool cryptonote::t_cryptonote_protoc
ol_handler<t_core>::relay_block(cryptonote::NOTIFY_NEW_BLOCK::request&, cryptonote::cryptonote_connection_context&) [with t_core = tests::proxy
_core]’
/home/user/monero_head/tests/core_proxy/core_proxy.cpp:278:1:   required from here
/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.inl:1098:31: error: ‘class tests::proxy_core’ has no member named ‘get_testnet’
       if(m_core.get_testnet() && support_flags & P2P_SUPPORT_FLAG_FLUFFY_BLOCKS)
                               ^
/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘int cryptonote::t_cryptonote_protocol_handler<t_core>::handle_notify_new_fluffy_block(int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&) [with t_core = tests::proxy_core]’:
/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.h:94:7:   required from ‘int cryptonote::t_cryptonote_protocol_handler<t_core>::handle_invoke_map(bool, int, const string&, std::__cxx11::string&, t_context&, bool&) [with t_context = cryptonote::cryptonote_connection_context; t_core = tests::proxy_core; std::__cxx11::string = std::__cxx11::basic_string<char>]’
/home/user/monero_head/src/p2p/net_node.h:151:7:   required from ‘int nodetool::node_server<t_payload_net_handler>::handle_invoke_map(bool, int, const string&, std::__cxx11::string&, t_context&, bool&) [with t_context = nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>; t_payload_net_handler = cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>; std::__cxx11::string = std::__cxx11::basic_string<char>]’
/home/user/monero_head/src/p2p/net_node.h:138:5:   required from ‘int nodetool::node_server<t_payload_net_handler>::invoke(int, const string&, std::__cxx11::string&, nodetool::node_server<t_payload_net_handler>::p2p_connection_context&) [with t_payload_net_handler = cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>; std::__cxx11::string = std::__cxx11::basic_string<char>; nodetool::node_server<t_payload_net_handler>::p2p_connection_context = nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>; typename t_payload_net_handler::connection_context = cryptonote::cryptonote_connection_context]’
/home/user/monero_head/tests/core_proxy/core_proxy.cpp:278:1:   required from here
/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.inl:477:14: error: ‘class tests::proxy_core’ has no member named ‘get_pool_transaction’
           if(!m_core.get_pool_transaction(tx_hash, tx))
              ^
/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.inl:533:9: error: ‘class tests::proxy_core’ has no member named  get_pool_transaction’
         if(m_core.get_pool_transaction(tx_hash, tx))

/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of ‘int cryptonote::t_cryptonote_protocol_handler<t_core>::handle_request_fluffy_missing_tx(int, cryptonote::NOTIFY_REQUEST_FLUFFY_MISSING_TX::request&, cryptonote::cryptonote_connection_context&) [with t_core = tests::proxy_core]’:
/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.h:95:7:   required from ‘int cryptonote::t_cryptonote_protocol_handler<t_core>::handle_invoke_map(bool, int, const string&, std::__cxx11::string&, t_context&, bool&) [with t_context = cryptonote::cryptonote_connection_context; t_core = tests::proxy_core; std::__cxx11::string = std::__cxx11::basic_string<char>]’
/home/user/monero_head/src/p2p/net_node.h:151:7:   required from ‘int nodetool::node_server<t_payload_net_handler>::handle_invoke_map(bool, int, const string&, std::__cxx11::string&, t_context&, bool&) [with t_context = nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>; t_payload_net_handler = cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>; std::__cxx11::string = std::__cxx11::basic_string<char>]’
/home/user/monero_head/src/p2p/net_node.h:138:5:   required from ‘int nodetool::node_server<t_payload_net_handler>::invoke(int, const string&, std::__cxx11::string&, nodetool::node_server<t_payload_net_handler>::p2p_connection_context&) [with t_payload_net_handler = cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>; std::__cxx11::string = std::__cxx11::basic_string<char>; nodetool::node_server<t_payload_net_handler>::p2p_connection_context = nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>; typename t_payload_net_handler::connection_context = cryptonote::cryptonote_connection_context]’
/home/user/monero_head/tests/core_proxy/core_proxy.cpp:278:1:   required from here
/home/user/monero_head/src/cryptonote_protocol/cryptonote_protocol_handler.inl:623:8: error: ‘class tests::proxy_core’ has no member named  get_blocks’
     if(!m_core.get_blocks(arg.current_blockchain_height - 1, 1, local_blocks, local_txs))
        ^
In file included from /usr/include/boost/system/error_code.hpp:22:0,
                 from /usr/include/boost/system/system_error.hpp:14,
                 from /usr/include/boost/thread/exceptions.hpp:22,
                 from /usr/include/boost/thread/pthread/thread_data.hpp:10,
                 from /usr/include/boost/thread/thread_only.hpp:17,
                 from /usr/include/boost/thread/thread.hpp:12,
                 from /usr/include/boost/thread.hpp:13,
                 from /home/user/monero_head/contrib/epee/include/misc_log_ex.h:43,
                 from /home/user/monero_head/contrib/epee/include/include_base_utils.h:32,
                 from /home/user/monero_head/tests/core_proxy/core_proxy.cpp:35:
/usr/include/c++/5/functional:2246:7: error: ‘std::function<_Res(_ArgTypes ...)>::function(_Functor) [with _Functor = cryptonote::t_cryptonote_protocol_handler<t_core>::relay_block(cryptonote::NOTIFY_NEW_BLOCK::request&, cryptonote::cryptonote_connection_context&) [with t_core = tests::proxy_core]::<lambda(cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>::connection_context&, nodetool::peerid_type, uint32_t)>; <template-parameter-2-2> = void; <template-parameter-2-3> = void; _Res = bool; _ArgTypes = {cryptonote::cryptonote_connection_context&, long unsigned int, unsigned int}]’, declared using local type ‘cryptonote::t_cryptonote_protocol_handler<t_core>::relay_block(cryptonote::NOTIFY_NEW_BLOCK::request&, cryptonote::cryptonote_connection_context&) [with t_core = tests::proxy_core]::<lambda(cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>::connection_context&, nodetool::peerid_type, uint32_t)>’, is used but never defined [-fpermissive]
       function<_Res(_ArgTypes...)>::
       ^
tests/core_proxy/CMakeFiles/core_proxy.dir/build.make:62: recipe for target 'tests/core_proxy/CMakeFiles/core_proxy.dir/core_proxy.cpp.o' failed
make[3]: *** [tests/core_proxy/CMakeFiles/core_proxy.dir/core_proxy.cpp.o] Error 1
make[3]: Leaving directory '/home/user/monero_head/build/release'
CMakeFiles/Makefile2:2298: recipe for target 'tests/core_proxy/CMakeFiles/core_proxy.dir/all' failed
make[2]: *** [tests/core_proxy/CMakeFiles/core_proxy.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
/home/user/monero_head/src/crypto/slow-hash.c: In function ‘cn_slow_hash’:
/home/user/monero_head/src/crypto/oaes_lib.c:944:2: warning: ‘aes_ctx’ may be used uninitialized in this function [-Wmaybe-uninitialized]
  free( *_ctx );
  ^
/home/user/monero_head/src/crypto/slow-hash.c:532:15: note: ‘aes_ctx’ was declared here
     oaes_ctx *aes_ctx;
               ^
make[3]: Leaving directory '/home/user/monero_head/build/release'
[ 72%] Built target performance_tests
make[2]: Leaving directory '/home/user/monero_head/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/user/monero_head/build/release'
Makefile:58: recipe for target 'release-all' failed
make: *** [release-all] Error 2


# Discussion History
## Gingeropolous | 2016-11-12T05:35:17+00:00
this built fine: 0e418d2 


## anonimal | 2016-11-12T06:02:39+00:00
Also reported in the [AUR](https://aur.archlinux.org/packages/bitmonero-git/).


## moneromooo-monero | 2016-11-12T10:20:16+00:00
https://github.com/monero-project/monero/pull/1325


## iDunk5400 | 2016-11-12T11:50:07+00:00
#1325 fixes the issue.

A workaround is to run make release instead of just running make.


## Gingeropolous | 2016-11-13T13:53:47+00:00
Thanks. Once again I wield my powerful "close and comment because I made the issue" superpowers! 


# Action History
- Created by: Gingeropolous | 2016-11-12T05:05:53+00:00
- Closed at: 2016-11-13T13:53:47+00:00
