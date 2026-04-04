---
title: 'Feature request: request payment in multiple outputs'
source_url: https://github.com/monero-project/monero-gui/issues/2541
author: rating89us
assignees: []
labels: []
created_at: '2019-12-02T07:05:48+00:00'
updated_at: '2019-12-02T07:43:20+00:00'
type: issue
status: closed
closed_at: '2019-12-02T07:43:20+00:00'
---

# Original Description
Having a single output in the wallet is a potential problem for senders of Monero, since the incoming change output is always locked for 10 blocks (~20 min).

Some proposed solutions included making the wallet suggest the user to do a transaction that splits its single output into multiple outputs. I propose a different solution, that is to make the wallet request multiple outputs when it is running low of outputs. This could be when it is receiving a payment for the first time or when the wallet has only 1-2 spendable outputs.

This could be done by _Receive page_ displaying a large QR code requesting a payment that creates multiple outputs. I'm not familiar with how "send to multiple addresses" function works, but here are some ideas:

**Example:** 
Bob wants to receive 0.5 XMR from Alice. Bob's wallet hasn't made any transactions yet.

**A) Request payment in multiple outputs for a single address**
Bob's wallet displays a large QR code cointaining a payment request for a transaction that creates multiple outputs in the same address:
- 0.1 XMR -> Address A
- 0.1 XMR -> Address A
- 0.1 XMR -> Address A
- 0.1 XMR -> Address A
- 0.1 XMR -> Address A

Request link: monero://48...(XMR address)...?tx_amount=0.5&outputs=5

**B) Request payment in multiple outputs for multiple addresses**
Bob's wallet displays a large QR code cointaining a payment request for a transaction that creates multiple outputs in multiple addresses:
- 0.1 XMR -> Address A
- 0.1 XMR -> Address B
- 0.1 XMR -> Address C
- 0.1 XMR -> Address D
- 0.1 XMR -> Address E

In both cases, if Alice accepts this special type of payment request, her wallet will create a transaction that pays for multiple addresses (but for a single user), with a transaction fee a little higher than usual.

# Discussion History
# Action History
- Created by: rating89us | 2019-12-02T07:05:48+00:00
- Closed at: 2019-12-02T07:43:20+00:00
