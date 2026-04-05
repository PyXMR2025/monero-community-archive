---
title: v2.6.4
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.6.4
author: xmrig
tag_name: v2.6.4
published_at: '2018-07-11T19:13:51+00:00'
---

# Version: v2.6.4

# Release Notes
### Changes

- [#700](https://github.com/xmrig/xmrig/issues/700) `cryptonight-lite/ipbc` replaced to `cryptonight-heavy/tube` for **Bittube (TUBE)**.
- Added `cryptonight/rto` (cryptonight variant 1 with IPBC/TUBE mod) variant for **Arto (RTO)** coin.
- Added `cryptonight/xao` (original cryptonight with bigger iteration count) variant for **Alloy (XAO)** coin.
- Better variant detection for **nicehash.com** and **minergate.com**.
- [#692](https://github.com/xmrig/xmrig/issues/692) Added support for specify both algorithm and variant via single `algo` option.