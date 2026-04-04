---
title: Weird behaviour after updating to version 0.18
source_url: https://github.com/monero-project/monero/issues/8472
author: erib3
assignees: []
labels: []
created_at: '2022-07-29T07:29:08+00:00'
updated_at: '2022-07-29T13:16:49+00:00'
type: issue
status: closed
closed_at: '2022-07-29T12:28:19+00:00'
---

# Original Description
So I installed the new release. I copied over my testnet wallets, when I ran monerod on testnet, it did this thing where it 'popped off blocks' then supposedly synced. Ok. Running the monero-wallet-rpc on testnet is fine but the money is pretty much all gone. Is that normal? Will the money come back?

Also when I try to revert to version 0.17, I get a DB error. --db-salvage does not help this, so I can only use the new release now.  

# Discussion History
## selsta | 2022-07-29T12:28:19+00:00
Testnet forked on May 16th. If you continued to use v0.17 after that date then you were on the wrong chain and all money you received on that wrong chain is gone.

> Also when I try to revert to version 0.17, I get a DB error. --db-salvage does not help this, so I can only use the new release now.

You can't use the old version anymore after a network upgrade.

If you are trying to test your monero integration in your app / website / ... then I would recommend to use stagenet instead.

## erib3 | 2022-07-29T13:16:49+00:00
thank you for the response

# Action History
- Created by: erib3 | 2022-07-29T07:29:08+00:00
- Closed at: 2022-07-29T12:28:19+00:00
