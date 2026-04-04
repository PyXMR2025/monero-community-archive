---
title: ' malloc(): memory corruption'
source_url: https://github.com/monero-project/monero/issues/4841
author: alextrezvy
assignees: []
labels: []
created_at: '2018-11-12T20:16:32+00:00'
updated_at: '2018-11-13T10:33:03+00:00'
type: issue
status: closed
closed_at: '2018-11-13T10:32:45+00:00'
---

# Original Description
Ubuntu 16.04, monero 0.13.0.4, 8 GB RAM:

> *** Error in `./monerod': malloc(): memory corruption: 0x00007fdebca771f0 ***
> ======= Backtrace: =========
> /lib/x86_64-linux-gnu/libc.so.6(+0x777e5)[0x7fe2780117e5]
> /lib/x86_64-linux-gnu/libc.so.6(+0x8213e)[0x7fe27801c13e]
> /lib/x86_64-linux-gnu/libc.so.6(__libc_malloc+0x54)[0x7fe27801e184]
> ./monerod(_Znwm+0x18)[0x55b808df2128]
> ./monerod(_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE7reserveEm+0x7d)[0x55b808e28f6d]
> ./monerod(_ZNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEE8overflowEi+0xe5)[0x55b808e6c015]
> ./monerod(_ZN10cryptonote18transaction_prefix12do_serializeILb1E14binary_archiveEEbRT0_IXT_EE+0x15)[0x55b808836195]
> ./monerod(_ZN10cryptonote11transaction19do_serialize_objectILb1E14binary_archiveEEbRT0_IXT_EE+0x2d)[0x55b8088362cd]
> ./monerod(_ZN10cryptonote29t_serializable_object_to_blobINS_11transactionEEEbRKT_RNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE+0x4b)[0x55b808b5082b]
> ./monerod(_ZN10cryptonote10tx_to_blobB5cxx11ERKNS_11transactionE+0x25)[0x55b808b47125]
> ./monerod(_ZN10cryptonote14BlockchainLMDB20add_transaction_dataERKN6crypto4hashERKNS_11transactionES4_S4_+0x28c)[0x55b80892f97c]
> ./monerod(_ZN10cryptonote12BlockchainDB15add_transactionERKN6crypto4hashERKNS_11transactionEPS3_S8_+0x164)[0x55b8088f4a44]
> ./monerod(_ZN10cryptonote12BlockchainDB9add_blockERKNS_5blockEmRKmS5_RKSt6vectorINS_11transactionESaIS7_EE+0xfa)[0x55b8088f528a]
> ./monerod(_ZN10cryptonote14BlockchainLMDB9add_blockERKNS_5blockEmRKmS5_RKSt6vectorINS_11transactionESaIS7_EE+0x1b0)[0x55b80892ac10]
> ./monerod(_ZN10cryptonote10Blockchain26handle_block_to_main_chainERKNS_5blockERKN6crypto4hashERNS_26block_verification_contextE+0x24f6)[0x55b8089558f6]
> ./monerod(_ZN10cryptonote10Blockchain13add_new_blockERKNS_5blockERNS_26block_verification_contextE+0x358)[0x55b80895ba68]
> ./monerod(_ZN10cryptonote4core21handle_incoming_blockERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERNS_26block_verification_contextEb+0x5c6)[0x55b808978116]
> ./monerod(_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE19try_add_next_blocksERNS_29cryptonote_connection_contextE+0x754)[0x55b8088c6c34]
> ./monerod(_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE27handle_response_get_objectsEiRNS_27NOTIFY_RESPONSE_GET_OBJECTS7requestERNS_29cryptonote_connection_contextE+0x1621)[0x55b8088caa81]
> ./monerod(_ZN4epee9net_utils17buff_to_t_adapterIN10cryptonote29t_cryptonote_protocol_handlerINS2_4coreEEENS2_27NOTIFY_RESPONSE_GET_OBJECTS7requestENS2_29cryptonote_connection_contextEN5boost3_bi6bind_tIiNS9_4_mfi3mf3IiS5_iRS7_RS8_EENSA_5list4INSA_5valueIPS5_EENS9_3argILi1EEENSL_ILi2EEENSL_ILi3EEEEEEEEEiPT_iRKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEET2_RT1_+0x37a)[0x55b80875992a]
> ./monerod(_ZN10cryptonote29t_cryptonote_protocol_handlerINS_4coreEE17handle_invoke_mapINS_29cryptonote_connection_contextEEEibiRKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERSA_RT_Rb+0x222)[0x55b80875b1a2]
> ./monerod(_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEEEEibiRKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERSF_RT_Rb+0xc2)[0x55b80875b4b2]
> ./monerod(_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE6notifyEiRKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERNS_24p2p_connection_context_tINS1_29cryptonote_connection_contextEEE+0x50)[0x55b80875b880]
> ./monerod(_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE11handle_recvEPKvm+0x4ad)[0x55b8088d9f9d]
> ./monerod(_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x228)[0x55b8088f2be8]
> ./monerod(_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEESM_mEEEEvRPNS2_11strand_implERT_+0x7a)[0x55b8088bb24a]
> ./monerod(_ZN5boost4asio6detail18completion_handlerINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS8_5list3INS8_5valueINS_10shared_ptrISN_EEEEPFNS_3argILi1EEEvEPFNSY_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESP_mEES16_EEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESR_m+0x188)[0x55b8088bb6b8]
> ./monerod(_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x226)[0x55b8088bbaa6]
> ./monerod(_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESQ_m+0x250)[0x55b8088bbd80]
> ./monerod(_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationERKNS_6system10error_codeEm+0x1f4)[0x55b8086d12e4]
> ./monerod(_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x844)[0x55b80889d754]
> ./monerod(+0x9ff64d)[0x55b808dc764d]
> /lib/x86_64-linux-gnu/libpthread.so.0(+0x76ba)[0x7fe27836b6ba]
> /lib/x86_64-linux-gnu/libc.so.6(clone+0x6d)[0x7fe2780a141d]
> ======= Memory map: ========
> 55b8083c8000-55b809194000 r-xp 00000000 08:05 3281681                    /home/user/bin/monero-gui-v0.13.0.4/monerod
> 55b809393000-55b8093ce000 r--p 00dcb000 08:05 3281681                    /home/user/bin/monero-gui-v0.13.0.4/monerod
> 55b8093ce000-55b80941d000 rw-p 00e06000 08:05 3281681                    /home/user/bin/monero-gui-v0.13.0.4/monerod
> 55b80941d000-55b80941e000 rw-p 00000000 00:00 0 
> 55b80941e000-55b809489000 rw-p 00000000 00:00 0 
> 55b809a6a000-55b809c42000 rw-p 00000000 00:00 0                          [heap]
> 7fde80000000-7fde80106000 rw-p 00000000 00:00 0 
> 7fde80106000-7fde84000000 ---p 00000000 00:00 0 
> 7fde84000000-7fde84021000 rw-p 00000000 00:00 0 
> 7fde84021000-7fde88000000 ---p 00000000 00:00 0 
> 7fde88000000-7fde88106000 rw-p 00000000 00:00 0 
> 7fde88106000-7fde8c000000 ---p 00000000 00:00 0 
> 7fde8c000000-7fde8c106000 rw-p 00000000 00:00 0 
> 7fde8c106000-7fde90000000 ---p 00000000 00:00 0 
> 7fde90000000-7fde90e75000 rw-p 00000000 00:00 0 
> 7fde90e75000-7fde94000000 ---p 00000000 00:00 0 
> 7fde94000000-7fde94106000 rw-p 00000000 00:00 0 
> 7fde94106000-7fde98000000 ---p 00000000 00:00 0 
> 7fde98000000-7fde995eb000 rw-p 00000000 00:00 0 
> 7fde995eb000-7fde9c000000 ---p 00000000 00:00 0 
> 7fde9d5fa000-7fde9d5fb000 ---p 00000000 00:00 0 
> 7fde9d5fb000-7fde9ddfb000 rw-p 00000000 00:00 0 
> 7fde9ddfb000-7fde9ddfc000 ---p 00000000 00:00 0 
> 7fde9ddfc000-7fde9e5fc000 rw-p 00000000 00:00 0 
> 7fde9e5fc000-7fde9e5fd000 ---p 00000000 00:00 0 
> 7fde9e5fd000-7fde9edfd000 rw-p 00000000 00:00 0 
> 7fde9edfd000-7fde9edfe000 ---p 00000000 00:00 0 
> 7fde9edfe000-7fde9f5fe000 rw-p 00000000 00:00 0 
> 7fde9f5fe000-7fde9f5ff000 ---p 00000000 00:00 0 
> 7fde9f5ff000-7fde9faff000 rw-p 00000000 00:00 0 
> 7fde9faff000-7fde9fb00000 ---p 00000000 00:00 0 
> 7fde9fb00000-7fdea0000000 rw-p 00000000 00:00 0 
> 7fdea0000000-7fdea1638000 rw-p 00000000 00:00 0 
> 7fdea1638000-7fdea4000000 ---p 00000000 00:00 0 
> 7fdea4000000-7fdea5251000 rw-p 00000000 00:00 0 
> 7fdea5251000-7fdea8000000 ---p 00000000 00:00 0 
> 7fdea8000000-7fdea953a000 rw-p 00000000 00:00 0 
> 7fdea953a000-7fdeac000000 ---p 00000000 00:00 0 
> 7fdeac000000-7fdead463000 rw-p 00000000 00:00 0 
> 7fdead463000-7fdeb0000000 ---p 00000000 00:00 0 
> 7fdeb0000000-7fdeb0ced000 rw-p 00000000 00:00 0 
> 7fdeb0ced000-7fdeb4000000 ---p 00000000 00:00 0 
> 7fdeb4000000-7fdeb563c000 rw-p 00000000 00:00 0 
> 7fdeb563c000-7fdeb8000000 ---p 00000000 00:00 0 
> 7fdeb8000000-7fdeb9102000 rw-p 00000000 00:00 0 
> 7fdeb9102000-7fdebc000000 ---p 00000000 00:00 0 
> 7fdebc000000-7fdebcabc000 rw-p 00000000 00:00 0 
> 7fdebcabc000-7fdec0000000 ---p 00000000 00:00 0 
> 7fdec0000000-7fdec0021000 rw-p 00000000 00:00 0 
> 7fdec0021000-7fdec4000000 ---p 00000000 00:00 0 
> 7fdec41ca000-7fdec41e0000 r-xp 00000000 08:05 3013662                    /lib/x86_64-linux-gnu/libgcc_s.so.1
> 7fdec41e0000-7fdec43df000 ---p 00016000 08:05 3013662                    /lib/x86_64-linux-gnu/libgcc_s.so.1
> 7fdec43df000-7fdec43e0000 rw-p 00015000 08:05 3013662                    /lib/x86_64-linux-gnu/libgcc_s.so.1
> 7fdec43e0000-7fdec43e1000 ---p 00000000 00:00 0 
> 7fdec43e1000-7fdec48e1000 rw-p 00000000 00:00 0 
> 7fdec48e1000-7fdec48e2000 ---p 00000000 00:00 0 
> 7fdec48e2000-7fdec4de2000 rw-p 00000000 00:00 0 
> 7fdec4de2000-7fdec4de3000 ---p 00000000 00:00 0 
> 7fdec4de3000-7fdec52e3000 rw-p 00000000 00:00 0 
> 7fdec52e3000-7fdec52e4000 ---p 00000000 00:00 0 
> 7fdec52e4000-7fdec57e4000 rw-p 00000000 00:00 0 
> 7fdec57e4000-7fdec57e5000 ---p 00000000 00:00 0 
> 7fdec57e5000-7fdec5ce5000 rw-p 00000000 00:00 0 
> 7fdec5ce5000-7fdec5ce6000 ---p 00000000 00:00 0 
> 7fdec5ce6000-7fdec61e6000 rw-p 00000000 00:00 0 
> 7fdec61e6000-7fdec61e7000 ---p 00000000 00:00 0 
> 7fdec61e7000-7fdec66e7000 rw-p 00000000 00:00 0 
> 7fdec66e7000-7fdec66e8000 ---p 00000000 00:00 0 
> 7fdec66e8000-7fdec6ee8000 rw-p 00000000 00:00 0 
> 7fdec6ee8000-7fdec6ee9000 ---p 00000000 00:00 0 
> 7fdec6ee9000-7fdec76e9000 rw-p 00000000 00:00 0 
> 7fdec76e9000-7fdec76ea000 ---p 00000000 00:00 0 
> 7fdec76ea000-7fdec7eea000 rw-p 00000000 00:00 0 
> 7fdec7eea000-7fdec7eeb000 ---p 00000000 00:00 0 
> 7fdec7eeb000-7fdecb9ce000 rw-p 00000000 00:00 0 
> 7fdecb9ce000-7fe264000000 r--s 00000000 08:12 19398664                   /media/user/storage/mdata/lmdb/data.mdb
> 7fe264000000-7fe2642a7000 rw-p 00000000 00:00 0 
> 7fe2642a7000-7fe268000000 ---p 00000000 00:00 0 
> 7fe268000000-7fe26829a000 rw-p 00000000 00:00 0 
> 7fe26829a000-7fe26c000000 ---p 00000000 00:00 0 
> 7fe26c000000-7fe26c2a8000 rw-p 00000000 00:00 0 
> 7fe26c2a8000-7fe270000000 ---p 00000000 00:00 0 
> 7fe270000000-7fe2703ec000 rw-p 00000000 00:00 0 
> 7fe2703ec000-7fe274000000 ---p 00000000 00:00 0 
> 7fe27406e000-7fe274281000 rw-p 00000000 00:00 0 
> 7fe274281000-7fe274282000 ---p 00000000 00:00 0 
> 7fe274282000-7fe274782000 rw-p 00000000 00:00 0 
> 7fe274782000-7fe274b8b000 r--p 00000000 08:05 1316419                    /usr/lib/locale/locale-archive
> 7fe274b8b000-7fe274b8c000 ---p 00000000 00:00 0 
> 7fe274b8c000-7fe27538c000 rw-p 00000000 00:00 0 
> 7fe27538c000-7fe27538d000 ---p 00000000 00:00 0 
> 7fe27538d000-7fe275d8e000 rw-p 00000000 00:00 0 
> 7fe275d8e000-7fe275d8f000 ---p 00000000 00:00 0 
> 7fe275d8f000-7fe27658f000 rw-p 00000000 00:00 0 
> 7fe27658f000-7fe276590000 ---p 00000000 00:00 0 
> 7fe276590000-7fe276d90000 rw-p 00000000 00:00 0 
> 7fe276d90000-7fe276d91000 ---p 00000000 00:00 0 
> 7fe276d91000-7fe277591000 rw-p 00000000 00:00 0 
> 7fe277591000-7fe277592000 ---p 00000000 00:00 0 
> 7fe277592000-7fe277d92000 rw-p 00000000 00:00 0 
> 7fe277d92000-7fe277d99000 r-xp 00000000 08:05 3013642                    /lib/x86_64-linux-gnu/librt-2.23.so
> 7fe277d99000-7fe277f98000 ---p 00007000 08:05 3013642                    /lib/x86_64-linux-gnu/librt-2.23.so
> 7fe277f98000-7fe277f99000 r--p 00006000 08:05 3013642                    /lib/x86_64-linux-gnu/librt-2.23.so
> 7fe277f99000-7fe277f9a000 rw-p 00007000 08:05 3013642                    /lib/x86_64-linux-gnu/librt-2.23.so
> 7fe277f9a000-7fe27815a000 r-xp 00000000 08:05 3008859                    /lib/x86_64-linux-gnu/libc-2.23.so
> 7fe27815a000-7fe27835a000 ---p 001c0000 08:05 3008859                    /lib/x86_64-linux-gnu/libc-2.23.so
> 7fe27835a000-7fe27835e000 r--p 001c0000 08:05 3008859                    /lib/x86_64-linux-gnu/libc-2.23.so
> 7fe27835e000-7fe278360000 rw-p 001c4000 08:05 3008859                    /lib/x86_64-linux-gnu/libc-2.23.so
> 7fe278360000-7fe278364000 rw-p 00000000 00:00 0 
> 7fe278364000-7fe27837c000 r-xp 00000000 08:05 3008858                    /lib/x86_64-linux-gnu/libpthread-2.23.so
> 7fe27837c000-7fe27857b000 ---p 00018000 08:05 3008858                    /lib/x86_64-linux-gnu/libpthread-2.23.so
> 7fe27857b000-7fe27857c000 r--p 00017000 08:05 3008858                    /lib/x86_64-linux-gnu/libpthread-2.23.so
> 7fe27857c000-7fe27857d000 rw-p 00018000 08:05 3008858                    /lib/x86_64-linux-gnu/libpthread-2.23.so
> 7fe27857d000-7fe278581000 rw-p 00000000 00:00 0 
> 7fe278581000-7fe278689000 r-xp 00000000 08:05 3008855                    /lib/x86_64-linux-gnu/libm-2.23.so
> 7fe278689000-7fe278888000 ---p 00108000 08:05 3008855                    /lib/x86_64-linux-gnu/libm-2.23.so
> 7fe278888000-7fe278889000 r--p 00107000 08:05 3008855                    /lib/x86_64-linux-gnu/libm-2.23.so
> 7fe278889000-7fe27888a000 rw-p 00108000 08:05 3008855                    /lib/x86_64-linux-gnu/libm-2.23.so
> 7fe27888a000-7fe27888d000 r-xp 00000000 08:05 3008861                    /lib/x86_64-linux-gnu/libdl-2.23.so
> 7fe27888d000-7fe278a8c000 ---p 00003000 08:05 3008861                    /lib/x86_64-linux-gnu/libdl-2.23.so
> 7fe278a8c000-7fe278a8d000 r--p 00002000 08:05 3008861                    /lib/x86_64-linux-gnu/libdl-2.23.so
> 7fe278a8d000-7fe278a8e000 rw-p 00003000 08:05 3008861                    /lib/x86_64-linux-gnu/libdl-2.23.so
> 7fe278a8e000-7fe278ab4000 r-xp 00000000 08:05 3008857                    /lib/x86_64-linux-gnu/ld-2.23.so
> 7fe278b68000-7fe278c6e000 rw-p 00000000 00:00 0 
> 7fe278c6e000-7fe278c8c000 r-xp 00000000 08:05 3010084                    /lib/x86_64-linux-gnu/libudev.so.1.6.4
> 7fe278c8c000-7fe278c8d000 r--p 0001d000 08:05 3010084                    /lib/x86_64-linux-gnu/libudev.so.1.6.4
> 7fe278c8d000-7fe278c8e000 rw-p 0001e000 08:05 3010084                    /lib/x86_64-linux-gnu/libudev.so.1.6.4
> 7fe278c8e000-7fe278c8f000 rw-p 00000000 00:00 0 
> 7fe278cae000-7fe278caf000 rw-p 00000000 00:00 0 
> 7fe278caf000-7fe278cb1000 rw-s 00000000 08:12 19398663                   /media/user/storage/mdata/lmdb/lock.mdb
> 7fe278cb1000-7fe278cb3000 rw-p 00000000 00:00 0 
> 7fe278cb3000-7fe278cb4000 r--p 00025000 08:05 3008857                    /lib/x86_64-linux-gnu/ld-2.23.so
> 7fe278cb4000-7fe278cb5000 rw-p 00026000 08:05 3008857                    /lib/x86_64-linux-gnu/ld-2.23.so
> 7fe278cb5000-7fe278cb6000 rw-p 00000000 00:00 0 
> 7ffd58d05000-7ffd58d29000 rw-p 00000000 00:00 0                          [stack]
> 7ffd58de7000-7ffd58dea000 r--p 00000000 00:00 0                          [vvar]
> 7ffd58dea000-7ffd58dec000 r-xp 00000000 00:00 0                          [vdso]
> ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
> Aborted (core dumped)

Doesn't run anymore.

# Discussion History
## alextrezvy | 2018-11-12T20:27:01+00:00
[monero.log](https://github.com/monero-project/monero/files/2573499/monero.log)


## moneromooo-monero | 2018-11-12T20:47:25+00:00
Any chance you can run (and reproduce the problem) with ASAN ?
-D SANITIZE=ON on the cmake command line.

## alextrezvy | 2018-11-13T06:17:36+00:00
Now it fails differently:
> 2018-11-13 06:14:46.849	    7f6531768780	FATAL	daemon	src/daemon/daemon.cpp:207	Uncaught exception! Attempt to get block from height 1258656 failed -- block not in db

I don't know if it is related to the previous failure or not. Here is the log:
[monero.log](https://github.com/monero-project/monero/files/2574837/monero.log)


## moneromooo-monero | 2018-11-13T08:48:38+00:00
I can't tell, but that database looks corrupted. --db-salvage might help. If not, it'll need resyncing.

## alextrezvy | 2018-11-13T10:32:45+00:00
It seems like HDD power supply problem (because of strange ticks). Now connected to another power line and try again.

# Action History
- Created by: alextrezvy | 2018-11-12T20:16:32+00:00
- Closed at: 2018-11-13T10:32:45+00:00
