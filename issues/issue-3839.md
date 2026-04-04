---
title: Wrong UI Presented After Deleting Default Wallet
source_url: https://github.com/monero-project/monero-gui/issues/3839
author: elibroftw
assignees: []
labels: []
created_at: '2022-02-14T05:35:22+00:00'
updated_at: '2022-02-14T05:57:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
OS: Windows

1. Have at least one wallet file
2. Duplicate wallet dir and keys "main" to `wallet-test` and `wallet-test.keys`
3. Open GUI and open `wallet-test` 
4. Close GUI
5. Delete the wallet-test folder
6. Launch GUI
7. Screenshot happens
8. Press continue
9. You now have to select a mode; I use advanced even though I don't run monerod from the GUI
10. Finally at UI that I should've been presented with at first
![image](https://user-images.githubusercontent.com/21298211/153806084-a3c5e234-e410-4410-8ced-a669e4f375c6.png)


# Discussion History
# Action History
- Created by: elibroftw | 2022-02-14T05:35:22+00:00
