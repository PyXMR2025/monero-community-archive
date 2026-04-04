---
title: Invalid transactions are somehow reaching the daemon's tx pool resulting in
  rejected mined blocks.
source_url: https://github.com/monero-project/monero/issues/792
author: osensei
assignees: []
labels: []
created_at: '2016-04-03T20:32:46+00:00'
updated_at: '2016-05-10T12:34:36+00:00'
type: issue
status: closed
closed_at: '2016-05-10T12:34:36+00:00'
---

# Original Description
After the fork my mining pool found 2 blocks that were rejected by the daemon. At that time I had log level set to 0 so I couldn't get much info on the reason why they were rejected.

Then I restarted the mining pool and flushed the daemon's tx pool hoping for the best and it worked. The pool has found several blocks since then. My conclusion was that there must have been some pre-fork transactions still hanging there on the txpool and that the formed blocks were rejected because those transaction were invalid because of a low mixin.

Yesterday my daemon rejected a mined block again, but this time I had log level set to 1 and the reason was what I had guessed previously. Here is the log output:

```
2016-Apr-02 17:36:07.941034 [RPC0]transaction with hash 8c8f2a8a28b4493e0baae503b433a6159f4870bdbe324a473b5cd83b3f90fcda not found in db
2016-Apr-02 17:36:07.997365 [RPC0]Tx <8c8f2a8a28b4493e0baae503b433a6159f4870bdbe324a473b5cd83b3f90fcda> has too low mixin (0), and more than one mixable input with unmixable inputs
2016-Apr-02 17:36:07.997408 [RPC0]Block with id: <86ee04b009806e57411f108a036562bb39788a1e39e4a6dc028cb1e0007b19f5> has at least one transaction (id: <8c8f2a8a28b4493e0baae503b433a6159f4870bdbe324a473b5cd83b3f90fcda>) with wrong inputs.
2016-Apr-02 17:36:07.997736 [RPC0]BLOCK ADDED AS INVALID: <86ee04b009806e57411f108a036562bb39788a1e39e4a6dc028cb1e0007b19f5>, prev_id=<2f5aa2dd327e8d97a1928956c5f3bf5e5f45d5cab36425ee1539bfc2da72bc54>, m_invalid_blocks count=1
2016-Apr-02 17:36:07.997753 [RPC0]Block with id <86ee04b009806e57411f108a036562bb39788a1e39e4a6dc028cb1e0007b19f5> added as invalid because of wrong inputs in transactions
2016-Apr-02 17:36:07.999741 [RPC0]Tx <8c8f2a8a28b4493e0baae503b433a6159f4870bdbe324a473b5cd83b3f90fcda> has too low mixin (0), and more than one mixable input with unmixable inputs
2016-Apr-02 17:36:08.000252 [RPC0]ERROR /home/monero/bitmonero/src/cryptonote_core/cryptonote_core.cpp:741 mined block failed verification
2016-Apr-02 17:36:08.598435 [RPC1]Tx <8c8f2a8a28b4493e0baae503b433a6159f4870bdbe324a473b5cd83b3f90fcda> has too low mixin (0), and more than one mixable input with unmixable inputs
```

This is the print_pool_sh output for that transaction:

```
id: 8c8f2a8a28b4493e0baae503b433a6159f4870bdbe324a473b5cd83b3f90fcda
blob_size: 65862
fee: 0.650000000000
receive_time: 1459609526
kept_by_block: T
max_used_block_height: 1013514
max_used_block_id: 8567d8db974a8c2aa2d46b3a62e703781f3b97e4f13a7e3c8608b168ceb76d37
last_failed_height: 0
last_failed_id: 0000000000000000000000000000000000000000000000000000000000000000
```

And here it's the complete output of print_pool: [txpool.txt](https://github.com/monero-project/bitmonero/files/201538/txpool.txt)

Of course after seeing this I flushed the tx pool again, and just a few minutes later my pool found another block, which was accepted this time.


# Discussion History
## fluffypony | 2016-05-10T12:34:36+00:00
Fixes in #796 


# Action History
- Created by: osensei | 2016-04-03T20:32:46+00:00
- Closed at: 2016-05-10T12:34:36+00:00
