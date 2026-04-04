---
title: 'Error level message:'
source_url: https://github.com/monero-project/monero/issues/6630
author: ronohara
assignees: []
labels: []
created_at: '2020-06-06T10:01:00+00:00'
updated_at: '2020-06-22T04:58:14+00:00'
type: issue
status: closed
closed_at: '2020-06-08T10:24:11+00:00'
---

# Original Description
'Nitrogen Nebula' (v0.16.0.0-release)

Lots of these messages. But the daemon seems to be functioning. Any thoughts ?

ot found in txpool: 
2020-06-06 06:36:45.306	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-06-06 06:58:32.192	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-06-06 07:16:45.895	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-06-06 07:24:54.837	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-06-06 07:29:45.545	I SYNCHRONIZED OK
2020-06-06 07:33:21.374	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-06-06 07:36:42.292	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-06-06 07:49:44.001	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-06-06 08:00:17.878	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-06-06 08:24:15.897	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-06-06 09:05:47.332	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-06-06 09:17:42.161	E Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2


# Discussion History
## moneromooo-monero | 2020-06-06T11:18:51+00:00
Do you have a stack trace for it (see the log).

## ronohara | 2020-06-06T20:18:53+00:00
2020-06-06 20:12:52.764 [P2P3]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:1519    Exception at [core::handle_incoming_block()], what
=Tx not found in txpool: 
2020-06-06 20:13:33.530 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2020-06-06 20:13:33.531 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x119) [0x55d381acf44c]:__cxa_throw+0x119) [0x55d
381acf44c]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [2] monerod(+0x37215e) [0x55d381b1415e] 
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x30) [0x55d38219d810]:_ZN7randomx6VmBaseINS_18La
rgePageAllocatorELb0EE8allocateEv+0x30) [0x55d38219d810]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0xef) [0x55d38219af2f]:_create_vm+0xef) [0x55d382
19af2f]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x471) [0x55d381fbe511]:_slow_hash+0x471) [0x55d3
81fbe511]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0xb9) [0x55d381fa71c9]:_ZN10cryptonote18get_block
_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xb9) [0x55d381fa71c9]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [7]  0x27) [0x55d381fa7337]:_ZN10cryptonote18get_block
_longhashEPKNS_10BlockchainERKNS_5blockEmi+0x27) [0x55d381fa7337]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [8]  0xb7) [0x55d381f4b697]:_ZNK10cryptonote10Blockcha
in21block_longhash_workerEmRKN4epee4spanIKNS_5blockEEERSt13unordered_mapIN6crypto4hashESA_St4hashISA_ESt8equal_toISA_ESaISt4pairIKSA_SA_EEE+0xb7) 
[0x55d381f4b697]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [9]  0x43a) [0x55d38200145a]:_ZN5tools10threadpool3run
Eb+0x43a) [0x55d38200145a]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [10]  0x3e) [0x55d382001dde]:_ZN5tools10threadpool6wai
ter4waitEPS0_+0x3e) [0x55d382001dde]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [11]  0x11a9) [0x55d381f4e009]:_ZN10cryptonote10Blockc
hain30prepare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x11a9) [0x55d381f4e009]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [12]  0x41) [0x55d381f73d71]:_ZN10cryptonote4core30pre
pare_handle_incoming_blocksERKSt6vectorINS_20block_complete_entryESaIS2_EERS1_INS_5blockESaIS7_EE+0x41) [0x55d381f73d71]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [13]  0x25fd) [0x55d381eca94d]:_ZN10cryptonote29t_cryp
tonote_protocol_handlerINS_4coreEE30handle_notify_new_fluffy_blockEiRN4epee10misc_utils11struct_initINS_23NOTIFY_NEW_FLUFFY_BLOCK9request_tEEERNS_
29cryptonote_connection_contextE+0x25fd) [0x55d381eca94d]
2020-06-06 20:13:33.537 [P2P7]  INFO    stacktrace      src/common/stack_trace.cpp:172      [14]  0x1d15) [0x55d381bf8a35]:_ZN8nodetool11node_serv
erIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE17handle_invoke_mapINS_24p2p_connection_context_tINS1_29cryptonote_connection_context
EEEEEibiN4epee4spanIKhEERNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEERT_Rb+0x1d15) [0x55d381bf8a35]
@


