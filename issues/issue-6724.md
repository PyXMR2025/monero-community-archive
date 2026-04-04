---
title: Monerod is constantly terminating
source_url: https://github.com/monero-project/monero/issues/6724
author: normoes
assignees: []
labels: []
created_at: '2020-07-27T15:31:12+00:00'
updated_at: '2020-08-09T00:11:37+00:00'
type: issue
status: closed
closed_at: '2020-07-30T10:54:59+00:00'
---

# Original Description
I run `monerod` (`v0.16.0.1`) like this:
```
monerod --data-dir /monero --rpc-ssl disabled --no-zmq --rpc-restricted-bind-port 18081--log-level 3 --max-log-file-size 5242880 --max-log-files 3 --confirm-external-bind --non-interactive --rpc-bind-ip 0.0.0.0 --rpc-bind-port 18090 --p2p-bind-ip 0.0.0.0 --p2p-bind-port 18080 --check-updates disabled
```

Requests from `162.250.189.42` seem to take `monerod` down all the time - It is constantly restarting. It only takes a few seconds to go down.

This is the error log when started with `--restricted-rpc`
```
877 2020-07-27 14:46:59.994 [RPC0]  DEBUG   net contrib/epee/include/net/abstract_tcp_server2.inl:1274  handle_accept
878 2020-07-27 14:46:59.994 [RPC0]  DEBUG   net contrib/epee/include/net/abstract_tcp_server2.inl:1298  New server for RPC connections, SSL disabled
879 2020-07-27 14:46:59.994 [RPC0]  DEBUG   net contrib/epee/include/net/abstract_tcp_server2.inl:914   set m_connection_type = RPC
880 2020-07-27 14:46:59.994 [RPC0]  DEBUG   net.conn    contrib/epee/src/connection_basic.cpp:153   Spawned connection #5 to 0.0.0.0 currently we have sockets count:2
881 2020-07-27 14:46:59.994 [RPC0]  DEBUG   net contrib/epee/include/net/abstract_tcp_server2.inl:111   test, connection constructor set m_connection_type=1
882 2020-07-27 14:46:59.994 [RPC0]  TRACE   net contrib/epee/include/net/abstract_tcp_server2.inl:191   [sock 0x7efc600115e0] new connection from 162.250.189.42:56892 INC to 172.17.0.2:18081, total sockets objects 2
883 2020-07-27 14:46:59.994 [RPC0]  TRACE   net contrib/epee/include/net/abstract_tcp_server2.inl:740   New connection from host 162.250.189.42: 0
884 2020-07-27 14:46:59.994 [RPC0]  TRACE   net contrib/epee/include/net/abstract_tcp_server2.inl:757   Setting 00:00:10 expiry
885 2020-07-27 14:46:59.994 [RPC0]  DEBUG   net contrib/epee/include/net/abstract_tcp_server2.inl:328    connection type RPC 172.17.0.2:18081 <--> 162.250.189.42:56892 (via 162.250.189.42:56892)
886 2020-07-27 14:46:59.995 [RPC1]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:172    Moving counter buffer by 1 second 0 < 526 (last time 0)
887 2020-07-27 14:46:59.995 [RPC1]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:208    Throttle throttle_speed_in: packet of ~276b  (from 276 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [276 0 0 0 0 0 0 0 0 0 ]
888 2020-07-27 14:46:59.995 [RPC1]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:208    Throttle <<< global-IN: packet of ~276b  (from 276 b) Speed AVG= 635[w=3.68]  635[w=3.68] /  Limit=8192 KiB/sec  [319 1912822 404146 51134 26540 0 0 0 0 0 ]
889 2020-07-27 14:46:59.995 [RPC1]  ERROR   net.http    contrib/epee/include/net/http_protocol_handler.inl:387  [162.250.189.42:56892 INC] simple_http_connection_handler<t_connection_context>::handle_invoke_query_line(): Failed to match first line: !�
890 2020-07-27 14:46:59.995 [RPC1]  INFO    stacktrace  src/common/stack_trace.cpp:133  Exception: std::runtime_error
891 2020-07-27 14:46:59.995 [RPC1]  INFO    stacktrace  src/common/stack_trace.cpp:134  Unwound call stack:

```

