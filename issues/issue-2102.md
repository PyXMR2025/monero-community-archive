---
title: monerod "stopped working" windows 10
source_url: https://github.com/monero-project/monero/issues/2102
author: owen358
assignees: []
labels:
- invalid
created_at: '2017-06-21T16:07:44+00:00'
updated_at: '2017-09-20T21:06:34+00:00'
type: issue
status: closed
closed_at: '2017-09-20T21:06:34+00:00'
---

# Original Description
I am trying to mine monero. The first step is to open monerod.  it didnt work from the command line. so i double clicked on monerod in the wondows explorer.  it started to sync but my computer turned off overnight so i am not sure if it completed or not. when i try to sync again it just says "stopped working" every time with no explanation or error message. how can i proceed. i am lost here and there seems to be no source of instructions online in spite of searching for hours. there are tutorials but none work for me. there is always an error which no one addresses, help is much appreciated.

# Discussion History
## moneromooo-monero | 2017-06-21T16:15:07+00:00
It is likely the OS crash corrupted the database. In that case, you'd have to remove it (it's called data.mdb), and monerod will restart syncing. If your computer restarts often, you may want to set monerod in db safe sync mode, which is much slower, but more resistant to windows, for instance: --db-sync-mode safe:async:5000


## owen358 | 2017-06-21T16:24:04+00:00
i searched in windows explorer for data.mdb but nothing came up. where is this file located?

## moneromooo-monero | 2017-06-21T16:36:59+00:00
I think it might be C:\ProgramData on windows ?

## owen358 | 2017-06-22T09:54:03+00:00
that worked. i am now syncing the blockchain. however i have another problem. i was supposed to type this command before starting th emonerod.

" C:\monero>monero-blockchain-import.exe --verify 0 --input-file ./blockchain.raw"

since it took a couple of hours to download i forgot and started monerod before doing this.  does this matter if i do it after and not before?
 when i type the above command i get the following error?

'monero-blockchain-import.exe' is not recognized as an internal or external command,
operable program or batch file.

do i need to start the whole process again from scratch? (at this point the blockchain has almost finished syncing)

## moneromooo-monero | 2017-06-22T10:12:01+00:00
This is a bug tracker, not a support chat. Try #monero on freenode, reddit, etc.

## moneromooo-monero | 2017-09-20T21:01:19+00:00
+invalid

# Action History
- Created by: owen358 | 2017-06-21T16:07:44+00:00
- Closed at: 2017-09-20T21:06:34+00:00
