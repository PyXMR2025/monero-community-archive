---
title: 'read error: "end of file"'
source_url: https://github.com/xmrig/xmrig/issues/3469
author: GamerWierdo100
assignees: []
labels: []
created_at: '2024-04-27T01:24:40+00:00'
updated_at: '2025-06-18T22:15:06+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:15:06+00:00'
---

# Original Description
**Describe the bug**
When i use Xmrig i get read error: "end of file"

**To Reproduce**
Start Xmrig linux with `./xmrig --cuda -o stratum+tcp://sha256.auto.nicehash.com:9200 -u 3EwSHpA4SCeQwwcecdpoFjBwtZzjQ6Vmni --tls --nicehash -o stratum+tcp://sha256.auto.nicehash.com:9200 --rig-id 3EwSHpA4SCeQwwcecdpoFjBwtZzjQ6Vmni --tls`

**Expected behavior**
It should start mining towards my nicehash stratum

**Required data**
 - XMRig version: XMRig/6.21.3 gcc/11.4.0 (built for Linux x86-64, 64 bit)
 - Miner log as text or screenshot:
```
 ~/Appimages/xmrig-6.21.3$ ./xmrig --cuda -o stratum+tcp://sha256.auto.nicehash.com:9200 -u 3EwSHpA4SCeQwwcecdpoFjBwtZzjQ6Vmni --tls --nicehash -o stratum+tcp://sha256.auto.nicehash.com:9200 --rig-id 3EwSHpA4SCeQwwcecdpoFjBwtZzjQ6Vmni --tls
 * ABOUT        XMRig/6.21.3 gcc/11.4.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.48.0 OpenSSL/3.0.13 hwloc/2.10.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 7 7700X 8-Core Processor (1) 64-bit AES
                L2:8.0 MB L3:32.0 MB 8C/16T NUMA:1
 * MEMORY       5.8/30.5 GB (19%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://sha256.auto.nicehash.com:9200 algo auto
 * POOL #2      stratum+tcp://sha256.auto.nicehash.com:9200 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled (/home/arun/Appimages/xmrig-6.21.3/libxmrig-cuda.so: cannot open shared object file: No such file or directory)
[2024-04-26 20:10:41.854]  net      stratum+tcp://sha256.auto.nicehash.com:9200 read error: "end of file"
[2024-04-26 20:10:46.422]  signal   Ctrl+C received, exiting
```
 - Config file or command line (without wallets): `./xmrig --cuda -o stratum+tcp://sha256.auto.nicehash.com:9200 -u 3EwSHpA4SCeQwwcecdpoFjBwtZzjQ6Vmni --tls --nicehash -o stratum+tcp://sha256.auto.nicehash.com:9200 --rig-id 3EwSHpA4SCeQwwcecdpoFjBwtZzjQ6Vmni --tls
`
 - OS: [e.g. Windows] KUbuntu
 - For GPU related issues: information about GPUs and driver version: RTX 4070 Ti Super, drivers latest from ubuntu-drivers

# Discussion History
## SChernykh | 2024-04-27T06:43:38+00:00
`sha256.auto.nicehash.com`
XMRig doesn't support SHA256

## GamerWierdo100 | 2024-04-27T17:06:31+00:00
@SChernykh what is the supported version?

## flatounet | 2024-05-09T02:47:57+00:00
i got same error here ,
using bat file for config no error it mining :  but i have failled MRS MOD ,
solution  start xmrig.exe file i dont have MRS error but : "end of file" ...
 ( edited file , config is good my wallet / pool / algo is the same from bat file 
 didnt see space or missing space at end of file ... )
( see post from 2022 we are 2024 ...)
( xmrig 6.21.3 for windows 11 64 updated )


## SChernykh | 2024-05-09T06:15:54+00:00
> see post from 2022 we are 2024 ...

Time to fix your config in 2024. This is not an XMRig error, you're just connecting to a wrong URL.

## Minearm-RPM | 2024-06-09T06:10:39+00:00
俺也一样

# Action History
- Created by: GamerWierdo100 | 2024-04-27T01:24:40+00:00
- Closed at: 2025-06-18T22:15:06+00:00
