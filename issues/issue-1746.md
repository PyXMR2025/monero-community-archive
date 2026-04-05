---
title: 'Connect error: Operation Canceled'
source_url: https://github.com/xmrig/xmrig/issues/1746
author: david-serrano
assignees: []
labels: []
created_at: '2020-06-24T09:01:51+00:00'
updated_at: '2024-11-03T14:05:44+00:00'
type: issue
status: closed
closed_at: '2020-06-24T10:37:02+00:00'
---

# Original Description
**Describe the bug**
having this issue as of last night, tried using the latest release, and also ports 5555. 443 and 8080, with tls and without, with worker name as password and without, but nothing seems to work.. both on command line args and in config.json

This happens on two miners running on windows, however a miner running on Mac is perfectly fine.

**To Reproduce**
just ran the normal command line args ./xmrig -o [pool] -u [address] -p [workerName]

**Expected behavior**
The pool to connect and mining to start as normal

**Required data**
OS: Windows
Log: 

```
 * ABOUT        XMRig/6.2.2 gcc/10.1.0rAmS9h5zY52n3TZL8zg5n8 -k --tls -p worker1
 * LIBS         libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz (1) x64 AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       3.6/15.9 GB (23%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:5555 algo auto
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume
 * OPENCL       disabled
 * CUDA         disabled

net pool.supportxmr.com: 5555 connect error: "operation canceled"
```


**Additional context**
At one point during the mining i got the following:
```
cpu Rejected (diff [...]) "Unauthenticated"
net No active pools, stop mining
```
After this everything fell over i believe, and restarting the miner with all the configs described above resulted in nothing working

# Discussion History
## david-serrano | 2020-06-24T09:57:35+00:00
Update on this: tethering through a mobile hotspot seems to fix the issue, could the network config have been broken somehow during execution?

## xmrig | 2020-06-24T10:33:37+00:00
`"operation canceled"` means connection is not established in 20 seconds and forcibly closed to try again, it is almost the same as connection timeout, but with fixed platform independent time.

Please try open http://pool.supportxmr.com:5555/ in your browser, you should see text `Mining Pool Online` if it timeouts too, network issues confirmed and nothing can be done on the miner side.
Thank you.

## david-serrano | 2020-06-24T10:37:02+00:00
yeah, i tried that on the browser too, the connection just timed out, so it's a network issue rather than a miner or pool issue i believe! gonna try the following:
```
netsh interface show interface
netsh interface ipv4 show dnsservers
netsh interface ipv4 add dnsserver "Ethernet0" address=8.8.8.8 index=1
netsh interface ipv4 add dnsserver "Ethernet0" address=8.8.4.4 index=2
insted of "Ethernet0" set your name interface from
```
which will hopefully solve it and i'll close the issue

## lcj1988 | 2021-07-27T07:54:39+00:00
I am using unMineable software, during a sudden power outage, it shows the"operation canceled ",I updates the software, but it still can not working. How can I solve this?

## lcj1988 | 2021-07-27T07:55:13+00:00
[2021-07-27 15:49:20.441]  net      rx.unmineable.com:3333 connect error: "operation canceled"

[2021-07-27 15:49:45.625]  net      rx.unmineable.com:3333 connect error: "operation canceled"

[2021-07-27 15:50:10.814]  net      rx.unmineable.com:3333 connect error: "operation canceled"

## stefan2630 | 2021-10-27T14:53:36+00:00
[2021-10-27 08:19:54.263] no active connection
[2021-10-27 08:19:56.180]  net      donate.v2.xmrig.com:3333 connect error: "operation canceled"
[2021-10-27 08:20:21.231]  net      donate.v2.xmrig.com:3333 connect error: "operation canceled"
[2021-10-27 08:20:46.300]  net      donate.v2.xmrig.com:3333 connect error: "operation canceled"
[2021-10-27 08:21:11.359]  net      donate.v2.xmrig.com:3333 connect error: "operation canceled"
[2021-10-27 08:21:36.428]  net      donate.v2.xmrig.com:3333 connect error: "operation canceled"
[2021-10-27 08:24:32.320] no results yet


i keep getting this what does it mean and how do i fix this 

## rosariokt | 2023-09-09T04:48:12+00:00
> [2021-10-27 08:19:54.263] no active connection [2021-10-27 08:19:56.180] net donate.v2.xmrig.com:3333 connect error: "operation canceled" [2021-10-27 08:20:21.231] net donate.v2.xmrig.com:3333 connect error: "operation canceled" [2021-10-27 08:20:46.300] net donate.v2.xmrig.com:3333 connect error: "operation canceled" [2021-10-27 08:21:11.359] net donate.v2.xmrig.com:3333 connect error: "operation canceled" [2021-10-27 08:21:36.428] net donate.v2.xmrig.com:3333 connect error: "operation canceled" [2021-10-27 08:24:32.320] no results yet
> 
> i keep getting this what does it mean and how do i fix this

install tor ...and in your configuration use sock5 to connect to the mining pool

## Dijkstarlin | 2024-07-05T16:08:40+00:00
same problem and these command don't work,what should i do?

## MAGNAT12 | 2024-11-03T14:01:05+00:00
 ```* LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i3-8100 CPU @ 3.60GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       5.8/15.9 GB (36%)
                DIMM_A0: 8 GB DDR4 @ 2400 MHz CB8GU2666.C8JT
                DIMM_B0: 8 GB DDR4 @ 2400 MHz CB8GU2666.C8JT
 * MOTHERBOARD  Colorful Technology And Development Co.,LTD - DJ H310M-E
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.2miners.com:2222 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-11-03 18:58:52.386]  net      xmr.2miners.com:2222 162.19.139.184 connect error: "operation canceled"
[2024-11-03 18:59:17.568]  net      xmr.2miners.com:2222 162.19.139.184 connect error: "operation canceled"```

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
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1]
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
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2]
        ],
        "rx": [0, 1, 2],
        "rx/wow": [0, 1, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow"
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
            "algo": "rx/0",
            "coin": null,
            "url": "xmr.2miners.com:2222",
            "user": "",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "sni": false,
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
}```
help me 


# Action History
- Created by: david-serrano | 2020-06-24T09:01:51+00:00
- Closed at: 2020-06-24T10:37:02+00:00
