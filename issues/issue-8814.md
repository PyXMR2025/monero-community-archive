---
title: LMDB trashed, again.
source_url: https://github.com/monero-project/monero/issues/8814
author: trasherdk
assignees: []
labels: []
created_at: '2023-03-29T16:58:21+00:00'
updated_at: '2023-04-28T04:34:05+00:00'
type: issue
status: closed
closed_at: '2023-04-28T04:34:05+00:00'
---

# Original Description
My mainnet `Monero 'Fluorine Fermi' (v0.18.2.0-release)` have been running happily for a while, when something happened.

Then I notice a lot of these messages:
```
2023-03-29 15:19:24.993        I SYNCHRONIZATION started
2023-03-29 15:19:26.881 I [116.108.19.18:42988 INC] Sync data returned a new top block candidate: 2852601 -> 2852666 [Your node is 65 blocks (2.2 hours) behind] 
2023-03-29 15:19:26.882 I SYNCHRONIZATION started
status
Height: 2852601/2852601 (100.0%) on mainnet, not mining, net hash 2.55 GH/s, v16, 5(out)+1(in) connections, uptime 0d 14h 50m 16s
2023-03-29 15:19:32.150   I [91.115.255.185:62399 INC] Sync data returned a new top block candidate: 2852601 -> 2852666 [Your node is 65 blocks (2.2 hours) behind] 
2023-03-29 15:19:32.150        I SYNCHRONIZATION started
2023-03-29 15:19:33.677        I [212.99.226.35:9080 OUT] Sync data returned a new top block candidate: 2852601 -> 2852666 [Your node is 65 blocks (2.2 hours) behind] 
```

So, for some reason, it's not syncing anymore. I tried to restart monerod, and saw a bunch of:
```
2023-03-29 15:19:58.515        E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:19:58.515        E Failed to get tx <3fbb4323adb4398274078059963c4abd911f2c72bed12b0cc92a76a9de7125ba> from txpool for re-validation
2023-03-29 15:19:58.515        E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:19:58.515        E Failed to get tx <80ac8a69df574e699225774877166017e098dc8eec339305629bc2b1c5db45ba> from txpool for re-validation
2023-03-29 15:19:58.515        E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:19:58.515        E Failed to get tx <fa27e12c68493ebbfd2296ba0fb04bcfdd1eacd438fe4c58229462565fd9ceba> from txpool for re-validation
2023-03-29 15:19:58.515        E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:19:58.515        E Failed to get tx <a43ca4a8443e3dfa03f9d89f0083a9a65feaa2386ca7f03ff5b5b42f288059be> from txpool for re-validation
2023-03-29 15:19:58.515        E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:19:58.515        E Failed to get tx <b546e6b0e396a596237c6e594c8f39a168dd25bde4c26e7b9ab16319d3b313bf> from txpool for re-validation
2023-03-29 15:19:58.515        E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:19:58.515        E Failed to get tx <4702ffe6ff574da7f66509ebf054db4565ef33f3bb7e287401c32a46d4c8aec2> from txpool for re-validation
2023-03-29 15:19:58.515        E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:19:58.515        E Failed to get tx <9c84ce1f4fa482943104122646845b19360c34bcdf45cd2afb776c5e30431dc4> from txpool for re-validation
2023-03-29 15:19:58.515        E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:19:58.515        E Failed to get tx <c98ee2cd777e36334295709edb5a99525c89be516034d1bda77fd9881a26e7c8> from txpool for re-validation
...
...
2023-03-29 15:20:15.432        E failed to find transaction input in key images. img=<fff7b49a289e58f4b667fac60979ac30adf070758beecf87b7155559e5e854d1>
2023-03-29 15:20:15.433        E transaction id = <48240292b808dce1f3aab4d0a5e306a74bf90ce82e99b4e30d5617d4fc3b2f29>
2023-03-29 15:20:15.434        W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:20:15.434        W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:20:15.435        E Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:20:15.436        W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:20:15.436        E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:20:17.108        I [192.252.212.27:61491 OUT] Sync data returned a new top block candidate: 2852601 -> 2852667 [Your node is 66 blocks (2.2 hours) behind] 
2023-03-29 15:20:17.108        I SYNCHRONIZATION started
2023-03-29 15:20:23.770        I [45.83.220.102:18080 OUT] Sync data returned a new top block candidate: 2852601 -> 2852667 [Your node is 66 blocks (2.2 hours) behind] 
2023-03-29 15:20:23.770        I SYNCHRONIZATION started
2023-03-29 15:20:29.011        I [132.177.197.115:35194 INC] Sync data returned a new top block candidate: 2852601 -> 2852667 [Your node is 66 blocks (2.2 hours) behind] 
```