This is the error log when started with `--rpc-restricted-bind-port 18081`:
```
2020-07-27 15:20:50.259	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1274	handle_accept
2020-07-27 15:20:50.259	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1298	New server for RPC connections, SSL disabled
2020-07-27 15:20:50.259	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:914	set m_connection_type = RPC 
2020-07-27 15:20:50.259	[RPC1]	DEBUG	net.conn	contrib/epee/src/connection_basic.cpp:153	Spawned connection #48 to 0.0.0.0 currently we have sockets count:4
2020-07-27 15:20:50.259	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:111	test, connection constructor set m_connection_type=1
2020-07-27 15:20:50.259	[RPC1]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:191	[sock 0x7f03800184a0] new connection from 162.250.189.42:59564 INC to 172.17.0.2:18081, total sockets objects 4
2020-07-27 15:20:50.259	[RPC1]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:740	New connection from host 162.250.189.42: 0
2020-07-27 15:20:50.259	[RPC1]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:757	Setting 00:00:10 expiry
2020-07-27 15:20:50.259	[RPC1]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:328	 connection type RPC 172.17.0.2:18081 <--> 162.250.189.42:59564 (via 162.250.189.42:59564)
2020-07-27 15:20:50.260	[RPC0]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:172	Moving counter buffer by 1 second 0 < 2556 (last time 0)
2020-07-27 15:20:50.260	[RPC0]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:208	Throttle throttle_speed_in: packet of ~276b  (from 276 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [276 0 0 0 0 0 0 0 0 0 ]
2020-07-27 15:20:50.260	[RPC0]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:208	Throttle <<< global-IN: packet of ~276b  (from 276 b) Speed AVG=4113[w=9.447] 4113[w=9.447] /  Limit=8192 KiB/sec  [1086478 7154792 5906854 4342235 6176347 6652998 4670967 3149403 29809 622497 ]
2020-07-27 15:20:50.260	[RPC0]	ERROR	net.http	contrib/epee/include/net/http_protocol_handler.inl:387	[162.250.189.42:59564 INC] simple_http_connection_handler<t_connection_context>::handle_invoke_query_line(): Failed to match first line: !�
2020-07-27 15:20:50.260	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-07-27 15:20:50.260	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-07-27 15:20:50.265	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x111) [0x558a6169cca1]:__wrap___cxa_throw+0x111) [0x558a6169cca1]
2020-07-27 15:20:50.265	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] monerod(+0x471b2e) [0x558a61221b2e] 
2020-07-27 15:20:50.265	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x123) [0x558a61b96493]:_ZN2el4base26DefaultLogDispatchCallback8dispatchEONSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES8_S8_+0x123) [0x558a61b96493]
2020-07-27 15:20:50.265	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x611) [0x558a61b96d91]:_ZN2el4base26DefaultLogDispatchCallback6handleEPKNS_15LogDispatchDataE+0x611) [0x558a61b96d91]
2020-07-27 15:20:50.265	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x15e) [0x558a61b97ade]:_ZN2el4base13LogDispatcher8dispatchEv+0x15e) [0x558a61b97ade]
2020-07-27 15:20:50.265	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x1c7) [0x558a61b97eb7]:_ZN2el4base6Writer15triggerDispatchEv+0x1c7) [0x558a61b97eb7]
2020-07-27 15:20:50.265	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x238) [0x558a61b98398]:_ZN2el4base6Writer15processDispatchEv+0x238) [0x558a61b98398]
2020-07-27 15:20:50.265	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x3d7) [0x558a612eb507]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE24handle_invoke_query_lineEv+0x3d7) [0x558a612eb507]
2020-07-27 15:20:50.265	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x4d5) [0x558a612ed6c5]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE14handle_buff_inERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x4d5) [0x558a612ed6c5]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x40) [0x558a612edc50]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE11handle_recvEPKvm+0x40) [0x558a612edc50]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x1b6) [0x558a612ede76]:_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE11handle_readERKN5boost6system10error_codeEm+0x1b6) [0x558a612ede76]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x83) [0x558a612b7953]:_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSA_4http19http_custom_handlerINSA_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISG_EEEEPFNS_3argILi1EEEvEPFNSR_ILi2EEEvEEEEESI_mEEEEvRPNS2_11strand_implERT_+0x83) [0x558a612b7953]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x5e) [0x558a612b7c7e]:_ZN5boost4asio6detail15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSA_4http19http_custom_handlerINSA_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISG_EEEEPFNS_3argILi1EEEvEPFNSR_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEclISI_mEEvRKT_RKT0_+0x5e) [0x558a612b7c7e]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x2a0) [0x558a612bf800]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSE_4http19http_custom_handlerINSE_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESM_mEES13_EEEEvRPNS2_11strand_implERT_+0x2a0) [0x558a612bf800]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x2b1) [0x558a612c4cf1]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_4http19http_custom_handlerINSC_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISI_EEEEPFNS_3argILi1EEEvEPFNST_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEENS1_18io_object_executorINS0_8executorEEEE11do_completeEPvPNS1_19scheduler_operationESM_m+0x2b1) [0x558a612c4cf1]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16]  0x1d5) [0x558a612755b5]:_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPvPNS1_19scheduler_operationERKNS_6system10error_codeEm+0x1d5) [0x558a612755b5]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17]  0x410) [0x558a61275c50]:_ZN5boost4asio6detail9scheduler10do_run_oneERNS1_27conditionally_enabled_mutex11scoped_lockERNS1_21scheduler_thread_infoERKNS_6system10error_codeE+0x410) [0x558a61275c50]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18]  0xe9) [0x558a6127a849]:_ZN5boost4asio6detail9scheduler3runERNS_6system10error_codeE+0xe9) [0x558a6127a849]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19]  0x1c5) [0x558a61283155]:_ZN4epee9net_utils18boosted_tcp_serverINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE13worker_threadEv+0x1c5) [0x558a61283155]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] monerod(+0xc27d2a) [0x558a619d7d2a] 
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0x7fa3) [0x7f1b99f15fa3]:_64-linux-gnu/libpthread.so.0(+0x7fa3) [0x7f1b99f15fa3]
2020-07-27 15:20:50.266	[RPC0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22]  0x3f) [0x7f1b99e464cf]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f1b99e464cf]
```

