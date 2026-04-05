---
title: MSR at Intel(R) Core(TM) i7-2600K CPU
source_url: https://github.com/xmrig/xmrig/issues/2011
author: DeadManWalkingTO
assignees: []
labels: []
created_at: '2020-12-27T22:11:59+00:00'
updated_at: '2021-01-10T01:05:49+00:00'
type: issue
status: closed
closed_at: '2021-01-10T01:05:49+00:00'
---

# Original Description
**Describe the bug**
XMRig cannot set MSR 0x000001a4 to 0x0000000f
Intel(R) Core(TM) i7-2600K CPU

**To Reproduce**
root@host:~# ./xmrig

**Expected behavior**
[2020-12-27 23:46:42.446]  msr      cannot set MSR 0x000001a4 to 0x0000000f

**Required data**
**root@host:~# ./xmrig**
```
 * ABOUT        xmrig/6.7.0 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-2600K CPU @ 3.40GHz (1) 64-bit AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       3.4/11.6 GB (29%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xxx.xxx.xxx.xxx:xxxx algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-12-27 23:46:42.442]  net      use pool xxx.xxx.xxx.xxx:xxxx TLSv1.3 xxx.xxx.xxx.xxx
[2020-12-27 23:46:42.442]  net      fingerprint (SHA-256): "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
[2020-12-27 23:46:42.442]  net      new job from xxx.xxx.xxx.xxx:xxxx diff 500 algo rx/0 height 2261616
[2020-12-27 23:46:42.442]  cpu      use argon2 implementation SSSE3
[2020-12-27 23:46:42.446]  msr      cannot set MSR 0x000001a4 to 0x0000000f
[2020-12-27 23:46:42.446]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2020-12-27 23:46:42.446]  randomx  init dataset algo rx/0 (8 threads) seed af3e382c9115171a...
[2020-12-27 23:46:42.686]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (240 ms)
[2020-12-27 23:46:47.659]  randomx  dataset ready (4973 ms)
[2020-12-27 23:46:47.659]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2020-12-27 23:46:47.662]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (3 ms)
[2020-12-27 23:46:48.210]  cpu      accepted (1/0) diff 500 (24 ms)
[2020-12-27 23:46:48.414]  cpu      accepted (2/0) diff 500 (25 ms)

```
**config.json**
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
    "autosave": false,
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
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "cn/0": null,
        "cn-lite/0": null
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
        "cn/0": null,
        "cn-lite/0": null
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
			"url": "",
			"user": "",
            "pass": "x",
            "rig-id": null,
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": true,
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
**root@host:~# uname -a**
```Linux m15l64 5.4.0-58-generic #64-Ubuntu SMP Wed Dec 9 08:16:25 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux```

**Additional context**
Any idea?
Thank you!

# Discussion History
## SChernykh | 2020-12-28T11:44:48+00:00
https://xmrig.com/docs/miner/randomx-optimization-guide/msr
- Check that you're not running inside a VM
- Disable secure boot in BIOS.

# Action History
- Created by: DeadManWalkingTO | 2020-12-27T22:11:59+00:00
- Closed at: 2021-01-10T01:05:49+00:00
