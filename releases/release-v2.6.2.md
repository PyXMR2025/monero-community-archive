---
title: v2.6.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.6.2
author: xmrig
tag_name: v2.6.2
published_at: '2018-05-06T19:39:42+00:00'
---

# Version: v2.6.2

# Release Notes
### Major changes since v2.5
 - [#168](https://github.com/xmrig/xmrig-proxy/issues/168) Added support for [mining algorithm negotiation](https://github.com/xmrig/xmrig-proxy/blob/dev/doc/STRATUM_EXT.md#1-mining-algorithm-negotiation).
 - [#563](https://github.com/xmrig/xmrig/issues/563) Added [advanced threads mode](https://github.com/xmrig/xmrig/issues/563), now possible configure each thread individually.
 - [#255](https://github.com/xmrig/xmrig/issues/563) Low power mode extended to **triple**, **quard** and **penta** modes.
 - Improved performance for new cryptonight variants.
 - Added support for **rig-id** stratum protocol extensions, compatible with xmr-stak.
 - Changed behavior for option `variant=-1` for `cryptonight`, now variant is `1` by default, if you mine old coins need change `variant` to `0`.
 - New algorithms:
   - **CryptoNight-Heavy** for Sumokoin, Haven Protocol and Loki.
   - **CryptoNight-Lite** variant **ipbc** for IPBC coin.
   - **CryptoNight** variant **xtl** for upcoming Stellite (XTL) fork.


[Full changelog](https://github.com/xmrig/xmrig/blob/master/CHANGELOG.md)