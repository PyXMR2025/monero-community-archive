---
title: '"Exception in main! Error adding spent key image to db transaction: MDB_BAD_TXN..."
  On Mac OS Sonoma'
source_url: https://github.com/monero-project/monero/issues/9037
author: dicelander
assignees: []
labels:
- arm
- mac
created_at: '2023-10-24T20:07:30+00:00'
updated_at: '2024-12-14T00:17:00+00:00'
type: issue
status: closed
closed_at: '2024-12-14T00:17:00+00:00'
---

# Original Description
```
2023-10-24 09:44:21.703	     0x1e3c5d300	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.1-release)
2023-10-24 09:44:21.703	     0x1e3c5d300	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2023-10-24 09:44:21.703	     0x1e3c5d300	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2023-10-24 09:44:21.703	     0x1e3c5d300	INFO	global	src/daemon/core.h:64	Initializing core...
2023-10-24 09:44:21.704	     0x1e3c5d300	INFO	global	src/cryptonote_core/cryptonote_core.cpp:523	Loading blockchain from folder ***... (omitted because sensitive info in path)
2023-10-24 09:44:21.998	     0x1e3c5d300	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2023-10-24 09:44:21.998	     0x1e3c5d300	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2023-10-24 09:44:21.998	     0x1e3c5d300	ERROR	daemon	src/daemon/main.cpp:377	Exception in main! Error adding spent key image to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
```

Error happens when synchronizing blockchain on MacOS Sonoma 14.0 Apple Silicon (M1) on both 0.18.3.1 and 0.18.2.2. Doesn't happen on Monterey (also M1) or on Debian 11.3 ARM (Virtual Machine) (where I was able to complete sync with the very same blockchain file).

# Discussion History
## selsta | 2023-10-24T20:08:49+00:00
How did you install monerod? Where did you store the blockchain?

## dicelander | 2023-10-24T20:19:27+00:00
Monerod is installed from official binaries, downloaded from official download links from this project's releases page. Blockchain file is stored on internal SSD. Copied the data dir to a Debian virtual machine, checked the md5 sum (was the same as the file on Sonoma SSD), used both 0.18.3.1 and 0.18.2.2 and was able to finish syncing a copy each time. Did the same with another machine running Monterey on M1 and was also able to finish syncing.
So the issue seems to be specific to Sonoma

## selsta | 2023-10-24T20:59:39+00:00
The text usually indicates a corrupted blockchain. It's difficult to figure out how this happened, did you have a power loss during sync at some point? I run Sonoma myself and did not have any issues yet. There are also no other reports about this.

I'm also not sure why it works on other OS.

My suggestion would be to sync from scratch with v0.18.3.1 and report back if this issue shows up again.

## dicelander | 2023-10-24T21:22:22+00:00
The issue happens whenever I try to sync a blockchain on Sonoma (M1), even from scratch

## selsta | 2023-10-24T21:23:55+00:00
At what percentage / block height does that happen? Is it consistent or random?

## dicelander | 2023-10-25T01:05:30+00:00
It seems almost random, now some reason it synced the last 95 blocks and happened again at 100% with the following errors:

