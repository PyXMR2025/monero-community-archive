---
title: Deterministically generate transaction key
source_url: https://github.com/monero-project/monero/issues/6638
author: ghost
assignees: []
labels: []
created_at: '2020-06-10T11:18:31+00:00'
updated_at: '2020-06-12T15:53:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After transactions are created it may still be useful to know the transaction key to prove payment to an auditor for example. A problem with Monero wallets at the moment is that transaction keys are created completely randomly meaning upon loss of the wallet and restoration from a mnemonic seed the transaction keys are permanently lost. This could be remedied by generating the transaction key deterministically from wallet parameters and input parameters leading to a fully recoverable wallet.

# Discussion History
## SarangNoether | 2020-06-10T13:40:14+00:00
What exactly would you intend to be proved about the transaction in this case? Simply a proof of knowledge of the transaction private key corresponding to the given transaction public key?

## ghost | 2020-06-11T13:53:19+00:00
Well yes you can use the private transaction key to prove you created a payment without having to reveal your private view key for example

## SarangNoether | 2020-06-11T15:55:12+00:00
If properly implemented, this would also have the benefit of mitigating against poor random number generation. A bad random number generator would negatively affect other areas of transaction construction, of course.

## UkoeHB | 2020-06-11T16:11:16+00:00
My concern is if a person's private keys are compromised and tx private keys are deterministic, then the compromiser will be able to figure out the recipients of all his transactions. 

Moreover, knowing tx private keys isn't enough to prove payment to an auditor, as the recipient addresses are also required. Since recipient addresses must be stored anyway, not much is gained/lost whether or not the tx private keys are stored.

## moneromooo-monero | 2020-06-11T16:12:00+00:00
You can prove payment without having to give a tx key.

## SarangNoether | 2020-06-11T16:13:09+00:00
Right, but a proof of knowledge of the transaction key is one simple way that also has the benefit of reducing reliance on random number generation.

## ghost | 2020-06-11T19:37:53+00:00
Don't you have to reveal your private view key to be able to prove payment with the tx key?

## SarangNoether | 2020-06-11T19:40:15+00:00
There are different types of transaction proofs available. You could sign messages with the transaction private key that can be verified with only the transaction public key, without revealing secret data.

## ghost | 2020-06-12T06:09:58+00:00
Yeah I mistyped I meant don't you have to reveal your private view key to be able to prove payment **without** the transaction private key?

## SarangNoether | 2020-06-12T12:41:40+00:00
There are other things you can prove without it, like being able to sign using the output private key against the key image (which reveals the public key), or generating a new signature using the same ring and key image.

## stoffu | 2020-06-12T15:39:27+00:00
> or generating a new signature using the same ring and key image.

FWIW, this is what spend proofs do (see `get/check_spend_proof` command).

## UkoeHB | 2020-06-12T15:53:53+00:00
Ch. 8 of [ZtM2](https://web.getmonero.org/library/Zero-to-Monero-2-0-0.pdf) discusses all the transaction proofs in Monero (and some that don't exist yet).

# Action History
- Created by: ghost | 2020-06-10T11:18:31+00:00
