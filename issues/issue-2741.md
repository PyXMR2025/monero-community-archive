---
title: Power8 - Monerod not syncing
source_url: https://github.com/monero-project/monero/issues/2741
author: lemonsked
assignees: []
labels: []
created_at: '2017-10-30T17:18:19+00:00'
updated_at: '2019-01-30T04:11:46+00:00'
type: issue
status: closed
closed_at: '2017-11-14T13:30:13+00:00'
---

# Original Description
`2017-10-30 17:17:16.156     100064abf170        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to create a read transaction for the db: MDB_READERS_FULL: Environment maxreaders limit reached
2017-10-30 17:17:16.157     100061dbf170        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to create a read transaction for the db: MDB_READERS_FULL: Environment maxreaders limit reached
2017-10-30 17:17:16.162     100066dbf170        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to create a read transaction for the db: MDB_READERS_FULL: Environment maxreaders limit reached
2017-10-30 17:17:16.219     1000159bf170        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to create a read transaction for the db: MDB_READERS_FULL: Environment maxreaders limit reached
2017-10-30 17:17:16.219     100014fbf170        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to create a read transaction for the db: MDB_READERS_FULL: Environment maxreaders limit reached
2017-10-30 17:17:27.162 [P2P3]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to renew a read transaction for the db: Invalid argument
2017-10-30 17:17:27.373 [P2P7]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to renew a read transaction for the db: Invalid argument
2017-10-30 17:17:27.967 [P2P5]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to renew a read transaction for the db: Invalid argument
2017-10-30 17:17:30.184 [P2P5]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Failed to renew a read transaction for the db: Invalid argument
`
Ubuntu 16.04


# Discussion History
## hyc | 2017-10-30T17:20:47+00:00
The default maxreaders limit is 126. How many threads are you using?

## lemonsked | 2017-10-30T17:23:17+00:00
Default? The dedi has 160 threads though.
I used make -j150 to compile it though.

## hyc | 2017-10-30T17:38:04+00:00
That make flag has nothing to do with what monerod uses at runtime.

For the moment you're going to have to run with fewer threads. In fact, much fewer. Run `monerod --max-concurrency 60` until we have a patch to raise the DB setting.

## lemonsked | 2017-10-30T17:46:26+00:00
Still doesn’t sync. https://hastebin.com/rojobedalo.sql

## hyc | 2017-10-30T18:08:53+00:00
Try the patch in PR #2742

## ChrisDowning | 2017-10-31T10:17:35+00:00
I have been encountering this issue (`Environment maxreaders limit reached` followed by a segfault) using both 0.11.0.0 and 0.11.1.0 on an Intel server too. Following the advice in this thread, I set `max_concurrency` to 60 first but still faced the same problem, however dropping it to 44 seems to have worked. Once I have finished syncing I would be happy to try other values to see what the "sweet spot" is if necessary; I went with 44 purely to match the number of physical cores in the box.

## lemonsked | 2017-10-31T10:54:19+00:00
20 worked for me. Dropped from 60 to 20. Haven't tried anything else.

## moneroexamples | 2019-01-30T00:16:55+00:00
This issue has been recently encountered in openmoenro in https://github.com/moneroexamples/openmonero/issues/127#issuecomment-458696396  Thus I want to share my observation/experience as they might be useful for others who encounter the same issue in their projects.

In openmonero, the issue was encountered where there were more than 120 accounts being used/imported at the same time. In this case, there would be 120 threads which would access lmdb in read only mode to tx data. This was resulting in MDB_READERS_FULL. Initially I though it is because all the threads are not synchronized and access lmdb in parallel. But after further testing and work, I found that it's about no of threads only. Wether they access lmdb in parallel or not, did not matter. Thus as long as there were 120+ readers of the lmdb (paraller or not) the error was occurring. 

The solution was to limit number of threads that access lmdb. So now, the 120+ don't access lmdb directly, but instead use a thread pool for that. The tread pool has limited number of threads/workers (e.g. 8) that access the lmdb on behave of the 120+ threads. So the 120+ threads submit jobs (read lmdb jobs) to the thread pool queue, and the workers in the thread execute the jobs from the queue. 





## hyc | 2019-01-30T02:42:32+00:00
You've run into LMDB's default maxreaders setting. I don't believe we're explicitly configuring this, but you could simply add a call for that when opening the LMDB environment.

## moneroexamples | 2019-01-30T04:11:46+00:00
@hyc 

Thanks. For now its good. Using thread pool also has other benefits, so will see how it goes.

# Action History
- Created by: lemonsked | 2017-10-30T17:18:19+00:00
- Closed at: 2017-11-14T13:30:13+00:00
