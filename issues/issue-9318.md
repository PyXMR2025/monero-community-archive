---
title: aggregating multisig partial signatures
source_url: https://github.com/monero-project/monero/issues/9318
author: SepehrDamavandi
assignees: []
labels:
- wallet
created_at: '2024-05-05T02:46:20+00:00'
updated_at: '2024-06-10T03:21:51+00:00'
type: issue
status: closed
closed_at: '2024-06-10T03:21:51+00:00'
---

# Original Description
I ran a M/N multi signature account locally. From what I noticed, there is no aggregation command in cli-wallet or RPC to aggregate partial signatures and the process of finalizing transactions has a sequential order.  Alice who generates the transaction needs to send it to Bob, Bob needs to sign and pass to Carol and so on, until the transaction is signed by the threshold size and ready to be submitted. Are there any commands or RPC API for Alice to be able to gather all the signatures from collaborators and aggregate them to make and submit the final transaction? In other words, I want the process to be done not in sequential order but in parallel. 
Also, I noticed that there is a maximum limit(16) on signer numbers participating in the multisig account. You have mentioned that in order to be able to support more signers efficiently, the key exchange phase should be done FROST style. Is there an implementation of this? how can I remove the limit of signers?

# Discussion History
## SepehrDamavandi | 2024-05-07T03:41:51+00:00
Is it even possible to aggregate partial signatures from one wallet? or should it have this sequential order?


## SepehrDamavandi | 2024-05-09T13:06:56+00:00
ANYONE?

## selsta | 2024-05-18T23:59:10+00:00
@UkoeHB can you answer this?

## UkoeHB | 2024-05-19T01:29:21+00:00
The current implementation does round-robin signing. The 16-signer limit exists because wallet setup becomes extremely slow with larger group sizes. 

I have aggregation-style signing implemented for CLSAG in the Seraphis library, but actually changing the wallet workflow to use it would require quite a lot of implementation and review work. I wouldn't bet on seeing it in the monero repo for at least a year.

## SepehrDamavandi | 2024-05-20T18:06:50+00:00
@UkoeHB Do you have an implementation of this aggregation-style for CLSAG? 

## UkoeHB | 2024-05-20T19:01:56+00:00
Yes, [here](https://github.com/UkoeHB/monero/blob/60c5d7e8058008e6b755c0ceadb86c1fd88b52cf/tests/unit_tests/multisig_signing.cpp#L579) is a test for it.

## SepehrDamavandi | 2024-05-22T15:56:45+00:00
Thank you, @UkoeHB I appreciate it.

Is it true that changing the key aggregation style from MuSig2 to FROST would require changings in the wallet functions that handle multisig operations?  or are they both endup with each participant having `N - M + 1` private keys? 

And about the Seraphis library, does it provide the siggnature aggregation command through RPC API? 

 

## UkoeHB | 2024-05-22T22:04:25+00:00
> Is it true that changing the key aggregation style from MuSig2 to FROST would require changings in the wallet functions that handle multisig operations? or are they both endup with each participant having N - M + 1 private keys?

You'd need an entirely new multisig account management/setup API.

> And about the Seraphis library, does it provide the siggnature aggregation command through RPC API?

No, only the backend functionality is implemented.

# Action History
- Created by: SepehrDamavandi | 2024-05-05T02:46:20+00:00
- Closed at: 2024-06-10T03:21:51+00:00
