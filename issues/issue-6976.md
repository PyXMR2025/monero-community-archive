---
title: Cannot create or restore wallet on Windows 7 virtual machine
source_url: https://github.com/monero-project/monero/issues/6976
author: moneroentusi
assignees: []
labels: []
created_at: '2020-11-04T19:18:37+00:00'
updated_at: '2020-11-04T20:19:43+00:00'
type: issue
status: closed
closed_at: '2020-11-04T20:19:30+00:00'
---

# Original Description
I've installed the GUI Wallet 0.17.1.1 on my Windows 7 virtual machine and I can't create a new wallet, I do everything and at the last steep when I hit Create wallet nothing happens. Also, the wallet does not connect to the node installed on the virtual machine. Anybody can help me please?

I also tried to restore my existing wallet and it does not work, I enter the seed and restore height, I chose a password and when I hit Open wallet I get the following: Please enter the password for: monero-core.Uh3212 (which is not the wallet name I choose), if I enter my password I get the following: Couldn't open wallet: file not found "C:/Users/Myuser/AppData/Local/Temp/monero-core.Uh3212.Keys

With the previous version everything worked fine.

# Discussion History
## moneroentusi | 2020-11-04T20:19:43+00:00
I fixed the problem by giving the virtual machine more cores per processor and I checked all 3 boxes from Virtualization engine

# Action History
- Created by: moneroentusi | 2020-11-04T19:18:37+00:00
- Closed at: 2020-11-04T20:19:30+00:00
