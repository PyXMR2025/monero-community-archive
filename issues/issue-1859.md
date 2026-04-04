---
title: App crashes when trying to send
source_url: https://github.com/monero-project/monero-gui/issues/1859
author: geft
assignees: []
labels: []
created_at: '2018-12-24T04:19:01+00:00'
updated_at: '2018-12-27T03:35:50+00:00'
type: issue
status: closed
closed_at: '2018-12-27T03:35:50+00:00'
---

# Original Description
1. Press send and see loading screen.
2. After a few minutes wondering why it's still loading, I check my Ledger to see that I have to verify the transaction. Note that I had to re-enter my Ledger password since it automatically locks itself. I verify on the Ledger.
3. After a few minutes the Ledger asks for another verification. I verify again.
4. App crashes.

I'm on Windows 64, 13.0.4. It sends just fine if I quickly verify the transaction, but there is no prompt on the GUI to do that so I have to stare at the Ledger.

# Discussion History
## selsta | 2018-12-24T14:12:42+00:00
Timeout is set to two minutes, if you take longer than that the app can crash.

## geft | 2018-12-24T14:23:32+00:00
Is that expected? Why can't the app just cancel the operation in a safe way?

## selsta | 2018-12-27T00:22:53+00:00
AFAIK @cslashm is working on this.

## geft | 2018-12-27T03:35:50+00:00
In that case I guess I'll close this.

# Action History
- Created by: geft | 2018-12-24T04:19:01+00:00
- Closed at: 2018-12-27T03:35:50+00:00
