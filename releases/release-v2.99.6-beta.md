---
title: v2.99.6-beta
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.99.6-beta
author: xmrig
tag_name: v2.99.6-beta
published_at: '2019-08-13T19:57:06+00:00'
---

# Version: v2.99.6-beta

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- http://workers.xmrig.info/
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

## v2.99.4-beta
- [#1062](https://github.com/xmrig/xmrig/issues/1062) Fixed 32 bit support. **32 bit is slow and deprecated**.
- [#1088](https://github.com/xmrig/xmrig/pull/1088) Fixed macOS compilation.
- [#1095](https://github.com/xmrig/xmrig/pull/1095) Fixed compatibility with hwloc 1.10.x.
- Optimized RandomX initialization and switching, fixed rare crash when re-initialize dataset.
- Fixed ARM build with hwloc.

## v2.99.5-beta
- [#1066](https://github.com/xmrig/xmrig/issues/1066#issuecomment-518080529) Fixed crash and added error message if pool not ready for RandomX.
- [#1092](https://github.com/xmrig/xmrig/issues/1092) Fixed crash if wrong CPU affinity used.
- [#1103](https://github.com/xmrig/xmrig/issues/1103) Improved auto configuration for RandomX for CPUs where L2 cache is limiting factor.
- [#1105](https://github.com/xmrig/xmrig/issues/1105) Improved auto configuration for `cn-pico` algorithm.
- [#1106](https://github.com/xmrig/xmrig/issues/1106) Fixed `hugepages` field in summary API. 
- Added alternative short format for CPU threads.
- Changed format for CPU threads with intensity above 1.
- Name for reference RandomX configuration changed to `rx/test` to avoid potential conflicts in future.

## v2.99.6-beta
- Added commands `pause` and `resume` via JSON RPC 2.0 API (`POST /json_rpc`).
- Fixed autoconfig regression (since 2.99.5), mostly `rx/wow` was affected by this bug.
- Fixed user job recovery after donation round.
- Information about AVX2 CPU feature how hidden in miner summary.