---
title: Trezor and Ledger Devices NOT interoperable when configuring from same BIP
  39 seed words
source_url: https://github.com/monero-project/monero/issues/5744
author: skaht
assignees: []
labels: []
created_at: '2019-07-09T00:50:23+00:00'
updated_at: '2019-10-04T21:32:58+00:00'
type: issue
status: closed
closed_at: '2019-10-04T21:32:58+00:00'
---

# Original Description
This is very annoying and will cause substantial adoption user base issues in the future when it comes to wallet recovery.  

Will need to understand what Trezor is doing to synthesize addresses from BIP 39 seeds to have documented at https://monero.stackexchange.com/questions/9815/support-for-a-ledger-nano-s-recovery-plan-b/10922#10922.

# Discussion History
## skaht | 2019-09-24T00:14:44+00:00
Initialized with the worst 256-bit BIP 39 12-word test vector seeds

`% echo -n 00000000000000000000000000000000 | bx mnemonic-new`
**abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about**

After using GUI v0.14.1.0 'Boron Butterfly' (with Ledger Nano X and Trezor Model T support) and following instructions at https://wiki.trezor.io/Monero#Monero_GUI, the resulting primary account address is:
 
**44jKQv6ZKMd5ecLLmkNJGi7azgSptEq8ki7TFiat1TfLfdDQ1tQ7ZYa3cRh7X2uRwvLDjddWh97ajeyhR2seKSECQeDx1WR**

which also matches results of: 

`% trezorctl monero-get-address -n "m/44'/128'/0'"`
**44jKQv6ZKMd5ecLLmkNJGi7azgSptEq8ki7TFiat1TfLfdDQ1tQ7ZYa3cRh7X2uRwvLDjddWh97ajeyhR2seKSECQeDx1WR**

However, the address above absolutely does not correspond with results from a **Ledger Nano S** or **Ledger Nano X** behaviors that  can be mimicked with the following piped command lines, contrast to **Monero Address:** result.

`% echo "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about" | bx mnemonic-to-seed -p "" | bx hd-new | bx hd-private -d -i 44 | bx hd-private -d -i 128 |  bx hd-private -d -i 0 | bx hd-private -i 0 | bx hd-private -i 0 | bx hd-to-ec | ./kec256 | ./xmr`

    Seed                 : 907cf0eb0e0bbd761a7ed9bc8777fa5530e8262792a3e718533a1a357a1e4199
    Private Spend Key    : 3b094ca7218f175e91fa2402b4ae239a2fe8262792a3e718533a1a357a1e4109
    Private View Key     : 0f3fe25d0c6d4c94dde0c0bcc214b233e9c72927f813728b0f01f28f9d5e1201
    Public Spend Key     : dae41d6b13568fdd71ec3d20c2f614c65fe819f36ca5da8d24df3bd89b2bad9d
    Public View Key      : 865cbfab852a1d1ccdfc7328e4dac90f78fc2154257d07522e9b79e637326dfa
    Monero Address       : 49vDbkSo7eve3J41sBdjvjaBUyz8qHohsQcGtRf63qEUTMBvmA45fpp5pSacMdSg7A3b71RejLzB8EkGbfjp5PELVF2N4Zn
    Electrum Seed Words  : tavern judge beyond bifocals deepest mural onward dummy eagle diode gained vacation rally cause firm idled jerseys moat vigilant upload bobsled jobs cunning doing jobs

Other than than the HD path being shortened, it is unclear what the **Trezor Model T** is really doing to synthesize its primary account address, i.e., **44jKQv6ZKMd5ecLLmkNJGi7azgSptEq8ki7TFiat1TfLfdDQ1tQ7ZYa3cRh7X2uRwvLDjddWh97ajeyhR2seKSECQeDx1WR**.




## prusnak | 2019-09-29T17:24:43+00:00
Trezor is using [SLIP-0010](https://github.com/satoshilabs/slips/blob/master/slip-0010.md) which is not used by Ledger. Ledger uses BIP32 to generate a secp256k1 private key, then they convert this key to ed25519 by hashing it, which is quite funky.

This was already raised one year ago in https://github.com/monero-project/monero/issues/4704 but there was no reaction from Monero or Ledger developers.

## skaht | 2019-10-01T03:37:24+00:00
@prusnak - Thanks for the pointer to demystify matters:-) Only need to get bitcoin-explorer (bx) command line to be SLIP-10 enabled for the ed25519 elliptic curve. 

The succinct answer from your feedback is found at https://github.com/trezor/trezor-core/tree/master/docs/coins#list-of-used-derivation-paths. This table provides top level logical **SLIP-10** details for HD key synthesis paths. 

With the **ed25519** private spend key, it is possible to derive the associated Monero Electrum words. At https://github.com/skaht/XMR, the **bytes_to_words** command line example towards the bottom of the page can be applied to synthesize Monero Electrum seed words. I believe this should enable independent source code to recreate traditional Monero Electrum wallet recovery seed words from a configured Trezor Model T's BIP 39 seed words.

## skaht | 2019-10-01T04:04:23+00:00
@prusnak  - It would be really useful if there was an additional **trezorctl** command where one can specify BIP 39 seed words and an optional BIP 39 passphrase with a Monero account number and the result will be 25 Monero Electrum seed words that could be used to configure other Monero wallets in a pinch. 

This would provide the functionality of  https://github.com/LedgerHQ/ledger-app-monero/tree/master/tools/python documented at https://monero.stackexchange.com/questions/9815/support-for-a-ledger-nano-s-recovery-plan-b/10922#10922. 

This Ledger Python code gave customers options when Ledger messed up during a Monero hard fork upgrade earlier this year. Most people unaware could not access their Nano S stored XMR for a few weeks until Ledger fixed the issue it introduced.

Having a **Plan B** for accessing Monero contained within a Trezor Model T would be prudent capability for customers to have, albeit primarily for power users and cybersecurity professionals.

## prusnak | 2019-10-01T10:33:31+00:00
> It would be really useful if there was an additional trezorctl command where one can specify BIP 39 seed words and an optional BIP 39 passphrase

This really does not belong to trezorctl, because the thing you want to achieve has nothing to do with Trezor. It is just converting seed from one format (general standard) to another. It might make sense to create such tool within Monero community, though.

## skaht | 2019-10-01T23:50:06+00:00
Makes sense. SLIP-10 enabling the libbitcoin-explorer (bx) HD wallet command line interface can be one approach for accomplishing what you are suggested above outside the Monero Community.

## prusnak | 2019-10-02T07:38:51+00:00
Let's close this.

## skaht | 2019-10-04T21:32:54+00:00
Agreed, it makes sense to close #5744. There is no issue with Monero BIP 39 seed word interoperability between different vendor devices as long as there are independent open sources available to synthesize associated Monero keys and address for the different vendors. The libbitcoin dev team is thinking (very limited bandwidth) about supporting SLIP-10 tech that is applied by Trezor..

A work-in-progress summary of how Trezor Model T synthesize keys and addresses is posted at the bottom of https://monero.stackexchange.com/questions/9815/support-for-a-ledger-nano-s-recovery-plan-b/10922#10922, while details for Ledger Model S or Model X are posted up top.

Thanks for your assist:-)

# Action History
- Created by: skaht | 2019-07-09T00:50:23+00:00
- Closed at: 2019-10-04T21:32:58+00:00
