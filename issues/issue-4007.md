---
title: Funds Lost from CEX to Private Wallet
source_url: https://github.com/monero-project/monero-gui/issues/4007
author: pjbukem
assignees: []
labels: []
created_at: '2022-08-18T10:22:29+00:00'
updated_at: '2022-08-19T14:13:29+00:00'
type: issue
status: closed
closed_at: '2022-08-19T14:13:29+00:00'
---

# Original Description
Hi there, I transferred some XMR from a CEX to my primary receiving address and it has failed to show up. CEX has told me it's not their problem and that I should try to contact the receiving platform. Apologies if this is not the right place, but I can't see how the transfer could have gone wrong as the receiving address matches up with my account. Any suggestions as to what might have gone wrong would be greatly appreciated. Happy to provide more details about transaction if it helps. 

# Discussion History
## selsta | 2022-08-18T10:45:53+00:00
Can you go to Settings -> Info and say which

- Version
- Wallet mode

you have?

## pjbukem | 2022-08-18T13:17:40+00:00
It's 0.18.1.0-release (Qt 5.12.8)

Advanced mode (Remote node)

## selsta | 2022-08-18T16:29:06+00:00
Which remote node did you set? What block height are you on in the bottom left corner?

## pjbukem | 2022-08-19T08:36:48+00:00
The remote node was uwillrunanodesoon.moneroworld.com, but recently switched to http://209.97.185.45:18089. I believe the block height is 2688925 but I'm not sure what it was at the time. 

## selsta | 2022-08-19T10:44:46+00:00
Please use a remote node from here: https://github.com/monero-project/monero-gui/issues/3989#issuecomment-1214412781

The blockheight has to be the same as on xmrchain.net, it seems your remote node wasn't updated for v0.18

## pjbukem | 2022-08-19T10:55:48+00:00
Fantastic, it worked! Thanks for your help, really appreciated. 

# Action History
- Created by: pjbukem | 2022-08-18T10:22:29+00:00
- Closed at: 2022-08-19T14:13:29+00:00
