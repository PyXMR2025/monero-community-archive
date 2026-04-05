---
title: n/a rates and connect error armv8
source_url: https://github.com/xmrig/xmrig/issues/1811
author: seisdr
assignees: []
labels:
- question
created_at: '2020-08-13T22:20:44+00:00'
updated_at: '2020-08-14T13:22:35+00:00'
type: issue
status: closed
closed_at: '2020-08-14T13:22:35+00:00'
---

# Original Description
I been using old pre built xmrig it wasn't working  I just build the latest and I faced the same error the rates shows on n/a and nothing work 
```
u0_a96@localhost:~/xmrig/build$ ./xmrig --tls -o zergpool.com -u  -p 
 * ABOUT        XMRig/6.3.1 clang/9.0.0
 * LIBS         libuv/1.33.1 OpenSSL/1.1.1d
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARMv8 (1) x64 AES
                threads:8
 * MEMORY       1.5/1.8 GB (83%)
 * DONATE       1%
 * POOL #1      zergpool.com algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-08-14 01:13:19.615]  net      zergpool.com connect error: "operation canceled"
[2020-08-14 01:13:20.006]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2020-08-14 01:13:22.114]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
```

# Discussion History
## seisdr | 2020-08-13T22:22:50+00:00
```
[2020-08-14 01:22:19.243] no any results yet
[2020-08-14 01:22:22.087] no active connection
[2020-08-14 01:22:24.429]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2020-08-14 01:22:32.796]  net      zergpool.com connect error: "operation canceled"
```

## seisdr | 2020-08-13T22:29:34+00:00
I compile it without hwloc

## seisdr | 2020-08-13T22:31:10+00:00
the old version also was without hwloc support

## xmrig | 2020-08-13T23:09:39+00:00
Zero hashrate because there is no connection to the pool, you must use `MINER COMMAND LINE GENERATOR` on that pool to set up the region and port.
If you plan to mine RandomX your device has not enough memory for it in fast mode.
Thank you.


## seisdr | 2020-08-13T23:39:34+00:00
what about this
```
23
 * ABOUT        XMRig/6.3.1 clang/9.0.0
 * LIBS         libuv/1.33.1 OpenSSL/1.1.1d
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARMv8 (1) x64 AES
                threads:8
 * MEMORY       1.4/1.8 GB (77%)
 * DONATE       1%
 * POOL #1      stratum+tcp://scrypt.eu.nicehash.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-08-14 02:35:48.317]  net      stratum+tcp://scrypt.eu.nicehash.com:3333 read error: "end of file"
[2020-08-14 02:35:54.354]  net      stratum+tcp://scrypt.eu.nicehash.com:3333 read error: "end of file"
[2020-08-14 02:36:00.341]  net      stratum+tcp://scrypt.eu.nicehash.com:3333 read error: "end of file"
[2020-08-14 02:36:06.355]  net      stratum+tcp://scrypt.eu.nicehash.com:3333 read error: "end of file"
[2020-08-14 02:36:12.368]  net      stratum+tcp://scrypt.eu.nicehash.com:3333 read error: "end of file"
```

## SChernykh | 2020-08-14T07:23:50+00:00
> what about this

This is `scrypt` Nicehash server, XMRig doesn't support this algorithm. What coin are you trying to mine?

## seisdr | 2020-08-14T13:22:35+00:00
I don't know , it working now thank you

# Action History
- Created by: seisdr | 2020-08-13T22:20:44+00:00
- Closed at: 2020-08-14T13:22:35+00:00
