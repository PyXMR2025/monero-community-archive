---
title: JSON decode failed
source_url: https://github.com/xmrig/xmrig/issues/3635
author: SKnig171
assignees: []
labels: []
created_at: '2025-02-12T15:30:37+00:00'
updated_at: '2025-06-16T15:19:03+00:00'
type: issue
status: closed
closed_at: '2025-06-16T15:19:03+00:00'
---

# Original Description
Hi, when i start the miner i get the following code:



`C:\Alle Dateien\Desktop\xmrig-6.22.2>xmrig.exe -a rx -o stratum+ssl://rx.unmineable.com:443 -u ETH:0xE4D889dE12e54f5c785d39D4bE83142D169e5e95.unmineable_worker_tnbjwlnd#Bitcoin-Tips -p x
 * ABOUT        XMRig/6.22.2 gcc/13.2.0 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 3 3300U with Radeon Vega Mobile Gfx (1) 64-bit AES
                L2:2.0 MB L3:4.0 MB 4C/4T NUMA:1
 * MEMORY       5.3/5.9 GB (89%)
                Bottom - Slot 1 (left): <empty>
                Bottom - Slot 2 (right): 8 GB DDR4 @ 2400 MHz M471A1K43DB1-CTD
 * MOTHERBOARD  HP - 8615
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+ssl://rx.unmineable.com:443 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2025-02-12 16:27:35.607]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.609]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.609]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.609]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.609]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.610]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.610]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.610]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.610]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.610]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.611]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.611]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.611]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.611]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.612]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:35.612]  net      stratum+ssl://rx.unmineable.com:443 read error: "end of file"
[2025-02-12 16:27:41.594]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.594]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.594]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.594]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.595]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.595]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.595]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.595]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.595]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.595]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.595]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.595]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.596]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.596]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.596]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:41.596]  net      stratum+ssl://rx.unmineable.com:443 read error: "end of file"
[2025-02-12 16:27:47.642]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.643]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.643]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.644]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.644]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.644]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.645]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.646]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.646]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.647]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.648]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.649]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.649]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.650]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.652]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:47.652]  net      stratum+ssl://rx.unmineable.com:443 read error: "end of file"
[2025-02-12 16:27:53.688]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.688]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.688]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.689]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.689]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.689]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.689]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.689]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.689]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.690]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.690]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.690]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.691]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.691]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.691]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:53.691]  net      stratum+ssl://rx.unmineable.com:443 read error: "end of file"
[2025-02-12 16:27:59.772]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.772]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.772]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.772]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.773]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.773]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.774]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.774]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.776]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.776]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.776]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.777]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.777]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.777]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.778]  net      stratum+ssl://rx.unmineable.com:443 JSON decode failed
[2025-02-12 16:27:59.778]  net      stratum+ssl://rx.unmineable.com:443 read error: "end of file"
`

Can someone help me please? 
Connection to the internet is given.

# Discussion History
## SChernykh | 2025-02-13T08:08:10+00:00
Add `--tls` to the command line?

# Action History
- Created by: SKnig171 | 2025-02-12T15:30:37+00:00
- Closed at: 2025-06-16T15:19:03+00:00
