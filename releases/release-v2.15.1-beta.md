---
title: v2.15.1-beta
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.15.1-beta
author: xmrig
tag_name: v2.15.1-beta
published_at: '2019-04-01T12:24:39+00:00'
---

# Version: v2.15.1-beta

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