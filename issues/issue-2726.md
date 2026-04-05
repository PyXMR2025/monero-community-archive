---
title: Program just hanges
source_url: https://github.com/xmrig/xmrig/issues/2726
author: arthurmelton
assignees: []
labels: []
created_at: '2021-11-27T02:09:16+00:00'
updated_at: '2021-11-27T12:12:05+00:00'
type: issue
status: closed
closed_at: '2021-11-27T12:12:05+00:00'
---

# Original Description
**Describe the bug**
The program just hangs when mining (I can get it to receive new jobs but have never gotten it to send hashes). It runs for about 1-2 mins then just hangs even cpu just goes to 0% by xmrig.

**To Reproduce**
Run the executable

**Expected behavior**
I have it working on a different computer working just fine (at a different location).

**Required data**

<details open>
<summary>Log</summary>
<br>

sometimes it will do this or it has also just printed the new job many times till the diff goes to 100

```
 * ABOUT        XMRig/6.15.3 gcc/5.4.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD EPYC 7282 16-Core Processor (1) 64-bit AES VM
                L2:2.0 MB L3:16.0 MB 4C/4T NUMA:1
 * MEMORY       7.1/7.8 GB (91%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-26 19:55:23.694]  net      use pool gulf.moneroocean.stream:10128  18.210.126.40
[2021-11-26 19:55:23.695]  net      new job from gulf.moneroocean.stream:10128 diff 128001 algo rx/0 height 2502091 (17 tx)
[2021-11-26 19:55:23.695]  cpu      use argon2 implementation AVX2
[2021-11-26 19:55:23.699]  msr      msr kernel module is not available
[2021-11-26 19:55:23.700]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-11-26 19:55:23.700]  randomx  init dataset algo rx/0 (4 threads) seed e3c8069132208c2c...
[2021-11-26 19:55:23.707]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (7 ms)
```

</details>

<details open>
<summary>Config</summary>
<br>

```json
 {
    "api": {
        "id": null,
        "worker-id": "somehost"
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
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3],
        "astrobwt": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/gpu": [0, 1, 2, 3],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "rx": [0, 1, 2, 3],
        "rx/wow": [0, 1, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "gulf.moneroocean.stream:10128",
            "user": "wallet",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
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
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": false,
    "pause-on-battery": false,
    "pause-on-active": false
}
```

</details>

<details open>
<summary>Neofetch</summary>
<br>

```
       _,met$$$$$gg.          container@9d5ab7e0-0ace-4a3a-b6a7-b154fdd930b8 
    ,g$$$$$$$$$$$$$$$P.       ---------------------------------------------- 
  ,g$$P"        """Y$$.".     OS: Debian GNU/Linux 10 (buster) x86_64 
 ,$$P'              `$$$.     Host: KVM/QEMU (Standard PC (i440FX + PIIX, 1996) pc-i440fx-5.0) 
',$$P       ,ggs.     `$$b:   Kernel: 5.4.0-70-generic 
`d$$'     ,$P"'   .    $$$    Uptime: 56 days, 21 hours, 5 mins 
 $$P      d$'     ,    $$P    Packages: 370 (dpkg) 
 $$:      $$.   -    ,d$$'    Shell: sh 
 $$;      Y$b._   _,d$P'      CPU: AMD EPYC 7282 (4) @ 2.800GHz 
 Y$$.    `.`"Y$$$$P"'         Memory: 5677MiB / 7961MiB 
 `$$b      "-.__
  `Y$$                                                
   `Y$$.                                              
     `$$b.
       `Y$$b.
          `"Y$b._
              `"""
```

</details>

**Additional context**
I have also allowed the port 10128 I dont know if that is needed but I thought that might be needed but that did not work. If you need any more info please just ask for it.

# Discussion History
## SChernykh | 2021-11-27T08:00:55+00:00
`* MEMORY       7.1/7.8 GB (91%)`
RandomX needs 2.1+ GB free memory, and you have only 0.7 GB free.

# Action History
- Created by: arthurmelton | 2021-11-27T02:09:16+00:00
- Closed at: 2021-11-27T12:12:05+00:00