```
2023-10-25 00:46:42.364	I Loading checkpoints
2023-10-25 00:46:42.864	I Core initialized OK
2023-10-25 00:46:42.864	I Initializing p2p server...
2023-10-25 00:46:42.872	I p2p server initialized OK
2023-10-25 00:46:42.872	I Initializing core RPC server...
2023-10-25 00:46:42.874	I Binding on 127.0.0.1 (IPv4):18081
2023-10-25 00:46:42.892	I core RPC server initialized OK on port: 18081
2023-10-25 00:46:42.894	I Starting core RPC server...
2023-10-25 00:46:42.894	I core RPC server started ok
2023-10-25 00:46:42.895	I Starting p2p net loop...
2023-10-25 00:46:43.897	I 
2023-10-25 00:46:43.897	I **********************************************************************
2023-10-25 00:46:43.897	I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-10-25 00:46:43.897	I 
2023-10-25 00:46:43.897	I You can set the level of process detailization through "set_log <level|categories>" command,
2023-10-25 00:46:43.897	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-10-25 00:46:43.897	I 
2023-10-25 00:46:43.897	I Use the "help" command to see the list of available commands.
2023-10-25 00:46:43.897	I Use "help <command>" to see a command's documentation.
2023-10-25 00:46:43.898	I **********************************************************************
2023-10-25 00:46:43.899	W Unable to send transaction(s), no available connections
2023-10-25 00:46:46.860	I [193.142.58.222:18080 OUT] Sync data returned a new top block candidate: 3003116 -> 3003211 [Your node is 95 blocks (3.2 hours) behind] 
2023-10-25 00:46:46.861	I SYNCHRONIZATION started
2023-10-25 00:47:01.841	I Synced 3003136/3003211 (99%, 75 left)
2023-10-25 00:47:10.081	I Synced 3003156/3003211 (99%, 55 left)
2023-10-25 00:47:18.001	I Synced 3003176/3003211 (99%, 35 left)
2023-10-25 00:47:25.899	I Synced 3003196/3003211 (99%, 15 left)
2023-10-25 00:47:38.090	I Synced 95 blocks in 46 seconds (2.065 blocks per second)
2023-10-25 00:47:38.091	I 
2023-10-25 00:47:38.091	I **********************************************************************
2023-10-25 00:47:38.091	I You are now synchronized with the network. You may now start monero-wallet-cli.
2023-10-25 00:47:38.091	I 
2023-10-25 00:47:38.091	I Use the "help" command to see the list of available commands.
2023-10-25 00:47:38.091	I **********************************************************************
2023-10-25 00:47:38.091	I Synced 3003211/3003211
status
Height: 3003214/3003214 (100.0%) on mainnet, not mining, net hash 2.58 GH/s, v16, 12(out)+0(in) connections, uptime 0d 0h 11m 0s
2023-10-25 00:58:18.239	W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 00:58:18.240	W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 00:58:18.240	E Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 00:58:18.240	W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 00:58:18.240	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 00:59:00.496	E Transaction spends at least one output which is too young
2023-10-25 00:59:07.447	E Transaction spends at least one output which is too young
2023-10-25 00:59:11.758	E Transaction spends at least one output which is too young
2023-10-25 00:59:24.555	E Transaction spends at least one output which is too young
2023-10-25 00:59:30.627	I [193.142.4.47:18085 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:30.628	I SYNCHRONIZATION started
2023-10-25 00:59:31.408	I [13.48.10.12:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:31.409	I SYNCHRONIZATION started
2023-10-25 00:59:34.556	I [162.218.65.39:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:34.556	I SYNCHRONIZATION started
2023-10-25 00:59:35.286	I [178.63.84.121:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:35.286	I SYNCHRONIZATION started
2023-10-25 00:59:36.212	I [12.34.98.148:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:36.212	I SYNCHRONIZATION started
2023-10-25 00:59:36.703	I [193.142.4.47:18085 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:36.703	I SYNCHRONIZATION started
2023-10-25 00:59:37.539	I [12.34.98.148:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:37.539	I SYNCHRONIZATION started
2023-10-25 00:59:38.225	I [76.106.42.36:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:38.225	I SYNCHRONIZATION started
2023-10-25 00:59:38.676	I [193.142.4.47:18085 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:38.676	I SYNCHRONIZATION started
2023-10-25 00:59:39.082	I [66.94.107.91:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:39.083	I SYNCHRONIZATION started
2023-10-25 00:59:39.791	I [178.63.84.121:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:39.792	I SYNCHRONIZATION started
2023-10-25 00:59:40.214	I [66.94.107.91:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:40.214	I SYNCHRONIZATION started
2023-10-25 00:59:41.017	I [13.48.10.12:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:41.018	I SYNCHRONIZATION started
2023-10-25 00:59:41.478	I [66.94.107.91:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:41.478	I SYNCHRONIZATION started
2023-10-25 00:59:42.289	I [13.48.10.12:18080 OUT] Sync data returned a new top block candidate: 3003214 -> 3003216 [Your node is 2 blocks (4.0 minutes) behind] 
2023-10-25 00:59:42.289	I SYNCHRONIZATION started
```

This "SYNCHRONIZATION started" then repeats indefinitely

