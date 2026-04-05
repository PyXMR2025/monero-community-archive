---
title: v3.1.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v3.1.1
author: xmrig
tag_name: v3.1.1
published_at: '2019-08-31T01:16:18+00:00'
---

# Version: v3.1.1

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- http://workers.xmrig.info/

## v3.1.1
- [#1133](https://github.com/xmrig/xmrig/issues/1133) Fixed syslog regression.
- [#1138](https://github.com/xmrig/xmrig/issues/1138) Fixed multiple network bugs.
- [#1141](https://github.com/xmrig/xmrig/issues/1141) Fixed log in background mode.
- [#1142](https://github.com/xmrig/xmrig/pull/1142) RandomX hashrate improved by 0.5-1.5% depending on variant and CPU.
- [#1146](https://github.com/xmrig/xmrig/pull/1146) Fixed race condition in RandomX thread init.
- [#1148](https://github.com/xmrig/xmrig/pull/1148) Fixed, on Linux linker marking entire executable as having an executable stack.
- Fixed, for Argon2 algorithms command line options like `--threads` was ignored.
- Fixed command line options for single pool, free order allowed again.