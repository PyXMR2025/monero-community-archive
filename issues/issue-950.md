---
title: simplewallet --restore-deterministic-wallet isn't detecting past transactions
source_url: https://github.com/monero-project/monero/issues/950
author: mmortal03
assignees: []
labels:
- bug
created_at: '2016-08-08T19:38:08+00:00'
updated_at: '2016-09-26T01:16:38+00:00'
type: issue
status: closed
closed_at: '2016-09-26T01:16:38+00:00'
---

# Original Description
Restoring from deterministic seed isn't detecting any past transactions. MoneroMooo's theory from the bitcointalk thread is that this may be happening because "simplewallet now skips refresh till the block the wallet was created, so there must be a bug that makes it think it doesn't need to refresh those early blocks."

Steps to reproduce:

Run simplewallet --restore-deterministic-wallet
pick a wallet file name 
pick a password
Enter an Electrum seed that represents an address with past transactions (you can use the one below)
Let simplewallet scan for past transactions.

Bug: After scanning, no transaction history will be found, and the balance will display as zero, even if the wallet actually has a current balance. Running refresh, rescan_bc, etc. don't help. 

You can use the following seed to reproduce the issue:

toilet zeal lion cafe circle ruthless inkling were dauntless jogger custom lagoon suddenly bays torch pager uttered react nurse cause aphid vulture bounced civilian lagoon

This had past transactions that began at block 1088432.


# Discussion History
## hyc | 2016-08-09T21:45:04+00:00
What git rev did you build from?


## mmortal03 | 2016-08-09T22:28:45+00:00
Originally (From July 8th): https://github.com/monero-project/bitmonero/commit/18dd50702407ece54a98563921fa744c6b7c15b2

As well as the current revision: https://github.com/monero-project/bitmonero/commit/0fbe9cfcdb9df2b141024eec04c3c7412791b741


## mmortal03 | 2016-08-09T22:29:44+00:00
Meaning, it must have become broken before July 8th.


## luigi1111 | 2016-08-10T14:15:45+00:00
mmortal03, this patch fixes these issues for me (I was able to reproduce the behavior you experienced).


## mmortal03 | 2016-08-11T03:19:05+00:00
Thanks @luigi1111 , I've just finished testing @hyc 's "better fix", and it does seem to fix the problem: https://github.com/monero-project/bitmonero/pull/952/commits/709c7247cd525952e89c4b8975171152a3969d92


## mmortal03 | 2016-09-26T01:16:38+00:00
The fix was merged soon after the above was tested, so I'm closing this.


# Action History
- Created by: mmortal03 | 2016-08-08T19:38:08+00:00
- Closed at: 2016-09-26T01:16:38+00:00
