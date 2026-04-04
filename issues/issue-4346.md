---
title: 'malloc(): memory corruption'
source_url: https://github.com/monero-project/monero/issues/4346
author: trasherdk
assignees: []
labels: []
created_at: '2018-09-07T14:45:22+00:00'
updated_at: '2018-09-11T17:02:25+00:00'
type: issue
status: closed
closed_at: '2018-09-11T17:02:24+00:00'
---

# Original Description
Running monero-v0.12.3.0 on Slackware64 14.2 - 4 cores, 8 GB RAM.
After "a while" (5 hours, 20 minutes, random) the daemon crashes.

This is what the screen looked like (followed by the last 50 log entries):
    
	*** Error in `${HOME}/bin/monerod': malloc(): memory corruption: 0x00007fbbcc00bd10 ***
	======= Backtrace: =========
	/lib64/libc.so.6(+0x776f4)[0x7fbc3a4c26f4]
	/lib64/libc.so.6(+0x8198e)[0x7fbc3a4cc98e]
	/lib64/libc.so.6(__libc_malloc+0x54)[0x7fbc3a4ce864]
	/usr/lib64/libstdc++.so.6(_Znwm+0x18)[0x7fbc3afddd18]
	/usr/lib64/libstdc++.so.6(_ZNSs4_Rep9_S_createEmmRKSaIcE+0x59)[0x7fbc3b01c819]
	/usr/lib64/libstdc++.so.6(_ZNSs4_Rep8_M_cloneERKSaIcEm+0x1b)[0x7fbc3b01d5fb]
	/usr/lib64/libstdc++.so.6(_ZNSs7reserveEm+0x34)[0x7fbc3b01d6a4]
	/usr/lib64/libstdc++.so.6(_ZNSt15basic_stringbufIcSt11char_traitsIcESaIcEE8overflowEi+0xa1)[0x7fbc3b014f51]
	/usr/lib64/libstdc++.so.6(_ZNSt15basic_streambufIcSt11char_traitsIcEE6xsputnEPKcl+0x89)[0x7fbc3b068ea9]
	/usr/lib64/libstdc++.so.6(_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_l+0x12e)[0x7fbc3b059bee]
	${HOME}/bin/monerod(_ZN4epee9net_utils16network_throttle20_handle_trafic_exactEmm+0x1fc)[0x55db6a874bec]
	${HOME}/bin/monerod(_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE11handle_readERKN5boost6system10error_codeEm+0x84)[0x55db6a6ae734]
	${HOME}/bin/monerod(_ZN5boost4asio6detail14strand_service8dispatchINS1_7binder2INS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS5_5list3INS5_5valueINS_10shared_ptrISK_EEEEPFNS_3argILi1EEEvEPFNSV_ILi2EEEvEEEEESM_mEEEEvRPNS2_11strand_implERT_+0x7a)[0x55db6a67853a]
	${HOME}/bin/monerod(_ZN5boost4asio6detail18completion_handlerINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSC_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS8_5list3INS8_5valueINS_10shared_ptrISN_EEEEPFNS_3argILi1EEEvEPFNSY_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESP_mEES16_EEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESR_m+0x188)[0x55db6a6789a8]
	${HOME}/bin/monerod(_ZN5boost4asio6detail14strand_service8dispatchINS1_17rewrapped_handlerINS1_7binder2INS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSD_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS9_5list3INS9_5valueINS_10shared_ptrISO_EEEEPFNS_3argILi1EEEvEPFNSZ_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEESQ_mEES17_EEEEvRPNS2_11strand_implERT_+0x226)[0x55db6a678d96]
	${HOME}/bin/monerod(_ZN5boost4asio6detail23reactive_socket_recv_opINS0_17mutable_buffers_1ENS1_15wrapped_handlerINS0_10io_service6strandENS_3_bi6bind_tIvNS_4_mfi3mf2IvN4epee9net_utils10connectionINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEERKNS_6system10error_codeEmEENS7_5list3INS7_5valueINS_10shared_ptrISM_EEEEPFNS_3argILi1EEEvEPFNSX_ILi2EEEvEEEEENS1_26is_continuation_if_runningEEEE11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationESQ_m+0x250)[0x55db6a679070]
	${HOME}/bin/monerod(_ZN5boost4asio6detail13epoll_reactor16descriptor_state11do_completeEPNS1_15task_io_serviceEPNS1_25task_io_service_operationERKNS_6system10error_codeEm+0x164)[0x55db6a47ef24]
	${HOME}/bin/monerod(_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x8c4)[0x55db6a65a494]
	/usr/lib64/libboost_thread.so.1.59.0(+0x115a5)[0x7fbc3b2de5a5]
	/lib64/libpthread.so.0(+0x7684)[0x7fbc3a81b684]
	/lib64/libc.so.6(clone+0x6d)[0x7fbc3a551eed]
	======= Memory map: ========
	55db6a2bc000-55db6aa55000 r-xp 00000000 08:12 2359305    ${HOME}/bin/monerod
	55db6ac55000-55db6ac64000 r--p 00799000 08:12 2359305    ${HOME}/bin/monerod
	55db6ac64000-55db6ac65000 rw-p 007a8000 08:12 2359305    ${HOME}/bin/monerod
	55db6ac65000-55db6ac91000 rw-p 00000000 00:00 0 
	55db6bf7e000-55db6c0b1000 rw-p 00000000 00:00 0          [heap]
	7fbb94000000-7fbb94295000 rw-p 00000000 00:00 0 
	7fbb94295000-7fbb98000000 ---p 00000000 00:00 0 
	7fbb9c000000-7fbb9c3b7000 rw-p 00000000 00:00 0 
	7fbb9c3b7000-7fbba0000000 ---p 00000000 00:00 0 
	7fbba0000000-7fbba0295000 rw-p 00000000 00:00 0 
	7fbba0295000-7fbba4000000 ---p 00000000 00:00 0 
	7fbba4000000-7fbba4021000 rw-p 00000000 00:00 0 
	7fbba4021000-7fbba8000000 ---p 00000000 00:00 0 
	7fbbac000000-7fbbac021000 rw-p 00000000 00:00 0 
	7fbbac021000-7fbbb0000000 ---p 00000000 00:00 0 
	7fbbb0000000-7fbbb0295000 rw-p 00000000 00:00 0 
	7fbbb0295000-7fbbb4000000 ---p 00000000 00:00 0 
	7fbbb4000000-7fbbb4021000 rw-p 00000000 00:00 0 
	7fbbb4021000-7fbbb8000000 ---p 00000000 00:00 0 
	7fbbb9afb000-7fbbb9afc000 ---p 00000000 00:00 0 
	7fbbb9afc000-7fbbba2fc000 rw-p 00000000 00:00 0 
	7fbbba2fc000-7fbbba2fd000 ---p 00000000 00:00 0 
	7fbbba2fd000-7fbbbaafd000 rw-p 00000000 00:00 0 
	7fbbbaafd000-7fbbbaafe000 ---p 00000000 00:00 0 
	7fbbbaafe000-7fbbbb2fe000 rw-p 00000000 00:00 0 
	7fbbbb2fe000-7fbbbb2ff000 ---p 00000000 00:00 0 
	7fbbbb2ff000-7fbbbbaff000 rw-p 00000000 00:00 0 
	7fbbbbaff000-7fbbbbb00000 ---p 00000000 00:00 0 
	7fbbbbb00000-7fbbbc000000 rw-p 00000000 00:00 0 
	7fbbbc000000-7fbbbc021000 rw-p 00000000 00:00 0 
	7fbbbc021000-7fbbc0000000 ---p 00000000 00:00 0 
	7fbbc0000000-7fbbc0021000 rw-p 00000000 00:00 0 
	7fbbc0021000-7fbbc4000000 ---p 00000000 00:00 0 
	7fbbc4000000-7fbbc4021000 rw-p 00000000 00:00 0 
	7fbbc4021000-7fbbc8000000 ---p 00000000 00:00 0 
	7fbbc8000000-7fbbc8021000 rw-p 00000000 00:00 0 
	7fbbc8021000-7fbbcc000000 ---p 00000000 00:00 0 
	7fbbcc000000-7fbbcc021000 rw-p 00000000 00:00 0 
	7fbbcc021000-7fbbd0000000 ---p 00000000 00:00 0 
	7fbbd0000000-7fbbd0021000 rw-p 00000000 00:00 0 
	7fbbd0021000-7fbbd4000000 ---p 00000000 00:00 0 
	7fbbd4000000-7fbbd4021000 rw-p 00000000 00:00 0 
	7fbbd4021000-7fbbd8000000 ---p 00000000 00:00 0 
	7fbbd8000000-7fbbd8021000 rw-p 00000000 00:00 0 
	7fbbd8021000-7fbbdc000000 ---p 00000000 00:00 0 
	7fbbdc000000-7fbbdc021000 rw-p 00000000 00:00 0 
	7fbbdc021000-7fbbe0000000 ---p 00000000 00:00 0 
	7fbbe0000000-7fbbe0021000 rw-p 00000000 00:00 0 
	7fbbe0021000-7fbbe4000000 ---p 00000000 00:00 0 
	7fbbe42f5000-7fbbe42f6000 ---p 00000000 00:00 0 
	7fbbe42f6000-7fbbe47f6000 rw-p 00000000 00:00 0 
	7fbbe47f6000-7fbbe47f7000 ---p 00000000 00:00 0 
	7fbbe47f7000-7fbbe4cf7000 rw-p 00000000 00:00 0 
	7fbbe4cf7000-7fbbe4cf8000 ---p 00000000 00:00 0 
	7fbbe4cf8000-7fbbe51f8000 rw-p 00000000 00:00 0 
	7fbbe51f8000-7fbbe51f9000 ---p 00000000 00:00 0 
	7fbbe51f9000-7fbbe56f9000 rw-p 00000000 00:00 0 
	7fbbe56f9000-7fbbe56fa000 ---p 00000000 00:00 0 
	7fbbe56fa000-7fbbe5bfa000 rw-p 00000000 00:00 0 
	7fbbe5bfa000-7fbbe5bfb000 ---p 00000000 00:00 0 
	7fbbe5bfb000-7fbbe60fb000 rw-p 00000000 00:00 0 
	7fbbe60fb000-7fbbe60fc000 ---p 00000000 00:00 0 
	7fbbe60fc000-7fbbe65fc000 rw-p 00000000 00:00 0 
	7fbbe65fc000-7fbbe65fd000 ---p 00000000 00:00 0 
	7fbbe65fd000-7fbbe6afd000 rw-p 00000000 00:00 0 
	7fbbe6afd000-7fbbe6afe000 ---p 00000000 00:00 0 
	7fbbe6afe000-7fbbe6ffe000 rw-p 00000000 00:00 0 
	7fbbe6ffe000-7fbbe6fff000 ---p 00000000 00:00 0 
	7fbbe6fff000-7fbbe77ff000 rw-p 00000000 00:00 0 
	7fbbe77ff000-7fbbe7800000 ---p 00000000 00:00 0 
	7fbbe7800000-7fbbe8000000 rw-p 00000000 00:00 0 
	7fbbe8000000-7fbbe8021000 rw-p 00000000 00:00 0 
	7fbbe8021000-7fbbec000000 ---p 00000000 00:00 0 
	7fbbec000000-7fbbec021000 rw-p 00000000 00:00 0 
	7fbbec021000-7fbbf0000000 ---p 00000000 00:00 0 
	7fbbf0000000-7fbbf0021000 rw-p 00000000 00:00 0 
	7fbbf0021000-7fbbf4000000 ---p 00000000 00:00 0 
	7fbbf41b0000-7fbbf41b1000 ---p 00000000 00:00 0 
	7fbbf41b1000-7fbbf49b1000 rw-p 00000000 00:00 0 
	7fbbf49b1000-7fbbf49b2000 ---p 00000000 00:00 0 
	7fbbf49b2000-7fbbf51b2000 rw-p 00000000 00:00 0 
	7fbbf51b2000-7fbbf51b3000 ---p 00000000 00:00 0 
	7fbbf51b3000-7fbbf59b3000 rw-p 00000000 00:00 0 
	7fbbf59b3000-7fbbf59b4000 ---p 00000000 00:00 0 
	7fbbf59b4000-7fbbf61b4000 rw-p 00000000 00:00 0 
	7fbbf61b4000-7fbbf61b5000 ---p 00000000 00:00 0 
	7fbbf61b5000-7fbbf69b5000 rw-p 00000000 00:00 0 
	7fbbf69b5000-7fbbf69b6000 ---p 00000000 00:00 0 
	7fbbf69b6000-7fbbf71b6000 rw-p 00000000 00:00 0 
	7fbbf71b6000-7fbbf71b7000 ---p 00000000 00:00 0 
	7fbbf71b7000-7fbbf79b7000 rw-p 00000000 00:00 0 
	7fbbf79b7000-7fbc379b7000 r--s 00000000 08:12 2359319    ${HOME}/data/stagenet/lmdb/data.mdb
	7fbc379b7000-7fbc37bb8000 rw-p 00000000 00:00 0 
	7fbc37bb8000-7fbc37bdc000 r-xp 00000000 08:02 393224     /lib64/liblzma.so.5.2.2
	7fbc37bdc000-7fbc37ddc000 ---p 00024000 08:02 393224     /lib64/liblzma.so.5.2.2
	7fbc37ddc000-7fbc37ddd000 rw-p 00024000 08:02 393224     /lib64/liblzma.so.5.2.2
	7fbc37ddd000-7fbc37e23000 r-xp 00000000 08:02 547073     /usr/lib64/libevent-2.0.so.5.1.9
	7fbc37e23000-7fbc38022000 ---p 00046000 08:02 547073     /usr/lib64/libevent-2.0.so.5.1.9
	7fbc38022000-7fbc38023000 r--p 00045000 08:02 547073     /usr/lib64/libevent-2.0.so.5.1.9
	7fbc38023000-7fbc38024000 rw-p 00046000 08:02 547073     /usr/lib64/libevent-2.0.so.5.1.9
	7fbc38024000-7fbc38025000 rw-p 00000000 00:00 0 
	7fbc38025000-7fbc3802f000 r-xp 00000000 08:02 560859     /usr/lib64/libunwind.so.8.0.1
	7fbc3802f000-7fbc3822f000 ---p 0000a000 08:02 560859     /usr/lib64/libunwind.so.8.0.1
	7fbc3822f000-7fbc38230000 r--p 0000a000 08:02 560859     /usr/lib64/libunwind.so.8.0.1
	7fbc38230000-7fbc38231000 rw-p 0000b000 08:02 560859     /usr/lib64/libunwind.so.8.0.1
	7fbc38231000-7fbc3823f000 rw-p 00000000 00:00 0 
	7fbc3823f000-7fbc383c5000 r-xp 00000000 08:02 545722     /usr/lib64/libicuuc.so.56.1
	7fbc383c5000-7fbc385c4000 ---p 00186000 08:02 545722     /usr/lib64/libicuuc.so.56.1
	7fbc385c4000-7fbc385d4000 r--p 00185000 08:02 545722     /usr/lib64/libicuuc.so.56.1
	7fbc385d4000-7fbc385d5000 rw-p 00195000 08:02 545722     /usr/lib64/libicuuc.so.56.1
	7fbc385d5000-7fbc385d7000 rw-p 00000000 00:00 0 
	7fbc385d7000-7fbc38858000 r-xp 00000000 08:02 545717     /usr/lib64/libicui18n.so.56.1
	7fbc38858000-7fbc38a58000 ---p 00281000 08:02 545717     /usr/lib64/libicui18n.so.56.1
	7fbc38a58000-7fbc38a66000 r--p 00281000 08:02 545717     /usr/lib64/libicui18n.so.56.1
	7fbc38a66000-7fbc38a68000 rw-p 0028f000 08:02 545717     /usr/lib64/libicui18n.so.56.1
	7fbc38a68000-7fbc3a24b000 r--p 00000000 08:02 545723     /usr/lib64/libicudata.so.56.1
	7fbc3a24b000-7fbc3a44a000 ---p 017e3000 08:02 545723     /usr/lib64/libicudata.so.56.1
	7fbc3a44a000-7fbc3a44b000 r--p 017e2000 08:02 545723     /usr/lib64/libicudata.so.56.1
	7fbc3a44b000-7fbc3a60b000 r-xp 00000000 08:02 393412     /lib64/libc-2.23.so
	7fbc3a60b000-7fbc3a80a000 ---p 001c0000 08:02 393412     /lib64/libc-2.23.so
	7fbc3a80a000-7fbc3a80e000 r--p 001bf000 08:02 393412     /lib64/libc-2.23.so
	7fbc3a80e000-7fbc3a810000 rw-p 001c3000 08:02 393412     /lib64/libc-2.23.so
	7fbc3a810000-7fbc3a814000 rw-p 00000000 00:00 0 
	7fbc3a814000-7fbc3a82c000 r-xp 00000000 08:02 393407     /lib64/libpthread-2.23.so
	7fbc3a82c000-7fbc3aa2b000 ---p 00018000 08:02 393407     /lib64/libpthread-2.23.so
	7fbc3aa2b000-7fbc3aa2c000 r--p 00017000 08:02 393407     /lib64/libpthread-2.23.so
	7fbc3aa2c000-7fbc3aa2d000 rw-p 00018000 08:02 393407     /lib64/libpthread-2.23.so
	7fbc3aa2d000-7fbc3aa31000 rw-p 00000000 00:00 0 
	7fbc3aa31000-7fbc3aa47000 r-xp 00000000 08:02 537762     /usr/lib64/libgcc_s.so.1
	7fbc3aa47000-7fbc3ac46000 ---p 00016000 08:02 537762     /usr/lib64/libgcc_s.so.1
	7fbc3ac46000-7fbc3ac47000 r--p 00015000 08:02 537762     /usr/lib64/libgcc_s.so.1
	7fbc3ac47000-7fbc3ac48000 rw-p 00016000 08:02 537762     /usr/lib64/libgcc_s.so.1
	7fbc3ac48000-7fbc3ad50000 r-xp 00000000 08:02 393402     /lib64/libm-2.23.so
	7fbc3ad50000-7fbc3af4f000 ---p 00108000 08:02 393402     /lib64/libm-2.23.so
	7fbc3af4f000-7fbc3af50000 r--p 00107000 08:02 393402     /lib64/libm-2.23.so
	7fbc3af50000-7fbc3af51000 rw-p 00108000 08:02 393402     /lib64/libm-2.23.so
	7fbc3af51000-7fbc3b0bd000 r-xp 00000000 08:02 537833     /usr/lib64/libstdc++.so.6.0.21
	7fbc3b0bd000-7fbc3b2bd000 ---p 0016c000 08:02 537833     /usr/lib64/libstdc++.so.6.0.21
	7fbc3b2bd000-7fbc3b2c7000 r--p 0016c000 08:02 537833     /usr/lib64/libstdc++.so.6.0.21
	7fbc3b2c7000-7fbc3b2c9000 rw-p 00176000 08:02 537833     /usr/lib64/libstdc++.so.6.0.21
	7fbc3b2c9000-7fbc3b2cd000 rw-p 00000000 00:00 0 
	7fbc3b2cd000-7fbc3b2f1000 r-xp 00000000 08:02 570980     /usr/lib64/libboost_thread.so.1.59.0
	7fbc3b2f1000-7fbc3b4f1000 ---p 00024000 08:02 570980     /usr/lib64/libboost_thread.so.1.59.0
	7fbc3b4f1000-7fbc3b4f3000 rw-p 00024000 08:02 570980     /usr/lib64/libboost_thread.so.1.59.0
	7fbc3b4f3000-7fbc3b52b000 r-xp 00000000 08:02 570954     /usr/lib64/libboost_serialization.so.1.59.0
	7fbc3b52b000-7fbc3b72b000 ---p 00038000 08:02 570954     /usr/lib64/libboost_serialization.so.1.59.0
	7fbc3b72b000-7fbc3b72e000 rw-p 00038000 08:02 570954     /usr/lib64/libboost_serialization.so.1.59.0
	7fbc3b72e000-7fbc3b73e000 r-xp 00000000 08:02 570981     /usr/lib64/libboost_date_time.so.1.59.0
	7fbc3b73e000-7fbc3b93e000 ---p 00010000 08:02 570981     /usr/lib64/libboost_date_time.so.1.59.0
	7fbc3b93e000-7fbc3b93f000 rw-p 00010000 08:02 570981     /usr/lib64/libboost_date_time.so.1.59.0
	7fbc3b93f000-7fbc3bb69000 r-xp 00000000 08:02 393316     /lib64/libcrypto.so.1.0.0
	7fbc3bb69000-7fbc3bd69000 ---p 0022a000 08:02 393316     /lib64/libcrypto.so.1.0.0
	7fbc3bd69000-7fbc3bd84000 r--p 0022a000 08:02 393316     /lib64/libcrypto.so.1.0.0
	7fbc3bd84000-7fbc3bd90000 rw-p 00245000 08:02 393316     /lib64/libcrypto.so.1.0.0
	7fbc3bd90000-7fbc3bd93000 rw-p 00000000 00:00 0 
	7fbc3bd93000-7fbc3bdfb000 r-xp 00000000 08:02 393315     /lib64/libssl.so.1.0.0
	7fbc3bdfb000-7fbc3bffb000 ---p 00068000 08:02 393315     /lib64/libssl.so.1.0.0
	7fbc3bffb000-7fbc3bfff000 r--p 00068000 08:02 393315     /lib64/libssl.so.1.0.0
	7fbc3bfff000-7fbc3c006000 rw-p 0006c000 08:02 393315     /lib64/libssl.so.1.0.0
	7fbc3c006000-7fbc3c0a9000 r-xp 00000000 08:02 560802     /usr/lib64/libunbound.so.2.5.3
	7fbc3c0a9000-7fbc3c2a9000 ---p 000a3000 08:02 560802     /usr/lib64/libunbound.so.2.5.3
	7fbc3c2a9000-7fbc3c2aa000 r--p 000a3000 08:02 560802     /usr/lib64/libunbound.so.2.5.3
	7fbc3c2aa000-7fbc3c2af000 rw-p 000a4000 08:02 560802     /usr/lib64/libunbound.so.2.5.3
	7fbc3c2af000-7fbc3c2b9000 r-xp 00000000 08:02 560773     /usr/lib64/libpcsclite.so.1.0.0
	7fbc3c2b9000-7fbc3c4b8000 ---p 0000a000 08:02 560773     /usr/lib64/libpcsclite.so.1.0.0
	7fbc3c4b8000-7fbc3c4b9000 r--p 00009000 08:02 560773     /usr/lib64/libpcsclite.so.1.0.0
	7fbc3c4b9000-7fbc3c4ba000 rw-p 0000a000 08:02 560773     /usr/lib64/libpcsclite.so.1.0.0
	7fbc3c4ba000-7fbc3c4bd000 r-xp 00000000 08:02 393227     /lib64/libtermcap.so.2.0.8
	7fbc3c4bd000-7fbc3c6bc000 ---p 00003000 08:02 393227     /lib64/libtermcap.so.2.0.8
	7fbc3c6bc000-7fbc3c6bd000 rw-p 00002000 08:02 393227     /lib64/libtermcap.so.2.0.8
	7fbc3c6bd000-7fbc3c6fc000 r-xp 00000000 08:02 524374     /usr/lib64/libreadline.so.6.3
	7fbc3c6fc000-7fbc3c8fc000 ---p 0003f000 08:02 524374     /usr/lib64/libreadline.so.6.3
	7fbc3c8fc000-7fbc3c904000 rw-p 0003f000 08:02 524374     /usr/lib64/libreadline.so.6.3
	7fbc3c904000-7fbc3c906000 rw-p 00000000 00:00 0 
	7fbc3c906000-7fbc3c95b000 r-xp 00000000 08:02 560854     /usr/lib64/libsodium.so.23.0.0
	7fbc3c95b000-7fbc3cb5a000 ---p 00055000 08:02 560854     /usr/lib64/libsodium.so.23.0.0
	7fbc3cb5a000-7fbc3cb5b000 r--p 00054000 08:02 560854     /usr/lib64/libsodium.so.23.0.0
	7fbc3cb5b000-7fbc3cb5c000 rw-p 00055000 08:02 560854     /usr/lib64/libsodium.so.23.0.0
	7fbc3cb5c000-7fbc3cbd8000 r-xp 00000000 08:02 527213     /usr/lib64/libzmq.so.5.1.1
	7fbc3cbd8000-7fbc3cdd7000 ---p 0007c000 08:02 527213     /usr/lib64/libzmq.so.5.1.1
	7fbc3cdd7000-7fbc3cddc000 r--p 0007b000 08:02 527213     /usr/lib64/libzmq.so.5.1.1
	7fbc3cddc000-7fbc3cddd000 rw-p 00080000 08:02 527213     /usr/lib64/libzmq.so.5.1.1
	7fbc3cddd000-7fbc3cde0000 r-xp 00000000 08:02 570977     /usr/lib64/libboost_system.so.1.59.0
	7fbc3cde0000-7fbc3cfdf000 ---p 00003000 08:02 570977     /usr/lib64/libboost_system.so.1.59.0
	7fbc3cfdf000-7fbc3cfe0000 rw-p 00002000 08:02 570977     /usr/lib64/libboost_system.so.1.59.0
	7fbc3cfe0000-7fbc3d0db000 r-xp 00000000 08:02 570974     /usr/lib64/libboost_regex.so.1.59.0
	7fbc3d0db000-7fbc3d2db000 ---p 000fb000 08:02 570974     /usr/lib64/libboost_regex.so.1.59.0
	7fbc3d2db000-7fbc3d2e1000 rw-p 000fb000 08:02 570974     /usr/lib64/libboost_regex.so.1.59.0
	7fbc3d2e1000-7fbc3d357000 r-xp 00000000 08:02 570958     /usr/lib64/libboost_program_options.so.1.59.0
	7fbc3d357000-7fbc3d556000 ---p 00076000 08:02 570958     /usr/lib64/libboost_program_options.so.1.59.0
	7fbc3d556000-7fbc3d55a000 rw-p 00075000 08:02 570958     /usr/lib64/libboost_program_options.so.1.59.0
	7fbc3d55a000-7fbc3d570000 r-xp 00000000 08:02 570968     /usr/lib64/libboost_filesystem.so.1.59.0
	7fbc3d570000-7fbc3d770000 ---p 00016000 08:02 570968     /usr/lib64/libboost_filesystem.so.1.59.0
	7fbc3d770000-7fbc3d771000 rw-p 00016000 08:02 570968     /usr/lib64/libboost_filesystem.so.1.59.0
	7fbc3d771000-7fbc3d777000 r-xp 00000000 08:02 570970     /usr/lib64/libboost_chrono.so.1.59.0
	7fbc3d777000-7fbc3d976000 ---p 00006000 08:02 570970     /usr/lib64/libboost_chrono.so.1.59.0
	7fbc3d976000-7fbc3d977000 rw-p 00005000 08:02 570970     /usr/lib64/libboost_chrono.so.1.59.0
	7fbc3d977000-7fbc3d97a000 r-xp 00000000 08:02 393413     /lib64/libdl-2.23.so
	7fbc3d97a000-7fbc3db79000 ---p 00003000 08:02 393413     /lib64/libdl-2.23.so
	7fbc3db79000-7fbc3db7a000 r--p 00002000 08:02 393413     /lib64/libdl-2.23.so
	7fbc3db7a000-7fbc3db7b000 rw-p 00003000 08:02 393413     /lib64/libdl-2.23.so
	7fbc3db7b000-7fbc3db82000 r-xp 00000000 08:02 393317     /lib64/librt-2.23.so
	7fbc3db82000-7fbc3dd81000 ---p 00007000 08:02 393317     /lib64/librt-2.23.so
	7fbc3dd81000-7fbc3dd82000 r--p 00006000 08:02 393317     /lib64/librt-2.23.so
	7fbc3dd82000-7fbc3dd83000 rw-p 00007000 08:02 393317     /lib64/librt-2.23.so
	7fbc3dd83000-7fbc3dda8000 r-xp 00000000 08:02 393438     /lib64/ld-2.23.so
	7fbc3de2d000-7fbc3de7b000 r--p 00000000 08:02 668153     /usr/lib64/locale/en_DK.utf8/LC_CTYPE
	7fbc3de7b000-7fbc3df91000 rw-p 00000000 00:00 0 
	7fbc3dfa2000-7fbc3dfa5000 rw-p 00000000 00:00 0 
	7fbc3dfa5000-7fbc3dfa7000 rw-s 00000000 08:12 2359318    ${HOME}/data/stagenet/lmdb/lock.mdb
	7fbc3dfa7000-7fbc3dfa8000 rw-p 00000000 00:00 0 
	7fbc3dfa8000-7fbc3dfa9000 r--p 00025000 08:02 393438     /lib64/ld-2.23.so
	7fbc3dfa9000-7fbc3dfaa000 rw-p 00026000 08:02 393438     /lib64/ld-2.23.so
	7fbc3dfaa000-7fbc3dfab000 rw-p 00000000 00:00 0 
	7ffc18856000-7ffc1887c000 rw-p 00000000 00:00 0          [stack]
	7ffc18893000-7ffc18896000 r--p 00000000 00:00 0          [vvar]
	7ffc18896000-7ffc18898000 r-xp 00000000 00:00 0          [vdso]
	ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0  [vsyscall]
	./start-daemon.sh: line 29:  6090 Aborted                 
	$BIN --data-dir ${HOMEDIR}/data/ \
		--log-file ${LOGFILE} \
		--max-log-file-size 2500000 \
		--pidfile ${HOMEDIR}/${CURRENCY}d.pid \
		--confirm-external-bind \
		--zmq-rpc-bind-ip $IPADDR \
		--p2p-bind-ip $IPADDR \
		--rpc-bind-ip $IPADDR
    

**Log file entries**
    
	$ tail -n 50 log/monerod.log 
	[P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:163      [8] /lib64/libpthread.so.0+0x7684 [0x7fbc3a81b684]
	[P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:163      [9] /lib64/libc.so.6:clone+0x6d [0x7fbc3a551eed]
	[P2P4]  INFO    stacktrace      src/common/stack_trace.cpp:163
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: std::bad_alloc
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [1] ${HOME}/bin/monerod:__cxa_throw+0xa7 [0x55db6a798fa7]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [2] /usr/lib64/libstdc++.so.6+0x8cd5c [0x7fbc3afddd5c]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [3] /usr/lib64/libstdc++.so.6:std::string::_Rep::_S_create(unsigned long, unsigned long, std::allocator<char> const&)+0x59 [0x7fbc3b01c819]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [4] /usr/lib64/libstdc++.so.6:std::string::_Rep::_M_clone(std::allocator<char> const&, unsigned long)+0x1b [0x7fbc3b01d5fb]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [5] /usr/lib64/libstdc++.so.6:std::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(std::string const&)+0x3c [0x7fbc3b01dcdc]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] ${HOME}/bin/monerod:std::_Rb_tree_iterator<std::pair<std::string const, unsigned int> > std::_Rb_tree<std::string, std::pair<std::string const, unsigned int>, std::_Select1st<std::pair<std::string const, unsigned int> >, std::less<std::string>, std::allocator<std::pair<std::string const, unsigned int> > >::_M_emplace_hint_unique<std::piecewise_construct_t const&, std::tuple<std::string const&>, std::tuple<> >(std::_Rb_tree_const_iterator<std::pair<std::string const, unsigned int> >, std::piecewise_construct_t const&, std::tuple<std::string const&>&&, std::tuple<>&&)+0x43 [0x55db6a4b8e83]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [7] ${HOME}/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::host_count(std::string const&, int)+0x3c7 [0x55db6a6726a7]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [8] ${HOME}/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::shutdown()+0x19e [0x55db6a672d3e]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [9] ${HOME}/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0xb0 [0x55db6a672e30]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [10] ${HOME}/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3a2 [0x55db6a64f2a2]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [11] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x414 [0x55db6a695554]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [12] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x6ce [0x55db6a6a88ce]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [13] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connect_to_seed()+0x14c [0x55db6a6ab3ec]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [14] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x32e [0x55db6a6abe7e]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [15] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x80 [0x55db6a642a30]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [16] ${HOME}/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x27 [0x55db6a65c6a7]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [17] ${HOME}/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x109 [0x55db6a643169]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [18] ${HOME}/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x8c4 [0x55db6a65a494]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [19] /usr/lib64/libboost_thread.so.1.59.0+0x115a5 [0x7fbc3b2de5a5]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [20] /lib64/libpthread.so.0+0x7684 [0x7fbc3a81b684]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163      [21] /lib64/libc.so.6:clone+0x6d [0x7fbc3a551eed]
	[P2P6]  INFO    stacktrace      src/common/stack_trace.cpp:163
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:124  Exception: std::bad_alloc
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:125  Unwound call stack:
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [1] ${HOME}/bin/monerod:__cxa_throw+0xa7 [0x55db6a798fa7]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [2] /usr/lib64/libstdc++.so.6+0x8cd5c [0x7fbc3afddd5c]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [3] /usr/lib64/libstdc++.so.6:std::string::_Rep::_S_create(unsigned long, unsigned long, std::allocator<char> const&)+0x59 [0x7fbc3b01c819]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [4] /usr/lib64/libstdc++.so.6:std::string::_Rep::_M_clone(std::allocator<char> const&, unsigned long)+0x1b [0x7fbc3b01d5fb]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [5] /usr/lib64/libstdc++.so.6:std::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(std::string const&)+0x3c [0x7fbc3b01dcdc]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [6] ${HOME}/bin/monerod:std::_Rb_tree_iterator<std::pair<std::string const, unsigned int> > std::_Rb_tree<std::string, std::pair<std::string const, unsigned int>, std::_Select1st<std::pair<std::string const, unsigned int> >, std::less<std::string>, std::allocator<std::pair<std::string const, unsigned int> > >::_M_emplace_hint_unique<std::piecewise_construct_t const&, std::tuple<std::string const&>, std::tuple<> >(std::_Rb_tree_const_iterator<std::pair<std::string const, unsigned int> >, std::piecewise_construct_t const&, std::tuple<std::string const&>&&, std::tuple<>&&)+0x43 [0x55db6a4b8e83]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [7] ${HOME}/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::host_count(std::string const&, int)+0x3c7 [0x55db6a6726a7]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [8] ${HOME}/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::shutdown()+0x19e [0x55db6a672d3e]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [9] ${HOME}/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0xb0 [0x55db6a672e30]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [10] ${HOME}/bin/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3a2 [0x55db6a64f2a2]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [11] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x6fd [0x55db6a6a88fd]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [12] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connect_to_seed()+0x14c [0x55db6a6ab3ec]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [13] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x32e [0x55db6a6abe7e]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [14] ${HOME}/bin/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x80 [0x55db6a642a30]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [15] ${HOME}/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x27 [0x55db6a65c6a7]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [16] ${HOME}/bin/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x109 [0x55db6a643169]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [17] ${HOME}/bin/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x8c4 [0x55db6a65a494]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [18] /usr/lib64/libboost_thread.so.1.59.0+0x115a5 [0x7fbc3b2de5a5]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [19] /lib64/libpthread.so.0+0x7684 [0x7fbc3a81b684]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163      [20] /lib64/libc.so.6:clone+0x6d [0x7fbc3a551eed]
	[P2P5]  INFO    stacktrace      src/common/stack_trace.cpp:163
    


# Discussion History
## moneromooo-monero | 2018-09-07T17:04:42+00:00
Looks like weird locking in what calls that code, and m_history is likely written while read. It'll take a bit to work out what this locking is supposed to do exactly. The bad_alloc exceptions in the log might be fixed by a patch that's not in a release yet (979105b2989746f1a426588862127d28c418f124).

## trasherdk | 2018-09-08T06:10:07+00:00
@moneromooo-monero 
So far it seems that the `Exception: std::bad_alloc` repeating in the logfile is fixed by the (979105b) patch.

An unpatched monerod is running, without problems, on an old Compaq laptop:
`Linux compaq-laptop 4.4.144 #2 SMP Thu Jul 26 12:45:38 CDT 2018 x86_64 Intel(R) Core(TM)2 Duo CPU     T8100  @ 2.10GHz GenuineIntel GNU/Linux` 2GB RAM.

