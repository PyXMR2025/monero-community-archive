---
title: 'bitmonerod: boost::archive::archive_exception'
source_url: https://github.com/monero-project/monero/issues/1091
author: radfish
assignees: []
labels: []
created_at: '2016-09-18T06:41:05+00:00'
updated_at: '2016-09-18T18:11:59+00:00'
type: issue
status: closed
closed_at: '2016-09-18T18:11:59+00:00'
---

# Original Description
bitmonerod f5c7905 crashed with this in the log:

The box ran out of space at some point, not sure whether it is related. No core was generated unfortunately.

```
2016-Sep-07 06:21:48.024709 [P2P5]    17                  0xb6e9fbc8 clone + 0x78
2016-Sep-07 06:31:42.715770 [P2P1]Exception: boost::archive::archive_exception
2016-Sep-07 06:31:42.715961 [P2P1]Unwinded call stack:
2016-Sep-07 06:31:42.717915 [P2P1]     1                  0x331618 __cxa_throw + 0x84
2016-Sep-07 06:31:42.728974 [P2P1]     2                  0x93048 epee::json_rpc::response<cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM::response, epee::json_rpc::error>::~response() + 0x0
2016-Sep-07 06:31:42.783800 [P2P1]Exception: std::bad_cast
2016-Sep-07 06:31:42.784000 [P2P1]Unwinded call stack:
2016-Sep-07 06:31:42.786205 [P2P1]     1                  0x331618 __cxa_throw + 0x84
2016-Sep-07 06:31:43.244932 [P2P1]     2                  0xb69ba1b0 std::__throw_bad_cast() + 0x3c
2016-Sep-07 06:31:43.281924 [P2P1]     3                  0xb69f2db0 std::basic_filebuf<char, std::char_traits<char> >::_M_convert_to_external(char*, int) + 0x19c
2016-Sep-07 06:31:43.301378 [P2P1]     4                  0xb69f3198 std::basic_filebuf<char, std::char_traits<char> >::overflow(int) + 0xe8
2016-Sep-07 06:31:43.312512 [P2P1]     5                  0xb69f2f74 std::basic_filebuf<char, std::char_traits<char> >::_M_terminate_output() + 0x138
2016-Sep-07 06:31:43.323525 [P2P1]     6                  0xb69f5e24 std::basic_filebuf<char, std::char_traits<char> >::close() + 0x2c
2016-Sep-07 06:31:43.334711 [P2P1]     7                  0xb69f8114 std::basic_ofstream<char, std::char_traits<char> >::~basic_ofstream() + 0x3c
2016-Sep-07 06:31:43.336747 [P2P1]     8                  0xe2ef4 nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::store_config() + 0x378
2016-Sep-07 06:31:43.338872 [P2P1]     9                  0xdff34 nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() + 0xb0
2016-Sep-07 06:31:43.340841 [P2P1]    10                  0x112ed4 epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) + 0x20
2016-Sep-07 06:31:43.342856 [P2P1]    11                  0xfa85c boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::ta
```


# Discussion History
## moneromooo-monero | 2016-09-18T09:04:42+00:00
The second one looks like it's failing to save the p2p state file, and so would be expected if you were ENOSPC.
The first one is odd. It may be misreported. P2P threads should not access the histogram stuff anyway.


## radfish | 2016-09-18T18:11:59+00:00
Ok, ENOSPC, then not worth digging.


# Action History
- Created by: radfish | 2016-09-18T06:41:05+00:00
- Closed at: 2016-09-18T18:11:59+00:00
