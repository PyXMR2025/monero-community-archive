---
title: Bad Huge Pages on fresh Debian host server
source_url: https://github.com/xmrig/xmrig/issues/2335
author: PT400C
assignees: []
labels: []
created_at: '2021-04-30T19:19:43+00:00'
updated_at: '2021-09-06T09:47:48+00:00'
type: issue
status: closed
closed_at: '2021-09-06T09:47:48+00:00'
---

# Original Description
Hey, running the command `./xmrig -o xmrpool.eu:9999 -u WALLET-ID -k --tls` (latest version at the moment) works just fine. But I noticed that my system gives me this prompt which I assume means that not all available power is used for calculation `randomx allocated 2336 MB (2080+256) huge pages 89% 1040/1168 +JIT (197 ms).` Also running one of the benchmark commands gives me the same result. Not all huge pages are available.

The host system has 64 GB of ram and runs a Ryzen 5 3600X.

Do you maybe have a clue what might be going wrong?

EDIT: When mining, `cat /proc/meminfo` shows this for hugePages: 

_HugePages_Total:    1302
HugePages_Free:      115
HugePages_Rsvd:       59
HugePages_Surp:        0
Hugepagesize:       2048 kB_



`sysctl -a | grep hugepage` prints:

_vm.nr_hugepages = 1302
vm.nr_hugepages_mempolicy = 1302
vm.nr_overcommit_hugepages = 0_


# Discussion History
# Action History
- Created by: PT400C | 2021-04-30T19:19:43+00:00
- Closed at: 2021-09-06T09:47:48+00:00
