---
title: 'monerod: Exception: boost::wrapexcept<boost::bad_weak_ptr>'
source_url: https://github.com/monero-project/monero/issues/8341
author: jeffro256
assignees: []
labels: []
created_at: '2022-05-18T21:28:10+00:00'
updated_at: '2026-04-19T21:41:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is a new exception that I only started seeing recently. It occurs every ~15 seconds while running monerod, no matter the network:
```
2022-05-18 21:24:56.907	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2022-05-18 21:24:56.907	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x1cf) [0x7fd791e592f6]:_ZN5tools15log_stack_traceEPKc+0x1cf) [0x7fd791e592f6]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0xc8) [0x7fd791e59050]:__cxa_throw+0xc8) [0x7fd791e59050]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x66) [0x56113aa58294]:_ZN5boost15throw_exceptionINS_12bad_weak_ptrEEEvRKT_+0x66) [0x56113aa58294]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x84) [0x56113aa4745a]:_ZN5boost6detail12shared_countC1ERKNS0_10weak_countE+0x84) [0x56113aa4745a]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x2f) [0x7fd79447a337]:_ZN5boost10shared_ptrIN4epee9net_utils10connectionINS1_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEEEC1ISC_EERKNS_8weak_ptrIT_EE+0x2f) [0x7fd79447a337]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x36) [0x7fd79446cac6]:_ZN5boost23enable_shared_from_thisIN4epee9net_utils10connectionINS1_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEEE16shared_from_thisEv+0x36) [0x7fd79446cac6]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7]  0x3a) [0x7fd7944583d4]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE21safe_shared_from_thisEv+0x3a) [0x7fd7944583d4]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8]  0x3f) [0x7fd7944c3cc5]:_ZN4epee9net_utils10connectionINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE7add_refEv+0x3f) [0x7fd7944c3cc5]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9]  0xef) [0x7fd79442d5c9]:_ZN4epee5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE16start_outer_callEv+0xef) [0x7fd79442d5c9]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10]  0x129) [0x7fd7944202a1]:_ZN4epee5levin29async_protocol_handler_configIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEE18foreach_connectionIZNS2_11node_serverINS4_29t_cryptonote_protocol_handlerINS4_4coreEEEE12is_peer_usedERKNS2_19peerlist_entry_baseINS_9net_utils15network_addressEEEEUlRKS6_E_EEbRKT_+0x129) [0x7fd7944202a1]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0x115) [0x7fd7943e704b]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE12is_peer_usedERKNS_19peerlist_entry_baseIN4epee9net_utils15network_addressEEE+0x115) [0x7fd7943e704b]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0x4c1) [0x7fd7943eab03]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE15connect_to_seedEN4epee9net_utils4zoneE+0x4c1) [0x7fd7943eab03]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x642) [0x7fd7943e30f8]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17connections_makerEv+0x642) [0x7fd7943e30f8]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x68) [0x7fd7944687ac]:_ZNK5boost4_mfi3mf0IbN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS4_4coreEEEEEEclEPS8_+0x68) [0x7fd7944687ac]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0x52) [0x7fd794451e42]:_ZN5boost3_bi5list1INS0_5valueIPN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS5_4coreEEEEEEEEclIbNS_4_mfi3mf0IbS9_EENS0_5list0EEET_NS0_4typeISI_EERT0_RT1_l+0x52) [0x7fd794451e42]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16]  0x48) [0x7fd794438252]:_ZN5boost3_bi6bind_tIbNS_4_mfi3mf0IbN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS6_4coreEEEEEEENS0_5list1INS0_5valueIPSA_EEEEEclEv+0x48) [0x7fd794438252]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17]  0x44) [0x7fd79441c50e]:_ZN4epee11math_helper11once_a_timeINS0_21get_constant_intervalILm1000000EEELb1EE7do_callIN5boost3_bi6bind_tIbNS6_4_mfi3mf0IbN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINSD_4coreEEEEEEENS7_5list1INS7_5valueIPSH_EEEEEEEEbT_+0x44) [0x7fd79441c50e]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18]  0x118) [0x7fd7943e1e74]:_ZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE11idle_workerEv+0x118) [0x7fd7943e1e74]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19]  0x68) [0x7fd7944687ac]:_ZNK5boost4_mfi3mf0IbN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS4_4coreEEEEEEclEPS8_+0x68) [0x7fd7944687ac]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20]  0x52) [0x7fd794451e42]:_ZN5boost3_bi5list1INS0_5valueIPN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS5_4coreEEEEEEEEclIbNS_4_mfi3mf0IbS9_EENS0_5list0EEET_NS0_4typeISI_EERT0_RT1_l+0x52) [0x7fd794451e42]
2022-05-18 21:24:56.931	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0x48) [0x7fd794438252]:_ZN5boost3_bi6bind_tIbNS_4_mfi3mf0IbN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS6_4coreEEEEEEENS0_5list1INS0_5valueIPSA_EEEEEclEv+0x48) [0x7fd794438252]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22]  0x20) [0x7fd794448b48]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE20idle_callback_conextIN5boost3_bi6bind_tIbNSC_4_mfi3mf0IbNS4_11node_serverINS6_29t_cryptonote_protocol_handlerINS6_4coreEEEEEEENSD_5list1INSD_5valueIPSL_EEEEEEE12call_handlerEv+0x20) [0x7fd794448b48]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23]  0x43) [0x7fd79442daa3]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE20global_timer_handlerIN5boost3_bi6bind_tIbNSC_4_mfi3mf0IbNS4_11node_serverINS6_29t_cryptonote_protocol_handlerINS6_4coreEEEEEEENSD_5list1INSD_5valueIPSL_EEEEEEEEbNSC_10shared_ptrINSA_20idle_callback_conextIT_EEEE+0x43) [0x7fd79442daa3]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24]  0x99) [0x7fd7944a8573]:_ZNK5boost4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS2_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSD_20idle_callback_conextINS_3_bi6bind_tIbNS0_3mf0IbNS7_11node_serverINS9_29t_cryptonote_protocol_handlerINS9_4coreEEEEEEENSG_5list1INSG_5valueIPSN_EEEEEEEEEEEclEPSD_SW_+0x99) [0x7fd7944a8573]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [25]  0x91) [0x7fd7944a6393]:_ZN5boost3_bi5list2INS0_5valueIPN4epee9net_utils18boosted_tcp_serverINS3_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEEEENS2_INS_10shared_ptrINSE_20idle_callback_conextINS0_6bind_tIbNS_4_mfi3mf0IbNS8_11node_serverINSA_29t_cryptonote_protocol_handlerINSA_4coreEEEEEEENS0_5list1INS2_IPSQ_EEEEEEEEEEEEEclIbNSK_3mf1IbSE_SY_EENS0_7rrlist1IRKNS_6system10error_codeEEEEET_NS0_4typeIS1A_EERT0_RT1_l+0x91) [0x7fd7944a6393]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [26]  0x53) [0x7fd7944a3b4d]:_ZN5boost3_bi6bind_tIbNS_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS4_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSF_20idle_callback_conextINS1_IbNS2_3mf0IbNS9_11node_serverINSB_29t_cryptonote_protocol_handlerINSB_4coreEEEEEEENS0_5list1INS0_5valueIPSN_EEEEEEEEEEEENS0_5list2INSQ_IPSF_EENSQ_ISW_EEEEEclIRKNS_6system10error_codeEEEbOT_+0x53) [0x7fd7944a3b4d]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [27]  0x27) [0x7fd7944a0fdb]:_ZN5boost4asio6detail7binder1INS_3_bi6bind_tIbNS_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS7_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSI_20idle_callback_conextINS4_IbNS5_3mf0IbNSC_11node_serverINSE_29t_cryptonote_protocol_handlerINSE_4coreEEEEEEENS3_5list1INS3_5valueIPSQ_EEEEEEEEEEEENS3_5list2INST_IPSI_EENST_ISZ_EEEEEENS_6system10error_codeEEclEv+0x27) [0x7fd7944a0fdb]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [28]  0x74) [0x7fd79449e46b]:_ZN5boost4asio19asio_handler_invokeINS0_6detail7binder1INS_3_bi6bind_tIbNS_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS8_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSJ_20idle_callback_conextINS5_IbNS6_3mf0IbNSD_11node_serverINSF_29t_cryptonote_protocol_handlerINSF_4coreEEEEEEENS4_5list1INS4_5valueIPSR_EEEEEEEEEEEENS4_5list2INSU_IPSJ_EENSU_IS10_EEEEEENS_6system10error_codeEEEEEvRT_z+0x74) [0x7fd79449e46b]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [29]  0x37) [0x7fd79449bb28]:_ZN33boost_asio_handler_invoke_helpers6invokeIN5boost4asio6detail7binder1INS1_3_bi6bind_tIbNS1_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS1_10shared_ptrINSK_20idle_callback_conextINS6_IbNS7_3mf0IbNSE_11node_serverINSG_29t_cryptonote_protocol_handlerINSG_4coreEEEEEEENS5_5list1INS5_5valueIPSS_EEEEEEEEEEEENS5_5list2INSV_IPSK_EENSV_IS11_EEEEEENS1_6system10error_codeEEES18_EEvRT_RT0_+0x37) [0x7fd79449bb28]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [30]  0x27) [0x7fd794499c3e]:_ZN5boost4asio6detail19asio_handler_invokeINS1_7binder1INS_3_bi6bind_tIbNS_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS8_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSJ_20idle_callback_conextINS5_IbNS6_3mf0IbNSD_11node_serverINSF_29t_cryptonote_protocol_handlerINSF_4coreEEEEEEENS4_5list1INS4_5valueIPSR_EEEEEEEEEEEENS4_5list2INSU_IPSJ_EENSU_IS10_EEEEEENS_6system10error_codeEEES17_S19_EEvRT_PNS3_IT0_T1_EE+0x27) [0x7fd794499c3e]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [31]  0x32) [0x7fd794497d1f]:_ZN33boost_asio_handler_invoke_helpers6invokeIN5boost4asio6detail7binder1INS1_3_bi6bind_tIbNS1_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS9_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS1_10shared_ptrINSK_20idle_callback_conextINS6_IbNS7_3mf0IbNSE_11node_serverINSG_29t_cryptonote_protocol_handlerINSG_4coreEEEEEEENS5_5list1INS5_5valueIPSS_EEEEEEEEEEEENS5_5list2INSV_IPSK_EENSV_IS11_EEEEEENS1_6system10error_codeEEES1B_EEvRT_RT0_+0x32) [0x7fd794497d1f]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [32]  0x46) [0x7fd794494c40]:_ZNK5boost4asio6detail18io_object_executorINS0_8executorEE8dispatchINS1_7binder1INS_3_bi6bind_tIbNS_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINSB_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSM_20idle_callback_conextINS8_IbNS9_3mf0IbNSG_11node_serverINSI_29t_cryptonote_protocol_handlerINSI_4coreEEEEEEENS7_5list1INS7_5valueIPSU_EEEEEEEEEEEENS7_5list2INSX_IPSM_EENSX_IS13_EEEEEENS_6system10error_codeEEESaIvEEEvOT_RKT0_+0x46) [0x7fd794494c40]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [33]  0x52) [0x7fd79449042e]:_ZN5boost4asio6detail12handler_workINS_3_bi6bind_tIbNS_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS7_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSI_20idle_callback_conextINS4_IbNS5_3mf0IbNSC_11node_serverINSE_29t_cryptonote_protocol_handlerINSE_4coreEEEEEEENS3_5list1INS3_5valueIPSQ_EEEEEEEEEEEENS3_5list2INST_IPSI_EENST_ISZ_EEEEEENS1_18io_object_executorINS0_8executorEEES19_E8completeINS1_7binder1IS16_NS_6system10error_codeEEEEEvRT_RS16_+0x52) [0x7fd79449042e]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [34]  0x11d) [0x7fd79448ba5e]:_ZN5boost4asio6detail12wait_handlerINS_3_bi6bind_tIbNS_4_mfi3mf1IbN4epee9net_utils18boosted_tcp_serverINS7_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEENS_10shared_ptrINSI_20idle_callback_conextINS4_IbNS5_3mf0IbNSC_11node_serverINSE_29t_cryptonote_protocol_handlerINSE_4coreEEEEEEENS3_5list1INS3_5valueIPSQ_EEEEEEEEEEEENS3_5list2INST_IPSI_EENST_ISZ_EEEEEENS1_18io_object_executorINS0_8executorEEEE11do_completeEPvPNS1_19scheduler_operationERKNS_6system10error_codeEm+0x11d) [0x7fd79448ba5e]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [35]  0x3a) [0x56113aa48b5c]:_ZN5boost4asio6detail19scheduler_operation8completeEPvRKNS_6system10error_codeEm+0x3a) [0x56113aa48b5c]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [36]  0x1c6) [0x56113aa4d080]:_ZN5boost4asio6detail9scheduler10do_run_oneERNS1_27conditionally_enabled_mutex11scoped_lockERNS1_21scheduler_thread_infoERKNS_6system10error_codeE+0x1c6) [0x56113aa4d080]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [37]  0xf8) [0x56113aa4c77c]:_ZN5boost4asio6detail9scheduler3runERNS_6system10error_codeE+0xf8) [0x56113aa4c77c]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [38]  0x4c) [0x56113aa4d56c]:_ZN5boost4asio10io_context3runEv+0x4c) [0x56113aa4d56c]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [39]  0x146) [0x7fd79442e588]:_ZN4epee9net_utils18boosted_tcp_serverINS_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEE13worker_threadEv+0x146) [0x7fd79442e588]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [40]  0x68) [0x7fd7944c849a]:_ZNK5boost4_mfi3mf0IbN4epee9net_utils18boosted_tcp_serverINS2_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEEEclEPSD_+0x68) [0x7fd7944c849a]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [41]  0x52) [0x7fd7944c70cc]:_ZN5boost3_bi5list1INS0_5valueIPN4epee9net_utils18boosted_tcp_serverINS3_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEEEEEclIbNS_4_mfi3mf0IbSE_EENS0_5list0EEET_NS0_4typeISN_EERT0_RT1_l+0x52) [0x7fd7944c70cc]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [42]  0x48) [0x7fd7944c4c5e]:_ZN5boost3_bi6bind_tIbNS_4_mfi3mf0IbN4epee9net_utils18boosted_tcp_serverINS4_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEEEENS0_5list1INS0_5valueIPSF_EEEEEclEv+0x48) [0x7fd7944c4c5e]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [43]  0x22) [0x7fd7944c0b90]:_ZN5boost6detail11thread_dataINS_3_bi6bind_tIbNS_4_mfi3mf0IbN4epee9net_utils18boosted_tcp_serverINS6_5levin22async_protocol_handlerIN8nodetool24p2p_connection_context_tIN10cryptonote29cryptonote_connection_contextEEEEEEEEENS2_5list1INS2_5valueIPSH_EEEEEEE3runEv+0x22) [0x7fd7944c0b90]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [44]  0x1143b) [0x7fd79122643b]:_64-linux-gnu/libboost_thread.so.1.71.0(+0x1143b) [0x7fd79122643b]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [45]  0x8609) [0x7fd790d87609]:_64-linux-gnu/libpthread.so.0(+0x8609) [0x7fd790d87609]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [46]  0x43) [0x7fd790cac163]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7fd790cac163]
2022-05-18 21:24:56.932	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172
```

