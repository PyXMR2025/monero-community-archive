---
title: badly formatted archive breaks linux auto-update
source_url: https://github.com/monero-project/monero/issues/8521
author: BeholdersEye
assignees: []
labels: []
created_at: '2022-08-20T12:14:40+00:00'
updated_at: '2022-08-20T12:16:53+00:00'
type: issue
status: closed
closed_at: '2022-08-20T12:16:53+00:00'
---

# Original Description



tar xvf monero-gui-linux-x64-v0.18.1.0.tar.bz2 
monero-gui-v0.18.1.0/
monero-gui-v0.18.1.0/LICENSE
tar: monero-gui-v0.18.1.0/LICENSE: implausibly old time stamp     -9223372036854775808
monero-gui-v0.18.1.0/extras/
monero-gui-v0.18.1.0/extras/monero-blockchain-ancestry
tar: monero-gui-v0.18.1.0/extras/monero-blockchain-ancestry:     implausibly old time stamp -9223372036854775808
monero-gui-v0.18.1.0/extras/monero-blockchain-depth
tar: monero-gui-v0.18.1.0/extras/monero-blockchain-depth:     implausibly old time stamp -9223372036854775808



May I also suggest not letting hardware wallets' suck dictate the pace of Monero releases in the future.

# Discussion History
# Action History
- Created by: BeholdersEye | 2022-08-20T12:14:40+00:00
- Closed at: 2022-08-20T12:16:53+00:00
