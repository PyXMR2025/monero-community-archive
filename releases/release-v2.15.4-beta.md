---
title: v2.15.4-beta
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.15.4-beta
author: xmrig
tag_name: v2.15.4-beta
published_at: '2019-06-02T07:54:17+00:00'
---

# Version: v2.15.4-beta

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev

## v2.15.0-beta
- [#314](https://github.com/xmrig/xmrig-proxy/issues/314) Added donate over proxy feature.
  - Added new option `donate-over-proxy`.
  - Added real graceful exit.

## v2.15.1-beta
- [#1007](https://github.com/xmrig/xmrig/issues/1007) Old HTTP API backend based on libmicrohttpd, replaced to custom HTTP server (libuv + http_parser).
- [#257](https://github.com/xmrig/xmrig-nvidia/pull/257) New logging subsystem, file and syslog now always without colors.

## v2.15.2-beta
- [#1010](https://github.com/xmrig/xmrig/pull/1010#issuecomment-482632107) Added daemon support (solo mining).
- [#1012](https://github.com/xmrig/xmrig/pull/1012) Fixed compatibility with clang 9.
- Config subsystem was rewritten, internally JSON is primary format now.
- Fixed regression, big HTTP responses was truncated.

## v2.15.3-beta
- [#1014](https://github.com/xmrig/xmrig/issues/1014) Fixed regression, default value for `algo` option was not applied.

## v2.15.4-beta
- Added global uptime and extended connection information in API.
- API now return current algorithm instead of global algorithm specified in config.
- This version also include all changes from stable version [v2.14.4](https://github.com/xmrig/xmrig/releases/tag/v2.14.4).