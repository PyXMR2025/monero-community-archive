---
title: Bug when changing wallet password
source_url: https://github.com/monero-project/monero/issues/6827
author: keffnet
assignees: []
labels: []
created_at: '2020-09-19T15:39:26+00:00'
updated_at: '2022-02-19T04:05:13+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:05:13+00:00'
---

# Original Description
Running 0.17.0 (not tested in previous version)

If you change the password on your wallet the funds are "gone" until you quit and start the wallet again.

Log with sensitive info and balance altered.

Balance: 1.000000000000, unlocked balance: 1.000000000000
Background refresh thread started
[wallet XXX]: password
Wallet password:
Enter a new password for the wallet:
Confirm password:
[wallet XXX]: rescan_bc
Starting refresh...
Enter password (output received):
Refresh done, blocks received: 12
Balance: 0.000000000000, unlocked balance: 0.000000000000


[wallet XXX]: exit
Start again..
Wallet password:
Starting refresh...
Balance: 1.000000000000, unlocked balance: 1.000000000000

--
Log file attached
[log.txt](https://github.com/monero-project/monero/files/5250116/log.txt)


# Discussion History
## selsta | 2022-02-19T04:05:13+00:00
Can't reproduce with the latest version. Also why did you rescan after changing password? That will make your balance gone until it fully synced the wallet again.

# Action History
- Created by: keffnet | 2020-09-19T15:39:26+00:00
- Closed at: 2022-02-19T04:05:13+00:00
