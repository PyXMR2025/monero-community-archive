---
title: Exception on sync
source_url: https://github.com/monero-project/monero/issues/7367
author: badfiles
assignees: []
labels: []
created_at: '2021-02-10T10:08:56+00:00'
updated_at: '2022-02-19T00:36:42+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:36:42+00:00'
---

# Original Description
```
2021-02-10 10:04:26.283	    7fdafa84c000	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Oxygen Orion' (v0.17.0.0-cb70ae945) Daemonised
2021-02-10 10:04:26.283	    7fdafa84c000	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-02-10 10:04:26.283	    7fdafa84c000	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-02-10 10:04:26.283	    7fdafa84c000	INFO	global	src/daemon/core.h:63	Initializing core...
2021-02-10 10:04:26.283	    7fdafa84c000	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder /var/monero/lmdb ...
2021-02-10 10:04:26.332	    7fdafa84c000	INFO	global	src/cryptonote_core/cryptonote_core.cpp:690	Loading checkpoints
2021-02-10 10:04:26.332	    7fdafa84c000	INFO	global	src/daemon/core.h:73	Core initialized OK
2021-02-10 10:04:26.332	    7fdafa84c000	INFO	global	src/daemon/p2p.h:63	Initializing p2p server...
2021-02-10 10:04:26.337	    7fdafa84c000	INFO	global	src/daemon/p2p.h:68	p2p server initialized OK
2021-02-10 10:04:26.337	    7fdafa84c000	INFO	global	src/daemon/rpc.h:63	Initializing core RPC server...
2021-02-10 10:04:26.337	    7fdafa84c000	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 172.*.*.1 (IPv4):18081
2021-02-10 10:04:27.366	    7fdafa84c000	INFO	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2021-02-10 10:04:27.367	    7fdafa84c000	INFO	global	src/daemon/rpc.h:74	Starting core RPC server...
2021-02-10 10:04:27.367	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:79	core RPC server started ok
2021-02-10 10:04:27.367	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:78	Starting p2p net loop...
2021-02-10 10:04:28.367	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1734	
2021-02-10 10:04:28.367	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1734	**********************************************************************
2021-02-10 10:04:28.368	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1734	The daemon will start synchronizing with the network. This may take a long time to complete.
2021-02-10 10:04:28.368	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1734	
2021-02-10 10:04:28.368	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1734	You can set the level of process detailization through "set_log <level|categories>" command,
2021-02-10 10:04:28.368	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1734	where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2021-02-10 10:04:28.368	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1734	
2021-02-10 10:04:28.368	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1734	Use the "help" command to see the list of available commands.
2021-02-10 10:04:28.368	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1734	Use "help <command>" to see a command's documentation.
2021-02-10 10:04:28.368	[P2P3]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1734	**********************************************************************
2021-02-10 10:04:28.798	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:378	[69.244.130.248:18080 OUT] Sync data returned a new top block candidate: 2199852 -> 2293657 [Your node is 93805 blocks (4.3 months) behind] 
2021-02-10 10:04:28.798	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:378	SYNCHRONIZATION started
2021-02-10 10:04:34.447	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2021-02-10 10:04:34.447	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x10d) [0x563c21b4a41d]:__cxa_throw+0x10d) [0x563c21b4a41d]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x62) [0x563c21d13b12]:_Z21allocLargePagesMemorym+0x62) [0x563c21d13b12]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0xbc) [0x563c21d0862c]:_alloc_cache+0xbc) [0x563c21d0862c]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x23c) [0x563c21afaa5c]:_slow_hash+0x23c) [0x563c21afaa5c]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0xf6) [0x563c21ae2ff6]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmPKS7_i+0xf6) [0x563c21ae2ff6]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x1f) [0x563c21ae31df]:_ZN10cryptonote18get_block_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x1f) [0x563c21ae31df]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0xb8) [0x563c21a76fe8]:_ZNK10cryptonote10Blockchain21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb8) [0x563c21a76fe8]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x451) [0x563c21b419c1]:_ZN5tools10threadpool3runEb+0x451) [0x563c21b419c1]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0x36) [0x563c21b427c6]:_ZN5tools10threadpool6waiter4waitEv+0x36) [0x563c21b427c6]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x10ce) [0x563c21a8b18e]:_ZN10cryptonote10Blockchain30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x10ce) [0x563c21a8b18e]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x2b) [0x563c21aaf36b]:_ZN10cryptonote4core30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x2b) [0x563c21aaf36b]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0xc6c) [0x563c21a4e6ac]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE19try_add_next_blocksERNS_29cryptonote_connection_contextE+0xc6c) [0x563c21a4e6ac]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x2501) [0x563c21a55751]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE27handle_response_get_objectsEiRN4epee10misc_utils11struct_initINS_27NOTIFY_RESPONSE_GET_OBJECTS9request_tEEERNS_29cryptonote_connection_contextE+0x2501) [0x563c21a55751]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x3dc) [0x563c21773aec]:_ZN4epee9net_utils17buff_to_t_adapterIN10cryptonote29t_cryptonote_protocol_handlerINS2_4coreEEENS_10misc_utils11struct_initINS2_27NOTIFY_RESPONSE_GET_OBJECTS9request_tEEENS2_29cryptonote_connection_contextESt5_BindIFMS5_FiiRSA_RSB_EPS5_St12_PlaceholderILi1EESI_ILi2EESI_ILi3EEEEEEiPT_iNS_4spanIKhEET2_RT1_+0x3dc) [0x563c21773aec]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x1e8) [0x563c217758a8]:_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE17handle_invoke_mapINS_29cryptonote_connection_contextEEEibiN4epee4spanIKhEERNS5_10byte_sliceERT_Rb+0x1e8) [0x563c217758a8]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16]  0x24b) [0x563c21775feb]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEEEibiN4epee4spanIKhEERNSA_10byte_sliceERT_Rb+0x24b) [0x563c21775feb]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17]  0x54) [0x563c21776434]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE6notifyEiN4epee4spanIKhEERNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEE+0x54) [0x563c21776434]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18]  0xfb4) [0x563c21a0d904]:_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE11handle_recvEPKvm+0xfb4) [0x563c21a0d904]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19]  0x1a7) [0x563c21a288e7]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x1a7) [0x563c21a288e7]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20]  0xd2) [0x563c219f5bd2]:_ZN5boost4asio6detail15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEclISM_mEEvRKT_RKT0_+0xd2) [0x563c219f5bd2]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xe9) [0x563c219f7569]:_ZN5boost4asio6detail18completion_handlerINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS8_5list3INS8_5valueINS_10shared_ptrISN_EEEEPFNS_3argILi1EEEvEPFNSY_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESP_mEES16_EEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESR_m+0xe9) [0x563c219f7569]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22]  0x1ff) [0x563c219fdf1f]:_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x1ff) [0x563c219fdf1f]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23]  0x1f4) [0x563c219fe1f4]:_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESQ_m+0x1f4) [0x563c219fe1f4]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24]  0x174) [0x563c216f2214]:_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationERKNS_6system10error_codeEm+0x174) [0x563c216f2214]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [25]  0x2eb) [0x563c216f1e4b]:_ZN5boost4asio6detail15task_io_service10do_run_oneERNS1_11scoped_lockINS1_11posix_mutexEEERNS1_27task_io_service_thread_infoERKNS_6system10error_codeE+0x2eb) [0x563c216f1e4b]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [26]  0x20d) [0x563c219cb4ed]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x20d) [0x563c219cb4ed]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [27]  0x11bcd) [0x7fdaf85f2bcd]:_64-linux-gnu/libboost_thread.so.1.65.1(+0x11bcd) [0x7fdaf85f2bcd]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [28]  0x76db) [0x7fdaf784c6db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7fdaf784c6db]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [29]  0x3f) [0x7fdaf757571f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7fdaf757571f]
2021-02-10 10:04:34.453	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

# Discussion History
## moneromooo-monero | 2021-02-10T10:49:42+00:00
Is your daemon failing to sync ? You did not say what's going wrong, and the lost does not show anything wrong.

## badfiles | 2021-02-10T20:44:16+00:00
it does not
if Exception: std::runtime_error  on every block is OK and 20M log per day is also OK then I have nothing to add

## moneromooo-monero | 2021-02-11T12:30:27+00:00
Yes, those just mean it can't allocate large pages, but it can allocate nomnal ones if it continues.

## M4rotte | 2022-02-12T13:27:11+00:00
Hi,

I experience the same issue. I had this error message when I got home. I tried to stop and run monerod again but I keep getting this error :

```
2022-02-12 13:00:41.527     7f3e27c6ca00        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-02-12 13:00:41.527     7f3e27c6ca00        INFO    global  src/daemon/main.cpp:296 Monero 'Oxygen Orion' (v0.17.3.0-release)
2022-02-12 13:00:41.527     7f3e27c6ca00        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2022-02-12 13:00:41.528     7f3e27c6ca00        WARNING daemon  src/daemon/executor.cpp:61      Monero 'Oxygen Orion' (v0.17.3.0-release) Daemonised
2022-02-12 13:00:41.528     7f3e27c6ca00        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2022-02-12 13:00:41.528     7f3e27c6ca00        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2022-02-12 13:00:41.530     7f3e27c6ca00        INFO    global  src/daemon/core.h:64    Initializing core...
2022-02-12 13:00:41.531     7f3e27c6ca00        INFO    global  src/cryptonote_core/cryptonote_core.cpp:517     Loading blockchain from folder /data/Monero/BlockChain/lmdb ...
2022-02-12 13:00:41.531     7f3e27c6ca00        WARNING global  src/blockchain_db/lmdb/db_lmdb.cpp:1362 The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2022-02-12 13:02:33.497     7f3e27c6ca00        INFO    global  src/cryptonote_core/cryptonote_core.cpp:692     Loading checkpoints
2022-02-12 13:02:33.498     7f3e27c6ca00        INFO    global  src/daemon/core.h:81    Core initialized OK
2022-02-12 13:02:33.498     7f3e27c6ca00        INFO    global  src/daemon/p2p.h:64     Initializing p2p server...
2022-02-12 13:02:33.530     7f3e27c6ca00        INFO    global  src/daemon/p2p.h:69     p2p server initialized OK
2022-02-12 13:02:33.530     7f3e27c6ca00        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2022-02-12 13:02:33.531     7f3e27c6ca00        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 127.0.0.1 (IPv4):18081
2022-02-12 13:02:34.114     7f3e27c6ca00        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2022-02-12 13:02:34.117     7f3e27c6ca00        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2022-02-12 13:02:34.117 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2022-02-12 13:02:34.117 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:79     Starting p2p net loop...
2022-02-12 13:02:35.118 [P2P3]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    
2022-02-12 13:02:35.118 [P2P3]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    **********************************************************************
2022-02-12 13:02:35.118 [P2P3]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    The daemon will start synchronizing with the network. This may take a long time to complete.
2022-02-12 13:02:35.118 [P2P3]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    
2022-02-12 13:02:35.118 [P2P3]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    You can set the level of process detailization through "set_log <level|categories>" command,
2022-02-12 13:02:35.118 [P2P3]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2022-02-12 13:02:35.118 [P2P3]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    
2022-02-12 13:02:35.118 [P2P3]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    Use the "help" command to see the list of available commands.
2022-02-12 13:02:35.118 [P2P3]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    Use "help <command>" to see a command's documentation.
2022-02-12 13:02:35.118 [P2P3]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1734    **********************************************************************
2022-02-12 13:02:36.090 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:411     [39.108.121.114:18080 OUT] Sync data returned a new top block candidate: 2503305 -> 2557865 [Your node is 54560 blocks (2.5 months) behind] 
2022-02-12 13:02:36.090 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:411     SYNCHRONIZATION started
2022-02-12 13:02:51.592 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:411     [74.135.197.38:18080 OUT] Sync data returned a new top block candidate: 2503305 -> 2557866 [Your node is 54561 blocks (2.5 months) behind] 
2022-02-12 13:02:51.592 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:411     SYNCHRONIZATION started
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x116) [0x556d8a6b09b5]:__cxa_throw+0x116) [0x556d8a6b09b5]
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/local/bin/monerod(+0x127d41) [0x556d8a70cd41] 
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3] /usr/local/bin/monerod(+0x89256d) [0x556d8ae7756d] 
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/local/bin/monerod(+0x64495b) [0x556d8ac2995b] 
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/local/bin/monerod(+0x62c05e) [0x556d8ac1105e] 
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/local/bin/monerod(+0x62c205) [0x556d8ac11205] 
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [7] /usr/local/bin/monerod(+0x62c2b8) [0x556d8ac112b8] 
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/local/bin/monerod(+0x5c4311) [0x556d8aba9311] 
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/local/bin/monerod(+0x68a770) [0x556d8ac6f770] 
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [10]  0xb787) [0x7f3e2a6f8787]:_64-linux-gnu/libboost_thread.so.1.74.0(+0xb787) [0x7f3e2a6f8787]
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [11]  0x8ea7) [0x7f3e2a362ea7]:_64-linux-gnu/libpthread.so.0(+0x8ea7) [0x7f3e2a362ea7]
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0x3f) [0x7f3e2a290def]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f3e2a290def]
2022-02-12 13:03:50.359     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:172  
2022-02-12 13:03:50.743     7f1d357f7700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
```

And then the message repeats after a few minutes. Although I still get some info message on syncing :

```
2022-02-12 13:19:40.724	[P2P0]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1680	Synced 2503405/2557875 (97%, 54470 left, 0% of total synced, estimated 6.0 days left)
2022-02-12 13:19:40.727	    7f1d35cf8700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::runtime_error
2022-02-12 13:19:40.727	    7f1d35cf8700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
```

Should I ignore those message? Yes those stack traces has a log level of INFO, not ERROR, but I didn’t have any of these the first times I ran the program and it synced so far. I only had the INFO messages on the progress of the synchronization, so this is surprising.

Have a nice day.

## selsta | 2022-02-19T00:36:42+00:00
If everything else works fine you can ignore it.

# Action History
- Created by: badfiles | 2021-02-10T10:08:56+00:00
- Closed at: 2022-02-19T00:36:42+00:00
