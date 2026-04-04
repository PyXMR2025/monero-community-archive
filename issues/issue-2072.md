---
title: command_parser_executor.cpp.o variable 'it' set but not used
source_url: https://github.com/monero-project/monero/issues/2072
author: ghost
assignees: []
labels: []
created_at: '2017-06-04T21:41:09+00:00'
updated_at: '2017-06-04T21:44:15+00:00'
type: issue
status: closed
closed_at: '2017-06-04T21:44:15+00:00'
---

# Original Description
Ubuntu 16.04, GCC 6.3.0

```
[ 86%] Building CXX object src/daemon/CMakeFiles/daemon.dir/command_parser_executor.cpp.o
In file included from /home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization.h:33:0,
                 from /home/nodey/monero/src/cryptonote_basic/cryptonote_basic.h:46,
                 from /home/nodey/monero/src/common/dns_utils.h:32,
                 from /home/nodey/monero/src/daemon/command_parser_executor.cpp:29:
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h: In instantiation of ‘bool epee::serialization::serialize_stl_container_pod_val_as_blob(const stl_container&, t_storage&, typename t_storage::hsection, const char*) [with stl_container = std::__cxx11::list<crypto::hash>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’:
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:300:76:   required from ‘static bool epee::serialization::selector<true>::serialize_stl_container_pod_val_as_blob(const t_type&, t_storage&, typename t_storage::hsection, const char*) [with t_type = std::__cxx11::list<crypto::hash>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:170:9:   required from ‘static bool cryptonote::COMMAND_RPC_GET_HASHES_FAST::response::serialize_map(this_type&, t_storage&, typename t_storage::hsection) [with bool is_store = true; this_type = const cryptonote::COMMAND_RPC_GET_HASHES_FAST::response; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:169:7:   required from ‘bool cryptonote::COMMAND_RPC_GET_HASHES_FAST::response::store(t_storage&, typename t_storage::hsection) const [with t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/contrib/epee/include/storages/portable_storage_template_helper.h:111:7:   required from ‘bool epee::serialization::store_t_to_binary(t_struct&, std::__cxx11::string&, size_t) [with t_struct = cryptonote::COMMAND_RPC_GET_HASHES_FAST::response; std::__cxx11::string = std::__cxx11::basic_string<char>; size_t = long unsigned int]’
/home/nodey/monero/src/rpc/core_rpc_server.h:78:7:   required from ‘bool cryptonote::core_rpc_server::handle_http_request_map(const epee::net_utils::http::http_request_info&, epee::net_utils::http::http_response_info&, t_context&) [with t_context = epee::net_utils::connection_context_base]’
/home/nodey/monero/src/rpc/core_rpc_server.h:72:5:   required from here
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:129:46: warning: variable ‘it’ set but not used [-Wunused-but-set-variable]
       typename stl_container::const_iterator it = container.begin();
                                              ^~
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h: In instantiation of ‘bool epee::serialization::serialize_stl_container_pod_val_as_blob(const stl_container&, t_storage&, typename t_storage::hsection, const char*) [with stl_container = std::__cxx11::list<cryptonote::COMMAND_RPC_GET_RANDOM_RCT_OUTPUTS::out_entry>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’:
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:300:76:   required from ‘static bool epee::serialization::selector<true>::serialize_stl_container_pod_val_as_blob(const t_type&, t_storage&, typename t_storage::hsection, const char*) [with t_type = std::__cxx11::list<cryptonote::COMMAND_RPC_GET_RANDOM_RCT_OUTPUTS::out_entry>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:446:9:   required from ‘static bool cryptonote::COMMAND_RPC_GET_RANDOM_RCT_OUTPUTS::response::serialize_map(this_type&, t_storage&, typename t_storage::hsection) [with bool is_store = true; this_type = const cryptonote::COMMAND_RPC_GET_RANDOM_RCT_OUTPUTS::response; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:445:7:   required from ‘bool cryptonote::COMMAND_RPC_GET_RANDOM_RCT_OUTPUTS::response::store(t_storage&, typename t_storage::hsection) const [with t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/contrib/epee/include/storages/portable_storage_template_helper.h:111:7:   required from ‘bool epee::serialization::store_t_to_binary(t_struct&, std::__cxx11::string&, size_t) [with t_struct = cryptonote::COMMAND_RPC_GET_RANDOM_RCT_OUTPUTS::response; std::__cxx11::string = std::__cxx11::basic_string<char>; size_t = long unsigned int]’
/home/nodey/monero/src/rpc/core_rpc_server.h:82:7:   required from ‘bool cryptonote::core_rpc_server::handle_http_request_map(const epee::net_utils::http::http_request_info&, epee::net_utils::http::http_response_info&, t_context&) [with t_context = epee::net_utils::connection_context_base]’
/home/nodey/monero/src/rpc/core_rpc_server.h:72:5:   required from here
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:129:46: warning: variable ‘it’ set but not used [-Wunused-but-set-variable]
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h: In instantiation of ‘bool epee::serialization::serialize_stl_container_pod_val_as_blob(const stl_container&, t_storage&, typename t_storage::hsection, const char*) [with stl_container = std::vector<crypto::hash>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’:
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:300:76:   required from ‘static bool epee::serialization::selector<true>::serialize_stl_container_pod_val_as_blob(const t_type&, t_storage&, typename t_storage::hsection, const char*) [with t_type = std::vector<crypto::hash>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:1045:9:   required from ‘static bool cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_HASHES::response::serialize_map(this_type&, t_storage&, typename t_storage::hsection) [with bool is_store = true; this_type = const cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_HASHES::response; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:1043:7:   required from ‘bool cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_HASHES::response::store(t_storage&, typename t_storage::hsection) const [with t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/contrib/epee/include/storages/portable_storage_template_helper.h:65:7:   required from ‘bool epee::serialization::store_t_to_json(t_struct&, std::__cxx11::string&, size_t, bool) [with t_struct = cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_HASHES::response; std::__cxx11::string = std::__cxx11::basic_string<char>; size_t = long unsigned int]’
/home/nodey/monero/src/rpc/core_rpc_server.h:95:7:   required from ‘bool cryptonote::core_rpc_server::handle_http_request_map(const epee::net_utils::http::http_request_info&, epee::net_utils::http::http_response_info&, t_context&) [with t_context = epee::net_utils::connection_context_base]’
/home/nodey/monero/src/rpc/core_rpc_server.h:72:5:   required from here
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:129:46: warning: variable ‘it’ set but not used [-Wunused-but-set-variable]
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h: In instantiation of ‘bool epee::serialization::serialize_stl_container_pod_val_as_blob(const stl_container&, t_storage&, typename t_storage::hsection, const char*) [with stl_container = std::__cxx11::list<cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::out_entry>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’:
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:300:76:   required from ‘static bool epee::serialization::selector<true>::serialize_stl_container_pod_val_as_blob(const t_type&, t_storage&, typename t_storage::hsection, const char*) [with t_type = std::__cxx11::list<cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::out_entry>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:315:9:   required from ‘static bool cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::outs_for_amount::serialize_map(this_type&, t_storage&, typename t_storage::hsection) [with bool is_store = true; this_type = const cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::outs_for_amount; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:313:7:   required from ‘bool cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::outs_for_amount::store(t_storage&, typename t_storage::hsection) const [with t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:170:11:   required from ‘bool epee::serialization::serialize_stl_container_t_obj(const stl_container&, t_storage&, typename t_storage::hsection, const char*) [with stl_container = std::vector<cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::outs_for_amount>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:262:45:   [ skipping 2 instantiation contexts, use -ftemplate-backtrace-limit=0 to disable ]
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:294:28:   required from ‘static bool epee::serialization::selector<true>::serialize(const t_type&, t_storage&, typename t_storage::hsection, const char*) [with t_type = std::vector<cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::outs_for_amount>; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:324:9:   required from ‘static bool cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::response::serialize_map(this_type&, t_storage&, typename t_storage::hsection) [with bool is_store = true; this_type = const cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::response; t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/src/rpc/core_rpc_server_commands_defs.h:323:7:   required from ‘bool cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::response::store(t_storage&, typename t_storage::hsection) const [with t_storage = epee::serialization::portable_storage; typename t_storage::hsection = epee::serialization::section*]’
/home/nodey/monero/contrib/epee/include/storages/portable_storage_template_helper.h:111:7:   required from ‘bool epee::serialization::store_t_to_binary(t_struct&, std::__cxx11::string&, size_t) [with t_struct = cryptonote::COMMAND_RPC_GET_RANDOM_OUTPUTS_FOR_AMOUNTS::response; std::__cxx11::string = std::__cxx11::basic_string<char>; size_t = long unsigned int]’
/home/nodey/monero/src/rpc/core_rpc_server.h:80:7:   required from ‘bool cryptonote::core_rpc_server::handle_http_request_map(const epee::net_utils::http::http_request_info&, epee::net_utils::http::http_response_info&, t_context&) [with t_context = epee::net_utils::connection_context_base]’
/home/nodey/monero/src/rpc/core_rpc_server.h:72:5:   required from here
/home/nodey/monero/contrib/epee/include/serialization/keyvalue_serialization_overloads.h:129:46: warning: variable ‘it’ set but not used [-Wunused-but-set-variable]
```

# Discussion History
# Action History
- Created by: ghost | 2017-06-04T21:41:09+00:00
- Closed at: 2017-06-04T21:44:15+00:00
