---
title: Memory exhaustion issues likely with a malicious blocks
source_url: https://github.com/monero-project/monero/issues/7225
author: arizvisa
assignees: []
labels: []
created_at: '2020-12-29T11:27:08+00:00'
updated_at: '2021-01-12T12:28:19+00:00'
type: issue
status: closed
closed_at: '2021-01-12T03:02:28+00:00'
---

# Original Description
This has been occurring at the \_exact\_ same time during multiple synchronizations. Some issues are titled with memory leak, but this 100% seems like a malicious block or flaw in the implementation of cryptonote. The readline interface does not interpret commands after encountering the memory issue, so normally you're forced to kill the process. Prior to commit b2221881a172f445ca2bb9e962033796d5cf70ac, however, this would seem to corrupt the lmdb as anytime I'd load `monerod` again, non-recoverable mutex errors would occur.

Condition 1:
```
2020-12-29 11:04:59.235 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2020-12-29 11:04:59.710 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2020-12-29 11:06:39.016 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left, xx% of total synced, estimated 1.8 hours left)
2020-12-29 11:06:39.418 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2020-12-29 11:06:39.829 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2020-12-29 11:06:40.249 I [batch] DB resize needed
2020-12-29 11:06:40.249 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2020-12-29 11:06:40.512 W Failed to set new mapsize: Cannot allocate memory
status
```

