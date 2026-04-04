---
title: Error while opening wallet with hardware key (Ledger Nano S)
source_url: https://github.com/monero-project/monero/issues/6181
author: marcinulan
assignees: []
labels: []
created_at: '2019-11-25T17:05:18+00:00'
updated_at: '2019-11-25T18:59:07+00:00'
type: issue
status: closed
closed_at: '2019-11-25T17:30:48+00:00'
---

# Original Description
1. Open monero wallet app
2. Choose to open a wallet created in previous version with hardware key (Nano S)
3. Plug-in Ledger Nano S, unlock it and open Monero App on Ledger
4. Type in password
5. Click 'Ok'

Expected result: wallet is opened
Actual result: I get an error "Couldn't open wallet: Wrong Device Status: SW=6930 (EXPECT=9000, MASK=ffff)"

Software versions:
Mac OS X 64-bit: 0.15.0.1 Carbon Chamaeleon
Ledger firmware: 1.6.0 (Secure Element), 1.11 (MC)
Monero App on the Ledger: 1.4.1

![Zrzut ekranu 2019-11-25 o 17 45 47](https://user-images.githubusercontent.com/13141685/69560611-4be03d80-0fac-11ea-9996-c4e3e6071369.png)

# Discussion History
## rating89us | 2019-11-25T17:27:25+00:00
You are using monero-gui, and here is the repository of monero-cli
There is already an issue for your problem here:
https://github.com/monero-project/monero-gui/issues/2480

## selsta | 2019-11-25T18:59:06+00:00
v1.4.2 is now out: https://www.reddit.com/r/Monero/comments/e1k7dg/ledger_monero_app_142_is_out/

# Action History
- Created by: marcinulan | 2019-11-25T17:05:18+00:00
- Closed at: 2019-11-25T17:30:48+00:00
