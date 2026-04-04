---
title: '[UX] If User tries to open a stagenet wallet, let them'
source_url: https://github.com/monero-project/monero-gui/issues/4069
author: elibroftw
assignees: []
labels: []
created_at: '2022-11-15T05:13:56+00:00'
updated_at: '2023-01-11T17:17:09+00:00'
type: issue
status: closed
closed_at: '2023-01-11T17:17:09+00:00'
---

# Original Description
Suppose I open up the GUI and now select a wallet from the file. I know the wallet is a stagenet file, but when I try unlocking it, Monero hits me with the you can't open this in the mainnet wallet. 

Tell the user to switch it from the previous page or add an option to make it easier to switch the network from the unlock page itself.

# Discussion History
## plowsof | 2022-12-18T21:32:38+00:00
Confirmed:
on the 'gui' screen with wallet file icons in the default folder, selecting a wallet from a different network works fine, you can go back and forth no problem. shown [here on line 151](https://github.com/monero-project/monero-gui/blob/48393db2c75bd306e7d7f5cd2c226880a5eb0386/wizard/WizardOpenWallet1.qml#L150)
the issue is when you specifically click on "browse file system" and select the wallet from here - then you see the old error

* when opening a wallet using the graphical icon (not browse file system) - if you select a different network - it auto changes, but the next time you start the Monero GUI - it will error if the wallets network type isnt whats saved in settings i think.

# Action History
- Created by: elibroftw | 2022-11-15T05:13:56+00:00
- Closed at: 2023-01-11T17:17:09+00:00
