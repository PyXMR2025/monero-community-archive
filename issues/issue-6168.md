---
title: monero-blockchain-prune corrupts the pruned database if interupted
source_url: https://github.com/monero-project/monero/issues/6168
author: ku4eto
assignees: []
labels: []
created_at: '2019-11-22T06:17:23+00:00'
updated_at: '2022-02-19T04:47:52+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:47:52+00:00'
---

# Original Description
As the tittle suggest.

Using 15.0 release, Windows 10 x64.

Synced the entire blockchain from the RAW file. Size was ~77GB.

I decide to prune it with the `moner-blockchain-prune --data-dir PATH --db-sync-mode fastest --copy-pruned-database`

After taking 6 hours, and still at ~12GB size, i had to shutdown the process.

There are no `save` commands, so i just issued SIGINT (CTRL+C).

Today, i try to restart the process with the same command.

The result is as follow:

```
2019-11-22 06:04:08.378 I Starting...
2019-11-22 06:04:08.378 I Initializing source blockchain (BlockchainDB)
2019-11-22 06:04:08.394 I Loading blockchain from folder "F:\Blockchain\bitmonero\lmdb" ...
2019-11-22 06:04:08.456 I source blockchain storage initialized OK
2019-11-22 06:04:08.472 I Loading blockchain from folder "F:\Blockchain\bitmonero\lmdb-pruned" ...
2019-11-22 06:04:08.550 W Error attempting to retrieve a hard fork version at height 1971956 from the db: MDB_NOTFOUND: No matching key/data pair found
2019-11-22 06:04:08.566 E Exception at [Pruning error], what=Error attempting to retrieve a hard fork version at height 1971956 from the db: MDB_NOTFOUND: No matching key/data pair found
```
Trying to load the `monerod` from that DB or from the other one does not work, closes right away with the same error.

The prune.log contains the following:

```
2019-11-21 22:06:43.260	11196	INFO	bcutil	src/blockchain_utilities/blockchain_prune.cpp:157	Copying spent_keys
2019-11-21 22:11:31.506	11196	INFO	global	src/blockchain_utilities/blockchain_prune.cpp:120	LMDB Mapsize increased.  Old: 12805MiB, New: 13317MiB
2019-11-22 06:02:43.497	3784	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-11-22 06:02:43.513	3784	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO,bcutil:INFO
2019-11-22 06:02:43.513	3784	INFO	bcutil	src/blockchain_utilities/blockchain_prune.cpp:494	Starting...
2019-11-22 06:02:43.513	3784	INFO	bcutil	src/blockchain_utilities/blockchain_prune.cpp:523	Initializing source blockchain (BlockchainDB)
2019-11-22 06:02:43.513	3784	INFO	bcutil	src/blockchain_utilities/blockchain_prune.cpp:566	Loading blockchain from folder "F:\Blockchain\bitmonero\lmdb" ...
2019-11-22 06:03:10.660	3784	INFO	bcutil	src/blockchain_utilities/blockchain_prune.cpp:581	source blockchain storage initialized OK
2019-11-22 06:03:10.682	3784	INFO	bcutil	src/blockchain_utilities/blockchain_prune.cpp:566	Loading blockchain from folder "F:\Blockchain\bitmonero\lmdb-pruned" ...
2019-11-22 06:03:10.846	3784	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1369	LMDB memory map needs to be resized, doing that now.
2019-11-22 06:03:10.854	3784	INFO	global	src/blockchain_db/lmdb/db_lmdb.cpp:569	LMDB Mapsize increased.  Old: 13317MiB, New: 14341MiB
2019-11-22 06:03:11.108	3784	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Error attempting to retrieve a hard fork version at height 1971956 from the db: MDB_NOTFOUND: No matching key/data pair found
2019-11-22 06:03:11.153	3784	ERROR	bcutil	src/blockchain_utilities/blockchain_prune.cpp:639	Exception at [Pruning error], what=Error attempting to retrieve a hard fork version at height 1971956 from the db: MDB_NOTFOUND: No matching key/data pair found
```


After trying to start the monerod few more times, it worked and synced properly.
Still cant get the `prune` to resume though.




# Discussion History
## moneromooo-monero | 2019-11-23T01:46:04+00:00
From the paths, it's partly written blockchain that's corrupt, not the original one.

## ku4eto | 2019-11-23T06:52:53+00:00
> 
> 
> From the paths, it's partly written blockchain that's corrupt, not the original one.

Yes, that is correct, i corrected my initial comment, since i got the original one to work.

Is this an expected behavior, for the copied pruned database to get corrupted, when the process gets interrupted?

## moneromooo-monero | 2019-11-23T11:49:03+00:00
Not really expected nor unexpected. I wasn't expecting anything in particular tbh. I don't think it's worth the time making it incremental since it's a one off and the original blockchain's safe.

## selsta | 2022-02-19T04:47:52+00:00
Closing for expected behaviour. It's generally easier to resync from scratch with `--prune-blockchain`.

# Action History
- Created by: ku4eto | 2019-11-22T06:17:23+00:00
- Closed at: 2022-02-19T04:47:52+00:00
