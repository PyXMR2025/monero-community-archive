---
title: 'Monero GUI Wallet: How do I transfer all the transaction histories from one
  wallet to another'
source_url: https://github.com/monero-project/monero-gui/issues/4172
author: ch9PcB
assignees: []
labels: []
created_at: '2023-05-07T19:01:06+00:00'
updated_at: '2023-05-09T10:00:17+00:00'
type: issue
status: closed
closed_at: '2023-05-09T10:00:17+00:00'
---

# Original Description
I am using Monero GUI Wallet (Linux), 0.18.2.2 - Fluorine Fermi and have just created a second wallet.

I wish to transfer (or copy, whatever you call it) all of the transaction histories from the first wallet to the second.

I used Google Search to look for tips before posting my question here. There is this post titled [How to clear the transaction history in the GUI wallet?](https://www.reddit.com/r/Monero/comments/cvpps0/how_to_clear_the_transaction_history_in_the_gui/) but it doesn't answer my question.

Thank you for your help.

# Discussion History
## selsta | 2023-05-07T19:02:53+00:00
You can't copy the transaction history since the transactions didn't happen inside this new wallet. Each wallet has its own history that you can't manipulate.

## ch9PcB | 2023-05-08T06:40:57+00:00
@selsta 

> Each wallet has its own history that you can't manipulate.

Suppose my motive for creating the second wallet is to have a fresh new seed; but otherwise all the transactions that occurred in the first wallet apply to the second. You can say that the second wallet is a "clone" of the first except for the 25-random-word seed.

## selsta | 2023-05-08T10:27:50+00:00
It is not possible to clone a transaction history. If you want to use a new wallet with a fresh seed, you will have to manually transfer the funds from the old wallet to the new one. The transaction history will not be copied over.

## ch9PcB | 2023-05-08T11:32:10+00:00
@selsta

If you plan to add new features to Monero GUI Wallet, please do consider the option of changing the seed of the existing wallet.

The current version, Fluorine Fermi, already allows a user to change the password of his wallet; so why not the seed as well?

## selsta | 2023-05-08T11:47:01+00:00
Can you explain why you want to change the seed?

> The current version, Fluorine Fermi, already allows a user to change the password of his wallet; so why not the seed as well?

The short answer is what you are suggesting isn't possible.

## ch9PcB | 2023-05-08T17:31:19+00:00
@selsta 

> Can you explain why you want to change the seed?

When a user suspects the seed has been compromised

## selsta | 2023-05-08T17:33:54+00:00
> When a user suspects the seed has been compromised

In this case a user has to create a new wallet and transfer the funds from the old wallet to the new wallet. Changing a seed isn't cryptographically possible.

If you want access to your old account history you can export it to `.csv`, or simply open the old empty wallet.

## ch9PcB | 2023-05-09T10:00:17+00:00
@selsta

Thank you for your tips.

I shall close this ticket.

# Action History
- Created by: ch9PcB | 2023-05-07T19:01:06+00:00
- Closed at: 2023-05-09T10:00:17+00:00