## moneromooo-monero | 2020-06-07T00:08:34+00:00
This is an unrelated exception.

## ronohara | 2020-06-08T06:28:50+00:00
These messages are immediately after the Error level message - so if they are unrelated then the Error message does not trigger a stack trace.  

## ronohara | 2020-06-08T10:24:11+00:00
I guess this is mostly cosmetic then.. I will close the issue.

## hundehausen | 2020-06-10T14:34:36+00:00
I get these error messages since I upgraded to v.0.16.0.0 on my public node: 

2020-05-27 14:12:15.243	    7f4b16392780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-05-27 14:12:15.243	    7f4b16392780	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-05-27 14:12:15.243	    7f4b16392780	INFO	global	src/daemon/main.cpp:271	Monero 'Nitrogen Nebula' (v0.16.0.0-release)
2020-05-27 14:12:15.243	    7f4b16392780	INFO	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2020-05-27 14:12:15.245	    7f4b16392780	WARNING	daemon	src/daemon/executor.cpp:61	Monero 'Nitrogen Nebula' (v0.16.0.0-release) Daemonised
2020-05-27 14:12:15.245	    7f4b16392780	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2020-05-27 14:12:15.245	    7f4b16392780	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2020-05-27 14:12:15.247	    7f4b16392780	INFO	global	src/daemon/core.h:63	Initializing core...
2020-05-27 14:12:15.247	    7f4b16392780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:506	Loading blockchain from folder /home/monero/.bitmonero/lmdb ...
2020-05-27 14:12:15.247	    7f4b16392780	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1326	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2020-05-27 14:12:21.685	    7f4b16392780	INFO	global	src/cryptonote_core/cryptonote_core.cpp:668	Loading checkpoints
2020-05-27 14:12:21.687	    7f4b16392780	INFO	global	src/daemon/core.h:73	Core initialized OK
2020-05-27 14:12:21.687	    7f4b16392780	INFO	global	src/daemon/p2p.h:63	Initializing p2p server...
2020-05-27 14:12:21.694	    7f4b16392780	INFO	global	src/daemon/p2p.h:68	p2p server initialized OK
2020-05-27 14:12:21.694	    7f4b16392780	INFO	global	src/daemon/rpc.h:63	Initializing core RPC server...
2020-05-27 14:12:21.694	    7f4b16392780	WARNING	daemon.rpc	src/rpc/core_rpc_server.cpp:305	The RPC server is accessible from the outside, but no RPC payment was setup. RPC access will be free for all.
2020-05-27 14:12:21.694	    7f4b16392780	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 0.0.0.0 (IPv4):18081
2020-05-27 14:12:23.631	    7f4b16392780	INFO	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2020-05-27 14:12:23.631	    7f4b16392780	INFO	global	src/daemon/rpc.h:74	Starting core RPC server...
2020-05-27 14:12:23.631	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:79	core RPC server started ok
2020-05-27 14:12:23.632	[SRV_MAIN]	INFO	global	src/daemon/daemon.cpp:203	Public RPC port 18081 will be advertised to other peers over P2P
2020-05-27 14:12:23.632	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:78	Starting p2p net loop...
2020-05-27 14:12:24.259	[P2P8]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2341	
2020-05-27 14:12:24.259	[P2P8]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2341	**********************************************************************
2020-05-27 14:12:24.259	[P2P8]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2341	You are now synchronized with the network. You may now start monero-wallet-cli.
2020-05-27 14:12:24.259	[P2P8]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2341	
2020-05-27 14:12:24.259	[P2P8]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2341	Use the "help" command to see the list of available commands.
2020-05-27 14:12:24.259	[P2P8]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2341	**********************************************************************
2020-05-27 14:12:24.633	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1654	
2020-05-27 14:12:24.633	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1654	**********************************************************************
2020-05-27 14:12:24.633	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1654	The daemon will start synchronizing with the network. This may take a long time to complete.
2020-05-27 14:12:24.633	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1654	
2020-05-27 14:12:24.633	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1654	You can set the level of process detailization through "set_log <level|categories>" command,
2020-05-27 14:12:24.633	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1654	where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-05-27 14:12:24.633	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1654	
2020-05-27 14:12:24.633	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1654	Use the "help" command to see the list of available commands.
2020-05-27 14:12:24.633	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1654	Use "help <command>" to see a command's documentation.
2020-05-27 14:12:24.633	[P2P7]	INFO	global	src/cryptonote_core/cryptonote_core.cpp:1654	**********************************************************************
2020-05-27 14:12:24.732	[miner 0]	INFO	global	src/cryptonote_basic/miner.cpp:526	Miner thread was started [0]
2020-05-27 16:22:32.829	[P2P9]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 16:26:31.576	[P2P8]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 16:30:44.818	[P2P9]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 16:31:51.307	[P2P8]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 16:42:35.235	[P2P3]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 16:48:02.247	[P2P2]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 16:56:02.469	[P2P7]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 16:56:32.550	[P2P7]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 16:59:16.943	[P2P0]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:01:11.578	[P2P0]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:01:31.396	[P2P2]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:03:55.433	[P2P1]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:04:59.415	[P2P1]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:07:25.093	[P2P2]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:13:06.487	[P2P9]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:14:47.655	[P2P6]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:18:19.646	[P2P5]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:20:18.689	[P2P0]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:23:25.045	[P2P1]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:28:01.819	[P2P0]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:32:35.410	[P2P8]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:33:11.627	[P2P1]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:33:12.343	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2301	SYNCHRONIZED OK
2020-05-27 17:37:23.442	[P2P0]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:38:12.835	[P2P8]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:46:45.156	[P2P4]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:55:37.858	[P2P4]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:56:14.195	[P2P1]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:57:15.840	[P2P3]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 17:57:29.168	[P2P2]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-27 18:00:20.950	[P2P4]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool:



