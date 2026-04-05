---
title: v2.99.3-beta
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.99.3-beta
author: xmrig
tag_name: v2.99.3-beta
published_at: '2019-07-30T02:49:06+00:00'
---

# Version: v2.99.3-beta

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Release Notes](https://github.com/xmrig/xmrig/issues/1077)

## v2.99.0-beta
- [#1050](https://github.com/xmrig/xmrig/pull/1050) Added RandomXL algorithm for [Loki](https://loki.network/), algorithm name used by miner is `randomx/loki` or `rx/loki`.
- Added [flexible](https://github.com/xmrig/xmrig/blob/evo/doc/CPU.md) multi algorithm configuration.
- Added unlimited switching between incompatible algorithms, all mining options can be changed in runtime.
- Breaked backward compatibility with previous configs and command line, `variant` option replaced to `algo`, global option `algo` removed, all CPU related settings moved to `cpu` object.
- Options `av`, `safe` and `max-cpu-usage` removed.
- Algorithm `cn/msr` renamed to `cn/fast`.
- Algorithm `cn/xtl` removed.
- API endpoint `GET /1/threads` replaced to `GET /2/backends`.

## v2.99.1-beta
- [#1072](https://github.com/xmrig/xmrig/issues/1072) Fixed RandomX `seed_hash` re-initialization.

## v2.99.2-beta
- [#1077](https://github.com/xmrig/xmrig/issues/1077) Added NUMA support via **hwloc**.
- Fixed miner freeze when switch between RandomX variants.
- Fixed dataset initialization speed on Linux if thread affinity was used.

## v2.99.3-beta
- [#1082](https://github.com/xmrig/xmrig/issues/1082) Fixed hwloc auto configuration on AMD FX CPUs.
- Added command line option `--export-topology` for export hwloc topology to a XML file.