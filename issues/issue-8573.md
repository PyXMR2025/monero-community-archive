---
title: 'When syncing blockchain "Error in handle_invoke_map: std::bad_alloc"'
source_url: https://github.com/monero-project/monero/issues/8573
author: Akmoniades
assignees: []
labels: []
created_at: '2022-09-18T19:45:32+00:00'
updated_at: '2023-01-05T01:40:12+00:00'
type: issue
status: closed
closed_at: '2023-01-05T01:35:50+00:00'
---

# Original Description
I'm currently running OpenBSD 7.1 and followed the instructions in the Readme.  The installation seems to complete just fine, but when syncing the blockchain, I get the following: 

```
Error in handle_invoke_map: std::bad_alloc
Exception at [portable_storage::load_from_binary], what=std::bad_alloc
```
The second line of this error message repeats until I sigterm the terminal.  This has happened when I have deleted the blockchain and started over, and I have even tried reinstalling a few times without any success.  I looked through the repo issues to see if anyone had raised this before.   Those seemed to be related to either insufficient RAM or an outdated Boost version.   I have 16GB of RAM on my machine, and my current Boost version is 1.78.00 (which is the version currently in the OpenBSD repos). 

Do you know what my issue might be?  If this is a RAM Issue, is there a flag I could pass to limit it? 


# Discussion History
## selsta | 2022-09-18T23:15:12+00:00
How long does it take until this issue shows up?

## Akmoniades | 2022-09-21T17:59:53+00:00
Sorry for the delay in my reply. 

> How long does it take until this issue shows up?

It happens almost always when the blockchain is almost finished syncing (usually at 97% or 98%).  Is that significant?  

If I try to reboot and start the daemon again where it left off, I get the error: 

`Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type you may want to start with --db-salvage`

And if I try `monerod --db-salvage`, I get:

```
W Failed to commit a transaction to the db: MDB_CORRUPTED: Located page was wrong type.

E Error opening database: Failed to commit a transaction to the DB: MBD_CORRUPTED: Located page was wrong type

I Stopping cryptonote protocol . . . 

I Cryptonote protocol stopped successfully

E Exception in main! Failed to initialize core

```

I've just been deleting the blockchain and starting over again, but the same thing keeps happening.

## Akmoniades | 2022-09-22T13:33:46+00:00
Update: I managed to get the entire blockchain to sync to 100% (with the same std::bad_alloc error during sync, which I ignored).  But now I get the following error when trying to start the daemon: 

```

W Attempt to get block from height 2715573 failed - - block not in db

I Stopping cryptonote protocol

I Cryptonote protocol stopped successfully

E Exception in main! Attempt to get block from height 2715573 failed - - block not in db
```

## offshoremonero | 2022-11-30T07:26:03+00:00
Are you running it with blockchain pruning on?

## Akmoniades | 2023-01-05T01:35:50+00:00
Sorry.  I hadn't logged into Github in a while.  

Yes, I was running it with blockchain pruning on.  I tried redownloading the blockchain without pruning, but it segfaulted before finishing the full download (several times).

Ultimately, the way I fixed it was rebooting, not pruning, and whenever it segfaulted, I rebooted and picked up where I left off.  After about 4-5 reboots, it synced.  I did eventually get it synced.

# Action History
- Created by: Akmoniades | 2022-09-18T19:45:32+00:00
- Closed at: 2023-01-05T01:35:50+00:00
