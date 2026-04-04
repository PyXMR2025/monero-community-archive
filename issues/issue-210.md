---
title: getblocktemplate should return previous block ID
source_url: https://github.com/monero-project/monero/issues/210
author: iamsmooth
assignees: []
labels: []
created_at: '2015-01-05T22:59:54+00:00'
updated_at: '2015-02-03T23:25:18+00:00'
type: issue
status: closed
closed_at: '2015-02-03T23:25:18+00:00'
---

# Original Description
Issue #209, while explained unclearly, refers to the situation after a reorg, when the height does not change but the previous work is no longer valid. Given the information provided there is no obvious way (aside from parsing the previous block ID out of the blob) for a miner to recognize this.


# Discussion History
## netmonk | 2015-01-06T12:28:34+00:00
:) you find a perl translator :+1: 


# Action History
- Created by: iamsmooth | 2015-01-05T22:59:54+00:00
- Closed at: 2015-02-03T23:25:18+00:00
