---
title: 'Feature request: Background mining only when profitability exceeds threshold'
source_url: https://github.com/monero-project/monero/issues/8623
author: Scalena
assignees: []
labels: []
created_at: '2022-10-24T15:57:41+00:00'
updated_at: '2023-01-18T04:20:31+00:00'
type: issue
status: closed
closed_at: '2023-01-18T04:20:30+00:00'
---

# Original Description
The mining difficulty of Monero keeps fluctuating, so for background miners who want to dedicate only a fraction of their CPU power to mining, it would be reasonable to do so preferably, when the reward per hash (=profitabilty) is above average. This would have the following benefits:

* For the individual background miner, the profitability will be slightly higher without using more system resources,
* For the network, it will reduce difficulty fluctuations if enough background miners adopt this strategy.

The simplest algorithm to implement this would be to automatically enable background mining only when the current profitability is above the <i>n</i>th percentile in relation to a defined lookback period. Of course, this simple algorithm will not work in the special cases of a monotonically increasing or decreasing difficulty, but this might either be considered of no practical relevance or be addressed by a more refined algorithm.

# Discussion History
## One-horse-wagon | 2022-10-24T19:28:20+00:00
It would seem this has already been addressed with programs and internet sites giving the profitability of mining the different POW coins.  I fail to see how this would encourage more monero mining.

## Scalena | 2022-10-25T15:04:19+00:00
@One-horse-wagon I'm not sure whether you're getting my point exactly. The term "profitability" might be a bit misleading here, I'm not referring to economic profitability but simply to the amount of monero earned per hash. This quantity fluctuates (due to fluctuating POW difficulty mostly) and some background miners might prefer to only mine when it is above average. Maybe I'm the one missing something here, but as far as I see, this cannot be addressed by a profitability computing website website but only be the background miner code itself.

## Gingeropolous | 2023-01-18T04:16:50+00:00
i think this would be problematic in the core software, because you'd have to code in a source for the price data.

though perhaps the user could enter the price source via command line, something like

--profit --price-source=some.api.somewhere

the --profit flag indicates that the software should only mine if profitable, and the --price-source points to some API.

though, this seems .... silly. The luck of finding a block doesn't increase or decrease depending on the profitability. 

perhaps this would make sense if you have a very quick timeframe for selling mining proceeds, but in that case this might be better done in the mining software (like xmrig), not the daemon. 

## selsta | 2023-01-18T04:20:30+00:00
This seems out of scope for monerod itself and should be suggested to a dedicated mining software like xmrig.

# Action History
- Created by: Scalena | 2022-10-24T15:57:41+00:00
- Closed at: 2023-01-18T04:20:30+00:00
