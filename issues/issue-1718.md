---
title: v13.0.3 GUI does not allow transaction under 1 XMR
source_url: https://github.com/monero-project/monero-gui/issues/1718
author: BigslimVdub
assignees: []
labels:
- resolved
created_at: '2018-11-02T03:09:19+00:00'
updated_at: '2018-11-03T01:23:03+00:00'
type: issue
status: closed
closed_at: '2018-11-02T12:18:25+00:00'
---

# Original Description
OSX 10.13.6
monero-gui-mac-x64-v0.13.0.3.tar.bz2

Trying to send a transaction, GUI does not unlock the send button unless over 1 xmr is entered. If a decimal is the first point, I can not send a transaction. 
It does not change with custom decorations on or off. 

<img width="636" alt="less than 1" src="https://user-images.githubusercontent.com/30030687/47891871-01c96e80-de23-11e8-95da-2834661687cc.png">

<img width="647" alt="more than 1" src="https://user-images.githubusercontent.com/30030687/47891876-068e2280-de23-11e8-8438-ccc11b27c029.png">


# Discussion History
## dEBRUYNE-1 | 2018-11-02T11:45:59+00:00
Amounts below one can be denoted with `0.` 

By design, the GUI does not accept amounts that start with a `.`



## dEBRUYNE-1 | 2018-11-02T12:11:59+00:00
+resolved

## sanderfoobar | 2018-11-02T12:20:02+00:00
Specifying amount `.194` never worked. Older versions would eat the period and end up with `194`.

## BigslimVdub | 2018-11-03T01:23:03+00:00
Followup:
Silly me, it's been almost a year since I sent a TX from my monero wallet but I even checked my history and it even has 0 before the decimals for all the tx I had made. Duh
<img width="251" alt="less than one transaction" src="https://user-images.githubusercontent.com/30030687/47946652-a8be1100-dedc-11e8-8004-3f72b2db1e69.png">


# Action History
- Created by: BigslimVdub | 2018-11-02T03:09:19+00:00
- Closed at: 2018-11-02T12:18:25+00:00