The monorod, that had the problem, is running in a VirtualBox guest, on:
`Linux ghost-m1 4.4.144 #1 SMP Mon Aug 13 18:16:20 CEST 2018 x86_64 Intel(R) Xeon(R) CPU E3-1230 v5 @ 3.40GHz GenuineIntel GNU/Linux`.


## trasherdk | 2018-09-08T19:43:20+00:00
After applying  the (979105b) patch, both remote nodes have been running, without 
any log, or screen, messages, indicating problems.
The local node, and two wallets, unpatched, are still running, with no hickups.

Could the problem be related to Virtualbox guest?

## moneromooo-monero | 2018-09-08T22:00:51+00:00
I think the problem is incorrect locking in the traffic tracker caller.

## moneromooo-monero | 2018-09-09T12:24:33+00:00
Upon closer examination, locking seems OK. That trace could be where the damage was detected, and the corruption happened sometime earlier. If you can repro this, running monerod with ASAN (Address sanitizer, running cmake with -D SANITIZE=ON) would help spot that original location.

## trasherdk | 2018-09-09T14:25:58+00:00
Okay. (979105b) did the trick. No crashes since yesterday.
Thank you.


## trasherdk | 2018-09-11T06:06:01+00:00
@moneromooo-monero 
Just to follow up. Running a daemon, compiled with ASAN, produces the following error:
	
	=================================================================
	==14426==ERROR: LeakSanitizer: detected memory leaks

	Direct leak of 658 byte(s) in 1 object(s) allocated from:
	    #0 0x7f14f7541c6a in malloc (/usr/lib64/libasan.so.2+0x93c6a)
	    #1 0x7f14f5be60d5 in xmalloc (/lib64/libtermcap.so.2+0x10d5)
	
