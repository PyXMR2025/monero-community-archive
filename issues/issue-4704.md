---
title: Derivation scheme for HW wallets
source_url: https://github.com/monero-project/monero/issues/4704
author: tsusanka
assignees: []
labels: []
created_at: '2018-10-23T09:50:02+00:00'
updated_at: '2025-06-25T12:24:20+00:00'
type: issue
status: closed
closed_at: '2019-10-03T13:59:35+00:00'
---

# Original Description
In our upcoming Monero implementation for Trezor, we plan to use [SLIP-0010](https://github.com/satoshilabs/slips/blob/master/slip-0010.md) as our primary derivation method.

If I'm not mistaken the current Ledger implementation uses BIP-32 scheme with secp256k1 and then converts the secp256k1 point into a ed25519 point. SLIP-0010 takes a different apporach and specifies how to derive a BIP-32-like path on ed25519 curve directly.

Does Monero have any opinion on this? We believe the Monero community should agree on some "standard" to allow compatibility between different HW vendors. Failing to do so would lead to an inconsistency where the same mnemonic seed does not converge to the same wallet.

We strongly suggest this to be SLIP-0010, mostly becuase Ledger's way adds another dependency for the hardware wallet: the secp256k1 curve (Monero does not need it otherwise). In case there is some Monero-only minimalistic HW, it would need to implement secp256k as well, which seems unfortunate.

cc @cslashm 

# Discussion History
## lacksfish | 2018-10-23T10:00:21+00:00
I can imagine that there could be some security concerns from reusing the same point accross several elliptic curves - that always bothered me about the Ledger Monero integration.

Instead, having a root private key that allows to derive pseudo-random basepoints that are different for every elliptic curve, but have a deterministic derivation based of of the root private key. If I understood correctly.

It's good to see this discussion kicked off.

## prusnak | 2019-10-02T07:38:45+00:00
Let's close this.

## dEBRUYNE-1 | 2019-10-03T13:57:18+00:00
+resolved

## selsta | 2019-10-03T14:04:42+00:00
Seeing that Trezor used SLIP-0010, it should be recommended for future HW wallet integrations.

## cslashm | 2019-10-03T15:55:49+00:00
I think it should be better to follow https://cardanolaunch.com/assets/Ed25519_BIP.pdf from cardano project. The derivation is more flexible.

Btw, today Ledger derive a path according to BIP32 and use the private key as hash seed for view/spend key computation

## prusnak | 2019-10-03T15:57:59+00:00
@cslashm Can you name some advantages of Ed25519_BIP when compared to SLIP-10?

## cslashm | 2019-10-03T17:20:31+00:00
Mainly it allows hardened and non-hardened key derivation.
SLIP10 has unsupported path for ed25519

## prusnak | 2019-10-03T17:26:27+00:00
Since there are no change addresses in Monero I fail to see why it is important to have non-hardened key derivation.

## sedited | 2019-10-03T18:59:28+00:00
I agree as well that non-hardened derivation is not needed. It would be nice though to document how BIP-44 style accounts can be used with the SLIP-10 derivation scheme.

## Lafudoci | 2021-05-09T10:19:02+00:00
I didn't realize their derivation are different until today, when I bought Trezor and tried to replace my third OLED-failure ledger nano s. That's really frustrating. My seed were metal punched copies and multiple remote backup. And now they are wasted just because I switch to the other wallet vendor.

## CyberAshven | 2025-06-24T18:59:40+00:00
After years from this implementation, we can see incompatibility across many Hardware wallet vendors. The only hardware wallet that I know of that is also compatible with Trezor Monero implementation is the OneKey wallet. May I ask what specific derivation path Trezor is using for Monero? All of the below paths are not working.

m/44'/128'/0'/0
m/44'/128'/0'/1
m/44'/128'/1'
m/44'/128'/1'/0
m/44'/128'/1'/1


## CyberAshven | 2025-06-24T19:01:34+00:00
> I didn't realize their derivation are different until today, when I bought Trezor and tried to replace my third OLED-failure ledger nano s. That's really frustrating. My seed were metal punched copies and multiple remote backup. And now they are wasted just because I switch to the other wallet vendor.

It does work with the OneKey wallet

## johnr365 | 2025-06-25T12:24:00+00:00
> May I ask what specific derivation path Trezor is using for Monero? All of the below paths are not working.
> 
> m/44'/128'/0'/0 m/44'/128'/0'/1 m/44'/128'/1' m/44'/128'/1'/0 m/44'/128'/1'/1

While you're waiting for an answer on this, in case you didn't already see it (and it's of use), one of the Trezor devs has a Git repo with a tool for extracting the Monero wallet keys from Trezor seeds:
https://github.com/ph4r05/monero-agent/blob/master/PoC.md#trezor-seeds

# Action History
- Created by: tsusanka | 2018-10-23T09:50:02+00:00
- Closed at: 2019-10-03T13:59:35+00:00
