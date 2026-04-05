---
title: 'FIXME: get_transaction_weight_limit for FCMP++'
source_url: https://github.com/seraphis-migration/monero/issues/171
author: bvcxza
assignees: []
labels: []
created_at: '2025-10-12T14:09:20+00:00'
updated_at: '2025-10-13T16:31:56+00:00'
type: issue
status: closed
closed_at: '2025-10-13T16:31:56+00:00'
---

# Original Description
I got this error always on monerod starting.

Start command:

`monerod --testnet --log-file output.log --no-zmq --out-peers 16 --in-peers 8 --log-level 0 --p2p-bind-ip 127.0.0.1 --rpc-bind-ip 127.0.0.1 --rpc-max-connections-per-private-ip 100 --rpc-max-connections 100 --disable-dns-checkpoints --check-updates disabled --rpc-restricted-bind-ip=127.0.0.1 --rpc-restricted-bind-port=28089 --no-igd --confirm-external-bind --max-connections-per-ip 10 --prune-blockchain`


```
2025-10-12 13:58:19.599	I Monero 'FCMP++ / Carrot alpha stressnet' (v0.19.0.0-alpha.1.1-f76c469de)
2025-10-12 13:58:19.599	I Initializing cryptonote protocol...
2025-10-12 13:58:19.599	I Cryptonote protocol initialized OK
2025-10-12 13:58:19.600	I Initializing core...
2025-10-12 13:58:19.600	I Loading blockchain from folder /home/usr/.bitmonero/testnet/lmdb ...
2025-10-12 13:58:19.688	I Loading checkpoints
2025-10-12 13:58:19.716	I Core initialized OK
2025-10-12 13:58:19.716	I Initializing p2p server...
2025-10-12 13:58:19.720	I p2p server initialized OK
2025-10-12 13:58:19.720	I Initializing core RPC server...
2025-10-12 13:58:19.720	I Binding on 127.0.0.1 (IPv4):28081
2025-10-12 13:58:19.727	I core RPC server initialized OK on port: 28081
2025-10-12 13:58:19.727	I Initializing restricted RPC server...
2025-10-12 13:58:19.727	I Binding on 127.0.0.1 (IPv4):28089
2025-10-12 13:58:19.867	I restricted RPC server initialized OK on port: 28089
2025-10-12 13:58:19.867	W WARN: --zmq-rpc-bind-port has no effect because --no-zmq was specified
2025-10-12 13:58:19.867	I Starting core RPC server...
2025-10-12 13:58:19.867	I core RPC server started ok
2025-10-12 13:58:19.867	I Starting restricted RPC server...
2025-10-12 13:58:19.868	I restricted RPC server started ok
2025-10-12 13:58:19.868	I Starting p2p net loop...
2025-10-12 13:58:20.868	I 
2025-10-12 13:58:20.869	I **********************************************************************
2025-10-12 13:58:20.869	I The daemon will start synchronizing with the network. This may take a long time to complete.
2025-10-12 13:58:20.869	I 
2025-10-12 13:58:20.869	I You can set the level of process detailization through "set_log <level|categories>" command,
2025-10-12 13:58:20.869	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2025-10-12 13:58:20.869	I 
2025-10-12 13:58:20.869	I Use the "help" command to see the list of available commands.
2025-10-12 13:58:20.869	I Use "help <command>" to see a command's documentation.
2025-10-12 13:58:20.869	I **********************************************************************
2025-10-12 13:58:21.378	I 
2025-10-12 13:58:21.378	I **********************************************************************
2025-10-12 13:58:21.378	I You are now synchronized with the network. You may now start monero-wallet-cli.
2025-10-12 13:58:21.378	I 
2025-10-12 13:58:21.378	I Use the "help" command to see the list of available commands.
2025-10-12 13:58:21.378	I **********************************************************************
2025-10-12 13:58:22.700	E FIXME: get_transaction_weight_limit for FCMP++
```


# Discussion History
## nahuhh | 2025-10-12T15:33:40+00:00
Known, and is on the TODOs

it happens when your node sees a transaction. It only prints once to avoid spam

# Action History
- Created by: bvcxza | 2025-10-12T14:09:20+00:00
- Closed at: 2025-10-13T16:31:56+00:00
