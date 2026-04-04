---
title: 'Consensus Discussion: locked transfers in case of 4 minute block time'
source_url: https://github.com/monero-project/monero/issues/5776
author: dnaleor
assignees: []
labels:
- invalid
created_at: '2019-07-26T16:16:59+00:00'
updated_at: '2019-08-27T15:42:03+00:00'
type: issue
status: closed
closed_at: '2019-08-27T15:42:03+00:00'
---

# Original Description
As some of you probably know, monero always kept open the possibility to increase the blocktime to 4 minutes. In the past we already increased it from 1 min to 2 minutes. This is part of our 'social consensus'. 

I want to address an issue for people who are using or planning to use the locked_transfer feature. When you do such a transaction, you need to specify a number of blocks. If you for example would lock a transaction for 263000 blocks, that would correspond to roughly one year of locktime.

Imagine now that in 6 months we would introduce a 4 minute block time, this could significantly increase the locktime because the 131500 remaining blocks at the moment of the fork would take a full year to be mined, making the effective lock time not 12 but 18 months. 

It would be good to have a discussion about how we would handle this issue so we establish 'social consensus' beforehand. 

# Discussion History
## dnaleor | 2019-07-26T16:28:04+00:00
My personal opinion is that we should in that case code in something for "legacy locked transactions" that would enable those txo's to be spent at half the remaining number of blocks. 

It's -I guess- in theory even possible to do this beforehand by changing consensus code now to already include a void parameter that is a placeholder for the fork height for 4 minute blocks and use that parameter in the calculation of the valid spend height.

Pseudocode:
```

int forkHeightFourMininutes = 0   // placeholder for potential 4 minute block height
if (forkHeightFourMininutes == 0){
spendHeight =  transactionHeight + lockblocks
}
else{
remainingBlocks = transactionHeight + lockblocks - currentHeight
spendHeight = forkHeightFourMininutes + remainingBlocks/2
}

```

## moneromooo-monero | 2019-08-19T15:27:19+00:00
If you want to lock on a time, then use a time, not a block height. Values above 500000000 are a UNIX timestamp (1970 epoch). Changing the unlock heights as you request seems like a surefire way to kick ourselves in the butt with a time delay.

## moneromooo-monero | 2019-08-27T15:27:12+00:00
Closing, since this was based on not knowing timestamps were allowed.

+invalid

# Action History
- Created by: dnaleor | 2019-07-26T16:16:59+00:00
- Closed at: 2019-08-27T15:42:03+00:00
