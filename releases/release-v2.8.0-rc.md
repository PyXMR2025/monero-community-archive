---
title: v2.8.0-rc
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.8.0-rc
author: xmrig
tag_name: v2.8.0-rc
published_at: '2018-10-01T10:38:42+00:00'
---

# Version: v2.8.0-rc

# Release Notes
### Changes

- **[#753](https://github.com/xmrig/xmrig/issues/753) Added new algorithm [CryptoNight variant 2](https://github.com/xmrig/xmrig/issues/753) for Monero fork, thanks [@SChernykh](https://github.com/SChernykh).**
  - Added global and per thread option `"asm"` and and command line equivalent.
- **[#758](https://github.com/xmrig/xmrig/issues/758) Added SSL/TLS support for secure connections to pools.**
  - Added per pool options `"tls"` and `"tls-fingerprint"` and command line equivalents.
- [#767](https://github.com/xmrig/xmrig/issues/767) Added config autosave feature, same with GPU miners.  
- [#245](https://github.com/xmrig/xmrig-proxy/issues/245) Fixed API ID collision when run multiple miners on same machine.
- [#757](https://github.com/xmrig/xmrig/issues/757) Fixed send buffer overflow.