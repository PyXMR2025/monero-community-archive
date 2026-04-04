---
title: monerod exceptions with background mining. - kills daemon
source_url: https://github.com/monero-project/monero/issues/6658
author: ronohara
assignees: []
labels: []
created_at: '2020-06-15T09:13:31+00:00'
updated_at: '2022-02-19T04:37:31+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:37:31+00:00'
---

# Original Description
Environment: 

Arch Linux
Monero 'Nitrogen Nebula' (v0.16.0.0-release)

monerod run as root at a command prompt operates correctly and enables background mining with the following entries in monerod.conf

bg-mining-enable=1
bg-mining-ignore-battery=1
bg-mining-miner-target=65
mining-threads=8

start-mining=47KpiyHgdgdgdggdXo8H6CYxmS8iNEU6JLsNCTqZD9pSc9BZg8NFShH4NeW259D64MzcGWtFp3WbKxd7887

^^^^^ this is a fake address - I use a correct address in the config file.



When run from monerod.service (ether as Type=simple or Type=forking) and with this command:
ExecStart=/usr/bin/monerod --config-file /etc/monerod.conf \
    --non-interactive  --pidfile /run/monero/monerod.pid

The daemon hits a stack trace.  If I comment out the start-mining command the daemon runs correctly - obviously without mining.

2020-06-15 09:08:49.000 [miner 6]       INFO    global  src/cryptonote_basic/miner.cpp:546      background mining is enabled, but not started, waiting un
til start triggers
2020-06-15 09:08:49.000 [miner 3]       INFO    global  src/cryptonote_basic/miner.cpp:546      background mining is enabled, but not started, waiting un
til start triggers
2020-06-15 09:08:58.600 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2020-06-15 09:08:58.600 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-06-15 09:08:58.604 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x119) [0x56079db4f44c]:__cxa_throw+0x119) [0x56
079db4f44c]
2020-06-15 09:08:58.605 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x37215e) [0x56079db9415e] 
2020-06-15 09:08:58.605 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x198) [0x56079e21aca8]:_alloc_cache+0x198) [0x5
6079e21aca8]
2020-06-15 09:08:58.605 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0x2ac) [0x56079e03e34c]:_slow_hash+0x2ac) [0x560
79e03e34c]
2020-06-15 09:08:58.605 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0xb9) [0x56079e0271c9]:_ZN10cryptonote18get_bloc
k_longhashEPKNS_10BlockchainERKNS_5blockERN6crypto4hashEmi+0xb9) [0x56079e0271c9]
2020-06-15 09:08:58.605 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0x913) [0x56079e1bd993]:_ZN10cryptonote5miner13w
orker_threadEv+0x913) [0x56079e1bd993]
2020-06-15 09:08:58.605 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [7]  0x11857) [0x7fa2fa4ec857]:_thread.so.1.72.0(+0x1
1857) [0x7fa2fa4ec857]
2020-06-15 09:08:58.605 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /usr/lib/libpthread.so.0(+0x9422) [0x7fa2f9e17422
] 
2020-06-15 09:08:58.605 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [9] /usr/lib/libc.so.6(clone+0x43) [0x7fa2f9d46bf3] 
2020-06-15 09:08:58.605 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172
2020-06-15 09:08:58.994 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::runtime_error
2020-06-15 09:08:58.994 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-06-15 09:08:58.995 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x119) [0x56079db4f44c]:__cxa_throw+0x119) [0x56
079db4f44c]
2020-06-15 09:08:58.995 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/bin/monerod(+0x37215e) [0x56079db9415e] 
2020-06-15 09:08:58.995 [miner 7]       INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x3a) [0x56079e21adea]:_alloc_dataset+0x3a) [0x5
6079e21adea]


<cut>  lots more - 1 per mining thread

2020-06-15 09:09:08.788     7f8b470fc700        INFO    stacktrace      src/common/stack_trace.cpp:172      [12] /usr/lib/libc.so.6(clone+0x43) [0x7fa2f9
d46bf3] 
2020-06-15 09:09:08.788     7f8b470fc700        INFO    stacktrace      src/common/stack_trace.cpp:172
2020-06-15 09:09:29.426 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped
2020-06-15 09:09:29.427     7f8b81917700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::system_error
2020-06-15 09:09:29.427     7f8b81917700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-06-15 09:09:29.430     7f8b81917700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x119) [0x56079db4f44c]:__cxa_throw+0x11
9) [0x56079db4f44c]
2020-06-15 09:09:29.430     7f8b81917700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2]  0xf4) [0x56079db93c92]:_ZN6detail6expect
6throw_ESt10error_codePKcS3_j+0xf4) [0x56079db93c92]
2020-06-15 09:09:29.430     7f8b81917700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x551) [0x56079e0d0ca1]:_ZN10cryptonote3
rpc9ZmqServer5serveEv+0x551) [0x56079e0d0ca1]
2020-06-15 09:09:29.430     7f8b81917700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0x11857) [0x7fa2fa4ec857]:_thread.so.1.7
2.0(+0x11857) [0x7fa2fa4ec857]
2020-06-15 09:09:29.430     7f8b81917700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /usr/lib/libpthread.so.0(+0x9422) [0x7fa2
f9e17422] 
2020-06-15 09:09:29.430     7f8b81917700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /usr/lib/libc.so.6(clone+0x43) [0x7fa2f9d
46bf3] 
2020-06-15 09:09:29.430     7f8b81917700        INFO    stacktrace      src/common/stack_trace.cpp:172
2020-06-15 09:09:29.430 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:84     Stopping core RPC server...
2020-06-15 09:09:29.431 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:217       Node stopped.
2020-06-15 09:09:29.701 [miner 3]       INFO    global  src/cryptonote_basic/miner.cpp:598      Miner thread stopped [3]
2020-06-15 09:09:29.701 [miner 7]       INFO    global  src/cryptonote_basic/miner.cpp:598      Miner thread stopped [7]
2020-06-15 09:09:29.731 [miner 6]       INFO    global  src/cryptonote_basic/miner.cpp:598      Miner thread stopped [6]
2020-06-15 09:09:29.731 [miner 4]       INFO    global  src/cryptonote_basic/miner.cpp:598      Miner thread stopped [4]
2020-06-15 09:09:29.732 [miner 2]       INFO    global  src/cryptonote_basic/miner.cpp:598      Miner thread stopped [2]
2020-06-15 09:09:29.732 [miner 1]       INFO    global  src/cryptonote_basic/miner.cpp:598      Miner thread stopped [1]
2020-06-15 09:09:29.732 [miner 5]       INFO    global  src/cryptonote_basic/miner.cpp:598      Miner thread stopped [5]
2020-06-15 09:09:29.732 [miner 0]       INFO    global  src/cryptonote_basic/miner.cpp:598      Miner thread stopped [0]
2020-06-15 09:09:29.944 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2020-06-15 09:09:29.944 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2020-06-15 09:09:29.948 [SRV_MAIN]      INFO    global  src/daemon/core.h:94    Deinitializing core...
2020-06-15 09:09:30.236 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2020-06-15 09:09:30.236 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully


At this point the daemon has shut down.









# Discussion History
## moneromooo-monero | 2020-10-15T22:41:54+00:00
Does this case work with 0.17.1.0 ? The thread pool code was armoured against exceptions.

# Action History
- Created by: ronohara | 2020-06-15T09:13:31+00:00
- Closed at: 2022-02-19T04:37:31+00:00
