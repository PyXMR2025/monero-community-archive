---
title: 'just mining on 50% (4 of 8) cores on Intel Atom C2750? '
source_url: https://github.com/xmrig/xmrig/issues/1736
author: divinity76
assignees: []
labels: []
created_at: '2020-06-16T07:56:56+00:00'
updated_at: '2020-08-19T01:12:16+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:12:16+00:00'
---

# Original Description
have a Intel Atom C2750, it has 8 cores and 8 threads (no hyperhtreading) and 4MB ~~L3~~ L2 cpu cache, and xmrig just mines on 4 of the cores, 

notable about C2750 is that it has 8 cores, but only 4MB L2-cache, is that the problem? not enough cpu cache to run more than 4 mining threads? 

here's xmrig's output:
```
 * ABOUT        XMRig/5.11.3 gcc/5.4.0
 * LIBS         libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
 * CPU          Intel(R) Atom(TM) CPU C2750 @ 2.40GHz (1) x64 AES
                L2:4.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       3.2/15.6 GB (21%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      monero.herominers.com:10191 algo rx/0
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
[2020-06-16 09:27:22.691]  net  use pool monero.herominers.com:10191  138.201.217.40
[2020-06-16 09:27:22.691]  net  new job from monero.herominers.com:10191 diff 50000 algo rx/0 height 2121722
[2020-06-16 09:27:22.691]  cpu  use argon2 implementation SSSE3
[2020-06-16 09:27:22.695]  msr  msr kernel module is not available
[2020-06-16 09:27:22.695]  rx   init dataset algo rx/0 (8 threads) seed b0920b700fc794ff...
[2020-06-16 09:27:23.345]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (650 ms)
[2020-06-16 09:27:33.633]  rx   dataset ready (10288 ms)
[2020-06-16 09:27:33.633]  cpu  use profile  rx  (4 threads) scratchpad 2048 KB
[2020-06-16 09:27:33.696]  cpu  READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (62 ms)
(...stuff...)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |    90.5 |    90.5 |    90.5 |
|        1 |        2 |    90.6 |    90.5 |    90.5 |
|        2 |        4 |    90.3 |    90.5 |    90.5 |
|        3 |        6 |    90.4 |    90.3 |    90.4 |
|        - |        - |   361.9 |   361.8 |   361.9 |
[2020-06-16 09:43:07.169] speed 10s/60s/15m 361.9 361.8 361.9 H/s max 362.9 H/s
```

here is my base configuration:
```json
{
    "log-file": "mining.log",
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
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "x-priority-comment":"set process priority (null default,0 idle, 2 normal to 5 highest, ps if you use 5 you should also disable yield!)",
        "priority": 0,
        "memory-pool": false,
                "X-yield-comment":"if max priority, set yield to false...",
        "yield": false,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "rx/0",
            "coin": null,
            "url": "monero.herominers.com:10191",
            "user": "45iMsbuzbvwCimzEKcws7LPTUFEwna4hmYkiMYxAB13gJMvYWa5UR2Ch2vvs5etkcoLZWeUgLfFUNNKwMhVG72uC8u6zG8v",
            "pass": "honningas_idle_intel_atom_C2750",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
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
    "verbose": 0,
    "watch": true
}
```

and here is what xmrig turns it into
```json
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
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": 0,
        "memory-pool": false,
        "yield": false,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
        ],
        "cn-heavy": [
            [1, -1],
            [1, -1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "rx": [0, 2, 4, 6],
        "rx/arq": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 2, 4, 6],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": "mining.log",
    "pools": [
        {
            "algo": "rx/0",
            "coin": null,
            "url": "monero.herominers.com:10191",
            "user": "45iMsbuzbvwCimzEKcws7LPTUFEwna4hmYkiMYxAB13gJMvYWa5UR2Ch2vvs5etkcoLZWeUgLfFUNNKwMhVG72uC8u6zG8v",
            "pass": "honningas_idle_intel_atom_C2750",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
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
    "verbose": 0,
    "watch": true
}
```

# Discussion History
## ghost | 2020-06-16T12:55:04+00:00
Your CPU Has 8 cores and threads, but it's have only 4 MB of Cache. U'll get the best hashrate using the 2 cores, due to 2 MB cache is used on one core in Xmrig. If you use more cores, the hashrate will be lower, the cache will then be inefficiently distributed among the cores. 

## divinity76 | 2020-06-16T14:04:32+00:00
@Red26e7t doesn't look like it, here's my hashrate with 4 mining threads:

