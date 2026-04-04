---
title: problem with alt chains
source_url: https://github.com/monero-project/monero/issues/119
author: iamsmooth
assignees: []
labels:
- enhancement
created_at: '2014-09-06T18:05:34+00:00'
updated_at: '2022-07-20T19:48:26+00:00'
type: issue
status: closed
closed_at: '2022-07-20T19:47:53+00:00'
---

# Original Description
The recent attack resulted in the following message on some nodes, but the message indicates an inconsistency in the alt chain data structure, so there is likely some earlier consistency check missing

2014-Sep-06 11:02:18.859952 [P2P4]ERROR /home/user/bitmonero/src/cryptonote_core/blockchain_storage.cpp:771 alternative chain have wrong connection to main chain


# Discussion History
## fluffypony | 2016-01-25T17:51:15+00:00
I think we've fixed this with blockchain_db?


## iamsmooth | 2016-02-15T01:57:30+00:00
I'm not sure we ever identified the root cause so it is difficult to say whether it is fixed. Much of the alt chain code works similarly with blockchain_db since alt chains are not stored in the db


## dEBRUYNE-1 | 2018-01-08T12:42:38+00:00
+enhancement

## Cactii1 | 2022-07-20T01:04:02+00:00
Looks like this was fixed, should probably close this issue.

## selsta | 2022-07-20T19:48:26+00:00
This issue is almost 8 years old and it's unclear if it's still relevant. It can be reopened if we get other reports about this.

# Action History
- Created by: iamsmooth | 2014-09-06T18:05:34+00:00
- Closed at: 2022-07-20T19:47:53+00:00
