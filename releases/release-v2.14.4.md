---
title: v2.14.4
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.14.4
author: xmrig
tag_name: v2.14.4
published_at: '2019-05-30T06:02:12+00:00'
---

# Version: v2.14.4

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev

## v2.14.0
- **[#969](https://github.com/xmrig/xmrig/pull/969) Added new algorithm `cryptonight/rwz`, short alias `cn/rwz` (also known as CryptoNight ReverseWaltz), for upcoming [Graft](https://www.graft.network/) fork.**
- **[#931](https://github.com/xmrig/xmrig/issues/931) Added new algorithm `cryptonight/zls`, short alias `cn/zls` for [Zelerius Network](https://zelerius.org) fork.**
- **[#940](https://github.com/xmrig/xmrig/issues/940) Added new algorithm `cryptonight/double`, short alias `cn/double` (also known as CryptoNight HeavyX), for [X-CASH](https://x-cash.org/).**
- [#951](https://github.com/xmrig/xmrig/issues/951#issuecomment-469581529) Fixed crash if AVX was disabled on OS level.
- [#952](https://github.com/xmrig/xmrig/issues/952) Fixed compile error on some Linux.
- [#957](https://github.com/xmrig/xmrig/issues/957#issuecomment-468890667) Added support for embedded config.
- [#958](https://github.com/xmrig/xmrig/pull/958) Fixed incorrect user agent on ARM platforms.
- [#968](https://github.com/xmrig/xmrig/pull/968) Optimized `cn/r` algorithm performance.

## v2.14.1
* [#975](https://github.com/xmrig/xmrig/issues/975) Fixed crash on Linux if double thread mode used.

## v2.14.4
- [#992](https://github.com/xmrig/xmrig/pull/992)  Fixed compilation with Clang 3.5.
- [#1012](https://github.com/xmrig/xmrig/pull/1012) Fixed compilation with Clang 9.0.
- In HTTP API for unknown hashrate now used `null` instead of `0.0`.
- Fixed MSVC 2019 version detection.
- Removed obsolete automatic variants.
