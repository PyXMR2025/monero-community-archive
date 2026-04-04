---
title: My Monero blockchain is broken (and for the second time!)
source_url: https://github.com/monero-project/monero/issues/8887
author: hugohugo130
assignees: []
labels: []
created_at: '2023-06-01T10:47:25+00:00'
updated_at: '2023-06-04T00:52:36+00:00'
type: issue
status: closed
closed_at: '2023-06-04T00:52:36+00:00'
---

# Original Description
the monerod.exe can't parse block from blob

2023-06-01 10:42:56.337 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-06-01 10:42:56.353 I Initializing cryptonote protocol...
2023-06-01 10:42:56.353 I Cryptonote protocol initialized OK
2023-06-01 10:42:56.353 I Initializing core...
2023-06-01 10:42:56.353 I Loading blockchain from folder G:\monero-blockchain\lmdb ...
2023-06-01 10:42:56.560 E Failed to parse block from blob
2023-06-01 10:42:56.602 I Stopping cryptonote protocol...
2023-06-01 10:42:56.617 I Cryptonote protocol stopped successfully
2023-06-01 10:42:56.617 E Exception in main! Failed to parse block from blob retrieved from the db


I'm using Windows 11
CPU: 12th Gen Inter(R) Core(TM) i7-1255U
RAM: 8GBx2 DDR4 SODIMM speed 3200MHz(Hynix)
DISK: 490GB SSD(system) + 2TB HDD
GPU: Intel(R) Iris(R) Xe Graphics
Internet: Ethernet

monero gui version is v0.18.2.2

# Discussion History
## plowsof | 2023-06-01T11:44:10+00:00
i notice `G:\monero-blockchain\lmdb` (External USB drive?) try starting with `--db-salvage flag` one time linked in the thread/comment below. if ti doesnt work, you have to start over (deleting the blockchain data file) with safe sync mode to reduce the chances of this happening again https://github.com/monero-project/monero/issues/7023#issuecomment-729197298

https://github.com/monero-project/monero/issues/7023#issuecomment-729157265

## hugohugo130 | 2023-06-01T11:47:59+00:00
G: partition is my SSD partition

## hugohugo130 | 2023-06-01T11:50:02+00:00
and I can't use "flag" command, because it said Unknown command: flag

## plowsof | 2023-06-01T12:13:57+00:00
apologies hugohugo130 i accidentally included the flag in quotes. `--db-salvage` only (do not forget to also include your `--data-dir` otherwise it will attempt to salvage a db file in the default location) e.g. `monerod.exe --data-dir G:\monero-blockchain --db-salvage`

## hugohugo130 | 2023-06-01T12:38:10+00:00
but I pruned my blockchain

## hugohugo130 | 2023-06-01T12:39:07+00:00
D:\Apps\monero-gui-v0.18.2.2>monerod.exe --prune-blockchain  --db-salvage --data-dir "G:\monero-blockchain"
2023-06-01 12:38:21.216 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-06-01 12:38:21.216 I Initializing cryptonote protocol...
2023-06-01 12:38:21.216 I Cryptonote protocol initialized OK
2023-06-01 12:38:21.217 I Initializing core...
2023-06-01 12:38:21.217 I Loading blockchain from folder G:\monero-blockchain\lmdb ...
2023-06-01 12:38:22.746 E Failed to parse block from blob
2023-06-01 12:38:22.763 I Stopping cryptonote protocol...
2023-06-01 12:38:22.764 I Cryptonote protocol stopped successfully
2023-06-01 12:38:22.764 E Exception in main! Failed to parse block from blob retrieved from the db

So I need to resync the blockchain?

## plowsof | 2023-06-01T15:35:48+00:00
side note: if you run `--prune-blockchain` once , you don't have to pass that flag again. (ofcourse if you resync you will have to pass it initially)

 Let me confirm if you can try anything else, but, if you need to resync the block chain add `--db-sync-mode safe:sync` to the flags to hopefully stop this from happening



## hugohugo130 | 2023-06-03T11:25:27+00:00
Because the space used by my SSD will use double space (or even triple space), so it is easy to run out of space. After the space is insufficient, monerod.exe will stop unexpectedly, causing data.mdb to be damaged.

## hugohugo130 | 2023-06-03T11:26:51+00:00
Luckily, I backed up the file and I tested, is valid data.mdb, I'm copying it to G:\monero-blockchain

## plowsof | 2023-06-03T13:45:37+00:00
so this is simply a 'ran out of storage space' issue? can be closed?

## hugohugo130 | 2023-06-04T00:52:36+00:00
okay, closed this issue

# Action History
- Created by: hugohugo130 | 2023-06-01T10:47:25+00:00
- Closed at: 2023-06-04T00:52:36+00:00
