---
title: 'monero-wallet-cli : wrong numbers with pending transfers'
source_url: https://github.com/monero-project/monero/issues/1054
author: schnerchi
assignees: []
labels: []
created_at: '2016-09-05T19:42:35+00:00'
updated_at: '2016-10-05T05:33:24+00:00'
type: issue
status: closed
closed_at: '2016-10-05T05:33:24+00:00'
---

# Original Description
After sending a tx, show_transfers will show wrong numbers for the pending transaction. sometimes the shown numbers (sent amount and fee) add up to (sent amount)+fee, though not always...

tested with master commit afe3cce


# Discussion History
## moneromooo-monero | 2016-09-18T09:09:26+00:00
If you have that wallet still, please try with https://github.com/monero-project/monero/pull/1085 which I think should fix it (it does here, but just in case the patch doesn't catch all cases).


## schnerchi | 2016-10-05T05:33:24+00:00
Hmm... tested it and seams to work. 


# Action History
- Created by: schnerchi | 2016-09-05T19:42:35+00:00
- Closed at: 2016-10-05T05:33:24+00:00
