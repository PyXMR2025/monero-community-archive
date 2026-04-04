---
title: Support transaction key in Check Transaction section
source_url: https://github.com/monero-project/monero-gui/issues/2431
author: rating89us
assignees: []
labels: []
created_at: '2019-11-10T19:11:04+00:00'
updated_at: '2019-12-08T10:03:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
According to https://web.getmonero.org/resources/user-guides/prove-payment.html, transaction verification requires three pieces of information:
- Transaction ID
- Recipient address
- Transaction key

Alternatively, when transaction key is not available, a spend transaction proof (tx proof or _Spend Proof_) can be used, which is a string that can be obtained with the P button in GUI and starts with "SpendProofV1...". 

The Advanced > Prove/check page > Check Transaction in GUI has four fields:
- Transaction ID
- (Recipient) Address
- Message (optional)
- Signature

![image](https://user-images.githubusercontent.com/45968869/68549248-85367c00-03f6-11ea-9fa7-157b585efa60.png)

The problem: the signature field in this page only accepts _Spend proof_ (the SpendProofV1... generated when clicking the P button) as a proof, and it doesn't accept a _Transaction key_ as a proof. 

Most Monero desktop and mobile wallets provide the Transaction key of past transactions, but they don't provide the Spend proof (which can only be obtained in Monero GUI and CLI). 

Therefore, currently it's not possible to verify a transaction in Monero GUI if the user provides you transaction ID + recipient address + transaction key. In this case verification must be done in Monero CLI (using the command _check_tx_key TXID TXKEY ADDRESS_) or external websites (like https://www.exploremonero.com/receipt or https://xmr.llcoins.net/checktx.html)

My suggestion:
- Add a Transaction Key field (a 5th field): this way users can input either the transaction key or the transaction proof (SpendProofV1) to verify a transaction.
- Update instructions: "_As a signature, you can either use a transaction key (tx key) or a Spend Proof (tx proof). For the case with Spend Proof, you don't need to specify the recipient address._"

# Discussion History
# Action History
- Created by: rating89us | 2019-11-10T19:11:04+00:00
