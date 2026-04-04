---
title: Continuous boost::bad_weak_ptr exception
source_url: https://github.com/monero-project/monero/issues/4991
author: ghost
assignees: []
labels:
- duplicate
created_at: '2018-12-18T12:58:22+00:00'
updated_at: '2019-03-12T09:25:43+00:00'
type: issue
status: closed
closed_at: '2018-12-18T13:25:16+00:00'
---

# Original Description
| Q             | A
| ------------- | ---
| Component | monerod
| Version  | `v.0.13.0.4-release`
| Blockchain | mainnet / fully synced

Various nodes are continuous returning the following exception stack:

```shell
2018-12-18 06:33:26.947 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<boost::bad_weak_ptr> >
2018-12-18 06:33:26.947 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2018-12-18 06:33:26.957 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1] /usr/local/bin/monerod:__wrap___cxa_throw+0x10a [0x55b4d0fee4ea]
2018-12-18 06:33:26.957 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/local/bin/monerod:void boost::throw_exception<boost::bad_weak_ptr>(boost::bad_weak_ptr const&)+0x12d [0x55b4d0cda27d]
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::crypton$
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/local/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::crypton$
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/local/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_contex$
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned l$
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::check_connection_and_handshake_wi$
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::gray_peerlist_housekeeping()+0x14$
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/local/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0xb8 [0x55b4d0e8d69$
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10] /usr/local/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote$
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11] /usr/local/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server$
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/local/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote$
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13] /usr/local/bin/monerod+0x9ff64d [0x55b4d13ce64d]
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14] /lib/x86_64-linux-gnu/libpthread.so.0+0x76db [0x7fcaffdd36db]
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7fcaffafc88f]
2018-12-18 06:33:26.958 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:172
```

# Discussion History
## moneromooo-monero | 2018-12-18T13:10:29+00:00
Continuous for a short time, or really really continuous ?

## ghost | 2018-12-18T13:15:36+00:00
> @moneromooo-monero: Continuous for a short time, or really really continuous ?

It depends. Sometimes it goes on for five times within two minutes and sometimes it takes hours.

## moneromooo-monero | 2018-12-18T13:20:36+00:00
Oh, so nowhere near continuous then.

## moneromooo-monero | 2018-12-18T13:21:14+00:00
See #4365 

+duplicate


# Action History
- Created by: ghost | 2018-12-18T12:58:22+00:00
- Closed at: 2018-12-18T13:25:16+00:00
