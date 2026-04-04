---
title: Load only latest 25 Transactions in History
source_url: https://github.com/monero-project/monero-gui/issues/1437
author: italocoin-project
assignees: []
labels:
- resolved
- Hacktoberfest
created_at: '2018-05-31T23:16:47+00:00'
updated_at: '2019-04-24T12:27:43+00:00'
type: issue
status: closed
closed_at: '2019-04-24T12:27:43+00:00'
---

# Original Description
The problem i find in history is that it stucks the whole wallet if you have a lots of transactions, my idea would be this:

Load latest 25 transactions and to se more will be added a "Load More" button

Its really needed because when i have many transactions the wallet hangs and just crashes or i need to end thask forcefully, even when syncing it would be good to not load history in the wallet because that hangs the wallet to, let me know what you guys think about it

Regards

# Discussion History
## dEBRUYNE-1 | 2018-06-01T11:39:13+00:00
Kind of similar to #1433. 

## erciccione | 2018-10-06T16:00:37+00:00
+hacktoberfest

## NoreiT | 2019-02-10T09:38:44+00:00
Would it be possible to at least not loading history after clicking history tab? I tried to find it but werent able to.

## selsta | 2019-02-18T14:52:23+00:00
@NoreiT Can you rephrase that? Why should the history not load when clicking on history?

## NoreiT | 2019-02-18T19:56:43+00:00
> @NoreiT Can you rephrase that? Why should the history not load when clicking on history?

Point is, that with big number of TXs, whole history is loaded right after you click History tab. And for large number of TXs, you will end up with non-responsive wallet (in better case, othewise wallet just crash after some time). 

Date filtering works only after History is loaded.

## selsta | 2019-04-24T12:21:07+00:00
#2025 

+resolved

# Action History
- Created by: italocoin-project | 2018-05-31T23:16:47+00:00
- Closed at: 2019-04-24T12:27:43+00:00
