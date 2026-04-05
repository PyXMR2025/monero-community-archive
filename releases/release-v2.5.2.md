---
title: v2.5.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.5.2
author: xmrig
tag_name: v2.5.2
published_at: '2018-03-26T07:04:09+00:00'
---

# Version: v2.5.2

# Release Notes
### v2.5.0

- [#434](https://github.com/xmrig/xmrig/issues/434) **Added support for Monero v7 PoW, scheduled on April 6. You can update miner now, no need to wait for April 6.**
- Added full IPv6 support.
- Added protocol extension, when use the miner with xmrig-proxy 2.5+ no more need manually specify `nicehash` option.
- [#123](https://github.com/xmrig/xmrig-proxy/issues/123) Fixed regression (all versions since 2.4 affected) fragmented responses from pool/proxy was parsed incorrectly.
- [#428](https://github.com/xmrig/xmrig/issues/428) Fixed regression (version 2.4.5 affected) with CPU cache size detection.

### v2.5.1
- [#454](https://github.com/xmrig/xmrig/issues/454) Fixed build with libmicrohttpd version below v0.9.35.
- [#456](https://github.com/xmrig/xmrig/issues/459) Verbose errors related to donation pool was not fully silenced.
- [#459](https://github.com/xmrig/xmrig/issues/459) Fixed regression (version 2.5.0 affected) with connection to **xmr.f2pool.com**.

# v2.5.2
- [#448](https://github.com/xmrig/xmrig/issues/478) Fixed broken reconnect.