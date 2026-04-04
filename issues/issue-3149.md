---
title: '[Wallet API] Plan for upgrading restoreFromKeys'
source_url: https://github.com/monero-project/monero/issues/3149
author: stoffu
assignees: []
labels:
- invalid
created_at: '2018-01-17T22:49:19+00:00'
updated_at: '2018-09-14T16:01:29+00:00'
type: issue
status: closed
closed_at: '2018-09-14T12:16:59+00:00'
---

# Original Description
As per https://github.com/monero-project/monero/pull/3104#issuecomment-357505047:

1. **(done, #3104)** Introduce a new function `restoreFromKeysWithPassword`, and mark `restoreFromKeys` as deprecated.

2. After one release cycle, remove `restoreFromKeys`. All API users should be using `restoreFromKeysWithPassword` at this point.

3. After another release cycle, bring back `restoreFromKeys` again which is just an alias to `restoreFromKeysWithPassword`, and mark `restoreFromKeysWithPassword` as deprecated.

4. After another release cycle, remove `restoreFromKeysWithPassword`. All API users should be using `restoreFromKeys` with the upgraded functionality at this point.


# Discussion History
## moneromooo-monero | 2018-01-17T22:56:40+00:00
That sounds like a lot of trouble. I'd rather we don't treat this as a stable API since it's obviously far from stable yet, but then if someone wants to do the work I won't stop them.

## stoffu | 2018-01-17T23:03:23+00:00
@moneromooo-monero 
I also had a similar opinion (https://github.com/monero-project/monero/pull/3104#issuecomment-357429844):

> Now I'm wondering - is it really necessary to keep the deprecated version for backward compatibility? AFAIK only software products that use the wallet API are Monerujo and monero-wallet-gui. Can't we just introduce the new function signatures and force the users (Monerujo & monero-wallet-gui) to upgrade their code?

but it wasn't supported. CC @dEBRUYNE-1 @m2049r 

## m2049r | 2018-01-23T18:04:10+00:00
let's pretend it's stable and see how it goes :)

## moneromooo-monero | 2018-09-14T12:07:32+00:00
So this was abandoned.

+invalid


## m2049r | 2018-09-14T16:01:29+00:00
? so you are keeping the totally unsecure ```restoreFromKeys```? it should have the functionality of ```restoreFromKeysWithPassword```. and so ```restoreFromKeysWithPassword``` has no purpose any longer.

# Action History
- Created by: stoffu | 2018-01-17T22:49:19+00:00
- Closed at: 2018-09-14T12:16:59+00:00
