---
title: 'connect error: "operation canceled"'
source_url: https://github.com/xmrig/xmrig/issues/3507
author: Dijkstarlin
assignees: []
labels: []
created_at: '2024-07-05T16:34:53+00:00'
updated_at: '2025-06-18T22:10:18+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:10:18+00:00'
---

# Original Description
**Describe the bug**
`        Controller1-ChannelD: 2 GB LPDDR4 @ 4267 MHz 53E1G32D2NP-046   

 * MOTHERBOARD  LENOVO - 20XW004WCD

 * DONATE       1%

 * ASSEMBLY     auto:intel

 * POOL #1      stratum+ssl://rx.unmineable.com:4444 algo rx/0

 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
* HTTP API     127.0.0.1:60070
* OPENCL       disabled

 * CUDA         disabled
[2024-07-06 00:20:46.801]  net      stratum+ssl://rx.unmineable.com:4444 98.159.108.71 connect error: "operation canceled"
[2024-07-06 00:21:12.068]  net      stratum+ssl://rx.unmineable.com:4444 98.159.108.71 connect error: "operation canceled"
[2024-07-06 00:21:37.284]  net      stratum+ssl://rx.unmineable.com:4444 98.159.108.71 connect error: "operation canceled"`


nslookup http://pool.supportxmr.com:5555/
server:  dns.google
Address:  8.8.8.8

*** dns.google cannot find http://pool.supportxmr.com:5555/: Non-existent domain
**To Reproduce**
I just downloaded the file and i'm pretty sure that the wallet and address are both ok.I pinged the website and it goes timeout,
so i guess it's more probably a network issue instead of some local issues.However i 've tried many ways from others' same problem and nothing worked,since i'm a green hand maybe there are some wrong opertations.
**Expected behavior**
Please give me some sugguestions and i can provide more information if wanted.

**Required data**
 - XMRig version
    - 6.21.3
 - OS: Windows 11 64

**Additional context**
D:\miner\unMiner\resources\miners\win32\xmrig-6.21.3
The "win32" is very suspicious.


# Discussion History
## Dijkstarlin | 2024-07-06T00:17:05+00:00
More info:i use clash

# Action History
- Created by: Dijkstarlin | 2024-07-05T16:34:53+00:00
- Closed at: 2025-06-18T22:10:18+00:00
