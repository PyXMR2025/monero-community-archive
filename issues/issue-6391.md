---
title: There is a problem in sync during monerod. Who can give me some suggestions？
source_url: https://github.com/monero-project/monero/issues/6391
author: xcoin-dev
assignees: []
labels: []
created_at: '2020-03-15T08:52:57+00:00'
updated_at: '2022-03-16T15:51:25+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:51:24+00:00'
---

# Original Description
set_log 4
Log level is now 4
2020-03-15 08:45:03.315 T [sock 28] Some not success at read: End of file:2
2020-03-15 08:45:03.315 T [sock 28] peer closed connection
2020-03-15 08:45:03.315 T Closed connection from host 46.32.53.120: 1
2020-03-15 08:45:03.315 I Failed to invoke command 1001 return code -3
2020-03-15 08:45:03.315 W [46.32.53.120:18089 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-03-15 08:45:03.315 T [46.32.53.120:18089 OUT] [levin_protocol] <<-- finish_outer_call
2020-03-15 08:45:03.315 W [46.32.53.120:18089 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 08:45:03.315 T [46.32.53.120:18089 OUT] [sock 28] release
2020-03-15 08:45:03.316 T [sock 28] Socket destroyed
2020-03-15 08:45:03.316 I [46.32.53.120:18089 OUT] [priority]Failed to HANDSHAKE with peer 46.32.53.120:18089
2020-03-15 08:45:03.316 I [46.32.53.120:18089 OUT] [0] state: closed in state before_handshake
2020-03-15 08:45:03.316 D Connecting to 95.217.11.65:18089(peer_type=1, last_seen: never)...
2020-03-15 08:45:03.316 I [46.32.53.120:18089 1878e0b4-35be-4cff-96b3-adc51b824ba6 OUT] CLOSE CONNECTION
2020-03-15 08:45:03.316 T [46.32.53.120:18089 OUT] ~async_protocol_handler()
2020-03-15 08:45:03.316 D Spawned connection #58 to 0.0.0.0 currently we have sockets count:3
2020-03-15 08:45:03.316 D test, connection constructor set m_connection_type=2
2020-03-15 08:45:03.316 D Destructing connection #57 to 46.32.53.120
2020-03-15 08:45:03.316 D connections_ size now 1
2020-03-15 08:45:03.316 D Trying to connect to 95.217.11.65:18089, bind_ip = 0.0.0.0
2020-03-15 08:45:03.694 T Connected success to 95.217.11.65:18089
2020-03-15 08:45:03.695 T [sock 0x7f054c02f140] new connection from 95.217.11.65:18089 OUT to 192.168.0.12:33748, total sockets objects 2
2020-03-15 08:45:03.695 T New connection from host 95.217.11.65: 0
2020-03-15 08:45:03.695 I [95.217.11.65:18089 847c0c10-830e-42e5-bf3a-282ab936ac25 OUT] NEW CONNECTION
2020-03-15 08:45:03.695 T Setting 00:00:10 expiry
2020-03-15 08:45:03.695 D  connection type P2P 192.168.0.12:33748 <--> 95.217.11.65:18089 (via 95.217.11.65:18089)
2020-03-15 08:45:03.695 T Blockchain::get_tail_id
2020-03-15 08:45:03.695 T BlockchainLMDB::top_block_hash
2020-03-15 08:45:03.695 T BlockchainLMDB::height
2020-03-15 08:45:03.695 T BlockchainLMDB::block_rtxn_start
2020-03-15 08:45:03.695 T mdb_txn_safe: destructor
2020-03-15 08:45:03.695 T BlockchainLMDB::get_block_hash_from_height
2020-03-15 08:45:03.695 T BlockchainLMDB::block_rtxn_start
2020-03-15 08:45:03.695 T mdb_txn_safe: destructor
2020-03-15 08:45:03.695 T BlockchainLMDB::get_block_cumulative_difficulty  height: 0
2020-03-15 08:45:03.695 T BlockchainLMDB::block_rtxn_start
2020-03-15 08:45:03.695 T mdb_txn_safe: destructor
2020-03-15 08:45:03.695 T BlockchainLMDB::get_blockchain_pruning_seed
2020-03-15 08:45:03.695 T BlockchainLMDB::block_rtxn_start
2020-03-15 08:45:03.695 T mdb_txn_safe: destructor
2020-03-15 08:45:03.695 T [95.217.11.65:18089 OUT] [levin_protocol] -->> start_outer_call
2020-03-15 08:45:03.695 T Moving counter buffer by 1 second 0 < 279988 (last time 0)
2020-03-15 08:45:03.695 T Throttle throttle_speed_out: packet of ~352b  (from 352 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [352 0 0 0 0 0 0 0 0 0 ]
2020-03-15 08:45:03.695 D do_send_chunk() NOW SENSD: packet=352 B
2020-03-15 08:45:03.695 T handler_write (direct) - before ASIO write, for packet=352 B (after sleep)
2020-03-15 08:45:03.695 T Setting 00:05:00 expiry
2020-03-15 08:45:03.696 D [95.217.11.65:18089 OUT] LEVIN_PACKET_SENT. [len=319, flags1, r?=1, cmd = 1001, ver=1
2020-03-15 08:45:03.696 T [95.217.11.65:18089 OUT] [levin_protocol] -->> start_outer_call
2020-03-15 08:45:03.696 D [95.217.11.65:18089 OUT] anvoke_handler, timeout: 5000
2020-03-15 08:45:03.696 T [95.217.11.65:18089 OUT] [levin_protocol] <<-- finish_outer_call
2020-03-15 08:45:03.696 T [95.217.11.65:18089 OUT] [sock 28] release
2020-03-15 08:45:03.696 T [95.217.11.65:18089 OUT] [sock 28] Async send calledback 352
2020-03-15 08:45:03.696 T Moving counter buffer by 1 second 279987 < 279988 (last time 279987)
2020-03-15 08:45:03.696 T dbg >>> global-OUT: speed is A= 114.459 vs Max=2.09715e+06  so sleep: D=-9.22546 sec E=    1056 (Enow=    1408) M=2.09715e+06 W=   9.226 R=1.93473e+07 Wgood      11 History: [0 352 0 352 0 0 0 0 0 352 ] m_last_sample_time=  279988
2020-03-15 08:45:03.696 T Throttle >>> global-OUT: packet of ~352b  (from 352 b) Speed AVG=   0[w=9.226]    0[w=9.226] /  Limit=2048 KiB/sec  [352 352 0 352 0 0 0 0 0 352 ]
2020-03-15 08:45:08.696 I [95.217.11.65:18089 OUT] Timeout on invoke operation happened, command: 1001 timeout: 5000
2020-03-15 08:45:08.696 I Failed to invoke command 1001 return code -4
2020-03-15 08:45:08.696 W [95.217.11.65:18089 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2020-03-15 08:45:08.696 W [95.217.11.65:18089 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 08:45:08.696 T Closed connection from host 95.217.11.65: 1
2020-03-15 08:45:08.696 T [sock 28] Some not success at read: End of file:2
2020-03-15 08:45:08.697 I [95.217.11.65:18089 OUT] [priority]Failed to HANDSHAKE with peer 95.217.11.65:18089
2020-03-15 08:45:08.697 T [sock 28] peer closed connection
2020-03-15 08:45:08.697 D Connecting to 95.217.2.237:18089(peer_type=1, last_seen: never)...
2020-03-15 08:45:08.697 T [95.217.11.65:18089 OUT] [levin_protocol] <<-- finish_outer_call
2020-03-15 08:45:08.697 T [95.217.11.65:18089 OUT] [sock 28] release
2020-03-15 08:45:08.697 T [sock 28] Socket destroyed
2020-03-15 08:45:08.697 D Spawned connection #59 to 0.0.0.0 currently we have sockets count:3
2020-03-15 08:45:08.697 D test, connection constructor set m_connection_type=2
2020-03-15 08:45:08.697 D connections_ size now 1
2020-03-15 08:45:08.697 I [95.217.11.65:18089 OUT] [0] state: closed in state before_handshake
2020-03-15 08:45:08.697 D Trying to connect to 95.217.2.237:18089, bind_ip = 0.0.0.0
2020-03-15 08:45:08.698 I [95.217.11.65:18089 847c0c10-830e-42e5-bf3a-282ab936ac25 OUT] CLOSE CONNECTION
2020-03-15 08:45:08.698 T [95.217.11.65:18089 OUT] ~async_protocol_handler()
2020-03-15 08:45:08.698 D Destructing connection #58 to 95.217.11.65
2020-03-15 08:45:09.090 T Connected success to 95.217.2.237:18089
2020-03-15 08:45:09.091 T [sock 0x7f054c00f870] new connection from 95.217.2.237:18089 OUT to 192.168.0.12:54792, total sockets objects 2
2020-03-15 08:45:09.091 T New connection from host 95.217.2.237: 0
2020-03-15 08:45:09.091 I [95.217.2.237:18089 2676d693-a585-4bca-a11c-079e1f9d4f2b OUT] NEW CONNECTION
2020-03-15 08:45:09.091 T Setting 00:00:10 expiry
2020-03-15 08:45:09.091 D  connection type P2P 192.168.0.12:54792 <--> 95.217.2.237:18089 (via 95.217.2.237:18089)
2020-03-15 08:45:09.091 T Blockchain::get_tail_id
2020-03-15 08:45:09.091 T BlockchainLMDB::top_block_hash
2020-03-15 08:45:09.091 T BlockchainLMDB::height
2020-03-15 08:45:09.091 T BlockchainLMDB::block_rtxn_start
2020-03-15 08:45:09.091 T mdb_txn_safe: destructor
2020-03-15 08:45:09.091 T BlockchainLMDB::get_block_hash_from_height
2020-03-15 08:45:09.091 T BlockchainLMDB::block_rtxn_start
2020-03-15 08:45:09.091 T mdb_txn_safe: destructor
2020-03-15 08:45:09.091 T BlockchainLMDB::get_block_cumulative_difficulty  height: 0
2020-03-15 08:45:09.091 T BlockchainLMDB::block_rtxn_start
2020-03-15 08:45:09.091 T mdb_txn_safe: destructor
2020-03-15 08:45:09.091 T BlockchainLMDB::get_blockchain_pruning_seed
2020-03-15 08:45:09.091 T BlockchainLMDB::block_rtxn_start
2020-03-15 08:45:09.091 T mdb_txn_safe: destructor
2020-03-15 08:45:09.091 T [95.217.2.237:18089 OUT] [levin_protocol] -->> start_outer_call
2020-03-15 08:45:09.091 T Moving counter buffer by 1 second 0 < 279993 (last time 0)
2020-03-15 08:45:09.092 T Throttle throttle_speed_out: packet of ~352b  (from 352 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [352 0 0 0 0 0 0 0 0 0 ]
2020-03-15 08:45:09.092 D do_send_chunk() NOW SENSD: packet=352 B
2020-03-15 08:45:09.092 T handler_write (direct) - before ASIO write, for packet=352 B (after sleep)
2020-03-15 08:45:09.092 T Setting 00:05:00 expiry
2020-03-15 08:45:09.092 D [95.217.2.237:18089 OUT] LEVIN_PACKET_SENT. [len=319, flags1, r?=1, cmd = 1001, ver=1
2020-03-15 08:45:09.092 T [95.217.2.237:18089 OUT] [levin_protocol] -->> start_outer_call
2020-03-15 08:45:09.092 D [95.217.2.237:18089 OUT] anvoke_handler, timeout: 5000
2020-03-15 08:45:09.092 T [95.217.2.237:18089 OUT] [levin_protocol] <<-- finish_outer_call
2020-03-15 08:45:09.092 T [95.217.2.237:18089 OUT] [sock 29] release
2020-03-15 08:45:09.092 T [95.217.2.237:18089 OUT] [sock 29] Async send calledback 352
2020-03-15 08:45:09.092 T Moving counter buffer by 1 second 279988 < 279993 (last time 279988)
2020-03-15 08:45:09.092 T Moving counter buffer by 1 second 279989 < 279993 (last time 279989)
2020-03-15 08:45:09.092 T Moving counter buffer by 1 second 279990 < 279993 (last time 279990)
2020-03-15 08:45:09.092 T Moving counter buffer by 1 second 279991 < 279993 (last time 279991)
2020-03-15 08:45:09.092 T Moving counter buffer by 1 second 279992 < 279993 (last time 279992)
2020-03-15 08:45:09.092 T dbg >>> global-OUT: speed is A= 109.737 vs Max=2.09715e+06  so sleep: D=-9.62246 sec E=    1056 (Enow=    1408) M=2.09715e+06 W=   9.623 R=2.01798e+07 Wgood      11 History: [0 0 0 0 0 352 352 0 352 0 ] m_last_sample_time=  279994
2020-03-15 08:45:09.092 T Throttle >>> global-OUT: packet of ~352b  (from 352 b) Speed AVG=   0[w=9.623]    0[w=9.623] /  Limit=2048 KiB/sec  [352 0 0 0 0 352 352 0 352 0 ]
set_log 0

# Discussion History
## xcoin-dev | 2020-03-15T08:53:44+00:00
ufw is disable and isp is ok.
i can telnet my server:18080,
but height always 1,can't sync network

## xcoin-dev | 2020-03-15T08:57:35+00:00
start:
./monerod --data-dir="/monerodata/moneroblock" --add-priority-node=opennode.xmr-tw.org:18089 --add-priority-node=node.moneroworld.com:18089 --add-priority-node=uwillrunanodesoon.moneroworld.com:18089 --add-priority-node=node.xmr.to:18081 --add-priority-node=nodes.hashvault.pro:18081 --add-priority-node=node.supportxmr.com:18081

add many peers ...
who can help me about it

## xcoin-dev | 2020-03-15T09:29:57+00:00
2020-03-15 09:28:51.958 W [71.127.156.63:18089 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-03-15 09:28:51.958 W [71.127.156.63:18089 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 09:28:51.958 I [71.127.156.63:18089 OUT] [priority]Failed to HANDSHAKE with peer 71.127.156.63:18089
2020-03-15 09:28:51.959 I [71.127.156.63:18089 OUT] [0] state: closed in state before_handshake
2020-03-15 09:28:51.959 I [71.127.156.63:18089 0992303e-66bb-416d-8344-9a7a982b4ea8 OUT] CLOSE CONNECTION
2020-03-15 09:28:52.116 I [162.210.173.15:18089 19454f70-ca8e-4e24-a6e5-60af0e05b39d OUT] NEW CONNECTION
2020-03-15 09:28:52.273 I Failed to invoke command 1001 return code -3
2020-03-15 09:28:52.273 W [162.210.173.15:18089 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-03-15 09:28:52.273 W [162.210.173.15:18089 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 09:28:52.273 I [162.210.173.15:18089 OUT] [priority]Failed to HANDSHAKE with peer 162.210.173.15:18089
2020-03-15 09:28:52.273 I [162.210.173.15:18089 OUT] [0] state: closed in state before_handshake
2020-03-15 09:28:52.273 I [162.210.173.15:18089 19454f70-ca8e-4e24-a6e5-60af0e05b39d OUT] CLOSE CONNECTION
2020-03-15 09:28:52.525 I [73.62.241.45:18089 5cb8bd5f-ca2a-45f0-a0d4-fd1a2e4274cd OUT] NEW CONNECTION
2020-03-15 09:28:52.777 I Failed to invoke command 1001 return code -3
2020-03-15 09:28:52.777 W [73.62.241.45:18089 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-03-15 09:28:52.777 W [73.62.241.45:18089 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 09:28:52.777 I [73.62.241.45:18089 OUT] [priority]Failed to HANDSHAKE with peer 73.62.241.45:18089
2020-03-15 09:28:52.777 I [73.62.241.45:18089 OUT] [0] state: closed in state before_handshake
2020-03-15 09:28:52.777 I [73.62.241.45:18089 5cb8bd5f-ca2a-45f0-a0d4-fd1a2e4274cd OUT] CLOSE CONNECTION
2020-03-15 09:28:53.021 I [116.203.154.248:18089 4c25734c-b5e5-4181-82e9-f610d221f36c OUT] NEW CONNECTION
2020-03-15 09:28:58.021 I [116.203.154.248:18089 OUT] Timeout on invoke operation happened, command: 1001 timeout: 5000
2020-03-15 09:28:58.021 I Failed to invoke command 1001 return code -4
2020-03-15 09:28:58.021 W [116.203.154.248:18089 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2020-03-15 09:28:58.021 W [116.203.154.248:18089 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 09:28:58.021 I [116.203.154.248:18089 OUT] [0] state: closed in state before_handshake
2020-03-15 09:28:58.021 I [116.203.154.248:18089 OUT] [priority]Failed to HANDSHAKE with peer 116.203.154.248:18089
2020-03-15 09:28:58.022 I [116.203.154.248:18089 4c25734c-b5e5-4181-82e9-f610d221f36c OUT] CLOSE CONNECTION
2020-03-15 09:28:58.222 I [104.238.221.81:18089 72957ef4-5f2e-400b-b4bf-52b93fcfbb94 OUT] NEW CONNECTION
2020-03-15 09:28:58.444 I Failed to invoke command 1001 return code -3
2020-03-15 09:28:58.444 W [104.238.221.81:18089 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-03-15 09:28:58.444 I [104.238.221.81:18089 OUT] [0] state: closed in state before_handshake
2020-03-15 09:28:58.444 W [104.238.221.81:18089 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 09:28:58.444 I [104.238.221.81:18089 OUT] [priority]Failed to HANDSHAKE with peer 104.238.221.81:18089
2020-03-15 09:28:58.444 I [104.238.221.81:18089 72957ef4-5f2e-400b-b4bf-52b93fcfbb94 OUT] CLOSE CONNECTION
2020-03-15 09:28:58.678 I [63.34.74.228:18081 cbb958b8-1bfc-47e5-bffd-426b25b81d00 OUT] NEW CONNECTION
2020-03-15 09:28:58.910 I Failed to invoke command 1001 return code -3
2020-03-15 09:28:58.910 W [63.34.74.228:18081 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-03-15 09:28:58.910 I [63.34.74.228:18081 OUT] [0] state: closed in state before_handshake
2020-03-15 09:28:58.910 W [63.34.74.228:18081 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 09:28:58.910 I [63.34.74.228:18081 OUT] [priority]Failed to HANDSHAKE with peer 63.34.74.228:18081
2020-03-15 09:28:58.910 I [63.34.74.228:18081 cbb958b8-1bfc-47e5-bffd-426b25b81d00 OUT] CLOSE CONNECTION
2020-03-15 09:28:59.176 I [148.251.178.238:18081 5ee7948c-66e9-48e8-b007-ef969100d99a OUT] NEW CONNECTION
2020-03-15 09:28:59.445 I Failed to invoke command 1001 return code -3
2020-03-15 09:28:59.445 W [148.251.178.238:18081 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-03-15 09:28:59.445 I [148.251.178.238:18081 OUT] [0] state: closed in state before_handshake
2020-03-15 09:28:59.445 W [148.251.178.238:18081 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 09:28:59.445 I [148.251.178.238:18081 OUT] [priority]Failed to HANDSHAKE with peer 148.251.178.238:18081
2020-03-15 09:28:59.445 I [148.251.178.238:18081 5ee7948c-66e9-48e8-b007-ef969100d99a OUT] CLOSE CONNECTION
2020-03-15 09:28:59.727 I [195.201.100.183:18081 6c5c8250-05f4-447a-a92b-46add74beab2 OUT] NEW CONNECTION
2020-03-15 09:29:00.009 I Failed to invoke command 1001 return code -3
2020-03-15 09:29:00.009 W [195.201.100.183:18081 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-03-15 09:29:00.009 I [195.201.100.183:18081 OUT] [0] state: closed in state before_handshake
2020-03-15 09:29:00.009 W [195.201.100.183:18081 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 09:29:00.009 I [195.201.100.183:18081 OUT] [priority]Failed to HANDSHAKE with peer 195.201.100.183:18081
2020-03-15 09:29:00.009 I [195.201.100.183:18081 6c5c8250-05f4-447a-a92b-46add74beab2 OUT] CLOSE CONNECTION
2020-03-15 09:29:00.279 I [148.251.178.238:18081 13b02fe1-ed92-48f0-9fab-2468478b6efe OUT] NEW CONNECTION
2020-03-15 09:29:00.545 I Failed to invoke command 1001 return code -3
2020-03-15 09:29:00.545 W [148.251.178.238:18081 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2020-03-15 09:29:00.545 I [148.251.178.238:18081 OUT] [0] state: closed in state before_handshake
2020-03-15 09:29:00.545 W [148.251.178.238:18081 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 09:29:00.546 I [148.251.178.238:18081 OUT] [priority]Failed to HANDSHAKE with peer 148.251.178.238:18081
2020-03-15 09:29:00.546 I [148.251.178.238:18081 13b02fe1-ed92-48f0-9fab-2468478b6efe OUT] CLOSE CONNECTION
2020-03-15 09:29:00.807 I [116.202.103.24:18089 e46ebd03-6295-4a4e-a313-ee22098550b1 OUT] NEW CONNECTION
2020-03-15 09:29:05.807 I [116.202.103.24:18089 OUT] Timeout on invoke operation happened, command: 1001 timeout: 5000
2020-03-15 09:29:05.807 I Failed to invoke command 1001 return code -4
2020-03-15 09:29:05.807 W [116.202.103.24:18089 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2020-03-15 09:29:05.808 W [116.202.103.24:18089 OUT] COMMAND_HANDSHAKE Failed
2020-03-15 09:29:05.808 I [116.202.103.24:18089 OUT] [0] state: closed in state before_handshake
2020-03-15 09:29:05.808 I [116.202.103.24:18089 e46ebd03-6295-4a4e-a313-ee22098550b1 OUT] CLOSE CONNECTION
2020-03-15 09:29:05.808 I [116.202.103.24:18089 OUT] Failed to HANDSHAKE with peer 116.202.103.24:18089
2020-03-15 09:29:06.808 I Failed to connect to any, trying seeds
2020-03-15 09:29:07.112 I 0Connect failed to 195.154.123.123:18080
2020-03-15 09:29:12.112 I 0Connect failed to 198.74.231.92:18080
2020-03-15 09:29:17.113 I 0Connect failed to 212.83.172.165:18080
2020-03-15 09:29:22.113 I 0Connect failed to 212.83.175.67:18080
2020-03-15 09:29:22.417 I 0Connect failed to 5.9.100.248:18080
2020-03-15 09:29:27.417 I 0Connect failed to 107.152.130.98:18080
2020-03-15 09:29:32.418 I 0Connect failed to 161.67.132.39:18080

## xiphon | 2020-03-15T09:55:40+00:00
Please either use valid P2P priority nodes (not public RPC nodes) or drop all the `--add-priority-node` arguments.

## xcoin-dev | 2020-03-15T10:59:24+00:00
i try just start by :./monerod
but also can't sync
height is still in 1,

log:
set_log 4
Log level is now 4
2020-03-15 10:58:12.972 T Failed to connect to 192.110.160.146:18080, because of timeout (5000)
2020-03-15 10:58:12.973 T [sock -1] Socket destroyed without shutdown.
2020-03-15 10:58:12.973 T [sock -1] Socket destroyed
2020-03-15 10:58:12.973 T [<none> OUT] ~async_protocol_handler()
2020-03-15 10:58:12.973 D Destructing connection #1 to 0.0.0.0
2020-03-15 10:58:12.973 I 0Connect failed to 192.110.160.146:18080
2020-03-15 10:58:12.973 D Connecting to 195.154.123.123:18080(peer_type=1, last_seen: never)...
2020-03-15 10:58:12.973 D Spawned connection #2 to 0.0.0.0 currently we have sockets count:2
2020-03-15 10:58:12.974 D test, connection constructor set m_connection_type=2
2020-03-15 10:58:12.974 D connections_ size now 1
2020-03-15 10:58:12.974 D Trying to connect to 195.154.123.123:18080, bind_ip = 0.0.0.0
2020-03-15 10:58:13.262 T Some problems at connect, message: Connection refused
2020-03-15 10:58:13.262 T [sock -1] Socket destroyed without shutdown.
2020-03-15 10:58:13.262 T [sock -1] Socket destroyed
2020-03-15 10:58:13.262 T [<none> OUT] ~async_protocol_handler()
2020-03-15 10:58:13.262 D Destructing connection #2 to 0.0.0.0
2020-03-15 10:58:13.262 I 0Connect failed to 195.154.123.123:18080
2020-03-15 10:58:13.262 D Connecting to 198.74.231.92:18080(peer_type=1, last_seen: never)...
2020-03-15 10:58:13.262 D Spawned connection #3 to 0.0.0.0 currently we have sockets count:2
2020-03-15 10:58:13.262 D test, connection constructor set m_connection_type=2
2020-03-15 10:58:13.262 D connections_ size now 1
2020-03-15 10:58:13.262 D Trying to connect to 198.74.231.92:18080, bind_ip = 0.0.0.0
2020-03-15 10:58:18.263 T Failed to connect to 198.74.231.92:18080, because of timeout (5000)
2020-03-15 10:58:18.263 T [sock -1] Socket destroyed without shutdown.
2020-03-15 10:58:18.263 T [sock -1] Socket destroyed
2020-03-15 10:58:18.263 T [<none> OUT] ~async_protocol_handler()
2020-03-15 10:58:18.263 D Destructing connection #3 to 0.0.0.0
2020-03-15 10:58:18.263 I 0Connect failed to 198.74.231.92:18080
2020-03-15 10:58:18.263 D Connecting to 212.83.172.165:18080(peer_type=1, last_seen: never)...
2020-03-15 10:58:18.263 D Spawned connection #4 to 0.0.0.0 currently we have sockets count:2
2020-03-15 10:58:18.263 D test, connection constructor set m_connection_type=2
2020-03-15 10:58:18.263 D connections_ size now 1
2020-03-15 10:58:18.263 D Trying to connect to 212.83.172.165:18080, bind_ip = 0.0.0.0
2020-03-15 10:58:23.264 T Failed to connect to 212.83.172.165:18080, because of timeout (5000)
2020-03-15 10:58:23.266 T [sock -1] Socket destroyed without shutdown.
2020-03-15 10:58:23.266 T [sock -1] Socket destroyed
2020-03-15 10:58:23.266 T [<none> OUT] ~async_protocol_handler()

## xcoin-dev | 2020-03-15T11:04:51+00:00
Height: 1/1 (100.0%) on mainnet, not mining, net hash 0 H/s, v1, up to date, 0(out)+0(in) connections, uptime 0d 0h 6m 6s

I've been trying to solve this problem for two days, but I haven't made progress

## xiphon | 2020-03-15T11:31:12+00:00
`192.110.160.146:18080` node appears to be online, but according to the logs, your monerod instance failed to connect to it due to network connection timeout. 
At this point i would suggest to double check network connection status, firewall settings/rules, etc.

## xcoin-dev | 2020-03-15T12:28:07+00:00
thanks your help..I checked them many times
And the server orther port is normal,,,such as 80,20888,21888.
monero-wallet-rpc is work!  i can connect and get json rpc result..
so ,I don't know what to do. Is there any other way？

root@node-10:~# service iptables status
Unit iptables.service could not be found.
root@node-10:~# ufw status
Status: inactive
root@node-10:~# firewalld --states
Command 'firewalld' not found, but can be installed with:
apt install firewalld




## trasherdk | 2020-03-15T14:01:48+00:00
How about `iptables -L -nvx` ?

## xcoin-dev | 2020-03-15T14:27:27+00:00
Chain INPUT (policy ACCEPT 92245 packets, 253094734 bytes)
    pkts      bytes target     prot opt in     out     source               destination
 1630588 492312920 ufw-before-logging-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 1630588 492312920 ufw-before-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 1605598 478306693 ufw-after-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 1605592 478306381 ufw-after-logging-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 1605592 478306381 ufw-reject-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 1605592 478306381 ufw-track-input  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
    pkts      bytes target     prot opt in     out     source               destination
       0        0 ufw-before-logging-forward  all  --  *      *       0.0.0.0/0            0.0.0.0/0
       0        0 ufw-before-forward  all  --  *      *       0.0.0.0/0            0.0.0.0/0
       0        0 ufw-after-forward  all  --  *      *       0.0.0.0/0            0.0.0.0/0
       0        0 ufw-after-logging-forward  all  --  *      *       0.0.0.0/0            0.0.0.0/0
       0        0 ufw-reject-forward  all  --  *      *       0.0.0.0/0            0.0.0.0/0
       0        0 ufw-track-forward  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain OUTPUT (policy ACCEPT 71578 packets, 6593825 bytes)
    pkts      bytes target     prot opt in     out     source               destination
 1914665 325347649 ufw-before-logging-output  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 1914665 325347649 ufw-before-output  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 1888122 288996347 ufw-after-output  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 1888122 288996347 ufw-after-logging-output  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 1888122 288996347 ufw-reject-output  all  --  *      *       0.0.0.0/0            0.0.0.0/0
 1888122 288996347 ufw-track-output  all  --  *      *       0.0.0.0/0            0.0.0.0/0

Chain ufw-after-forward (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-after-input (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-after-logging-forward (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-after-logging-input (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-after-logging-output (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-after-output (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-before-forward (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-before-input (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-before-logging-forward (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-before-logging-input (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-before-logging-output (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-before-output (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-reject-forward (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-reject-input (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-reject-output (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-track-forward (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-track-input (1 references)
    pkts      bytes target     prot opt in     out     source               destination

Chain ufw-track-output (1 references)
    pkts      bytes target     prot opt in     out     source               destination

## xcoin-dev | 2020-03-15T14:28:30+00:00
> How about `iptables -L -nvx` ?

Is there any problem with the results above?

Maybe it's my service provider's problem, even if I open all security groups

## trasherdk | 2020-03-16T01:49:37+00:00
Looks okay to me.

You might want to take this to [monero.stackexchange.com](https://monero.stackexchange.com/questions/ask)

## selsta | 2022-03-16T15:51:24+00:00
Closing due to inactivity and no other reports of similar issues.

# Action History
- Created by: xcoin-dev | 2020-03-15T08:52:57+00:00
- Closed at: 2022-03-16T15:51:24+00:00
