---
title: 'OS X Build Fails - Error: no member named ''get_block_sync_size'' in ''tests::proxy_core'''
source_url: https://github.com/monero-project/monero/issues/1154
author: monerobby
assignees: []
labels: []
created_at: '2016-09-30T23:39:01+00:00'
updated_at: '2016-10-04T22:13:31+00:00'
type: issue
status: closed
closed_at: '2016-10-04T22:13:31+00:00'
---

# Original Description
Trying to build fresh from git after successfully build just a couple weeks prior but it is now failing with this error:

`In file included from /Users/MyUser/Documents/programming/monero/monero/tests/core_proxy/core_proxy.cpp:50:
In file included from /Users/MyUser/Documents/programming/monero/monero/src/cryptonote_protocol/cryptonote_protocol_handler.h:166:
/Users/MyUser/Documents/programming/monero/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:653:41: error: no member named 'get_block_sync_size' in
      'tests::proxy_core'
      const size_t count_limit = m_core.get_block_sync_size();
                                 ~~~~~~ ^
/Users/MyUser/Documents/programming/monero/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:609:5: note: in instantiation of member function
      'cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>::request_missing_objects' requested here
    request_missing_objects(context, true);
    ^
/Users/MyUser/Documents/programming/monero/monero/src/cryptonote_protocol/cryptonote_protocol_handler.h:91:83: note: in instantiation of member function
      'cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>::handle_response_get_objects' requested here
      HANDLE_NOTIFY_T2(NOTIFY_RESPONSE_GET_OBJECTS, &cryptonote_protocol_handler::handle_response_get_objects)
                                                                                  ^
/Users/MyUser/Documents/programming/monero/monero/src/p2p/net_node.h:149:7: note: in instantiation of function template specialization
      'cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>::handle_invoke_map<cryptonote::cryptonote_connection_context>' requested here
      CHAIN_INVOKE_MAP_TO_OBJ_FORCE_CONTEXT(m_payload_handler, typename t_payload_net_handler::connection_context&)
      ^
/Users/MyUser/Documents/programming/monero/monero/contrib/epee/include/storages/levin_abstract_invoke2.h:278:17: note: expanded from macro
      'CHAIN_INVOKE_MAP_TO_OBJ_FORCE_CONTEXT'
  int res = obj.handle_invoke_map(is_notify, command, in_buff, buff_out, static_cast<context_type>(context), handled); \
                ^
/Users/MyUser/Documents/programming/monero/monero/src/p2p/net_node.h:137:5: note: in instantiation of function template specialization
      'nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<tests::proxy_core>
      >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >' requested here
    CHAIN_LEVIN_INVOKE_MAP2(p2p_connection_context); //move levin_commands_handler interface invoke(...) callbacks into invoke map
    ^
/Users/MyUser/Documents/programming/monero/monero/contrib/epee/include/storages/levin_abstract_invoke2.h:208:10: note: expanded from macro 'CHAIN_LEVIN_INVOKE_MAP2'
  return handle_invoke_map(false, command, in_buff, buff_out, context, handled); \
         ^
/Users/MyUser/Documents/programming/monero/monero/src/p2p/net_node.h:85:5: note: in instantiation of member function
      'nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<tests::proxy_core> >::invoke' requested here
    node_server(t_payload_net_handler& payload_handler)
    ^
/Users/MyUser/Documents/programming/monero/monero/tests/core_proxy/core_proxy.cpp:107:88: note: in instantiation of member function
      'nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<tests::proxy_core> >::node_server' requested here
  nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<tests::proxy_core> > p2psrv {
                                                                                       ^
64 warnings and 1 error generated.
make[3]: *** [tests/core_proxy/CMakeFiles/core_proxy.dir/core_proxy.cpp.o] Error 1
make[2]: *** [tests/core_proxy/CMakeFiles/core_proxy.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release-all] Error 2`


# Discussion History
## moneromooo-monero | 2016-10-01T09:11:21+00:00
https://github.com/monero-project/monero/pull/1159


# Action History
- Created by: monerobby | 2016-09-30T23:39:01+00:00
- Closed at: 2016-10-04T22:13:31+00:00
