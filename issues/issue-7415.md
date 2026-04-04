---
title: 'Problems syncing node '
source_url: https://github.com/monero-project/monero/issues/7415
author: TechyGuy17
assignees: []
labels: []
created_at: '2021-03-02T07:14:34+00:00'
updated_at: '2021-03-02T13:56:42+00:00'
type: issue
status: closed
closed_at: '2021-03-02T13:56:42+00:00'
---

# Original Description
2021-03-02 07:03:03.942 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1643    Synced 185097/2308022 (8%, 2122925 left)
2021-03-02 07:03:03.957 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1643    Synced 185102/2308022 (8%, 2122920 left)
2021-03-02 07:03:03.969 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1643    Synced 185107/2308022 (8%, 2122915 left)
2021-03-02 07:03:04.271 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1643    Synced 185112/2308022 (8%, 2122910 left)
2021-03-02 07:03:04.325 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped
2021-03-02 07:03:04.325     7f07c1ae2700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::system_error
2021-03-02 07:03:04.325     7f07c1ae2700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2021-03-02 07:03:04.326     7f07c1ae2700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x113) [0x55c525b00b8a]:__cxa_throw+0x113) [0x55c525b00b8a]
2021-03-02 07:03:04.326     7f07c1ae2700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2]  0xee) [0x55c525afd196]:_ZN6detail6expect6throw_ESt10error_codePKcS3_j+0xee) [0x55c525afd196]
2021-03-02 07:03:04.326     7f07c1ae2700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x96a) [0x55c52604024a]:_ZN10cryptonote3rpc9ZmqServer5serveEv+0x96a) [0x55c52604024a]
2021-03-02 07:03:04.326     7f07c1ae2700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0x1143b) [0x7f08ae0ba43b]:_64-linux-gnu/libboost_thread.so.1.71.0(+0x1143b) [0x7f08ae0ba43b]
2021-03-02 07:03:04.326     7f07c1ae2700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x9609) [0x7f08adcfe609]:_64-linux-gnu/libpthread.so.0(+0x9609) [0x7f08adcfe609]
2021-03-02 07:03:04.326     7f07c1ae2700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0x43) [0x7f08adc25293]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f08adc25293]
2021-03-02 07:03:04.326     7f07c1ae2700        INFO    stacktrace      src/common/stack_trace.cpp:172
2021-03-02 07:03:04.328 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:84     Stopping core RPC server...
2021-03-02 07:03:04.328 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:227       Node stopped.
2021-03-02 07:03:04.328 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2021-03-02 07:03:04.328 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2021-03-02 07:03:04.447 [SRV_MAIN]      INFO    global  src/daemon/core.h:94    Deinitializing core...
2021-03-02 07:03:47.523 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2021-03-02 07:03:47.523 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully

Trying to sync my node but after a few minutes it starts with this, then i can just restart it and it syncs a bit more but goes back to this after. How can i fix it?

# Discussion History
## selsta | 2021-03-02T07:38:03+00:00
Do you use systemd?

## TechyGuy17 | 2021-03-02T07:53:28+00:00
> Do you use systemd?

What?


## TechyGuy17 | 2021-03-02T09:45:02+00:00
> Do you use systemd?

Oh. yes i use systemd

## selsta | 2021-03-02T10:14:25+00:00
Could it be that systemd is exiting monerod for some reason? Your logs don't have anything interesting.

## TechyGuy17 | 2021-03-02T10:31:24+00:00
> Could it be that systemd is exiting monerod for some reason? Your logs don't have anything interesting.

Is there any way i can check? 

