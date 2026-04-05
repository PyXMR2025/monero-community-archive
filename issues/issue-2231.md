---
title: Minergate Support
source_url: https://github.com/xmrig/xmrig/issues/2231
author: andress134
assignees: []
labels: []
created_at: '2021-04-03T04:16:56+00:00'
updated_at: '2021-04-04T07:31:34+00:00'
type: issue
status: closed
closed_at: '2021-04-04T07:31:34+00:00'
---

# Original Description
**Describe the bug**
I dont know what happen but, it stopped working for minergate, im testing on linux, ubuntu/debian and nothing, is not starting mining

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**

 * ABOUT        XMRig/6.10.0 gcc/9.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU E3-1230 v6 @ 3.50GHz (1) 64-bit AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       12.7/15.6 GB (81%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.pool.minergate.com:45700 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-04-03 06:15:18.824] no active connection

here is my command ./xmrig --opencl -o xmr.pool.minergate.com:45700 -u user --tls -k --coin monero -a argon2/chukwa

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2021-04-03T07:23:16+00:00
Coin Monero with Algo argon2/chukwa is a mismatch?  Specify one or the other instead of both, or use `--coin monero --algo rx/0` so they match correctly.

## andress134 | 2021-04-03T20:33:19+00:00
> Coin Monero with Algo argon2/chukwa is a mismatch? Specify one or the other instead of both, or use `--coin monero --algo rx/0` so they match correctly.

I tried also ./xmrig -o stratum+tcp://xmr.pool.minergate.com:45700 -u user -p x --donate-level 1 --max-cpu-usage 75

## andress134 | 2021-04-04T00:38:09+00:00
so i think some wrong on this xmrig version, im using same servers, same command that have used with other version and it has working fine, but now, i run it and keep blocked

./xmrig-o stratum+tcp://xmr.pool.minergate.com:45700 -u user -p x --donate-level 1 --max-cpu-usage 75
 * ABOUT        XMRig/6.10.0 gcc/5.4.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz (1) 64-bit AES VM
                L2:4.0 MB L3:27.5 MB 1C/1T NUMA:1
 * MEMORY       1.7/1.8 GB (95%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum+tcp://xmr.pool.minergate.com:45700 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled


## Spudz76 | 2021-04-04T01:13:19+00:00
All your memory is gone somehow, which could be why that last run didn't work.  1.8GB total while RandomX needs a free minimum of 2.3GB.

Also gcc5 is really antique and likely has been untested for a while, should be gcc7 or newer.

## andress134 | 2021-04-04T07:20:24+00:00
> All your memory is gone somehow, which could be why that last run didn't work. 1.8GB total while RandomX needs a free minimum of 2.3GB.
> 
> Also gcc5 is really antique and likely has been untested for a while, should be gcc7 or newer.

I am 100% convinced that the problem is from xmrig, not the servers
I used the same servers until xmrig version 6.8 and it worked perfectly, since the launch of 6.9 I started to lose the hash, and now 6.10 doesn't work at all.
I tried another test, on a much larger server and it doesn't work

```js
./xmrig -o stratum+tcp://xmr.pool.minergate.com:45700 -u user -p x --donate-level 1 --max-cpu-usage 75
 * ABOUT        XMRig/6.10.0 gcc/5.4.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7281 16-Core Processor (3) 64-bit AES VM
                L2:0.0 MB L3:0.0 MB 3C/3T NUMA:1
 * MEMORY       1.2/3.8 GB (32%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      stratum+tcp://xmr.pool.minergate.com:45700 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
```

Still not working, i can't mining on minergate, using same servers that have used for mining long time  utill version 6.8xmrig

## SChernykh | 2021-04-04T07:23:54+00:00
Don't mine on minergate. It's a scam pool that steals 30% of your hashrate. That said, it is a pool problem, not xmrig problem. Try another pool.

## andress134 | 2021-04-04T07:25:12+00:00
> Don't mine on minergate. It's a scam pool that steals 30% of your hashrate. That said, it is a pool problem, not xmrig problem. Try another pool.

could you recommend a better alternative than minergate?

## SChernykh | 2021-04-04T07:30:52+00:00
List of pools: https://miningpoolstats.stream/monero
Try a pool not in top 3. Hashvault and MoneroOcean are good pools.

## andress134 | 2021-04-04T07:31:23+00:00
> List of pools: https://miningpoolstats.stream/monero
> Try a pool not in top 3. Hashvault and MoneroOcean are good pools.

Okay, thank you

# Action History
- Created by: andress134 | 2021-04-03T04:16:56+00:00
- Closed at: 2021-04-04T07:31:34+00:00
