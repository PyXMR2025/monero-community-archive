---
title: v2.99.2-beta Release Notes
source_url: https://github.com/xmrig/xmrig/issues/1077
author: xmrig
assignees: []
labels:
- NUMA
- META
created_at: '2019-07-28T10:37:23+00:00'
updated_at: '2019-08-10T12:30:46+00:00'
type: issue
status: closed
closed_at: '2019-08-10T12:30:46+00:00'
---

# Original Description
**v2.99.2 is a second major update in 2.99 series, this version introduce NUMA support for RandomX and other algorithms and bug fixes since 2.99.1.**

* **hwloc** dependency added, possible build without hwloc `-DWITH_HWLOC=OFF` but it disable all NUMA related features and new advanced autoconfig.
* If miner built with hwloc RandomX dataset and cache will be allocated on each NUMA node to improve performance.
* New autoconfig use thread affinity, it very important on NUMA hardware.

New options placed in `randomx` object in config file:
```json
{
    ...
    "randomx": {
        "init": -1,
        "numa": true
    },
    ...
}
```
Command line equivalents: `--randomx-init` and `--randomx-no-numa`.

⚠️ Config from other 2.99.x is compatible, but better remove `cpu` object from old config to allow create new threads configuration.

### Previous release notes
* [2.99.0-beta](https://github.com/xmrig/xmrig/issues/1066)

# Discussion History
## xmrig | 2019-07-29T02:11:02+00:00
v2.99.2-beta released https://github.com/xmrig/xmrig/releases/tag/v2.99.2-beta if miner still have issues with NUMA please run command `lstopo topo.xml` from hwloc package and open new issue with `topo.xml` and other useful information.
Thank you.

## xmrig | 2019-07-29T04:04:53+00:00
Mining RandomX require 1168 hugepages for dataset and cache per NUMA node + one page per thread, so recommended use `sudo sysctl -w vm.nr_hugepages=1280` (old manuals usually reserve only 128 pages), for 2 NUMA nodes `sudo sysctl -w vm.nr_hugepages=2560` etc.

## xmrig | 2019-07-30T02:52:11+00:00
v2.99.3-beta released https://github.com/xmrig/xmrig/releases/tag/v2.99.3-beta it contains bugfix for AMD FX CPUs.

# Action History
- Created by: xmrig | 2019-07-28T10:37:23+00:00
- Closed at: 2019-08-10T12:30:46+00:00
