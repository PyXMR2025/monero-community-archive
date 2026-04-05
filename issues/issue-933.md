---
title: '"Illegal instruction" error on i686-pae'
source_url: https://github.com/xmrig/xmrig/issues/933
author: mooleshacat
assignees: []
labels: []
created_at: '2019-02-14T06:50:54+00:00'
updated_at: '2019-02-19T03:09:32+00:00'
type: issue
status: closed
closed_at: '2019-02-19T03:09:32+00:00'
---

# Original Description
It only gets me an extra 4 H/s per mini-server I set up, but I have at least 13 of them and they use little power :) also want to get a bunch of old CPU's and trash them :)

```
root@RS01:~/MINERS/webchain-miner# ./webchain-miner --help
Illegal instruction
```

**uname -a:**
```
root@RS01:~/MINERS/webchain-miner# uname -a
Linux RS01 4.9.0-8-686-pae #1 SMP Debian 4.9.130-2 (2018-10-27) i686 GNU/Linux
```

**cat /proc/cpuinfo:**
```
root@RS01:~/MINERS/webchain-miner# cat /proc/cpuinfo 
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 11
model name      : Mobile Intel(R) Celeron(TM) CPU          650MHz
stepping        : 4
cpu MHz         : 650.004
cache size      : 256 KB
physical id     : 0
siblings        : 1
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fdiv_bug        : no
f00f_bug        : no
coma_bug        : no
fpu             : yes
fpu_exception   : yes
cpuid level     : 2
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 sep mtrr pge mca cmov pse36 mmx fxsr sse
bugs            : cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf
bogomips        : 1300.00
clflush size    : 32
cache_alignment : 32
address sizes   : 36 bits physical, 32 bits virtual
power management:
```

# Discussion History
## xmrig | 2019-02-19T03:09:32+00:00
This CPU lacks `sse2` support, just `sse` not enough.
Thank you.

# Action History
- Created by: mooleshacat | 2019-02-14T06:50:54+00:00
- Closed at: 2019-02-19T03:09:32+00:00
