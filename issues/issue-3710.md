---
title: ' Failed to deinitialize core'
source_url: https://github.com/monero-project/monero/issues/3710
author: EnricoSx
assignees: []
labels: []
created_at: '2018-04-26T13:31:02+00:00'
updated_at: '2018-04-26T13:37:15+00:00'
type: issue
status: closed
closed_at: '2018-04-26T13:37:14+00:00'
---

# Original Description
i run monerod for the first time ,on ubuntu server 16.04 vps (aruba).

```
2018-04-26 13:28:49.189     7fac2cc8a740        INFO    global  src/daemon/main.cpp:280 Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-04-26 13:28:49.190     7fac2cc8a740        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-04-26 13:28:49.191     7fac2cc8a740        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-04-26 13:28:49.191     7fac2cc8a740        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-04-26 13:28:49.446     7fac2cc8a740        INFO    global  src/daemon/core.h:103   Deinitializing core...
2018-04-26 13:28:49.452     7fac2cc8a740        ERROR   daemon  src/daemon/core.h:108   Failed to deinitialize core...
2018-04-26 13:28:49.452     7fac2cc8a740        INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2018-04-26 13:28:49.453     7fac2cc8a740        INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully
2018-04-26 13:28:49.453     7fac2cc8a740        ERROR   daemon  src/daemon/main.cpp:288 Exception in main! Failed to initialize p2p server
```

# Discussion History
## EnricoSx | 2018-04-26T13:37:14+00:00
solved:
No space left on device

# Action History
- Created by: EnricoSx | 2018-04-26T13:31:02+00:00
- Closed at: 2018-04-26T13:37:14+00:00
