---
title: v2.6.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.6.3
author: xmrig
tag_name: v2.6.3
published_at: '2018-06-13T14:52:04+00:00'
---

# Version: v2.6.3

# Release Notes
### Changes

- **Added support for new cryptonight-heavy variant xhv** (`cn-heavy/xhv`) for upcoming Haven Protocol fork.
- **Added support for new cryptonight variant msr** (`cn/msr`) also known as `cryptonight-fast` for upcoming Masari fork.
- Added new detailed hashrate report.
- [#446](https://github.com/xmrig/xmrig/issues/446) Likely fixed SIGBUS error on 32 bit ARM CPUs.
- [#551](https://github.com/xmrig/xmrig/issues/551) Fixed `cn-heavy` algorithm on ARMv8.
- [#614](https://github.com/xmrig/xmrig/issues/614) Fixed display issue with huge pages percentage when colors disabled.
- [#615](https://github.com/xmrig/xmrig/issues/615) Fixed build without libcpuid.
- [#629](https://github.com/xmrig/xmrig/pull/629) Fixed file logging with non-seekable files.
- [#672](https://github.com/xmrig/xmrig/pull/672) Reverted back `cryptonight-light` and exit if no valid algorithm specified.