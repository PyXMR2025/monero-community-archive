---
title: Segmentation fault with v6.3.4 on Ubuntu 20.04.1 while mining cn-heavy/xhv
source_url: https://github.com/xmrig/xmrig/issues/1847
author: fmasclef
assignees: []
labels: []
created_at: '2020-09-25T09:15:45+00:00'
updated_at: '2021-04-26T12:10:53+00:00'
type: issue
status: closed
closed_at: '2020-09-25T16:09:21+00:00'
---

# Original Description
**Describe the bug**
`xmrig` crash right after ending OpenCL compilation when threads are `READY`. It always ends up in process killed or segfault if using opencl cache.

**To Reproduce**
- do an Ubuntu 20.04.1 fresh install
- add your user to both `video` and `render` groups
- install AMD APP SDK 3 and make sure to export LD_LIBRARY_PATH (not sure it's needed)
- reboot
- install latest AMD PRO drivers
- reboot
- `clinfo` shows the OpenCL info, including all video adapters (here, 3)
- follow compilation guide (or use the focal binary, same result)
- start mining cn-heavy/xhv

**Expected behavior**
`xmrig` to actualy mine something

**Required data**
 - Miner log as text or screenshot
with opencl cache :
```
me@rig:/data/git/xmrig/build$ ./xmrig -c config.json
 * ABOUT        XMRig/6.3.4 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Celeron(R) CPU G3900 @ 2.80GHz (1) x64 AES
                L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
 * MEMORY       0.9/3.7 GB (24%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.hashvault.pro:443 algo auto
[2020-09-25 10:48:45.945] POOLS --------------------------------------------------------------------
[2020-09-25 10:48:45.945] url:       pool.hashvault.pro:443
[2020-09-25 10:48:45.945] host:      pool.hashvault.pro
[2020-09-25 10:48:45.945] port:      443
[2020-09-25 10:48:45.945] user:      a_wallet_address_goes_here
[2020-09-25 10:48:45.945] pass:      rig
[2020-09-25 10:48:45.945] rig-id     (null)
[2020-09-25 10:48:45.945] algo:      invalid
[2020-09-25 10:48:45.945] nicehash:  0
[2020-09-25 10:48:45.945] keepAlive: 60
[2020-09-25 10:48:45.945] --------------------------------------------------------------------------
 * COMMANDS     hashrate, pause, resume, results, connection
[2020-09-25 10:48:45.946]  config   configuration saved to: "/data/crypto/xmrig/config.json"
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3143.9)
 * OPENCL GPU   #0 01:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
 * OPENCL GPU   #1 04:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
 * OPENCL GPU   #2 05:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
 * CUDA         disabled
[2020-09-25 10:48:45.946] [pool.hashvault.pro:443] state: "unconnected" -> "host-lookup"
[2020-09-25 10:48:45.951] [pool.hashvault.pro:443] state: "host-lookup" -> "connecting"
[2020-09-25 10:48:45.973] [pool.hashvault.pro:443] state: "connecting" -> "connected"
[2020-09-25 10:48:45.973] [pool.hashvault.pro:443] TLS send     (283 bytes)
[2020-09-25 10:48:45.996] [pool.hashvault.pro:443] TLS received (1328 bytes)
[2020-09-25 10:48:45.997] [pool.hashvault.pro:443] TLS send     (93 bytes)
[2020-09-25 10:48:46.019] [pool.hashvault.pro:443] TLS received (258 bytes)
[2020-09-25 10:48:46.019] [pool.hashvault.pro:443] send (496 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"a_wallet_address_goes_here","pass":"rig","agent":"XMRig/6.3.4 (Linux x86_64) libuv/1.34.2 gcc/9.3.0","algo":["cn/1","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/ccx","rx/0","rx/wow","rx/loki","rx/arq","rx/sfx","rx/keva","astrobwt","kawpow"]}}"
[2020-09-25 10:48:46.019] [pool.hashvault.pro:443] TLS send     (525 bytes)
[2020-09-25 10:48:46.041] [pool.hashvault.pro:443] TLS received (1071 bytes)
[2020-09-25 10:48:46.042] [pool.hashvault.pro:443] received (1041 bytes): "{"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"f6c446c7-987e-45da-9f62-7b69cefde281","job":{"blob":"0e0eaaddb6fb05069cc0cad651fd19c1b092f434f61f325b38ede7c9874dcd6d0d9936bd4166ee000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000eb96a9d2010000005083d1cc010000007f293fc10100000ed85ac3ed03c696b770550de3419745c5246b48bfe2ae9a0a2d0b02f8c57b22f31762e3dc52168cedf1cbd648898b0504738f6795b73974960667242633727dcb83f086fdc074306efb5014d6cb2d59826877d195e01de8f99ad0460a07370001","job_id":"09a577ff-ad6f-4b2e-aeeb-19953817222c","target":"22480700","id":"f6c446c7-987e-45da-9f62-7b69cefde281","timestamp":1601023726029,"height":688552,"algo":"cn-heavy/xhv","variant":"xhv","motd":"0D0A486173685661756C74206B6565707320796F757220726967206861736872617465207365637572652E205468616E6B7320666F72207472757374696E67207573210D0A"},"extensions":["algo","motd","keepalive"],"status":"OK"}}"
[2020-09-25 10:48:46.042]  net      use pool pool.hashvault.pro:443 TLSv1.2 138.201.36.249
[2020-09-25 10:48:46.042]  net      new job from pool.hashvault.pro:443 diff 9000 algo cn-heavy/xhv height 688552
[2020-09-25 10:48:46.042]  opencl   use profile  cn-heavy  (6 threads) scratchpad 4096 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  1 |   0 | 01:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  2 |   1 | 04:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  3 |   1 | 04:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  4 |   2 | 05:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  5 |   2 | 05:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
Segmentation fault
```

without opencl cache:
```
me@rig:/data/git/xmrig/build$ ./xmrig -c config.json --opencl-no-cache
 * ABOUT        XMRig/6.3.4 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Celeron(R) CPU G3900 @ 2.80GHz (1) x64 AES
                L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
 * MEMORY       0.9/3.7 GB (24%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.hashvault.pro:443 algo auto
[2020-09-25 10:49:05.625] POOLS --------------------------------------------------------------------
[2020-09-25 10:49:05.625] url:       pool.hashvault.pro:443
[2020-09-25 10:49:05.625] host:      pool.hashvault.pro
[2020-09-25 10:49:05.625] port:      443
[2020-09-25 10:49:05.625] user:      a_wallet_address_goes_here
[2020-09-25 10:49:05.625] pass:      rig
[2020-09-25 10:49:05.625] rig-id     (null)
[2020-09-25 10:49:05.625] algo:      invalid
[2020-09-25 10:49:05.625] nicehash:  0
[2020-09-25 10:49:05.625] keepAlive: 60
[2020-09-25 10:49:05.625] --------------------------------------------------------------------------
 * COMMANDS     hashrate, pause, resume, results, connection
[2020-09-25 10:49:05.626]  config   configuration saved to: "/data/crypto/xmrig/config.json"
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3143.9)
 * OPENCL GPU   #0 01:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
 * OPENCL GPU   #1 04:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
 * OPENCL GPU   #2 05:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
 * CUDA         disabled
[2020-09-25 10:49:05.626] [pool.hashvault.pro:443] state: "unconnected" -> "host-lookup"
[2020-09-25 10:49:05.693] [pool.hashvault.pro:443] state: "host-lookup" -> "connecting"
[2020-09-25 10:49:05.715] [pool.hashvault.pro:443] state: "connecting" -> "connected"
[2020-09-25 10:49:05.715] [pool.hashvault.pro:443] TLS send     (283 bytes)
[2020-09-25 10:49:05.738] [pool.hashvault.pro:443] TLS received (1328 bytes)
[2020-09-25 10:49:05.740] [pool.hashvault.pro:443] TLS send     (93 bytes)
[2020-09-25 10:49:05.762] [pool.hashvault.pro:443] TLS received (258 bytes)
[2020-09-25 10:49:05.762] [pool.hashvault.pro:443] send (496 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"a_wallet_address_goes_here","pass":"rig","agent":"XMRig/6.3.4 (Linux x86_64) libuv/1.34.2 gcc/9.3.0","algo":["cn/1","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/ccx","rx/0","rx/wow","rx/loki","rx/arq","rx/sfx","rx/keva","astrobwt","kawpow"]}}"
[2020-09-25 10:49:05.762] [pool.hashvault.pro:443] TLS send     (525 bytes)
[2020-09-25 10:49:05.785] [pool.hashvault.pro:443] TLS received (1071 bytes)
[2020-09-25 10:49:05.785] [pool.hashvault.pro:443] received (1041 bytes): "{"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","job":{"blob":"0e0eaaddb6fb05069cc0cad651fd19c1b092f434f61f325b38ede7c9874dcd6d0d9936bd4166ee000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000eb96a9d2010000005083d1cc010000007f293fc10100000ed85ac3ed03c696b770550de3419745c5246b48bfe2ae9a0a2d0b02f8c57b22f31762e3dc52168cedf1cbd648898b0504738f6795b73974960667242633727d44544643f7edc3b5e50b6679d7dcd31f18f69d0b5602a9915905f546fe2e2dd401","job_id":"88b37336-fe90-45c7-b8e8-c11245a5a062","target":"22480700","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023745773,"height":688552,"algo":"cn-heavy/xhv","variant":"xhv","motd":"0D0A486173685661756C74206B6565707320796F757220726967206861736872617465207365637572652E205468616E6B7320666F72207472757374696E67207573210D0A"},"extensions":["algo","motd","keepalive"],"status":"OK"}}"
[2020-09-25 10:49:05.785]  net      use pool pool.hashvault.pro:443 TLSv1.2 138.201.36.249
[2020-09-25 10:49:05.785]  net      new job from pool.hashvault.pro:443 diff 9000 algo cn-heavy/xhv height 688552
[2020-09-25 10:49:05.785]  opencl   use profile  cn-heavy  (6 threads) scratchpad 4096 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  1 |   0 | 01:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  2 |   1 | 04:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  3 |   1 | 04:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  4 |   2 | 05:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  5 |   2 | 05:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
[2020-09-25 10:49:05.929]  opencl   GPU #0 compiling...
[2020-09-25 10:49:08.012] [pool.hashvault.pro:443] TLS received (811 bytes)
[2020-09-25 10:49:08.013] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0eaaddb6fb05069cc0cad651fd19c1b092f434f61f325b38ede7c9874dcd6d0d9936bd4166ee000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000eb96a9d2010000005083d1cc010000007f293fc10100000ed85ac3ed03c696b770550de3419745c5246b48bfe2ae9a0a2d0b02f8c57b22f31762e3dc52168cedf1cbd648898b0504738f6795b73974960667242633727dd95aca8c927e7a5102aa83ebd133ef022b883822bfb628a4ea623d6d191dacd901","job_id":"d964c3ec-f625-4519-a34d-f4b98f70f31f","target":"40010400","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023748001,"height":688552,"algo":"cn-heavy/xhv","variant":"xhv"}}"
[2020-09-25 10:49:08.013]  net      new job from pool.hashvault.pro:443 diff 16364 algo cn-heavy/xhv height 688552
[2020-09-25 10:49:30.934]  opencl   GPU #0 compilation completed (25005 ms)
[2020-09-25 10:49:31.046]  opencl   GPU #2 compiling...
[2020-09-25 10:49:38.669] [pool.hashvault.pro:443] TLS received (811 bytes)
[2020-09-25 10:49:38.670] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0ea2deb6fb05069cc0cad651fd19c1b092f434f61f325b38ede7c9874dcd6d0d9936bd4166ee000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000eb96a9d2010000005083d1cc010000007f293fc10100000ed85ac3ed03c696b770550de3419745c5246b48bfe2ae9a0a2d0b02f8c57b22f31762e3dc52168cedf1cbd648898b0504738f6795b73974960667242633727dbec46c06d4bd05bb431f8402d2e2f7680ae1c8802f9c6356cf489ff5a6265ee901","job_id":"be27a97e-7b70-4f99-bc0d-6677756e0b42","target":"40010400","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023778656,"height":688552,"algo":"cn-heavy/xhv","variant":"xhv"}}"
[2020-09-25 10:49:38.670]  net      new job from pool.hashvault.pro:443 diff 16364 algo cn-heavy/xhv height 688552
[2020-09-25 10:49:43.821] [pool.hashvault.pro:443] TLS received (811 bytes)
[2020-09-25 10:49:43.821] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0ea7deb6fb05669407d8ef104a89ed818ba0c9df4b067df20993336663d86bf2ee612ffa5e50000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000315acdd2010000003179d7cc01000000e4f65cc1010000c9265118921e7a9d3e977724d4c9c26d8dc3e26ae666071cca3e1d8054c215a9e6066b3e34fba2fcd0d7f4be742b90cd750f842a44c0fbeaa51bcf3ac50a51ac3f1ade10541dec020def6e98a4bf1d85977a440f2b16ac7493a186f1cbbe752501","job_id":"126ec86a-d40b-4184-a6b6-27414623d7bc","target":"40010400","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023783808,"height":688553,"algo":"cn-heavy/xhv","variant":"xhv"}}"
[2020-09-25 10:49:43.821]  net      new job from pool.hashvault.pro:443 diff 16364 algo cn-heavy/xhv height 688553
[2020-09-25 10:49:54.454]  opencl   GPU #2 compilation completed (23408 ms)
[2020-09-25 10:49:54.454]  opencl   GPU #2 compiling...
[2020-09-25 10:50:07.473]  opencl   #0 01:00.0  67W 28C    0RPM 1125/1000MHz
[2020-09-25 10:50:07.475]  opencl   #1 04:00.0  36W 25C  867RPM 300/300MHz
[2020-09-25 10:50:07.475]  opencl   #2 05:00.0  33W 24C  861RPM 300/300MHz
[2020-09-25 10:50:07.475]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2020-09-25 10:50:08.014] [pool.hashvault.pro:443] TLS received (811 bytes)
[2020-09-25 10:50:08.014] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0ea7deb6fb05669407d8ef104a89ed818ba0c9df4b067df20993336663d86bf2ee612ffa5e50000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000315acdd2010000003179d7cc01000000e4f65cc1010000c9265118921e7a9d3e977724d4c9c26d8dc3e26ae666071cca3e1d8054c215a9e6066b3e34fba2fcd0d7f4be742b90cd750f842a44c0fbeaa51bcf3ac50a51ac70f1d316f870e391c88d87a8368ef9d1762c4ff7572d39cd3ab7370b4a2a017e01","job_id":"9ef5c36e-b0e9-4672-97f0-841986b87941","target":"ec010600","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023808002,"height":688553,"algo":"cn-heavy/xhv","variant":"xhv"}}"
[2020-09-25 10:50:08.014]  net      new job from pool.hashvault.pro:443 diff 10909 algo cn-heavy/xhv height 688553
[2020-09-25 10:50:17.889]  opencl   GPU #2 compilation completed (23435 ms)
[2020-09-25 10:50:18.004]  opencl   GPU #1 compiling...
[2020-09-25 10:50:41.360]  opencl   GPU #1 compilation completed (23357 ms)
[2020-09-25 10:50:41.360]  opencl   GPU #1 compiling...
[2020-09-25 10:51:04.715]  opencl   GPU #1 compilation completed (23355 ms)
[2020-09-25 10:51:04.715]  opencl   GPU #0 compiling...
[2020-09-25 10:51:09.137]  opencl   #0 01:00.0  66W 28C    0RPM 1125/1000MHz
[2020-09-25 10:51:09.137]  opencl   #1 04:00.0  33W 24C  869RPM 300/300MHz
[2020-09-25 10:51:09.137]  opencl   #2 05:00.0  33W 24C  861RPM 300/300MHz
[2020-09-25 10:51:09.137]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2020-09-25 10:51:09.137] [pool.hashvault.pro:443] TLS received (811 bytes)
[2020-09-25 10:51:09.137] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0ea7deb6fb05669407d8ef104a89ed818ba0c9df4b067df20993336663d86bf2ee612ffa5e50000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000315acdd2010000003179d7cc01000000e4f65cc1010000c9265118921e7a9d3e977724d4c9c26d8dc3e26ae666071cca3e1d8054c215a9e6066b3e34fba2fcd0d7f4be742b90cd750f842a44c0fbeaa51bcf3ac50a51acbfb60a54cf45cfe3574cc1ffe9f870fc25425d5477494119dd0039706e5b455901","job_id":"dc33c871-d03c-41c7-b6fb-68dae75c8818","target":"c7020900","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023868001,"height":688553,"algo":"cn-heavy/xhv","variant":"xhv"}}"
[2020-09-25 10:51:09.137]  net      new job from pool.hashvault.pro:443 diff 7273 algo cn-heavy/xhv height 688553
[2020-09-25 10:51:22.938] [pool.hashvault.pro:443] TLS received (811 bytes)
[2020-09-25 10:51:22.938] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0e8adfb6fb050524aef0247301bc3b328374654a7bd65e6e1138f22d7a51fc77195bd349252f000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000d43bdfd2010000003179d7cc01000000c5ec62c1010000e96ea8a2373c25b6cd77d83f3a3c4abcb8b6703d4a0cd346f82d76b065e0bc2eaa18b425117ae985f524b15a60d925b89ce6a2bd5771a96092fb90ea1dcb654b04dd4d72d6b49e43b2f5189b1ba1a3233ddb147848e015d7a736546cba2a4f2801","job_id":"297bc150-4599-45be-a811-459dff98fbe5","target":"c7020900","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023882920,"height":688554,"algo":"cn-heavy/xhv","variant":"xhv"}}"
[2020-09-25 10:51:22.938]  net      new job from pool.hashvault.pro:443 diff 7273 algo cn-heavy/xhv height 688554
[2020-09-25 10:51:29.657]  opencl   GPU #0 compilation completed (24941 ms)
[2020-09-25 10:51:29.657]  opencl   READY threads 6/6 (143871 ms)
Killed
me@rig:/data/git/xmrig/build$
```
 - Config file or command line (without wallets)
```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": false,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false
    },
    "opencl": {
        "enabled": true,
        "cache": false,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "astrobwt": [
            {
                "index": 0,
                "intensity": 192,
                "threads": [-1, -1]
            },
            {
                "index": 1,
                "intensity": 192,
                "threads": [-1, -1]
            },
            {
                "index": 2,
                "intensity": 192,
                "threads": [-1, -1]
            }
        ],
        "cn": [
            {
                "index": 0,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 576,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 576,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 576,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 9437184,
                "worksize": 256,
                "threads": [-1]
            },
            {
                "index": 1,
                "intensity": 9437184,
                "worksize": 256,
                "threads": [-1]
            },
            {
                "index": 2,
                "intensity": 9437184,
                "worksize": 256,
                "threads": [-1]
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 448,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 1,
                "intensity": 448,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 2,
                "intensity": 448,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 1,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 2,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 1,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 2,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.hashvault.pro:443",
            "user": "a_wallet_address",
            "pass": "rig",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": "420c7850e09b7c0bdcf748a7da9eb3647daf8515718f36d9ccfdd6b9ff834b14",
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "verbose": 1,
    "watch": true,
    "pause-on-battery": false
}
```
 - OS: Ubuntu 20.04.1 (Linux rig 5.4.0-48-generic #52-Ubuntu SMP Thu Sep 10 10:58:49 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux)
 - For GPU related issues: information about GPUs and driver version.
AMD driver `amdgpu-pro-20.30-1109583-ubuntu-20.04`
```Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.1 AMD-APP (3143.9)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 3
  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Radeon RX 580 Series
  Device Topology:				 PCI[ B#1, D#0, F#0 ]
  Max compute units:				 36
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1411Mhz
  Address bits:					 64
  Max memory allocation:			 3422266572
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 16
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 2048
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 4289183744
  Constant buffer size:				 3422266572
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 32768
  Max pipe arguments:				 0
  Max pipe active reservations:			 0
  Max pipe packet size:				 0
  Max global variable size:			 0
  Max global variable preferred total size:	 0
  Max read/write image args:			 0
  Max on device events:				 0
  Queue on device max size:			 0
  Max on device queues:				 0
  Queue on device preferred size:		 0
  SVM capabilities:
    Coarse grain buffer:			 No
    Fine grain buffer:				 No
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:
    Out-of-Order:				 No
    Profiling :					 No
  Platform ID:					 0x7f7e7a861e50
  Name:						 Ellesmere
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 1.2
  Driver version:				 3143.9
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 AMD-APP (3143.9)
  Extensions:					 cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event


  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Radeon RX 580 Series
  Device Topology:				 PCI[ B#4, D#0, F#0 ]
  Max compute units:				 36
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1411Mhz
  Address bits:					 64
  Max memory allocation:			 3422155161
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 16
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 2048
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 4289060864
  Constant buffer size:				 3422155161
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 32768
  Max pipe arguments:				 0
  Max pipe active reservations:			 0
  Max pipe packet size:				 0
  Max global variable size:			 0
  Max global variable preferred total size:	 0
  Max read/write image args:			 0
  Max on device events:				 0
  Queue on device max size:			 0
  Max on device queues:				 0
  Queue on device preferred size:		 0
  SVM capabilities:
    Coarse grain buffer:			 No
    Fine grain buffer:				 No
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:
    Out-of-Order:				 No
    Profiling :					 No
  Platform ID:					 0x7f7e7a861e50
  Name:						 Ellesmere
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 1.2
  Driver version:				 3143.9
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 AMD-APP (3143.9)
  Extensions:					 cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event


  Device Type:					 CL_DEVICE_TYPE_GPU
  Vendor ID:					 1002h
  Board name:					 Radeon RX 580 Series
  Device Topology:				 PCI[ B#5, D#0, F#0 ]
  Max compute units:				 36
  Max work items dimensions:			 3
    Max work items[0]:				 1024
    Max work items[1]:				 1024
    Max work items[2]:				 1024
  Max work group size:				 256
  Preferred vector width char:			 4
  Preferred vector width short:			 2
  Preferred vector width int:			 1
  Preferred vector width long:			 1
  Preferred vector width float:			 1
  Preferred vector width double:		 1
  Native vector width char:			 4
  Native vector width short:			 2
  Native vector width int:			 1
  Native vector width long:			 1
  Native vector width float:			 1
  Native vector width double:			 1
  Max clock frequency:				 1411Mhz
  Address bits:					 64
  Max memory allocation:			 3422155161
  Image support:				 Yes
  Max number of images read arguments:		 128
  Max number of images write arguments:		 8
  Max image 2D width:				 16384
  Max image 2D height:				 16384
  Max image 3D width:				 2048
  Max image 3D height:				 2048
  Max image 3D depth:				 2048
  Max samplers within kernel:			 16
  Max size of kernel argument:			 1024
  Alignment (bits) of base address:		 2048
  Minimum alignment (bytes) for any datatype:	 128
  Single precision floating point capability
    Denorms:					 No
    Quiet NaNs:					 Yes
    Round to nearest even:			 Yes
    Round to zero:				 Yes
    Round to +ve and infinity:			 Yes
    IEEE754-2008 fused multiply-add:		 Yes
  Cache type:					 Read/Write
  Cache line size:				 64
  Cache size:					 16384
  Global memory size:				 4289060864
  Constant buffer size:				 3422155161
  Max number of constant args:			 8
  Local memory type:				 Scratchpad
  Local memory size:				 32768
  Max pipe arguments:				 0
  Max pipe active reservations:			 0
  Max pipe packet size:				 0
  Max global variable size:			 0
  Max global variable preferred total size:	 0
  Max read/write image args:			 0
  Max on device events:				 0
  Queue on device max size:			 0
  Max on device queues:				 0
  Queue on device preferred size:		 0
  SVM capabilities:
    Coarse grain buffer:			 No
    Fine grain buffer:				 No
    Fine grain system:				 No
    Atomics:					 No
  Preferred platform atomic alignment:		 0
  Preferred global atomic alignment:		 0
  Preferred local atomic alignment:		 0
  Kernel Preferred work group size multiple:	 64
  Error correction support:			 0
  Unified memory for Host and Device:		 0
  Profiling timer resolution:			 1
  Device endianess:				 Little
  Available:					 Yes
  Compiler available:				 Yes
  Execution capabilities:
    Execute OpenCL kernels:			 Yes
    Execute native function:			 No
  Queue on Host properties:
    Out-of-Order:				 No
    Profiling :					 Yes
  Queue on Device properties:
    Out-of-Order:				 No
    Profiling :					 No
  Platform ID:					 0x7f7e7a861e50
  Name:						 Ellesmere
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 1.2
  Driver version:				 3143.9
  Profile:					 FULL_PROFILE
  Version:					 OpenCL 1.2 AMD-APP (3143.9)
  Extensions:					 cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event
```
**Additional context**
Video BIOS are original ones.

# Discussion History
## fmasclef | 2020-09-25T11:28:46+00:00
I mitigate this issue by reducing the number of threads. Using the following config :

```
"cn-heavy": [
            {
                "index": 0,
                "intensity": 576,
                "worksize": 8,
                "strided_index": [1],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 576,
                "worksize": 8,
                "strided_index": [1],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 576,
                "worksize": 8,
                "strided_index": [1],
                "threads": [-1],
                "unroll": 8
            }
        ],
```

It's mining !

```
 * ABOUT        XMRig/6.3.4 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Celeron(R) CPU G3900 @ 2.80GHz (1) x64 AES
                L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
 * MEMORY       0.6/3.7 GB (16%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.hashvault.pro:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3143.9)
 * OPENCL GPU   #0 01:00.0 Radeon RX 580 Series (Ellesmere) 1220 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #1 04:00.0 Radeon RX 580 Series (Ellesmere) 1220 MHz cu:36 mem:3839/4090 MB
 * OPENCL GPU   #2 05:00.0 Radeon RX 580 Series (Ellesmere) 1220 MHz cu:36 mem:3839/4090 MB
 * CUDA         disabled
[2020-09-25 13:13:44.527]  net      use pool pool.hashvault.pro:443 TLSv1.2 138.201.36.249
[2020-09-25 13:13:44.527]  net      new job from pool.hashvault.pro:443 diff 9000 algo cn-heavy/xhv height 688636
[2020-09-25 13:13:44.527]  opencl   use profile  cn-heavy  (3 threads) scratchpad 4096 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  1 |   1 | 04:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
|  2 |   2 | 05:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
[2020-09-25 13:13:44.787]  opencl   GPU #0 compiling...
[2020-09-25 13:14:09.815]  opencl   GPU #0 compilation completed (25028 ms)
[2020-09-25 13:14:09.928]  opencl   GPU #2 compiling...
[2020-09-25 13:14:33.330]  opencl   GPU #2 compilation completed (23403 ms)
[2020-09-25 13:14:33.443]  opencl   GPU #1 compiling...
[2020-09-25 13:14:36.618]  net      new job from pool.hashvault.pro:443 diff 9000 algo cn-heavy/xhv height 688637
[2020-09-25 13:14:46.193]  opencl   #0 01:00.0  55W 34C    0RPM 1008/1000MHz
[2020-09-25 13:14:46.193]  opencl   #1 04:00.0  32W 27C  868RPM 300/300MHz
[2020-09-25 13:14:46.193]  opencl   #2 05:00.0  32W 25C  860RPM 300/300MHz
[2020-09-25 13:14:46.193]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2020-09-25 13:14:56.858]  opencl   GPU #1 compilation completed (23414 ms)
[2020-09-25 13:14:56.858]  opencl   READY threads 3/3 (72332 ms)
[2020-09-25 13:15:01.214]  opencl   accepted (1/0) diff 9000 (44 ms)
[2020-09-25 13:15:07.072]  opencl   accepted (2/0) diff 9000 (43 ms)
```

So I guess 4GB are too few for 2 threads. There might be some room for improvement as it seems `xmrig` uses only half the memory available on each board.

## fmasclef | 2020-09-25T16:09:21+00:00
Intensity increased, hashrate as well.

## Saikatsaha1996 | 2021-04-26T12:10:53+00:00
> **Describe the bug**
> `xmrig` crash right after ending OpenCL compilation when threads are `READY`. It always ends up in process killed or segfault if using opencl cache.
> 
> **To Reproduce**
> 
> * do an Ubuntu 20.04.1 fresh install
> * add your user to both `video` and `render` groups
> * install AMD APP SDK 3 and make sure to export LD_LIBRARY_PATH (not sure it's needed)
> * reboot
> * install latest AMD PRO drivers
> * reboot
> * `clinfo` shows the OpenCL info, including all video adapters (here, 3)
> * follow compilation guide (or use the focal binary, same result)
> * start mining cn-heavy/xhv
> 
> **Expected behavior**
> `xmrig` to actualy mine something
> 
> **Required data**
> 
> * Miner log as text or screenshot
>   with opencl cache :
> 
> ```
> me@rig:/data/git/xmrig/build$ ./xmrig -c config.json
>  * ABOUT        XMRig/6.3.4 gcc/9.3.0
>  * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
>  * HUGE PAGES   supported
>  * 1GB PAGES    disabled
>  * CPU          Intel(R) Celeron(R) CPU G3900 @ 2.80GHz (1) x64 AES
>                 L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
>  * MEMORY       0.9/3.7 GB (24%)
>  * DONATE       5%
>  * ASSEMBLY     auto:intel
>  * POOL #1      pool.hashvault.pro:443 algo auto
> [2020-09-25 10:48:45.945] POOLS --------------------------------------------------------------------
> [2020-09-25 10:48:45.945] url:       pool.hashvault.pro:443
> [2020-09-25 10:48:45.945] host:      pool.hashvault.pro
> [2020-09-25 10:48:45.945] port:      443
> [2020-09-25 10:48:45.945] user:      a_wallet_address_goes_here
> [2020-09-25 10:48:45.945] pass:      rig
> [2020-09-25 10:48:45.945] rig-id     (null)
> [2020-09-25 10:48:45.945] algo:      invalid
> [2020-09-25 10:48:45.945] nicehash:  0
> [2020-09-25 10:48:45.945] keepAlive: 60
> [2020-09-25 10:48:45.945] --------------------------------------------------------------------------
>  * COMMANDS     hashrate, pause, resume, results, connection
> [2020-09-25 10:48:45.946]  config   configuration saved to: "/data/crypto/xmrig/config.json"
>  * ADL          press e for health report
>  * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3143.9)
>  * OPENCL GPU   #0 01:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
>  * OPENCL GPU   #1 04:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
>  * OPENCL GPU   #2 05:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
>  * CUDA         disabled
> [2020-09-25 10:48:45.946] [pool.hashvault.pro:443] state: "unconnected" -> "host-lookup"
> [2020-09-25 10:48:45.951] [pool.hashvault.pro:443] state: "host-lookup" -> "connecting"
> [2020-09-25 10:48:45.973] [pool.hashvault.pro:443] state: "connecting" -> "connected"
> [2020-09-25 10:48:45.973] [pool.hashvault.pro:443] TLS send     (283 bytes)
> [2020-09-25 10:48:45.996] [pool.hashvault.pro:443] TLS received (1328 bytes)
> [2020-09-25 10:48:45.997] [pool.hashvault.pro:443] TLS send     (93 bytes)
> [2020-09-25 10:48:46.019] [pool.hashvault.pro:443] TLS received (258 bytes)
> [2020-09-25 10:48:46.019] [pool.hashvault.pro:443] send (496 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"a_wallet_address_goes_here","pass":"rig","agent":"XMRig/6.3.4 (Linux x86_64) libuv/1.34.2 gcc/9.3.0","algo":["cn/1","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/ccx","rx/0","rx/wow","rx/loki","rx/arq","rx/sfx","rx/keva","astrobwt","kawpow"]}}"
> [2020-09-25 10:48:46.019] [pool.hashvault.pro:443] TLS send     (525 bytes)
> [2020-09-25 10:48:46.041] [pool.hashvault.pro:443] TLS received (1071 bytes)
> [2020-09-25 10:48:46.042] [pool.hashvault.pro:443] received (1041 bytes): "{"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"f6c446c7-987e-45da-9f62-7b69cefde281","job":{"blob":"0e0eaaddb6fb05069cc0cad651fd19c1b092f434f61f325b38ede7c9874dcd6d0d9936bd4166ee000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000eb96a9d2010000005083d1cc010000007f293fc10100000ed85ac3ed03c696b770550de3419745c5246b48bfe2ae9a0a2d0b02f8c57b22f31762e3dc52168cedf1cbd648898b0504738f6795b73974960667242633727dcb83f086fdc074306efb5014d6cb2d59826877d195e01de8f99ad0460a07370001","job_id":"09a577ff-ad6f-4b2e-aeeb-19953817222c","target":"22480700","id":"f6c446c7-987e-45da-9f62-7b69cefde281","timestamp":1601023726029,"height":688552,"algo":"cn-heavy/xhv","variant":"xhv","motd":"0D0A486173685661756C74206B6565707320796F757220726967206861736872617465207365637572652E205468616E6B7320666F72207472757374696E67207573210D0A"},"extensions":["algo","motd","keepalive"],"status":"OK"}}"
> [2020-09-25 10:48:46.042]  net      use pool pool.hashvault.pro:443 TLSv1.2 138.201.36.249
> [2020-09-25 10:48:46.042]  net      new job from pool.hashvault.pro:443 diff 9000 algo cn-heavy/xhv height 688552
> [2020-09-25 10:48:46.042]  opencl   use profile  cn-heavy  (6 threads) scratchpad 4096 KB
> |  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
> |  0 |   0 | 01:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> |  1 |   0 | 01:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> |  2 |   1 | 04:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> |  3 |   1 | 04:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> |  4 |   2 | 05:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> |  5 |   2 | 05:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> Segmentation fault
> ```
> 
> without opencl cache:
> 
> ```
> me@rig:/data/git/xmrig/build$ ./xmrig -c config.json --opencl-no-cache
>  * ABOUT        XMRig/6.3.4 gcc/9.3.0
>  * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
>  * HUGE PAGES   supported
>  * 1GB PAGES    disabled
>  * CPU          Intel(R) Celeron(R) CPU G3900 @ 2.80GHz (1) x64 AES
>                 L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
>  * MEMORY       0.9/3.7 GB (24%)
>  * DONATE       5%
>  * ASSEMBLY     auto:intel
>  * POOL #1      pool.hashvault.pro:443 algo auto
> [2020-09-25 10:49:05.625] POOLS --------------------------------------------------------------------
> [2020-09-25 10:49:05.625] url:       pool.hashvault.pro:443
> [2020-09-25 10:49:05.625] host:      pool.hashvault.pro
> [2020-09-25 10:49:05.625] port:      443
> [2020-09-25 10:49:05.625] user:      a_wallet_address_goes_here
> [2020-09-25 10:49:05.625] pass:      rig
> [2020-09-25 10:49:05.625] rig-id     (null)
> [2020-09-25 10:49:05.625] algo:      invalid
> [2020-09-25 10:49:05.625] nicehash:  0
> [2020-09-25 10:49:05.625] keepAlive: 60
> [2020-09-25 10:49:05.625] --------------------------------------------------------------------------
>  * COMMANDS     hashrate, pause, resume, results, connection
> [2020-09-25 10:49:05.626]  config   configuration saved to: "/data/crypto/xmrig/config.json"
>  * ADL          press e for health report
>  * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3143.9)
>  * OPENCL GPU   #0 01:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
>  * OPENCL GPU   #1 04:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
>  * OPENCL GPU   #2 05:00.0 Radeon RX 580 Series (Ellesmere) 1411 MHz cu:36 mem:3263/4090 MB
>  * CUDA         disabled
> [2020-09-25 10:49:05.626] [pool.hashvault.pro:443] state: "unconnected" -> "host-lookup"
> [2020-09-25 10:49:05.693] [pool.hashvault.pro:443] state: "host-lookup" -> "connecting"
> [2020-09-25 10:49:05.715] [pool.hashvault.pro:443] state: "connecting" -> "connected"
> [2020-09-25 10:49:05.715] [pool.hashvault.pro:443] TLS send     (283 bytes)
> [2020-09-25 10:49:05.738] [pool.hashvault.pro:443] TLS received (1328 bytes)
> [2020-09-25 10:49:05.740] [pool.hashvault.pro:443] TLS send     (93 bytes)
> [2020-09-25 10:49:05.762] [pool.hashvault.pro:443] TLS received (258 bytes)
> [2020-09-25 10:49:05.762] [pool.hashvault.pro:443] send (496 bytes): "{"id":1,"jsonrpc":"2.0","method":"login","params":{"login":"a_wallet_address_goes_here","pass":"rig","agent":"XMRig/6.3.4 (Linux x86_64) libuv/1.34.2 gcc/9.3.0","algo":["cn/1","cn/2","cn/r","cn/fast","cn/half","cn/xao","cn/rto","cn/rwz","cn/zls","cn/double","cn-lite/1","cn-heavy/0","cn-heavy/tube","cn-heavy/xhv","cn-pico","cn-pico/tlo","cn/ccx","rx/0","rx/wow","rx/loki","rx/arq","rx/sfx","rx/keva","astrobwt","kawpow"]}}"
> [2020-09-25 10:49:05.762] [pool.hashvault.pro:443] TLS send     (525 bytes)
> [2020-09-25 10:49:05.785] [pool.hashvault.pro:443] TLS received (1071 bytes)
> [2020-09-25 10:49:05.785] [pool.hashvault.pro:443] received (1041 bytes): "{"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","job":{"blob":"0e0eaaddb6fb05069cc0cad651fd19c1b092f434f61f325b38ede7c9874dcd6d0d9936bd4166ee000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000eb96a9d2010000005083d1cc010000007f293fc10100000ed85ac3ed03c696b770550de3419745c5246b48bfe2ae9a0a2d0b02f8c57b22f31762e3dc52168cedf1cbd648898b0504738f6795b73974960667242633727d44544643f7edc3b5e50b6679d7dcd31f18f69d0b5602a9915905f546fe2e2dd401","job_id":"88b37336-fe90-45c7-b8e8-c11245a5a062","target":"22480700","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023745773,"height":688552,"algo":"cn-heavy/xhv","variant":"xhv","motd":"0D0A486173685661756C74206B6565707320796F757220726967206861736872617465207365637572652E205468616E6B7320666F72207472757374696E67207573210D0A"},"extensions":["algo","motd","keepalive"],"status":"OK"}}"
> [2020-09-25 10:49:05.785]  net      use pool pool.hashvault.pro:443 TLSv1.2 138.201.36.249
> [2020-09-25 10:49:05.785]  net      new job from pool.hashvault.pro:443 diff 9000 algo cn-heavy/xhv height 688552
> [2020-09-25 10:49:05.785]  opencl   use profile  cn-heavy  (6 threads) scratchpad 4096 KB
> |  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
> |  0 |   0 | 01:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> |  1 |   0 | 01:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> |  2 |   1 | 04:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> |  3 |   1 | 04:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> |  4 |   2 | 05:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> |  5 |   2 | 05:00.0 |       576 |     8 |   2304 | Radeon RX 580 Series (Ellesmere)
> [2020-09-25 10:49:05.929]  opencl   GPU #0 compiling...
> [2020-09-25 10:49:08.012] [pool.hashvault.pro:443] TLS received (811 bytes)
> [2020-09-25 10:49:08.013] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0eaaddb6fb05069cc0cad651fd19c1b092f434f61f325b38ede7c9874dcd6d0d9936bd4166ee000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000eb96a9d2010000005083d1cc010000007f293fc10100000ed85ac3ed03c696b770550de3419745c5246b48bfe2ae9a0a2d0b02f8c57b22f31762e3dc52168cedf1cbd648898b0504738f6795b73974960667242633727dd95aca8c927e7a5102aa83ebd133ef022b883822bfb628a4ea623d6d191dacd901","job_id":"d964c3ec-f625-4519-a34d-f4b98f70f31f","target":"40010400","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023748001,"height":688552,"algo":"cn-heavy/xhv","variant":"xhv"}}"
> [2020-09-25 10:49:08.013]  net      new job from pool.hashvault.pro:443 diff 16364 algo cn-heavy/xhv height 688552
> [2020-09-25 10:49:30.934]  opencl   GPU #0 compilation completed (25005 ms)
> [2020-09-25 10:49:31.046]  opencl   GPU #2 compiling...
> [2020-09-25 10:49:38.669] [pool.hashvault.pro:443] TLS received (811 bytes)
> [2020-09-25 10:49:38.670] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0ea2deb6fb05069cc0cad651fd19c1b092f434f61f325b38ede7c9874dcd6d0d9936bd4166ee000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000eb96a9d2010000005083d1cc010000007f293fc10100000ed85ac3ed03c696b770550de3419745c5246b48bfe2ae9a0a2d0b02f8c57b22f31762e3dc52168cedf1cbd648898b0504738f6795b73974960667242633727dbec46c06d4bd05bb431f8402d2e2f7680ae1c8802f9c6356cf489ff5a6265ee901","job_id":"be27a97e-7b70-4f99-bc0d-6677756e0b42","target":"40010400","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023778656,"height":688552,"algo":"cn-heavy/xhv","variant":"xhv"}}"
> [2020-09-25 10:49:38.670]  net      new job from pool.hashvault.pro:443 diff 16364 algo cn-heavy/xhv height 688552
> [2020-09-25 10:49:43.821] [pool.hashvault.pro:443] TLS received (811 bytes)
> [2020-09-25 10:49:43.821] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0ea7deb6fb05669407d8ef104a89ed818ba0c9df4b067df20993336663d86bf2ee612ffa5e50000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000315acdd2010000003179d7cc01000000e4f65cc1010000c9265118921e7a9d3e977724d4c9c26d8dc3e26ae666071cca3e1d8054c215a9e6066b3e34fba2fcd0d7f4be742b90cd750f842a44c0fbeaa51bcf3ac50a51ac3f1ade10541dec020def6e98a4bf1d85977a440f2b16ac7493a186f1cbbe752501","job_id":"126ec86a-d40b-4184-a6b6-27414623d7bc","target":"40010400","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023783808,"height":688553,"algo":"cn-heavy/xhv","variant":"xhv"}}"
> [2020-09-25 10:49:43.821]  net      new job from pool.hashvault.pro:443 diff 16364 algo cn-heavy/xhv height 688553
> [2020-09-25 10:49:54.454]  opencl   GPU #2 compilation completed (23408 ms)
> [2020-09-25 10:49:54.454]  opencl   GPU #2 compiling...
> [2020-09-25 10:50:07.473]  opencl   #0 01:00.0  67W 28C    0RPM 1125/1000MHz
> [2020-09-25 10:50:07.475]  opencl   #1 04:00.0  36W 25C  867RPM 300/300MHz
> [2020-09-25 10:50:07.475]  opencl   #2 05:00.0  33W 24C  861RPM 300/300MHz
> [2020-09-25 10:50:07.475]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
> [2020-09-25 10:50:08.014] [pool.hashvault.pro:443] TLS received (811 bytes)
> [2020-09-25 10:50:08.014] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0ea7deb6fb05669407d8ef104a89ed818ba0c9df4b067df20993336663d86bf2ee612ffa5e50000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000315acdd2010000003179d7cc01000000e4f65cc1010000c9265118921e7a9d3e977724d4c9c26d8dc3e26ae666071cca3e1d8054c215a9e6066b3e34fba2fcd0d7f4be742b90cd750f842a44c0fbeaa51bcf3ac50a51ac70f1d316f870e391c88d87a8368ef9d1762c4ff7572d39cd3ab7370b4a2a017e01","job_id":"9ef5c36e-b0e9-4672-97f0-841986b87941","target":"ec010600","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023808002,"height":688553,"algo":"cn-heavy/xhv","variant":"xhv"}}"
> [2020-09-25 10:50:08.014]  net      new job from pool.hashvault.pro:443 diff 10909 algo cn-heavy/xhv height 688553
> [2020-09-25 10:50:17.889]  opencl   GPU #2 compilation completed (23435 ms)
> [2020-09-25 10:50:18.004]  opencl   GPU #1 compiling...
> [2020-09-25 10:50:41.360]  opencl   GPU #1 compilation completed (23357 ms)
> [2020-09-25 10:50:41.360]  opencl   GPU #1 compiling...
> [2020-09-25 10:51:04.715]  opencl   GPU #1 compilation completed (23355 ms)
> [2020-09-25 10:51:04.715]  opencl   GPU #0 compiling...
> [2020-09-25 10:51:09.137]  opencl   #0 01:00.0  66W 28C    0RPM 1125/1000MHz
> [2020-09-25 10:51:09.137]  opencl   #1 04:00.0  33W 24C  869RPM 300/300MHz
> [2020-09-25 10:51:09.137]  opencl   #2 05:00.0  33W 24C  861RPM 300/300MHz
> [2020-09-25 10:51:09.137]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
> [2020-09-25 10:51:09.137] [pool.hashvault.pro:443] TLS received (811 bytes)
> [2020-09-25 10:51:09.137] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0ea7deb6fb05669407d8ef104a89ed818ba0c9df4b067df20993336663d86bf2ee612ffa5e50000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000315acdd2010000003179d7cc01000000e4f65cc1010000c9265118921e7a9d3e977724d4c9c26d8dc3e26ae666071cca3e1d8054c215a9e6066b3e34fba2fcd0d7f4be742b90cd750f842a44c0fbeaa51bcf3ac50a51acbfb60a54cf45cfe3574cc1ffe9f870fc25425d5477494119dd0039706e5b455901","job_id":"dc33c871-d03c-41c7-b6fb-68dae75c8818","target":"c7020900","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023868001,"height":688553,"algo":"cn-heavy/xhv","variant":"xhv"}}"
> [2020-09-25 10:51:09.137]  net      new job from pool.hashvault.pro:443 diff 7273 algo cn-heavy/xhv height 688553
> [2020-09-25 10:51:22.938] [pool.hashvault.pro:443] TLS received (811 bytes)
> [2020-09-25 10:51:22.938] [pool.hashvault.pro:443] received (781 bytes): "{"jsonrpc":"2.0","method":"job","params":{"blob":"0e0e8adfb6fb050524aef0247301bc3b328374654a7bd65e6e1138f22d7a51fc77195bd349252f000000009633c9da130000001f662e3f0000000010215f6d8d020000390c150b000000000000000000000000eb959533ab0100000000000000000000fc8e2acc8a01000071c0de6969010000a644376be0bd00000000000000000000000000000000000000583201cd01000000d43bdfd2010000003179d7cc01000000c5ec62c1010000e96ea8a2373c25b6cd77d83f3a3c4abcb8b6703d4a0cd346f82d76b065e0bc2eaa18b425117ae985f524b15a60d925b89ce6a2bd5771a96092fb90ea1dcb654b04dd4d72d6b49e43b2f5189b1ba1a3233ddb147848e015d7a736546cba2a4f2801","job_id":"297bc150-4599-45be-a811-459dff98fbe5","target":"c7020900","id":"3f167ef2-77c0-4d32-bbf7-ab795b60d570","timestamp":1601023882920,"height":688554,"algo":"cn-heavy/xhv","variant":"xhv"}}"
> [2020-09-25 10:51:22.938]  net      new job from pool.hashvault.pro:443 diff 7273 algo cn-heavy/xhv height 688554
> [2020-09-25 10:51:29.657]  opencl   GPU #0 compilation completed (24941 ms)
> [2020-09-25 10:51:29.657]  opencl   READY threads 6/6 (143871 ms)
> Killed
> me@rig:/data/git/xmrig/build$
> ```
> 
> * Config file or command line (without wallets)
> 
> ```
> {
>     "api": {
>         "id": null,
>         "worker-id": null
>     },
>     "http": {
>         "enabled": false,
>         "host": "127.0.0.1",
>         "port": 0,
>         "access-token": null,
>         "restricted": true
>     },
>     "autosave": true,
>     "background": false,
>     "colors": true,
>     "title": true,
>     "randomx": {
>         "init": -1,
>         "mode": "auto",
>         "1gb-pages": false,
>         "rdmsr": true,
>         "wrmsr": true,
>         "cache_qos": false,
>         "numa": true,
>         "scratchpad_prefetch_mode": 1
>     },
>     "cpu": {
>         "enabled": false,
>         "huge-pages": true,
>         "hw-aes": null,
>         "priority": null,
>         "memory-pool": false,
>         "yield": true,
>         "max-threads-hint": 100,
>         "asm": true,
>         "argon2-impl": null,
>         "astrobwt-max-size": 550,
>         "astrobwt-avx2": false
>     },
>     "opencl": {
>         "enabled": true,
>         "cache": false,
>         "loader": null,
>         "platform": "AMD",
>         "adl": true,
>         "astrobwt": [
>             {
>                 "index": 0,
>                 "intensity": 192,
>                 "threads": [-1, -1]
>             },
>             {
>                 "index": 1,
>                 "intensity": 192,
>                 "threads": [-1, -1]
>             },
>             {
>                 "index": 2,
>                 "intensity": 192,
>                 "threads": [-1, -1]
>             }
>         ],
>         "cn": [
>             {
>                 "index": 0,
>                 "intensity": 864,
>                 "worksize": 8,
>                 "strided_index": [1, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             },
>             {
>                 "index": 1,
>                 "intensity": 864,
>                 "worksize": 8,
>                 "strided_index": [1, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             },
>             {
>                 "index": 2,
>                 "intensity": 864,
>                 "worksize": 8,
>                 "strided_index": [1, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             }
>         ],
>         "cn-heavy": [
>             {
>                 "index": 0,
>                 "intensity": 576,
>                 "worksize": 8,
>                 "strided_index": [1, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             },
>             {
>                 "index": 1,
>                 "intensity": 576,
>                 "worksize": 8,
>                 "strided_index": [1, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             },
>             {
>                 "index": 2,
>                 "intensity": 576,
>                 "worksize": 8,
>                 "strided_index": [1, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             }
>         ],
>         "cn-lite": [
>             {
>                 "index": 0,
>                 "intensity": 1728,
>                 "worksize": 8,
>                 "strided_index": [1, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             },
>             {
>                 "index": 1,
>                 "intensity": 1728,
>                 "worksize": 8,
>                 "strided_index": [1, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             },
>             {
>                 "index": 2,
>                 "intensity": 1728,
>                 "worksize": 8,
>                 "strided_index": [1, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             }
>         ],
>         "cn-pico": [
>             {
>                 "index": 0,
>                 "intensity": 1728,
>                 "worksize": 8,
>                 "strided_index": [2, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             },
>             {
>                 "index": 1,
>                 "intensity": 1728,
>                 "worksize": 8,
>                 "strided_index": [2, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             },
>             {
>                 "index": 2,
>                 "intensity": 1728,
>                 "worksize": 8,
>                 "strided_index": [2, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             }
>         ],
>         "cn/2": [
>             {
>                 "index": 0,
>                 "intensity": 864,
>                 "worksize": 8,
>                 "strided_index": [2, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             },
>             {
>                 "index": 1,
>                 "intensity": 864,
>                 "worksize": 8,
>                 "strided_index": [2, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             },
>             {
>                 "index": 2,
>                 "intensity": 864,
>                 "worksize": 8,
>                 "strided_index": [2, 2],
>                 "threads": [-1, -1],
>                 "unroll": 8
>             }
>         ],
>         "kawpow": [
>             {
>                 "index": 0,
>                 "intensity": 9437184,
>                 "worksize": 256,
>                 "threads": [-1]
>             },
>             {
>                 "index": 1,
>                 "intensity": 9437184,
>                 "worksize": 256,
>                 "threads": [-1]
>             },
>             {
>                 "index": 2,
>                 "intensity": 9437184,
>                 "worksize": 256,
>                 "threads": [-1]
>             }
>         ],
>         "rx": [
>             {
>                 "index": 0,
>                 "intensity": 448,
>                 "worksize": 8,
>                 "threads": [-1, -1],
>                 "bfactor": 6,
>                 "gcn_asm": true,
>                 "dataset_host": false
>             },
>             {
>                 "index": 1,
>                 "intensity": 448,
>                 "worksize": 8,
>                 "threads": [-1, -1],
>                 "bfactor": 6,
>                 "gcn_asm": true,
>                 "dataset_host": false
>             },
>             {
>                 "index": 2,
>                 "intensity": 448,
>                 "worksize": 8,
>                 "threads": [-1, -1],
>                 "bfactor": 6,
>                 "gcn_asm": true,
>                 "dataset_host": false
>             }
>         ],
>         "rx/arq": [
>             {
>                 "index": 0,
>                 "intensity": 576,
>                 "worksize": 8,
>                 "threads": [-1, -1],
>                 "bfactor": 6,
>                 "gcn_asm": true,
>                 "dataset_host": false
>             },
>             {
>                 "index": 1,
>                 "intensity": 576,
>                 "worksize": 8,
>                 "threads": [-1, -1],
>                 "bfactor": 6,
>                 "gcn_asm": true,
>                 "dataset_host": false
>             },
>             {
>                 "index": 2,
>                 "intensity": 576,
>                 "worksize": 8,
>                 "threads": [-1, -1],
>                 "bfactor": 6,
>                 "gcn_asm": true,
>                 "dataset_host": false
>             }
>         ],
>         "rx/wow": [
>             {
>                 "index": 0,
>                 "intensity": 576,
>                 "worksize": 8,
>                 "threads": [-1, -1],
>                 "bfactor": 6,
>                 "gcn_asm": true,
>                 "dataset_host": false
>             },
>             {
>                 "index": 1,
>                 "intensity": 576,
>                 "worksize": 8,
>                 "threads": [-1, -1],
>                 "bfactor": 6,
>                 "gcn_asm": true,
>                 "dataset_host": false
>             },
>             {
>                 "index": 2,
>                 "intensity": 576,
>                 "worksize": 8,
>                 "threads": [-1, -1],
>                 "bfactor": 6,
>                 "gcn_asm": true,
>                 "dataset_host": false
>             }
>         ],
>         "cn/0": false,
>         "cn-lite/0": false
>     },
>     "cuda": {
>         "enabled": false,
>         "loader": null,
>         "nvml": true
>     },
>     "donate-level": 5,
>     "donate-over-proxy": 1,
>     "log-file": null,
>     "pools": [
>         {
>             "algo": null,
>             "coin": null,
>             "url": "pool.hashvault.pro:443",
>             "user": "a_wallet_address",
>             "pass": "rig",
>             "rig-id": null,
>             "nicehash": false,
>             "keepalive": true,
>             "enabled": true,
>             "tls": true,
>             "tls-fingerprint": "420c7850e09b7c0bdcf748a7da9eb3647daf8515718f36d9ccfdd6b9ff834b14",
>             "daemon": false,
>             "socks5": null,
>             "self-select": null
>         }
>     ],
>     "print-time": 60,
>     "health-print-time": 60,
>     "retries": 5,
>     "retry-pause": 5,
>     "syslog": false,
>     "tls": {
>         "enabled": false,
>         "protocols": null,
>         "cert": null,
>         "cert_key": null,
>         "ciphers": null,
>         "ciphersuites": null,
>         "dhparam": null
>     },
>     "user-agent": null,
>     "verbose": 1,
>     "watch": true,
>     "pause-on-battery": false
> }
> ```
> 
> * OS: Ubuntu 20.04.1 (Linux rig 5.4.0-48-generic #52-Ubuntu SMP Thu Sep 10 10:58:49 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux)
> * For GPU related issues: information about GPUs and driver version.
>   AMD driver `amdgpu-pro-20.30-1109583-ubuntu-20.04`
> 
> ```
>   Platform Profile:				 FULL_PROFILE
>   Platform Version:				 OpenCL 2.1 AMD-APP (3143.9)
>   Platform Name:				 AMD Accelerated Parallel Processing
>   Platform Vendor:				 Advanced Micro Devices, Inc.
>   Platform Extensions:				 cl_khr_icd cl_amd_event_callback cl_amd_offline_devices
> 
> 
>   Platform Name:				 AMD Accelerated Parallel Processing
> Number of devices:				 3
>   Device Type:					 CL_DEVICE_TYPE_GPU
>   Vendor ID:					 1002h
>   Board name:					 Radeon RX 580 Series
>   Device Topology:				 PCI[ B#1, D#0, F#0 ]
>   Max compute units:				 36
>   Max work items dimensions:			 3
>     Max work items[0]:				 1024
>     Max work items[1]:				 1024
>     Max work items[2]:				 1024
>   Max work group size:				 256
>   Preferred vector width char:			 4
>   Preferred vector width short:			 2
>   Preferred vector width int:			 1
>   Preferred vector width long:			 1
>   Preferred vector width float:			 1
>   Preferred vector width double:		 1
>   Native vector width char:			 4
>   Native vector width short:			 2
>   Native vector width int:			 1
>   Native vector width long:			 1
>   Native vector width float:			 1
>   Native vector width double:			 1
>   Max clock frequency:				 1411Mhz
>   Address bits:					 64
>   Max memory allocation:			 3422266572
>   Image support:				 Yes
>   Max number of images read arguments:		 128
>   Max number of images write arguments:		 8
>   Max image 2D width:				 16384
>   Max image 2D height:				 16384
>   Max image 3D width:				 2048
>   Max image 3D height:				 2048
>   Max image 3D depth:				 2048
>   Max samplers within kernel:			 16
>   Max size of kernel argument:			 1024
>   Alignment (bits) of base address:		 2048
>   Minimum alignment (bytes) for any datatype:	 128
>   Single precision floating point capability
>     Denorms:					 No
>     Quiet NaNs:					 Yes
>     Round to nearest even:			 Yes
>     Round to zero:				 Yes
>     Round to +ve and infinity:			 Yes
>     IEEE754-2008 fused multiply-add:		 Yes
>   Cache type:					 Read/Write
>   Cache line size:				 64
>   Cache size:					 16384
>   Global memory size:				 4289183744
>   Constant buffer size:				 3422266572
>   Max number of constant args:			 8
>   Local memory type:				 Scratchpad
>   Local memory size:				 32768
>   Max pipe arguments:				 0
>   Max pipe active reservations:			 0
>   Max pipe packet size:				 0
>   Max global variable size:			 0
>   Max global variable preferred total size:	 0
>   Max read/write image args:			 0
>   Max on device events:				 0
>   Queue on device max size:			 0
>   Max on device queues:				 0
>   Queue on device preferred size:		 0
>   SVM capabilities:
>     Coarse grain buffer:			 No
>     Fine grain buffer:				 No
>     Fine grain system:				 No
>     Atomics:					 No
>   Preferred platform atomic alignment:		 0
>   Preferred global atomic alignment:		 0
>   Preferred local atomic alignment:		 0
>   Kernel Preferred work group size multiple:	 64
>   Error correction support:			 0
>   Unified memory for Host and Device:		 0
>   Profiling timer resolution:			 1
>   Device endianess:				 Little
>   Available:					 Yes
>   Compiler available:				 Yes
>   Execution capabilities:
>     Execute OpenCL kernels:			 Yes
>     Execute native function:			 No
>   Queue on Host properties:
>     Out-of-Order:				 No
>     Profiling :					 Yes
>   Queue on Device properties:
>     Out-of-Order:				 No
>     Profiling :					 No
>   Platform ID:					 0x7f7e7a861e50
>   Name:						 Ellesmere
>   Vendor:					 Advanced Micro Devices, Inc.
>   Device OpenCL C version:			 OpenCL C 1.2
>   Driver version:				 3143.9
>   Profile:					 FULL_PROFILE
>   Version:					 OpenCL 1.2 AMD-APP (3143.9)
>   Extensions:					 cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event
> 
> 
>   Device Type:					 CL_DEVICE_TYPE_GPU
>   Vendor ID:					 1002h
>   Board name:					 Radeon RX 580 Series
>   Device Topology:				 PCI[ B#4, D#0, F#0 ]
>   Max compute units:				 36
>   Max work items dimensions:			 3
>     Max work items[0]:				 1024
>     Max work items[1]:				 1024
>     Max work items[2]:				 1024
>   Max work group size:				 256
>   Preferred vector width char:			 4
>   Preferred vector width short:			 2
>   Preferred vector width int:			 1
>   Preferred vector width long:			 1
>   Preferred vector width float:			 1
>   Preferred vector width double:		 1
>   Native vector width char:			 4
>   Native vector width short:			 2
>   Native vector width int:			 1
>   Native vector width long:			 1
>   Native vector width float:			 1
>   Native vector width double:			 1
>   Max clock frequency:				 1411Mhz
>   Address bits:					 64
>   Max memory allocation:			 3422155161
>   Image support:				 Yes
>   Max number of images read arguments:		 128
>   Max number of images write arguments:		 8
>   Max image 2D width:				 16384
>   Max image 2D height:				 16384
>   Max image 3D width:				 2048
>   Max image 3D height:				 2048
>   Max image 3D depth:				 2048
>   Max samplers within kernel:			 16
>   Max size of kernel argument:			 1024
>   Alignment (bits) of base address:		 2048
>   Minimum alignment (bytes) for any datatype:	 128
>   Single precision floating point capability
>     Denorms:					 No
>     Quiet NaNs:					 Yes
>     Round to nearest even:			 Yes
>     Round to zero:				 Yes
>     Round to +ve and infinity:			 Yes
>     IEEE754-2008 fused multiply-add:		 Yes
>   Cache type:					 Read/Write
>   Cache line size:				 64
>   Cache size:					 16384
>   Global memory size:				 4289060864
>   Constant buffer size:				 3422155161
>   Max number of constant args:			 8
>   Local memory type:				 Scratchpad
>   Local memory size:				 32768
>   Max pipe arguments:				 0
>   Max pipe active reservations:			 0
>   Max pipe packet size:				 0
>   Max global variable size:			 0
>   Max global variable preferred total size:	 0
>   Max read/write image args:			 0
>   Max on device events:				 0
>   Queue on device max size:			 0
>   Max on device queues:				 0
>   Queue on device preferred size:		 0
>   SVM capabilities:
>     Coarse grain buffer:			 No
>     Fine grain buffer:				 No
>     Fine grain system:				 No
>     Atomics:					 No
>   Preferred platform atomic alignment:		 0
>   Preferred global atomic alignment:		 0
>   Preferred local atomic alignment:		 0
>   Kernel Preferred work group size multiple:	 64
>   Error correction support:			 0
>   Unified memory for Host and Device:		 0
>   Profiling timer resolution:			 1
>   Device endianess:				 Little
>   Available:					 Yes
>   Compiler available:				 Yes
>   Execution capabilities:
>     Execute OpenCL kernels:			 Yes
>     Execute native function:			 No
>   Queue on Host properties:
>     Out-of-Order:				 No
>     Profiling :					 Yes
>   Queue on Device properties:
>     Out-of-Order:				 No
>     Profiling :					 No
>   Platform ID:					 0x7f7e7a861e50
>   Name:						 Ellesmere
>   Vendor:					 Advanced Micro Devices, Inc.
>   Device OpenCL C version:			 OpenCL C 1.2
>   Driver version:				 3143.9
>   Profile:					 FULL_PROFILE
>   Version:					 OpenCL 1.2 AMD-APP (3143.9)
>   Extensions:					 cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event
> 
> 
>   Device Type:					 CL_DEVICE_TYPE_GPU
>   Vendor ID:					 1002h
>   Board name:					 Radeon RX 580 Series
>   Device Topology:				 PCI[ B#5, D#0, F#0 ]
>   Max compute units:				 36
>   Max work items dimensions:			 3
>     Max work items[0]:				 1024
>     Max work items[1]:				 1024
>     Max work items[2]:				 1024
>   Max work group size:				 256
>   Preferred vector width char:			 4
>   Preferred vector width short:			 2
>   Preferred vector width int:			 1
>   Preferred vector width long:			 1
>   Preferred vector width float:			 1
>   Preferred vector width double:		 1
>   Native vector width char:			 4
>   Native vector width short:			 2
>   Native vector width int:			 1
>   Native vector width long:			 1
>   Native vector width float:			 1
>   Native vector width double:			 1
>   Max clock frequency:				 1411Mhz
>   Address bits:					 64
>   Max memory allocation:			 3422155161
>   Image support:				 Yes
>   Max number of images read arguments:		 128
>   Max number of images write arguments:		 8
>   Max image 2D width:				 16384
>   Max image 2D height:				 16384
>   Max image 3D width:				 2048
>   Max image 3D height:				 2048
>   Max image 3D depth:				 2048
>   Max samplers within kernel:			 16
>   Max size of kernel argument:			 1024
>   Alignment (bits) of base address:		 2048
>   Minimum alignment (bytes) for any datatype:	 128
>   Single precision floating point capability
>     Denorms:					 No
>     Quiet NaNs:					 Yes
>     Round to nearest even:			 Yes
>     Round to zero:				 Yes
>     Round to +ve and infinity:			 Yes
>     IEEE754-2008 fused multiply-add:		 Yes
>   Cache type:					 Read/Write
>   Cache line size:				 64
>   Cache size:					 16384
>   Global memory size:				 4289060864
>   Constant buffer size:				 3422155161
>   Max number of constant args:			 8
>   Local memory type:				 Scratchpad
>   Local memory size:				 32768
>   Max pipe arguments:				 0
>   Max pipe active reservations:			 0
>   Max pipe packet size:				 0
>   Max global variable size:			 0
>   Max global variable preferred total size:	 0
>   Max read/write image args:			 0
>   Max on device events:				 0
>   Queue on device max size:			 0
>   Max on device queues:				 0
>   Queue on device preferred size:		 0
>   SVM capabilities:
>     Coarse grain buffer:			 No
>     Fine grain buffer:				 No
>     Fine grain system:				 No
>     Atomics:					 No
>   Preferred platform atomic alignment:		 0
>   Preferred global atomic alignment:		 0
>   Preferred local atomic alignment:		 0
>   Kernel Preferred work group size multiple:	 64
>   Error correction support:			 0
>   Unified memory for Host and Device:		 0
>   Profiling timer resolution:			 1
>   Device endianess:				 Little
>   Available:					 Yes
>   Compiler available:				 Yes
>   Execution capabilities:
>     Execute OpenCL kernels:			 Yes
>     Execute native function:			 No
>   Queue on Host properties:
>     Out-of-Order:				 No
>     Profiling :					 Yes
>   Queue on Device properties:
>     Out-of-Order:				 No
>     Profiling :					 No
>   Platform ID:					 0x7f7e7a861e50
>   Name:						 Ellesmere
>   Vendor:					 Advanced Micro Devices, Inc.
>   Device OpenCL C version:			 OpenCL C 1.2
>   Driver version:				 3143.9
>   Profile:					 FULL_PROFILE
>   Version:					 OpenCL 1.2 AMD-APP (3143.9)
>   Extensions:					 cl_khr_fp64 cl_amd_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_vec3 cl_amd_printf cl_amd_media_ops cl_amd_media_ops2 cl_amd_popcnt cl_khr_image2d_from_buffer cl_khr_spir cl_khr_gl_event
> ```
> 
> **Additional context**
> Video BIOS are original ones.

How can I use index, wsize, intensity  in comment line ?..

# Action History
- Created by: fmasclef | 2020-09-25T09:15:45+00:00
- Closed at: 2020-09-25T16:09:21+00:00
