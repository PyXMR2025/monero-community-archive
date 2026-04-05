---
title: Cache QoS issue XMRig v 6.24.0
source_url: https://github.com/xmrig/xmrig/issues/3685
author: Ferrar4ik
assignees: []
labels: []
created_at: '2025-07-12T11:13:10+00:00'
updated_at: '2025-07-12T13:08:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
XMRig use: 2 nodes for 20 threads each. Nodes use RandomX Optimization: Huge Pages, MSR mod, and NUMA is used for full isolation of nodes.
But Cache QoS doesn't work when. 
How to fix the Cache QoS issue?

**Describe the bug**
XMRig Disabled algorithm "rx/0" detected, reconnect
When Cache QoS on. 

Use in CLI ./xmrig -a rx/monero -o [pool.hashvault.pro:443](https://pool.hashvault.pro/) - doesn't fix the problem
Use "threads" { "index": 0, "affinity": 0, "rx": "rx/monero" } in "randomx" - doesn't fix the problem

**To Reproduce**

1. "cpu": {
    "enabled": false
2. "cache_qos": true,
3. I specified "threads" in RandomX "randomx"
4. For Node0 (0-19) "threads": [
      { "index": 0, "affinity": 0 }, ... { "index": 19, "affinity": 19 }
5. "algo": "rx/monero"

For start XMRig command:
numactl --cpunodebind=0 --membind=0 ./xmrig \
  -a rx/monero \
  -c config_node0.json

**Expected behavior**
The XMRig doesn't work with Cache QoS on.
---------------------------------------------------------- 
**Required data**

 - numactl --cpunodebind=0 --membind=0 ./xmrig \
  -a rx/monero \
  -c config_node0.json

 * ABOUT        XMRig/6.24.0 gcc/13.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.51.0 OpenSSL/3.0.16 hwloc/2.12.1
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) CPU E5-2698 v4 @ 2.20GHz (2) 64-bit AES
                L2:10.0 MB L3:100.0 MB 40C/40T NUMA:2
 * MEMORY       248.6/251.8 GB (99%)
                P1-DIMMA1: 32 GB DDR4 @ 2400 MHz 36ASF4G72LZ-2G3B1  
                P1-DIMMB1: 32 GB DDR4 @ 2400 MHz 36ASF4G72LZ-2G3B1  
                P1-DIMMC1: 32 GB DDR4 @ 2400 MHz 36ASF4G72LZ-2G3B1  
                P1-DIMMD1: 32 GB DDR4 @ 2400 MHz 36ASF4G72LZ-2G3B1  
                P2-DIMME1: 32 GB DDR4 @ 2400 MHz 36ASF4G72LZ-2G3B1  
                P2-DIMMF1: 32 GB DDR4 @ 2400 MHz 36ASF4G72LZ-2G3B1  
                P2-DIMMG1: 32 GB DDR4 @ 2400 MHz M386A4K40BB0-CRC   
                P2-DIMMH1: 32 GB DDR4 @ 2400 MHz M386A4K40BB0-CRC   
 * MOTHERBOARD  Supermicro - X10DRL-i
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.hashvault.pro:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2025-07-12 13:23:26.542]  net      pool.hashvault.pro:443 incompatible/disabled algorithm "rx/0" detected, reconnect
[2025-07-12 13:23:26.542]  net      pool.hashvault.pro:443 login error code: 6
---------------------------------------------------------- 
 - OS: Fedora Linux 42 WS Edition

[config_node0.json](https://github.com/user-attachments/files/21195673/config_node0.json)

# Discussion History
## xmrig | 2025-07-12T13:08:02+00:00
This is a badly wrong configuration, no `"threads"` option is supposed to be in `"randomx"`. Even if it is placed in the right place, there is no such syntax for threads. On top of this, you disable the CPU backend, so nothing to mine. Also, `rx/monero` is not a valid alias. Use the default config example as a starting point.
Thank you.

# Action History
- Created by: Ferrar4ik | 2025-07-12T11:13:10+00:00
