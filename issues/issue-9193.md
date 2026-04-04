---
title: 'database: Potential data race for mutual exclusion'
source_url: https://github.com/monero-project/monero/issues/9193
author: hinto-janai
assignees: []
labels:
- database
created_at: '2024-02-21T19:35:31+00:00'
updated_at: '2024-02-22T22:37:26+00:00'
type: issue
status: closed
closed_at: '2024-02-22T22:37:26+00:00'
---

# Original Description
## What
There may be a data race when needing to acquire mutual exclusive access to `monerod`'s database, e.g. when resizing.

## Invariant
When resizing LMDB's memory map, the caller must ensure they have mutual exclusive access to it.

As per [`mdb_env_set_mapsize()`](http://www.lmdb.tech/doc/group__mdb.html#gaa2506ec8dab3d969b0e609cd82e619e5) docs:
> This function [...] may be called at later times if no transactions are active in this process. Note that the library does not check for this condition, the caller must ensure it explicitly.

An error is returned if there are other write transactions and presumably UB will occur if read transaction(s) exist.

## Implementation
The solution to this was implemented in https://github.com/monero-project/monero/pull/289, and is still used today. My understanding of this code is:

There are 2 atomic values used to achieve mutual exclusive access to the database:

https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/blockchain_db/lmdb/db_lmdb.cpp#L354-L355

The atomic bool is used to indicate "do not enter, we are resizing". Before starting a transaction, this bool will be spinned on until it is `false`. It is set to `true` when LMDB is resizing:
https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/blockchain_db/lmdb/db_lmdb.cpp#L448-L451

When resizing, this prevents _new_ transactions from starting.

To handle _currently_ active transactions, each transaction will `num_active_txns++` after successfully passing the atomic bool, and will `num_active_txns--` when done. The thread resizing will spin until `num_active_txns` is 0, indicating there are no more transactions:

https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/blockchain_db/lmdb/db_lmdb.cpp#L453-L456

Now, with no new transactions allowed, and all current ones gone, we _should_ have mutual exclusive access to the database and resizing should be OK.

## Problem
2 atomic operations back-to-back are not atomic. Other threads are free to execute in-between 2 atomic operations. What may occur in the above implementation is such:
```text
  Thread 1 (resizing)                             Thread 2 (normal read tx)
          |                                                 |
          |                                                 |
          |                                           lmdb_txn_begin()
          |                                     "not resizing, OK to start tx"
  prevent_new_txns()                                        |
"no new tx's can start"                                     |
          |                                                 |
 wait_no_active_txns()                                      |
  "spin until 0 tx's"                                       |
          |                                          num_active_txns++
          |                                                 |
 mdb_env_set_mapsize()   <--- ⚠️ unsafe ⚠️ --->   start_doing_tx_stuff()
``` 
There is space in-between `Thread 2` succesfully entering a transaction and updating `num_active_txns`.

If `Thread 2` is scheduled out by the OS after `lmdb_txn_begin()` but before `num_active_txns++` (unlikely but non-zero chance) `Thread 1` will incorrectly assume it has mutual exclusive access and start the resize.

https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/blockchain_db/lmdb/db_lmdb.cpp#L606-L608

Some crashes occurring near a resize that could be explained by this:
- https://github.com/monero-project/monero/issues/2851
- https://github.com/monero-project/monero/issues/2911
- https://github.com/monero-project/monero/issues/3230

# Discussion History
## 0xFFFC0000 | 2024-02-22T08:31:12+00:00
In case you use `blockchain.cpp` to interact with `db_lmdb.cpp`, [9181](https://github.com/monero-project/monero/pull/9181) does fix this. Since no read transaction can start while there is a `write` transaction going on, and `write` transactions cannot start until acquires an exclusive lock on db.

## vtnerd | 2024-02-22T18:25:24+00:00
@hinto-janai I believe you mis-read the code:
```c++
while (creation_gate.test_and_set());
   num_active_txns++;
   creation_gate.clear();
```
Thread1 is blocked from advancing until `creation_gate.clear()` is called. This is basically just a spin mutex protecting `num_active_txns`.

The patch by @0xFFFC0000 is likely overkill, and not needed (that's just my knee-jerk reaction at this point).

## selsta | 2024-02-22T18:29:12+00:00
@vtnerd this isn't related to this specific issue but sometimes when there is heavy RPC traffic it's possible that the node can't add new blocks and falls behind due to the current locking mechanism. moneromooo suggested a while ago that a rw lock would help here.

## vtnerd | 2024-02-22T18:29:58+00:00
And to describe why the example doesn't work as @hinto-janai suggested - `lmdb_txn_begin()` should have `creation_gate` as `true`, so Thread1 is blocked in `prevent_new_txs` because the prior value is `true` until after `num_active_txns++` is modified.

## vtnerd | 2024-02-22T18:35:33+00:00
> @vtnerd this isn't related to this specific issue but sometimes when there is heavy RPC traffic it's possible that the node can't add new blocks and falls behind due to the current locking mechanism. moneromooo suggested a while ago that a rw lock would help here.

Yes, this may have some resource starvation issues since it's a dirty spin lock instead of some queued lock. But there is no data race afaik.

I'm not certain that #9181 fixes this though, I think the original spin lock code would have to be removed as well.

## 0xFFFC0000 | 2024-02-22T18:40:14+00:00

> The patch by @0xFFFC0000 is likely overkill, and not needed (that's just my knee-jerk reaction at this point).

I believe if you read the PR *carefully*,  you will realize that PR is addressing another issue. As a side-effect, it does solve the data race problem on `lmdb_db` too if you are accessing `lmdb` via blockchain.cpp APIs. 

If you want to go into more technical depth, I am happy to do it :)

## vtnerd | 2024-02-22T18:42:18+00:00
> I'm not certain that https://github.com/monero-project/monero/pull/9181 fixes this though, I think the original spin lock code would have to be removed as well.

Scratch that, #9181 probably works, but we just wasting cycles on atomic operations.

## vtnerd | 2024-02-22T18:45:12+00:00
@0xFFFC0000 well there is no data race where @hinto-janai describes, so you are saying there is yet another one? I'm doubting this as well, but sure why not enlighten me.

## 0xFFFC0000 | 2024-02-22T18:56:24+00:00
> @0xFFFC0000 well there is no data race where @hinto-janai describes, so you are saying there is yet another one? I'm doubting this as well, but sure why not enlighten me.

I did *specifically* talk about rw access from `blockchain.cpp`. 

About the data race, directly from `lmdb_db`, as hinto explains in his comment, I have not tried to prove (or disprove) it either. 

Keep in mind, if you are interacting with `lmdb_db` via `blockchain.cpp`,  that data race cannot happen due to `rwlock`.

Though I am tracking you and @hinto-janai discussion, to understand the situation. 

## vtnerd | 2024-02-22T18:58:36+00:00
And sorry for being a bit rude, I'm just crabby that I have to review this DB change :/

## 0xFFFC0000 | 2024-02-22T19:03:07+00:00
> And sorry for being a bit rude, I'm just crabby that I have to review this DB change :/

No no, I didn't even realize or notice anything rude from you :)

We were just discussing technical matters as always. Don't mention it at all. Looking forward to continuing our discussion. Because (possibility of) data race is a multi-level issue, we have to address it.  

## hyc | 2024-02-22T19:08:12+00:00
@vtnerd is correct in his first reply https://github.com/monero-project/monero/issues/9193#issuecomment-1960019411. Because of the first `creation_gate.test_and_set()` when `mdb_txn_safe` begins, `prevent_new_txns()` cannot proceed until the `creation_gate.clear()`. There is no race there.

## vtnerd | 2024-02-22T19:12:00+00:00
@0xFFFC0000 is this about the potential starvation issue that @selsta mentioned or some other data race? I still don't know why #9181 was created (perhaps the discussion should move to that PR). It sounds like #9181 was **not** created due to the specific issue referenced by @hinto-janai in this issue.

## 0xFFFC0000 | 2024-02-22T19:14:46+00:00
> It sounds like #9181 was **not** created due to the specific issue referenced by @hinto-janai in this issue.

Exactly, the 9181 is for a different issue. But a side-effect of that locking is, as I mentioned in my [first comment](https://github.com/monero-project/monero/issues/9193#issuecomment-1958943358), _**if**_ there was a data race in `lmdb_db`, it would've not happened if you were accessing it via `Blockchain.cpp` APIs, since it does have its own locking mechanism. 

I am available to discuss it on the PR page.


## hinto-janai | 2024-02-22T22:37:26+00:00
@vtnerd Ah you are correct. I was looking at `lmdb_resized()` where that constructor doesn't run so the 2 atomics being checked appear like an ABA problem. Although, every transaction (in `db_lmdb.cpp` at least) seems to be guarded by `mdb_txn_safe` at some point in the call stack.

There's `BlockchainLMDB::do_resize()` which doesn't use `mdb_txn_safe` but seems like that's guarded by a lock.

# Action History
- Created by: hinto-janai | 2024-02-21T19:35:31+00:00
- Closed at: 2024-02-22T22:37:26+00:00
