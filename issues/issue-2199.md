---
title: Solo mining error or generated a bad new genesis tx
source_url: https://github.com/monero-project/monero/issues/2199
author: loldlm1
assignees: []
labels: []
created_at: '2017-07-24T14:56:30+00:00'
updated_at: '2018-06-03T10:56:51+00:00'
type: issue
status: closed
closed_at: '2017-08-08T11:00:15+00:00'
---

# Original Description
I did a Monero fork and i added to it a code to generate for me a new genesis tx with the knowed command `--print-genesis-tx` and it works great at start, it generates something like this `013c01ff000180cab5ee01029b2e4c0281c0b02e7c53291a94d1d0cbff8883f8024f5142ee494ffbbd08807121015b6c9c53d57e60a1283edfba1d2a6510c922f351d86c7f537de64082fdb76110` but if a try to do a solo mining i get this:

```
strat_mining <address>
```
```
2017-07-23 16:27:52.542	[miner 0]	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:917	mined block failed verification
2017-07-23 16:27:52.561	[miner 0]	INFO 	global	src/cryptonote_basic/miner.cpp:456	Found block for difficulty: 1
2017-07-23 16:27:52.561	[miner 0]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3164	Block with id is INVALID: <b89cd1e533c067989f52f3dc38f3b14fed297f3b20a2c9a0910e31bcdb9e4092>
```

I want to premine my own cryptocurrency so the first block is 0 and the next is the max amount. But i think it isn't the problem, I think the problem is the genesis that i create.



# Discussion History
## moneromooo-monero | 2017-07-24T16:38:54+00:00
Run with log level 1, it'll tell you what is wrong. This is not a support channel, however, so futher questions of this type will be ignored. Try #monero or reddit, which are for user type questions.

## loldlm1 | 2017-07-25T13:57:01+00:00
Sorry i was a little tired with this problemas, i already fixed it disabling this
```
your_coin/CMakeLists.txt:102 # set this to 0 if per-block checkpoint needs to be disabled set(PER_BLOCK_CHECKPOINT 0)
```

## moneromooo-monero | 2017-08-08T10:54:55+00:00
+resolved

## 3ch0elite | 2018-01-09T09:21:32+00:00
loldlm1 can you share with me the code you used to generate the genesis-tx 

## ghost | 2018-06-03T10:56:51+00:00
@3ch0elite did you manage to print or generate the genesis-tx?

# Action History
- Created by: loldlm1 | 2017-07-24T14:56:30+00:00
- Closed at: 2017-08-08T11:00:15+00:00
