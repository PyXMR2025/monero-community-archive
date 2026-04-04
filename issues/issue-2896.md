---
title: '[Feature] separate, shorter mnemonic for public address'
source_url: https://github.com/monero-project/monero/issues/2896
author: nasaWelder
assignees: []
labels: []
created_at: '2017-12-07T23:18:38+00:00'
updated_at: '2017-12-13T05:37:05+00:00'
type: issue
status: closed
closed_at: '2017-12-13T05:36:29+00:00'
---

# Original Description
Private seed mnemonic really helps me feel confident that I copied things down. And some people are dyslexic... However on cold storage computer I'm getting really paranoid that I'll send funds to nowhere if I mess up the public Address.

Prevailing wisdom says to copy addresses several times which just increases chance for human error, then there's error in typing it into exchange for use.

QR codes are ok but not helpful for architectures that don't have gui deployed like raspPi(arm7). I also don't like the idea of having to trust my QR code reader also since not human readable. 

I'm sure there's a way to design scheme that won't confuse people with private seed, such as different dictionary, word amount, perhaps more.



# Discussion History
## dEBRUYNE-1 | 2017-12-08T11:05:14+00:00
>However on cold storage computer I'm getting really paranoid that I'll send funds to nowhere if I mess up the public Address.

Just as fyi, you can always verify your transaction by setting up a view only wallet or "decrypting" the transaction on a block explorer:

https://monero.stackexchange.com/questions/6137/how-do-i-as-a-recipient-verify-that-my-transaction-actually-arrived



## moneromooo-monero | 2017-12-10T00:21:53+00:00
The public address has a checksum.

Changing the encoding format would not solve the problem anyway.

## nasaWelder | 2017-12-10T20:52:16+00:00
@moneromooo-monero so should I delete this? 

## moneromooo-monero | 2017-12-11T12:59:14+00:00
If your problem was just a typo in a public address meaning lost monero, yes. Easy to try yourself by the way, and run "set always-confirm-transfers 1" set prior to the test.

## nasaWelder | 2017-12-13T05:37:05+00:00
Not very useful idea, it turns out.

# Action History
- Created by: nasaWelder | 2017-12-07T23:18:38+00:00
- Closed at: 2017-12-13T05:36:29+00:00