Backtrace:
```
2020-12-29 11:06:40.249	[P2P2]	INFO	global	src/blockchain_db/lmdb/db_lmdb.cpp:664	[batch] DB resize needed
2020-12-29 11:06:40.249	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1644	Synced 2177362/2262732 (96%, 85370 left)
2020-12-29 11:06:40.512	[P2P2]	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:82	Failed to set new mapsize: Cannot allocate memory
2020-12-29 11:06:40.527	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: cryptonote::DB_ERROR
2020-12-29 11:06:40.528	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x116) [0x55a669f611b4]:__cxa_throw+0x116) [0x55a669f611b4]
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/local/bin/monerod(+0x3032a1) [0x55a669f752a1] 
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0xb05) [0x55a66a57b925]:_ZN10cryptonote14BlockchainLMDB9do_resizeEm+0xb05) [0x55a66a57b925]
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x179) [0x55a66a5b3f89]:_ZN10cryptonote14BlockchainLMDB11batch_startEmm+0x179) [0x55a66a5b3f89]
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x10f) [0x55a66a45a52f]:_ZN10cryptonote14tx_memory_pool26get_relayable_transactionsERSt6vectorISt5tupleIJN6crypto4hashENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_12relay_methodEEESaISC_EE+0x10f) [0x55a66a45a52f]
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x54) [0x55a66a442234]:_ZN10cryptonote4core25relay_txpool_transactionsEv+0x54) [0x55a66a442234]
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x111) [0x55a66a4427e1]:_ZN10cryptonote4core7on_idleEv+0x111) [0x55a66a4427e1]
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x52) [0x55a66a35fc52]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE20global_timer_handlerIN5boost3_bi6bind_tIbNSC_4_mfi3mf0IbNS6_29t_cryptonote_protocol_handlerINS6_4coreEEEEENSD_5list1INSD_5valueIPSJ_EEEEEEEEbNSC_10shared_ptrINSA_20idle_callback_conextIT_EEEE+0x52) [0x55a66a35fc52]
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x2a0) [0x55a66a383f70]:_ZN5boost4asio6detail12wait_handlerINS_3_bi6bind_tIbNS_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS7_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSI_20idle_callback_conextINS4_IbNS5_3mf0IbNSE_29t_cryptonote_protocol_handlerINSE_4coreEEEEENS3_5list1INS3_5valueIPSO_EEEEEEEEEEEENS3_5list2INSR_IPSI_EENSR_ISX_EEEEEENS1_18io_object_executorINS0_8executorEEEE11do_completeEPvPNS1_19scheduler_operationERKNS_6system10error_codeEm+0x2a0) [0x55a66a383f70]
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/local/bin/monerod(+0x692224) [0x55a66a304224] 
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x20a) [0x55a66a34221a]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x20a) [0x55a66a34221a]
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x11fa8) [0x7f9dd04e5fa8]:_thread.so.1.73.0(+0x11fa8) [0x7f9dd04e5fa8]
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] /lib64/libpthread.so.0(+0x93f9) [0x7f9dd012e3f9] 
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] /lib64/libc.so.6(clone+0x43) [0x7f9dd005b903] 
2020-12-29 11:06:40.539	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

I have a backup of the db at around 94%, so I can probably reproduce this with full logs if necessary. Upon restarting monerod (commit b2221881a172f445ca2bb9e962033796d5cf70ac), later there's an issue with RandomX.

Condition 2:
```
2020-12-29 11:18:34.641 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)                                                                                              
2020-12-29 11:18:35.069 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)                                                                                              
2020-12-29 11:18:35.230 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)                                                                                              
2020-12-29 11:18:35.403 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2020-12-29 11:18:35.619 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2020-12-29 11:18:35.868 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2020-12-29 11:18:36.182 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
Couldn't allocate RandomX cache  
```

Backtrace:
```
2020-12-29 11:18:35.868	[P2P0]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1644	Synced 2182122/2262737 (96%, 80615 left)
2020-12-29 11:18:36.182	[P2P0]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1644	Synced 2182142/2262737 (96%, 80595 left)
2020-12-29 11:18:36.184	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-12-29 11:18:36.184	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-12-29 11:18:36.192	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x116) [0x556ac11bf1b4]:__cxa_throw+0x116) [0x556ac11bf1b4]
2020-12-29 11:18:36.192	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/local/bin/monerod(+0x33a3b9) [0x556ac120a3b9] 
2020-12-29 11:18:36.192	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x17d) [0x556ac191a44d]:_alloc_cache+0x17d) [0x556ac191a44d]
2020-12-29 11:18:36.192	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x29b) [0x556ac16ea54b]:_slow_hash+0x29b) [0x556ac16ea54b]
2020-12-29 11:18:36.192	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x13e) [0x556ac16d253e]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmPKS7_i+0x13e) [0x556ac16d253e]
2020-12-29 11:18:36.192	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x28) [0x556ac16d2688]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x28) [0x556ac16d2688]
2020-12-29 11:18:36.192	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0xb1) [0x556ac166cea1]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb1) [0x556ac166cea1]
2020-12-29 11:18:36.192	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x470) [0x556ac1730990]:_ZN5tools10threadpool3runEb+0x470) [0x556ac1730990]
2020-12-29 11:18:36.192	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x3c) [0x556ac173132c]:_ZN5tools10threadpool6waiter4waitEv+0x3c) [0x556ac173132c]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x1350) [0x556ac1674160]:_ZN10cryptonote10Blockchain30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x1350) [0x556ac1674160]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x3f) [0x556ac1699e9f]:_ZN10cryptonote4core30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x3f) [0x556ac1699e9f]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0xca4) [0x556ac162f7f4]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE19try_add_next_blocksERNS_29cryptonote_connection_contextE+0xca4) [0x556ac162f7f4]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x209f) [0x556ac163638f]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE27handle_response_get_objectsEiRN4epee10misc_utils11struct_initINS_27NOTIFY_RESPONSE_GET_OBJECTS9request_tEEERNS_29cryptonote_connection_contextE+0x209f) [0x556ac163638f]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x1515) [0x556ac12e9b25]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEEEibiN4epee4spanIKhEERNSA_10byte_sliceERT_Rb+0x1515) [0x556ac12e9b25]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x5f) [0x556ac12ec6ef]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE6notifyEiN4epee4spanIKhEERNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEE+0x5f) [0x556ac12ec6ef]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16]  0xaf4) [0x556ac15d6894]:_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE11handle_recvEPKvm+0xaf4) [0x556ac15d6894]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17]  0x1a1) [0x556ac16059c1]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x1a1) [0x556ac16059c1]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18]  0x7a) [0x556ac15cbafa]:_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEESM_mEEEEvRPNS2_11strand_implERT_+0x7a) [0x556ac15cbafa]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19]  0x142) [0x556ac15d43c2]:_ZN5boost4asio6detail18completion_handlerINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS8_5list3INS8_5valueINS_10shared_ptrISN_EEEEPFNS_3argILi1EEEvEPFNSY_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESP_mEES16_EEE11do_completeEPvPNS1_19scheduler_operationESR_m+0x142) [0x556ac15d43c2]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20]  0x1fc) [0x556ac15d46ec]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x1fc) [0x556ac15d46ec]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0x345) [0x556ac15e2dc5]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEENS1_18io_object_executorINS0_8executorEEEE11do_completeEPvPNS1_19scheduler_operationESQ_m+0x345) [0x556ac15e2dc5]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/local/bin/monerod(+0x692224) [0x556ac1562224] 
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23]  0x20a) [0x556ac15a021a]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x20a) [0x556ac15a021a]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24]  0x11fa8) [0x7fb78cce9fa8]:_thread.so.1.73.0(+0x11fa8) [0x7fb78cce9fa8]
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [25] /lib64/libpthread.so.0(+0x93f9) [0x7fb78c9323f9] 
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [26] /lib64/libc.so.6(clone+0x43) [0x7fb78c85f903] 
2020-12-29 11:18:36.193	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-12-29 11:18:36.194	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2020-12-29 11:18:36.194	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x116) [0x556ac11bf1b4]:__cxa_throw+0x116) [0x556ac11bf1b4]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x48) [0x556ac1926668]:_ZN7randomx16AlignedAllocatorILm64EE11allocMemoryEm+0x48) [0x556ac1926668]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x1d5) [0x556ac191a4a5]:_alloc_cache+0x1d5) [0x556ac191a4a5]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x75d) [0x556ac16eaa0d]:_slow_hash+0x75d) [0x556ac16eaa0d]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x13e) [0x556ac16d253e]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmPKS7_i+0x13e) [0x556ac16d253e]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x28) [0x556ac16d2688]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x28) [0x556ac16d2688]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0xb1) [0x556ac166cea1]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb1) [0x556ac166cea1]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x470) [0x556ac1730990]:_ZN5tools10threadpool3runEb+0x470) [0x556ac1730990]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x3c) [0x556ac173132c]:_ZN5tools10threadpool6waiter4waitEv+0x3c) [0x556ac173132c]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x1350) [0x556ac1674160]:_ZN10cryptonote10Blockchain30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x1350) [0x556ac1674160]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x3f) [0x556ac1699e9f]:_ZN10cryptonote4core30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x3f) [0x556ac1699e9f]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0xca4) [0x556ac162f7f4]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE19try_add_next_blocksERNS_29cryptonote_connection_contextE+0xca4) [0x556ac162f7f4]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x209f) [0x556ac163638f]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE27handle_response_get_objectsEiRN4epee10misc_utils11struct_initINS_27NOTIFY_RESPONSE_GET_OBJECTS9request_tEEERNS_29cryptonote_connection_contextE+0x209f) [0x556ac163638f]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x1515) [0x556ac12e9b25]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEEEibiN4epee4spanIKhEERNSA_10byte_sliceERT_Rb+0x1515) [0x556ac12e9b25]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x5f) [0x556ac12ec6ef]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE6notifyEiN4epee4spanIKhEERNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEE+0x5f) [0x556ac12ec6ef]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16]  0xaf4) [0x556ac15d6894]:_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE11handle_recvEPKvm+0xaf4) [0x556ac15d6894]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17]  0x1a1) [0x556ac16059c1]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x1a1) [0x556ac16059c1]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18]  0x7a) [0x556ac15cbafa]:_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEESM_mEEEEvRPNS2_11strand_implERT_+0x7a) [0x556ac15cbafa]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19]  0x142) [0x556ac15d43c2]:_ZN5boost4asio6detail18completion_handlerINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS8_5list3INS8_5valueINS_10shared_ptrISN_EEEEPFNS_3argILi1EEEvEPFNSY_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESP_mEES16_EEE11do_completeEPvPNS1_19scheduler_operationESR_m+0x142) [0x556ac15d43c2]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20]  0x1fc) [0x556ac15d46ec]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x1fc) [0x556ac15d46ec]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0x345) [0x556ac15e2dc5]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEENS1_18io_object_executorINS0_8executorEEEE11do_completeEPvPNS1_19scheduler_operationESQ_m+0x345) [0x556ac15e2dc5]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/local/bin/monerod(+0x692224) [0x556ac1562224] 
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23]  0x20a) [0x556ac15a021a]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x20a) [0x556ac15a021a]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24]  0x11fa8) [0x7fb78cce9fa8]:_thread.so.1.73.0(+0x11fa8) [0x7fb78cce9fa8]
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [25] /lib64/libpthread.so.0(+0x93f9) [0x7fb78c9323f9] 
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [26] /lib64/libc.so.6(clone+0x43) [0x7fb78c85f903] 
2020-12-29 11:18:36.199	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	
```
lmk if you'd prefer I demangle these symbols...

# Discussion History
## selsta | 2020-12-30T23:00:51+00:00
Does this issue happen with v0.17.1.8? https://www.getmonero.org/downloads/

## arizvisa | 2021-01-04T17:02:25+00:00
Just resumed synchronization with commit 36dfd41e01ebc852e094f268433344404c042591, and it seems that I'm past that RandomX allocation issue.

```
2021-01-04 16:58:25.710 I [127.0.0.1:18080 OUT] Sync data returned a new top block candidate: XXXXXXX -> XXXXXXX [Your node is XXXXX blocks (x.x months) behind] 
2021-01-04 16:58:25.710 I SYNCHRONIZATION started
2021-01-04 16:58:35.194 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2021-01-04 16:58:37.133 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
```

I'm stuck on a hotspot for a bit, but later this week (when I get to a place the b/w is free) I'll resume from the previous height that was causing those previous reports and let you guys know prior to closing this issue.

## Voker57 | 2021-01-06T10:25:58+00:00
Still happens for me with 0.18.1.8, monero quickly swells to 6gb RAM on certain block.

## dEBRUYNE-1 | 2021-01-06T18:05:53+00:00
@Voker57 - Please try compiling the `release-v0.17` branch.

https://github.com/monero-project/monero#compiling-monero-from-source

## moneromooo-monero | 2021-01-09T01:36:22+00:00
Should now be fixed. I'll close once you confirm.
Nothing to do with blocks fwiw.

## arizvisa | 2021-01-09T02:32:02+00:00
kk.

ah. weird then, as it kept reproducing at around the same synchronization point.

## arizvisa | 2021-01-10T02:25:26+00:00
Okay. With commit 36dfd41e01ebc852e094f268433344404c042591 that got me past the RandomX issue. I encounter the following, but after killing the process I'm able to resume synchronization.

```
2021-01-10 02:01:46.664 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2021-01-10 02:01:46.940 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2021-01-10 02:01:48.955 I [batch] DB resize needed
2021-01-10 02:01:48.955 I Synced XXXXXXX/XXXXXXX (XX%, XXXXX left)
2021-01-10 02:04:19.062 W Failed to set new mapsize: Cannot allocate memory
```

I'm rebuilding and re-copying the database I have from XX%, so I'll let y'all know in a bit about the symptoms with commit 8fef32e45c80aec41f25be9d1d8fb75adc883c64 which should be the latest (as of now is tagged v0.17.1.9) in the release-v0.17 branch.

## moneromooo-monero | 2021-01-10T02:29:47+00:00
Do you have enough disk space ?

## arizvisa | 2021-01-10T03:01:48+00:00
```
$ df -h | grep monero
/dev/sdb1               239G  161G   78G  68% /run/media/user/monero
```

## arizvisa | 2021-01-10T03:07:09+00:00
After I restore the former DB, I'll resume synchronization w/ a binary built from the v0.17.1.9 tag and full logging enabled. I'm just rsync'ing from my backup usb over my monero one, so the bitmonero.log is being directly overwritten rather than rolled over.

## arizvisa | 2021-01-10T03:31:37+00:00
Okay. Not sure if it's happening at the same place, but the logging has blocked at the following, and the daemon isn't replying to my "help" command.
```
2021-01-10 03:22:19.086 T BlockchainLMDB::get_block_timestamp
2021-01-10 03:22:19.086 T Blockchain::check_block_timestamp
2021-01-10 03:22:19.086 T Blockchain::get_difficulty_for_next_block
2021-01-10 03:22:19.086 T BlockchainLMDB::height
2021-01-10 03:22:19.086 T Blockchain::get_tail_id
2021-01-10 03:22:19.086 T BlockchainLMDB::top_block_hash
2021-01-10 03:22:19.086 T BlockchainLMDB::height
2021-01-10 03:22:19.086 T BlockchainLMDB::get_block_hash_from_height
2021-01-10 03:22:19.086 T Blockchain::get_tail_id
2021-01-10 03:22:19.086 T BlockchainLMDB::top_block_hash
2021-01-10 03:22:19.086 T BlockchainLMDB::height
```

Memory usage seems to be slowly increasing...
```
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       4.0Gi       1.4Gi       222Mi        10Gi        10Gi
Swap:          13Gi       169Mi        13Gi
```
then a minute later:
```
~$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       4.0Gi       571Mi       217Mi        10Gi        10Gi
Swap:          13Gi       169Mi        13Gi
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       4.0Gi       558Mi       217Mi        10Gi        10Gi
Swap:          13Gi       169Mi        13Gi
```

## arizvisa | 2021-01-10T03:38:11+00:00
Ahh.."sync_info" just responded (see attached file: [blah.txt](https://github.com/monero-project/monero/files/5792172/blah.txt)) and I realized I forgot to blacklist tor endpoints prior to running it this time...

"status" returned too:
```
status
Height: XXXXXXX/XXXXXXX (XX.X%) on mainnet, not mining, net hash 1.43 GH/s, v12, 12(out)+0(in) connections, uptime 0d 0h 24m 8s
```

I'm backing up the log-level=4 logs and will attach them in a sec...

## arizvisa | 2021-01-10T03:52:12+00:00
It seems like just "help" stopped emitting things for some reason...I snapshot the logs and moved them to another hd, but am waiting till it gets to past XX% which is closer to where the issue was that I first reported since I'm not sure if this is first weird symptom is actually related to my original report or not.

## arizvisa | 2021-01-11T13:26:51+00:00
Okay. It look a while running it all day, but now I get.
```
2021-01-11 13:23:52.614 D Run server thread name: P2P
2021-01-11 13:23:52.614 D Run server thread name: P2P
2021-01-11 13:23:52.614 D Run server thread name: P2P
2021-01-11 13:23:52.614 D JOINING all threads
2021-01-11 13:23:53.616 D STARTED PEERLIST IDLE HANDSHAKE
2021-01-11 13:23:53.616 D FINISHED PEERLIST IDLE HANDSHAKE
2021-01-11 13:23:53.617 T Blockchain::get_current_blockchain_height
2021-01-11 13:23:53.617 T mdb_txn_safe: destructor
2021-01-11 13:23:53.617 T BlockchainLMDB::height
2021-01-11 13:23:53.618 T batch transaction: aborted
2021-01-11 13:23:53.618 T BlockchainLMDB::block_rtxn_start
2021-01-11 13:23:53.620 D Checking for a new monero version for source
2021-01-11 13:23:53.620 D Checking updates for source monero
2021-01-11 13:23:53.621 T mdb_txn_safe: destructor
2021-01-11 13:23:53.621 D get_next_needed_pruning_stripe: want height XXXXXXX (XXXXXXX from blockchain, XXXXXXX from block queue), stripe 7 (0/12 on it and 0 on 8, 0 others) -> 7 (+0), current peers 
2021-01-11 13:23:53.621 D Making expected connection, type 0, 0/2 connections
2021-01-11 13:23:53.622 D Considering connecting (out) to anchor peer: xxxxxxxxxxxxxxxx 127.0.0.1:18080
2021-01-11 13:23:53.624 D test, connection constructor set m_connection_type=2
2021-01-11 13:23:53.624 D connections_ size now 1
2021-01-11 13:23:53.625 D Trying to connect to 127.0.0.1:18080, bind_ip = 0.0.0.0
terminate called after throwing an instance of 'boost::wrapexcept<boost::lock_error>'
  what():  boost: mutex lock failed in pthread_mutex_lock: Invalid argument
