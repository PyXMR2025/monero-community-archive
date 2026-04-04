---
title: monerod segmentation fault
source_url: https://github.com/monero-project/monero/issues/8915
author: Systemmanic
assignees: []
labels: []
created_at: '2023-06-22T20:57:21+00:00'
updated_at: '2023-06-24T17:24:13+00:00'
type: issue
status: closed
closed_at: '2023-06-24T17:24:13+00:00'
---

# Original Description
Happens consistently when running.

## Error

```
[1]    22312 segmentation fault  /opt/homebrew/opt/monero/bin/monerod
```

## Full log

```
$ /opt/homebrew/opt/monero/bin/monerod                    
2023-06-22 20:55:46.466	I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-06-22 20:55:46.466	I Initializing cryptonote protocol...
2023-06-22 20:55:46.466	I Cryptonote protocol initialized OK
2023-06-22 20:55:46.466	I Initializing core...
2023-06-22 20:55:46.466	I Loading blockchain from folder /Users/davidkane/.bitmonero/lmdb ...
2023-06-22 20:55:46.489	I Loading checkpoints
2023-06-22 20:55:46.489	I Core initialized OK
2023-06-22 20:55:46.489	I Initializing p2p server...
2023-06-22 20:55:46.492	I p2p server initialized OK
2023-06-22 20:55:46.492	I Initializing core RPC server...
2023-06-22 20:55:46.492	I Binding on 127.0.0.1 (IPv4):18081
2023-06-22 20:55:46.495	I core RPC server initialized OK on port: 18081
2023-06-22 20:55:46.496	I Starting core RPC server...
2023-06-22 20:55:46.496	I core RPC server started ok
2023-06-22 20:55:46.496	I Starting p2p net loop...
2023-06-22 20:55:47.497	I 
2023-06-22 20:55:47.498	I **********************************************************************
2023-06-22 20:55:47.498	I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-06-22 20:55:47.498	I 
2023-06-22 20:55:47.498	I You can set the level of process detailization through "set_log <level|categories>" command,
2023-06-22 20:55:47.498	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-06-22 20:55:47.498	I 
2023-06-22 20:55:47.498	I Use the "help" command to see the list of available commands.
2023-06-22 20:55:47.498	I Use "help <command>" to see a command's documentation.
2023-06-22 20:55:47.498	I **********************************************************************
2023-06-22 20:55:48.070	I [66.220.106.111:18080 OUT] Sync data returned a new top block candidate: 2913948 -> 2913960 [Your node is 12 blocks (24.0 minutes) behind] 
2023-06-22 20:55:48.070	I SYNCHRONIZATION started
2023-06-22 20:55:50.010	W monerod is now disconnected from the network
2023-06-22 20:55:50.347	I [199.116.84.87:18085 OUT] Sync data returned a new top block candidate: 2913950 -> 2913960 [Your node is 10 blocks (20.0 minutes) behind] 
2023-06-22 20:55:50.347	I SYNCHRONIZATION started
[1]    22312 segmentation fault  /opt/homebrew/opt/monero/bin/monerod
```

## Versions

### monerod
```
$ monerod --version
Monero 'Fluorine Fermi' (v0.18.2.2-release)
```

### OS
```
Darwin 22.5.0 arm64
```

Ideas?


# Discussion History
## selsta | 2023-06-24T17:24:12+00:00
Please see this issue: https://github.com/monero-project/monero/issues/8829

# Action History
- Created by: Systemmanic | 2023-06-22T20:57:21+00:00
- Closed at: 2023-06-24T17:24:13+00:00