## dicelander | 2023-10-25T01:17:28+00:00
Seeing system logs, seems like it's an issue or some kind of conflict with Spotlight. If I stop Spotlight from indexing stuff (this is a new Sonoma installation, so spotlight is pretty hungry right now) monerod syncs just fine. As soon as I allow it to index stuff again, monerod fails.

## selsta | 2023-10-25T01:20:49+00:00
Any logs from this conflict that you can share?

Spotlight syncing should not be related, unless your SSD is broken. Which also shouldn't be the case with a new Mac.

## dicelander | 2023-10-25T01:55:15+00:00
Not sure what on these logs consists of sensitive or identifying info. What made me attempt disabling indexing was noticing a bunch of "mds_stores" crash logs on console, which google told me is related to spotlight.

I removed the index restriction on the monero data dir and as soon as it got a new top block candidate it went all to space. Now I'm pretty sure that the my new copy of the blockchain, if it wasn't before, is now corrupted. When I run monerod it now spews this mess:

```
2023-10-25 01:40:31.883	I Monero 'Fluorine Fermi' (v0.18.3.1-release)
2023-10-25 01:40:31.883	I Initializing cryptonote protocol...
2023-10-25 01:40:31.883	I Cryptonote protocol initialized OK
2023-10-25 01:40:31.884	I Initializing core...
2023-10-25 01:40:31.884	I Loading blockchain from folder (my home dir)/.bitmonero/lmdb ...
2023-10-25 01:40:31.934	E Transaction spends at least one output which is too young
2023-10-25 01:40:32.021	E Transaction spends at least one output which is too young
2023-10-25 01:40:32.065	E Transaction spends at least one output which is too young
2023-10-25 01:40:32.082	W Error attempting to retrieve an output pubkey from the dbMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <b97d3f95867e4f4a64ba0be38b83eacac9044e6fa71d013dedc11da2e497bb58> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <5a9dacaebd8dae6cc5d8ae0633b22802f90b8ded9c896c8e1bac22e1b9d0e25a> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <62bb104f8612e0fbd70753de55641c86ab6e51afe74456b0ad709dc64af2995b> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <f1f074d1ba1ba9f2593b8a70efe882f6583781aff09206f37b2a639720d81e5c> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <c1288d57019dec04327460bad4586953e43d07012027c7c2a9ccd73b449a2d5e> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <f362af66876c6cf2279dce5dd31b5cf69948ad4a266f6ccae3c89bee7b427062> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <5fd0d4ba88e7e2cf97059f9638cfa2ec7950669320122922d2bc62f7e5f71764> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <0634b388e062fc2bf4684374adc70174124131a304eaa2d75d06c76aeff03866> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <c50f56315aec1e1ae3fa171e90dc05bbd62d0c68dc5772ca89438c5400feea6f> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <3c08b878127914efdedf0e035b8467df9426dbcff246ca4d6e9982ea35a54872> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <33ea266bb47ef6a18c0c70c691031d1754b5cc0ee0621d61d2c34e5065c28d77> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <c82fd87250bfb85981cea985ce779d6a9d56ac70f16141337c5988bff718f878> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <89add0be34e1d2d02f89bcda9095f0113ac62eb5e38229b6d60dc92131f6357a> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.082	E Failed to get tx <2d16ba506f0529af709131a31f87fe88911d6406d18be95fda0d86db4fe0107b> from txpool for re-validation
2023-10-25 01:40:32.082	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <3dfc02bdca1a15624e6f69d25ed4b3a4130c8990a8615dfa796f2e3cfc35c97c> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <0090a9b4017f5dfcee1fcc78bd52154e729372919f14d7cac407f7adb9a2b77d> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <28c0b44cf90232df9c92d55f4aeeac96200684dd094ded2be715072b31ce4f81> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <1e93b8f85ddd05ef2f3bf17daf3e188e41bf5872d097ed91e1d8b20a8f73d581> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <a112a8ea7ac051e7821640603618ca43fc46363de4b68ed4972292a2fa51af87> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <d75dba3a5cc02ed1f491475df83ffcceb7ee13f52a0d25d3e6b299d0d158cd87> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <fb17574f63f7806451265cdbe9eb92e52102359e9d250b574a59db322cf13688> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <9ed532651c4c499c93544193c6d2076212af60f056eb3ac896501a6513d28088> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <ef5a31c55d138869caae44bdd2a66fdf5f62f4832232f335e82cceada0e00689> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <993a117f08a0e98a8fe31dd180de338abf657ae6d2e55d3bd971fd02cbc5718b> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <2840e5c102392ca6066d7f303311d45db06d9049cdf271aba1ef043b8163ff8d> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <3d97c0cd8ff277fce86dfbb29c4aada084c3bbda6e4e636f5764b5df1531138f> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <76f3f387e32d413a6ac320d091a526e76e2784e8ef3919f7807c3129beb4628f> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <f9019f2c91000f68dc8bee5527cd43b0815fac65a29751d6f9a475448cc64191> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <7d5390ca25ee5d84e9e325b0d332f4e4fd50b9501a1a2a98b9166ac478f32c93> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <a715e668afb4c26bac8954c9fe951f317a3d499335454b65bc8441cad41eaf95> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <0bf45bf7106643d2c41803c4ccf9cd6d513722adb5328252a0b77bfdf2919e98> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <6da1e25b360972fabb470d439f6ffaf0a770f60397dc69420d77c69a0a0c9d9a> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <ad1aba03adabf560b562ffa7a579f5b85364c2a0c8e962655e94a6c67d34f89d> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <4b9867c03ba4a12651572aa88ec470843d03178b7efc91f43812c52cfc06daa0> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <603fc5a31ae599dce25357c452c521c497a71fb04369b89cc4b092e09b3d4ca1> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <839de720dd76acb6fd98a0dc8429cfdcafa1301d97daedc74194df7ac9f470a1> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <5e87c672cbb4fc88cf3b3904292b334823fa67869f7b99cc04e6ba6ed45987a1> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <98a1eebe592a01b2073b69ac200daba3aab0c46976f4c62e2bffcf93694d76a2> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <b9e811c1924b27c2ca588593633973a78054a6eb5607bf25a0aeed0e4fb562a5> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <b35bc7bcdb247438e36155fbfc489be78da5152d697e53e2c09d6a22b9f349a9> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <74d73a9995da1ebaf2ec0249da8dafafc62f96050e7a2d0cb4ce82628dfaf9b0> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <fb6742808e8db85565a4751236b03ce5741f104ac24faadff47d5ca3e89461b1> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <197f57f6bca7ecf5a3081550b5d36b3fa46b15c1633a1130775accbdde7f9fb3> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <bd51dfdac541fae2dbf79c1d5883824c6b3489bc5ec4807654ff0ea3a0f4f6b5> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <a6e9e1c4cab6a6e28fd8d176344901900ec3ec466aec3b2bb3df81acce18eeb6> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <a7d69a476b55bc472a49d4c91f2038827fb1bd018349cd1264f7560331cf94b9> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <4b2d247037639c57414dbb327bcc0333544708ec8627b6d13e10505024b791bd> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <d98f61ee9120f1666484a37ca53becd97cd95f1c5806672240a9e32404f442c5> from txpool for re-validation
2023-10-25 01:40:32.083	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.083	E Failed to get tx <29b8b44c7a39c935427f8c6a856210b58ed80f0f4f9fa7fe04164e986685a7c6> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <017c5f53186aa8f766f3f76207e2a8b52cc6612cf1135fd8f433d8d2182af0c6> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <181bec001fd1d50e3ef59b13c42de941b37b316b016ccf8a5c9ce12acd9b4ac8> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <d1d785e8886df2119998d475b69c0234db67703628c8e4afe116b6e0ec9c13cb> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <1defc0abfaaebe3ad19de3e8c8f0a7c5389a57426063d8b9304de0579f5c4ecd> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <0eef1cfeb93de15ac4c5129c6db00180faca35b734047f491d4e6219534bddd0> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <df801c1791cbd00f339265831e2c26acb1d97b1eba9c430284f862167c944fd1> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <e2645b4044610a062c35f0e94322ef81ec69d8110a68379dfa5fd5de9a9801d3> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <8b7a18738e5efe90a0d32f5585b8bc4a76500a94c98c9ac606ba506273a251d3> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <4c5dac657b459dfd1dbf58ab6b340ce4fb6961d657ec96f8ccb69bb8d2c5a3d7> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <03f2137089b9df9942777190ff5fcf145a9f2d9e790e2b3311377aeea70633d8> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <4623a32a401092e3fa38059f4eacb383f1c9e6796e7cbe2cdb024c4169f729dd> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <6d6cb49ffebd732cb345e16d57411e511cb669cfca51025649f3eff50e9bbae5> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <40d47d5019f991f96a52ce8ae709a91bf35e8febc8449059fcb052fe7fa7d3e5> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <233b9219527793d063ddc02696b482a24f7b848aa8be3358a0138e95918153e6> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <a30c7198c26719dd40d1d543ee3fee2a135f5059f05a7346a74b958b8a2103e7> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <7fbf20a73b350644c673d482245417ce539a526ea4aacaf343aa8acfbfab8ae9> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <36d3024b3ce900311ccf5e0d26f0a5b8b944d80cf90feafc079e0afb32533ceb> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <38793323b1f2f7113164e94a8318b2c714cecb6ef7886d6217d8a21329bdd5ef> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <a720c2bbc4dd453924434c1d33bee69c54dcad7de6f321c6a266d29bb55b1bf9> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <440939cac33e3d9f4d0464edf814b098f302ed28e450fc48b515197f960844f9> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <28698ba6e1ba6e9d0ecbd3af9f7f267837ba4d4fe33de92b556d48ba7b3655fa> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <019cf8a8a1694016888a2a753eabe2b1e8b2c67ac80aa287f9d2059299a2c8fc> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <3b568397cfbccd666b86d2c0583dfd9f5d531551ad333ad0f4fb897f5ef88ffd> from txpool for re-validation
2023-10-25 01:40:32.084	E Failed to remove tx from txpool: Error finding txpool tx meta: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	E Failed to get tx <e0499685c16b8982c422ae53e847098b2b109d453eeee044101587bb91ec18fe> from txpool for re-validation
2023-10-25 01:40:32.084	W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:32.084	I Loading checkpoints
2023-10-25 01:40:32.087	I Core initialized OK
2023-10-25 01:40:32.087	I Initializing p2p server...
2023-10-25 01:40:32.090	I p2p server initialized OK
2023-10-25 01:40:32.090	I Initializing core RPC server...
2023-10-25 01:40:32.091	I Binding on 127.0.0.1 (IPv4):18081
2023-10-25 01:40:32.105	I core RPC server initialized OK on port: 18081
2023-10-25 01:40:32.106	I Starting core RPC server...
2023-10-25 01:40:32.106	I core RPC server started ok
2023-10-25 01:40:32.106	I Starting p2p net loop...
2023-10-25 01:40:33.107	I 
2023-10-25 01:40:33.107	I **********************************************************************
2023-10-25 01:40:33.107	I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-10-25 01:40:33.108	I 
2023-10-25 01:40:33.108	I You can set the level of process detailization through "set_log <level|categories>" command,
2023-10-25 01:40:33.108	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-10-25 01:40:33.108	I 
2023-10-25 01:40:33.108	I Use the "help" command to see the list of available commands.
2023-10-25 01:40:33.108	I Use "help <command>" to see a command's documentation.
2023-10-25 01:40:33.108	I **********************************************************************
2023-10-25 01:40:33.136	W Unable to send transaction(s), no available connections
2023-10-25 01:40:33.721	I [68.112.145.64:18080 OUT] Sync data returned a new top block candidate: 3003223 -> 3003229 [Your node is 6 blocks (12.0 minutes) behind] 
2023-10-25 01:40:33.722	I SYNCHRONIZATION started
2023-10-25 01:40:35.470	E failed to find transaction input in key images. img=<fd5aa27222f77b7ed3a91cdc0b556a6e7bd6dc51d95f7263a10397d8d05e55a0>
2023-10-25 01:40:35.470	E transaction id = <d334b02eb4ef8d9fbed11bf94d7dd3cb69146996286ee101d5380004a6924b54>
2023-10-25 01:40:35.471	W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:35.471	W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:35.471	E Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:35.471	W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-10-25 01:40:35.471	E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
```

