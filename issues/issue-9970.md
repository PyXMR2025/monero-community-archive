---
title: Daemon logs deep alternative chains (>60k blocks) on fully synced node
source_url: https://github.com/monero-project/monero/issues/9970
author: Rav3nPL
assignees: []
labels: []
created_at: '2025-06-25T11:35:16+00:00'
updated_at: '2025-08-14T18:41:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Running a fully synced node and observed strange behavior.

At current block height 3,441,665, the daemon log shows lines such as:
```
BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3379202
BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3415868
```
This suggests the node is considering alternative chains that would require a reorg of 62,000 or 25,000 blocks.

Such deep reorganizations should never be possible or even considered by the software. This may indicate an issue with unsynced or misconfigured mining.



# Discussion History
## nahuhh | 2025-06-25T12:42:39+00:00
Share the actual output please (+ maybe 50 lines before and after)

## Rav3nPL | 2025-06-25T12:50:02+00:00
Sure, there is part of the log.

```
2025-06-25 08:46:17.142 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2409    Synced 335 blocks in 14.9 minutes (0.374 blocks per second)
2025-06-25 08:46:17.142 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2413
2025-06-25 08:46:17.142 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2413    **********************************************************************
2025-06-25 08:46:17.142 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2413    You are now synchronized with the network. You may now start monero-wallet-cli.
2025-06-25 08:46:17.142 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2413
2025-06-25 08:46:17.142 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2413    Use the "help" command to see the list of available commands.
2025-06-25 08:46:17.142 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2413    **********************************************************************
2025-06-25 08:50:05.599 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:501     [45.84.107.76:12834 INC] Sync data returned a new top block candidate: 3441590 -> 3441591 [Your node is 1 blocks (2.0 minutes) behind]
2025-06-25 08:50:05.599 [P2P0]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:501     SYNCHRONIZATION started
2025-06-25 09:10:57.104 [RPC0]  WARNING miner   src/cryptonote_basic/miner.cpp:415      Background mining controller thread started
2025-06-25 09:10:57.105 [miner 0]       INFO    global  src/cryptonote_basic/miner.cpp:529      Miner thread was started [0]
2025-06-25 09:10:57.505 [miner 0]       INFO    global  src/cryptonote_basic/miner.cpp:549      background mining is enabled, but not started, waiting until start triggers
2025-06-25 09:11:07.103     75f4d2bfb6c0        ERROR   miner   src/cryptonote_basic/miner.cpp:1073     couldn't query power status from /sys/class/power_supply
2025-06-25 09:25:59.747 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3379202
2025-06-25 09:25:59.747 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <02951088f9248bc2f4f9359d7445ac1b890f76baf21fc5904ccd524b65b9a1dd>
2025-06-25 09:25:59.747 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <1772882c65be69dafad7ad09bda1a24d29307d6fed967474f2169c0100000000>
2025-06-25 09:25:59.747 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     551735318570
2025-06-25 10:18:42.738 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3415868
2025-06-25 10:18:42.739 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <626fe3afc6015981cc83ea38ec91de5f3c72dd9b4ad74f1528cc56ed6b33e74e>
2025-06-25 10:18:42.739 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <70eb5bb1c7ffd638544504ae3c47231828406319d5d331da2df13e0000000000>
2025-06-25 10:18:42.739 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     628588039363
2025-06-25 11:15:27.535     7b237b189340        INFO    logging contrib/epee/src/mlog.cpp:274   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2025-06-25 11:15:27.535     7b237b189340        INFO    logging contrib/epee/src/mlog.cpp:274   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:ERROR,logging:INFO,msgwriter:INFO
2025-06-25 11:15:27.535     7b237b189340        INFO    global  src/daemon/main.cpp:309 Monero 'Fluorine Fermi' (v0.18.4.0-release)
2025-06-25 11:15:28.688     7b237b189340        INFO    msgwriter       src/common/scoped_message_writer.h:102  Height: 3441665, target: 3441665 (100%)
2025-06-25 11:15:28.688     7b237b189340        INFO    msgwriter       src/common/scoped_message_writer.h:102  Downloading at 2 kB/s
2025-06-25 11:15:28.688     7b237b189340        INFO    msgwriter       src/common/scoped_message_writer.h:102  120 peers
```

## Rav3nPL | 2025-06-26T18:17:03+00:00
Similar thing today, over 25k blocks deep "alternative".
edit: It is the same as reported earlier.  Maybe some kind of attack to stress nodes?
When this happens I/O is crazy.

