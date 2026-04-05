---
title: v1.0.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v1.0.0
author: xmrig
tag_name: v1.0.0
published_at: '2017-06-16T13:45:53+00:00'
---

# Version: v1.0.0

# Release Notes
- Miner complete rewritten in C++ with libuv.
- This version should be fully compatible (except config file) with previos versions, many new nice features will come in next versions.
- This is still beta. If you found regression, stability or perfomance issues or have an idea for new feature please fell free to open new [issue](https://github.com/xmrig/xmrig/issues/new).
- Added new option `--print-time=N`, print hashrate report every N seconds.
- New hashrate reports, by default every 60 secons.
- Added Microsoft Visual C++ 2015 and 2017 support.
- Removed dependency on libcurl.
- To compile this version from source please switch to [dev](https://github.com/xmrig/xmrig/tree/dev) branch.