2020-05-28 16:27:15.787	[P2P1]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:27:15.787	[P2P1]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:31:03.930	[P2P6]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:31:03.930	[P2P6]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:35:16.325	[P2P4]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-28 16:37:36.108	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:37:36.108	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:41:45.862	[P2P0]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-28 16:47:21.446	[P2P9]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-28 16:51:26.886	[P2P9]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:51:26.887	[P2P9]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:52:22.892	[P2P5]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-28 16:54:20.244	[P2P3]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:54:20.245	[P2P3]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:55:17.989	[P2P8]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:55:17.989	[P2P8]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:56:24.949	[P2P5]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:56:24.949	[P2P5]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 16:56:42.275	[P2P5]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-28 16:58:19.080	[P2P5]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1519	Exception at [core::handle_incoming_block()], what=Tx not found in txpool: 
2020-05-28 17:00:34.484	[P2P0]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:00:34.484	[P2P0]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:00:44.446	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:00:44.446	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:03:55.315	[P2P5]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:03:55.315	[P2P5]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:04:48.738	[P2P8]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:04:48.738	[P2P8]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:05:12.905	[P2P8]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:05:12.905	[P2P8]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:06:54.966	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:06:54.966	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:08:35.379	[P2P6]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:08:35.379	[P2P6]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:09:14.204	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:09:14.204	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:10:07.376	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:10:07.376	[P2P2]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:10:22.641	[P2P0]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:10:22.641	[P2P0]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta
2020-05-28 17:13:59.617	[P2P1]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:1356	  failed to find tx meta




## ReadandSweepm | 2020-06-11T10:48:00+00:00
I have the same issue

## Cideg | 2020-06-12T15:07:49+00:00
I have the same problem

```
2020-06-12 15:05:12.899 E Exception at [core::handle_incoming_block()], what=Tx not found in txpool:

```


## Hohhle | 2020-06-22T04:58:14+00:00
Same issue as well. Stops with stop_mining command.
But prevents mining via start_mining command with that error unless save/exit and restarting daemon. Does it occur when an orphan block is known to occur, even though daemon was still on main chain?

# Action History
- Created by: ronohara | 2020-06-06T10:01:00+00:00
- Closed at: 2020-06-08T10:24:11+00:00