No other log or screen messages, that I would worry about.


## moneromooo-monero | 2018-09-11T09:09:58+00:00
That's a known leak due to using readline. Probably a race.

## trasherdk | 2018-09-11T12:12:38+00:00
I've got a few more from monero-wallet-cli

	
	=================================================================
	==13963==ERROR: LeakSanitizer: detected memory leaks
	
	Direct leak of 658 byte(s) in 1 object(s) allocated from:
	    #0 0x7fe070756c6a in malloc (/usr/lib64/libasan.so.2+0x93c6a)
	    #1 0x7fe06f5b00d5 in xmalloc (/lib64/libtermcap.so.2+0x10d5)
	
	Direct leak of 32 byte(s) in 1 object(s) allocated from:
	    #0 0x7fe070756c6a in malloc (/usr/lib64/libasan.so.2+0x93c6a)
	    #1 0x7fe06f7e8078 in xmalloc (/usr/lib64/libreadline.so.6+0x36078)
	
	Indirect leak of 2 byte(s) in 1 object(s) allocated from:
	    #0 0x7fe070756c6a in malloc (/usr/lib64/libasan.so.2+0x93c6a)
	    #1 0x7fe06f7e8078 in xmalloc (/usr/lib64/libreadline.so.6+0x36078)
	
	SUMMARY: AddressSanitizer: 692 byte(s) leaked in 3 allocation(s).
	

