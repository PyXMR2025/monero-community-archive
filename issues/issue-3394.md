---
title: end of file in every configuration scenario
source_url: https://github.com/xmrig/xmrig/issues/3394
author: pthoelken
assignees: []
labels: []
created_at: '2023-12-29T07:24:25+00:00'
updated_at: '2025-06-16T19:48:15+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:48:15+00:00'
---

# Original Description
**Describe the bug**
I've configured my start parameters from the xmrig configuration wizard. But I got the following errors from the start parameters below. It's really frustrating.

**Start Parameters (I've tried both):**
./xmrig -o stratum+ssl://keccak.auto.nicehash.com:443 -u 999999asdasdasd9asd99999 --tls -k --nicehash
./xmrig -o keccak.auto.nicehash.com:443 -u 999999asdasdasd9asd99999 --tls -k --nicehash

**Error Message:**
```
 * ABOUT        XMRig/6.21.0 gcc/5.4.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7702P 64-Core Processor (1) 64-bit AES VM
                L2:3.0 MB L3:16.0 MB 6C/6T NUMA:1
 * MEMORY       4.3/15.6 GB (28%)
                DIMM 0: 16 GB RAM @ 0 MHz DIMM 0
 * MOTHERBOARD KVM Server
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      keccak.auto.nicehash.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-12-29 08:19:21.056]  net      keccak.auto.nicehash.com:443 read error: "end of file"
```

**Required data**
 - Config file or command line (without wallets) - I've using the starting parameters.
 - OS: Debian 11
 - CPU Mining


# Discussion History
## SChernykh | 2023-12-29T07:34:08+00:00
`keccak.auto.nicehash.com` is not a RandomX pool. Judging by the name, it's not even something that XMRig supports. Try another pool.

## koitsu | 2024-03-14T09:43:39+00:00
@pthoelken You didn't specify an algorithm in your command-line arguments (`-a xxx`).  The server is kicking you out for this reason (and possibly more than just that).  I suspect it's exactly what SChernykh said.

# Action History
- Created by: pthoelken | 2023-12-29T07:24:25+00:00
- Closed at: 2025-06-16T19:48:15+00:00
