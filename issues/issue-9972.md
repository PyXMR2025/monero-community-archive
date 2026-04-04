---
title: System crashed overnight, blockchain (seemingly) corrupted
source_url: https://github.com/monero-project/monero/issues/9972
author: GanerCodes
assignees: []
labels:
- question
created_at: '2025-06-28T14:21:55+00:00'
updated_at: '2025-10-11T20:32:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
$ /mnt/cunk/Crypto/Monero ✝ monerod --log-level 4 --data-dir /mnt/cunk/Crypto/Monero/ --block-sync-size 20

2025-06-28 14:20:10.967	I Monero 'Fluorine Fermi' (v0.18.4.0-release)
2025-06-28 14:20:10.968	I Moving from main() into the daemonize now.
2025-06-28 14:20:10.968	I Initializing cryptonote protocol...
2025-06-28 14:20:10.968	I Cryptonote protocol initialized OK
2025-06-28 14:20:10.968	T Blockchain::Blockchain
2025-06-28 14:20:10.968	I Initializing core...
2025-06-28 14:20:10.968	T BlockchainLMDB::BlockchainLMDB
2025-06-28 14:20:10.968	T BlockchainLMDB::get_db_name
2025-06-28 14:20:10.969	I Loading blockchain from folder /mnt/cunk/Crypto/Monero/lmdb ...
2025-06-28 14:20:10.969	D option: fast
2025-06-28 14:20:10.969	D option: async
2025-06-28 14:20:10.969	D option: 250000000bytes
2025-06-28 14:20:10.969	T BlockchainLMDB::open
2025-06-28 14:20:10.969	W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2025-06-28 14:20:10.969	T BlockchainLMDB::need_resize
2025-06-28 14:20:10.969	D DB map size:     274620592128
2025-06-28 14:20:10.969	D Space used:      246954536960
2025-06-28 14:20:10.969	D Space remaining: 27666055168
2025-06-28 14:20:10.969	D Size threshold:  0
2025-06-28 14:20:10.969	D Percent used: 89.9257  Percent threshold: 90.0000
2025-06-28 14:20:10.969	D Setting m_height to: 3441341
malloc(): unaligned tcache chunk detected
Aborted
```

here's some GDB info that's over my head

![Image](https://github.com/user-attachments/assets/2890f3f5-25a9-4189-b76d-7036562f3c01)

besides fixing this issue in the general case, is there any "hacks" i can use to like, delete the last few hundred entries from the db or something? my internet is not fast so 230GB can be multiple days

# Discussion History
## nahuhh | 2025-06-28T15:09:21+00:00
Looks like your drive is out of space?

## GanerCodes | 2025-06-28T22:56:17+00:00
> Looks like your drive is out of space?

nope only 52% used

## nahuhh | 2025-06-28T22:59:37+00:00
Try starting with --db-salvage

## GanerCodes | 2025-06-29T01:37:53+00:00
> Try starting with --db-salvage

tried that already, it just exits wthout saying anything and the problem persists

## x64x2 | 2025-06-29T03:41:22+00:00
> > Try starting with --db-salvage
> 
> tried that already, it just exits wthout saying anything and the problem persists

compatability issues

## GanerCodes | 2025-06-29T07:31:31+00:00
> compatability issues

?

## GanerCodes | 2025-06-29T17:05:51+00:00
ok actually i got it to say something
```
/mnt/cunk/Crypto/Test/lmdb ✝ monerod --db-salvage --log-level 4 --data-dir /mnt/cunk/Crypto/Test
2025-06-29 17:07:27.652	I Monero 'Fluorine Fermi' (v0.18.4.0-release)
2025-06-29 17:07:27.652	I Moving from main() into the daemonize now.
2025-06-29 17:07:27.652	I Initializing cryptonote protocol...
2025-06-29 17:07:27.652	I Cryptonote protocol initialized OK
2025-06-29 17:07:27.653	T Blockchain::Blockchain
2025-06-29 17:07:27.653	I Initializing core...
2025-06-29 17:07:27.653	T BlockchainLMDB::BlockchainLMDB
2025-06-29 17:07:27.653	T BlockchainLMDB::get_db_name
2025-06-29 17:07:27.653	I Loading blockchain from folder /mnt/cunk/Crypto/Test/lmdb ...
2025-06-29 17:07:27.653	D option: fast
2025-06-29 17:07:27.653	D option: async
2025-06-29 17:07:27.653	D option: 250000000bytes
2025-06-29 17:07:27.653	T BlockchainLMDB::open
2025-06-29 17:07:27.653	W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2025-06-29 17:07:27.654	T BlockchainLMDB::need_resize
2025-06-29 17:07:27.654	D DB map size:     274620592128
2025-06-29 17:07:27.654	D Space used:      246954475520
2025-06-29 17:07:27.654	D Space remaining: 27666116608
2025-06-29 17:07:27.654	D Size threshold:  0
2025-06-29 17:07:27.654	D Percent used: 89.9257  Percent threshold: 90.0000
2025-06-29 17:07:28.450	W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2025-06-29 17:07:28.451	T mdb_txn_safe: destructor
2025-06-29 17:07:28.451	T mdb_txn_safe: m_txn not NULL in destructor - calling mdb_txn_abort()
2025-06-29 17:07:28.451	E Error opening database: Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2025-06-29 17:07:28.451	T BlockchainLMDB::~BlockchainLMDB
2025-06-29 17:07:28.451	T Miner has received stop signal
2025-06-29 17:07:28.451	T Not mining - nothing to stop
2025-06-29 17:07:28.451	T Blockchain::deinit
2025-06-29 17:07:28.451	T Stopping blockchain read/write activity
2025-06-29 17:07:28.451	I Stopping cryptonote protocol...
2025-06-29 17:07:28.451	I Cryptonote protocol stopped successfully
2025-06-29 17:07:28.451	E Exception in main! Failed to initialize core
```

## atoi2008 | 2025-08-14T01:20:53+00:00
try using db-sync-mode=safe:sync

> In the event of a system crash or power failure, the (default) fast:async:* mode can result in a corrupted blockchain. It should not corrupt if just monerod crashes. If you are concerned with system crashes, use safe:sync.

see docs here [https://docs.getmonero.org/interacting/monerod-reference/#performance](https://docs.getmonero.org/interacting/monerod-reference/#performance)

## nahuhh | 2025-08-14T03:24:11+00:00
> try using db-sync-mode=safe:sync

Monerod switches to safe:sync autonatically when within, iirc, 5 blocks of the chain tip

> > In the event of a system crash or power failure, the (default) fast:async:* mode can result in a corrupted blockchain. It should not corrupt if just monerod crashes. If you are concerned with system crashes, use safe:sync.
> 
> see docs here [https://docs.getmonero.org/interacting/monerod-reference/#performance](https://docs.getmonero.org/interacting/monerod-reference/#performance)



## Kenneth142006 | 2025-09-02T13:53:27+00:00
so what the solution

## nahuhh | 2025-09-02T14:05:34+00:00
Resync

## atoi2008 | 2025-09-04T23:43:40+00:00
Delete the database and resync. Find a bootstrap to save on download time

On Tue, Sep 2, 2025, 7:05 AM nahuhh ***@***.***> wrote:

> *nahuhh* left a comment (monero-project/monero#9972)
> <https://github.com/monero-project/monero/issues/9972#issuecomment-3245506829>
>
> Resync
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/9972#issuecomment-3245506829>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AB53Y4ZPUZTWOOT5VZC3IB33QWP4LAVCNFSM6AAAAACAK7DOB6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTENBVGUYDMOBSHE>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


## Kenneth142006 | 2025-10-07T22:37:43+00:00
any blockchain developer am buidling a project and i need a blockchain developer

## atoi2008 | 2025-10-08T05:15:22+00:00
How can I help you?

On Tue, Oct 7, 2025, 3:38 PM BGC Network ***@***.***> wrote:

> *Kenneth142006* left a comment (monero-project/monero#9972)
> <https://github.com/monero-project/monero/issues/9972#issuecomment-3378942674>
>
> any blockchain developer am buidling a project and i need a blockchain
> developer
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/9972#issuecomment-3378942674>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AB53Y42GDEKLHRR7MWVFDBD3WQ6E3AVCNFSM6AAAAACAK7DOB6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTGNZYHE2DENRXGQ>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


## Kenneth142006 | 2025-10-11T20:31:42+00:00
> How can I help you?
> […](#)

I want a blockchain developer that we can work together to build a blockchain fork monero and new features we can discuss privately

# Action History
- Created by: GanerCodes | 2025-06-28T14:21:55+00:00
