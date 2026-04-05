---
title: v2.9.4
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.9.4
author: xmrig
tag_name: v2.9.4
published_at: '2019-01-19T17:29:01+00:00'
---

# Version: v2.9.4

# Release Notes
## Notes

- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev

## v2.9.4
- [#913](https://github.com/xmrig/xmrig/issues/913) Fixed Masari (MSR) support (this update required for upcoming fork).
- [#915](https://github.com/xmrig/xmrig/pull/915) Improved security, JIT memory now read-only after patching.

## v2.9.3
- [#909](https://github.com/xmrig/xmrig/issues/909) Fixed compile errors on FreeBSD.
- [#912](https://github.com/xmrig/xmrig/pull/912) Fixed, C++ implementation of `cn/half` was produce up to 13% of invalid hashes.

## v2.9.2
- [#907](https://github.com/xmrig/xmrig/pull/907) Fixed crash on Linux.

## v2.9.1
- Restored compatibility with https://stellite.hashvault.pro.

## v2.9.0
- [#899](https://github.com/xmrig/xmrig/issues/899) Added support for new algorithm `cn/half` for Masari and Stellite forks.
- [#834](https://github.com/xmrig/xmrig/pull/834) Added ASM optimized code for AMD Bulldozer.
- [#839](https://github.com/xmrig/xmrig/issues/839) Fixed FreeBSD compile.
- [#857](https://github.com/xmrig/xmrig/pull/857) Fixed impossible to build for macOS without clang.