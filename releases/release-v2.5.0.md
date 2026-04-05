---
title: v2.5.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.5.0
author: xmrig
tag_name: v2.5.0
published_at: '2018-03-14T16:48:10+00:00'
---

# Version: v2.5.0

# Release Notes
### Changes

- [#434](https://github.com/xmrig/xmrig/issues/434) **Added support for Monero v7 PoW, scheduled on March 28. You can update miner now, no need to wait for March 28.**
- Added full IPv6 support.
- Added protocol extension, when use the miner with xmrig-proxy 2.5+ no more need manually specify `nicehash` option.
- [#123](https://github.com/xmrig/xmrig-proxy/issues/123) Fixed regression (all versions since 2.4 affected) fragmented responses from pool/proxy was parsed incorrectly.
- [#428](https://github.com/xmrig/xmrig/issues/428) Fixed regression (version 2.4.5 affected) with CPU cache size detection.