---
title: 'connect error: "operation canceled"'
source_url: https://github.com/xmrig/xmrig/issues/3110
author: ThanatosXingYu
assignees: []
labels:
- question
created_at: '2022-08-26T11:06:29+00:00'
updated_at: '2024-11-03T14:27:21+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:21:26+00:00'
---

# Original Description
After I updated xmrig, I forgot to change the default config.json
Mining for donate.v2.xmrig.com:3333
Then I changed it
Mining at pool.supportxmr.com:3333
Prompt "error", and then I use the wizard, which gives me pool.supportxmr.com:443
But I still failed
I also tried to change TLS to true or false
But it still does
![QQ截图20220826190553](https://user-images.githubusercontent.com/53430376/186890643-fa4acd13-93e5-4540-b87b-3cb833049fe1.png)



# Discussion History
## ThanatosXingYu | 2022-08-26T11:06:52+00:00
This is my config.json

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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
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
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6]
        ],
        "rx": [0, 2, 4, 6],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
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
            "url": "pool.supportxmr.com:3333",
            "user": "46yGZ8MYpL6ES5TqT4LXeQeffQLQvG9oRM682XhuTDU2DET2RkPLppAKDWhtYqRsZg7hMQuiVPxhaeM5mAea7twq7DZeT1H",
            "pass": "mine",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
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

## SChernykh | 2022-08-26T11:36:06+00:00
Set `tls` to false because 3333 is non-tls port there. You can also try to set `algo` to `rx/0`.

## ThanatosXingYu | 2022-08-26T13:56:28+00:00

> Set `tls` to false because 3333 is non-tls port there. You can also try to set `algo` to `rx/0`.

Even if I set TLS to false, xmrig still reports an error
Even when I set algo to Rx / 0, it doesn't work
![QQ截图20220826215258](https://user-images.githubusercontent.com/53430376/186919834-9856a93e-8b78-4192-b869-2b0815063f20.png)
![QQ截图20220826215315](https://user-images.githubusercontent.com/53430376/186919841-b1810df0-7187-41dd-97d0-39f8ba1b7009.png)



## SChernykh | 2022-08-26T13:57:45+00:00
`"algo":"rx/0"`
You need to use quotes there.

## ThanatosXingYu | 2022-08-26T13:59:56+00:00
> `"algo":"rx/0"` 你需要在那里使用引号。
![QQ截图20220826215852](https://user-images.githubusercontent.com/53430376/186920693-2d1198e4-17e8-4237-b8ea-57e524f7adb0.png)
![QQ截图20220826215900](https://user-images.githubusercontent.com/53430376/186920703-ae9288fd-df79-408c-ad54-7172aee8c6f5.png)

still not
aaaaaa


## SChernykh | 2022-08-26T14:06:13+00:00
What's the output of `ping pool.supportxmr.com` if you run it in command line?

## ThanatosXingYu | 2022-08-26T14:11:45+00:00
> What's the output of `ping pool.supportxmr.com` if you run it in command line?

Maybe I know that's why.
It outputs timed out!!!
thxxxxxxxxxxxxxxx

## SChernykh | 2022-08-26T14:21:43+00:00
I was more interested in what IP address it's trying to ping. It can be that your DNS server blocks `pool.supportxmr.com`.

## ThanatosXingYu | 2022-08-26T14:23:23+00:00
If so, what should I do

## Spudz76 | 2022-08-26T15:24:18+00:00
Use external public DNS like 1.1.1.1 or 9.9.9.9 (if the ISP is filtering DNS) and/or a VPN (if the ISP is cutting connections to known mining pool IPs)

## im10furry | 2024-02-13T15:45:15+00:00
> > Set `tls` to false because 3333 is non-tls port there. You can also try to set `algo` to `rx/0`.
> 
> Even if I set TLS to false, xmrig still reports an error Even when I set algo to Rx / 0, it doesn't work ![QQ截图20220826215258](https://user-images.githubusercontent.com/53430376/186919834-9856a93e-8b78-4192-b869-2b0815063f20.png) ![QQ截图20220826215315](https://user-images.githubusercontent.com/53430376/186919841-b1810df0-7187-41dd-97d0-39f8ba1b7009.png)

The port is set to 33333，TLS was true，auto.c3pool.com:33333

## Spudz76 | 2024-02-13T20:08:25+00:00
Strings in JSON must be quoted.  So, `"algo": "rx/0",` not `"algo": rx/0,`

## MAGNAT12 | 2024-11-03T13:59:59+00:00
help me
```ABOUT        XMRig/6.22.2 gcc/13.2.0 (built for Windows x86-64, 64 bit)
 * LIBS         libuv/1.49.2 OpenSSL/3.0.15 hwloc/2.11.2
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
}


## im10furry | 2024-11-03T14:26:57+00:00
Try another pool and DNS, such as the cat pool: c3pool.org

# Action History
- Created by: ThanatosXingYu | 2022-08-26T11:06:29+00:00
- Closed at: 2022-12-13T14:21:26+00:00
