---
title: 'Build warning: rpc_commands may be used uninitialised in this function'
source_url: https://github.com/monero-project/monero/issues/1594
author: ghost
assignees: []
labels: []
created_at: '2017-01-19T22:53:09+00:00'
updated_at: '2017-02-24T06:06:36+00:00'
type: issue
status: closed
closed_at: '2017-02-24T06:06:36+00:00'
---

# Original Description
```
[ 90%] Linking CXX executable ../../bin/monerod
/home/nodey/monero/src/daemon/daemon.cpp: In member function ‘run’:
/home/nodey/monero/src/daemon/daemon.cpp:138:36: warning: ‘rpc_commands’ may be used uninitialized in this function [-Wmaybe-uninitialized]
       rpc_commands->stop_handling();
                                    ^
/home/nodey/monero/src/daemon/daemon.cpp:126:34: note: ‘rpc_commands’ was declared here
     daemonize::t_command_server* rpc_commands;
```

Ubuntu 16.04, ARMv8

# Discussion History
## moneromooo-monero | 2017-01-20T19:00:13+00:00
False positive. You could initialize rpc_commands to NULL at declaration time, that should shut it up I think.

# Action History
- Created by: ghost | 2017-01-19T22:53:09+00:00
- Closed at: 2017-02-24T06:06:36+00:00
