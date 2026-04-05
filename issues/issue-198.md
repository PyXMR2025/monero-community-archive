---
title: Ryzen Threadripper 1950X
source_url: https://github.com/xmrig/xmrig/issues/198
author: hammuh1911
assignees: []
labels:
- bug
- NUMA
created_at: '2017-11-13T07:42:06+00:00'
updated_at: '2019-08-02T12:38:34+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:38:34+00:00'
---

# Original Description
I use Nicehash Legacy Miner and have very low hash rate with xmrig.
(xmr-stak-cpu is working fine with more than 1 kH/s)
I am using Ryzen Threadripper 1950x. Specs:
16 cores
32 threads
32 MB L3 cache
What settings do I use to improve hashrate? I think there needs to be CPU affinity but am not sure how to figure the value. Thanks!

# Discussion History
## Algeroth123 | 2017-11-16T19:16:03+00:00
show us numactl --hardware


## ghost | 2017-11-16T23:19:30+00:00
Hi I'm having a similar issue. I have 2 TR pc's, 1950X's. One is running and earning over 3.50$/day , while my other one that is similarly cooled (slightly higher temp though), is only earning 0.11$/day. Both are stock... What could be causing the degraded performance? 

Good Hashrate PC has 128GB RAM, while slower one has only 8GB, but the one earning more has 2 GPU's also mining while this one that's slow has no GPU's mining. Same PSU, similarly priced boards, and SSD's slow one while NVME is in fast one.

Both win10, both same version of nicehash -- also is numactl --hardware a miner command, *nix command, or what exactly?

## xmrig | 2017-11-17T09:46:49+00:00
Probably CPU running in NUMA mode, in that case you need run miner on each node.
It know issue, check related #86, and already in roadmap.

## xmrig | 2019-07-29T02:19:10+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: hammuh1911 | 2017-11-13T07:42:06+00:00
- Closed at: 2019-08-02T12:38:34+00:00