I have tried to pop blocks off the chain:
```sh
$ monero-blockchain-import --offline --disable-dns-checkpoints --pop-blocks 100 --data-dir /var/lib/monero/data/mainnet/2023-03-29 15:34:54.641 I Starting...
2023-03-29 15:34:54.641 I database: LMDB
2023-03-29 15:34:54.641 I verify:  true
2023-03-29 15:34:54.641 I batch:   true  batch size: 5000
2023-03-29 15:34:54.641 I resume:  true
2023-03-29 15:34:54.641 I nettype: mainnet
2023-03-29 15:34:54.641 I bootstrap file path: /var/lib/monero/data/mainnet/export/blockchain.raw
2023-03-29 15:34:54.641 I database path:       /var/lib/monero/data/mainnet/
2023-03-29 15:34:54.642 I Loading blockchain from folder /var/lib/monero/data/mainnet/lmdb ...
2023-03-29 15:34:54.940 W Error attempting to retrieve an output pubkey from the dbMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:34:54.941 E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:34:54.941 E Failed to get tx <783b9c467c17a8b4c50ba6eebaf453ee55737720a898e287f4fb94daca291c2b> from txpool for re-validation
2023-03-29 15:34:54.941 E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
...
...
2023-03-29 15:34:54.945 E Failed to get tx <fb6e746cf915287e447e0e72fe6f6f88472adaadf14da2b4eefcc992bb61edf6> from txpool for re-validation
2023-03-29 15:34:54.945 E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:34:54.945 E Failed to get tx <5e570779c588b6075fddf86f3f925de9cd298c9ee357fce10b390f711af4fbfe> from txpool for re-validation
2023-03-29 15:34:54.945 W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 15:34:54.945 I Loading checkpoints
2023-03-29 15:34:54.945 I height: 2852601
2023-03-29 15:34:58.989 I height: 2852501
```

So, it's still bitching, let's pop more blocks:
```sh
$ monero-blockchain-import --offline --disable-dns-checkpoints --pop-blocks 200 --data-dir /var/lib/monero/data/mainnet/
2023-03-29 15:35:51.431 I Starting...
2023-03-29 15:35:51.431 I database: LMDB
2023-03-29 15:35:51.431 I verify:  true
2023-03-29 15:35:51.432 I batch:   true  batch size: 5000
2023-03-29 15:35:51.432 I resume:  true
2023-03-29 15:35:51.432 I nettype: mainnet
2023-03-29 15:35:51.432 I bootstrap file path: /var/lib/monero/data/mainnet/export/blockchain.raw
2023-03-29 15:35:51.432 I database path:       /var/lib/monero/data/mainnet/
2023-03-29 15:35:51.433 I Loading blockchain from folder /var/lib/monero/data/mainnet/lmdb ...
2023-03-29 15:35:51.512 I Loading checkpoints
2023-03-29 15:35:51.513 I height: 2852501
Error loading blockchain db: Error finding spent key to removeMDB_PAGE_NOTFOUND: Requested page not found -- shutting down now
```