```
[2020-06-16 15:57:40.726] speed 10s/60s/15m 361.7 361.6 361.9 H/s max 363.2 H/s
[2020-06-16 15:57:46.069]  net  new job from monero.herominers.com:10191 diff 15000 algo rx/0 height 2121932
[2020-06-16 15:58:10.755]  cpu  accepted (579/0) diff 15000 (35 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |    90.0 |    90.2 |    90.4 |
|        1 |        2 |    90.4 |    90.3 |    90.5 |
|        2 |        4 |    90.5 |    90.4 |    90.5 |
|        3 |        6 |    90.3 |    90.5 |    90.6 |
|        - |        - |   361.2 |   361.5 |   361.9 |
[2020-06-16 15:58:11.771] speed 10s/60s/15m 361.2 361.5 361.9 H/s max 363.2 H/s
```

and here's the rate with 2 threads:
```
[2020-06-16 16:02:40.957] speed 10s/60s/15m 183.4 183.7 n/a H/s max 184.2 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |    92.0 |    91.9 |     n/a |
|        1 |        2 |    91.8 |    91.8 |     n/a |
|        - |        - |   183.8 |   183.7 |     n/a |
```

(in both cases hugepages was allocated 100% and 1gb pages was disabled)

## divinity76 | 2020-06-16T14:09:17+00:00
@Red26e7t even more interestingly, when i manually configured it to run 8 threads, here's what i get:

```
[2020-06-16 16:08:29.766] speed 10s/60s/15m 595.5 595.8 n/a H/s max 596.8 H/s
[2020-06-16 16:08:34.219]  net  new job from monero.herominers.com:10191 diff 19397 algo rx/0 height 2121943
[2020-06-16 16:08:55.188]  cpu  accepted (3/0) diff 19397 (33 ms)
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |    73.4 |    73.5 |     n/a |
|        1 |        2 |    78.0 |    77.8 |     n/a |
|        2 |        1 |    73.5 |    73.5 |     n/a |
|        3 |        3 |    73.3 |    73.3 |     n/a |
|        4 |        4 |    73.4 |    73.5 |     n/a |
|        5 |        5 |    73.4 |    73.5 |     n/a |
|        6 |        6 |    77.7 |    77.7 |     n/a |
|        7 |        7 |    72.7 |    72.6 |     n/a |
|        - |        - |   595.5 |   595.4 |     n/a |
[2020-06-16 16:09:04.180] speed 10s/60s/15m 595.5 595.4 n/a H/s max 596.8 H/s
```

i wonder if it has something to do with: this *WEIRD* cpu does not have a l3 cache at all, only has l1/l2 cache (that's highly unusual for Intel CPUs afaik)

maybe related?

## ghost | 2020-06-16T14:26:01+00:00
In the case of the computer I use, it looks like this:
CPU: i5 6200u - 2 cores, 4 threads, L2 cache: 512KB, L3 cache: 3 MB, 2,3 gHz base, 2,8 gHz turbo, 
Huge Pages Enabled, Windows 10 Home.
Results:
1 core: ~ 600 H / s
2 cores: ~ 650 H / S,
2 cores, use of 4 threads: ~ 300 H / s.
I meet with your situation for the first time.

## divinity76 | 2020-06-16T14:27:44+00:00
@Red26e7t yeah, hyperthreading is useless for mining, if you try to mine on the real core and the hyperthreaded core simultaneously, you will actually mine slower than mining only on the non-hyperthreaded-cores ^^  (xmrig attempts to avoid mining on the HT-cores as well)

i'm surprised going from 1 core to 2 cores only gave +50 though, guess that's the L3 cache size?

## Lonnegan | 2020-07-13T14:42:31+00:00
The Intel Atom C2750 doesn't have 4 MB L2 cache; it has 4x 1 MB L2 cache, each private for 2 cores. That's a big diffence, because that means, the L2 cache is too small for even a single RX thread. And that means, that the CPU has to access RAM under any circumstances. And that's the reason, why 8 threads are faster than 4 or 2. If the CPU needs to access the slow RAM anyway, it can do so with all cores instead of just 2 or 4.

You should consider to mine a coin, that has a scratchpad size of just 1 MB instead of 2 MB as RandomX has. Then start 4 threads and the mining data will fit into the L2 cache. 👍 I'm not 100 percent sure, but I think Wownero uses a RX variant with 1 MB scratchpad.

# Action History
- Created by: divinity76 | 2020-06-16T07:56:56+00:00
- Closed at: 2020-08-19T01:12:16+00:00