System:
```
OS: Ubuntu 20
CPU: Intel Xeon E5-1650v4
RAM: 32 GB
Compiler: g++ (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
```

# Discussion History
## engdude | 2022-08-09T22:31:41+00:00
I got the same issue on ubuntu 22.04 with 8 Gig and fixed it ( mostly - it's now very rare) with 
vm.nr_hugepages=1280
in sysctl.conf

my monerod is running as it's own user

## shaohme | 2024-04-01T09:30:11+00:00
This happens for me too, although no usable stack trace in my current build

```
2024-04-01 09:01:43.457	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2496	
2024-04-01 09:01:43.457	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2496	**********************************************************************
2024-04-01 09:01:43.457	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2496	You are now synchronized with the network. You may now start monero-wallet-cli.
2024-04-01 09:01:43.457	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2496	
2024-04-01 09:01:43.457	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2496	Use the "help" command to see the list of available commands.
2024-04-01 09:01:43.457	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2496	**********************************************************************
2024-04-01 09:13:48.449	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2024-04-01 09:13:48.449	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-04-01 09:13:48.449	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [1]  0x12f) [0x55dae531f312]:__cxa_throw+0x12f) [0x55dae531f312]
2024-04-01 09:13:48.449	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [2] /usr/bin/monerod(+0x44cc7) [0x55dae5301cc7] 
2024-04-01 09:13:48.449	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [3] /usr/bin/monerod(+0x3f38d4) [0x55dae56b08d4] 
2024-04-01 09:13:48.449	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [4] /usr/bin/monerod(+0x40b63c) [0x55dae56c863c] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [5] /usr/bin/monerod(+0x413439) [0x55dae56d0439] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [6] /usr/bin/monerod(+0x41378c) [0x55dae56d078c] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [7] /usr/bin/monerod(+0x469a17) [0x55dae5726a17] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [8] /usr/bin/monerod(+0x477111) [0x55dae5734111] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [9] /usr/bin/monerod(+0x479bb4) [0x55dae5736bb4] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [10] /usr/bin/monerod(+0x47b79b) [0x55dae573879b] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [11] /usr/bin/monerod(+0x3e8bb8) [0x55dae56a5bb8] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [12] /usr/bin/monerod(+0x42533b) [0x55dae56e233b] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [13] /usr/bin/monerod(+0x42886a) [0x55dae56e586a] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [14] /usr/bin/monerod(+0xfd76f) [0x55dae53ba76f] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [15] /usr/bin/monerod(+0x3d00c1) [0x55dae568d0c1] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [16] /usr/bin/monerod(+0x4114b6) [0x55dae56ce4b6] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [17]  0x94ae) [0x7fc711a074ae]:_thread.so.1.84.0(+0x94ae) [0x7fc711a074ae]
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [18] /usr/lib64/libc.so.6(+0x86f4c) [0x7fc7110c6f4c] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	   [19] /usr/lib64/libc.so.6(+0xf8548) [0x7fc711138548] 
2024-04-01 09:13:48.450	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

## e9x | 2025-01-20T02:57:54+00:00
Bruh!!!! Is there any better solution besides ignoring this error in logs? 🙈

## vtnerd | 2025-01-20T23:46:00+00:00
PR #7345 should fix this. I need to rebase the PR, and resolve the possible memory leak. The latter is going to be difficult, as it was never obvious why the patch created a memory leak (ASAN reported no leaks).


## What's Happening

The `foreach_connection` function is called _just before_ a `connection_ptr` goes out of scope. The destructor of the connection object is blocked waiting on `foreach_connection`, while `foreach_connection` tries to get `shared_from_this()` to increment the `shared_ptr` `strong_count`. Since the object is already in the destructor, the `shared_ptr` already has a `strong_count == 0`, and an exception is thrown.


## Fundamental Problem

The `shared_ptr` isn't being used correctly - the connection map has a raw pointer instead of a `weak_ptr`. Using `weak_ptr.lock()` will correctly "synchronize" the two events such that a `nullptr` will be returned (and hopefully checked) by `foreach_connection` instead of an exception being thrown.


## No Other Fix

`shared_from_this()` doesn't have a non-throwing overload because it normally is only invoked when `1 <= strong_count`. So aside from #7345 style fix, I don't think anything else can be done other than disabling stack tracing when **building** `monerod`.

## c3cuddles | 2025-12-24T20:36:36+00:00
Hoping PR #7345 gets merged soon. In my case, these boost weakptr exceptions made up 99.99% of my log files before adjusting the log level to exclude them:

```
$ tail -n 10000 /var/log/monero/monero.log | grep -v 'stacktrace'
2025-12-24 19:19:37.025 [P2P4]  INFO    global  src/p2p/net_node.inl:192        Host 5.12.58.238 unblocked.
```

## selsta | 2025-12-24T20:38:41+00:00
#7345 is unfortunately broken, there is a subtle bug that shows up after a week or so and crashes the node. We were not able to track it down yet.

## e9x | 2026-04-19T21:41:11+00:00
put a cronjob on it and continue ignoring the error!!!! issue closed as not planned!!!!!!!!!!

# Action History
- Created by: jeffro256 | 2022-05-18T21:28:10+00:00
