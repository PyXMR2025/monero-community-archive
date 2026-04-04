---
title: Able to send transaction with mixin of 2 on v0.11.0.0 release
source_url: https://github.com/monero-project/monero/issues/2415
author: campassi
assignees: []
labels:
- invalid
created_at: '2017-09-08T16:40:30+00:00'
updated_at: '2017-11-08T22:45:46+00:00'
type: issue
status: closed
closed_at: '2017-09-08T17:48:23+00:00'
---

# Original Description
[wallet 44x44x]: `transfer unimportant 3 44x44x .05`
Wallet password: **
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
Failed to check for backlog: no connection to daemon
Is this okay anyway?  (Y/Yes/N/No): y
Sending 0.050000000000.  The transaction fee is 0.003365050000
Is this okay?  (Y/Yes/N/No): y
Transaction successfully submitted, transaction <1412ed7dd4d6df7f7d2be9ec16afb7c87c60b6733848979c3b44549983ce19e8>
You can check its status by using the `show_transfers` command.

http://moneroblocks.info/search/1412ed7dd4d6df7f7d2be9ec16afb7c87c60b6733848979c3b44549983ce19e8

# Discussion History
## moneromooo-monero | 2017-09-08T17:43:12+00:00
Nice, I didn't realize you could set priority as a one off.
Anyway, this is fine, till the fork in a few days.

+invalid


## campassi | 2017-09-08T17:44:26+00:00
Thank you for your feedback moneromooo

# Action History
- Created by: campassi | 2017-09-08T16:40:30+00:00
- Closed at: 2017-09-08T17:48:23+00:00
