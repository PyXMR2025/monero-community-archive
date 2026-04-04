---
title: 'Occasional Exception: std::runtime_error'
source_url: https://github.com/monero-project/monero/issues/6696
author: trasherdk
assignees: []
labels: []
created_at: '2020-06-28T07:28:24+00:00'
updated_at: '2022-02-19T04:28:57+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:28:57+00:00'
---

# Original Description
I saw this a lot (Monero v0.16.0.0) before enabling `HugePages` in the kernel: Slackware 14.2 x64 Kernel `4.4.227`.

Upgrading to `Monero v0.16.0.1` and compile kernel with `HugePages` I've seen this only twice in 2 days.

```
$ ./usr/bin/monerod --version
Monero 'Nitrogen Nebula' (v0.16.0.1-6ea322d78)
```
Monero was build without the `boost-1.73 fix ( f35ced6d7f00282091a9623bad573132f42a91b0 )`  which break `boost-1.59`.
 
```
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [1]   0xa7)  [0x564dd838e927]:__cxa_throw+0xa7) [0x564dd838e927]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [2]   0x62)  [0x564dd856e152]:_Z21allocLargePagesMemorym+0x62) [0x564dd856e152]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [3]   0xbc)  [0x564dd856398c]:_alloc_cache+0xbc) [0x564dd856398c]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [4]   0x5ec) [0x564dd834330c]:_slow_hash+0x5ec) [0x564dd834330c]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [5]   0xc9)  [0x564dd832b8b9]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xc9) [0x564dd832b8b9]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [6]   0x31)  [0x564dd832ba91]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x31) [0x564dd832ba91]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [7]   0x127) [0x564dd82c16d7]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0x127) [0x564dd82c16d7]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [8]   0x246) [0x564dd83867d6]:_ZN5tools10threadpool3runEb+0x246) [0x564dd83867d6]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [9]   0x39)  [0x564dd8387269]:_ZN5tools10threadpool6waiter4waitEPS0_+0x39) [0x564dd8387269]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [10]  0x1256)[0x564dd82d1d36]:_ZN10cryptonote10Blockchain30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x1256) [0x564dd82d1d36]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [11]  0x2b)  [0x564dd82f7a8b]:_ZN10cryptonote4core30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x2b) [0x564dd82f7a8b]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [12]  0x275f)[0x564dd8257f1f]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE30handle_notify_new_fluffy_blockEiRN4epee10misc_utils11struct_initINS_23NOTIFY_NEW_FLUFFY_BLOCK9request_tEEERNS_29cryptonote_connection_contextE+0x275f) [0x564dd8257f1f]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [13]  0x31f) [0x564dd7fad73f]:_ZN4epee9net_utils17buff_to_t_adapterIN10cryptonote29t_cryptonote_protocol_handlerINS2_4coreEEENS_10misc_utils11struct_initINS2_23NOTIFY_NEW_FLUFFY_BLOCK9request_tEEENS2_29cryptonote_connection_contextEN5boost3_bi6bind_tIiNSC_4_mfi3mf3IiS5_iRSA_RSB_EENSD_5list4INSD_5valueIPS5_EENSC_3argILi1EEENSO_ILi2EEENSO_ILi3EEEEEEEEEiPT_iNS_4spanIKhEET2_RT1_+0x31f) [0x564dd7fad73f]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [14]  0x4d1) [0x564dd7faff11]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE17handle_invoke_mapINS_29cryptonote_connection_contextEEEibiN4epee4spanIKhEERSsRT_Rb+0x4d1) [0x564dd7faff11]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [15]  0xbd)  [0x564dd7fb63ad]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEEEibiN4epee4spanIKhEERSsRT_Rb+0xbd) [0x564dd7fb63ad]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [16]  0x4d)  [0x564dd7fb677d]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE6notifyEiN4epee4spanIKhEERNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEE+0x4d) [0x564dd7fb677d]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [17]  0x120a)[0x564dd82732fa]:_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE11handle_recvEPKvm+0x120a) [0x564dd82732fa]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [18]  0x1ec) [0x564dd829e16c]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x1ec) [0x564dd829e16c]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [19]  0x7a)  [0x564dd82466ca]:_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEESM_mEEEEvRPNS2_11strand_implERT_+0x7a) [0x564dd82466ca]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [20]  0x69)  [0x564dd8246939]:_ZN5boost4asio6detail15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEclISM_mEEvRKT_RKT0_+0x69) [0x564dd8246939]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [21]  0x105) [0x564dd8246ab5]:_ZN5boost4asio6detail18completion_handlerINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS8_5list3INS8_5valueINS_10shared_ptrISN_EEEEPFNS_3argILi1EEEvEPFNSY_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESP_mEES16_EEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESR_m+0x105) [0x564dd8246ab5]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [22]  0x226) [0x564dd82480e6]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x226) [0x564dd82480e6]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [23]  0x250) [0x564dd8248450]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESQ_m+0x250) [0x564dd8248450]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [24]  0x164) [0x564dd7f33d54]:_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationERKNS_6system10error_codeEm+0x164) [0x564dd7f33d54]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [25]  0x8a8) [0x564dd8219418]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x8a8) [0x564dd8219418]
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [26] /path/to/monerod(+0x9bf2a5) [0x564dd85b52a5] 
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [27] /lib64/libpthread.so.0(+0x7684) [0x7f4400739684] 
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172 [28] /lib64/libc.so.6(clone+0x6d) [0x7f440046feed] 
[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172
```

