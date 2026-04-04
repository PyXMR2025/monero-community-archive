---
title: Wallet created in GUI has too high height - gui v0.11.1.0
source_url: https://github.com/monero-project/monero/issues/2775
author: 1337tester
assignees: []
labels: []
created_at: '2017-11-08T00:19:20+00:00'
updated_at: '2017-11-09T12:56:25+00:00'
type: issue
status: closed
closed_at: '2017-11-09T12:56:25+00:00'
---

# Original Description
**Problem:**
As I created a wallet in the GUI for testnet , for some reason the **height was set far above the actual height.**

This setting can be generally quite confusing for the user and I bet there can be some panic when you suddenly see your balance as 0. Would it be feasible to set it always to 0 for new wallets?

**Info:**
Wallet creation height:
![debug](https://user-images.githubusercontent.com/6553766/32524778-a0ff055e-c421-11e7-8630-c1c329c9159f.jpg)

The height at the time of creation was ~
![blockheight_actual](https://user-images.githubusercontent.com/6553766/32524788-af98b600-c421-11e7-90ba-e3a784a90ad3.jpg)

[wallet_creation_log.txt](https://github.com/monero-project/monero/files/1452125/wallet_creation_log.txt)


Also seen in terminal app
![blockheight_wallet](https://user-images.githubusercontent.com/6553766/32524772-9d25547e-c421-11e7-9580-0d6c62140fdd.jpg)

OS where I tested was Ubuntu 17.04 (on a VM if that matters)
Additional wallet info - Language = English, password = " " (one space character, maybe this plays a role here)

# Discussion History
## Jaqueeee | 2017-11-08T06:39:51+00:00
Fixed by https://github.com/monero-project/monero/pull/2342
Unfortunately that PR isn’t included in the release branch/tag.

## moneromooo-monero | 2017-11-09T12:53:42+00:00
+resolved

# Action History
- Created by: 1337tester | 2017-11-08T00:19:20+00:00
- Closed at: 2017-11-09T12:56:25+00:00
