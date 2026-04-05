---
title: v0.8.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v0.8.0
author: xmrig
tag_name: v0.8.0
published_at: '2017-05-16T14:09:23+00:00'
---

# Version: v0.8.0

# Release Notes
- Added double hash mode, also known as lower power mode. `--av=2` and `--av=4`.
- Added smart automatic CPU configuration. Default threads count now depends on size of the L3 cache of CPU.
- Added CryptoNight-Lite support for AEON `-a cryptonight-lite`.
- Added `--max-cpu-usage` option for auto CPU configuration mode.
- Added `--safe` option for adjust threads and algorithm variations to current CPU.
- No more manual steps to enable huge pages on Windows. XMRig will do it automatically.
- Removed BMI2 algorithm variation.
- Removed default pool URL.