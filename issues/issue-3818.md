---
title: Error when opening mainnet wallet when Monero GUI is starting in stagenet mode
source_url: https://github.com/monero-project/monero-gui/issues/3818
author: rating89us
assignees: []
labels: []
created_at: '2022-01-13T15:58:32+00:00'
updated_at: '2022-03-03T00:04:15+00:00'
type: issue
status: closed
closed_at: '2022-03-03T00:04:15+00:00'
---

# Original Description
Steps to reproduce:
- Open a mainnet wallet
- Close the wallet and return to main menu
- In advanced options, choose stagenet in network type
- Close Monero GUI
- Reopen Monero GUI
- Monero GUI will try to open the last opened wallet (which is a mainnet wallet) while stagenet is selected, displaying the error below:
![image](https://user-images.githubusercontent.com/45968869/149363744-15ecec2f-2a0d-4f07-8db3-878d953e2afb.png)


# Discussion History
## reemuru | 2022-01-17T15:28:20+00:00
I just ran into this edge case when I was testing some stuff and jumping between stagenet and mainnet. I opened a [PR](https://github.com/monero-project/monero-gui/pull/3824) that resets the wallet path when changing network type. If user doesn't select new wallet after changing network type and closes they would now be forced back to wallet setup. Selecting the correct wallet file to match network type results in expected behavior. 

# Action History
- Created by: rating89us | 2022-01-13T15:58:32+00:00
- Closed at: 2022-03-03T00:04:15+00:00
