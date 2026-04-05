---
title: v2.6.0-beta1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.6.0-beta1
author: xmrig
tag_name: v2.6.0-beta1
published_at: '2018-04-03T12:04:44+00:00'
---

# Version: v2.6.0-beta1

# Release Notes
### Changes
 
- [#476](https://github.com/xmrig/xmrig/issues/476) **Added Cryptonight-Heavy support for Sumokoin ASIC resistance fork.**
 - HTTP server now runs in main loop, it make possible easy extend API without worry about thread synchronization.
 - Added initial graceful reload support, miner will reload configuration if config file changed, disabled by default until it will be fully implemented and tested.
 - Added API endpoint `PUT /1/config` to update current config.
 - Added API endpoint `GET /1/config` to get current active config.
 - Added API endpoint `GET /1/threads` to get current active threads configuration.
 - API endpoint `GET /` now deprecated, use `GET /1/summary` instead.
 - Added `--api-no-ipv6` and similar config option to disable IPv6 support for HTTP API.
 - Added `--api-no-restricted` to enable full access to api, this option has no effect if `--api-access-token` not specified.