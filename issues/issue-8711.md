---
title: monero-blockchain-stats omits data from final day
source_url: https://github.com/monero-project/monero/issues/8711
author: Rucknium
assignees: []
labels: []
created_at: '2023-01-16T21:13:44+00:00'
updated_at: '2023-02-06T17:36:49+00:00'
type: issue
status: closed
closed_at: '2023-02-06T17:36:49+00:00'
---

# Original Description
The shell command
`./monero-blockchain-stats --block-start=2797900 --block-stop=2800468`
prints
```
Date	Blocks/day	Blocks	Txs/Day	Txs	Bytes/Day	Bytes
2023-01-12	423	2798323	10478	10478	26770465	26770465
2023-01-13	688	2799011	15464	25942	38953621	65724086
2023-01-14	774	2799785	15034	40976	38456559	104180645
```

The start block, 2797900, has a timestamp of 2023-01-12 10:55:23 UTC. `monero-blockchain-stats` prints partial data from 2023-01-12, which is fine. The stop block, 2800468, is the final block on the day of 2023-01-15, but no data from 2023-01-15 is printed. (If `block-stop` is set to 2800469, i.e. one block into the next day (2023-01-16), still nothing from 2023-01-15 is printed. `block-stop` must be set to 2800470, i.e. two blocks into the next day, to print data from 2023-01-15.) Setting `block-stop` to a block with timestamp partway through 2023-01-15, e.g. 2800100, also prints nothing from 2023-01-15. This seems to be general behavior of the utility and not something specific to these particular days.

This isn't expected behavior. My suggestion is to print partial data for the final day, similar to the behavior for printing partial data for the first day. Another option is to not print any partial data (but then why would the flags allow the user to specify block heights and not dates directly?). In any case, if the user specifies a block height interval that completely covers a certain day, that day's data should be printed. That's not happening at the moment.

Thank you for any improvements that can be made.

# Discussion History
## plowsof | 2023-01-17T08:31:25+00:00
after a brief look:

setting [h <= block_stop](https://github.com/monero-project/monero/blob/master/src/blockchain_utilities/blockchain_stats.cpp#L232) we see:  edit* Rucknium explained to me how the blocks are indexed (height 0 being 1) so "<=" is incorrect here*
```
./monero-blockchain-stats --block-start=2800468 --block-stop=2800469
# DATA
Date	Blocks/day	Blocks	Txs/Day	Txs	Bytes/Day	Bytes
processing block: 2800468
processing block: 2800469
DEBUG: DAY HAS CHANGED
2023-01-15	1	2800469	26	26	54563	54563
```
so the print out only happens 'at day change' - 'for the previous day' - the for loop will process a partial day and not reach the 'end of day print out'. 

ideally, it would print the partial day after the for loop ends. my personal lack of knowledge is preventing this at the moment as im now asking myself "how to access variables outside of a for loop and why is the compiler angry at me"

edit* i learned how to set a variable. Is this your desired output?
```
./monero-blockchain-stats --block-start=2797900 --block-stop=2800468

# DATA
Date	Blocks/day	Blocks	Txs/Day	Txs	Bytes/Day	Bytes
2023-01-17 10:45:35.798	W Couldn't allocate RandomX cache using large pages
2023-01-12	423	2798323	10478	10478	26770465	26770465
2023-01-13	688	2799011	15464	25942	38953621	65724086
2023-01-14	774	2799785	15034	40976	38456559	104180645
2023-01-15	684	2800468	14076	55052	35789881	139970526
```

## hyc | 2023-01-17T16:13:47+00:00
will have a patch shortly

## Rucknium | 2023-01-21T18:02:59+00:00
#8712 appears to work properly after building locally. Thank you!

## hyc | 2023-01-21T18:15:51+00:00
That's great, but usually you should leave issues until the PR actually gets merged. And you would be better doing a review / approval of the PR than commenting here.

# Action History
- Created by: Rucknium | 2023-01-16T21:13:44+00:00
- Closed at: 2023-02-06T17:36:49+00:00