I have that for some time now. it is running in a docker container, so I am restricted somehow when debugging.

# Discussion History
## normoes | 2020-07-27T19:54:51+00:00
This seems to be the cause:
```
2020-07-27 19:53:09.862	[RPC1]	ERROR	net.http	contrib/epee/include/net/http_protocol_handler.inl:387	[162.250.189.42:57364 INC] simple_http_connection_handler<t_connection_context>::handle_invoke_query_line(): Failed to match first line: !�

```

This is then followed by a runtime error:
```
2020-07-27 19:53:09.862	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-07-27 19:53:09.862	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x111) [0x5619241b6ca1]:__wrap___cxa_throw+0x111) [0x5619241b6ca1]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] monerod(+0x471b2e) [0x561923d3bb2e] 
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x123) [0x5619246b0493]:_ZN2el4base26DefaultLogDispatchCallback8dispatchEONSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES8_S8_+0x123) [0x5619246b0493]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x611) [0x5619246b0d91]:_ZN2el4base26DefaultLogDispatchCallback6handleEPKNS_15LogDispatchDataE+0x611) [0x5619246b0d91]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x15e) [0x5619246b1ade]:_ZN2el4base13LogDispatcher8dispatchEv+0x15e) [0x5619246b1ade]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x1c7) [0x5619246b1eb7]:_ZN2el4base6Writer15triggerDispatchEv+0x1c7) [0x5619246b1eb7]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x238) [0x5619246b2398]:_ZN2el4base6Writer15processDispatchEv+0x238) [0x5619246b2398]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x3d7) [0x561923e05507]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE24handle_invoke_query_lineEv+0x3d7) [0x561923e05507]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x4d5) [0x561923e076c5]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE14handle_buff_inERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x4d5) [0x561923e076c5]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x40) [0x561923e07c50]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE11handle_recvEPKvm+0x40) [0x561923e07c50]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x1b6) [0x561923e07e76]:_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE11handle_readERKN5boost6system10error_codeEm+0x1b6) [0x561923e07e76]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x83) [0x561923dd1953]:_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSA_4http19http_custom_handlerINSA_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISG_EEEEPFNS_3argILi1EEEvEPFNSR_ILi2EEEvEEEEESI_mEEEEvRPNS2_11strand_implERT_+0x83) [0x561923dd1953]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x5e) [0x561923dd1c7e]:_ZN5boost4asio6detail15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSA_4http19http_custom_handlerINSA_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISG_EEEEPFNS_3argILi1EEEvEPFNSR_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEclISI_mEEvRKT_RKT0_+0x5e) [0x561923dd1c7e]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x2a0) [0x561923dd9800]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSE_4http19http_custom_handlerINSE_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESM_mEES13_EEEEvRPNS2_11strand_implERT_+0x2a0) [0x561923dd9800]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x2b1) [0x561923ddecf1]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_4http19http_custom_handlerINSC_23connection_context_baseEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISI_EEEEPFNS_3argILi1EEEvEPFNST_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEENS1_18io_object_executorINS0_8executorEEEE11do_completeEPvPNS1_19scheduler_operationESM_m+0x2b1) [0x561923ddecf1]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16]  0x1d5) [0x561923d8f5b5]:_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPvPNS1_19scheduler_operationERKNS_6system10error_codeEm+0x1d5) [0x561923d8f5b5]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17]  0x410) [0x561923d8fc50]:_ZN5boost4asio6detail9scheduler10do_run_oneERNS1_27conditionally_enabled_mutex11scoped_lockERNS1_21scheduler_thread_infoERKNS_6system10error_codeE+0x410) [0x561923d8fc50]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18]  0xe9) [0x561923d94849]:_ZN5boost4asio6detail9scheduler3runERNS_6system10error_codeE+0xe9) [0x561923d94849]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19]  0x1c5) [0x561923d9d155]:_ZN4epee9net_utils18boosted_tcp_serverINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE13worker_threadEv+0x1c5) [0x561923d9d155]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] monerod(+0xc27d2a) [0x5619244f1d2a] 
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0x7fa3) [0x7f0b09846fa3]:_64-linux-gnu/libpthread.so.0(+0x7fa3) [0x7f0b09846fa3]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22]  0x3f) [0x7f0b097774cf]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f0b097774cf]
2020-07-27 19:53:09.868	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

## normoes | 2020-07-28T06:42:49+00:00
With log level 1, I can see:
```
	
