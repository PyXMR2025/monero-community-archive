---
title: import sweep transactions into view wallets
source_url: https://github.com/monero-project/monero/issues/3208
author: Mansarde
assignees: []
labels: []
created_at: '2018-01-30T12:29:23+00:00'
updated_at: '2022-12-08T11:27:36+00:00'
type: issue
status: closed
closed_at: '2022-12-08T11:27:36+00:00'
---

# Original Description
As far as I understand, a view wallet can already see any transaction on the blockchain that has outputs destined for the wallet.
And by importing the key images of those transactions into that view wallet it becomes aware of which of these outputs has already been spent.

But if, for example, I sweep XMR that don't go back to the wallet's address but to someone else's, then the view wallet can't see that transaction.
I'm aware that the reason for that is because that kind of transaction does not contain any outputs that goes back to the wallet.

Now, because a full hot wallet which was restored from a seed _can_ see those wallet-leaving sweep transactions, I assume it's because of the private spend key.

### **So my question is:**
Would it be possible, hypothetically, to make a view wallet aware of these kinds of transactions (i.e. ones that don't have outputs destined for the wallet, but which were sent from the wallet nonetheless) by importing that information into it in some way?
Or would that create a vulnerability?

### **The reason I ask:**
Because `show_transfers` doesn't show sweep transactions that went to _another_ wallet, the sum of all the shown transactions doesn't equal the (correct) balance of the view wallet.
What if an auditor would like to see all transfers that were happening, including sweeps to other wallets, not just incoming transactions and whether they were spent?

### EDIT:
~~I remember reading somewhere else (another issue) that the zero-change output of a sweep is always sent to a random address. What if we sent the zero-change output back to the same wallet?
Wouldn't that make it possible for the view wallet to see sweep transactions we made to other wallets?~~

---

## Steps to reproduce:
1. Download Monero CLI v0.13.0.4
2. Create full testnet wallet "FULL" with this command:
`monero-wallet-cli --daemon-address testnet.xmrchain.net:28081 --trusted-daemon --testnet`
3. Receive 1 XMR to this wallet via https://dis.gratis/ or https://community.xmr.to/faucet/testnet or a similar service.

4. In the FULL wallet, get the view-key via the "viewkey" command and use it to create a view-only wallet "VIEW" with this command:
`monero-wallet-cli --daemon-address testnet.xmrchain.net:28081 --trusted-daemon --testnet --generate-from-view-key VIEW`
5. Send everything of the FULL wallet back to the faucet address (or any **other** wallet) via sweep_all:
`sweep_all elevated <RECEIVER-ADDRESS>`

6. When the transaction has the sufficient amount of confirmations, `refresh` the FULL wallet and verify via `show_transfers` that the outgoing transaction is shown.
7. Export the outputs and key images from the FULL wallet via these commands:
`export_outputs FULL_OUTPUTS`
`export_key_images FULL_KEY_IMAGES`
8. Copy the files FULL_OUTPUTS and FULL_KEY_IMAGES to the VIEW wallet's folder.
9. Switch to the VIEW wallet, `refresh` it and afterwards execute these commands:
`import_outputs FULL_OUTPUTS`
`import_key_images FULL_KEY_IMAGES`
10. `refresh` the VIEW wallet again for good measure and finally execute `show_transfers`.

## Observation:
The VIEW wallet only shows the initial incoming transaction of 1 XMR (received from the faucet) but not the outgoing transaction from the sweep_all command (of step 5).
## Expectation:
After importing the outputs and key images to the view wallet it should show "sweep_all" transactions that went to other wallets, just like the FULL wallet does.

# Discussion History
## dEBRUYNE-1 | 2018-01-30T13:47:06+00:00
>But if, for example, I sweep XMR that don't go back to the wallet's address but to someone else's, then the view wallet can't see that transaction.

It can if you imported the corresponding key images of all outputs. 

Please clarify whether your talking about a view wallet with import key images or without. 

## moneromooo-monero | 2018-01-30T13:47:23+00:00
The hot wallet can see those with the key images, which can be imported from the cold wallet (which needs the outputs from the hot wallet, another export/import). This is unrelated to whether an outgoing tx has any change.

## Mansarde | 2018-01-30T16:03:56+00:00
First of all, thanks for the responses, much appreciated!
>It can if you imported the corresponding key images of all outputs.
>
>Please clarify whether your talking about a view wallet with import key images or without.

I'm talking about a view wallet into which I always import all outputs and key images after any new transactions occurred.

>The hot wallet can see those with the key images, which can be imported from the cold wallet (which needs the outputs from the hot wallet, another export/import). This is unrelated to whether an outgoing tx has any change.

I tested the following on testnet, with a CLI compiled from master (on Jan 26):
When creating a view wallet _before_ a `sweep_all` is made from the hot wallet to another wallet, then the view wallet can indeed see that transaction as well (see pictures below).
But when I create the view wallet _after_ the `sweep_all`, then even after importing the outputs and key images from the hot wallet into the view wallet, the view wallet doesn't show that transaction (even though the balance is now correct).

Result of `sweep_all` on view-wallet that was *created* _before_ `sweep_all` (+ importing of outputs and key images):
![View-Wallet before](https://i.imgur.com/n4I4h79.png)
Result of `sweep_all` on view-wallet that was created _after_ `sweep_all` (+ importing of outputs and key images):
![View-Wallet after](https://i.imgur.com/kSf2zoI.png)

The transaction `b7985c92b2ff89350ff519efae9a4a33105fe72daf3d5536a8f870bdd418b82d` was a `sweep_all` back to the wallet and can be seen on both view-wallets.
But transaction `62a09d4a5ae5cf87f1c637b0bc429b055e2ff89151b9cea8fdcda528a9d6c3ee` is a `sweep_all` to another wallet and can not be seen by the view-wallet that was created _after_ the transaction was made (even after importing outputs and key images from the hot wallet).

Is this intended behaviour, or am I doing something wrong?

## moneromooo-monero | 2018-01-30T16:36:25+00:00
It should work. If it doesn't, either you made a mistake, or it's a bug. You say you imported all as you're supposed to, so it looks like it may be a bug at the moment. I'll have to test here to check.

## Mansarde | 2018-01-30T16:49:51+00:00
>It should work. If it doesn't, either you made a mistake, or it's a bug. You say you imported all as you're supposed to, so it looks like it may be a bug at the moment. I'll have to test here to check.

For what it's worth when importing the key images to that second view-wallet, then the output shows only the two transactions which have been spent, but not the transaction with the sweep to another wallet:
![](https://i.imgur.com/jvMm1ya.png)

If there's anything else you need from me to reproduce this behaviour, let me know. :)

## dEBRUYNE-1 | 2018-02-05T11:10:10+00:00
@Mansarde - I can't reproduce this with a master build. Could you try these steps?

1. Send 1 (t)XMR from wallet A to wallet B.

2. Send 0.1 (t)XMR back from wallet B to wallet A.

3. Create view-only wallet for wallet B.

4. `export_key_images` from wallet A.

5. `import_key_images` in wallet B.

6. `sweep_all` from wallet B to wallet A

On my end the hotwallet sees the outgoing sweep_all. 

## Mansarde | 2019-01-03T12:59:38+00:00
@dEBRUYNE-1 
My apologies for the late answer. It went under my radar due to some changes in my life.
I've now tried to reproduce both what I did in the OP as well as what you asked me to do.
I wasn't able to do step 5 of your post, because when I try to import key images or outputs from a different wallet I get these warnings:
`Error: Failed to import outputs OUTPUTS: Failed to decrypt outputs: Failed to authenticate ciphertext`
`Error: Failed to import key images: Failed to decrypt KEY_IMAGES: Failed to authenticate ciphertext`

I've updated the OP with detailed steps to reproduce the OP issue with Monero CLI v0.13.0.4

## Mansarde | 2022-12-08T11:27:29+00:00
Since this was in a now very old version and I'm not up-to-date with all the changes since then, I'm closing this.

# Action History
- Created by: Mansarde | 2018-01-30T12:29:23+00:00
- Closed at: 2022-12-08T11:27:36+00:00
