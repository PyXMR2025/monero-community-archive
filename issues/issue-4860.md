---
title: Buildroot package for miner builds on embedded devices
source_url: https://github.com/monero-project/monero/issues/4860
author: ponyatov
assignees: []
labels: []
created_at: '2018-11-16T07:55:32+00:00'
updated_at: '2022-07-20T21:00:05+00:00'
type: issue
status: closed
closed_at: '2022-07-20T21:00:05+00:00'
---

# Original Description
https://www.reddit.com/r/Monero/comments/90r9tf/dedicated_minimal_monerod_hardware/

It would be great to have Buildroot extension for building custom firmwares for multiple architectures including 
* x86_64/KVM for running on VDS servers and real x86 hardware, and 
* experimental ARM/MIPS for low-power bagcase miners (Raspberry Pi, HLK-MT7688, china Pi clones).

# Discussion History
## hyc | 2018-11-16T08:25:39+00:00
Note: raspberry Pi CPUs lack AES instructions, they are all unsuitable for mining.

## selsta | 2022-07-20T21:00:05+00:00
We have official ARM binaries now for both Linux and Android.

Please also see https://github.com/monero-ecosystem/PiNode-XMR

# Action History
- Created by: ponyatov | 2018-11-16T07:55:32+00:00
- Closed at: 2022-07-20T21:00:05+00:00
