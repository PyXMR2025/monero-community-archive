---
title: 'Error: failed to generate new wallet: failed to save file "testWallet.keys"'
source_url: https://github.com/monero-project/monero/issues/2369
author: Edoin
assignees: []
labels:
- invalid
created_at: '2017-08-28T18:19:16+00:00'
updated_at: '2018-01-10T12:32:22+00:00'
type: issue
status: closed
closed_at: '2017-09-30T09:18:20+00:00'
---

# Original Description
I have deployed a copy of monero for linux in centos 7 with version `Monero 'Wolfram Warptangent' (v0.10.3.1-release)`. 

I have finished synching with the mainnet using `./monerod --detached` and finished in 2 days. 

Now I am trying to create a wallet and it gives me this error `Error: failed to generate new wallet: failed to save file "testWallet.keys"` and this is my code

```./monero-wallet-cli --log-level 3 -- generate-new-wallet testWallet```

I am now stuck in this error and trying to figure out what are the missing files since I just followed what is on the documentation <https://www.monero.how/tutorial-how-to-speed-up-initial-blockchain-sync> without using the `sync boost` module. Thanks in advance.

# Discussion History
## moneromooo-monero | 2017-08-28T23:35:11+00:00
Do you have write permissions in . ?

## moneromooo-monero | 2017-09-21T08:51:54+00:00
Ping. If no reply, I'll assume you do not and close.

## moneromooo-monero | 2017-09-30T09:12:08+00:00
Looks like typical filesystem permission error.

+invalid

## AMatiasC | 2018-01-10T12:32:22+00:00
Hi, sorry! but i have the same error. I was changing permissions but I could not find the solution. The error is as follows:
"Enter the number corresponding to the language of your choice: 1
Error: failed to generate new wallet: failed to save file "test-etn.keys".

Please, help me! 
Thanks!

# Action History
- Created by: Edoin | 2017-08-28T18:19:16+00:00
- Closed at: 2017-09-30T09:18:20+00:00