## selsta | 2023-10-25T10:43:51+00:00
Can you rule out that you have a bad or broken SSD? Two programs that are disk related are crashing or corrupting on your system, Spotlight and monerod should be totally unrelated.

## dicelander | 2023-10-25T11:12:25+00:00
Running First Aid from disk utility while in recovery mode recovery shows the drive is fine. I tried moving the data dir to an external ssd that (should be) fine and got the same error when trying to sync monerod while spotlight indexes the drive. Erased the external drive and blocked spotlight from indexing it and was able to finish syncing just fine.

One thing I noticed is it happens when it gets new top block candidates after it finished syncing once. If I finish syncing on a different OS, move it and try to keep the same blockchain synced on Sonoma, as soon as it gets a new top block candidate message it fails.
If I sync it partially (say, 40 blocks) on another OS and move it to Sonoma, it finishes syncing just fine until it hits 100%, then I get the error when it tries adding another block.

Testing this is pretty frustrating because every new sync from scratch takes sooooooo looooong lol, I'm keeping mid sync copies from the blockchain at different stages to speed things up, not sure if it would matter, as the error always happens at the end

## selsta | 2023-10-25T17:18:42+00:00
Can you try to update to macOS 14.1?

## dicelander | 2023-11-03T21:15:09+00:00
Hi! Sorry for the delay.

