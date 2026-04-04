---
title: 'Exception: boost::wrapexcept<boost::bad_weak_ptr> and std::runtime_error'
source_url: https://github.com/monero-project/monero/issues/6473
author: icostan
assignees: []
labels: []
created_at: '2020-04-24T14:10:22+00:00'
updated_at: '2022-11-02T23:10:55+00:00'
type: issue
status: closed
closed_at: '2020-11-20T05:47:22+00:00'
---

# Original Description
Has anyone seen the following error/s in logs again and again? 

Not sure if they are related but I started to see these errors after my blockchain got corrupted, I did sync using the same machine/monero daemon version on a different SSD disk then copied the "data.mdb" and "lock.mdb" over to data dir.

Everything seems to work fine so far but I am worried about log pollution.

```shell
2020-04-24 13:42:22.633	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-04-24 13:42:22.633	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [1]  0x115) [0x5651ee0dbebc]:__cxa_throw+0x115) [0x5651ee0dbebc]
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [2] /usr/bin/monerod(+0x351be0) [0x5651ee115be0] 
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [3]  0x30) [0x5651ee701180]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x30) [0x5651ee701180]
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [4]  0x107) [0x5651ee6fe7c7]:_create_vm+0x107) [0x5651ee6fe7c7]
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [5]  0x476) [0x5651ee54fd56]:_slow_hash+0x476) [0x5651ee54fd56]
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [6]  0xb9) [0x5651ee539739]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xb9) [0x5651ee539739]
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [7]  0x27) [0x5651ee5398e7]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x27) [0x5651ee5398e7]
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [8]  0xb8) [0x5651ee4e5f38]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb8) [0x5651ee4e5f38]
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [9]  0x46a) [0x5651ee58c81a]:_ZN5tools10threadpool3runEb+0x46a) [0x5651ee58c81a]
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [10]  0x11807) [0x7f69f8176807]:_thread.so.1.72.0(+0x11807) [0x7f69f8176807]
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [11] /usr/lib/libpthread.so.0(+0x946f) [0x7f69f7e0346f] 
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	   [12] /usr/lib/libc.so.6(clone+0x43) [0x7f69f7d333d3] 
2020-04-24 13:42:22.639	   7f5378cdd700	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

```shell
2020-04-24 13:47:03.340	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2020-04-24 13:47:03.340	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-04-24 13:47:03.347	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [1]  0x115) [0x5651ee0dbebc]:__cxa_throw+0x115) [0x5651ee0dbebc]
2020-04-24 13:47:03.347	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [2]  0x174) [0x5651ee43d7e4]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE21safe_shared_from_thisEv+0x174) [0x5651ee43d7e4]
2020-04-24 13:47:03.347	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [3]  0x35) [0x5651ee45bb95]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE5closeEv+0x35) [0x5651ee45bb95]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [4]  0x3b3) [0x5651ee41e123]:_ZN4epee5levin29async_protocol_handler_configIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE5closeEN5boost5uuids4uuidE+0x3b3) [0x5651ee41e123]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [5]  0x56c) [0x5651ee4b152c]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE22do_handshake_with_peerERmRNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEb+0x56c) [0x5651ee4b152c]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [6]  0x258) [0x5651ee4b1c68]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE42try_to_connect_and_handshake_with_new_peerERKN4epee9net_utils15network_addressEbmNS5_8PeerTypeEm+0x258) [0x5651ee4b1c68]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [7]  0x129) [0x5651ee4b66a9]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE15connect_to_seedEv+0x129) [0x5651ee4b66a9]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [8]  0x536) [0x5651ee4b7466]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17connections_makerEv+0x536) [0x5651ee4b7466]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [9]  0xac) [0x5651ee415a8c]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE11idle_workerEv+0xac) [0x5651ee415a8c]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [10]  0x52) [0x5651ee450942]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE20global_timer_handlerIN5boost3_bi6bind_tIbNSC_4_mfi3mf0IbNS4_11node_serverINS6_29t_cryptonote_protocol_handlerINS6_4coreEEEEEEENSD_5list1INSD_5valueIPSL_EEEEEEEEbNSC_10shared_ptrINSA_20idle_callback_conextIT_EEEE+0x52) [0x5651ee450942]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [11]  0x2bc) [0x5651ee489abc]:_ZN5boost4asio6detail12wait_handlerINS_3_bi6bind_tIbNS_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS7_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSI_20idle_callback_conextINS4_IbNS5_3mf0IbNSC_11node_serverINSE_29t_cryptonote_protocol_handlerINSE_4coreEEEEEEENS3_5list1INS3_5valueIPSQ_EEEEEEEEEEEENS3_5list2INST_IPSI_EENST_ISZ_EEEEEENS1_18io_object_executorINS0_8executorEEEE11do_completeEPvPNS1_19scheduler_operationERKNS_6system10error_codeEm+0x2bc) [0x5651ee489abc]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [12]  0x512) [0x5651ee16e512]:_ZN5boost4asio6detail9scheduler3runERNS_6system10error_codeE+0x512) [0x5651ee16e512]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [13]  0x170) [0x5651ee436950]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x170) [0x5651ee436950]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [14]  0x11807) [0x7f69f8176807]:_thread.so.1.72.0(+0x11807) [0x7f69f8176807]
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [15] /usr/lib/libpthread.so.0(+0x946f) [0x7f69f7e0346f] 
2020-04-24 13:47:03.348	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [16] /usr/lib/libc.so.6(clone+0x43) [0x7f69f7d333d3] 
```

My system:

```shell
OS: Arch Linux x86_64 
Host: 81LF Lenovo Legion Y7000P-1060 
Kernel: 5.6.7-arch1-1 
CPU: Intel i7-8750H (12) @ 4.100GHz 

