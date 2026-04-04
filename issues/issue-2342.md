---
title: 'Restore with 24 words failed: Electrum-style word list failed verification'
source_url: https://github.com/monero-project/monero-gui/issues/2342
author: feugen
assignees: []
labels: []
created_at: '2019-08-08T11:43:23+00:00'
updated_at: '2019-08-08T13:57:45+00:00'
type: issue
status: closed
closed_at: '2019-08-08T13:57:45+00:00'
---

# Original Description
I just tried to restore my wallet from seed and I get the gui message: Electrum-style word list failed verification

In terminal it says: 

2019-08-08 11:25:18.334	E Invalid seed: language not found
2019-08-08 11:25:18.334	E Invalid seed: failed to convert words to bytes

My seed contains english words so I changed the language to english but it doesnt work. Its an bip39 seed from Ledger nano S, I guess it should work, or how do I access my wallet now without hardware device since gui is not working with hardware (https://github.com/monero-project/monero-gui/issues/2341) ? 


# Discussion History
## selsta | 2019-08-08T12:10:10+00:00
Did you enter your Ledger seed directly into the GUI? That’s not going to work. You’ll have to use this tool: https://github.com/LedgerHQ/ledger-app-monero/tree/master/tools/python

> gui is not working with hardware

The GUI *does* work with a hardware wallet, I explained it in the other issue.

## feugen | 2019-08-08T13:57:45+00:00
Ah ok, thanks I did not try it yet, but ill mark it as resolved

# Action History
- Created by: feugen | 2019-08-08T11:43:23+00:00
- Closed at: 2019-08-08T13:57:45+00:00
