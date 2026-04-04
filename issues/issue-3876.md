---
title: 'W WARNING: no two valid DNS TXT records were received'
source_url: https://github.com/monero-project/monero-gui/issues/3876
author: filwu8
assignees: []
labels: []
created_at: '2022-04-02T02:29:59+00:00'
updated_at: '2023-01-17T05:01:17+00:00'
type: issue
status: closed
closed_at: '2023-01-17T05:01:16+00:00'
---

# Original Description
monerod.exe  --zmq-pub   tcp://127.0.0.1:18083 --disable-dns-checkpoints --enable-dns-blocklist
pause

how to set dns？


2022-04-02 02:24:13.029 I **********************************************************************
2022-04-02 02:24:15.662 W WARNING: no two valid DNS TXT records were received
2022-04-02 02:24:17.920 I [109.194.35.141:18080 OUT] Sync data returned a new top block candidate: 2592761 -> 2592764 [Your node is 3 blocks (6.0 minutes) behind]
2022-04-02 02:24:17.920 I SYNCHRONIZATION started
2022-04-02 02:24:20.702 I Synced 2592764/2592764
2022-04-02 02:24:20.703 I SYNCHRONIZED OK
2022-04-02 02:24:20.704 I
2022-04-02 02:24:20.704 I **********************************************************************
2022-04-02 02:24:20.704 I You are now synchronized with the network. You may now start monero-wallet-cli.
2022-04-02 02:24:20.704 I
2022-04-02 02:24:20.704 I Use the "help" command to see the list of available commands.
2022-04-02 02:24:20.705 I **********************************************************************
2022-04-02 02:24:41.419 W WARNING: no two valid DNS TXT records were received

# Discussion History
## selsta | 2022-04-06T02:28:00+00:00
Can you check https://monero.stackexchange.com/a/10227 ?

## selsta | 2023-01-17T05:01:16+00:00
Closing due to inactivity and no reply.

# Action History
- Created by: filwu8 | 2022-04-02T02:29:59+00:00
- Closed at: 2023-01-17T05:01:16+00:00
