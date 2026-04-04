---
title: Transaction would be too large
source_url: https://github.com/monero-project/monero/issues/199
author: fish34
assignees: []
labels: []
created_at: '2014-12-08T12:27:23+00:00'
updated_at: '2018-03-05T23:55:38+00:00'
type: issue
status: closed
closed_at: '2015-02-03T18:13:36+00:00'
---

# Original Description
Today in the log error when wallet daemon try to make payouts:
Error with transfer RPC request to wallet daemon {"code":-4,"message":"Transaction would be too large.  try /transfer_split."}
What can we do with this error at the pool?


# Discussion History
## fluffypony | 2014-12-08T12:34:44+00:00
Use the transfer_split JSON RPC API call instead of transfer


## fluffypony | 2015-02-03T18:13:36+00:00
Closed


## reeyon | 2018-03-05T08:18:24+00:00
@fluffypony 
Hi i know this is old. But hope you can help to answer my question.
you'd mentioned to use transfer_split in API call.. 
where can I change it on the pool software?


## SamsungGalaxyPlayer | 2018-03-05T23:55:38+00:00
@reeyon this is a better question for [StackExchange](https://monero.stackexchange.com).

# Action History
- Created by: fish34 | 2014-12-08T12:27:23+00:00
- Closed at: 2015-02-03T18:13:36+00:00
