---
title: show_transfers missing entries during a transfer completion
source_url: https://github.com/monero-project/monero/issues/2202
author: evanrinehart
assignees: []
labels: []
created_at: '2017-07-24T23:10:59+00:00'
updated_at: '2017-08-07T17:54:17+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:54:17+00:00'
---

# Original Description
Step 0. Open your local monero-wallet-cli with a sync-ed up monerod running.

Step 1. Send monero from kraken to your wallet.

Step 2. show_transfers will eventually show something like this:
```
[wallet ????????]: show_transfers
    pool     in      10:11:19 PM      1.000000000000 <transaction hash> 0000000000000000 -
[wallet ????????]:
```

Step 3. After a while, show_transfers forgets about this momentarily:
```
[wallet ????????]: show_transfers
[wallet ????????]:
```

Step 4. Luckily, this is only temporary. When the transfer is complete, it comes back.
```
Height 1361000, transaction <transaction hash>, received 1.000000000000
[wallet ????????]: balance
Balance: 1.000000000000, unlocked balance: 0.000000000000
[wallet ????????]: show_transfers
 1361000     in      10:11:19 PM      1.000000000000 <transaction hash> 0000000000000000 -
[wallet ????????]:
```

# Discussion History
## moneromooo-monero | 2017-07-25T08:33:49+00:00
Thanks for the detalied report, fixed in https://github.com/monero-project/monero/pull/2203

## moneromooo-monero | 2017-08-07T17:50:38+00:00
+resolved

# Action History
- Created by: evanrinehart | 2017-07-24T23:10:59+00:00
- Closed at: 2017-08-07T17:54:17+00:00
