---
title: Restore with 24 words
source_url: https://github.com/monero-project/monero-gui/issues/1326
author: snirp
assignees: []
labels:
- invalid
created_at: '2018-04-17T18:23:02+00:00'
updated_at: '2019-09-05T02:00:34+00:00'
type: issue
status: closed
closed_at: '2019-09-05T02:00:34+00:00'
---

# Original Description
When restoring the wallet from the seed, you are given the option to enter 24 or 25 words. My assumption is that this is supposed to allow you to skip the checksum word. After entering 24 words, the `>` button is activated, but it fails to verify. Only after entering the correct checksum word are you able to continue.
 
This is somewhat confusing.

# Discussion History
## skaht | 2018-07-06T02:51:48+00:00
Hopefully, the following might provide a context to clear things up. 

I believe, but not certain, 24 seed words could be associated with the BIP 39 Standard that is natively supported by hardware wallets, e.g., Ledger, Trezor. It will be interesting to know if 24 words are supplied that they must be BIP 39 words, and if 25 words (--restore-deterministic-wallet, --electrum-seed) are supplied that they must be traditional Monero Electrum words? (It is worth noting the Electrum Seed Word Standard is a few years older than the BIP 39 Standard.)

The [**BIP 39 Standard**](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) (natively used by hardware wallets) supports restoration using 12, 15, 18, 21, or 24 words.  Production Bitcoin-like wallets using the BIP 39 Standard tend to support restoration with 12, 18, and 24 seed words. When 12 restoration seed words are used, those words provide a 4-bit checksum.  While at the other extreme, 24 words provide a 8-bit checksum.  In all cases, the checksum is taken care of by the last word.  However, the last word embodies more information than just a checksum. Skipping the last checksum word in the BIP 39 Standard will muck everything up, see https://bitcoin.stackexchange.com/questions/68605/how-to-generate-a-valid-hash-for-a-bip39-seed-phrase/75314#75314.

We don't want end users to confuse the BIP 39 standard that has 2048 words for multiple spoken [**languages**](https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md) with the traditional Monero 1626  Electrum words located [**here**](https://github.com/monero-project/monero/tree/master/src/mnemonics) in various header files.  

With the exception of [myMonero](https://mymonero.com/#/) wallets, traditional software-based Monero wallets use 25 words for restoration.  As you appear to already know, the 25th Electrum word of a sequence of words for restoring a Monero wallet, is always a repeat of one of the previous 24 words.  (This generally is not the case for the BIP 39 Standard.) Without the 25th word, the Electrum checksum is effectively bypassed. 

@snirp - Please provide a response to what you know to be the actual case. I'm wondering if there is a hidden undocumented feature you have run across that could provides a "Plan B" way out for those experimenting with new Ledger device capabilities. Such an ability existed 18 months ago when a Monero Trezor alpha implementation existed. 

## stoffu | 2018-07-06T06:15:52+00:00
@snirp 
> After entering 24 words, the > button is activated, but it fails to verify. 

What do you mean by "fail to verify"? I cannot reproduce it; restoring a wallet with a 24-word seed using the GUI just works for me. Please provide more details with screenshots etc.

@skaht 
BIP39 is not relevant for Monero's deterministic wallet restoration scheme.


## skaht | 2018-07-06T15:01:11+00:00
@stoffu - Concur that **--restore-deterministic-wallet** has nothing to do with **BIP 39**. Is only associated with Electrum words. Looking like the **BIP 39** is related to the configuration of hardware wallets only that support Monero. 

Are you aware of any existing tools to compute Electrum seed words out-of-band for each address that a Ledger Nano S produces (configured with one set of BIP 39 seed words)?  18 months ago, prior Monero alpha Trezor software had such a monetary wallet safety mechanism.

## stoffu | 2018-07-06T15:46:12+00:00
@skaht 
I don't know anything about the internal workings of Ledger Nano S.


## skaht | 2018-07-06T15:57:27+00:00
@stoffu 
I might be able to quickly help with that at a logical level for both Ledger and Trezor. 

See https://github.com/libbitcoin/libbitcoin/wiki/Altcoin-Version-Mappings#7-bitcoin-btc-bip-3944-technology-examples for the quick command line level UNIX piped examples. In particular, I need to update https://github.com/libbitcoin/libbitcoin/wiki/Altcoin-Version-Mappings#10-monero-xmr-bip-3944-technology-examples to effectively mimic what Ledger is logically doing.

## selsta | 2019-09-05T01:56:24+00:00
>  cannot reproduce it; restoring a wallet with a 24-word seed using the GUI just works for me.

Same here. Please comment if you can explain how to reproduce this issue.

+invalid

# Action History
- Created by: snirp | 2018-04-17T18:23:02+00:00
- Closed at: 2019-09-05T02:00:34+00:00