2020-07-28T07:37:30.843+01:00
2020-07-28 06:37:30.843 E [104.248.45.85:51308 INC] simple_http_connection_handler<t_connection_context>::handle_invoke_query_line(): Failed to match first line: ?!??????B?

2020-07-28T07:37:30.844+01:00
2020-07-28 06:37:30.843 E [104.248.45.85:51308 INC] simple_http_connection_handler::handle_char_out: Error state!!!
```

## normoes | 2020-07-28T08:29:12+00:00
@moneromooo-monero 

After changing the RPC port to something else, it is working, so the cause is some kind of "malicious" or stupid request to port `18081`, that makes the RPC and monerod stop working.

## normoes | 2020-07-29T05:12:56+00:00
Same on current `master` by the way.

## moneromooo-monero | 2020-07-29T11:11:00+00:00
Do the two patches in https://github.com/moneromooo-monero/bitmonero/tree/ex help ?

## normoes | 2020-07-29T11:35:04+00:00
Thanks, building right now.

I "hope" those requests are still coming in once ready.

## normoes | 2020-07-29T11:46:23+00:00
Same error:
```
2020-07-29 11:45:29.648	[P2P0]	INFO	net.p2p	src/p2p/net_node.inl:2430	[162.218.65.82:21352 7f8873ff-2689-4c58-99e8-d2178587933a INC] NEW CONNECTION
2020-07-29 11:45:29.728	[P2P1]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.82:21352 INC] 226 bytes received for category command-1001 initiated by peer
2020-07-29 11:45:29.728	[P2P1]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.82:21352 INC] 10 bytes sent for category command-1007 initiated by us
2020-07-29 11:45:29.730	[P2P1]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.82:21352 INC] 15639 bytes sent for category command-1001 initiated by peer
2020-07-29 11:45:29.889	[P2P3]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.82:21352 INC] 29 bytes received for category command-1007 initiated by us
2020-07-29 11:45:29.889	[P2P8]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2668	[162.218.65.82:21352 INC] [0] state: closed in state normal
2020-07-29 11:45:29.889	[P2P8]	INFO	net.p2p	src/p2p/net_node.inl:2446	[162.218.65.82:21352 7f8873ff-2689-4c58-99e8-d2178587933a INC] CLOSE CONNECTION
2020-07-29 11:45:30.017	[RPC1]	ERROR	net.http	contrib/epee/include/net/http_protocol_handler.inl:387	[51.79.58.90:50985 INC] simple_http_connection_handler<t_connection_context>::handle_invoke_query_line(): Failed to match first line: !�
2020-07-29 11:45:30.017	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-07-29 11:45:30.017	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x111) [0x55f0365435c1]:__wrap___cxa_throw+0x111) [0x55f0365435c1]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] monerod(+0x47c494) [0x55f0360ba494] 
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x123) [0x55f036a3f493]:_ZN2el4base26DefaultLogDispatchCallback8dispatchEONSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES8_S8_+0x123) [0x55f036a3f493]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x611) [0x55f036a3fd91]:_ZN2el4base26DefaultLogDispatchCallback6handleEPKNS_15LogDispatchDataE+0x611) [0x55f036a3fd91]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x15e) [0x55f036a40ade]:_ZN2el4base13LogDispatcher8dispatchEv+0x15e) [0x55f036a40ade]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x1c7) [0x55f036a40eb7]:_ZN2el4base6Writer15triggerDispatchEv+0x1c7) [0x55f036a40eb7]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x238) [0x55f036a41398]:_ZN2el4base6Writer15processDispatchEv+0x238) [0x55f036a41398]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x3d7) [0x55f0361893a7]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE24handle_invoke_query_lineEv+0x3d7) [0x55f0361893a7]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x4d5) [0x55f03618b565]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE14handle_buff_inERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x4d5) [0x55f03618b565]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x40) [0x55f03618baf0]:_ZN4epee9net_utils4http30simple_http_connection_handlerINS0_23connection_context_baseEE11handle_recvEPKvm+0x40) [0x55f03618baf0]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x1b9) [0x55f03618bd19]:_ZN4epee9net_utils10connectionINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE11handle_readERKN5boost6system10error_codeEm+0x1b9) [0x55f03618bd19]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x7b) [0x55f036150ffb]:_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2ISt5_BindIFMN4epee9net_utils10connectionINS7_4http19http_custom_handlerINS7_23connection_context_baseEEEEEFvRKNS_6system10error_codeEmENS_10shared_ptrISD_EESt12_PlaceholderILi1EESM_ILi2EEEESF_mEEEEvRPNS2_11strand_implERT_+0x7b) [0x55f036150ffb]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x5e) [0x55f03615129e]:_ZN5boost4asio6detail15wrapped_handlerINS0_10io_context6strandESt5_BindIFMN4epee9net_utils10connectionINS7_4http19http_custom_handlerINS7_23connection_context_baseEEEEEFvRKNS_6system10error_codeEmENS_10shared_ptrISD_EESt12_PlaceholderILi1EESM_ILi2EEEENS1_26is_continuation_if_runningEEclISF_mEEvRKT_RKT0_+0x5e) [0x55f03615129e]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x2a0) [0x55f03615a900]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandESt5_BindIFMN4epee9net_utils10connectionINSB_4http19http_custom_handlerINSB_23connection_context_baseEEEEEFvRKNS_6system10error_codeEmENS_10shared_ptrISH_EESt12_PlaceholderILi1EESQ_ILi2EEEENS1_26is_continuation_if_runningEEESJ_mEESU_EEEEvRPNS2_11strand_implERT_+0x2a0) [0x55f03615a900]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x2b1) [0x55f036161c91]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_context6strandESt5_BindIFMN4epee9net_utils10connectionINS9_4http19http_custom_handlerINS9_23connection_context_baseEEEEEFvRKNS_6system10error_codeEmENS_10shared_ptrISF_EESt12_PlaceholderILi1EESO_ILi2EEEENS1_26is_continuation_if_runningEEENS1_18io_object_executorINS0_8executorEEEE11do_completeEPvPNS1_19scheduler_operationESJ_m+0x2b1) [0x55f036161c91]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16]  0x1d5) [0x55f03610e555]:_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPvPNS1_19scheduler_operationERKNS_6system10error_codeEm+0x1d5) [0x55f03610e555]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17]  0x410) [0x55f03610ebf0]:_ZN5boost4asio6detail9scheduler10do_run_oneERNS1_27conditionally_enabled_mutex11scoped_lockERNS1_21scheduler_thread_infoERKNS_6system10error_codeE+0x410) [0x55f03610ebf0]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18]  0xe9) [0x55f0361137e9]:_ZN5boost4asio6detail9scheduler3runERNS_6system10error_codeE+0xe9) [0x55f0361137e9]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19]  0x1c5) [0x55f03611c0a5]:_ZN4epee9net_utils18boosted_tcp_serverINS0_4http19http_custom_handlerINS0_23connection_context_baseEEEE13worker_threadEv+0x1c5) [0x55f03611c0a5]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] monerod(+0xc4261a) [0x55f03688061a] 
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0x7fa3) [0x7f20e9454fa3]:_64-linux-gnu/libpthread.so.0(+0x7fa3) [0x7f20e9454fa3]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22]  0x3f) [0x7f20e93854cf]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f20e93854cf]
2020-07-29 11:45:30.022	[RPC1]	INFO	stacktrace	src/common/stack_trace.cpp:172	

