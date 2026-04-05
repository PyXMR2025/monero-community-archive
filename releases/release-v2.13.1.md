---
title: v2.13.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.13.1
author: xmrig
tag_name: v2.13.1
published_at: '2019-02-25T14:58:06+00:00'
---

# Version: v2.13.1

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev

## v2.13.0
- **[#938](https://github.com/xmrig/xmrig/issues/938) Added support for new algorithm `cryptonight/r`, short alias `cn/r` (also known as CryptoNightR or CryptoNight variant 4), for upcoming [Monero](https://www.getmonero.org/) fork on March 9, thanks [@SChernykh](https://github.com/SChernykh).**
- [#939](https://github.com/xmrig/xmrig/issues/939) Added support for dynamic (runtime) pools reload.
- [#932](https://github.com/xmrig/xmrig/issues/932) Fixed `cn-pico` hashrate drop, regression since v2.11.0.

## v2.13.1
[#946](https://github.com/xmrig/xmrig/pull/946) Optimized software AES implementations for CPUs without hardware AES support. `cn/r`, `cn/wow` up to 2.6 times faster, 4-9% improvements for other algorithms.