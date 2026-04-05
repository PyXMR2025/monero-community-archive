---
title: 'Feature request: Raptoreum (Ghostrider)'
source_url: https://github.com/xmrig/xmrig/issues/2688
author: Lonnegan
assignees: []
labels: []
created_at: '2021-11-12T09:39:05+00:00'
updated_at: '2021-11-24T17:07:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

the coin Raptoreum was only introduced in April 2021 and has yet managed to attract over 50.000 miners in that short peroid according to MiningPoolStats; as much as Monero, which is years old!

The algo named Ghostrider seems to be a variant or at least a relative to the CN family, so I'd like to request if it is possible to support it with xmrig.

https://cryptomining-blog.com/tag/ghostrider-algorithm/
https://docs.raptoreum.com/_media/GhostRider_Whitepaper.pdf

# Discussion History
## SChernykh | 2021-11-12T09:45:26+00:00
April 2021? It's a coin from 2018: https://bitcointalk.org/index.php?topic=5065848
That whitepaper is wrong, their actual code has different CN variants, half of which are not currently supported by xmrig.
Edit: so it was in testnet since 2018 and released in 2021, ok. Whitepaper is still wrong. I can look into it.

## MrFlipFlop | 2021-11-24T16:59:11+00:00
Support for the GR algo would be nice.
Currently only the RTM devs support the GR algo, plus having their own pool as default in the setup of GR miner causes too much centralization.
Was just now on the SOAT live and someone pointed this very thing, which from a quick look is true, and quite alerting.

A quick google-fu brought me here, trying to figure out if other cpu miners support the GR algo.
Any chance to have support on GR algo or dual mine XMR and RTM using Xmrig miner?

## Spudz76 | 2021-11-24T17:07:51+00:00
#2712 along with three other improvements to GR, have been inducted into the `dev` branch

# Action History
- Created by: Lonnegan | 2021-11-12T09:39:05+00:00
