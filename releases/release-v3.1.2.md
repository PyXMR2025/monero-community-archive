---
title: v3.1.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v3.1.2
author: xmrig
tag_name: v3.1.2
published_at: '2019-09-15T12:22:50+00:00'
---

# Version: v3.1.2

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- http://workers.xmrig.info/

## v3.1.2
- Many RandomX optimizations and fixes.
  - [#1132](https://github.com/xmrig/xmrig/issues/1132) Fixed build on CentOS 7.
  - [#1163](https://github.com/xmrig/xmrig/pull/1163) Optimized soft AES code, up to +30% hashrate on CPU without AES support and other optimizations.
  - [#1166](https://github.com/xmrig/xmrig/pull/1166) Fixed crash when initialize dataset with big threads count (eg 272).
  - [#1168](https://github.com/xmrig/xmrig/pull/1168) Optimized loading from scratchpad.
- [#1128](https://github.com/xmrig/xmrig/issues/1128) Fixed CMake 2.8 compatibility.