I did update to 14.1, error was gone for a while and I've been using the blockchain on an external ssd to try and isolate the behaviour.

Just now it happened again and voila, I couldn't eject the ssd because 'mds' (which apparently is part of spotlight), was accessing the drive (this one should've been already indexed and only holds the blockchain, so this behavior is quite weird)

I'm pretty sure it's some kind of bug with spotlight itself. The drive is essentially unusable until it stops doing whatever it is doing. I can't even eject it. Also, "mds_stores" is currently using over 40% of the CPU, while "mds" sometimes jumps to >100% and a LOT of "mdworker_shared" processes are running, by user _spotlight.

## selsta | 2023-11-03T21:18:39+00:00
You might want to reinstall macOS, definitely seems like some Spotlight related bug.

## terryschmidt | 2023-12-29T22:37:04+00:00
Hi guys. I have the same problem with virtually the same setup. An M1 Mac Mini running Sonoma 14.2.1 and I'm using an external drive. I barely have enough space to store the blockchain on my internal drive but when I do so, there are no issues. I understand this isn't Monero specific but it pretty frustrating and, in practice, is almost effectively an attack on the network from my point of view. If you're using a Mac, you keep your OS up to date, and you want or need to use an external drive, you just won't ever be able to synchronize.

## selsta | 2024-01-03T04:50:00+00:00
Did you try to disable Spotlight for the external drive as a workaround?