```

block position is at:
```
monero-logs7/monero.20210110221238.log-2021-01-11-04-40-12:2021-01-11 04:40:03.482      [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1644    Synced XXXXXXXX/XXXXXXXX (XX%, XXXXX left) (1.699609 sec, 11.767412 blocks/sec), 99.380096 MB queued in 80 spans, stripe 7 -> 7: [moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo.oo.o..]
monero-logs7/monero.20210110221238.log-2021-01-11-04-40-12:2021-01-11 04:40:06.995      [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1644    Synced XXXXXXXX/XXXXXXXX (XX%, XXXXX left) (3.512267 sec, 5.694328 blocks/sec), 97.158722 MB queued in 80 spans, stripe 7 -> 7: [moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo.o...]
monero-logs7/monero.20210110221238.log-2021-01-11-04-40-12:2021-01-11 04:40:12.372      [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1644    Synced XXXXXXX/XXXXXXX (XX%, XXXXX left) (5.375898 sec, 3.720309 blocks/sec), 96.088898 MB queued in 85 spans, stripe 7 -> 7: [moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo..]
```

So this is definitely at the time that I previously encountered the memory issue.

One moment while I tar up all the different logs and sort them out, get symbols for core files, etc.

[768264.445649] traps: monerod[1100109] general protection fault ip:7fa1f8629967 sp:7f89028fa640 error:0 in libc-2.32.so[7fa1f8629000+14f000]

## moneromooo-monero | 2021-01-11T14:00:18+00:00
Do you have a stack trace for this ?
gdb monerod
run usual-arguments-here
bt full

## moneromooo-monero | 2021-01-11T14:04:46+00:00
up 1
info locals
print this
print *this

## arizvisa | 2021-01-12T03:02:27+00:00
Okay. Looks like the memory exhaustion problem is solved w/ commit 8fef32e45c80aec41f25be9d1d8fb75adc883c64. Closing this issue.

## moneromooo-monero | 2021-01-12T12:28:19+00:00
Would be nice to fix the crash though.

# Action History
- Created by: arizvisa | 2020-12-29T11:27:08+00:00
- Closed at: 2021-01-12T03:02:28+00:00