```

## moneromooo-monero | 2020-07-29T11:55:51+00:00
Does it crash, or does it exit ? This doesn't seem to be the crash stack.

## normoes | 2020-07-29T12:04:45+00:00
It just stops working, so I guess it crashes.
if it exited, it would do so gracefully, i.e. we could see the logs, couldn't we?


What I copied above are the very last logs that can be found in the `bitmonero.log` file.

## normoes | 2020-07-29T12:36:53+00:00
I see simliar logs in the `stagenet` daemon, but this one is not going down.

I "forced" the error message by doing:
```
telnet IP PORT
somegarbage
```

Logs:
```
2020-07-29 12:34:31.018	[RPC1]	ERROR	net.http	contrib/epee/include/net/http_protocol_handler.inl:387	[****:56014 INC] simple_http_connection_handler<t_connection_context>::handle_invoke_query_line(): Failed to match first line: HOP
2020-07-29 12:34:31.019	[RPC1]	ERROR	net.http	contrib/epee/include/net/http_protocol_handler.inl:318	[****:56014 INC] simple_http_connection_handler::handle_char_out: Error state!!!
```

Not sure if that's useful at all.


I will try the same, on the `mainnet` daemon once it's running again on the other port.

## moneromooo-monero | 2020-07-29T13:02:28+00:00
That's normal. A crash or hang is not normal.

## moneromooo-monero | 2020-07-29T13:38:49+00:00
I can repro here, will fix.

## normoes | 2020-07-29T13:59:00+00:00
I also managed to get the `core` and ran `bt` (`gdb`). You gave me that hint on IRC some days/weeks ago.

How can I share that with you, if needed?

And, because I'm curious, how did you manage to reproduce it?

## moneromooo-monero | 2020-07-29T15:08:50+00:00
I piped /bin/* into it :)

## normoes | 2020-07-29T15:27:52+00:00
That's great :+1: 

## moneromooo-monero | 2020-07-29T17:05:01+00:00
There's a third patch in that branch which fixes my test case.
I have lots of interesting inputs from somewhere else which I'm going to test with too, so might be another patch later, but for now this one ought to fix yours.

## normoes | 2020-07-30T06:00:57+00:00
The patch is applied again - It is working now.

Thanks a lot!

I can still see the logs, of course. However, `monerod` just runs beautifully on and on.

There also are no logs like `exception: std::runtime_error` anymore.

## AJIekceu4 | 2020-07-30T08:12:29+00:00
Unfortunately this patch did not help with my problem: https://github.com/monero-project/monero/issues/6262

## normoes | 2020-07-30T10:54:59+00:00
I close this issue.

The problem described here is solved by the provided patch.

It looks like a PR was created already.

## selsta | 2020-08-09T00:11:36+00:00
We released v0.15.0.3 which includes a fix for this.

# Action History
- Created by: normoes | 2020-07-27T15:31:12+00:00
- Closed at: 2020-07-30T10:54:59+00:00