Monero 'Carbon Chamaeleon' (v0.15.0.5-release)
```

# Discussion History
## moneromooo-monero | 2020-04-24T14:22:51+00:00
They're known, the former is normal randomx noisy init probing, the second is fixed on github.

## Forage | 2020-05-05T08:34:13+00:00
I've got the same issue where `Exception: std::runtime_error` 'info' messages are flooding the log since it reoccurs about every 15 seconds. It renders the log quite unpractical to use.

Is this something that needs to be fixed in the monero project or in the librandomx project and thus has to be reported there?

```
2020-05-05 07:38:47.690 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2020-05-05 07:38:47.690 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x11a) [0x55e389c5d039]:__cxa_throw+0x11a) [0x55e389c5d039]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2]  0x1abae) [0x7f593520bbae]:_64-linux-gnu/librandomx.so.0(+0x1abae) [0x7f593520bbae]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x31) [0x7f593521fda1]:_64-linux-gnu/librandomx.so.0(_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x31) [0x7f593521fda1]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0x163) [0x7f593521af63]:_64-linux-gnu/librandomx.so.0(randomx_create_vm+0x163) [0x7f593521af63]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x43d) [0x55e38a07100d]:_slow_hash+0x43d) [0x55e38a07100d]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0xcb) [0x55e38a05d58b]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xcb) [0x55e38a05d58b]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7]  0x21) [0x55e38a05d741]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x21) [0x55e38a05d741]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8]  0xf5) [0x55e38a001f65]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xf5) [0x55e38a001f65]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9]  0x3b6) [0x55e38a0a6426]:_ZN5tools10threadpool3runEb+0x3b6) [0x55e38a0a6426]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10]  0x3b) [0x55e38a0a6deb]:_ZN5tools10threadpool6waiter4waitEPS0_+0x3b) [0x55e38a0a6deb]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11]  0x153f) [0x55e38a0152ef]:_ZN10cryptonote10Blockchain30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x153f) [0x55e38a0152ef]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0x33) [0x55e38a034943]:_ZN10cryptonote4core30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x33) [0x55e38a034943]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13]  0x2301) [0x55e389fa63a1]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE30handle_notify_new_fluffy_blockEiRN4epee10misc_utils11struct_initINS_23NOTIFY_NEW_FLUFFY_BLOCK9request_tEEERNS_29cryptonote_connection_contextE+0x2301) [0x55e389fa63a1]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14]  0x2c5) [0x55e389d4b9b5]:_ZN4epee9net_utils17buff_to_t_adapterIN10cryptonote29t_cryptonote_protocol_handlerINS2_4coreEEENS_10misc_utils11struct_initINS2_23NOTIFY_NEW_FLUFFY_BLOCK9request_tEEENS2_29cryptonote_connection_contextEN5boost3_bi6bind_tIiNSC_4_mfi3mf3IiS5_iRSA_RSB_EENSD_5list4INSD_5valueIPS5_EENSC_3argILi1EEENSO_ILi2EEENSO_ILi3EEEEEEEEEiPT_iNS_4spanIKhEET2_RT1_+0x2c5) [0x55e389d4b9b5]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [15]  0x323) [0x55e389d4c9a3]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE17handle_invoke_mapINS_29cryptonote_connection_contextEEEibiN4epee4spanIKhEERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERT_Rb+0x323) [0x55e389d4c9a3]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [16]  0x36b) [0x55e389d4cf0b]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEEEibiN4epee4spanIKhEERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERT_Rb+0x36b) [0x55e389d4cf0b]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [17]  0x59) [0x55e389d4d159]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE6notifyEiN4epee4spanIKhEERNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEE+0x59) [0x55e389d4d159]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [18]  0x1194) [0x55e389fdba84]:_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE11handle_recvEPKvm+0x1194) [0x55e389fdba84]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [19]  0x18a) [0x55e389febeda]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x18a) [0x55e389febeda]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [20]  0x7b) [0x55e389f99e3b]:_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEESM_mEEEEvRPNS2_11strand_implERT_+0x7b) [0x55e389f99e3b]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [21]  0x14a) [0x55e389f9a27a]:_ZN5boost4asio6detail18completion_handlerINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS8_5list3INS8_5valueINS_10shared_ptrISN_EEEEPFNS_3argILi1EEEvEPFNSY_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESP_mEES16_EEE11do_completeEPvPNS1_19scheduler_operationESR_m+0x14a) [0x55e389f9a27a]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [22]  0x1f6) [0x55e389f9a596]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x1f6) [0x55e389f9a596]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [23]  0x168) [0x55e389f9a7e8]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEEE11do_completeEPvPNS1_19scheduler_operationESQ_m+0x168) [0x55e389f9a7e8]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [24]  0x215) [0x55e389cca205]:_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPvPNS1_19scheduler_operationERKNS_6system10error_codeEm+0x215) [0x55e389cca205]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [25]  0x40c) [0x55e389cc959c]:_ZN5boost4asio6detail9scheduler10do_run_oneERNS1_27conditionally_enabled_mutex11scoped_lockERNS1_21scheduler_thread_infoERKNS_6system10error_codeE+0x40c) [0x55e389cc959c]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [26]  0x101) [0x55e389cc9781]:_ZN5boost4asio6detail9scheduler3runERNS_6system10error_codeE+0x101) [0x55e389cc9781]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [27]  0x161) [0x55e389f74071]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x161) [0x55e389f74071]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [28]  0x14615) [0x7f5934d12615]:_64-linux-gnu/libboost_thread.so.1.67.0(+0x14615) [0x7f5934d12615]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [29]  0x7fa3) [0x7f59349c1fa3]:_64-linux-gnu/libpthread.so.0(+0x7fa3) [0x7f59349c1fa3]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172      [30]  0x3f) [0x7f59348f24cf]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f59348f24cf]
2020-05-05 07:38:47.694 [P2P8]  INFO    stacktrace      src/common/stack_trace.cpp:172  
```


## hyc | 2020-05-05T21:22:37+00:00
It looks like RandomX is trying to allocate using large pages and that's failing. Anyway, you can make librandomx stop trying to use large pages by setting the environment variable MONERO_RANDOMX_UMASK=1 when running monerod.

I see, librandomx actually does throw exceptions on allocation errors. That's rude.

## Forage | 2020-05-06T07:26:16+00:00
Thanks for having a look.

Unfortunately the MONERO_RANDOMX_UMASK environment variable did not help as a work-around.

Besides it flooding the log it also appears to be linked to a drastic decrease in sync time.
These messages start to occur at around half way 97% sync. Up until than there's sync updates about every second. This changes to every 15 seconds together with the flood messages.

## moneromooo-monero | 2020-05-06T12:49:18+00:00
Most likely because that's where it starts verifying PoW.

## rofra | 2020-07-06T15:09:59+00:00
Same issue with https://github.com/XMRto/monero repo on kubernetes, MONERO_RANDOMX_UMASK did not help

## icostan | 2020-11-20T05:47:22+00:00
The crash related to ```LargePageAllocator``` can be fixed  with sys settings:

``` sh
sudo sysctl -w vm.nr_hugepages=1280
```

and the other error seems to be fixed as well.

## crocket | 2021-02-11T07:24:11+00:00
I have encountered this issue. I don't think this issue is fixed if it requires such a workaround as
```
sudo sysctl -w vm.nr_hugepages=1280
```

## blacklion | 2021-12-29T14:49:54+00:00
It is not fixed even in 0.17.3.0, at least for FreeBSD. I have huge pages and mlock enabled for users, but still get a lot of

```
2021-12-29 14:48:50.970 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:134  Exception: boost::wrapexcept<boost::bad_weak_ptr>
2021-12-29 14:48:50.970 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:135  Unwound call stack:
2021-12-29 14:48:51.133 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       1                  0x1a1254e
2021-12-29 14:48:51.295 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       2                  0x1456c5c
2021-12-29 14:48:51.457 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       3                  0x17f187e
2021-12-29 14:48:51.619 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       4                  0x17e6ae7
2021-12-29 14:48:51.782 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       5                  0x1780998
2021-12-29 14:48:51.947 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       6                  0x1780c4c
2021-12-29 14:48:52.110 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       7                  0x17c4876
2021-12-29 14:48:52.274 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       8                  0x17b2531
2021-12-29 14:48:52.438 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       9                  0x177ef00
2021-12-29 14:48:52.601 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       a                  0x180cfd2
2021-12-29 14:48:52.763 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       b                  0x180d964
2021-12-29 14:48:52.926 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       c                  0x1a5cc52
2021-12-29 14:48:53.091 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       d                  0x1431df1
2021-12-29 14:48:53.257 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       e                  0x14318b1
2021-12-29 14:48:53.424 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159       f                  0x17e919a
2021-12-29 14:48:53.588 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159      10                  0x80260b5ca
2021-12-29 14:48:53.750 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159      11                  0x8027aa08c
2021-12-29 14:48:53.918 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:159      12                  0x0
2021-12-29 14:48:53.918 [P2P0]  INFO    stacktrace      src/common/stack_trace.cpp:149  Failed to find the next frame
```

from monerod.

## blacklion | 2021-12-30T13:12:21+00:00
Enabling 1.5GB of locked memory for process (which is, I believe, analogous to Linux's  `sysctl -w vm.nr_hugepages=1280`) doesn't help. It allows `monerod` process to have 119GB (!) allocated and 4GB (!!!) resident, but sometimes it still throw this exception.

## proailurus | 2022-01-21T11:14:57+00:00
I keep getting these as well
>Exception: boost::wrapexcept<boost::bad_weak_ptr>

package is https://build.opensuse.org/package/show/openSUSE%3AFactory/monero

## selsta | 2022-05-18T23:14:27+00:00
continuing in #8341

## godfuture | 2022-11-01T20:04:35+00:00
Same issue here. I am using monero in a docker container. It worked for years. I am now many blocks late, so my instance starts synching. But after a while it stops. Mostly when these statements kick in:
```
2022-11-01 19:36:14.127	[P2P0]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:406	[64.98.81.85:18080 OUT] Sync data returned a new top block candidate: 2732066 -> 2746484 [Your node is 14418 blocks (20.0 days) behind] 
2022-11-01 19:36:14.127	[P2P0]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:406	SYNCHRONIZATION started
2022-11-01 19:39:50.432	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:406	[174.119.179.168:18080 OUT] Sync data returned a new top block candidate: 2732066 -> 2746484 [Your node is 14418 blocks (20.0 days) behind] 
2022-11-01 19:39:50.433	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:406	SYNCHRONIZATION started
2022-11-01 19:40:38.810	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:406	[99.249.31.171:18080 OUT] Sync data returned a new top block candidate: 2732066 -> 2746484 [Your node is 14418 blocks (20.0 days) behind] 
2022-11-01 19:40:38.810	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:406	SYNCHRONIZATION started
```
And sooner or later I always find:
```
2022-11-01 19:43:22.180	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2022-11-01 19:43:22.180	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2022-11-01 19:43:22.181	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2022-11-01 19:43:22.207	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2022-11-01 19:43:22.208	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2022-11-01 19:43:22.208	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

## selsta | 2022-11-01T21:18:11+00:00
@godfuture so does it not sync up at all anymore? or does it sync up and at some point fall behind again?

## godfuture | 2022-11-01T21:28:33+00:00
@selsta It does not sync up at all anymore. Well, in the beginning it syncs, but stops over time. I have done mem tests, reduced CPU clocks, increased hugepages...I dont know what to do anymore. It worked for long time. Now I saw the first time:
`2022-11-01 21:20:00.285	E point conv failed`

## selsta | 2022-11-01T21:44:53+00:00
Did you try resyncing from scratch?

## godfuture | 2022-11-02T21:55:32+00:00
> Did you try resyncing from scratch?

Yes, which in fact increased the frustration :-(

## selsta | 2022-11-02T23:10:55+00:00
@godfuture I need more info. Where did it get stuck first and where did it get stuck after the complete resync from scratch with deleted blockchain?

# Action History
- Created by: icostan | 2020-04-24T14:10:22+00:00
- Closed at: 2020-11-20T05:47:22+00:00
