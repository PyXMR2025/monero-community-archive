---
title: ARMv9 CIX CD8160/CD8180 CPU topology & identification information
source_url: https://github.com/xmrig/xmrig/issues/3788
author: craighammonds-sys
assignees: []
labels: []
created_at: '2026-03-02T05:16:25+00:00'
updated_at: '2026-03-03T02:10:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

I’m sharing hardware identification and topology information for a CIX ARMv9 SoC
(CD8160 / CD8180) used in the Orange Pi 6 Plus.

XMRig currently identifies this CPU generically, which is understandable given that
this chipset appears to be new and not widely documented upstream.

The information below is provided to help with correct CPU identification and
topology awareness on ARMv9 CIX platforms. No performance changes are being requested.
# CIX CD8160 / CD8180 ARMv9 SoC — Hardware Evidence for XMRig

## Board
- Orange Pi 6 Plus

## SoC
- Vendor: CIX
- Model: CIX P1 CD8160 (also marketed as CD8180 variant)
- Architecture: ARMv9-A
- NUMA nodes: 1

## CPU Topology

Heterogeneous ARMv9 configuration:

- 8 × Cortex-A720
  - CPU implementer: 0x41 (ARM)
  - CPU part: 0xD81
  - Max frequency: 2600 MHz

- 4 × Cortex-A520
  - CPU implementer: 0x41 (ARM)
  - CPU part: 0xD80
  - Max frequency: 1800 MHz

Total cores: 12  
Threads per core: 1

## Features
- AES
- PMULL
- SHA1 / SHA2 / SHA3
- SVE
- SVE2
- SVE AES / PMULL
- bf16 / i8mm

## devfreq (chipset fabric)
The following devfreq domains are exposed by the kernel:

- /sys/class/devfreq/CIXH3010:00
- /sys/class/devfreq/CIXH4000:00
- /sys/class/devfreq/CIXH5000:00

Observed default governors include `simple_ondemand` and `userspace`.
For RandomX workloads, stability improves when set to `performance`.

## Observed XMRig behaviour
- Auto-detection initially clamps RandomX threads conservatively
- Manual configuration with 12 threads is stable
- No NUMA splitting required
- No CPU affinity required

## Notes
- XMRig currently identifies the CPU generically (e.g. Cortex-A720)
- Cache sizes are not exposed to hwloc on this platform
- This document is provided to aid correct CPU identification and topology handling

# Discussion History
## SChernykh | 2026-03-02T09:47:52+00:00
Can you run `./xmrig --export-topology` on that device and attach the generated file?

## craighammonds-sys | 2026-03-03T02:10:04+00:00
[topology.xml](https://github.com/user-attachments/files/25699768/topology.xml)
Thankyou Here is the exported topology.xml from the device.

# Action History
- Created by: craighammonds-sys | 2026-03-02T05:16:25+00:00
