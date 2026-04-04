---
title: Numerical value instead of (all)
source_url: https://github.com/monero-project/monero-gui/issues/335
author: relics219
assignees: []
labels:
- resolved
created_at: '2016-12-22T17:09:36+00:00'
updated_at: '2017-08-07T19:05:11+00:00'
type: issue
status: closed
closed_at: '2017-08-07T19:05:10+00:00'
---

# Original Description
A small suggestion: when sending the maximum amount of Monero in your wallet would it be possible to have the actual number minus tx fees instead of (all)? 

# Discussion History
## ghost | 2016-12-22T17:29:08+00:00
It's a good idea, but the problem is that the sweep_all command is a calculation of the total balance minus the fee. The wallet would need to create the transaction (total balance - fees = the amount sent) even before you hit the Send button.

Perhaps in the future transactions could be calculated on the fly or something, but for now I don't see this changing.

## moneromooo-monero | 2016-12-26T11:42:21+00:00
Correct. It has to stay a placeholder for the reason above.

## ghost | 2017-03-29T03:48:02+00:00
This issue can probably be closed

## dEBRUYNE-1 | 2017-08-07T17:43:02+00:00
+resolved

# Action History
- Created by: relics219 | 2016-12-22T17:09:36+00:00
- Closed at: 2017-08-07T19:05:10+00:00
