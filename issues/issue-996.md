---
title: bitmonero_import crashes with latest blockchain.raw
source_url: https://github.com/monero-project/monero/issues/996
author: nicolaevladescu
assignees: []
labels: []
created_at: '2016-08-28T08:14:49+00:00'
updated_at: '2016-08-28T11:07:58+00:00'
type: issue
status: closed
closed_at: '2016-08-28T11:05:46+00:00'
---

# Original Description
Hello.

I had a problem with one outgoing transfer, my pc crashed before bitmonerod could add it to the transaction queue ( i think ). After restart i was getting something like "Monero key/data pair already exists", using simplewallet "show_transfers" at first the transaction was pending, then at some point i had my balance back again, and the pending transaction was not listed anymore, then i had a 0 balance, and no history ( no inputs also ) in "show_transfers".

So i decided to delete the local blockchain and start from scratch. I downloaded blockchain.raw and started the import, left it over night, found it in the morning like this:

```
D:\monero-v0-9-4-0>blockchain_import.exe --data-dir D:\monero_data --input-file D:\monero_data\blockchain.raw
```

```
[- batch commit at height 1010000 -]

2016-Aug-28 05:25:44.031440 loading block number 1011000
2016-Aug-28 05:26:17.343563 loading block number 1012000
2016-Aug-28 05:27:02.541826 loading block number 1013000
2016-Aug-28 05:27:38.221870 loading block number 1014000
block 1014250 / 11224772016-Aug-28 05:27:55.614291 ERROR C:/msys64/DISTRIBUTION-
BUILD/src/cryptonote_core/blockchain.cpp:2757 Error adding block with hash: <faf14ddeef5a04d563615748da9555fe1a5506969bb6eae6ba7af04096695b3a> to blockchain, what = Error adding spent key image to db transaction: MDB_MAP_FULL: Environment mapsize limit reached
2016-Aug-28 05:27:55.614291 Error attempting to retrieve a block hash from the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2016-Aug-28 05:27:55.614291 exception while reading from file, height=1014252: Error attempting to retrieve a block hash from the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2016-Aug-28 05:27:55.614291 Failed to query m_blocks
terminate called after throwing an instance of 'cryptonote::DB_ERROR'
  what():  Failed to query m_blocks

This application has requested the Runtime to terminate it in an unusual way.
Please contact the application's support team for more information.

I don't want to lose my balance, should i start it again ?
```


# Discussion History
## nicolaevladescu | 2016-08-28T08:18:26+00:00
I just noticed `MDB_MAP_FULL: Environment mapsize limit reached`, i will check my disk space and comeback, that could be the culprit,


## moneromooo-monero | 2016-08-28T09:48:06+00:00
Disk space can be an issue there, yes. Another possible issue is running on 32 bit (this got fixed very recently). In any case, restarting blockchain_import will restart from the point where it was before the error.


## moneromooo-monero | 2016-08-28T09:49:05+00:00
Also, you can't lose coins since they're in the wallet, so you could mess up your blockchain as much as you want, the coins are safe as long as you don't involve your private key, which the daemon knows nothing about :)


## nicolaevladescu | 2016-08-28T10:17:29+00:00
Yes, thanks, i know that as long as i have inputs pointing to a public address derived from my private key, and i have my private key, i cannot lose the funds. Also a transfer can either be in the blockchain or not.

i'm just being double careful because it's a new coin for me, just making sure i understand everything, and also i am aware that bugs can happen to any coin's software stack, either new or established.

Restarted the import again and it crashed at block 1118168 with:

```
transaction already exists at inserting to memorypool
failed to add transaction to transaction pool, height=1118168, tx_num=2
```

Restarting again :)


## radfish | 2016-08-28T10:28:57+00:00
duplicate of #880 exact same place of failure

Btw, what system is this on? Windows 32-bit?


## nicolaevladescu | 2016-08-28T11:05:46+00:00
Windows 10 Home, 64bit

It synced, i used `rescan_bc` from simplewaller, everything is fine now, i'm closing.


## nicolaevladescu | 2016-08-28T11:07:58+00:00
After two errors ( stated above ) and retrying, the blockchain.raw got imported and i could start bitmonerod, then bitmonerod synced itself to the latest blocks.

After `rescan_bc` from `simplewallet` the balance is back, all errors gone.


# Action History
- Created by: nicolaevladescu | 2016-08-28T08:14:49+00:00
- Closed at: 2016-08-28T11:05:46+00:00
