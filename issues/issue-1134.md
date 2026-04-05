---
title: 'only using physical cpu #1 on dual-cpu system'
source_url: https://github.com/xmrig/xmrig/issues/1134
author: divinity76
assignees: []
labels:
- question
created_at: '2019-08-22T19:59:03+00:00'
updated_at: '2019-08-23T00:14:57+00:00'
type: issue
status: closed
closed_at: '2019-08-23T00:14:57+00:00'
---

# Original Description
i got a system with 2x Xeon L5520 and hyperthreading enabled. usually i would set the following thread configuration for that:

```json
"threads": [
        {
            "low_power_mode": false,
            "affine_to_cpu": 0,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 2,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 4,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 6,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 8,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 10,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 12,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 14,
            "asm": true
        }
    ]
```

.. but as of... idk, a month ago, maybe? xmrig seems to be ignoring and removing the "thread" section of config.json, and it only uses the first physical CPU core. why is xmrig ignoring the thread section, and why is it only using the first cpu, seemingly ignoring the second physical cpu? 

![image](https://user-images.githubusercontent.com/1874996/63545677-4811ca80-c528-11e9-9ada-f8112026ef8c.png)

here is the original config.json:

```json
{
    "algo": "cryptonight",
    "api": {
        "port": 42548,
        "access-token": null,
        "id": null,
        "worker-id": "<CHANGE_ME_WORKER_NAME>",
        "ipv6": false,
        "restricted": true
    },
    "asm": true,
    "autosave": true,
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": 0,
    "donate-level": 1,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": "mining.log",
    "max-cpu-usage": 100,
    "pools": [
        {
            "url": "stratum+tcp://xmr.pool.minergate.com:45700",
            "user": "divinity76+mining@gmail.com",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "variant": -1,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "threads": [
        {
            "low_power_mode": false,
            "affine_to_cpu": 0,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 2,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 4,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 6,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 8,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 10,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 12,
            "asm": true
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": 14,
            "asm": true
        }
    ],
    "user-agent": null,
    "syslog": false,
    "watch": true
}
```

and here is the auto-converted config.json: 

```json
{
    "api": {
        "id": null,
        "worker-id": "<CHANGE_ME_WORKER_NAME>"
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "version": 1,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 8, 2, 10, 4, 12, 6, 14, 1, 9, 3, 11, 5, 13, 7, 15],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 1],
            [1, 3],
            [1, 5],
            [1, 7]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 1],
            [1, 3]
        ],
        "cn-lite": [
            [1, 0],
            [1, 8],
            [1, 2],
            [1, 10],
            [1, 4],
            [1, 12],
            [1, 6],
            [1, 14],
            [1, 1],
            [1, 9],
            [1, 3],
            [1, 11],
            [1, 5],
            [1, 13],
            [1, 7],
            [1, 15]
        ],
        "cn-pico": [
            [2, 0],
            [2, 8],
            [2, 2],
            [2, 10],
            [2, 4],
            [2, 12],
            [2, 6],
            [2, 14],
            [2, 1],
            [2, 9],
            [2, 3],
            [2, 11],
            [2, 5],
            [2, 13],
            [2, 7],
            [2, 15]
        ],
        "cn/gpu": [0, 8, 2, 10, 4, 12, 6, 14, 1, 9, 3, 11, 5, 13, 7, 15],
        "rx": [0, 2, 4, 6, 1, 3, 5, 7],
        "rx/wow": [0, 8, 2, 10, 4, 12, 6, 14, 1, 9, 3, 11, 5, 13, 7, 15],
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": "mining.log",
    "pools": [
        {
            "algo": null,
            "url": "stratum+tcp://xmr.pool.minergate.com:45700",
            "user": "divinity76+mining@gmail.com",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}
```

# Discussion History
## divinity76 | 2019-08-22T20:05:42+00:00
missclick

## xmrig | 2019-08-22T20:12:04+00:00
Can you show `lscpu` output?, but likely current configuration is correct, 0, 2, 4, 6 is first physical CPU, 1, 3, 5, 7 is second.
Thank you.

## divinity76 | 2019-08-22T20:40:35+00:00
lscpu:
```
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              16
On-line CPU(s) list: 0-15
Thread(s) per core:  2
Core(s) per socket:  4
Socket(s):           2
NUMA node(s):        2
Vendor ID:           GenuineIntel
CPU family:          6
Model:               26
Model name:          Intel(R) Xeon(R) CPU           L5520  @ 2.27GHz
Stepping:            5
CPU MHz:             2394.052
CPU max MHz:         2262.0000
CPU min MHz:         1596.0000
BogoMIPS:            4522.09
Virtualization:      VT-x
L1d cache:           32K
L1i cache:           32K
L2 cache:            256K
L3 cache:            8192K
NUMA node0 CPU(s):   0,2,4,6,8,10,12,14
NUMA node1 CPU(s):   1,3,5,7,9,11,13,15
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm dca sse4_1 sse4_2 popcnt lahf_lm ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid dtherm ida flush_l1d
```

if you look at the screenshot above, htop says core # 1,2,3,4,5,6,7,8 is running and 9,10,11,12,13,14,15,16 is idle..

here is a single-cpu system with 4 physical cores + hyperthreading, i expected to see something like this, where core 1,3,5,7 is running instead:
![image](https://user-images.githubusercontent.com/1874996/63547903-6c23da80-c52d-11e9-8330-dfc89d1a23b3.png)



## xmrig | 2019-08-22T21:02:36+00:00
Linux usually don't use odd/even mapping on Intel CPUs, so configuration correct, miner use both CPUs and physical cores, HT cores is idle.

```
NUMA node0 CPU(s):   0,2,4,6,8,10,12,14
NUMA node1 CPU(s):   1,3,5,7,9,11,13,15
```
Miner select 4 first cores from each CPU.

## xmrig | 2019-08-22T21:03:59+00:00
Your initial configuration was use only one CPU.

## divinity76 | 2019-08-23T00:14:57+00:00
oh seems you're right! sorry about the confusion

# Action History
- Created by: divinity76 | 2019-08-22T19:59:03+00:00
- Closed at: 2019-08-23T00:14:57+00:00
