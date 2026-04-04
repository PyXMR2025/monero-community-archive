---
title: monerod aborting with memory corruption, even with --db-salvage
source_url: https://github.com/monero-project/monero/issues/4983
author: nixn
assignees: []
labels: []
created_at: '2018-12-15T13:58:04+00:00'
updated_at: '2019-01-17T08:07:59+00:00'
type: issue
status: closed
closed_at: '2019-01-17T08:07:59+00:00'
---

# Original Description
here the console output
```
$ ./monerod --data-dir $PWD/data --db-salvage
2018-12-15 13:52:25,700 INFO  [default] Page size: 4096
2018-12-15 13:52:26.704	    7f3e401c4780	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.4-release)
2018-12-15 13:52:26.704	    7f3e401c4780	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-12-15 13:52:26.704	    7f3e401c4780	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-12-15 13:52:26.704	    7f3e401c4780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-12-15 13:52:27.868	    7f3e401c4780	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-12-15 13:52:27.868	    7f3e401c4780	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-12-15 13:52:27.868	    7f3e401c4780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-12-15 13:52:27.869	    7f3e401c4780	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-12-15 13:52:27.869	    7f3e401c4780	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-12-15 13:52:27.869	    7f3e401c4780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:447	Loading blockchain from folder /opt/monero/data/lmdb ...
2018-12-15 13:52:27.933	    7f3e401c4780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:585	Loading checkpoints
2018-12-15 13:52:28.103	    7f3e401c4780	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-12-15 13:52:28.103	    7f3e401c4780	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-12-15 13:52:28.103	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-12-15 13:52:28.104	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-12-15 13:52:29.104	[P2P2]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1489	
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************

2018-12-15 13:52:29.229	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[54.37.87.203:18080 OUT] Sync data returned a new top block candidate: 1699183 -> 1727145 [Your node is 27962 blocks (38 days) behind] 
SYNCHRONIZATION started
*** Error in `./monerod': malloc(): memory corruption: 0x00007f2bcc5e1b90 ***
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x70bfb)[0x7f3e3f5acbfb]
/lib/x86_64-linux-gnu/libc.so.6(+0x76fc6)[0x7f3e3f5b2fc6]
/lib/x86_64-linux-gnu/libc.so.6(+0x79089)[0x7f3e3f5b5089]
/lib/x86_64-linux-gnu/libc.so.6(__libc_malloc+0x54)[0x7f3e3f5b6f64]
./monerod(_Znwm+0x18)[0x55f9811d5128]
./monerod(_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE7reserveEm+0x7d)[0x55f98120bf6d]
./monerod(_ZNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEE8overflowEi+0xe5)[0x55f98124f015]
./monerod(_ZN10cryptonote18transaction_prefix12do_serializeILb1E14binary_archiveEEbRT0_IXT_EE+0x15)[0x55f980c19195]
./monerod(_ZN10cryptonote11transaction19do_serialize_objectILb1E14binary_archiveEEbRT0_IXT_EE+0x2d)[0x55f980c192cd]
./monerod(_ZN10cryptonote29t_serializable_object_to_blobINS_11transactionEEEbRKT_RNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x4b)[0x55f980f3382b]
./monerod(_ZN10cryptonote10tx_to_blobB5cxx11ERKNS_11transactionE+0x25)[0x55f980f2a125]
./monerod(_ZN10cryptonote14BlockchainLMDB20add_transaction_dataERKN6crypto4hashERKNS_11transactionES4_S4_+0x28c)[0x55f980d1297c]
./monerod(_ZN10cryptonote12BlockchainDB15add_transactionERKN6crypto4hashERKNS_11transactionEPS3_S8_+0x164)[0x55f980cd7a44]
./monerod(_ZN10cryptonote12BlockchainDB9add_blockERKNS_5blockEmRKmS5_RKSt6vectorINS_11transactionESaIS7_EE+0x1ac)[0x55f980cd833c]
./monerod(_ZN10cryptonote14BlockchainLMDB9add_blockERKNS_5blockEmRKmS5_RKSt6vectorINS_11transactionESaIS7_EE+0x1b0)[0x55f980d0dc10]
./monerod(_ZN10cryptonote10Blockchain26handle_block_to_main_chainERKNS_5blockERKN6crypto4hashERNS_26block_verification_contextE+0x24f6)[0x55f980d388f6]
./monerod(_ZN10cryptonote10Blockchain13add_new_blockERKNS_5blockERNS_26block_verification_contextE+0x358)[0x55f980d3ea68]
./monerod(_ZN10cryptonote4core21handle_incoming_blockERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERNS_26block_verification_contextEb+0x5c6)[0x55f980d5b116]
./monerod(_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE19try_add_next_blocksERNS_29cryptonote_connection_contextE+0x754)[0x55f980ca9c34]
./monerod(_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE27handle_response_get_objectsEiRNS_27NOTIFY_RESPONSE_GET_OBJECTS7requestERNS_29cryptonote_connection_contextE+0x1621)[0x55f980cada81]
./monerod(_ZN4epee9net_utils17buff_to_t_adapterIN10cryptonote29t_cryptonote_protocol_handlerINS2_4coreEEENS2_27NOTIFY_RESPONSE_GET_OBJECTS7requestENS2_29cryptonote_connection_contextEN5boost3_bi6bind_tIiNS9_4_mfi3mf3IiS5_iRS7_RS8_EENSA_5list4INSA_5valueIPS5_EENS9_3argILi1EEENSL_ILi2EEENSL_ILi3EEEEEEEEEiPT_iRKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEET2_RT1_+0x37a)[0x55f980b3c92a]
./monerod(_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE17handle_invoke_mapINS_29cryptonote_connection_contextEEEibiRKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERSA_RT_Rb+0x222)[0x55f980b3e1a2]
./monerod(_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEEEibiRKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERSF_RT_Rb+0xc2)[0x55f980b3e4b2]
./monerod(_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE6notifyEiRKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEE+0x50)[0x55f980b3e880]
./monerod(_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE11handle_recvEPKvm+0x4ad)[0x55f980cbcf9d]
./monerod(_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x228)[0x55f980cd5be8]
./monerod(_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEESM_mEEEEvRPNS2_11strand_implERT_+0x7a)[0x55f980c9e24a]
./monerod(_ZN5boost4asio6detail18completion_handlerINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS8_5list3INS8_5valueINS_10shared_ptrISN_EEEEPFNS_3argILi1EEEvEPFNSY_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESP_mEES16_EEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESR_m+0x188)[0x55f980c9e6b8]
./monerod(_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x226)[0x55f980c9eaa6]
./monerod(_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESQ_m+0x250)[0x55f980c9ed80]
./monerod(_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationERKNS_6system10error_codeEm+0x1f4)[0x55f980ab42e4]
./monerod(_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x844)[0x55f980c80754]
./monerod(+0x9ff64d)[0x55f9811aa64d]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x7494)[0x7f3e3f8e2494]
/lib/x86_64-linux-gnu/libc.so.6(clone+0x3f)[0x7f3e3f624acf]
======= Memory map: ========
55f9807ab000-55f981577000 r-xp 00000000 00:16 2920569                    /opt/monero/monerod
55f981776000-55f9817b1000 r--p 00dcb000 00:16 2920569                    /opt/monero/monerod
55f9817b1000-55f981800000 rw-p 00e06000 00:16 2920569                    /opt/monero/monerod
55f981800000-55f981801000 rw-p 00000000 00:00 0 
55f981801000-55f98186c000 rw-p 00000000 00:00 0 
55f98272f000-55f9828c2000 rw-p 00000000 00:00 0                          [heap]
7f2b9c000000-7f2b9c106000 rw-p 00000000 00:00 0 
7f2b9c106000-7f2ba0000000 ---p 00000000 00:00 0 
7f2ba0000000-7f2ba0106000 rw-p 00000000 00:00 0 
7f2ba0106000-7f2ba4000000 ---p 00000000 00:00 0 
7f2ba4000000-7f2ba4106000 rw-p 00000000 00:00 0 
7f2ba4106000-7f2ba8000000 ---p 00000000 00:00 0 
7f2ba8000000-7f2ba840e000 rw-p 00000000 00:00 0 
7f2ba840e000-7f2bac000000 ---p 00000000 00:00 0 
7f2bac000000-7f2bac106000 rw-p 00000000 00:00 0 
7f2bac106000-7f2bb0000000 ---p 00000000 00:00 0 
7f2bb0000000-7f2bb06ca000 rw-p 00000000 00:00 0 
7f2bb06ca000-7f2bb4000000 ---p 00000000 00:00 0 
7f2bb4000000-7f2bb436a000 rw-p 00000000 00:00 0 
7f2bb436a000-7f2bb8000000 ---p 00000000 00:00 0 
7f2bb8000000-7f2bb83cd000 rw-p 00000000 00:00 0 
7f2bb83cd000-7f2bbc000000 ---p 00000000 00:00 0 
7f2bbc000000-7f2bbc3e2000 rw-p 00000000 00:00 0 
7f2bbc3e2000-7f2bc0000000 ---p 00000000 00:00 0 
7f2bc0000000-7f2bc0597000 rw-p 00000000 00:00 0 
7f2bc0597000-7f2bc4000000 ---p 00000000 00:00 0 
7f2bc4000000-7f2bc45e8000 rw-p 00000000 00:00 0 
7f2bc45e8000-7f2bc8000000 ---p 00000000 00:00 0 
7f2bc8000000-7f2bc874d000 rw-p 00000000 00:00 0 
7f2bc874d000-7f2bcc000000 ---p 00000000 00:00 0 
7f2bcc000000-7f2bcc1c2000 rw-p 00000000 00:00 0 
7f2bcc1c2000-7f2bcc1c3000 rw-p 00000000 00:00 0 
7f2bcc1c3000-7f2bcc621000 rw-p 00000000 00:00 0 
7f2bcc621000-7f2bd0000000 ---p 00000000 00:00 0 
7f2bd1ffc000-7f2bd1ffd000 ---p 00000000 00:00 0 
7f2bd1ffd000-7f2bd27fd000 rw-p 00000000 00:00 0 
7f2bd27fd000-7f2bd27fe000 ---p 00000000 00:00 0 
7f2bd27fe000-7f2bd2ffe000 rw-p 00000000 00:00 0 
7f2bd2ffe000-7f2bd2fff000 ---p 00000000 00:00 0 
7f2bd2fff000-7f2bd37ff000 rw-p 00000000 00:00 0 
7f2bd37ff000-7f2bd3800000 ---p 00000000 00:00 0 
7f2bd3800000-7f2bd4000000 rw-p 00000000 00:00 0 
7f2bd4000000-7f2bd4021000 rw-p 00000000 00:00 0 
7f2bd4021000-7f2bd8000000 ---p 00000000 00:00 0 
7f2bd85f5000-7f2bd85f6000 ---p 00000000 00:00 0 
7f2bd85f6000-7f2bd8af6000 rw-p 00000000 00:00 0 
7f2bd8af6000-7f2bd8af7000 ---p 00000000 00:00 0 
7f2bd8af7000-7f2bd8ff7000 rw-p 00000000 00:00 0 
7f2bd8ff7000-7f2bd8ff8000 ---p 00000000 00:00 0 
7f2bd8ff8000-7f2bd94f8000 rw-p 00000000 00:00 0 
7f2bd94f8000-7f2bd94f9000 ---p 00000000 00:00 0 
7f2bd94f9000-7f2bd99f9000 rw-p 00000000 00:00 0 
7f2bd99f9000-7f2bd99fa000 ---p 00000000 00:00 0 
7f2bd99fa000-7f2bd9efa000 rw-p 00000000 00:00 0 
7f2bd9efa000-7f2bd9efb000 ---p 00000000 00:00 0 
7f2bd9efb000-7f2bda3fb000 rw-p 00000000 00:00 0 
7f2bda3fb000-7f2bda3fc000 ---p 00000000 00:00 0 
7f2bda3fc000-7f2bda8fc000 rw-p 00000000 00:00 0 
7f2bda8fc000-7f2bda8fd000 ---p 00000000 00:00 0 
7f2bda8fd000-7f2bdadfd000 rw-p 00000000 00:00 0 
7f2bdadfd000-7f2bdadfe000 ---p 00000000 00:00 0 
7f2bdadfe000-7f2bdb2fe000 rw-p 00000000 00:00 0 
7f2bdb2fe000-7f2bdb2ff000 ---p 00000000 00:00 0 
7f2bdb2ff000-7f2bdb7ff000 rw-p 00000000 00:00 0 
7f2bdb7ff000-7f2bdb800000 ---p 00000000 00:00 0 
7f2bdb800000-7f2bdc000000 rw-p 00000000 00:00 0 
7f2bdc000000-7f2bdc021000 rw-p 00000000 00:00 0 
7f2bdc021000-7f2be0000000 ---p 00000000 00:00 0 
7f2be02aa000-7f2be02c0000 r-xp 00000000 00:16 2406849                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7f2be02c0000-7f2be04bf000 ---p 00016000 00:16 2406849                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7f2be04bf000-7f2be04c0000 r--p 00015000 00:16 2406849                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7f2be04c0000-7f2be04c1000 rw-p 00016000 00:16 2406849                    /lib/x86_64-linux-gnu/libgcc_s.so.1
7f2be04c1000-7f2be04c2000 ---p 00000000 00:00 0 
7f2be04c2000-7f2be0cc2000 rw-p 00000000 00:00 0 
7f2be0cc2000-7f2be0cc3000 ---p 00000000 00:00 0 
7f2be0cc3000-7f2be14c3000 rw-p 00000000 00:00 0 
7f2be14c3000-7f2be14c4000 ---p 00000000 00:00 0 
7f2be14c4000-7f2be1cc4000 rw-p 00000000 00:00 0 
7f2be1cc4000-7f2be2110000 r--p 00000000 00:16 2694023                    /usr/lib/locale/locale-archive
7f2be2110000-7f3e2c000000 r--s 00000000 00:16 2920613                    /opt/monero/data/lmdb/data.mdb
7f3e2c000000-7f3e2c2a7000 rw-p 00000000 00:00 0 
7f3e2c2a7000-7f3e30000000 ---p 00000000 00:00 0 
7f3e30000000-7f3e30299000 rw-p 00000000 00:00 0 
7f3e30299000-7f3e34000000 ---p 00000000 00:00 0 
7f3e34000000-7f3e342a7000 rw-p 00000000 00:00 0 
7f3e342a7000-7f3e38000000 ---p 00000000 00:00 0 
7f3e38000000-7f3e383ec000 rw-p 00000000 00:00 0 
7f3e383ec000-7f3e3c000000 ---p 00000000 00:00 0 
7f3e3c12d000-7f3e3c12e000 ---p 00000000 00:00 0 
7f3e3c12e000-7f3e3c92e000 rw-p 00000000 00:00 0 
7f3e3c92e000-7f3e3c92f000 ---p 00000000 00:00 0 
7f3e3c92f000-7f3e3d330000 rw-p 00000000 00:00 0 
7f3e3d330000-7f3e3d331000 ---p 00000000 00:00 0 
7f3e3d331000-7f3e3db31000 rw-p 00000000 00:00 0 
7f3e3db31000-7f3e3db32000 ---p 00000000 00:00 0 
7f3e3db32000-7f3e3e332000 rw-p 00000000 00:00 0 
7f3e3e332000-7f3e3e333000 ---p 00000000 00:00 0 
7f3e3e333000-7f3e3eb33000 rw-p 00000000 00:00 0 
7f3e3eb33000-7f3e3eb34000 ---p 00000000 00:00 0 
7f3e3eb34000-7f3e3f334000 rw-p 00000000 00:00 0 
7f3e3f334000-7f3e3f33b000 r-xp 00000000 00:16 2411012                    /lib/x86_64-linux-gnu/librt-2.24.so
7f3e3f33b000-7f3e3f53a000 ---p 00007000 00:16 2411012                    /lib/x86_64-linux-gnu/librt-2.24.so
7f3e3f53a000-7f3e3f53b000 r--p 00006000 00:16 2411012                    /lib/x86_64-linux-gnu/librt-2.24.so
7f3e3f53b000-7f3e3f53c000 rw-p 00007000 00:16 2411012                    /lib/x86_64-linux-gnu/librt-2.24.so
7f3e3f53c000-7f3e3f6d1000 r-xp 00000000 00:16 2410995                    /lib/x86_64-linux-gnu/libc-2.24.so
7f3e3f6d1000-7f3e3f8d1000 ---p 00195000 00:16 2410995                    /lib/x86_64-linux-gnu/libc-2.24.so
7f3e3f8d1000-7f3e3f8d5000 r--p 00195000 00:16 2410995                    /lib/x86_64-linux-gnu/libc-2.24.so
7f3e3f8d5000-7f3e3f8d7000 rw-p 00199000 00:16 2410995                    /lib/x86_64-linux-gnu/libc-2.24.so
7f3e3f8d7000-7f3e3f8db000 rw-p 00000000 00:00 0 
7f3e3f8db000-7f3e3f8f3000 r-xp 00000000 00:16 2411010                    /lib/x86_64-linux-gnu/libpthread-2.24.so
7f3e3f8f3000-7f3e3faf2000 ---p 00018000 00:16 2411010                    /lib/x86_64-linux-gnu/libpthread-2.24.so
7f3e3faf2000-7f3e3faf3000 r--p 00017000 00:16 2411010                    /lib/x86_64-linux-gnu/libpthread-2.24.so
7f3e3faf3000-7f3e3faf4000 rw-p 00018000 00:16 2411010                    /lib/x86_64-linux-gnu/libpthread-2.24.so
7f3e3faf4000-7f3e3faf8000 rw-p 00000000 00:00 0 
7f3e3faf8000-7f3e3fbfb000 r-xp 00000000 00:16 2410999                    /lib/x86_64-linux-gnu/libm-2.24.so
7f3e3fbfb000-7f3e3fdfa000 ---p 00103000 00:16 2410999                    /lib/x86_64-linux-gnu/libm-2.24.so
7f3e3fdfa000-7f3e3fdfb000 r--p 00102000 00:16 2410999                    /lib/x86_64-linux-gnu/libm-2.24.so
7f3e3fdfb000-7f3e3fdfc000 rw-p 00103000 00:16 2410999                    /lib/x86_64-linux-gnu/libm-2.24.so
7f3e3fdfc000-7f3e3fdff000 r-xp 00000000 00:16 2410998                    /lib/x86_64-linux-gnu/libdl-2.24.so
7f3e3fdff000-7f3e3fffe000 ---p 00003000 00:16 2410998                    /lib/x86_64-linux-gnu/libdl-2.24.so
7f3e3fffe000-7f3e3ffff000 r--p 00002000 00:16 2410998                    /lib/x86_64-linux-gnu/libdl-2.24.so
7f3e3ffff000-7f3e40000000 rw-p 00003000 00:16 2410998                    /lib/x86_64-linux-gnu/libdl-2.24.so
7f3e40000000-7f3e40023000 r-xp 00000000 00:16 2410991                    /lib/x86_64-linux-gnu/ld-2.24.so
7f3e4002c000-7f3e401c9000 rw-p 00000000 00:00 0 
7f3e401c9000-7f3e401e8000 r-xp 00000000 00:16 2857937                    /lib/x86_64-linux-gnu/libudev.so.1.6.5
7f3e401e8000-7f3e401e9000 r--p 0001e000 00:16 2857937                    /lib/x86_64-linux-gnu/libudev.so.1.6.5
7f3e401e9000-7f3e401ea000 rw-p 0001f000 00:16 2857937                    /lib/x86_64-linux-gnu/libudev.so.1.6.5
7f3e4021b000-7f3e4021c000 rw-p 00000000 00:00 0 
7f3e4021c000-7f3e4021e000 rw-s 00000000 00:16 2920612                    /opt/monero/data/lmdb/lock.mdb
7f3e4021e000-7f3e40223000 rw-p 00000000 00:00 0 
7f3e40223000-7f3e40224000 r--p 00023000 00:16 2410991                    /lib/x86_64-linux-gnu/ld-2.24.so
7f3e40224000-7f3e40225000 rw-p 00024000 00:16 2410991                    /lib/x86_64-linux-gnu/ld-2.24.so
7f3e40225000-7f3e40226000 rw-p 00000000 00:00 0 
7fff709a4000-7fff709c7000 rw-p 00000000 00:00 0                          [stack]
7fff709da000-7fff709dd000 r--p 00000000 00:00 0                          [vvar]
7fff709dd000-7fff709df000 r-xp 00000000 00:00 0                          [vdso]
Aborted