## TechyGuy17 | 2021-03-02T13:22:37+00:00
I changed to loglevel=1 and got this 
2021-03-02 13:20:58.678 [P2P9]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2319    [45.37.132.5:18080 OUT] [0] state: requesting objects in state synchronizing
2021-03-02 13:20:58.679 [P2P3]  INFO    net.p2p src/p2p/net_node.inl:2625       [54.39.75.67:18080 300fd470-1585-45be-abe7-c08a134e98ac OUT] NEW CONNECTION
2021-03-02 13:20:58.679 [P2P3]  INFO    net.p2p.traffic contrib/epee/include/storages/levin_abstract_invoke2.h:45       [54.39.75.67:18080 OUT] 262 bytes sent for category command-1001 initiated by us
2021-03-02 13:20:58.691     7fda3cc2b700        INFO    net     contrib/epee/include/storages/levin_abstract_invoke2.h:158      Failed to invoke command 1007 return code -3
2021-03-02 13:20:58.691     7fda3cc2b700        WARNING net.p2p src/p2p/net_node.inl:2404       [137.74.139.48:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2021-03-02 13:20:58.692     7fda3cc2b700        INFO    net     contrib/epee/include/storages/levin_abstract_invoke2.h:158      Failed to invoke command 1001 return code -3
2021-03-02 13:20:58.692     7fda3cc2b700        WARNING net.p2p src/p2p/net_node.inl:1111       [54.39.75.67:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2021-03-02 13:20:58.692 [P2P3]  WARNING net.p2p src/p2p/net_node.inl:1170       [54.39.75.67:18080 OUT] COMMAND_HANDSHAKE Failed
2021-03-02 13:20:58.692 [P2P3]  INFO    net.p2p src/p2p/net_node.inl:1362       [54.39.75.67:18080 OUT] Failed to HANDSHAKE with peer 54.39.75.67:18080
2021-03-02 13:20:58.693     7fda3cc2b700        INFO    net     contrib/epee/include/storages/levin_abstract_invoke2.h:158      Failed to invoke command 1007 return code -3
2021-03-02 13:20:58.693     7fda3cc2b700        WARNING net.p2p src/p2p/net_node.inl:2404       [161.35.39.92:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2021-03-02 13:20:58.693     7fda3cc2b700        INFO    net     contrib/epee/include/storages/levin_abstract_invoke2.h:158      Failed to invoke command 1007 return code -3
2021-03-02 13:20:58.693     7fda3cc2b700        WARNING net.p2p src/p2p/net_node.inl:2404       [104.248.125.247:53796 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2021-03-02 13:20:58.695 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:1014       net_service loop stopped.
2021-03-02 13:20:58.695 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped
2021-03-02 13:20:58.696     7fda36ffd700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::system_error
2021-03-02 13:20:58.696     7fda36ffd700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2021-03-02 13:20:58.697     7fda36ffd700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x113) [0x561eca08db8a]:__cxa_throw+0x113) [0x561eca08db8a]
2021-03-02 13:20:58.697     7fda36ffd700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2]  0xee) [0x561eca08a196]:_ZN6detail6expect6throw_ESt10error_codePKcS3_j+0xee) [0x561eca08a196]
2021-03-02 13:20:58.697     7fda36ffd700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x96a) [0x561eca5cd24a]:_ZN10cryptonote3rpc9ZmqServer5serveEv+0x96a) [0x561eca5cd24a]
2021-03-02 13:20:58.697     7fda36ffd700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0x1143b) [0x7fdb610f343b]:_64-linux-gnu/libboost_thread.so.1.71.0(+0x1143b) [0x7fdb610f343b]
2021-03-02 13:20:58.697     7fda36ffd700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x9609) [0x7fdb60d37609]:_64-linux-gnu/libpthread.so.0(+0x9609) [0x7fdb60d37609]
2021-03-02 13:20:58.697     7fda36ffd700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0x43) [0x7fdb60c5e293]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7fdb60c5e293]
2021-03-02 13:20:58.697     7fda36ffd700        INFO    stacktrace      src/common/stack_trace.cpp:172
2021-03-02 13:20:58.697 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:84     Stopping core RPC server...
2021-03-02 13:20:58.698 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:227       Node stopped.
2021-03-02 13:20:58.698 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2021-03-02 13:20:58.698 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2021-03-02 13:20:58.698 [SRV_MAIN]      INFO    net     src/p2p/net_node.h:428  Killing the net_node
2021-03-02 13:20:58.952 [SRV_MAIN]      INFO    net     src/p2p/net_node.h:432  Joined extra background net_node threads
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2895    Target height decreasing from 2308226 to 0
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [137.74.139.48:18080 OUT] [0] state: closed in state normal
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [137.74.139.48:18080 fa109cbb-7252-4ebf-91c8-ea4c2cdc91dc OUT] CLOSE CONNECTION
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [195.201.41.204:18080 OUT] [0] state: closed in state synchronizing
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [195.201.41.204:18080 9b0189de-e860-4b25-b59a-db5a8b112924 OUT] CLOSE CONNECTION
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [54.39.75.67:18080 OUT] [0] state: closed in state before_handshake
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [54.39.75.67:18080 300fd470-1585-45be-abe7-c08a134e98ac OUT] CLOSE CONNECTION
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [82.64.112.145:18080 OUT] [0] state: closed in state synchronizing
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [82.64.112.145:18080 42c71cbe-d32c-4fdb-bf10-2a9c98784995 OUT] CLOSE CONNECTION
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [161.35.39.92:18080 OUT] [0] state: closed in state synchronizing
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [161.35.39.92:18080 66649e83-e827-47a8-967b-2daaf1fbb0fc OUT] CLOSE CONNECTION
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [45.37.132.5:18080 OUT] [0] state: closed in state synchronizing
2021-03-02 13:20:58.961 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [45.37.132.5:18080 3738545a-f0b6-4112-acc4-aa66b645c4a1 OUT] CLOSE CONNECTION
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [172.119.144.53:18080 OUT] [185] state: closed in state synchronizing
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [172.119.144.53:18080 f32fe0be-c45b-4421-87bd-df9bb308e345 OUT] CLOSE CONNECTION
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [104.248.125.247:53796 INC] [0] state: closed in state normal
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [104.248.125.247:53796 59ece0d4-3b3c-4176-9729-f2009e9ef325 INC] CLOSE CONNECTION
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [204.27.62.98:18080 OUT] [0] state: closed in state synchronizing
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [204.27.62.98:18080 703befaa-9374-4957-8cae-e43f15db5898 OUT] CLOSE CONNECTION
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [135.181.202.85:18080 OUT] [0] state: closed in state synchronizing
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [135.181.202.85:18080 6b80fcea-bbe9-4533-ac1d-2598fb863065 OUT] CLOSE CONNECTION
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [138.68.41.79:18080 OUT] [0] state: closed in state synchronizing
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [138.68.41.79:18080 04eee99f-06dd-4927-a783-59137d2236e7 OUT] CLOSE CONNECTION
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [116.202.31.212:18080 OUT] [0] state: closed in state synchronizing
2021-03-02 13:20:58.962 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [116.202.31.212:18080 ca023e60-1d3a-4b71-a4c2-7136c1bc0273 OUT] CLOSE CONNECTION
2021-03-02 13:20:58.963 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [116.203.80.47:18080 OUT] [183] state: closed in state synchronizing
2021-03-02 13:20:58.963 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [116.203.80.47:18080 05a144ac-8d6b-48ca-8d01-02099b18b116 OUT] CLOSE CONNECTION
2021-03-02 13:20:58.963 [SRV_MAIN]      INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2905    [173.249.41.199:56200 INC] [0] state: closed in state synchronizing
2021-03-02 13:20:58.963 [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2641       [173.249.41.199:56200 9e5a67d3-da3b-4984-bf4d-703af02bd210 INC] CLOSE CONNECTION
2021-03-02 13:20:58.963 [SRV_MAIN]      INFO    global  src/daemon/core.h:94    Deinitializing core...
2021-03-02 13:21:38.273 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2021-03-02 13:21:38.273 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully


## TechyGuy17 | 2021-03-02T13:56:42+00:00
Ok i think i have fixed it, when i start it manually it works fine, so i will just stop using the systemd 

# Action History
- Created by: TechyGuy17 | 2021-03-02T07:14:34+00:00
- Closed at: 2021-03-02T13:56:42+00:00
