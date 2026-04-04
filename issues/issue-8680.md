---
title: 'Daemon dont synchronize '
source_url: https://github.com/monero-project/monero/issues/8680
author: GottMitUns
assignees: []
labels: []
created_at: '2022-12-16T17:36:43+00:00'
updated_at: '2023-09-21T17:24:35+00:00'
type: issue
status: closed
closed_at: '2023-09-21T17:24:35+00:00'
---

# Original Description
```
[16/12/2022 14:32] 2022-12-16 17:32:57.650 I Monero 'Fluorine Fermi' (v0.18.1.2-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
```


# Discussion History
## selsta | 2022-12-16T17:38:58+00:00
Please post more information about what exactly you are trying to do and what issues you have.

## GottMitUns | 2022-12-16T18:30:18+00:00
> 

I am trying to synchronize DAEMON 

![image](https://user-images.githubusercontent.com/84939709/208164995-afff84b3-b375-41ac-a6a5-6e6de242d731.png)


![image](https://user-images.githubusercontent.com/84939709/208165043-750cf7b9-4de1-4e29-b153-77a91317681f.png)

Translate:

"Please verify the log of your wallet and daemon..."


## selsta | 2022-12-16T18:37:25+00:00
Did it work in the past and suddenly break? Or did it never start to sync?

## GottMitUns | 2022-12-16T18:40:10+00:00
> 

Suddenly it broke, I turned on the computer and went to sync and it doesn't sync anymore.

## selsta | 2022-12-16T18:45:30+00:00
Did you force shutdown your computer during sync? For example because of power loss? It sounds like your blockchain is corrupted.

## GottMitUns | 2022-12-16T18:46:11+00:00
> 

Yes, was because a power loss yesterday.

## selsta | 2022-12-16T18:50:43+00:00
You have to delete the blockchain and sync from scratch. It is corrupted. If you often have power loss issues you have to add `--db-sync-mode safe` into the "Variáveis de arranque do daemon" field here, then it won't corrupt but it will also take longer to sync: 
![](https://user-images.githubusercontent.com/84939709/208164995-afff84b3-b375-41ac-a6a5-6e6de242d731.png)


## trasherdk | 2022-12-19T10:33:30+00:00
My `Compaq T8100` is shutting down all the time, `Nouveau GPU core` overheating, and that's a hard crash :rofl: 

This have never caused the database to corrupt. It's running `Slackware64 15.0`

## afungible | 2022-12-21T02:48:36+00:00
Some ways out:

1) Start fresh, close all monero related process and do,
`./monerod --db-salvage --data-dir path\to\data.mdb` (blockchain file is the data.mdb file, see below)
This will try to synchronize the blockchain file
 
OR

2) Go to:
LINUX: `cd ~/.bitmonero/lmdb/`
WINDOWS: `"C:\ProgramData\bitmonero\lmdb" `
Find and delete the `data.mdb` file.
Open the Monero GUI, it will start to sync again (fresh)


## afungible | 2022-12-21T02:51:01+00:00
@GottMitUns 
Found this. Spend 5 minutes to read this carefully:
https://monero.stackexchange.com/questions/6825/i-am-using-the-gui-and-my-daemon-doesnt-start-anymore

# Action History
- Created by: GottMitUns | 2022-12-16T17:36:43+00:00
- Closed at: 2023-09-21T17:24:35+00:00
