---
title: '[Ubuntu] running `xmrig -B` doesnt seem to do anything'
source_url: https://github.com/xmrig/xmrig/issues/2485
author: 0xf0xx0
assignees: []
labels: []
created_at: '2021-07-16T10:28:29+00:00'
updated_at: '2021-09-28T02:22:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
`xmrig -B` doesn't seem to do anything.

**To Reproduce**
1. Compile xmrig.
2. run `./xmrig -B`.

**Expected behavior**
The process will move itself to the background and i can continue using my shell.

**Required data**
 - Miner log as text or screenshot
 ```
 * ABOUT        XMRig/6.13.1 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU @ 2.30GHz (1) 64-bit AES VM
                L2:0.2 MB L3:45.0 MB 1C/2T NUMA:1
 * MEMORY       0.6/1.9 GB (33%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      monerohash.com:9999 algo rx/wow
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-07-16 10:22:02.323]  net      use pool monerohash.com:9999 TLSv1.2 107.191.99.221
[2021-07-16 10:22:02.323]  net      fingerprint (SHA-256): "d4717e48f34da3ac0e16733405a4ee02f243b92afe673b02bf2cfacf6d7cc535"
[2021-07-16 10:22:02.323]  net      new job from monerohash.com:9999 diff 150000 algo rx/0 height 2405967
[2021-07-16 10:22:02.323]  cpu      use argon2 implementation AVX2
[2021-07-16 10:22:02.326]  msr      cannot read MSR 0x000001a4
[2021-07-16 10:22:02.326]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-07-16 10:22:02.326]  randomx  init dataset algo rx/0 (2 threads) seed 331da8a7a190a2cf...
[2021-07-16 10:22:02.327]  randomx  not enough memory for RandomX dataset
[2021-07-16 10:22:02.327]  randomx  failed to allocate RandomX dataset, switching to slow mode (0 ms)
[2021-07-16 10:22:03.030]  randomx  dataset ready (703 ms)
[2021-07-16 10:22:03.030]  cpu      use profile  rx  (1 thread) scratchpad 2048 KB
[2021-07-16 10:22:03.031]  cpu      READY threads 1/1 (1) huge pages 0% 0/1 memory 2048 KB (2 ms)
```
 - `./xmrig -o monerohash.com:9999  -k --tls`
 - OS: Ubuntu 20.04

**Additional context**
Just trying to utilize a server i rent.


# Discussion History
## xq0404 | 2021-07-18T00:26:54+00:00
You need to mine under "su root"

## PaulinaParangerHr | 2021-07-18T03:48:35+00:00
Ooh

## gMan1990 | 2021-09-26T07:01:18+00:00
@xq0404 if running as background mode, and do not config `log-file`, does it has a default log file?

## Spudz76 | 2021-09-26T14:47:42+00:00
Command line arguments do not override `background: false` in config.json

Like they would on a normal app.  Can't be changed now since apparently too many people know it works wrong and are expecting it to work how it already works, not how every other commandline app in history works.

Set `background: true` or do not use any config.json and only use command line options

## xq0404 | 2021-09-27T01:19:01+00:00
Also miner ID never works via config.json

## Spudz76 | 2021-09-27T13:06:12+00:00
rig-id is only supported by "some" pools.  Many still only accept a rig-id through password format.

## xq0404 | 2021-09-28T02:22:04+00:00
> rig-id is only supported by "some" pools. Many still only accept a rig-id through password format.

No wonder Nanopool does not seem to accept rig-id.

# Action History
- Created by: 0xf0xx0 | 2021-07-16T10:28:29+00:00
