---
title: monerod log location confusion
source_url: https://github.com/monero-project/monero/issues/6326
author: anonproject
assignees: []
labels: []
created_at: '2020-02-09T03:15:45+00:00'
updated_at: '2020-02-09T03:56:58+00:00'
type: issue
status: closed
closed_at: '2020-02-09T03:56:58+00:00'
---

# Original Description
Recently restarted monerod daemon which previously ran in pruned mode.

Now I see this in the bitmonero.log:

```text
 2020-02-05 02:18:28.791 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656
2020-02-05 02:18:28.792 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    **********************************************************************
2020-02-05 02:18:28.793 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    The daemon will start synchronizing with the network. This may take a long time to complete.
2020-02-05 02:18:28.794 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656
2020-02-05 02:18:28.794 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    You can set the level of process detailization through "set_log <level|categories>" command,
2020-02-05 02:18:28.794 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-02-05 02:18:28.795 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656
2020-02-05 02:18:28.795 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    Use the "help" command to see the list of available commands.
[detached (from session notes)]                                                                       [root@serv ~]# cat /tmp/monero.txt
2020-02-05 02:18:28.791 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656
2020-02-05 02:18:28.792 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    **********************************************************************                                      2020-02-05 02:18:28.793 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    The daemon will start synchronizing with the network. This may take a long time to complete.
2020-02-05 02:18:28.794 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656          2020-02-05 02:18:28.794 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    You can set the level of process detailization through "set_log <level|categories>" command,                2020-02-05 02:18:28.794 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-02-05 02:18:28.795 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656          2020-02-05 02:18:28.795 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    Use the "help" command to see the list of available commands.
2020-02-05 02:18:28.796 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    Use "help <command>" to see a command's documentation.
2020-02-05 02:18:28.796 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1656    **********************************************************************                                      2020-02-05 02:18:28.951 [P2P2]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1745    Version 0.15.0.1 of monero for source is available: https://downloads.getmonero.org/source/monero-source-v0.15.0.1.tar.bz2, SHA256 hash 083a3862f554a2e5157686d7a8075557dfd6f07de08069cac91017c17739750b
2020-02-05 02:18:38.829 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped  2020-02-05 02:18:38.901     7f4bc5de9700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: std::system_error                                                                        2020-02-05 02:18:38.901     7f4bc5de9700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2020-02-05 02:18:38.913     7f4bc5de9700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1]  0x10d) [0x55a3cf35c4ed]:__cxa_throw+0x10d) [0x55a3cf35c4ed]                                2020-02-05 02:18:38.913     7f4bc5de9700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2]  0x555) [0x55a3cf4d8c25]:_ZN6detail6expect6throw_ESt10error_codePKcS3_j+0x555) [0x55a3cf4d8c25]                                                                                                   2020-02-05 02:18:38.913     7f4bc5de9700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3]  0x276) [0x55a3cf39d866]:_ZN10cryptonote3rpc9ZmqServer5serveEv+0x276) [0x55a3cf39d866]
2020-02-05 02:18:38.913     7f4bc5de9700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4]  0x11bcd) [0x7f4c2c3f6bcd]:_64-linux-gnu/libboost_thread.so.1.65.1(+0x11bcd) [0x7f4c2c3f6bcd]
2020-02-05 02:18:38.913     7f4bc5de9700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5]  0x76db) [0x7f4c2b88e6db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7f4c2b88e6db]
2020-02-05 02:18:38.913     7f4bc5de9700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6]  0x3f) [0x7f4c2b5b788f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f4c2b5b788f]
2020-02-05 02:18:38.913     7f4bc5de9700        INFO    stacktrace      src/common/stack_trace.cpp:1722020-02-05 02:18:38.918 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:83     Stopping core RPC server...
2020-02-05 02:18:38.918 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:216       Node stopped.
2020-02-05 02:18:38.918 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:95     Deinitializing core RPC server...
2020-02-05 02:18:38.918 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2020-02-05 02:18:38.919 [SRV_MAIN]      INFO    global  src/daemon/core.h:94    Deinitializing core...
```

Any ideas?

# Discussion History
## moneromooo-monero | 2020-02-09T03:31:29+00:00
Do you have a process listening on 18082 ?

## anonproject | 2020-02-09T03:50:37+00:00
Woops.  Actually everything was working properly.  The log I provided was the old one, left from the /root/.bitmonero/ dir, when I was starting monerod manually. Then I created a new user monero and setted up systemd service and I forgot that now it will write the file into the home directory of the user monero!

I will drop the systemd config in case someone will face similar confusion.

* The following configure to be used via tor hidden service.

```text
[Unit]
Description=monerod
After=network.target

[Service]
Type=forking
PIDFile=/run/monero/monerod.pid
StandardOutput=journal

#iptables -I OUTPUT -p tcp -d 127.0.0.1 --dport 18081 -j ACCEPT

ExecStart=/usr/bin/torsocks -P 9050 /opt/monero/monero-x86_64-linux-gnu-v0.15.0.1/monerod \
 --prune-blockchain \
 --p2p-bind-ip 127.0.0.1 \
 --p2p-bind-port 18080 \
 --rpc-bind-ip 127.0.0.1 \
 --rpc-bind-port 18081 \
 --no-igd \
 --public-node \
 --restricted-rpc \
 --detach \
 --pidfile /run/monero/monerod.pid \
 --max-log-file-size 100000 \
 --max-log-files 1 \
 --log-level 1 \
 --log-file /var/log/monero/bitmonero.log

User=monero
Group=monero

# /run/monero
RuntimeDirectory=monero
RuntimeDirectoryMode=0710

Restart=on-failure

[Install]
WantedBy=multi-user.target
```

And the environment variables for daemon:

```text 
DNS_PUBLIC=tcp
TORSOCKS_ALLOW_INBOUND=1
```

# Action History
- Created by: anonproject | 2020-02-09T03:15:45+00:00
- Closed at: 2020-02-09T03:56:58+00:00