```
The log file does not add any additional information. The whole blockchain up to that point was downloaded with exactly this version, before it started crashing.

# Discussion History
## moneromooo-monero | 2018-12-15T16:07:37+00:00
Can you please:

1: give precise version information for the monerod you're running. Is this somehting you've built yourself, or download the binaries off getmonero.org, or elsewhere ?

2: start monerod again with --log-level 2, and paste the resulting log (probably to fpaste.org or paste.debian.net if it's big, and paste the URL here)

3: once that's done, can you run with valgrind ? You just install valgrind, then run the same command, but with "valgrind " in front, eg: valgrind ./monerod --blah, then paste anything valgrind finds.


## nixn | 2018-12-15T18:19:40+00:00
1. this is the official binary version 0.13.0.4 (Linux 64-bit CLI), downloaded from getmonero.org. The `monerod`s sha256sum is `2a986de34b97eb6b516c68598f48a51ef68ee1bed1128661ce537f8bd3ef153e`.

2. https://paste.fedoraproject.org/paste/O6YId8rFeoSvoXj-caT2Yw

3. with valgrind there occures another error: [edited for --show-leak-kinds=all and --log-level 2]
```
$ valgrind --leak-check=full --show-leak-kinds=all ./monerod --data-dir $PWD/data --db-salvage --log-level 2
==1999== Memcheck, a memory error detector
==1999== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==1999== Using Valgrind-3.12.0.SVN and LibVEX; rerun with -h for copyright info
==1999== Command: ./monerod --data-dir /opt/monero/data --db-salvage --log-level 2
==1999== 
2018-12-15 18:30:53,912 INFO  [default] Page size: 4096
2018-12-15 18:30:55.513	         407f880	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.4-release)
2018-12-15 18:30:55.520	         407f880	INFO 	daemon	src/daemon/main.cpp:289	Moving from main() into the daemonize now.
2018-12-15 18:30:55.523	         407f880	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-12-15 18:30:55.524	         407f880	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-12-15 18:30:55.563	         407f880	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-12-15 18:30:55.600	         407f880	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-12-15 18:30:55.606	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:1929	Set limit-up to 2048 kB/s
2018-12-15 18:30:55.608	         407f880	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-12-15 18:30:55.610	         407f880	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-12-15 18:30:55.612	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:1942	Set limit-down to 8192 kB/s
2018-12-15 18:30:55.613	         407f880	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-12-15 18:30:55.614	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:1964	Set limit-up to 2048 kB/s
2018-12-15 18:30:55.615	         407f880	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-12-15 18:30:55.615	         407f880	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-12-15 18:30:55.617	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:1968	Set limit-down to 8192 kB/s
2018-12-15 18:30:55.636	         7706700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2018-12-15 18:30:55.642	         7f07700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2018-12-15 18:30:55.668	         7706700	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2018-12-15 18:30:55.670	         7706700	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2018-12-15 18:30:55.715	         6704700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2018-12-15 18:30:55.883	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2018-12-15 18:30:55.963	         6f05700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2018-12-15 18:30:56.563	         7706700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2018-12-15 18:30:56.586	         6704700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2018-12-15 18:30:56.599	         6704700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2018-12-15 18:30:56.604	         7706700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2018-12-15 18:30:56.672	         7f07700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2018-12-15 18:30:56.673	         7f07700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2018-12-15 18:30:56.754	         6f05700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2018-12-15 18:30:56.754	         6f05700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2018-12-15 18:30:56.762	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2018-12-15 18:30:56.766	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2018-12-15 18:30:56.767	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2018-12-15 18:30:56.767	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2018-12-15 18:30:56.768	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2018-12-15 18:30:56.777	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 107.152.130.98:18080
2018-12-15 18:30:56.783	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=107.152.130.98, port=18080
2018-12-15 18:30:56.802	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 107.152.130.98:18080
2018-12-15 18:30:56.808	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 161.67.132.39:18080
2018-12-15 18:30:56.809	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=161.67.132.39, port=18080
2018-12-15 18:30:56.810	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 161.67.132.39:18080
2018-12-15 18:30:56.810	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 163.172.182.165:18080
2018-12-15 18:30:56.810	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=163.172.182.165, port=18080
2018-12-15 18:30:56.811	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 163.172.182.165:18080
2018-12-15 18:30:56.811	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 195.154.123.123:18080
2018-12-15 18:30:56.812	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=195.154.123.123, port=18080
2018-12-15 18:30:56.812	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 195.154.123.123:18080
2018-12-15 18:30:56.813	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 198.74.231.92:18080
2018-12-15 18:30:56.813	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=198.74.231.92, port=18080
2018-12-15 18:30:56.813	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 198.74.231.92:18080
2018-12-15 18:30:56.814	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 212.83.172.165:18080
2018-12-15 18:30:56.814	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.172.165, port=18080
2018-12-15 18:30:56.814	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.172.165:18080
2018-12-15 18:30:56.815	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 212.83.175.67:18080
2018-12-15 18:30:56.815	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.175.67, port=18080
2018-12-15 18:30:56.816	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.175.67:18080
2018-12-15 18:30:56.816	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 5.9.100.248:18080
2018-12-15 18:30:56.817	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=5.9.100.248, port=18080
2018-12-15 18:30:56.817	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 5.9.100.248:18080
2018-12-15 18:30:56.818	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:535	Number of seed nodes: 8
2018-12-15 18:30:56.985	         407f880	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 2 from name: P2P, prefix_name = P2P
2018-12-15 18:30:56.987	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:571	Binding on 0.0.0.0:18080
2018-12-15 18:30:56.999	         407f880	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:846	start accept
2018-12-15 18:30:57.013	         407f880	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:163	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2018-12-15 18:30:57.023	         407f880	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:92	test, connection constructor set m_connection_type=2
2018-12-15 18:30:57.030	         407f880	INFO 	net.p2p	src/p2p/net_node.inl:576	Net service bound to 0.0.0.0:18080
2018-12-15 18:30:57.031	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:2031	Attempting to add IGD port mapping.
2018-12-15 18:30:58.111	         407f880	WARN 	net.p2p	src/p2p/net_node.inl:2061	IGD was found but reported as not connected.
2018-12-15 18:30:58.114	         407f880	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-12-15 18:30:58.193	         407f880	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-12-15 18:30:58.197	         407f880	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 1 from name: RPC, prefix_name = RPC
2018-12-15 18:30:58.207	         407f880	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-12-15 18:30:58.218	         407f880	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:846	start accept
2018-12-15 18:30:58.219	         407f880	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:163	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2018-12-15 18:30:58.225	         407f880	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:92	test, connection constructor set m_connection_type=1
2018-12-15 18:30:58.229	         407f880	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-12-15 18:30:58.241	         407f880	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-12-15 18:30:58.297	         407f880	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:447	Loading blockchain from folder /opt/monero/data/lmdb ...
2018-12-15 18:30:58.317	         407f880	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:475	option: fast
2018-12-15 18:30:58.318	         407f880	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:475	option: async
2018-12-15 18:30:58.318	         407f880	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:475	option: 250000000bytes
2018-12-15 18:30:58.347	         407f880	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to open lmdb environment: Invalid argument
2018-12-15 18:30:58.503	         407f880	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:548	Error opening database: Failed to open lmdb environment: Invalid argument
2018-12-15 18:30:58.582	         407f880	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-12-15 18:30:58.589	         407f880	DEBUG	net	contrib/epee/include/net/net_helper.h:513	Problems at cancel: Bad file descriptor
2018-12-15 18:30:58.591	         407f880	DEBUG	net	contrib/epee/include/net/net_helper.h:516	Problems at shutdown: Bad file descriptor
2018-12-15 18:30:58.619	         407f880	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:171	Destructing connection p2p#0 to 0.0.0.0
2018-12-15 18:30:58.628	         407f880	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-12-15 18:30:58.629	         407f880	INFO 	net	src/p2p/net_node.h:250	Killing the net_node
2018-12-15 18:30:58.630	         407f880	INFO 	net	src/p2p/net_node.h:254	Joined extra background net_node threads
2018-12-15 18:30:58.632	         407f880	DEBUG	net.p2p	src/p2p/net_node.inl:2077	Attempting to delete IGD port mapping.
2018-12-15 18:30:59.653	         407f880	WARN 	net.p2p	src/p2p/net_node.inl:2104	IGD was found but reported as not connected.
2018-12-15 18:30:59.750	         407f880	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:171	Destructing connection p2p#0 to 0.0.0.0
2018-12-15 18:30:59.779	         407f880	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-12-15 18:30:59.783	         407f880	DEBUG	miner	src/cryptonote_basic/miner.cpp:362	Not mining - nothing to stop
2018-12-15 18:30:59.807	         407f880	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2018-12-15 18:30:59.813	         407f880	DEBUG	miner	src/cryptonote_basic/miner.cpp:362	Not mining - nothing to stop
2018-12-15 18:30:59.819	         407f880	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-12-15 18:30:59.820	         407f880	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
==1999== 
==1999== HEAP SUMMARY:
==1999==     in use at exit: 73,944 bytes in 8 blocks
==1999==   total heap usage: 29,801 allocs, 29,793 frees, 18,931,905 bytes allocated
==1999== 
==1999== 24 bytes in 1 blocks are still reachable in loss record 1 of 8
==1999==    at 0x4C2BBAF: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==1999==    by 0x9F3157: CRYPTO_malloc (in /opt/monero/monerod)
==1999==    by 0xA2D435: lh_insert (in /opt/monero/monerod)
==1999==    by 0xA2DF93: int_thread_set_item (in /opt/monero/monerod)
==1999==    by 0xA2EB8D: ERR_get_state (in /opt/monero/monerod)
==1999==    by 0xA2ED1E: ERR_clear_error (in /opt/monero/monerod)
==1999==    by 0x540451: cryptonote::core_rpc_server::core_rpc_server(cryptonote::core&, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >&) (in /opt/monero/monerod)
==1999==    by 0x483B3A: daemonize::t_rpc::t_rpc(boost::program_options::variables_map const&, daemonize::t_core&, daemonize::t_p2p&, bool, cryptonote::network_type, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (in /opt/monero/monerod)
==1999==    by 0x486184: daemonize::t_internals::t_internals(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4052FB: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4C0630: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4C763D: bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999== 
==1999== 32 bytes in 1 blocks are still reachable in loss record 2 of 8
==1999==    at 0x4C2BBAF: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==1999==    by 0x9F3157: CRYPTO_malloc (in /opt/monero/monerod)
==1999==    by 0xA2C8CE: sk_new (in /opt/monero/monerod)
==1999==    by 0x9CF739: load_builtin_compressions (in /opt/monero/monerod)
==1999==    by 0x9D1838: SSL_COMP_get_compression_methods (in /opt/monero/monerod)
==1999==    by 0x9D61D2: SSL_library_init (in /opt/monero/monerod)
==1999==    by 0x3F05F8: boost::asio::ssl::detail::openssl_init_base::instance() (in /opt/monero/monerod)
==1999==    by 0x3D803A: _GLOBAL__sub_I_command_parser_executor.cpp (in /opt/monero/monerod)
==1999==    by 0xBCD25C: __libc_csu_init (in /opt/monero/monerod)
==1999==    by 0x557D26F: (below main) (libc-start.c:247)
==1999== 
==1999== 32 bytes in 1 blocks are still reachable in loss record 3 of 8
==1999==    at 0x4C2BBAF: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==1999==    by 0x9F3157: CRYPTO_malloc (in /opt/monero/monerod)
==1999==    by 0xA2C8EC: sk_new (in /opt/monero/monerod)
==1999==    by 0x9CF739: load_builtin_compressions (in /opt/monero/monerod)
==1999==    by 0x9D1838: SSL_COMP_get_compression_methods (in /opt/monero/monerod)
==1999==    by 0x9D61D2: SSL_library_init (in /opt/monero/monerod)
==1999==    by 0x3F05F8: boost::asio::ssl::detail::openssl_init_base::instance() (in /opt/monero/monerod)
==1999==    by 0x3D803A: _GLOBAL__sub_I_command_parser_executor.cpp (in /opt/monero/monerod)
==1999==    by 0xBCD25C: __libc_csu_init (in /opt/monero/monerod)
==1999==    by 0x557D26F: (below main) (libc-start.c:247)
==1999== 
==1999== 128 bytes in 1 blocks are still reachable in loss record 4 of 8
==1999==    at 0x4C2BBAF: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==1999==    by 0x9F3157: CRYPTO_malloc (in /opt/monero/monerod)
==1999==    by 0xA2D101: lh_new (in /opt/monero/monerod)
==1999==    by 0xA2DC42: int_thread_get (in /opt/monero/monerod)
==1999==    by 0xA2DF5F: int_thread_set_item (in /opt/monero/monerod)
==1999==    by 0xA2EB8D: ERR_get_state (in /opt/monero/monerod)
==1999==    by 0xA2ED1E: ERR_clear_error (in /opt/monero/monerod)
==1999==    by 0x540451: cryptonote::core_rpc_server::core_rpc_server(cryptonote::core&, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >&) (in /opt/monero/monerod)
==1999==    by 0x483B3A: daemonize::t_rpc::t_rpc(boost::program_options::variables_map const&, daemonize::t_core&, daemonize::t_p2p&, bool, cryptonote::network_type, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (in /opt/monero/monerod)
==1999==    by 0x486184: daemonize::t_internals::t_internals(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4052FB: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4C0630: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999== 
==1999== 176 bytes in 1 blocks are still reachable in loss record 5 of 8
==1999==    at 0x4C2BBAF: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==1999==    by 0x9F3157: CRYPTO_malloc (in /opt/monero/monerod)
==1999==    by 0xA2D0DF: lh_new (in /opt/monero/monerod)
==1999==    by 0xA2DC42: int_thread_get (in /opt/monero/monerod)
==1999==    by 0xA2DF5F: int_thread_set_item (in /opt/monero/monerod)
==1999==    by 0xA2EB8D: ERR_get_state (in /opt/monero/monerod)
==1999==    by 0xA2ED1E: ERR_clear_error (in /opt/monero/monerod)
==1999==    by 0x540451: cryptonote::core_rpc_server::core_rpc_server(cryptonote::core&, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >&) (in /opt/monero/monerod)
==1999==    by 0x483B3A: daemonize::t_rpc::t_rpc(boost::program_options::variables_map const&, daemonize::t_core&, daemonize::t_p2p&, bool, cryptonote::network_type, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (in /opt/monero/monerod)
==1999==    by 0x486184: daemonize::t_internals::t_internals(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4052FB: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4C0630: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999== 
==1999== 248 bytes in 1 blocks are definitely lost in loss record 6 of 8
==1999==    at 0x4C2DBC5: calloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==1999==    by 0xBCE4A7: mdb_env_create (in /opt/monero/monerod)
==1999==    by 0x66B4C0: cryptonote::BlockchainLMDB::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int) (in /opt/monero/monerod)
==1999==    by 0x6B92D0: cryptonote::core::init(boost::program_options::variables_map const&, char const*, cryptonote::test_options const*) (in /opt/monero/monerod)
==1999==    by 0x429D42: daemonize::t_core::run() (in /opt/monero/monerod)
==1999==    by 0x407A09: daemonize::t_daemon::run(bool) (in /opt/monero/monerod)
==1999==    by 0x4C063D: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4C763D: bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x3DB234: main (in /opt/monero/monerod)
==1999== 
==1999== 600 bytes in 1 blocks are still reachable in loss record 7 of 8
==1999==    at 0x4C2BBAF: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==1999==    by 0x9F3157: CRYPTO_malloc (in /opt/monero/monerod)
==1999==    by 0xA2EB25: ERR_get_state (in /opt/monero/monerod)
==1999==    by 0xA2ED1E: ERR_clear_error (in /opt/monero/monerod)
==1999==    by 0x540451: cryptonote::core_rpc_server::core_rpc_server(cryptonote::core&, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >&) (in /opt/monero/monerod)
==1999==    by 0x483B3A: daemonize::t_rpc::t_rpc(boost::program_options::variables_map const&, daemonize::t_core&, daemonize::t_p2p&, bool, cryptonote::network_type, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (in /opt/monero/monerod)
==1999==    by 0x486184: daemonize::t_internals::t_internals(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4052FB: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4C0630: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x4C763D: bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) (in /opt/monero/monerod)
==1999==    by 0x3DB234: main (in /opt/monero/monerod)
==1999== 
==1999== 72,704 bytes in 1 blocks are still reachable in loss record 8 of 8
==1999==    at 0x4C2BBAF: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==1999==    by 0x3E506F: _GLOBAL__sub_I_eh_alloc.cc (in /opt/monero/monerod)
==1999==    by 0xBCD25C: __libc_csu_init (in /opt/monero/monerod)
==1999==    by 0x557D26F: (below main) (libc-start.c:247)
==1999== 
==1999== LEAK SUMMARY:
==1999==    definitely lost: 248 bytes in 1 blocks
==1999==    indirectly lost: 0 bytes in 0 blocks
==1999==      possibly lost: 0 bytes in 0 blocks
==1999==    still reachable: 73,696 bytes in 7 blocks
==1999==         suppressed: 0 bytes in 0 blocks
==1999== 
==1999== For counts of detected and suppressed errors, rerun with: -v
==1999== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```

## moneromooo-monero | 2018-12-15T22:24:57+00:00
This run with valgrind doesn't seem to have had any trouble. Can you please get a valgrind log when the error happens ?


## hyc | 2018-12-16T00:56:08+00:00
It failed to open the LMDB environment. I think this is the usual "valgrind doesn't support large mmaps" problem, which can only be fixed by recompiling valgrind with a larger map size limit.

## moneromooo-monero | 2018-12-16T01:01:20+00:00
Alternatively, there's ASAN, but that requires building monero (with -fsanitize=address).

## nixn | 2018-12-17T08:21:06+00:00
Now I tried with a newer valgrind, 3.14.0 (because of [this SO answer](https://stackoverflow.com/a/8649363)), but it did not help, still failing to initialize the LMDB environment.

While I could (try to) re-compile either valgrind with more mem or monerod with ASAN, it would be much easier and faster if I could take the one or the other pre-compiled somewhere. If you could point me in the right direction, I would try that.

## moneromooo-monero | 2018-12-17T09:21:07+00:00
I'll build a debug monerod from the 0.13 branch.
In the meantime, I tried syncing over that block from that peer, and didn't get anything wrong.


## moneromooo-monero | 2018-12-17T20:53:31+00:00
https://github.com/moneromooo-monero/bitmonero/blob/6db531e988097d0d2bb54d94c5b71608662c70ad/monerod

## nixn | 2018-12-17T21:16:44+00:00
Thanks for that, but I can't run it because it is missing several dynamically loaded libs:
```
$ ldd ./monerod-dbg
	linux-vdso.so.1 (0x00007ffc9a66b000)
	librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f1e243ea000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f1e241e6000)
	libdaemonizer.so => not found
	libdaemon_rpc_server.so => not found
	libboost_chrono.so.1.65.1 => not found
	libboost_filesystem.so.1.65.1 => not found
	libboost_program_options.so.1.65.1 => not found
	libboost_regex.so.1.65.1 => not found
	libboost_system.so.1.65.1 => not found
	libzmq.so.5 => /usr/lib/x86_64-linux-gnu/libzmq.so.5 (0x00007f1e23f5c000)
	libsodium.so.23 => not found
	libreadline.so.7 => /lib/x86_64-linux-gnu/libreadline.so.7 (0x00007f1e23d0f000)
	librpc.so => not found
	librpc_base.so => not found
	libserialization.so => not found
	libcryptonote_protocol.so => not found
	libp2p.so => not found
	libcryptonote_core.so => not found
	libblockchain_db.so => not found
	liblmdb.so => not found
	libmultisig.so => not found
	libringct.so => not found
	libcryptonote_basic.so => not found
	libcheckpoints.so => not found
	libdevice.so => not found
	libhidapi-libusb.so.0 => /usr/lib/x86_64-linux-gnu/libhidapi-libusb.so.0 (0x00007f1e23b07000)
	libringct_basic.so => not found
	libcommon.so => not found
	libcncrypto.so => not found
	libssl.so.1.1 => /usr/lib/x86_64-linux-gnu/libssl.so.1.1 (0x00007f1e2389b000)
	libunbound.so.2 => /usr/lib/x86_64-linux-gnu/libunbound.so.2 (0x00007f1e235fb000)
	libunwind.so.8 => /usr/lib/x86_64-linux-gnu/libunwind.so.8 (0x00007f1e233e0000)
	libcrypto.so.1.1 => /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1 (0x00007f1e22f4d000)
	libboost_date_time.so.1.65.1 => not found
	libversion.so => not found
	libboost_thread.so.1.65.1 => not found
	libboost_serialization.so.1.65.1 => not found
	libeasylogging.so => not found
	libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f1e22bcb000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f1e228c7000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f1e226aa000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f1e22493000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f1e220f4000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f1e2622c000)
	libsodium.so.18 => /usr/lib/x86_64-linux-gnu/libsodium.so.18 (0x00007f1e21e8e000)
	libpgm-5.2.so.0 => /usr/lib/x86_64-linux-gnu/libpgm-5.2.so.0 (0x00007f1e21c41000)
	libtinfo.so.5 => /lib/x86_64-linux-gnu/libtinfo.so.5 (0x00007f1e21a17000)
	libusb-1.0.so.0 => /lib/x86_64-linux-gnu/libusb-1.0.so.0 (0x00007f1e217fe000)
	libhogweed.so.4 => /usr/lib/x86_64-linux-gnu/libhogweed.so.4 (0x00007f1e215c9000)
	libnettle.so.6 => /usr/lib/x86_64-linux-gnu/libnettle.so.6 (0x00007f1e21392000)
	libgmp.so.10 => /usr/lib/x86_64-linux-gnu/libgmp.so.10 (0x00007f1e2110f000)
	liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5 (0x00007f1e20ee9000)
	libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007f1e263e3000)
```

In contrast, the original monerod has a very short list of dynamic libs:
```
$ ldd monerod
	linux-vdso.so.1 (0x00007ffca412d000)
	libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007fc16dd9e000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fc16c910000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fc16c60c000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fc16c3ef000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fc16c050000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fc16dbd5000)
	librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007fc16be48000)
```
Perhaps you can build it (mostly) statically (like the release version)? Or shall I better try to get every dependency installed? I'm on Debian Stretch.

## moneromooo-monero | 2018-12-17T21:55:00+00:00
Alright, I'll build boost with PIC, you'll have a binary in another day.

## moneromooo-monero | 2018-12-18T00:40:01+00:00
https://github.com/moneromooo-monero/bitmonero/blob/94701d6573f0ff79a00c35015fda28101eba2903/monerod.xz

## moneromooo-monero | 2018-12-18T00:40:32+00:00
Some libs are still dynamic. Hopefully that's enough.

## nixn | 2018-12-19T00:25:00+00:00
Thanks again, this one nearly works... Had to install only libsodium23 to make ldd happy, no problem with that. But now I encounter a glibc version mismatch:
```
$ ./monerod-dbg2 --data-dir $PWD/data --db-salvage --log-level 2
./monerod-dbg2: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.27' not found (required by ./monerod-dbg2)
```
As I said earlier I'm on Debian Stretch, which runs libc6 2.24 ([2.24-11+deb9u3 precisely atm](https://packages.debian.org/stretch/libc6)). If it's not too difficult for you, would you mind to compile another binary ready for this version?

## nixn | 2018-12-19T10:53:30+00:00
After some consideration I will update libc6 to Debian Buster (2.28) and try again running. I will report the results then.

## moneromooo-monero | 2018-12-19T10:54:31+00:00
I can make one with 2.19 (ie, earlier than yours), not sure that'd be OK or it if wants exact match.

## nixn | 2018-12-19T16:46:17+00:00
So I upgraded libc6 to 2.28 and ran monerod again, both the original and the dbg2 version, both of which abort with different errors now. The original stops with `malloc(): invalid size (unsorted)`, the dbg2 stops with `Illegal instruction`, both errors out of nowhere and without a stack trace or anything. I cannot even reliably tell when it happens.

Now I returned to the 2.24 version of libc6. The try with 2.28 was unsuccessful (and frustrating) and I would like to try the version you are offering. The "low" version (2.19) should not be a problem, the dbg2 version compiled against 2.27 also did run on 2.28. At least I hope so…

## moneromooo-monero | 2018-12-21T19:36:59+00:00
No need for 2.19 then, you'll still get invalid instruction. What is your CPU ?

## nixn | 2018-12-21T21:54:05+00:00
```
$ lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                4
On-line CPU(s) list:   0-3
Thread(s) per core:    1
Core(s) per socket:    4
Socket(s):             1
NUMA node(s):          1
Vendor ID:             AuthenticAMD
CPU family:            16
Model:                 4
Model name:            AMD Phenom(tm) II X4 965 Processor
Stepping:              3
CPU MHz:               2200.000
CPU max MHz:           3400,0000
CPU min MHz:           800,0000
BogoMIPS:              6785.07
Virtualization:        AMD-V
L1d cache:             64K
L1i cache:             64K
L2 cache:              512K
L3 cache:              6144K
NUMA node0 CPU(s):     0-3
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm 3dnowext 3dnow constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid pni monitor cx16 popcnt lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt nodeid_msr hw_pstate vmmcall npt lbrv svm_lock nrip_save
```
```
$ uname -a
Linux nix-pc 4.18.0-0.bpo.1-amd64 #1 SMP Debian 4.18.6-1~bpo9+1 (2018-09-13) x86_64 GNU/Linux
```

## moneromooo-monero | 2018-12-29T12:48:39+00:00
I assume you can compile some random small program that uses malloc with the same compiler and it doesn't die the same way ?

## nixn | 2019-01-04T09:27:24+00:00
Which compiler do you mean? I did not compile anything for monerod, it always was the binary you provided to me (the official version or the debug versions from this thread).

But to possibly answer your question: I compiled the small program from https://en.cppreference.com/w/cpp/memory/c/malloc and it does not die or do anything unexpected.

## moneromooo-monero | 2019-01-04T12:11:46+00:00
If you just ran a binary, it does not apply.
If you're getting consistent malloc corruption and I don't, with the same binary, it points to your glibc or other dynamically linked libs. But if it was your glibc, your system would likely die often, so I'm not sure what to do now if you can't build with ASAN or run with valgrind.


## moneromooo-monero | 2019-01-04T12:13:12+00:00
Unless it's "the original binary always dies of malloc corruption" and "the binary from mooo always dies with illegal insn". That seems more likely. In that case you need to build the binary on your particular arch.

## nixn | 2019-01-04T14:16:13+00:00
Ok, I will try to compile monerd myself and will report results.

Edit: just found the Debian stretch-backports version of monero. I will test it too and likely stick to it (if it works ofc.), but I will still compile it myself (already running) to verify the issue.
Btw. thanks for the easy compilation steps.

## nixn | 2019-01-05T22:45:09+00:00
Both, the self-compiled and the Debian version of monerod, throw this error! What could I do now to pinpoint the error?

## moneromooo-monero | 2019-01-05T23:14:50+00:00
This error is... invalid instruction, or the malloc corruption error ?

## nixn | 2019-01-06T08:07:18+00:00
Sorry. It's the malloc corruption error. The other one was only with the debug binary.

## moneromooo-monero | 2019-01-06T11:30:02+00:00
Is the self compiled one built with ASAN ? If not, add "-D SANITIZE=ON" to the cmake command line.

## nixn | 2019-01-07T20:15:43+00:00
So I created a new target `release-asan` in the top Makefile, it should be the same as the target `release` but with `-D SANITIZE=ON`:
```diff
diff --git a/Makefile b/Makefile
index 40b8839c..1b365b66 100644
--- a/Makefile
+++ b/Makefile
@@ -89,6 +89,10 @@ release-static:
        mkdir -p $(builddir)/release
        cd $(builddir)/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release $(topdir) && $(MAKE)
 
+release-asan:
+       mkdir -p $(builddir)/release-asan
+       cd $(builddir)/release-asan && cmake -D CMAKE_BUILD_TYPE=Release -D SANITIZE=ON $(topdir) && $(MAKE)
+
 coverage:
        mkdir -p $(builddir)/debug
        cd $(builddir)/debug && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=Debug -D COVERAGE=ON $(topdir) && $(MAKE) && $(MAKE) test
```
But `make release-asan` stops with the following error:
```
[ 89%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/bin/ld: ../../external/db_drivers/liblmdb/liblmdb.a(mdb.c.o): undefined reference to symbol 'pthread_mutexattr_setrobust@@GLIBC_2.12'
//lib/x86_64-linux-gnu/libpthread.so.0: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:136: recipe for target 'bin/monero-wallet-rpc' failed
```
According to [this answer](https://stackoverflow.com/a/46554419) I checked the existence of that symbol:
```
$ readelf -Ws /lib/x86_64-linux-gnu/libpthread.so.0 | grep pthread_mutexattr_setrobust
    92: 00000000000115a0    38 FUNC    GLOBAL DEFAULT   14 pthread_mutexattr_setrobust@@GLIBC_2.12
   332: 00000000000115a0    38 FUNC    WEAK   DEFAULT   14 pthread_mutexattr_setrobust_np@@GLIBC_2.4
   725: 00000000000115a0    38 FUNC    WEAK   DEFAULT   14 pthread_mutexattr_setrobust_np
   745: 00000000000115a0    38 FUNC    GLOBAL DEFAULT   14 pthread_mutexattr_setrobust
```
… and now I'm lost on where to add `-pthread` or `-lpthread` or how to add it properly (probably the CMake-way). Or should I do something else?

## moneromooo-monero | 2019-01-07T20:21:58+00:00
Try this:

<pre>
diff --git a/CMakeLists.txt b/CMakeLists.txt
index 31c3dbd21..e5178131b 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -933,6 +933,7 @@ if (HIDAPI_FOUND OR LibUSB_COMPILE_TEST_PASSED)
     list(APPEND EXTRA_LIBRARIES setupapi)
   endif()
 endif()
+list(APPEND EXTRA_LIBRARIES -lpthread)
 
 option(USE_READLINE "Build with GNU readline support." ON)
 if(USE_READLINE)

</pre>



## nixn | 2019-01-07T20:50:20+00:00
Thanks, now compilation worked. Running yields the following:
```
$ ~/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod --data-dir $PWD/data --db-salvage --log-level 2
2019-01-07 20:40:51,624 INFO  [default] Page size: 4096
2019-01-07 20:40:52.663	    7fbfb72e37c0	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.4-release)
2019-01-07 20:40:52.664	    7fbfb72e37c0	INFO 	daemon	src/daemon/main.cpp:289	Moving from main() into the daemonize now.
2019-01-07 20:40:52.664	    7fbfb72e37c0	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2019-01-07 20:40:52.665	    7fbfb72e37c0	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2019-01-07 20:40:52.666	    7fbfb72e37c0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2019-01-07 20:40:52.667	    7fbfb72e37c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2019-01-07 20:40:52.667	    7fbfb72e37c0	INFO 	net.p2p	src/p2p/net_node.inl:1929	Set limit-up to 2048 kB/s
2019-01-07 20:40:52.667	    7fbfb72e37c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2019-01-07 20:40:52.667	    7fbfb72e37c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2019-01-07 20:40:52.667	    7fbfb72e37c0	INFO 	net.p2p	src/p2p/net_node.inl:1942	Set limit-down to 8192 kB/s
2019-01-07 20:40:52.667	    7fbfb72e37c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2019-01-07 20:40:52.667	    7fbfb72e37c0	INFO 	net.p2p	src/p2p/net_node.inl:1964	Set limit-up to 2048 kB/s
2019-01-07 20:40:52.667	    7fbfb72e37c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2019-01-07 20:40:52.667	    7fbfb72e37c0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2019-01-07 20:40:52.667	    7fbfb72e37c0	INFO 	net.p2p	src/p2p/net_node.inl:1968	Set limit-down to 8192 kB/s
2019-01-07 20:40:52.668	    7fbfadcff700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2019-01-07 20:40:52.669	    7fbfad4fe700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2019-01-07 20:40:52.670	    7fbfaccfd700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2019-01-07 20:40:52.670	    7fbfb72e37c0	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2019-01-07 20:40:52.671	    7fbfac4fc700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2019-01-07 20:40:52.672	    7fbfadcff700	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2019-01-07 20:40:52.672	    7fbfadcff700	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

=================================================================
==25478==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7fbfac4fb070 at pc 0x561df90f857a bp 0x7fbfac4fb020 sp 0x7fbfac4fb018
READ of size 4 at 0x7fbfac4fb070 thread T4
==25478==AddressSanitizer: while reporting a bug found another one. Ignoring.
==25478==AddressSanitizer: while reporting a bug found another one. Ignoring.
==25478==AddressSanitizer: while reporting a bug found another one. Ignoring.
    #0 0x561df90f8579 in hashlittle (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xc5d579)
    #1 0x561df9072877 in rrset_key_hash (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xbd7877)
    #2 0x561df90595cd in rrset_cache_lookup (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xbbe5cd)
    #3 0x561df917412c in dns_cache_lookup (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xcd912c)
    #4 0x561df9183cba in processInitRequest (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xce8cba)
    #5 0x561df9187a8a in iter_handle (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xceca8a)
    #6 0x561df918d9b0 in iter_operate (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xcf29b0)
    #7 0x561df908ba82 in mesh_run (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xbf0a82)
    #8 0x561df908cfb6 in mesh_new_callback (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xbf1fb6)
    #9 0x561df9028a06 in libworker_fg (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xb8da06)
    #10 0x561df901de33 in ub_resolve (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xb82e33)
    #11 0x561df8da5f47 in tools::DNSResolver::get_record(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0x90af47)
    #12 0x561df8da64f8 in tools::DNSResolver::get_ipv4(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool&, bool&) (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0x90b4f8)
    #13 0x561df8ba0c97 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&)::{lambda()#1}::operator()() const (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0x705c97)
    #14 0x7fbfb355d115  (/usr/lib/x86_64-linux-gnu/libboost_thread.so.1.62.0+0x12115)
    #15 0x7fbfb5b4d493 in start_thread (/lib/x86_64-linux-gnu/libpthread.so.0+0x7493)
    #16 0x7fbfb29f7ace in __clone (/lib/x86_64-linux-gnu/libc.so.6+0xe8ace)

Address 0x7fbfac4fb070 is located in stack of thread T4 at offset 32 in frame
    #0 0x561df90727af in rrset_key_hash (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xbd77af)

  This frame has 1 object(s):
    [32, 34) 't' <== Memory access at offset 32 partially overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
Thread T4 created by T0 here:
    #0 0x7fbfb619ff59 in __interceptor_pthread_create (/usr/lib/x86_64-linux-gnu/libasan.so.3+0x30f59)
    #1 0x7fbfb355c478 in boost::thread::start_thread_noexcept() (/usr/lib/x86_64-linux-gnu/libboost_thread.so.1.62.0+0x11478)

SUMMARY: AddressSanitizer: stack-buffer-overflow (/home/nix/devel-other/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release-asan/bin/monerod+0xc5d579) in hashlittle
Shadow bytes around the buggy address:
  0x0ff8758975b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8758975c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8758975d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8758975e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff8758975f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0ff875897600: 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1[02]f4
  0x0ff875897610: f4 f4 f3 f3 f3 f3 00 00 00 00 00 00 00 00 00 00
  0x0ff875897620: f1 f1 f1 f1 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff875897630: 00 00 00 f4 f3 f3 f3 f3 00 00 00 00 00 00 00 00
  0x0ff875897640: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff875897650: 00 00 00 00 f1 f1 f1 f1 00 f4 f4 f4 f2 f2 f2 f2
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==25478==ABORTING
```
I'm not sure, but it seems to me to not be the original error.

## moneromooo-monero | 2019-01-07T23:30:37+00:00
It looks like a bug in your copy of libunbound.
Are you using a system one, or the source bundled with monero ?
"ldd monerod" will tell you.

## nixn | 2019-01-07T23:57:20+00:00
It must be the bundled one, because ldd does not list it and I did not even install the dev package in my system.
But cmake seems to have omitted it?
```
$ grep UNBOUND release-asan/CMakeCache.txt 
INSTALL_VENDORED_LIBUNBOUND:BOOL=OFF
UNBOUND_CHROOT_DIR:STRING=/usr/local/etc/unbound
UNBOUND_CONFIGFILE:STRING=/usr/local/etc/unbound/unbound.conf
UNBOUND_INCLUDE_DIR:PATH=UNBOUND_INCLUDE_DIR-NOTFOUND
UNBOUND_LIBRARIES:FILEPATH=UNBOUND_LIBRARIES-NOTFOUND
UNBOUND_PIDFILE:STRING=/usr/local/etc/unbound/unbound.pid
UNBOUND_RUN_DIR:STRING=/usr/local/etc/unbound
UNBOUND_SHARE_DIR:STRING=/usr/local/etc/unbound
UNBOUND_USERNAME:STRING=unbound
```

## moneromooo-monero | 2019-01-08T00:26:23+00:00
That jerk code overreads on purpose...

In external/unbound/util/storage/lookup3.c, add "#define VALGRIND 1" before this line:
uint32_t hashlittle( const void *key, size_t length, uint32_t initval)

## nixn | 2019-01-08T00:57:37+00:00
Now we're getting somewhere… [monerod-asan.log](https://github.com/monero-project/monero/files/2734816/monerod-asan.log)


## moneromooo-monero | 2019-01-08T11:13:28+00:00
Looks like a corrupt db. LMDB has a tendency to crash like this on corrupt data unfortunately. Thankfully the db is not under attacker control so this is no vulnerability (unless someone can alter your db file).
I asked hyc (the author of this code) for a double check.
Did the machine with the blockchain crash, go out of power, that kind of thing ?

## nixn | 2019-01-08T12:30:13+00:00
I cannot tell reliably, but it could be. I had issues with the underlying BTRFS, which remounted ro automatically, so a write could have been not completed properly. Or some random freezes for whatever reason.
Shouldn't the LMDB be crash-proof for exactly those kind of failures?

## moneromooo-monero | 2019-01-08T12:53:50+00:00
It is if you use the safe mode (see --db-sync-mode). Recent monero switches to safe mode once initial sync is finished. If you get a crash without safe mode on, then you risk corruption.

## nixn | 2019-01-08T20:13:56+00:00
I used it from the beginning (at least I think so):
```
$ cat data/bitmonero.conf
no-igd
enforce-dns-checkpointing
db-sync-mode safe:async
prep-blocks-threads 2
```
So now I have to re-download the whole chain. That's ok, I hope it works this time. When it's finished and working, I would close the issue then.

## nixn | 2019-01-08T20:43:57+00:00
Ouch! I realized now that the configuration file was not even read, so it was not running in safe mode. The file is even wrong and prevented the restart after some tweaking of paths. I thought setting `--data-dir` would suffice, if the config file is in there as `bitmonero.conf`.

I'm very sorry for bothering you with my stupidity :-(

## nixn | 2019-01-17T08:07:59+00:00
Finally in the new try the whole chain downloaded successfully and everything is working as expected. Thanks for your help and patience.

# Action History
- Created by: nixn | 2018-12-15T13:58:04+00:00
- Closed at: 2019-01-17T08:07:59+00:00
