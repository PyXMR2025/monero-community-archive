---
title: Permission error
source_url: https://github.com/monero-project/monero/issues/4829
author: ismaelbouyaf
assignees: []
labels: []
created_at: '2018-11-09T06:15:51+00:00'
updated_at: '2018-11-09T09:41:28+00:00'
type: issue
status: closed
closed_at: '2018-11-09T09:41:28+00:00'
---

# Original Description
When upgrading to version v0.13.0.4, the monero-blockchain tools on the previous database version stopped working:
```
$ ../monero/bin/monero-blockchain-export --data-dir $HOME/.no_backup/monerod/ --output-file $HOME/.no_backup/monerod/lmdb/foo.mdb --block-stop 1685554
2018-11-08 23:52:15,104 INFO  [default] Page size: 4096                                                                                                                                                                                       
2018-11-08 23:52:15.106     7fc7de795bc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:112      Starting...                                                                                                           
2018-11-08 23:52:15.106     7fc7de795bc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:138      Export output file: /home/immae/.no_backup/monerod/lmdb/foo.mdb                                                       
2018-11-08 23:52:15.106     7fc7de795bc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:151      Initializing source blockchain (BlockchainDB)                                                                         
2018-11-08 23:52:15.107     7fc7de795bc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:162      database: lmdb                                                                                                        
2018-11-08 23:52:15.107     7fc7de795bc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:168      Loading blockchain from folder /home/immae/.no_backup/monerod/lmdb ...                                                
2018-11-08 23:52:15.107     7fc7de795bc0        WARN    global  src/blockchain_db/lmdb/db_lmdb.cpp:1211 The blockchain is on a rotating drive: this will be very slow, use a SSD if possible                                                  
2018-11-08 23:52:15.107     7fc7de795bc0        INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:4213 Migrating blockchain from DB version 2 to 3 - this may take a while:                                                                  
2018-11-08 23:52:15.107     7fc7de795bc0        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   Failed to create a transaction for the db: Permission denied                                                          
2018-11-08 23:52:15.108     7fc7de795bc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:175      Error opening database: Failed to create a transaction for the db: Permission denied                                  
```
The error was the same with monero-blockchain-usage.

Every command was run with the same user (mine), and the permissions were correct. A run with `strace` shows no permission error (every open successes).

After deleting data.mdb and lock.mdb and resyncing from scratch, the same commands ran without any error.

I’ll keep the old database a few days if it can be of any help.

# Discussion History
## moneromooo-monero | 2018-11-09T08:53:13+00:00
You ran the exact same thing, once with strace and once without, the on with strace worked, and the one without strace did not ?

## ismaelbouyaf | 2018-11-09T08:57:35+00:00
No, sorry : 
- From the old database, I always get the "Permission denied", with or without strace. I ran strace to try to find out which file he was attempting to open, and saw that no "open" failed in the strace, so I have no clue of which "Permission denied" he’s complaining about.

- From the new database (after removing data.mdb and lock.mdb), everything works smoothly after resync.

## moneromooo-monero | 2018-11-09T08:58:13+00:00
Any other syscall gets you EPERM near the end ?

## ismaelbouyaf | 2018-11-09T09:06:15+00:00
No EPERM in the file.

However I just found out a possible cause of the problem.

It looks like he’s trying to open `$HOME/.no_backup/monerod/data.mdb` instead of `$HOME/.no_backup/monerod/lmdb/data.mdb`
But if I change the data-dir argument to `$HOME/.no_backup/monerod/lmdb`, he complains now that he cannot find files in `$HOME/.no_backup/monerod/lmdb/lmdb` : 
```
$ ../monero/bin/monero-blockchain-export --data-dir $HOME/.no_backup/monerod/lmdb --output-file $HOME/.no_backup/monerod/lmdb/foo.mdb --block-stop 1685554
2018-11-09 09:02:51,488 INFO  [default] Page size: 4096
2018-11-09 09:02:51.496     7fb8b958bbc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:112      Starting...
2018-11-09 09:02:51.496     7fb8b958bbc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:138      Export output file: /home/immae/.no_backup/monerod/lmdb/foo.mdb
2018-11-09 09:02:51.497     7fb8b958bbc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:151      Initializing source blockchain (BlockchainDB)
2018-11-09 09:02:51.499     7fb8b958bbc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:162      database: lmdb
2018-11-09 09:02:51.499     7fb8b958bbc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:168      Loading blockchain from folder /home/immae/.no_backup/monerod/lmdb/lmdb ...
2018-11-09 09:02:51.499     7fb8b958bbc0        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1202 Found existing LMDB files in /home/immae/.no_backup/monerod/lmdb
2018-11-09 09:02:51.500     7fb8b958bbc0        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1203 Move data.mdb and/or lock.mdb to /home/immae/.no_backup/monerod/lmdb/lmdb, or delete them, and then restart
2018-11-09 09:02:51.502     7fb8b958bbc0        WARN    bcutil  src/blockchain_utilities/blockchain_export.cpp:175      Error opening database: Database could not be opened
```

## ismaelbouyaf | 2018-11-09T09:09:28+00:00
attached: the strace for `-data-dir $HOME/.no_backup/monerod/`
[strace.txt](https://github.com/monero-project/monero/files/2565251/strace.txt)



## moneromooo-monero | 2018-11-09T09:16:08+00:00
It's fine. Just remove those files in the wrong place. Any EACCES in the strace log (there's none in the one you posted) ?

## ismaelbouyaf | 2018-11-09T09:19:12+00:00
No, you have the whole strace log (only a ENOENT when he tries to access /.../monerod/data.mdb instead of /.../monerod/lmdb/data.mdb )

## ismaelbouyaf | 2018-11-09T09:21:07+00:00
and their intended place is /.../monerod/lmdb (might not be the default).
Note however that the error doesn’t come if I restart the sync from scratch (same location), so it’s probably something with the fact that it’s an old version of the database?

## moneromooo-monero | 2018-11-09T09:22:02+00:00
Then the remaining thing is trying to write to a read only db or with a read only tx. Which it might do if trying to convert before export).

## moneromooo-monero | 2018-11-09T09:23:04+00:00
So run monerod, which should convert it, then export again. But that kinda implies you're trying to export with a more recent monero version that what you're otherwise running, which is odd.

## ismaelbouyaf | 2018-11-09T09:25:54+00:00
The database was created with the old version, and I tried to export with the new one yes.

I expected maybe wrongly that the tools would be able to load old versions of the database

## ismaelbouyaf | 2018-11-09T09:27:09+00:00
the steps I wanted to do was:
- stop old monerod
- update the monero binaries
- export the database and truncate the incorrect blocs since the hard fork
- start new monerod

which was maybe not the expected steps

## ismaelbouyaf | 2018-11-09T09:27:47+00:00
If it was not the intended step, I guess we can close the issue as non-relevant

## moneromooo-monero | 2018-11-09T09:31:42+00:00
monerod should now auto update and discard the "old chain" blocks.
Anyway, I'm adding a check for this case to error out with an explanatory message.

## ismaelbouyaf | 2018-11-09T09:33:45+00:00
oh, thanks for the information, I didn’t know about it. This will make the future upgrades easier :)

## moneromooo-monero | 2018-11-09T09:40:16+00:00
https://github.com/monero-project/monero/pull/4830

## ismaelbouyaf | 2018-11-09T09:41:28+00:00
:clap:

# Action History
- Created by: ismaelbouyaf | 2018-11-09T06:15:51+00:00
- Closed at: 2018-11-09T09:41:28+00:00
