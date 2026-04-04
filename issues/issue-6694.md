---
title: Monerod stuck at 2124792
source_url: https://github.com/monero-project/monero/issues/6694
author: starikanbich
assignees: []
labels: []
created_at: '2020-06-26T16:09:08+00:00'
updated_at: '2020-06-26T16:37:41+00:00'
type: issue
status: closed
closed_at: '2020-06-26T16:37:41+00:00'
---

# Original Description
Ubuntu 18.04

Monero 'Nitrogen Nebula' (v0.16.0.1-release)

Installed from here:
https://github.com/monero-project/monero
 
```
2020-06-26 14:25:22.538	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:368	SYNCHRONIZATION started
2020-06-26 14:25:24.739	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-06-26 14:25:24.739	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x10d) [0x5651d8b159fd]:__cxa_throw+0x10d) [0x5651d8b159fd]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x4e) [0x5651d8c98e6e]:_Z10setPagesRXPvm+0x4e) [0x5651d8c98e6e]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x73) [0x5651d8c8f5b3]:_init_cache+0x73) [0x5651d8c8f5b3]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x116) [0x5651d8ac8276]:_slow_hash+0x116) [0x5651d8ac8276]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xc9) [0x5651d8ab0419]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xc9) [0x5651d8ab0419]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x1d) [0x5651d8ab059d]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x1d) [0x5651d8ab059d]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0xa9) [0x5651d8a4cb39]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xa9) [0x5651d8a4cb39]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x415) [0x5651d8b0d395]:_ZN5tools10threadpool3runEb+0x415) [0x5651d8b0d395]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x37) [0x5651d8b0df77]:_ZN5tools10threadpool6waiter4waitEPS0_+0x37) [0x5651d8b0df77]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0xf1a) [0x5651d8a5d9aa]:_ZN10cryptonote10Blockchain30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0xf1a) [0x5651d8a5d9aa]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x2b) [0x5651d8a7fe8b]:_ZN10cryptonote4core30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x2b) [0x5651d8a7fe8b]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0xbea) [0x5651d89f62ea]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE19try_add_next_blocksERNS_29cryptonote_connection_contextE+0xbea) [0x5651d89f62ea]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x1cb4) [0x5651d89fc8f4]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE27handle_response_get_objectsEiRN4epee10misc_utils11struct_initINS_27NOTIFY_RESPONSE_GET_OBJECTS9request_tEEERNS_29cryptonote_connection_contextE+0x1cb4) [0x5651d89fc8f4]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x3e9) [0x5651d876db49]:_ZN4epee9net_utils17buff_to_t_adapterIN10cryptonote29t_cryptonote_protocol_handlerINS2_4coreEEENS_10misc_utils11struct_initINS2_27NOTIFY_RESPONSE_GET_OBJECTS9request_tEEENS2_29cryptonote_connection_contextEN5boost3_bi6bind_tIiNSC_4_mfi3mf3IiS5_iRSA_RSB_EENSD_5list4INSD_5valueIPS5_EENSC_3argILi1EEENSO_ILi2EEENSO_ILi3EEEEEEEEEiPT_iNS_4spanIKhEET2_RT1_+0x3e9) [0x5651d876db49]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x289) [0x5651d876f889]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE17handle_invoke_mapINS_29cryptonote_connection_contextEEEibiN4epee4spanIKhEERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERT_Rb+0x289) [0x5651d876f889]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16]  0x235) [0x5651d876fe45]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEEEibiN4epee4spanIKhEERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERT_Rb+0x235) [0x5651d876fe45]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17]  0x55) [0x5651d87700a5]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE6notifyEiN4epee4spanIKhEERNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEE+0x55) [0x5651d87700a5]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18]  0x1064) [0x5651d8a28a84]:_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE11handle_recvEPKvm+0x1064) [0x5651d8a28a84]
2020-06-26 14:25:24.751	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19]  0x18a) [0x5651d8a2ccfa]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x18a) [0x5651d8a2ccfa]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20]  0xd2) [0x5651d89dbca2]:_ZN5boost4asio6detail15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEclISM_mEEvRKT_RKT0_+0xd2) [0x5651d89dbca2]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xe5) [0x5651d89dddc5]:_ZN5boost4asio6detail18completion_handlerINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS8_5list3INS8_5valueINS_10shared_ptrISN_EEEEPFNS_3argILi1EEEvEPFNSY_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESP_mEES16_EEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESR_m+0xe5) [0x5651d89dddc5]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22]  0x1fa) [0x5651d89de0ca]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x1fa) [0x5651d89de0ca]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23]  0x1e9) [0x5651d89de399]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESQ_m+0x1e9) [0x5651d89de399]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24]  0x174) [0x5651d86f3bf4]:_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationERKNS_6system10error_codeEm+0x174) [0x5651d86f3bf4]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [25]  0x2eb) [0x5651d86f382b]:_ZN5boost4asio6detail15task_io_service10do_run_oneERNS1_11scoped_lockINS1_11posix_mutexEEERNS1_27task_io_service_thread_infoERKNS_6system10error_codeE+0x2eb) [0x5651d86f382b]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [26]  0x20d) [0x5651d89b5aed]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x20d) [0x5651d89b5aed]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [27]  0x11bcd) [0x7ff026222bcd]:_64-linux-gnu/libboost_thread.so.1.65.1(+0x11bcd) [0x7ff026222bcd]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [28]  0x76db) [0x7ff024f626db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7ff024f626db]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [29]  0x3f) [0x7ff024c8b88f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7ff024c8b88f]
2020-06-26 14:25:24.752	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-06-26 14:25:24.752	[P2P9]	ERROR	default	src/common/threadpool.cpp:118	wait should have been called before waiter dtor - waiting now
```

I'm have tried to add vm.nr_hugepages=2048, but the same.

Anyone can help me?

# Discussion History
## starikanbich | 2020-06-26T16:37:41+00:00
Ok solved.
=>
MONERO_RANDOMX_UMASK=1 ./monerod

# Action History
- Created by: starikanbich | 2020-06-26T16:09:08+00:00
- Closed at: 2020-06-26T16:37:41+00:00
