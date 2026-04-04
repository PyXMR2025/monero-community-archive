---
title: Failed to add genesis block to blockchain
source_url: https://github.com/monero-project/monero/issues/5075
author: guile124
assignees: []
labels:
- invalid
created_at: '2019-01-15T21:21:34+00:00'
updated_at: '2019-01-21T08:01:28+00:00'
type: issue
status: closed
closed_at: '2019-01-21T08:01:28+00:00'
---

# Original Description
node genesis -a cryptonight -t "Born.............!"
It print waiting and:

2019-01-15 20:49:03.589      7f02d8923780  ERROR  cn  src/cryptonote_basic/cryptonote_format_utils.cpp:184  Failed to parse transaction from blob
2019-01-15 20:49:03.589      7f02d8923780  ERROR  default  src/cryptonote_core/cryptonote_tx_utils.cpp:659  failed to parse coinbase tx from hard coded blob
2019-01-15 20:49:03.590      7f02d8923780  ERROR  blockchain  src/cryptonote_core/blockchain.cpp:430  Failed to add genesis block to blockchain

# Discussion History
## moneromooo-monero | 2019-01-15T22:06:27+00:00
What is: node genesis -a cryptonight -t "Born.............!" ?

## guile124 | 2019-01-15T22:53:37+00:00
Is the genesis node generator,
From this repo: https://github.com/nasa8x/node-genesis-block

## moneromooo-monero | 2019-01-15T23:22:04+00:00
Then it seems to be a problem with that software.

## PabloB07 | 2019-01-15T23:53:49+00:00
> Then it seems to be a problem with that software.

We have a problem with or without node-gensis-block.. so you have another way to create a genesis? i've created a dummy tx but doesn't work.

## moneromooo-monero | 2019-01-16T00:27:08+00:00
The genesis block is created directly by the code. You should not have to somehow create one yourself. Start monerod and it will seed the new blockchain with the genesis block.

## PabloB07 | 2019-01-16T02:33:46+00:00
> The genesis block is created directly by the code. You should not have to somehow create one yourself. Start monerod and it will seed the new blockchain with the genesis block.

Any example.. please?. thanks.

## moneromooo-monero | 2019-01-16T11:14:19+00:00
It's in Blockchain::init, near this comment:
MINFO("Blockchain not loaded, generating genesis block.");
If it doesn't work when using Monero normally, then I can have a look, but for now I'll assume this is this other software that's breaking.


## ghost | 2019-01-16T23:18:52+00:00
Dude...why do you think anyone should help out a pump-and-dump coin project for free?

## PabloB07 | 2019-01-17T22:51:56+00:00
> Dude...why do you think anyone should help out a pump-and-dump coin project for free?

Do you have any problem with that?..

## moneromooo-monero | 2019-01-18T00:24:16+00:00
Are you asking if we have a problem with scammers ? :)

## PabloB07 | 2019-01-18T10:21:04+00:00
Well thanks for all @moneromooo-monero :) , the problem is not fixed anyways... :/

## moneromooo-monero | 2019-01-18T10:49:56+00:00
Well, if it's ours, it'll get fixed. But it seems to be some other software trrying to stuff an incorrect genesis block in there. Try dumping the genesis block, then comparing to the one you see on a monero block explorer. If it's the same, then it's a monero bug. If it's not the same, then it's a "other software" bug.

## PabloB07 | 2019-01-20T23:35:45+00:00
> Well, if it's ours, it'll get fixed. But it seems to be some other software trrying to stuff an incorrect genesis block in there. Try dumping the genesis block, then comparing to the one you see on a monero block explorer. If it's the same, then it's a monero bug. If it's not the same, then it's a "other software" bug.

Thanks, i try it! i closed this issue.

## dEBRUYNE-1 | 2019-01-21T07:59:36+00:00
+invalid

# Action History
- Created by: guile124 | 2019-01-15T21:21:34+00:00
- Closed at: 2019-01-21T08:01:28+00:00
