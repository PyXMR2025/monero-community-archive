---
title: v2.8.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.8.3
author: xmrig
tag_name: v2.8.3
published_at: '2018-10-19T03:22:37+00:00'
---

# Version: v2.8.3

# Release Notes
## Notes

- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev

## v2.8.3
- [#813](https://github.com/xmrig/xmrig/issues/813) Fixed critical bug with Minergate pool and variant 2.

## v2.8.1
- [#768](https://github.com/xmrig/xmrig/issues/768) Fixed build with Visual Studio 2015.
- [#769](https://github.com/xmrig/xmrig/issues/769) Fixed regression, some ANSI escape sequences was in log with disabled colors.
- [#777](https://github.com/xmrig/xmrig/issues/777) Better report about pool connection issues. 
- Simplified checks for ASM auto detection, only AES support necessary.
- Added missing options to `--help` output.

## v2.8.0
- **[#753](https://github.com/xmrig/xmrig/issues/753) Added new algorithm [CryptoNight variant 2](https://github.com/xmrig/xmrig/issues/753) for Monero fork, thanks [@SChernykh](https://github.com/SChernykh).**
  - Added global and per thread option `"asm"` and and command line equivalent.
- **[#758](https://github.com/xmrig/xmrig/issues/758) Added SSL/TLS support for secure connections to pools.**
  - Added per pool options `"tls"` and `"tls-fingerprint"` and command line equivalents.
- [#767](https://github.com/xmrig/xmrig/issues/767) Added config autosave feature, same with GPU miners.  
- [#245](https://github.com/xmrig/xmrig-proxy/issues/245) Fixed API ID collision when run multiple miners on same machine.
- [#757](https://github.com/xmrig/xmrig/issues/757) Fixed send buffer overflow.