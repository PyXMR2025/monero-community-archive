---
title: monero rpc wallet shows wrong balance (too much)
source_url: https://github.com/monero-project/monero/issues/8613
author: anycolo
assignees: []
labels: []
created_at: '2022-10-17T11:15:08+00:00'
updated_at: '2024-07-31T23:17:15+00:00'
type: issue
status: closed
closed_at: '2024-07-31T23:17:15+00:00'
---

# Original Description
I generated a monero wallet long time ago using the gui wallet.
I uploaded the view only wallet to btcpayserver.
I have accepted payments for a while..

Yesterday,
I used the rpc connection to get balance. It showed the wrong amount in rpc, but the correct one in gui wallet.
I send a small amount (1 XMR) from monero gui wallet somewhere else. It shows the right amount in the gui wallet.
However, in rpc, it shows way too much balance...  almost double of X. This isn't right..

I then did this:
I generated a NEW wallet on monero wallet gui.
I sent all the money from the old wallet to the new wallet.
I generated a view only wallet to upload into btcpayserver and received this weird warning: "offset is larger than outputs" (i don't remember exactly, but it was something like that), but the view only wallet was saved and i managed to upload it into btcpayserver. It displayed right amount.
Unfortunately, after sending a small amount i again started to see too much money in rcp, but correct in gui.

Now, in the gui wallet if i try to generate view only wallet AGAIN (after moving the old view wallet to a different location), i get this error:

Imported outputs omit more outputs that we know of. Try using export_outputs all.

I think something is very wrong, maybe one of the outputs or public keys is somehow tainted, and i'm afraid that this will 'infect' any other wallet that i send this money to.

# Discussion History
## plowsof | 2022-10-17T12:24:12+00:00
gui = your hot wallet (with spend keys), rpc = view only wallet. when you spend from the monero gui, the view only wallet sees returning change as an unspent output (so increases the balance). you need to follow the same steps for cold signing (export / import key images to your view only wallet each time you spend from the hot wallet) 

## anycolo | 2022-10-18T08:47:45+00:00
This used to work before.. Both wallets displayed the correct amount. It didn't matter where i spent the money from.

## plowsof | 2022-10-18T11:21:29+00:00
if what you are saying is true then everything i know about how Monero works is a lie and we need to update the docs on this page here https://www.getmonero.org/resources/user-guides/view_only.html where key images are mentioned. 

## selsta | 2022-10-18T13:00:03+00:00
From https://www.getmonero.org/resources/user-guides/view_only.html

>If your wallet has outgoing transactions, the balance displayed will not be correct. To get a correct balance in a view-only wallet, you have to import the accompanying key images of each output of the wallet.

That's exactly what you are seeing here.

# Action History
- Created by: anycolo | 2022-10-17T11:15:08+00:00
- Closed at: 2024-07-31T23:17:15+00:00
