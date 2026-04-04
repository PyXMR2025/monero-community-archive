---
title: LMDB possible deadlock with low probability in the wrapper in lmdb_txn_begin()
source_url: https://github.com/monero-project/monero/issues/7957
author: TheQuantumPhysicist
assignees: []
labels: []
created_at: '2021-09-19T18:31:53+00:00'
updated_at: '2021-10-11T17:58:04+00:00'
type: issue
status: closed
closed_at: '2021-10-11T17:58:04+00:00'
---

# Original Description
Hi guys:

I think I caught a possible deadlock.

In [`lmdb_txn_begin()`](https://github.com/monero-project/monero/blob/ad9956d9873ad8281fd88daf8b9202c74db3f796/src/blockchain_db/lmdb/db_lmdb.cpp#L495) function, the `mdb_txn_begin()` is called, and then in rare cases, the result can be `MDB_MAP_RESIZED`, which will require to call a resize function, `lmdb_resized()`. However, notice that `lmdb_resized()` calls `mdb_txn_safe::wait_no_active_txns();`. This function waits for `num_active_txns` to be zero before it returns... but that will never happen! Because, looking at an example of when `lmdb_txn_begin()` is called, you construct `mdb_txn_safe()` right before it, like you do [here](https://github.com/monero-project/monero/blob/ad9956d9873ad8281fd88daf8b9202c74db3f796/src/blockchain_db/lmdb/db_lmdb.cpp#L3976), which will increment the count of `num_active_txns`.

So, in summary, [here](https://github.com/monero-project/monero/blob/ad9956d9873ad8281fd88daf8b9202c74db3f796/src/blockchain_db/lmdb/db_lmdb.cpp#L3976), you increase the count of `num_active_txns` by one, then in the next line (if `MDB_MAP_RESIZED`) you wait for it to go back to zero *forever* [here](https://github.com/monero-project/monero/blob/ad9956d9873ad8281fd88daf8b9202c74db3f796/src/blockchain_db/lmdb/db_lmdb.cpp#L499), because of [this](https://github.com/monero-project/monero/blob/ad9956d9873ad8281fd88daf8b9202c74db3f796/src/blockchain_db/lmdb/db_lmdb.cpp#L481).

Maybe I'm wrong... I don't know. It's 10:30 PM here, and I'm just too tired.

Regards.



# Discussion History
## hyc | 2021-09-19T18:45:36+00:00
Note that `MDB_MAP_RESIZED` can only happen because some other process resized the DB. In most cases, monerod is the only thing with the DB open. 

## TheQuantumPhysicist | 2021-09-19T19:01:07+00:00
Is it strictly another process or also another thread?


## hyc | 2021-09-19T19:12:10+00:00
If I meant thread I would have said thread. Process.

## TheQuantumPhysicist | 2021-09-19T19:22:07+00:00
This deadlocked for me at that point (not in Monero though). There was only one process opening the database, which is the unit tests. Given that I don't understand how lmdb works as deep as you do, I can't explain this. I don't know.

## hyc | 2021-09-19T19:35:50+00:00
Your analysis looks correct. I just don't see why that error would occur in a single process test.

# Action History
- Created by: TheQuantumPhysicist | 2021-09-19T18:31:53+00:00
- Closed at: 2021-10-11T17:58:04+00:00
