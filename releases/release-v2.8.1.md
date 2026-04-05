---
title: v2.8.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.8.1
author: xmrig
tag_name: v2.8.1
published_at: '2018-10-09T00:44:50+00:00'
---

# Version: v2.8.1

# Release Notes
### Notes

- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev

### Changes since v2.6.4

- **[#753](https://github.com/xmrig/xmrig/issues/753) Added new algorithm [CryptoNight variant 2](https://github.com/xmrig/xmrig/issues/753) for Monero fork, thanks [@SChernykh](https://github.com/SChernykh).**
  - Added global and per thread option `"asm"` and and command line equivalent.
- **[#758](https://github.com/xmrig/xmrig/issues/758) Added SSL/TLS support for secure connections to pools.**
  - Added per pool options `"tls"` and `"tls-fingerprint"` and command line equivalents.
- [#767](https://github.com/xmrig/xmrig/issues/767) Added config autosave feature, same with GPU miners.  
- [#245](https://github.com/xmrig/xmrig-proxy/issues/245) Fixed API ID collision when run multiple miners on same machine.
- [#757](https://github.com/xmrig/xmrig/issues/757) Fixed send buffer overflow.
- [#777](https://github.com/xmrig/xmrig/issues/777) Better report about pool connection issues. 