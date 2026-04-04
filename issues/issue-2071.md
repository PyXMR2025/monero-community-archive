---
title: epee keyvalue_serialization_overloads.h variable 'it' set but not used
source_url: https://github.com/monero-project/monero/issues/2071
author: ghost
assignees: []
labels: []
created_at: '2017-06-04T21:14:25+00:00'
updated_at: '2017-06-25T21:51:52+00:00'
type: issue
status: closed
closed_at: '2017-06-25T21:51:52+00:00'
---

# Original Description
Ubuntu 16.04, GCC 6.3.0

```
[ 69%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
In file included from /home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization.h:33:0,
                 from /home/nodey/monero/src/cryptonote_basic/cryptonote_basic.h:46,
                 from /home/nodey/monero/src/cryptonote_basic/account.h:33,
                 from /home/nodey/monero/src/wallet/wallet2.h:42,
                 from /home/nodey/monero/src/wallet/wallet2.cpp:40:
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h: In instantiation of ‘bool epee::serialization::serialize_stl_container_pod_val_as_blob(const stl_container&, t_storage&, typename t_storage::hsection, const char*) [with stl_container = std::__cxx11::list<crypto::hash>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’:
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:300:76:   required from ‘static bool epee::serialization::selector<true>::serialize_stl_container_pod_val_as_blob(const t_type&, t_storage&, typename t_storage::hsection, const char*) [with t_type = std::__cxx11::list<crypto::hash>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:85:9:   required from ‘static bool cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::request::serialize_map(this_type&, t_storage&, typename t_storage::hsection) [with bool is_store = true; this_type = const cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::request; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:84:7:   required from ‘bool cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::request::store(t_storage&, typename t_storage::hsection) const [with t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/contrib/epee/include/storages/portable_storage_template_helper.h:111:7:   required from ‘bool epee::serialization::store_t_to_binary(t_struct&, std::__cxx11::string&, size_t) [with t_struct = const cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::request; std::__cxx11::string = std::__cxx11::basic_string<char>; size_t = long unsigned int]’
/home/nodey/monero/contrib/epee/include/storages/http_abstract_invoke.h:75:43:   required from ‘bool epee::net_utils::invoke_http_bin(boost::string_ref, const t_request&, t_response&, t_transport&, std::chrono::milliseconds, boost::string_ref) [with t_request = cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::request; t_response = cryptonote::COMMAND_RPC_GET_BLOCKS_FAST::response; t_transport = epee::net_utils::http::http_simple_client; boost::string_ref = boost::basic_string_ref<char, std::char_traits<char> >; std::chrono::milliseconds = std::chrono::duration<long int, std::ratio<1l, 1000l> >]’
/home/nodey/monero/src/wallet/wallet2.cpp:1212:93:   required from here
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:129:46: warning: variable ‘it’ set but not used [-Wunused-but-set-variable]
       typename stl_container::const_iterator it = container.begin();
                                              ^~
```

Also appears elsewhere during compilation.

# Discussion History
## moneromooo-monero | 2017-06-09T17:48:30+00:00
Indeed, it appears useless, and can be removed safely.

## ghost | 2017-06-25T21:51:52+00:00
Thanks @binaryFate - will close this one now

# Action History
- Created by: ghost | 2017-06-04T21:14:25+00:00
- Closed at: 2017-06-25T21:51:52+00:00
