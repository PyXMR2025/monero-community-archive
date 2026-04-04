---
title: What is c if cols = 1 Error
source_url: https://github.com/monero-project/monero/issues/2868
author: vietanh79
assignees: []
labels: []
created_at: '2017-11-27T16:14:58+00:00'
updated_at: '2017-11-27T20:48:27+00:00'
type: issue
status: closed
closed_at: '2017-11-27T20:48:27+00:00'
---

# Original Description
I cant send coins from my wallet to bittrex wallet

It looked like this:

[wallet 43MhVc]:
[wallet 43MhVc]: balance
Balance: 119.954321910000, unlocked balance: 119.954321910000
[wallet 43MhVc]: transfer 1 463tWEBn5XZJSxLU6uLQnQ2iY9xuNcDbjLSjkn3XAXHCbLrTTErJrBWYgHJQyrCwkNgYvyV3z8zctJLPCZy24jvb3NiTcTJ 19.954321910000 126e621c89b84deea94e248540045e7e528cd164f434455fb09734c2b78f84b0
Wallet password: ************
Error: unexpected error: Error! What is c if cols = 1!
[wallet 43MhVc]:

This synstax is required by bittrex  transfer 1 base address amount payment id
I am using version: 0.11.1.0 Helium Hydra for Windows, 32-bit (Command-line Tools Only)
Can anyone help? Thanks a lot

# Discussion History
## iDunk5400 | 2017-11-27T20:32:34+00:00
You are trying to use an invalid ring size value. Minimum ring size is 5 (and also the default) since the September hardfork.

## moneromooo-monero | 2017-11-27T20:47:26+00:00
That error currently displays a more helpful message about too low mixin.

+resolved

# Action History
- Created by: vietanh79 | 2017-11-27T16:14:58+00:00
- Closed at: 2017-11-27T20:48:27+00:00