```
$ cat /proc/meminfo 
MemTotal:        8157228 kB
MemFree:         1160408 kB
MemAvailable:    5512152 kB
Buffers:         1114548 kB
Cached:          3161276 kB
SwapCached:            0 kB
Active:          4502428 kB
Inactive:        1975952 kB
Active(anon):    2202640 kB
Inactive(anon):      864 kB
Active(file):    2299788 kB
Inactive(file):  1975088 kB
Unevictable:           4 kB
Mlocked:               4 kB
SwapTotal:       1993704 kB
SwapFree:        1993704 kB
Dirty:                56 kB
Writeback:             0 kB
AnonPages:       2202396 kB
Mapped:           964476 kB
Shmem:               964 kB
Slab:             398820 kB
SReclaimable:     380744 kB
SUnreclaim:        18076 kB
KernelStack:        5440 kB
PageTables:        49792 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     6064124 kB
Committed_AS:    3633184 kB
VmallocTotal:   34359738367 kB
VmallocUsed:           0 kB
VmallocChunk:          0 kB
AnonHugePages:   2031616 kB
HugePages_Total:       8
HugePages_Free:        8
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:       13740 kB
DirectMap2M:     8374272 kB
```


# Discussion History
## Cideg | 2020-06-28T11:41:47+00:00
i get the same error: 
runtime error

