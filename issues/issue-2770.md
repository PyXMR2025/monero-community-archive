---
title: Received transaction not showing up in the wallet (with integrated address)
source_url: https://github.com/monero-project/monero-gui/issues/2770
author: nexon33
assignees: []
labels: []
created_at: '2020-02-07T19:44:13+00:00'
updated_at: '2020-02-09T14:27:18+00:00'
type: issue
status: closed
closed_at: '2020-02-09T14:27:18+00:00'
---

# Original Description
A while ago I received an xmr transaction to my wallet, however I had to use an integrated address for this and couldn't find any way to generate one in the wallet itsself.

I will loop through what exactly I did to cause this issue but first I will provide evidence this is a bug.
So to start off, when I go into the wallet-cli it will show an incorrect balance because that xmr transaction is not included, but when I type in the cli "check_tx_key <my txid> <tx key> <address>"
It will show that the xmr is received. It doesn't matter if I put the integrated address or the subaddress used to generate the integrated address, it will always show the received balance.
If I do the same check on xmrchain.net it will also confirm that the transaction has been received.

How did I generate the integrated address?

I used https://dustinlemos.com/integrated-address-demo/ and entered my subaddress, this generated an integrated address which I first checked using https://xmr.llcoins.net/addresstests.html by entering my subaddress and afterwards entering my integrated address and confirming that the standard xmr address of both addresses where equal. This was in fact the case.

Do I still have all the information about this transaction?

Yes I do still have the integrated address, the subaddress I used, the payment id of the integrated address that I generated and the secret view key of the transaction as well as the txid. If you need those to check then please provide me an email or other way to contact you and send the information too.

What have I tried to solve it?

Redownloading the whole blockchain to see if the blockchain wasn't corrupted. I also tried installing the xmr wallet on another pc and see if that would give different results, but sadly it didn't.

Any other important information:

I use a Ledger nano s hardware device to log into the monero wallet.

# Discussion History
# Action History
- Created by: nexon33 | 2020-02-07T19:44:13+00:00
- Closed at: 2020-02-09T14:27:18+00:00
