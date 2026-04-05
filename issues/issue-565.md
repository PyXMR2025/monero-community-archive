---
title: Am i missing someting in settings ?
source_url: https://github.com/xmrig/xmrig/issues/565
author: techmashido
assignees: []
labels: []
created_at: '2018-04-19T20:09:09+00:00'
updated_at: '2018-11-05T13:29:29+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:29:29+00:00'
---

# Original Description
Hi there,
I think i am getting less hashrates with this specs of my server. 
CPU family:            6
Model:                 85
Cores:                 32
Model name:            Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz
Stepping:              4
CPU MHz:               2693.674
BogoMIPS:              5387.34
Virtualization:        VT-x
Hypervisor vendor:     KVM
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              1024K
L3 cache:              33792K
NUMA node0 CPU(s):     0-31


**Case1**
I get 1K-1.2K h/s only when i used 28 cores

**Case2**
I get 250-350 h/s when i tested with below configuration

 * VERSIONS:     XMRig/2.5.2 libuv/1.9.1 gcc/7.2.0
 * HUGE PAGES:   available, disabled
 * CPU:          Intel(R) Xeon(R) Platinum 8168 CPU @ 2.70GHz (8) x64 AES-NI
 * CPU L2/L3:    64.0 MB/264.0 MB
 * THREADS:      6, cryptonight, av=1, donate=1%
 * POOL #1:      pool.supportxmr.com:5555

can anybody suggest some settings to tune it please?

# Discussion History
# Action History
- Created by: techmashido | 2018-04-19T20:09:09+00:00
- Closed at: 2018-11-05T13:29:29+00:00