And on a second instance. This one looks a little more serious.

	=================================================================
	==13955==ERROR: LeakSanitizer: detected memory leaks
	
	Direct leak of 2097152 byte(s) in 1 object(s) allocated from:
	    #0 0x7fe1ac823c6a in malloc (/usr/lib64/libasan.so.2+0x93c6a)
	    #1 0x55ad1b28126f in slow_hash_allocate_state (/home/crypto/local/mining/node-1/bin-key-0/monero-wallet-cli+0x9e326f)
	
	Direct leak of 658 byte(s) in 1 object(s) allocated from:
	    #0 0x7fe1ac823c6a in malloc (/usr/lib64/libasan.so.2+0x93c6a)
	    #1 0x7fe1ab67d0d5 in xmalloc (/lib64/libtermcap.so.2+0x10d5)
	
	SUMMARY: AddressSanitizer: 2097810 byte(s) leaked in 2 allocation(s).
	
And from monerod. Same slow_hash tingy:

	
	=================================================================
	==15027==ERROR: LeakSanitizer: detected memory leaks

	Direct leak of 20971520 byte(s) in 10 object(s) allocated from:
	    #0 0x7fa872245c6a in malloc (/usr/lib64/libasan.so.2+0x93c6a)
	    #1 0x558a8be15f4f in slow_hash_allocate_state (/home/crypto/local/mining/node-1/bin-key-0/monerod+0x83ef4f)

	Direct leak of 658 byte(s) in 1 object(s) allocated from:
	    #0 0x7fa872245c6a in malloc (/usr/lib64/libasan.so.2+0x93c6a)
	    #1 0x7fa8708ea0d5 in xmalloc (/lib64/libtermcap.so.2+0x10d5)

	SUMMARY: AddressSanitizer: 20972178 byte(s) leaked in 11 allocation(s).
	


## moneromooo-monero | 2018-09-11T13:11:45+00:00
All but the last one of the same cause. The last one is fine, it's a 2 MB buffer allocated per thread for cryptonight. It's allocated on demand, but sometimes not freed. Not really a leak since it'll be reused next time the thread needs a slow hash.

## trasherdk | 2018-09-11T17:02:24+00:00
Okay. All good then.

# Action History
- Created by: trasherdk | 2018-09-07T14:45:22+00:00
- Closed at: 2018-09-11T17:02:24+00:00
