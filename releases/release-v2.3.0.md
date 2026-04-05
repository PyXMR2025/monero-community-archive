---
title: v2.3.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.3.0
author: xmrig
tag_name: v2.3.0
published_at: '2017-08-21T10:47:37+00:00'
---

# Version: v2.3.0

# Release Notes
- Added `--cpu-priority` option (0 idle, 2 normal to 5 highest).
- Added `--user-agent` option, to set custom user-agent string for pool. For example `cpuminer-multi/0.1`.
- Added `--no-huge-pages` option, to disable huge pages support.
- [#62](https://github.com/xmrig/xmrig/issues/62) Don't send the login to the dev pool.
- Force reconnect if pool block miner IP address. helps switch to backup pool.
- Fixed: failed open default config file if path contains non English characters.
- Fixed: error occurred if try use unavailable stdin or stdout, regression since version 2.2.0.
- Fixed: message about huge pages support successfully enabled on Windows was not shown in release builds.

msvc version for win64 usually faster than gcc, but in some hardware configuration gcc faster.