```
 monerod sync_info
2025-06-26 18:13:16.679 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Height: 3442626, target: 3442626 (100%)
Downloading at 3 kB/s
129 peers

2025-06-26 16:40:26.349 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3415868
2025-06-26 16:40:26.350 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <626fe3afc6015981cc83ea38ec91de5f3c72dd9b4ad74f1528cc56ed6b33e74e>
2025-06-26 16:40:26.350 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <70eb5bb1c7ffd638544504ae3c47231828406319d5d331da2df13e0000000000>
2025-06-26 16:40:26.350 [P2P0]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     628588039363
```


## Rav3nPL | 2025-08-04T17:26:12+00:00
Another one “alternative hit” today, over 60k old (3404856).

```
2025-08-04 07:28:14.334 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3404856
2025-08-04 07:28:14.334 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <d95f9da99678dae788a6c5825f03c1adea28b3eb8f2ea018fee1e61468e34ca0>
2025-08-04 07:28:14.334 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <76e32e1c0196b3d0ee045f8e85caa7c53fbe591192253d35ab258b0100000000>
2025-08-04 07:28:14.334 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     539936500949
```
```
 monerod sync_info
2025-08-04 17:22:29.201 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Height: 3470636, target: 3470636 (100%)
```


## Rav3nPL | 2025-08-10T16:56:16+00:00
Height over 3474672
3415868 -> over 58k old, was seen earlier. Why it is an "alternative" again? :/
3474903 -> over 200 blocks, lil bit to far, was even valid reorg that like, ever on running network?


```
2025-08-10 06:50:18.763 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1617    Synced 3474672/3474672
2025-08-10 07:34:44.911 [P2P3]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3415868
2025-08-10 07:34:44.913 [P2P3]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <626fe3afc6015981cc83ea38ec91de5f3c72dd9b4ad74f1528cc56ed6b33e74e>
2025-08-10 07:34:44.913 [P2P3]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <70eb5bb1c7ffd638544504ae3c47231828406319d5d331da2df13e0000000000>
2025-08-10 07:34:44.913 [P2P3]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     628588039363
2025-08-10 15:45:01.829 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3474903
2025-08-10 15:45:01.831 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <b4e13030f2fefd7845075f99e98fd6f18c49a74982415a1b03876ae704ef9cac>
2025-08-10 15:45:01.831 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <d4df31e67a3825d2b7397ef713caab912fcbb424d362ddd931a7ce0000000000>
2025-08-10 15:45:01.831 [P2P1]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     733218766365
```

My idea of fixing it: disallow any alternate chain older than 100 blocks and ignore communication from node that send it, disconnect and ban 48h+ when got to the connection limit.
But just in case allow some --allow-old-alternatives [numblocks] switch/config parameter?


## jeffro256 | 2025-08-10T22:11:42+00:00
> My idea of fixing it: disallow any alternate chain older than 100 blocks and ignore communication from node that send it, disconnect and ban 48h+ when got to the connection limit.

This is a bad idea because it will cause irreversible network splits. The node needs to be able to handle reorgs, no matter how deep, as long as it is a valid re-org with a greater cumulative PoW than your current main chain. These alt chains in your logs do not have a cumulative PoW greater than your main chain, because the node isn't switching to them, but simply adding them as alternatives. 

## jeffro256 | 2025-08-10T22:18:52+00:00
Thank you for reporting this issue, by the way. This problem with the node has been known for a while, but the path for fixing it in a concise manner is unclear. It's sad that it seems to have been figured out how to be exploited now. Do you use Matrix or IRC or PGP? I'd like to see the results of running your daemon with `--log-level 2`, but it's usually a bad idea to post those logs publicly & unencrypted because it contains IP information, which can be used to tie your GH persona to your real IP address.

## nahuhh | 2025-08-10T23:21:06+00:00
> The node needs to be able to handle reorgs, no matter how deep, as long as it is a valid re-org with a greater cumulative PoW than your current main chain.

don't we effectively ban reorgs deeper than the latest checkpoint?
doesnt make sense that we'd be accepting alt chains from below our checkpoint

note for debugging: Looks like theyre running 18.4.0 which has checkpoint of 337XXXX, and all of the alt chains are after that height
i wonder what would happen if they were running checkpoints from 18.4.1?

## jeffro256 | 2025-08-14T18:41:48+00:00
> don't we effectively ban reorgs deeper than the latest checkpoint?
> doesnt make sense that we'd be accepting alt chains from below our checkpoint

Yes, this is true. I should have been more clear. The node needs to be able to handle reorgs of depth up to the latest checkpoint.

> note for debugging: Looks like theyre running 18.4.0 which has checkpoint of 337XXXX, and all of the alt chains are after that height
> i wonder what would happen if they were running checkpoints from 18.4.1?

The node would reject it pretty early on (and you wouldn't see these daemon messages) if the checkpoint is higher than the alt chain fork point.

# Action History
- Created by: Rav3nPL | 2025-06-25T11:35:16+00:00
