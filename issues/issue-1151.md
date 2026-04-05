---
title: ubuntu 16.04 8 gb ram
source_url: https://github.com/xmrig/xmrig/issues/1151
author: zhekafun
assignees: []
labels: []
created_at: '2019-08-30T06:44:35+00:00'
updated_at: '2019-08-30T08:36:48+00:00'
type: issue
status: closed
closed_at: '2019-08-30T08:36:48+00:00'
---

# Original Description
[2019-08-30 09:41:11.639]  cpu  use argon2 implementation XOP
[2019-08-30 09:41:11.639]  cpu  use profile  argon2  (6 threads) scratchpad 512 KB
[2019-08-30 09:41:11.647]  cpu  READY threads 6(6) huge pages 0/6 0% memory 3072 KB (8 ms)

memory freed
hugepages enabled by sysctl -w vm.nr_hugepages=128

# Discussion History
## xmrig | 2019-08-30T06:52:39+00:00
Please show output for `cat /proc/meminfo | grep HugePages`.
Thank you.

## zhekafun | 2019-08-30T08:29:17+00:00
cat /proc/meminfo | grep HugePages
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0


## xmrig | 2019-08-30T08:34:50+00:00
`HugePages_Total` and `HugePages_Free` should be 128, `sysctl -w vm.nr_hugepages=128` for some reason not applied. 

## zhekafun | 2019-08-30T08:36:48+00:00
solved runned enabler without su privs

# Action History
- Created by: zhekafun | 2019-08-30T06:44:35+00:00
- Closed at: 2019-08-30T08:36:48+00:00