Hmm, looks like I'm at the end of the road:
```
2023-03-29 16:37:42.502        I Initializing cryptonote protocol...
2023-03-29 16:37:42.502        I Cryptonote protocol initialized OK
2023-03-29 16:37:42.503        I Initializing core...
2023-03-29 16:37:42.503        I Loading blockchain from folder /var/lib/monero/data/mainnet/lmdb ...
2023-03-29 16:37:42.579        I Loading checkpoints
2023-03-29 16:37:42.588        I Core initialized OK
2023-03-29 16:37:42.588        I Initializing p2p server...
2023-03-29 16:37:42.602        I p2p server initialized OK
2023-03-29 16:37:42.602        I Initializing core RPC server...
2023-03-29 16:37:42.602        I Binding on 192.168.1.70 (IPv4):18081
2023-03-29 16:37:42.603        I core RPC server initialized OK on port: 18081
2023-03-29 16:37:42.603        I Initializing restricted RPC server...
2023-03-29 16:37:42.603        I Binding on 192.168.1.71 (IPv4):18084
2023-03-29 16:37:43.898        I restricted RPC server initialized OK on port: 18084
2023-03-29 16:37:43.899        I Starting core RPC server...
2023-03-29 16:37:43.899        I core RPC server started ok
2023-03-29 16:37:43.899        I Starting restricted RPC server...
2023-03-29 16:37:43.899        I restricted RPC server started ok
2023-03-29 16:37:43.904        I Public RPC port 18084 will be advertised to other peers over P2P
2023-03-29 16:37:43.904        I Starting p2p net loop...
2023-03-29 16:37:44.904        I
2023-03-29 16:37:44.905        I **********************************************************************
2023-03-29 16:37:44.905        I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-03-29 16:37:44.905        I
2023-03-29 16:37:44.905        I You can set the level of process detailization through "set_log <level|categories>" command,
2023-03-29 16:37:44.905        I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-03-29 16:37:44.905        I
2023-03-29 16:37:44.905        I Use the "help" command to see the list of available commands.
2023-03-29 16:37:44.905        I Use "help <command>" to see a command's documentation.
2023-03-29 16:37:44.905        I **********************************************************************
2023-03-29 16:37:45.774        I [185.125.169.149:18080 OUT] Sync data returned a new top block candidate: 2852501 -> 2852700 [Your node is 199 blocks (6.6 hours) behind] 
2023-03-29 16:37:45.774        I SYNCHRONIZATION started
...
...
2023-03-29 16:39:04.329        E Failed to get tx meta from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 16:39:04.329        E Failed to get tx meta from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 16:39:04.330        E Failed to get tx meta from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 16:39:04.330        E Failed to get tx meta from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 16:39:04.330        E Error adding transaction to txpool: Error adding txpool tx metadata to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 16:39:04.330        W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 16:39:04.330        E Exception at [core::handle_incoming_txs()], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 16:39:04.331        W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 16:39:04.331        E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-03-29 16:39:13.635        I p2p net loop stopped
2023-03-29 16:39:13.652        I Stopping core RPC server...
2023-03-29 16:39:13.653        I Stopping restricted RPC server...
2023-03-29 16:39:13.653        I Node stopped.
2023-03-29 16:39:13.654        I Deinitializing core RPC server...
2023-03-29 16:39:13.654        I Deinitializing restricted RPC server...
2023-03-29 16:39:13.654        I Deinitializing p2p...
2023-03-29 16:39:13.668        I Deinitializing core...
2023-03-29 16:39:13.710        I Stopping cryptonote protocol...
2023-03-29 16:39:13.710        I Cryptonote protocol stopped successfully
```

I guess rsync from the back-up node, again, is the way forward :angry: 

# Discussion History
## trasherdk | 2023-03-30T03:53:49+00:00
Okay, 6 hours later it's running again.

Does a LMDB repair tool exist for this thing?

## moneromooo-monero | 2023-04-03T14:42:52+00:00
--db-salvage

It doesn't to work often though.

Otherwise you'd need to get someone like hyc to look at your db to see what broke (I assume from your wording it broke while it was running, which is pretty peculiar).

## trasherdk | 2023-04-04T07:04:03+00:00
Yes, I did try the `--db-salvage` thingy, and it did not like the `lmdb` file.

Yes, it was running, and stopped syncing, probably a couple of hours before I checked the log, and saw the repeated:
```
2023-03-29 15:19:32.150        I SYNCHRONIZATION started
2023-03-29 15:19:33.677        I [212.99.226.35:9080 OUT] Sync data returned a new top block candidate: 2852601 -> 2852666 [Your node is 65 blocks (2.2 hours) behind] 
```

The `mainnet` daemon is running on a local `x86_64 Intel(R) Core(TM)2 Duo CPU T8100 @ 2.10GHz GenuineIntel GNU/Linux`, that should probably retire.

Maybe my old GPU mining rig should step up to the plate, and take over as DMZ, the problem with that, is that data storage is on a USB spinner.

Anyway. I did a rsync from a remote backup node, blocked public access to RPC and ZMQ, and it's been running stable since.


## moneromooo-monero | 2023-04-05T14:53:23+00:00
If it's on USB, you may want to check system logs for any kind of I/O error. That sounds like the likely reason.

## trasherdk | 2023-04-10T04:49:52+00:00
Nah, it's on a SSD, but the internal GPU `nouveau-pci-0100` is running hot, and shut down the computer.

It's a very old laptop:
`Linux compaq-laptop 5.15.94 #1 SMP PREEMPT Fri Feb 17 18:59:35 CST 2023 x86_64 Intel(R) Core(TM)2 Duo CPU     T8100  @ 2.10GHz GenuineIntel GNU/Linux`
So it's not surprising.


## Dinamitrii | 2023-04-18T23:38:32+00:00
Why do not just update to latest version and try again?

version
0.18.2.2-release

## trasherdk | 2023-04-28T04:34:05+00:00
Laptop retired. Now running on a 6 GPU, pre RandomX mining rig :rofl: 

# Action History
- Created by: trasherdk | 2023-03-29T16:58:21+00:00
- Closed at: 2023-04-28T04:34:05+00:00
