---
title: Core dump during sync
source_url: https://github.com/monero-project/monero/issues/8621
author: gus4rs
assignees: []
labels: []
created_at: '2022-10-23T10:47:46+00:00'
updated_at: '2022-10-24T18:20:22+00:00'
type: issue
status: closed
closed_at: '2022-10-24T18:20:22+00:00'
---

# Original Description
```Monero 'Fluorine Fermi' (v0.18.1.2-release)```

When running Monero, it just prints the following lines in a loop and doesn't sync:

```
2022-10-23 10:44:22.802 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2022-10-23 10:44:22.803 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    **********************************************************************
2022-10-23 10:44:22.803 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    The daemon will start synchronizing with the network. This may take a long time to complete.
2022-10-23 10:44:22.804 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2022-10-23 10:44:22.804 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    You can set the level of process detailization through "set_log <level|categories>" command,
2022-10-23 10:44:22.804 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2022-10-23 10:44:22.804 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808
2022-10-23 10:44:22.804 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    Use the "help" command to see the list of available commands.
2022-10-23 10:44:22.804 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    Use "help <command>" to see a command's documentation.
2022-10-23 10:44:22.804 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1808    **********************************************************************
2022-10-23 10:44:27.860 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     [185.99.254.10:18080 OUT] Sync data returned a new top block candidate: 2739670 -> 2739704 [Your node is 34 blocks (1.1 hours) behind] 
2022-10-23 10:44:27.861 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     SYNCHRONIZATION started
2022-10-23 10:44:30.883     7fc45ae05ac0        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-10-23 10:44:30.883     7fc45ae05ac0        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2022-10-23 10:44:30.884     7fc45ae05ac0        INFO    global  src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.1.2-release)
2022-10-23 10:44:30.885     7fc45ae05ac0        INFO    msgwriter       src/common/scoped_message_writer.h:102  Forking to background...
2022-10-23 10:44:30.900     7fc45ae05ac0        WARNING daemon  src/daemon/executor.cpp:61      Monero 'Fluorine Fermi' (v0.18.1.2-release) Daemonised
2022-10-23 10:44:30.900     7fc45ae05ac0        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2022-10-23 10:44:30.900     7fc45ae05ac0        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2022-10-23 10:44:30.902     7fc45ae05ac0        INFO    global  src/daemon/core.h:64    Initializing core...
2022-10-23 10:44:30.904     7fc45ae05ac0        INFO    global  src/cryptonote_core/cryptonote_core.cpp:523     Loading blockchain from folder /home/data/monero/.monero/lmdb ... 
2022-10-23 10:44:31.251     7fc45ae05ac0        INFO    global  src/cryptonote_core/cryptonote_core.cpp:698     Loading checkpoints
2022-10-23 10:44:31.252     7fc45ae05ac0        INFO    global  src/daemon/core.h:81    Core initialized OK
2022-10-23 10:44:31.252     7fc45ae05ac0        INFO    global  src/daemon/p2p.h:64     Initializing p2p server...
2022-10-23 10:44:31.267     7fc45ae05ac0        INFO    global  src/daemon/p2p.h:69     p2p server initialized OK
2022-10-23 10:44:31.268     7fc45ae05ac0        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2022-10-23 10:44:31.268     7fc45ae05ac0        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 0.0.0.0 (IPv4):18081
2022-10-23 10:44:31.313     7fc45ae05ac0        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2022-10-23 10:44:31.314     7fc45ae05ac0        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2022-10-23 10:44:31.315 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2022-10-23 10:44:31.315 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:79     Starting p2p net loop...

``` 

And it keeps printing those lines over and over, no ERROR in the logs, without even start to sync. Where should I look to troubleshoot it?


# Discussion History
## gus4rs | 2022-10-23T12:10:48+00:00
Upon closer Inspection, there is no "loop", the issue is a core dump and systemd trying to restart it. The dump was on

```
#0  0x0000563af892c288 in randomx_blake2b_init ()
[Current thread is 1 (Thread 0x7f3b59cfd640 (LWP 6437))]
```

I am using a Virtual Machine running Fedora Linux inside a Parallels Desktop MacOS 

## selsta | 2022-10-24T14:58:22+00:00
How much RAM does your system have? Try starting monerod with this env var: `MONERO_RANDOMX_UMASK=8 ./monerod`

## gus4rs | 2022-10-24T18:20:22+00:00
The problem was a kernel update: After I wiped the source code, checked it out again and recompiled, it's working again

# Action History
- Created by: gus4rs | 2022-10-23T10:47:46+00:00
- Closed at: 2022-10-24T18:20:22+00:00
