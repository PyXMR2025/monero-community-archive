---
title: Faster wallet refresh when restoring a wallet
source_url: https://github.com/monero-project/monero/issues/805
author: hyc
assignees: []
labels: []
created_at: '2016-04-14T00:58:37+00:00'
updated_at: '2016-07-07T20:02:12+00:00'
type: issue
status: closed
closed_at: '2016-07-07T20:02:12+00:00'
---

# Original Description
See here https://github.com/LMDB/bitmonero/tree/wallet2
Results with the new code are here https://gist.github.com/hyc/ffce33a965134ea2e52f2ee2d0c4c5f3

To summarize: for a wallet whose first block is 882230, restoring from deterministic seed takes
43:24.60 using the original wallet code. With the refresh-height patch and setting the refresh-height, so that blocks before that height are not scanned for transactions, it takes 27:56.49 including the time to read the blocks from disk, or only 6:32.26 if the blocks are already cached. With the fast_refresh patch, so that only hashes are retrieved up to that height, instead of full blocks, it takes 4:42.49 - just the time required to crunch the blocks from 882230 to the end. Here's a summary of the wall clock, user, and system CPU times for each run.

| Wallet | Wall | User | Sys | Daemon | Wall | User | Sys |
| --- | --- | --- | --- | --- | --- | --- | --- |
| orig | 2604.60 | 6653.25 | 112.69 | orig | 2601.87 | 73.63 | 12.40 |
| mid | 1676.49 | 610.12 | 48.36 | mid | 1661.73 | 92.50 | 27.85 |
| mid2 | 392.26 | 614.95 | 44.33 | mid2 | 376.23 | 72.23 | 12.88 |
| fast | 282.49 | 515.98 | 13.98 | fast | 316.50 | 10.85 | 2.29 |


# Discussion History
## fluffypony | 2016-07-07T20:02:12+00:00
Fixed


# Action History
- Created by: hyc | 2016-04-14T00:58:37+00:00
- Closed at: 2016-07-07T20:02:12+00:00
