---
title: service WinRing0_1_2_0 already exists, but with a different service name
source_url: https://github.com/xmrig/xmrig/issues/2795
author: Cat7373
assignees: []
labels: []
created_at: '2021-12-06T00:47:32+00:00'
updated_at: '2025-06-20T11:07:43+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:07:43+00:00'
---

# Original Description
**Describe the bug**
```
 * ABOUT        XMRig/6.16.2 MSVC/2019
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i5-9400F CPU @ 2.90GHz (1) 64-bit AES VM
                L2:1.5 MB L3:9.0 MB 6C/6T NUMA:1
 * MEMORY       12.3/31.9 GB (39%)
                DIMM_A1: 16 GB DDR4 @ 2666 MHz KHX2666C16/16G
                ChannelA-DIMM2: <empty>
                DIMM_B1: 16 GB DDR4 @ 2666 MHz KHX2666C16/16G
                ChannelB-DIMM2: <empty>
 * MOTHERBOARD  System manufacturer - System Product Name
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      x algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-12-06 08:43:50.282]  net      use x TLSv1.2 x
[2021-12-06 08:43:50.283]  net      fingerprint (SHA-256): "f5725c18577243b1a5bbff1bdad26b56cc13b5e96150ca6897330f015852b954"
[2021-12-06 08:43:50.283]  net      new job from x diff 100001 algo rx/0 height 2508555 (148 tx)
[2021-12-06 08:43:50.284]  cpu      use argon2 implementation AVX2
[2021-12-06 08:43:50.284]  msr      service WinRing0_1_2_0 already exists, but with a different service name
[2021-12-06 08:43:50.290]  msr      cannot set MSR 0x000001a4 to 0x000000000000000f
[2021-12-06 08:43:50.291]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2021-12-06 08:43:50.291]  randomx  init dataset algo rx/0 (6 threads) seed 5ab039574d1c5b6c...
[2021-12-06 08:43:50.292]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2021-12-06 08:43:53.007]  randomx  dataset ready (2714 ms)
[2021-12-06 08:43:53.008]  cpu      use profile  rx  (5 threads) scratchpad 2048 KB
[2021-12-06 08:43:53.033]  cpu      READY threads 5/5 (5) huge pages 100% 5/5 memory 10240 KB (25 ms)
```

**To Reproduce**
* run xmrig 6.11.2
* run xmrig 6.16.2

**Expected behavior**
x

**Required data**
 Config file or command line
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
        "huge-pages-jit": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": true,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3, 4, 5],
        "astrobwt": [0, 1, 2, 3, 4, 5],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3],
            [8, 4]
        ],
        "rx": [0, 1, 2, 3, 4],
        "rx/wow": [0, 1, 2, 3, 4, 5],
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
        "adl": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "x",
            "user": "x",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": true,
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
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
```

OS: Windows


# Discussion History
## Spudz76 | 2021-12-06T01:55:12+00:00
Some thermal/LED/watercooling type software has loaded an MSR-access driver for itself, and xmrig tried to use it anyway, and it didn't work.

MSRs are used to set cache-preload by xmrig, but MSRs are also used by monitoring software to read deeper thermal and watt usage information.

Remove whatever, and instead use OpenHardwareMonitor or CoreTemp as their drivers work okay alongside xmrig.

## Dastano | 2024-01-05T01:11:26+00:00
Is there a way to find out which driver it is? That loads as MSR?

 Got the same issue, but not running any Monitoring Software. Only thing I could Imagine is Lian Li Software. But I doubt. 

## Spudz76 | 2024-01-05T01:41:48+00:00
It should cross reference it for you, mine says:
```
[2024-01-04 18:38:32.312]  msr      service WinRing0_1_2_0 already exists
[2024-01-04 18:38:32.312]  msr      service path: "\??\C:\Program Files\OpenHardwareMonitor\OpenHardwareMonitorLib.sys"
[2024-01-04 18:38:32.312]  msr      service WinRing0_1_2_0 already exists, but with a different service name
[2024-01-04 18:38:32.312]  msr      0x000001a4:0x0000000000000000 -> 0x000000000000000f
[2024-01-04 18:38:32.430]  msr      register values for "intel" preset have been set successfully (120 ms)
```

So thus obviously it's OpenHardwareMonitor (but still works anyway).  I have `"verbose": 5` set in my config but it didn't seem required for these diagnostic messages.

EDIT: also LED control software since many also use sensor data for things (changing red when hot, whatever)

# Action History
- Created by: Cat7373 | 2021-12-06T00:47:32+00:00
- Closed at: 2025-06-20T11:07:43+00:00
