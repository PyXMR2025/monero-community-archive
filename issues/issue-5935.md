---
title: Select preferred unspent tx to transfer
source_url: https://github.com/monero-project/monero/issues/5935
author: zhongqiuwood
assignees: []
labels: []
created_at: '2019-09-26T08:44:25+00:00'
updated_at: '2019-09-26T10:43:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Addressing how to transfer by using specified txid rather than random ones.

## backaground
We are eager to select preferred unspent tx by ourselves to create 
an unsigned transcation. 

This feature significantly increases efficiency, 
and reduces the unsigned transcation size in case of transferring 
a big amount by providing a couple of large unspent tx.

Without the feature, thousands of small unspent tx might be selected to satisfy the amount.

# Discussion History
## zhongqiuwood | 2019-09-26T08:44:51+00:00
Refer to: https://github.com/monero-project/monero/pull/5934 for the fix.

# Action History
- Created by: zhongqiuwood | 2019-09-26T08:44:25+00:00
