---
title: My hash Rate not same as Website Benchmarks
source_url: https://github.com/xmrig/xmrig/issues/2578
author: decoderprogrammer
assignees: []
labels:
- question
created_at: '2021-09-13T11:24:01+00:00'
updated_at: '2022-04-03T14:38:36+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:38:36+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/43597613/133072422-2ac5e027-6e22-4331-9bae-7453ca92f9b9.png)
![image](https://user-images.githubusercontent.com/43597613/133075243-a77577e4-9627-4f52-92aa-2ae289c01f7d.png)

My system specifications:

HP DL360p Gen8
2x Intel Xeon 2680 v2
4x 4GB ECC support HP ram 1333 (Total 16GB)
Ubuntu 20 installed on 32GB micro Card (100MB/s read speed - 32 MB/s write speed)
NIC 10/100 

*Huge page support and available
*1GB page set
*The prefetches configurations disabled through bios setup
*The power settings is set for performance in bios setup
*The WMSR set to "0x1a4 0xf"
*The CPU priority is 5


like as website, but my hash rate is around of 6500 H/s but site wrote 9048. H/s What have I missed?
Thanks


# Discussion History
## SChernykh | 2021-09-13T11:38:47+00:00
You need 4 memory sticks per CPU to fill 4 memory channels on each CPU. Without that your hashrate will be lower.

## xmrig | 2021-09-13T11:42:41+00:00
You also need to rebuild the miner with hwloc support, this is very important on multi CPU systems and start with a new fresh config.
Thank you. 


## decoderprogrammer | 2021-09-13T11:47:42+00:00
@

> You need 4 memory sticks per CPU to fill 4 memory channels on each CPU. Without that your hashrate will be lower.

That's mean ,At least I must put 4x 2GB memory per each cpu?

## decoderprogrammer | 2021-09-13T11:57:29+00:00
> You also need to rebuild the miner with hwloc support, this is very important on multi CPU systems and start with a new fresh config.
> Thank you.

I Built my miner with this link method:
https://xmrig.com/docs/miner/build/ubuntu

if it is possible say me The rebuild miner method with hwloc support or a give me a link for it
thank you

## decoderprogrammer | 2021-09-13T12:03:59+00:00
> > You also need to rebuild the miner with hwloc support, this is very important on multi CPU systems and start with a new fresh config.
> > Thank you.
> 
> I Built my miner with this link method:
> https://xmrig.com/docs/miner/build/ubuntu
> 
> if it is possible say me The rebuild miner method with hwloc support or a give me a link for it
> thank you

This method must be Correct, is it?

```
git clone https://github.com/xmrig/xmrig
cd xmrig
mkdir build
cd bulid
cmake -DWITH_HWLOC=ON ..
make
```

## xmrig | 2021-09-13T12:36:54+00:00
Hwloc enabled by default, no need to specify `-DWITH_HWLOC=ON` so only useful value is `OFF`, but the screenshot clearly says that the miner built without hwloc. 
Thank you.

## Spudz76 | 2021-09-13T14:35:52+00:00
You probably should also use the `scripts/build_deps.sh` to just build the included versions instead of distro provided older `*-dev` packages.

And then use `-DBUILD_DEPS=../scripts/deps` with the cmake step

## decoderprogrammer | 2021-09-14T05:17:20+00:00
I did the instructions given included "build_deps" , "hwloc", Except 8x 2GB Memory Stick. but my hash rate is still as below:
![image](https://user-images.githubusercontent.com/43597613/133198219-c569ab05-8c48-4a7e-9572-7b8946187730.png)

It may get better after changing my memory sticks! I'm not sure!

but another problem, that is the Hash rate in the pool. it is so different range from 4kh to 8kh in a day .is it correct ? despite my hash rate in local is around 6100 to 6300. my pool is "Hashvault.pro"

![image](https://user-images.githubusercontent.com/43597613/133198948-a3461870-173d-4e2e-8c8c-c3442e9e5aae.png)


## decoderprogrammer | 2021-09-14T08:23:01+00:00
After I changed the Config.json file to this, my hash rate increased to 8.7 KH .is there any changes on my config file for better it?

Thanks

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
    "donate-level":1,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages":true,
        "rdmsr": true,
        "wrmsr": "-a 0x1a4 0xf",
        "cache_qos":false,
	"numa":true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages":true,
        "huge-pages-jit": false,
        "hw-aes": true,
        "priority": 5,
        "memory-pool": true,
        "yield": false,
        "asm": "intel",
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
        "cn": [
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1]
        ],
        "cn-heavy": [
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1]
        ],
        "cn-lite": [
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1],
            [1, -1]
        ],
        "cn-pico": [
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1]
        ],
        "cn/upx2": [
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1],
            [2, -1]
        ],
        "rx": [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        "rx/arq": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        "rx/keva": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        "rx/wow": [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        "cn-lite/0": false,
        "cn/0": false
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
            "coin": "monero",
            "url": "pool.hashvault.pro:443",
            "user": "46zuZ8GbwVkFGZ5ukL6ttR5B7reeRrw9hWv9ZErpk47dLforbahDYyxZDmbii9v1gxB1JfbRxJEL2Dawa4ddBKcfD4qzQ2F",
            "pass": null,
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
```


# Action History
- Created by: decoderprogrammer | 2021-09-13T11:24:01+00:00
- Closed at: 2022-04-03T14:38:36+00:00
