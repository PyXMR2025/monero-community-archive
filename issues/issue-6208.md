---
title: 'Feature request: request payment in multiple outputs'
source_url: https://github.com/monero-project/monero/issues/6208
author: rating89us
assignees: []
labels: []
created_at: '2019-12-02T07:49:30+00:00'
updated_at: '2019-12-02T18:05:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Having a single output in the wallet is a potential problem for senders of Monero, since the incoming change output is always locked for 10 blocks (~20 min).

Some proposed solutions included making the wallet suggest the user to do a transaction that splits its single output into multiple outputs. I propose a different solution, that is to make the wallet request multiple outputs when it is running low of outputs. This could be when it is receiving a payment for the first time or when the wallet has only 1-2 spendable outputs.

Implementation: 
- CLI wallet: a request link is created asking for a payment in multiple outputs
- GUI wallet: Receive page displays a large QR code requesting a payment in multiple outputs

**Example:**
Bob wants to receive 0.5 XMR from Alice. Bob's wallet hasn't made any transactions yet.

**A) Request payment in multiple outputs for a single address**
Bob's wallet displays a large QR code cointaining a payment request for a transaction that creates multiple outputs in the same address:

- 0.1 XMR -> Address A
- 0.1 XMR -> Address A
- 0.1 XMR -> Address A
- 0.1 XMR -> Address A
- 0.1 XMR -> Address A

Request link: _monero://48...(Address A)...?tx_amount=0.5&outputs=5_

**B) Request payment in multiple outputs for multiple addresses**
Bob's wallet displays a large QR code cointaining a payment request for a transaction that creates multiple outputs in multiple addresses:

- 0.1 XMR -> Address A
- 0.1 XMR -> Address B
- 0.1 XMR -> Address C
- 0.1 XMR -> Address D
- 0.1 XMR -> Address E

Request link: _monero://(Address A)(Address B)(Address C)(Address D)(Address E)?tx_amount=0.5&outputs=5_

In both cases, if Alice accepts this special type of payment request, her wallet will create a transaction that pays for multiple addresses (but for a single user), with a transaction fee a little higher than usual.

# Discussion History
## moneromooo-monero | 2019-12-02T12:33:01+00:00
This seems to leak information about the wallet's output makeup.

## rating89us | 2019-12-02T17:13:23+00:00
And what if instead of leaking for the receiver the wallet's output makeup, the wallet leaked only the information that a multiple address transaction was made?

When running low of outputs, the wallet could automatically transform a normal transaction into a multiple addresses one, which will end up paying the original receiver and creating new outputs to the wallet itself. External observers and the receiver can't know if the transaction was paying for multiple addresses or it was just the wallet creating outputs.

Also, the minimum number of outputs in a transaction could be increased from 2 to 3. This way the wallet can create an extra output for every input that is spent, while doing a "conventional" transaction with 3 outputs (payment + change + new output). Not sure how much would this bloat the blockchain.

## hyc | 2019-12-02T17:32:21+00:00
Increasing minimum outputs from 2 to 3 just means you've increased the number of outputs that are likely to be going back to the sender. Not a good privacy feature...

## moneromooo-monero | 2019-12-02T18:05:37+00:00
Automatically splitting change might be a good idea. I like this idea. Those txes seem impossible to tell from those with two recipients and one change with just blockchain data. Though since they go back to the same account, they could be linked later, which would give a clue. Still, I think it's a good idea. Do you want to propose it in #monero-dev or #monero-research-lab ? If you're not on IRC or a bridge I can do it.
I don't like the minimum change though.

# Action History
- Created by: rating89us | 2019-12-02T07:49:30+00:00
