---
title: Potential soft fork issue
source_url: https://github.com/monero-project/monero/issues/6620
author: VanGrx
assignees: []
labels: []
created_at: '2020-06-02T15:53:56+00:00'
updated_at: '2020-07-10T12:08:42+00:00'
type: issue
status: closed
closed_at: '2020-07-10T12:08:41+00:00'
---

# Original Description
Hello,
I am worried about [this handling of exceptions.](https://github.com/monero-project/monero/blob/master/src/cryptonote_core/blockchain.cpp#L3996-L4012)

If a transaction failed here, the txs before the one that failed(and miner tx also) is not removed from the blockchain so that node becomes invalid for the rest of the network.

# Discussion History
## moneromooo-monero | 2020-06-02T22:47:56+00:00
If either trigger, this is run:

> m_batch_success = false;

In cleanup_handle_incoming_blocks, if this flag is false, this is run:

> m_db->batch_abort();

which will abort the db txn, so anything tentatively written to the db is discarded.

Do you think there's bug which can make this discard not happen ? If so, can you be more precise ?


## VanGrx | 2020-06-05T16:24:33+00:00
Hello,
Thanks for reply!
Sorry, I checked again and here is [a potential problem that I found.](https://github.com/monero-project/monero/blob/master/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1477)
As this is the only place where the cleanup is not called right after the handle_incoming_block function it seems like a potential theoretical problem for soft fork. Right?



## moneromooo-monero | 2020-06-05T17:11:50+00:00
Looks like it's called in all cases. Maybe not if an exception happens in the connection dropping or logging I suppose, so some armour plating could be added. Can you see a path where it's not called ?

## VanGrx | 2020-06-05T17:48:36+00:00
[This](https://github.com/monero-project/monero/blob/master/src/cryptonote_protocol/block_queue.cpp#L95) is the assert that I found while doing connection dropping. 

Is there a reason why cleanup is not called right after the handle_incoming_block but actually added in every case of ifs?

## moneromooo-monero | 2020-06-05T18:20:00+00:00
Oooh, that's bad. Aby more info about this assert, like logs ?

The reason why it's not called right after adding is that if you call one block at a time, all the db stuff be slow I think. Batching blocks speeds up.

As for the exception, it looks like it should not leave the db in a bad state: if cleanup is not called, the incoming tx stays locked, and the next call locks up. Meanwhile, the interrupted db txn never gets committed either.

Did you end up with a bad db ?



## VanGrx | 2020-06-09T11:14:55+00:00
`Did you end up with a bad db ?`
Actually no, I am working on a project that is based on monero codebase, so after finding some project-specific issue, I took some time to check if monero project has some theoretical potential issues and wanted to give help to this project if possible. :)

## moneromooo-monero | 2020-06-09T16:32:43+00:00
Appreciated :)

The assert is definitely a bug if you get more info about it.
As for the tx being leftover in the db, I don't think that can happen but if you find a way, please tell.


## moneromooo-monero | 2020-07-08T22:56:24+00:00
I'll be closing this soon if you don't come up with an actual way for it to happen. If you're planning to look into it some more, say so and I'll leave it open.

## VanGrx | 2020-07-10T12:08:41+00:00
I don't think I'll check this more any time soon. I'll close it and when I get time, I'll open an issue with more accurate info. Thank You for all the feedback.

# Action History
- Created by: VanGrx | 2020-06-02T15:53:56+00:00
- Closed at: 2020-07-10T12:08:41+00:00
