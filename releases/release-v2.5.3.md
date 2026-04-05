---
title: v2.5.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.5.3
author: xmrig
tag_name: v2.5.3
published_at: '2018-04-22T15:51:07+00:00'
---

# Version: v2.5.3

# Release Notes
### Changes

- Fixed critical bug, in some cases miner was can't recovery connection and switch to failover pool, version 2.5.2 affected. If you use v2.6.0-beta3 this issue doesn't concern you.
- [#499](https://github.com/xmrig/xmrig/issues/499) IPv6 support disabled for internal HTTP API.
- Added workaround for nicehash.com if you use `cryptonightv7.<region>.nicehash.com` option `variant=1` will be set automatically.

For Sumokoin and Haven Protocol please use **v2.6**.