---
title: 'xmrig cannot connect to TCP port 3333 at MiningRigRentals (MRR) '
source_url: https://github.com/xmrig/xmrig/issues/2846
author: PSLLSP
assignees: []
labels:
- bug
created_at: '2021-12-30T08:54:24+00:00'
updated_at: '2025-06-16T20:26:15+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:26:15+00:00'
---

# Original Description
xmrig-6.16.2-linux-static-x64.tar.gz

It looks like `xmrig` doesn't support [client.reconnect](https://en.bitcoin.it/wiki/Stratum_mining_protocol#client.reconnect).

This config doesn't work, the issue:
```
$ cat test1-rtm-mrr.sh
#!/bin/sh
  
POOL="eu-de01.miningrigrentals.com:3333"

USER="droidMiner.217649"
PASS="TEST1"
#OPTS="-t 2"

./xmrig -a gr -o "$POOL" -u "$USER" -p "$PASS" $OPTS "$@"
```
```
$ sh test1-rtm-mrr.sh -t1
 * ABOUT        XMRig/6.16.2 gcc/9.3.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E31260L @ 2.40GHz (1) 64-bit AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       30.7/31.2 GB (98%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      eu-de01.miningrigrentals.com:3333 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-12-30 09:44:15.321]  net      use pool eu-de01.miningrigrentals.com:3333  188.166.161.62
[2021-12-30 09:44:15.327]  net      eu-de01.miningrigrentals.com:3333 read error: "end of file"
[2021-12-30 09:44:15.328]  net      no active pools, stop mining
[2021-12-30 09:44:21.286]  net      use pool eu-de01.miningrigrentals.com:3333  188.166.161.62
[2021-12-30 09:44:21.291]  net      eu-de01.miningrigrentals.com:3333 read error: "end of file"
[2021-12-30 09:44:21.291]  net      no active pools, stop mining
```

---

Workarround, connect to custom TCP port (this port is dynamic):
```
$ cat test2-rtm-mrr.sh
#!/bin/sh
  
#POOL="eu-de01.miningrigrentals.com:3333"
POOL="eu-de01.miningrigrentals.com:50821"

USER="droidMiner.217649"
PASS="TEST2"
#OPTS="-t 2"

./xmrig -a gr -o "$POOL" -u "$USER" -p "$PASS" $OPTS "$@"
```
---

`cpuminer-gr-1.2.4.1-x86_64_linux.tar.gz`, [cpuminer](https://github.com/WyvernTKC/cpuminer-gr-avx2/releases) that can connect to TCP port 3333, for a reference.

```
$ cat test3-rtm-mrr.sh 
#!/bin/sh

POOL="eu-de01.miningrigrentals.com:3333"
USER="droidMiner.217649"
PASS="TEST3"

OPTS=""

binaries/cpuminer-sse2 -a gr -o "$POOL" -u "$USER" -p "$PASS" $OPTS "$@"
```
```
$ sh test3-rtm-mrr.sh -t 1

         **********  cpuminer-opt-gr 1.2.4.1  *********** 
     A CPU miner with multi algo support and optimized for CPUs
     with AVX512, SHA and VAES extensions by JayDDee.
     with Ghostrider Algo by Ausminer & Delgon.
     Jay D Dee's BTC donation address: 12tdvfF7KmAsihBXQXynT6E6th2c2pByTT

     RTM 1.75% Fee

Prepared for Linux
CPU:          Intel(R) Xeon(R) CPU E31260L @ 2.40GHz
SW built on Nov 10 2021 with GCC 10.3.0
CPU features:  AVX     AES
SW features:   SSE2  
Algo features: AVX2   VAES
[2021-12-30 10:09:40] Software does NOT match CPU features!
[2021-12-30 10:09:40] Please check if proper binaries are being used.


[2021-12-30 10:09:40] Tune config 'tune_config' loaded succesfully
[2021-12-30 10:09:40] Huge Pages set up successfully.
[2021-12-30 10:09:40] Stratum connect stratum+tcp://eu-de01.miningrigrentals.com:3333
[2021-12-30 10:09:40] 1 of 8 miner threads started using 'gr' algorithm
[2021-12-30 10:09:41] Server requested reconnection to stratum+tcp://eu-de01.miningrigrentals.com:50821
[2021-12-30 10:09:41] Stratum connection established
[2021-12-30 10:09:42] Stratum connection established
[2021-12-30 10:09:42] CPU temp: curr 68 C max 0, Freq: 2.395/2.395 GHz
[2021-12-30 10:09:42] New Stratum Diff 0.190052, Block 216635, Job 000013ac-0
[2021-12-30 10:09:42] Block Algos: Turtlelite Fast Dark (Rot. 7.2, Speed: ~1.40x)
                      Diff: Net 7.3489, Stratum 0.19005, Target 2.9e-06
```

# Discussion History
## Spudz76 | 2021-12-30T12:44:59+00:00
Pull request above solves the issue, you can apply the diffs and build yourself, or await inclusion into dev (and later, master and releases)

# Action History
- Created by: PSLLSP | 2021-12-30T08:54:24+00:00
- Closed at: 2025-06-16T20:26:15+00:00
