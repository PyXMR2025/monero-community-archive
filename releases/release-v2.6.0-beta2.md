---
title: v2.6.0-beta2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.6.0-beta2
author: xmrig
tag_name: v2.6.0-beta2
published_at: '2018-04-09T17:36:22+00:00'
---

# Version: v2.6.0-beta2

# Release Notes
### Changes

**This version is a bugfix release for previous [beta1](https://github.com/xmrig/xmrig/releases/tag/v2.6.0-beta1).**

- Improved performance for `cryptonight v7` especially in double hash mode.
- [#499](https://github.com/xmrig/xmrig/issues/499) IPv6 disabled for internal HTTP API by default, was causing issues on some systems.
- Added short aliases for algorithm names: `cn`, `cn-lite` and `cn-heavy`.
- Fixed regressions (v2.6.0-beta1 affected)
  - [#494](https://github.com/xmrig/xmrig/issues/494) Command line option `--donate-level` was broken.
  - [#502](https://github.com/xmrig/xmrig/issues/502) Build without libmicrohttpd was broken.
  - Fixed nonce calculation for `--av 4` (software AES, double hash) was causing reduction of effective hashrate and rejected shares on nicehash.