```
2020-06-28 11:20:28.490	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-06-28 11:20:28.491	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x113) [0x558b87462f2f]:__cxa_throw+0x113) [0x558b87462f2f]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x315563) [0x558b874a1563] 
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x33) [0x558b87ad77b3]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x33) [0x558b87ad77b3]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0xde) [0x558b87ad4e4e]:_create_vm+0xde) [0x558b87ad4e4e]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x400) [0x558b87918450]:_slow_hash+0x400) [0x558b87918450]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xc5) [0x558b87901795]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xc5) [0x558b87901795]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x28) [0x558b87901908]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x28) [0x558b87901908]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xb5) [0x558b878adf85]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb5) [0x558b878adf85]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x407) [0x558b879585d7]:_ZN5tools10threadpool3runEb+0x407) [0x558b879585d7]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x141b5) [0x7f6b1c6cb1b5]:_64-linux-gnu/libboost_thread.so.1.67.0(+0x141b5) [0x7f6b1c6cb1b5]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x9669) [0x7f6b1bfdd669]:_64-linux-gnu/libpthread.so.0(+0x9669) [0x7f6b1bfdd669]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x43) [0x7f6b1bf05323]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f6b1bf05323]
2020-06-28 11:20:28.511	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-06-28 11:23:42.943	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-06-28 11:23:42.944	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x113) [0x558b87462f2f]:__cxa_throw+0x113) [0x558b87462f2f]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x315563) [0x558b874a1563] 
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x33) [0x558b87ad77b3]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x33) [0x558b87ad77b3]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0xde) [0x558b87ad4e4e]:_create_vm+0xde) [0x558b87ad4e4e]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x400) [0x558b87918450]:_slow_hash+0x400) [0x558b87918450]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xc5) [0x558b87901795]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xc5) [0x558b87901795]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x28) [0x558b87901908]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x28) [0x558b87901908]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xb5) [0x558b878adf85]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb5) [0x558b878adf85]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x407) [0x558b879585d7]:_ZN5tools10threadpool3runEb+0x407) [0x558b879585d7]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x141b5) [0x7f6b1c6cb1b5]:_64-linux-gnu/libboost_thread.so.1.67.0(+0x141b5) [0x7f6b1c6cb1b5]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x9669) [0x7f6b1bfdd669]:_64-linux-gnu/libpthread.so.0(+0x9669) [0x7f6b1bfdd669]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x43) [0x7f6b1bf05323]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f6b1bf05323]
2020-06-28 11:23:42.947	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-06-28 11:26:10.810	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-06-28 11:26:10.810	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-06-28 11:26:10.813	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x113) [0x558b87462f2f]:__cxa_throw+0x113) [0x558b87462f2f]
2020-06-28 11:26:10.813	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x315563) [0x558b874a1563] 
2020-06-28 11:26:10.813	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x33) [0x558b87ad77b3]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x33) [0x558b87ad77b3]
2020-06-28 11:26:10.813	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0xde) [0x558b87ad4e4e]:_create_vm+0xde) [0x558b87ad4e4e]
2020-06-28 11:26:10.813	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x400) [0x558b87918450]:_slow_hash+0x400) [0x558b87918450]
2020-06-28 11:26:10.813	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xc5) [0x558b87901795]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xc5) [0x558b87901795]
2020-06-28 11:26:10.813	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x28) [0x558b87901908]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x28) [0x558b87901908]
2020-06-28 11:26:10.814	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xb5) [0x558b878adf85]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb5) [0x558b878adf85]
2020-06-28 11:26:10.814	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x407) [0x558b879585d7]:_ZN5tools10threadpool3runEb+0x407) [0x558b879585d7]
2020-06-28 11:26:10.814	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x141b5) [0x7f6b1c6cb1b5]:_64-linux-gnu/libboost_thread.so.1.67.0(+0x141b5) [0x7f6b1c6cb1b5]
2020-06-28 11:26:10.814	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x9669) [0x7f6b1bfdd669]:_64-linux-gnu/libpthread.so.0(+0x9669) [0x7f6b1bfdd669]
2020-06-28 11:26:10.814	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x43) [0x7f6b1bf05323]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f6b1bf05323]
2020-06-28 11:26:10.814	    7f5349cf8700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-06-28 11:27:05.299	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-06-28 11:27:05.299	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x113) [0x558b87462f2f]:__cxa_throw+0x113) [0x558b87462f2f]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x315563) [0x558b874a1563] 
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x33) [0x558b87ad77b3]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x33) [0x558b87ad77b3]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0xde) [0x558b87ad4e4e]:_create_vm+0xde) [0x558b87ad4e4e]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x400) [0x558b87918450]:_slow_hash+0x400) [0x558b87918450]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xc5) [0x558b87901795]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xc5) [0x558b87901795]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x28) [0x558b87901908]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x28) [0x558b87901908]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xb5) [0x558b878adf85]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb5) [0x558b878adf85]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x407) [0x558b879585d7]:_ZN5tools10threadpool3runEb+0x407) [0x558b879585d7]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x3d) [0x558b87958c7d]:_ZN5tools10threadpool6waiter4waitEPS0_+0x3d) [0x558b87958c7d]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x1138) [0x558b878b4798]:_ZN10cryptonote10Blockchain30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x1138) [0x558b878b4798]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x30) [0x558b878d46a0]:_ZN10cryptonote4core30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x30) [0x558b878d46a0]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x236f) [0x558b8783b8cf]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE30handle_notify_new_fluffy_blockEiRN4epee10misc_utils11struct_initINS_23NOTIFY_NEW_FLUFFY_BLOCK9request_tEEERNS_29cryptonote_connection_contextE+0x236f) [0x558b8783b8cf]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x39a) [0x558b8757c0da]:_ZN4epee9net_utils17buff_to_t_adapterIN10cryptonote29t_cryptonote_protocol_handlerINS2_4coreEEENS_10misc_utils11struct_initINS2_23NOTIFY_NEW_FLUFFY_BLOCK9request_tEEENS2_29cryptonote_connection_contextEN5boost3_bi6bind_tIiNSC_4_mfi3mf3IiS5_iRSA_RSB_EENSD_5list4INSD_5valueIPS5_EENSC_3argILi1EEENSO_ILi2EEENSO_ILi3EEEEEEEEEiPT_iNS_4spanIKhEET2_RT1_+0x39a) [0x558b8757c0da]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x30f) [0x558b8757e78f]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE17handle_invoke_mapINS_29cryptonote_connection_contextEEEibiN4epee4spanIKhEERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERT_Rb+0x30f) [0x558b8757e78f]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16]  0x230) [0x558b8757ec40]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEEEibiN4epee4spanIKhEERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERT_Rb+0x230) [0x558b8757ec40]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17]  0x5e) [0x558b8757eebe]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE6notifyEiN4epee4spanIKhEERNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEE+0x5e) [0x558b8757eebe]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18]  0x10fc) [0x558b8787873c]:_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE11handle_recvEPKvm+0x10fc) [0x558b8787873c]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19]  0x185) [0x558b8788a865]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x185) [0x558b8788a865]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20]  0x83) [0x558b878302e3]:_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEESM_mEEEEvRPNS2_11strand_implERT_+0x83) [0x558b878302e3]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0x3ef) [0x558b87830d6f]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x3ef) [0x558b87830d6f]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22]  0x161) [0x558b878310e1]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEEE11do_completeEPvPNS1_19scheduler_operationESQ_m+0x161) [0x558b878310e1]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23]  0x175) [0x558b874f0085]:_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPvPNS1_19scheduler_operationERKNS_6system10error_codeEm+0x175) [0x558b874f0085]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24]  0x506) [0x558b874f0c96]:_ZN5boost4asio6detail9scheduler3runERNS_6system10error_codeE+0x506) [0x558b874f0c96]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [25]  0x252) [0x558b87804012]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x252) [0x558b87804012]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [26]  0x141b5) [0x7f6b1c6cb1b5]:_64-linux-gnu/libboost_thread.so.1.67.0(+0x141b5) [0x7f6b1c6cb1b5]
2020-06-28 11:27:05.320	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [27]  0x9669) [0x7f6b1bfdd669]:_64-linux-gnu/libpthread.so.0(+0x9669) [0x7f6b1bfdd669]
2020-06-28 11:27:05.321	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [28]  0x43) [0x7f6b1bf05323]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f6b1bf05323]
2020-06-28 11:27:05.321	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-06-28 11:28:42.901	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-06-28 11:28:42.901	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-06-28 11:28:42.903	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x113) [0x558b87462f2f]:__cxa_throw+0x113) [0x558b87462f2f]
2020-06-28 11:28:42.903	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x315563) [0x558b874a1563] 
2020-06-28 11:28:42.903	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x33) [0x558b87ad77b3]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x33) [0x558b87ad77b3]
2020-06-28 11:28:42.903	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0xde) [0x558b87ad4e4e]:_create_vm+0xde) [0x558b87ad4e4e]
2020-06-28 11:28:42.903	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x400) [0x558b87918450]:_slow_hash+0x400) [0x558b87918450]
2020-06-28 11:28:42.903	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xc5) [0x558b87901795]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xc5) [0x558b87901795]
2020-06-28 11:28:42.903	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x28) [0x558b87901908]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x28) [0x558b87901908]
2020-06-28 11:28:42.903	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xb5) [0x558b878adf85]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb5) [0x558b878adf85]
2020-06-28 11:28:42.903	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x407) [0x558b879585d7]:_ZN5tools10threadpool3runEb+0x407) [0x558b879585d7]
2020-06-28 11:28:42.904	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x141b5) [0x7f6b1c6cb1b5]:_64-linux-gnu/libboost_thread.so.1.67.0(+0x141b5) [0x7f6b1c6cb1b5]
2020-06-28 11:28:42.904	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x9669) [0x7f6b1bfdd669]:_64-linux-gnu/libpthread.so.0(+0x9669) [0x7f6b1bfdd669]
2020-06-28 11:28:42.904	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x43) [0x7f6b1bf05323]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f6b1bf05323]
2020-06-28 11:28:42.904	    7f534a6fa700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-06-28 11:29:47.328	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2020-06-28 11:29:47.328	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-06-28 11:29:47.334	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x113) [0x558b87462f2f]:__cxa_throw+0x113) [0x558b87462f2f]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x315563) [0x558b874a1563] 
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x33) [0x558b87ad77b3]:_ZN7randomx6VmBaseINS_18LargePageAllocatorELb0EE8allocateEv+0x33) [0x558b87ad77b3]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0xde) [0x558b87ad4e4e]:_create_vm+0xde) [0x558b87ad4e4e]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x400) [0x558b87918450]:_slow_hash+0x400) [0x558b87918450]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0xc5) [0x558b87901795]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xc5) [0x558b87901795]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x28) [0x558b87901908]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x28) [0x558b87901908]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0xb5) [0x558b878adf85]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb5) [0x558b878adf85]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x407) [0x558b879585d7]:_ZN5tools10threadpool3runEb+0x407) [0x558b879585d7]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x3d) [0x558b87958c7d]:_ZN5tools10threadpool6waiter4waitEPS0_+0x3d) [0x558b87958c7d]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x1138) [0x558b878b4798]:_ZN10cryptonote10Blockchain30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x1138) [0x558b878b4798]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x30) [0x558b878d46a0]:_ZN10cryptonote4core30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x30) [0x558b878d46a0]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x236f) [0x558b8783b8cf]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE30handle_notify_new_fluffy_blockEiRN4epee10misc_utils11struct_initINS_23NOTIFY_NEW_FLUFFY_BLOCK9request_tEEERNS_29cryptonote_connection_contextE+0x236f) [0x558b8783b8cf]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x39a) [0x558b8757c0da]:_ZN4epee9net_utils17buff_to_t_adapterIN10cryptonote29t_cryptonote_protocol_handlerINS2_4coreEEENS_10misc_utils11struct_initINS2_23NOTIFY_NEW_FLUFFY_BLOCK9request_tEEENS2_29cryptonote_connection_contextEN5boost3_bi6bind_tIiNSC_4_mfi3mf3IiS5_iRSA_RSB_EENSD_5list4INSD_5valueIPS5_EENSC_3argILi1EEENSO_ILi2EEENSO_ILi3EEEEEEEEEiPT_iNS_4spanIKhEET2_RT1_+0x39a) [0x558b8757c0da]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x30f) [0x558b8757e78f]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE17handle_invoke_mapINS_29cryptonote_connection_contextEEEibiN4epee4spanIKhEERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERT_Rb+0x30f) [0x558b8757e78f]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16]  0x230) [0x558b8757ec40]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEEEibiN4epee4spanIKhEERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERT_Rb+0x230) [0x558b8757ec40]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17]  0x5e) [0x558b8757eebe]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE6notifyEiN4epee4spanIKhEERNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEE+0x5e) [0x558b8757eebe]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18]  0x10fc) [0x558b8787873c]:_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE11handle_recvEPKvm+0x10fc) [0x558b8787873c]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19]  0x185) [0x558b8788a865]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x185) [0x558b8788a865]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20]  0x83) [0x558b878302e3]:_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEESM_mEEEEvRPNS2_11strand_implERT_+0x83) [0x558b878302e3]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0x3ef) [0x558b87830d6f]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x3ef) [0x558b87830d6f]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22]  0x161) [0x558b878310e1]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_context6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEEE11do_completeEPvPNS1_19scheduler_operationESQ_m+0x161) [0x558b878310e1]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23]  0x175) [0x558b874f0085]:_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPvPNS1_19scheduler_operationERKNS_6system10error_codeEm+0x175) [0x558b874f0085]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24]  0x506) [0x558b874f0c96]:_ZN5boost4asio6detail9scheduler3runERNS_6system10error_codeE+0x506) [0x558b874f0c96]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [25]  0x252) [0x558b87804012]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x252) [0x558b87804012]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [26]  0x141b5) [0x7f6b1c6cb1b5]:_64-linux-gnu/libboost_thread.so.1.67.0(+0x141b5) [0x7f6b1c6cb1b5]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [27]  0x9669) [0x7f6b1bfdd669]:_64-linux-gnu/libpthread.so.0(+0x9669) [0x7f6b1bfdd669]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [28]  0x43) [0x7f6b1bf05323]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f6b1bf05323]
2020-06-28 11:29:47.335	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-06-28 11:34:42.024	    7f537da29700	INFO	msgwriter	src/common/scoped_message_writer.h:102	0.16.0.0-f0ada2f22
2020-06-28 11:34:44.574	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:80	p2p net loop stopped
2020-06-28 11:34:44.632	    7f536ffff700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::system_error
2020-06-28 11:34:44.632	    7f536ffff700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-06-28 11:34:44.635	    7f536ffff700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x113) [0x558b87462f2f]:__cxa_throw+0x113) [0x558b87462f2f]
2020-06-28 11:34:44.635	    7f536ffff700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0xee) [0x558b874a10b8]:_ZN6detail6expect6throw_ESt10error_codePKcS3_j+0xee) [0x558b874a10b8]
2020-06-28 11:34:44.635	    7f536ffff700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x51a) [0x558b879a119a]:_ZN10cryptonote3rpc9ZmqServer5serveEv+0x51a) [0x558b879a119a]
2020-06-28 11:34:44.635	    7f536ffff700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x141b5) [0x7f6b1c6cb1b5]:_64-linux-gnu/libboost_thread.so.1.67.0(+0x141b5) [0x7f6b1c6cb1b5]
2020-06-28 11:34:44.635	    7f536ffff700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x9669) [0x7f6b1bfdd669]:_64-linux-gnu/libpthread.so.0(+0x9669) [0x7f6b1bfdd669]
2020-06-28 11:34:44.635	    7f536ffff700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x43) [0x7f6b1bf05323]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f6b1bf05323]
2020-06-28 11:34:44.635	    7f536ffff700	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

## tevador | 2020-06-30T21:00:02+00:00
It's not an actual error as indicated by the "INFO" log level on the left. Just ignore it. Monerod likes to log all thrown exceptions, even handled ones.

Everything will still work as usual, just PoW verification will be a tiny bit slower without hugepages.

## normoes | 2020-07-27T19:59:22+00:00
Looks simliar to this issue: https://github.com/monero-project/monero/issues/6724

But the linked issue logs `ERROR` instead of `INFO` and `monerod` is stopping.

## tevador | 2020-08-01T11:06:09+00:00
@normoes That issue is a completely unrelated error.

## Dendrocalamus64 | 2021-09-16T11:56:18+00:00
Started getting it on 'Oxygen Orion' (v0.17.2.0-release) around the 95% synced mark, RockPro64 with 4GB RAM.  The current Manjaro kernel (5.14.1-1-MANJARO-ARM) has HugePages enabled, but there aren't any configured by default.

Quick link to how to set them:
https://wiki.archlinux.org/title/KVM#Enabling_huge_pages

So, how many to configure?  4 or more is stopping the exception from occurring, 3 or less does not.  Instead of one log line per 20 blocks synced, multiple stack dumps per 20 is something I'd like to avoid.

Specifically, it started right after 'Synced 2324988/2450305 (94%, 125317 left)'

## selsta | 2022-02-19T04:28:57+00:00
https://github.com/monero-project/monero/pull/7084

# Action History
- Created by: trasherdk | 2020-06-28T07:28:24+00:00
- Closed at: 2022-02-19T04:28:57+00:00
