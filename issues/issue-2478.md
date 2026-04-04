---
title: Can't change language using main menu
source_url: https://github.com/monero-project/monero-gui/issues/2478
author: rating89us
assignees: []
labels: []
created_at: '2019-11-24T10:56:26+00:00'
updated_at: '2019-11-27T16:25:16+00:00'
type: issue
status: closed
closed_at: '2019-11-27T16:25:16+00:00'
---

# Original Description
Monero GUI v0.15.0.1

After opening Monero GUI for the second time, there are two ways to change the Language:
- Inside the wallet: globe icon in upper left side
- Main menu: using `Change language` button in Main menu or in "Change wallet mode" page 

The language is not changing in the second case, when the user is selecting a language for the second time in main menu, with the wallet closed. 

After choosing a new language, the main menu changes to the new language, but when the wallet is reopened, the old language is used.

Steps to reproduce:
1. Open a wallet file
2. Close wallet and go to Main Menu
3. Click "Change wallet mode" > "Change Language" > "Language"
4. Select a new language to the Monero GUI and click "Continue"
5. Select Wallet mode
6. Open a wallet file
7. Monero GUI will open the wallet in the old language

# Discussion History
# Action History
- Created by: rating89us | 2019-11-24T10:56:26+00:00
- Closed at: 2019-11-27T16:25:16+00:00
