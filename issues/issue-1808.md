---
title: xmrig.exe closes after running for a while (xmrig-6.3.1)
source_url: https://github.com/xmrig/xmrig/issues/1808
author: Tinovdk
assignees: []
labels: []
created_at: '2020-08-12T17:28:40+00:00'
updated_at: '2020-08-14T08:12:57+00:00'
type: issue
status: closed
closed_at: '2020-08-14T08:12:57+00:00'
---

# Original Description
xmrig.exe from xmrig-6.3.1-msvc-win64.zip closes after running for anywhere between some seconds to maybe 20 minues. I expect the program for days of not weeks or longer. I have tried:
- updating my chipset drivers
- disabling both combinations and all of the processor BIOS options
- changing processor values in the config file
-running xmrig.exe contained in xmrig-6.3.1-gcc-win64.zip
- run versions of XMrig back to version 5.11.4

**Miner log**
 * ABOUT        XMRig/6.3.1 MSVC/2019
 * LIBS         libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 5 1600 Six-Core Processor (1) x64 AES
                L2:3.0 MB L3:16.0 MB 6C/12T NUMA:1
 * MEMORY       5.2/32.0 GB (16%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmrpool.eu:5555 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-08-12 18:37:07.652]  net      use pool xmrpool.eu:5555  54.37.7.208
[2020-08-12 18:37:07.654]  net      new job from xmrpool.eu:5555 diff 50000 algo rx/0 height 2162942
[2020-08-12 18:37:07.654]  cpu      use argon2 implementation AVX2
[2020-08-12 18:37:07.680]  msr      0xc0011020:0x0006800000000010 -> 0x0000000000000000
[2020-08-12 18:37:07.680]  msr      0xc0011021:0x0000000000200000 -> 0x0000000000000040
[2020-08-12 18:37:07.681]  msr      0xc0011022:0x0000000000500000 -> 0x0000000000510000
[2020-08-12 18:37:07.681]  msr      0xc001102b:0x000000001808cc17 -> 0x000000001808cc16
[2020-08-12 18:37:07.794]  msr      register values for "ryzen" preset has been set successfully (140 ms)
[2020-08-12 18:37:07.795]  randomx  init dataset algo rx/0 (12 threads) seed 07391cfe8379829a...
[2020-08-12 18:37:07.801]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (6 ms)
[2020-08-12 18:37:11.974]  randomx  dataset ready (4173 ms)
[2020-08-12 18:37:11.974]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2020-08-12 18:37:12.145]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (169 ms)
[2020-08-12 18:37:24.248]  cpu      accepted (1/0) diff 50000 (77 ms)
[2020-08-12 18:37:38.643] [THREAD 14532] Access violation at 0x000002A0EDF57D2A: read at address 0x00000000FF202E74
[2020-08-12 18:37:38.869]  net      new job from xmrpool.eu:5555 diff 75000 algo rx/0 height 2162942
[2020-08-12 18:37:42.350]  cpu      accepted (2/0) diff 75000 (117 ms)
[2020-08-12 18:37:58.637]  cpu      accepted (3/0) diff 75000 (67 ms)
[2020-08-12 18:38:01.851]  cpu      accepted (4/0) diff 75000 (66 ms)
[2020-08-12 18:38:04.183] [THREAD 13380] Access violation at 0x000002A0EDE729AF: read at address 0x000002A18F6BA64D
[2020-08-12 18:38:04.355] [THREAD 13388] Access violation at 0x000002A0EDE51A7D: read at address 0x000005420021F420
[2020-08-12 18:38:04.653]  cpu      accepted (5/0) diff 75000 (59 ms)
[2020-08-12 18:38:05.000] [THREAD 7420] Access violation at 0x000002A0EDED557C: read at address 0x00000000DB01F5C0
[2020-08-12 18:38:07.588]  cpu      accepted (6/0) diff 75000 (59 ms)
[2020-08-12 18:38:11.992]  miner    speed 10s/60s/15m 3507.6 n/a n/a H/s max 3541.8 H/s
[2020-08-12 18:38:22.511] [THREAD 13388] Exception 0xC000001D at 0x000002A0EDE51803
[2020-08-12 18:38:24.515] [THREAD 13380] Exception 0xC000001D at 0x000002A0EDE72910
[2020-08-12 18:38:34.892]  net      new job from xmrpool.eu:5555 diff 112501 algo rx/0 height 2162942
[2020-08-12 18:38:37.220]  cpu      accepted (7/0) diff 112501 (63 ms)
[2020-08-12 18:38:43.235] [THREAD 13380] Access violation at 0x000002A0EDE7297D: read at address 0x00000541FFA850E0
[2020-08-12 18:38:49.159] [THREAD 14096] Access violation at 0x000002A0EDEB4042: read at address 0x0000000000000F64
[2020-08-12 18:38:49.160] [THREAD 14096] Access violation at 0x000002A0EDEC3A45: write at address 0x0000000000000000


**Config.json**
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
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 1],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 7]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 6],
            [1, 8]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11]
        ],
        "rx": [0, 2, 4, 1, 6, 8, 10, 7],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn/0": false,
        "cn-lite/0": false,
        "kawpow": false,
        "rx/arq": "rx/wow",
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
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": "monero",
            "url": "xmrpool.eu:5555",
            "user": "",
            "pass": "x",
            "rig-id": "test",
            "nicehash": false,
            "keepalive": true,
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
    "verbose": 2,
    "watch": true,
    "pause-on-battery": false
}

**System Information**
![notepad_2020-08-12_19-16-40](https://user-images.githubusercontent.com/42802450/90046432-c08d1080-dcd0-11ea-927d-8f597c312581.png)

**CPU**
![NVIDIA_Share_2020-08-12_19-09-33](https://user-images.githubusercontent.com/42802450/90046505-dc90b200-dcd0-11ea-968e-ee5b370de989.png)


# Discussion History
## offmarte | 2020-08-13T19:40:11+00:00
see this issue #1803
i also have a r5 1600. disabling opcache in bios solves the issue, try it. i use linux though, it could be some other problem on windows

## SChernykh | 2020-08-14T07:20:45+00:00
@Tinovdk you have to disable opcache in bios. If you don't have this option in bios, there's a special MSR mod setting you can use in config.json to disable opcache when xmrig starts.

## Tinovdk | 2020-08-14T08:12:57+00:00
@SChernykh Thanks for the tip of looking into MSR. Online I found mention of disabling opcache in bios but my bios does not give me that option. Setting this in the config solved the issue:

"randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": false,
        "wrmsr": ["0xc0011020:0x0", "0xc0011021:0x60", "0xc0011022:0x510000", "0xc001102b:0x1808cc16"],
        "cache_qos": false,
        "numa": true
}

# Action History
- Created by: Tinovdk | 2020-08-12T17:28:40+00:00
- Closed at: 2020-08-14T08:12:57+00:00
