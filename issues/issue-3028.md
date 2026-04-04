---
title: 'Ledger integration could/should detect Ledger wallet changes '
source_url: https://github.com/monero-project/monero-gui/issues/3028
author: sanderfoobar
assignees: []
labels: []
created_at: '2020-07-29T16:21:57+00:00'
updated_at: '2020-07-29T16:21:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
1. Open a wallet on the ledger device and open it in the GUI.
2. On the device, go to settings -> select account, and change the **ledger account** (a different Monero wallet altogether).
3. The GUI does not detect this change and assumes old wallet is still in use.
4. Clicking on Receive inside the GUI *will* fetch (the correct) new addresses from the Ledger device, but they wont be associated with the currently opened GUI wallet keysfile.

In addition, similar behavior can be observed with Ledger's "[Advanced Passphrase Protection](https://support.ledger.com/hc/en-us/articles/115005214529-Advanced-passphrase-security)" feature, where depending on *what* password you enter after the Ledger device went to sleep, a different wallet will be opened on the device.

This behavior can be observed in the GUI, CLI, and I also tested the Bitcoin Electrum wallet where the same occurs.

# Discussion History
# Action History
- Created by: sanderfoobar | 2020-07-29T16:21:57+00:00
