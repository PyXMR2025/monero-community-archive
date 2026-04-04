---
title: Daemon not initializing testnet when option is selected
source_url: https://github.com/monero-project/monero-gui/issues/280
author: ghost
assignees: []
labels:
- resolved
created_at: '2016-12-14T17:22:27+00:00'
updated_at: '2017-08-07T23:45:07+00:00'
type: issue
status: closed
closed_at: '2017-08-07T23:45:07+00:00'
---

# Original Description
Creating a testnet wallet and starting the daemon starts it on mainnet

# Discussion History
## Jaqueeee | 2016-12-14T17:28:08+00:00
You can forward cli arguments to the daemon if you start GUI from terminal
On mac: 
./monero-core.app/Contents/MacOS/monero-core --testnet


## ghost | 2016-12-14T18:26:52+00:00
There's a checkbox that says "testnet" on the open/create wallet wizard. Would it be possible to automatically start the daemon in testnet mode when that wallet is loaded/created?

## Jaqueeee | 2016-12-14T18:38:20+00:00
yes, it's possible, but since the daemon isn't killed when switching wallets there could be an issue when switching between testnet and mainnet.  Not sure what's best. 

## medusadigital | 2017-04-18T09:20:45+00:00
can this be closed ? 

AFAIk testnet flag is not needed anymore now. 

## medusadigital | 2017-08-07T23:44:08+00:00
+resolved

# Action History
- Created by: ghost | 2016-12-14T17:22:27+00:00
- Closed at: 2017-08-07T23:45:07+00:00
