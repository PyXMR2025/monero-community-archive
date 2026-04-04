---
title: HELP ME WITH MONERO PLEASE
source_url: https://github.com/monero-project/monero-gui/issues/4218
author: redelre
assignees: []
labels: []
created_at: '2023-09-19T09:47:48+00:00'
updated_at: '2023-09-19T15:59:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello, I am writing to you because I cannot find a solution with monero wallet.
I hope I explained myself well: I installed monero with blockchain, I made several transactions by opening multiple accounts. On Friday, after sending the last transaction on account number 3 that they entered, on Saturday I open monero wallet and it gives me the error Error: Unable to connect to daemon: 127.0.0.1:18081 each time.
In panic I uninstalled and reinstalled the wallet, but the accounts were gone and the address of account number 3 that I had opened was not there. I uninstalled everything and reinstalled everything again with the 25 words, but I still don't see my balance.
Please help me

# Discussion History
## selsta | 2023-09-19T12:24:22+00:00
> Error: Unable to connect to daemon: 127.0.0.1:18081

This error doesn't necessarily mean anything interesting, it just means it was trying to connect to a daemon that isn't running on you system.

To help you with your issues, can you go to Settings -> Info and share the values of

- Version
- Wallet mode
- Wallet restore height

## selsta | 2023-09-19T15:59:18+00:00
You have to wait until your wallet is fully synced, notice how it has Wallet blocks remaining in the bottom left corner?

# Action History
- Created by: redelre | 2023-09-19T09:47:48+00:00