https://discussions.apple.com/thread/8648215?sortBy=best

## terryschmidt | 2024-02-29T09:48:36+00:00
I tried disabling Spotlight for the entire external drive and I still have this problem.

## dicelander | 2024-02-29T11:27:24+00:00
Hi! Sorry for not responding earlier.
I managed to not have the issue ever again by using an APFS formatted external drive. I only use it on Mac anyway, so this wasn't a problem.

## selsta | 2024-02-29T11:35:41+00:00
@dicelander how was the drive formatted previously?

## dicelander | 2024-02-29T11:45:08+00:00
Internal drive has always been APFS, not sure why it was failing sync there before.
External drive used to be a single exFAT partition cause I wanted to also use it on other systems. Now I'm using an APFS for most of my data and a smaller exFAT partition for when I want to move stuff around between different OSs.
I noticed the weird spotlight indexing behavior stopped on APFS. Never payed much attention to the new exfat partition.

Sync on APFS was ridiculously faster than it used to be on exFAT

## terryschmidt | 2024-02-29T21:28:10+00:00
Reformatting my drive to APFS appears to have fixed it. I haven't fully sync'd yet but I'm way further than I've ever gotten before. I guess on an Apple machine you do things the Apple way. Good lord.

## Some1Else83129 | 2024-04-19T15:18:49+00:00
I've been wasting hours and fighting with this thing for the last two weeks on my Mac M1 until I read this last night. Backed up my external SSD, reformatted to APFS, copied blockchain and files over - and the daemon syncs! Issue resolved. A bittersweet thank you to all in the thread.

## selsta | 2024-12-14T00:17:00+00:00
Closing as the issue seems to be solved with using AFPS.

# Action History
- Created by: dicelander | 2023-10-24T20:07:30+00:00
- Closed at: 2024-12-14T00:17:00+00:00
