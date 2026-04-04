---
title: Testnet node does not start after new changes
source_url: https://github.com/monero-project/monero/issues/4363
author: moneroexamples
assignees: []
labels: []
created_at: '2018-09-12T03:09:03+00:00'
updated_at: '2018-09-13T23:42:23+00:00'
type: issue
status: closed
closed_at: '2018-09-12T23:53:38+00:00'
---

# Original Description
I just upgraded monero to the latest commits, and my testnet node does not start anymore. Guess its something to do with new BP. 

```
2018-09-12 03:06:52.339	    7f7bd7dc8080	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:439	Loading blockchain from folder /home/mwo/.bitmonero/testnet/lmdb ...
2018-09-12 03:06:52.401	    7f7bd7dc8080	INFO 	global	src/cryptonote_core/blockchain.cpp:455	Current top block <2bd42ca639373d2d7660c1d71d8dbf3bd30b78dd734e1d37433ddc32c10f8378> at height 1168598 has version 8 which disagrees with the ideal version 9
2018-09-12 03:06:52.401	    7f7bd7dc8080	INFO 	global	src/cryptonote_core/blockchain.cpp:457	Popping blocks... 1168598
2018-09-12 03:06:52.401	    7f7bd7dc8080	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:185	Failed to parse transaction from blob
2018-09-12 03:06:52.402	    7f7bd7dc8080	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:469	Error popping block from blockchain: Failed to parse transaction from blob retrieved from the db
2018-09-12 03:06:52.402	    7f7bd7dc8080	FATAL	daemon	src/daemon/daemon.cpp:195	Uncaught exception! Failed to parse transaction from blob retrieved from the db
```

What would be the solution? Should I re-sync to testnet from scratch? 


# Discussion History
## Gingeropolous | 2018-09-12T04:49:59+00:00
from irc earlier today

> <moneromooo> Pop blocks to 1057026 first, *before* pulling master.

you should really hangout there

## moneroexamples | 2018-09-12T06:06:10+00:00
Thanks. Tried popping, but also does not work. Will try re-syncing from scratch now. 

Yes, I will try visiting irc more:-)

## moneromooo-monero | 2018-09-12T08:17:55+00:00
Did you try popping *before* pulling ?

## moneroexamples | 2018-09-12T23:53:38+00:00
@moneromooo-monero 

No. Tried pooping after pulling. 

But its ok now. I re-synced from scratch and am at v9.

So I will close the issue now. Thanks.


## Gingeropolous | 2018-09-13T14:57:29+00:00
u said poop

## moneroexamples | 2018-09-13T23:42:23+00:00
@Gingeropolous 
Lol:-) Just noticed it. 

# Action History
- Created by: moneroexamples | 2018-09-12T03:09:03+00:00
- Closed at: 2018-09-12T23:53:38+00:00
