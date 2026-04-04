---
title: Erroneous output transaction value
source_url: https://github.com/monero-project/monero/issues/5542
author: Adreik
assignees: []
labels: []
created_at: '2019-05-14T10:35:28+00:00'
updated_at: '2019-05-15T07:34:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
So I was messing around on stagenet with watch-only and spending wallets; moving transactions between and broadcasting transactions from both, etc.

I noticed that several of the values from the show_transfers command on the watch only wallet had outgoing XMR values that were extremely high, far more than was spendable by the key. The wallet with the spendkey displayed the correct value, 0 (transfer to own address), as did the watch-only wallet after importing the outputs and key image data known to the wallet with the spendkey.

I am not 100% sure how to replicate this, but I have attached a screen capture of the lines in question (Three offending transactions visible).

![LargeOutgoingTransfers](https://user-images.githubusercontent.com/35472686/57691524-c5a38000-7687-11e9-9224-6626e5a8b69a.png)

Edit: 
Spendkeys: 
secret: 85175f1e0fd37be3b1abe19bf461242798965be4a291af5525928dd4f3ec250b
public: 2d7d13d0a6df4b4cfb7b25185c8edfcd6abe88073af879f1601e0895b55a81e2
Viewkeys:
secret: b7534b67d894bf2ebaf2fafdd579f0f2a2ff03c4afd3de947120b90b24522d00
public: 14d96ff4b1f3f057453e053a79227481d5e1aa7278dc3d80870c08c479f8b405

Edit:
I think I didn't save it initially or something so I have the wallet file of the view only wallet that displays the problem. Hopefully this is helpful to identifying the issue.
Password is "view". 

https://drive.google.com/open?id=1I5nDalKZdnl3Sg5Ji-sPl5C19NaHKtQj






# Discussion History
# Action History
- Created by: Adreik | 2019-05-14T10:35:28+00:00
