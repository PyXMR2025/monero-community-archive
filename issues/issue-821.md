---
title: 'cold-signing: multiple destinations only shows first one in confirmation popup'
source_url: https://github.com/monero-project/monero-gui/issues/821
author: Jaqueeee
assignees: []
labels:
- bug
created_at: '2017-08-14T14:52:25+00:00'
updated_at: '2018-01-03T15:53:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When signing a tx file only the first destination is showed in the confirmation dialog. 

# Discussion History
## Jaqueeee | 2017-08-14T14:52:32+00:00
+bug

## Timo614 | 2017-12-12T18:13:33+00:00
I spent a little bit looking into this bug documenting here what I've found.

The confirmation window shows data related to an unsigned transaction. It relies on the wallet API's UnsignedTransaction logic which provides methods that return vectors of data that match the order of the underlying transaction vector for a given type of data (so you can use the index to effectively cycle over data per transaction).

The GUI app loops over the transactions and attempts to display information about each:
https://github.com/monero-project/monero-gui/blob/master/pages/Transfer.qml#L550

This is the facade it's calling to interface with the UnsignedTransaction interface: https://github.com/monero-project/monero-gui/blob/master/src/libwalletqt/UnsignedTransaction.cpp#L15

The wallet2_api UnsignedTransaction interface:
https://github.com/monero-project/monero/blob/master/src/wallet/api/wallet2_api.h#L99

Problem is this API only returns data on a transaction level and in some cases does not have a one to one mapping of the vectors based on the transaction list as the GUI code is expecting above.

It does this for the address by always using the first recipient regardless of how many destinations exist: https://github.com/monero-project/monero/blob/master/src/wallet/api/unsigned_transaction.cpp#L296

The amount is not a one to one mapping to the transaction index though but rather it has a vector that includes all destinations as individual amounts without concern for which transaction they belong to. https://github.com/monero-project/monero/blob/master/src/wallet/api/unsigned_transaction.cpp#L223

We reference the amount based on the transaction index though as we're looping through.
https://github.com/monero-project/monero-gui/blob/master/pages/Transfer.qml#L554

I'm not sure if you can even generate a multi transaction with multi destinations (I can do one or the other but not both at the same time from my own test cases) but if you could we'd show the transaction amount incorrectly due to that index issue (if there were 2 transactions and transaction 1 had 2 destinations, transaction 2 would display transaction 1's 2nd amount due to this logic at the moment I believe).

## Timo614 | 2018-01-03T15:50:55+00:00
I made two branches for this (one in monero and one in monero-gui):
https://github.com/Timo614/monero/tree/wallet-api-unsigned-transaction-bug-fix https://github.com/Timo614/monero-gui/tree/unsigned-transaction-destination-bug-fix

Not sure on the process for releasing API changes but in the branch I refactored the transfer logic used by the history component so it could be used for unsigned transactions as well. If anyone knows: Are we okay with breaking this API or is it something we need backwards compatibility for? Wondering if it's safe to remove the old methods here as they were broken for that last comment's reasons. If it's just making the two PRs can file those so we can get this fixed just confirming what's ideal here process wise.

# Action History
- Created by: Jaqueeee | 2017-08-14T14:52:25+00:00
