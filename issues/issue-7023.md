---
title: '"Failed to parse block from blob" after trying to use same datadir with GUI
  release'
source_url: https://github.com/monero-project/monero/issues/7023
author: leafcutterant
assignees: []
labels: []
created_at: '2020-11-16T19:32:54+00:00'
updated_at: '2021-10-06T03:05:31+00:00'
type: issue
status: closed
closed_at: '2021-10-06T03:05:31+00:00'
---

# Original Description
On Windows, I wanted to update from 0.17.1.0 or 0.17.1.1 CLI (non-installer), can't remember exactly. Since the currently available GUI version is higher than the currently available CLI, I went for the GUI version (0.17.1.4) and manually cut-pasted the contents to overwrite the files properly and preserve the CLI version's folder structure.

I started monerod with my usual operators (defining the p2p port and the datadir), but it crashed/exited in a few seconds. I deleted the whole application folder, downloaded the latest CLI (0.17.1.3) and tried to run it the same way. It crashed the same.

My bitmonero.log says this:

````
INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
INFO	global	src/daemon/main.cpp:293	Monero 'Oxygen Orion' (v0.17.1.3-release)
INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
INFO	global	src/daemon/core.h:63	Initializing core...
INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder C:\monero\datatdir\lmdb ...
ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:1345	Failed to parse block from blob
INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
ERROR	daemon	src/daemon/main.cpp:361	Exception in main! Failed to parse block from blob retrieved from the db
````

If I start monerod without specifying the datadir, it doesn't crash, it keeps running.

Any ideas on what happened and how to make this work **without having to re-download the whole blockchain**?

# Discussion History
## dEBRUYNE-1 | 2020-11-17T09:46:34+00:00
Can you try starting with the `--db-salvage` flag? 

## selsta | 2020-11-17T18:58:29+00:00
Is the blockchain stored on an external hard disk / usb stick?

## leafcutterant | 2020-11-17T19:32:54+00:00
> Can you try starting with the --db-salvage flag?

@dEBRUYNE-1 thank you, that worked! The sync is very slow, but that might be for other reasons. What matters is that it runs now. Should I keep using monerod with this flag?

> Is the blockchain stored on an external hard disk / usb stick?

@selsta yes, it is on an external drive, and monerod is also running from that drive. Does this affect anything?

## selsta | 2020-11-17T19:40:23+00:00
> Should I keep using monerod with this flag?

You only have to add this flag once to repair the database. Slow sync is most likely due to using an external drive.

> Does this affect anything?

It increases the chance of corruption because it is easy to unplug the hard disk during sync. If you are careful it should be fine.



## sumogr | 2020-11-17T20:40:33+00:00
go with --db-sync-mode safe:sync

## leafcutterant | 2020-11-18T00:52:49+00:00
> go with --db-sync-mode safe:sync

Thanks @sumogr. Any guesstimates as to how much does it slow down the sync? Or other tradeoffs I may not be aware of?

## selsta | 2021-10-06T03:05:31+00:00
Corrupted db, closing.

# Action History
- Created by: leafcutterant | 2020-11-16T19:32:54+00:00
- Closed at: 2021-10-06T03:05:31+00:00
