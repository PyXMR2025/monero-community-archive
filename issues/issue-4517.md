---
title: Trezor Safe 7 support
source_url: https://github.com/monero-project/monero-gui/issues/4517
author: karelbilek
assignees: []
labels: []
created_at: '2025-10-27T10:04:17+00:00'
updated_at: '2026-03-15T22:42:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have Trezor's new Safe 7, I want to use it with Monero.

I don't see it in the menu and when I chose "Safe 5", it doesn't work.

(I know the devices are not generally available yet, so I don't expect this to be done soon, of course; I am just creating this now.)

# Discussion History
## selsta | 2025-10-27T16:43:23+00:00
Can you share the error message you are getting?

## karelbilek | 2025-10-27T18:42:03+00:00
OK, I will do it later.

In the meantime, I am looking how is trezor support done here. It seems it's using custom C++ code.

https://github.com/monero-project/monero/commits/d32b5bfe18e2f5b979fa8dc3a8966c76159ca722/src/device_trezor/trezor/transport.cpp

Trezor is now adding something called "trezor host protocol", the whole USB communication is encrypted with Noise protocol, and it's mandatory with Trezor Safe 7.

https://trezor.io/guides/trezor-devices/trezor-fundamentals/trezor-host-protocol

https://github.com/trezor/trezor-firmware/blob/m1nd3r/thp-documentation/docs/common/thp/specification.md

It is implemented here in trezor's own python trezorlib.

https://github.com/trezor/trezor-firmware/tree/main/python/src/trezorlib/transport/thp

edit:

and here in there official JS code for frontend

https://github.com/trezor/trezor-suite/blob/develop/packages/connect/src/device/thp/pairing.ts

https://github.com/trezor/trezor-suite/tree/eca5223578b1cc14f43e5efcc2244448dbe750ff/packages/protocol/src/protocol-thp

## r1sk01 | 2025-12-05T04:43:57+00:00
trezor safe 7 released around a week ago, i have one and cant use it for monero yet, hopefully support is added

## vampyren | 2025-12-09T16:38:34+00:00
Same here, tried to use other version of Trezor and they all failed. Hope we get support for Trezor 7 soon.
Ledger Stax is really unstable with monero and crashes the whole device. Will report a bug for it soon.

## lavahott | 2025-12-28T15:27:28+00:00
im sure that they will implement support in the near future. For now cake wallet seems to be the closest in terms of supporting the safe 7. You can already use it for btc, eth and some other coins, just not xmr yet.

## vampyren | 2025-12-28T16:32:55+00:00
> im sure that they will implement support in the near future. For now cake wallet seems to be the closest in terms of supporting the safe 7. You can already use it for btc, eth and some other coins, just not xmr yet.

Thanks for the tips. I will wait. I dont want another thirdparty wallet and risk hack or bug. I use Ledger for everything but wanted to move to Trezor but this is just holding me back. Actually Solana as well. I use Solflare for staking and split but Trezor is not supported there either. Its really a shame. Great HW wallet but very little support where it counts. Hope it can get more native app and support in the future. 

## mmilata | 2026-03-10T12:35:31+00:00
If I understand correctly the major missing piece is a C++ library for Trezor-Host Protocol which Safe 7 uses. Trezor is currently working on a Rust library for that, with an API that should make it possible to write a C wrapper. So that would be one option, other options are to reimplement it from scratch ([spec](https://github.com/trezor/trezor-firmware/blob/f2b38c1acbe7dc2afc033ba250b4dfced556bb5b/docs/common/thp/specification.md)) or somehow wrap e.g. the python library.

## emailschaden | 2026-03-15T22:42:33+00:00
[Related issue on monero-project/monero](https://github.com/monero-project/monero/issues/10368)

# Action History
- Created by: karelbilek | 2025-10-27T10:04:17+00:00
