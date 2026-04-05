---
title: Only recognize 1 CPU in my 2 physical CPU machine?
source_url: https://github.com/xmrig/xmrig/issues/2201
author: kaiwu-astro
assignees: []
labels: []
created_at: '2021-03-23T06:23:50+00:00'
updated_at: '2021-03-29T09:44:17+00:00'
type: issue
status: closed
closed_at: '2021-03-23T09:17:42+00:00'
---

# Original Description
My machine has 2 Physical Intel(R) Xeon(R) CPU E5-2678 v3 @ 2.50GHz, which has 24 cores x 2 = 48 cores

https://xmrig.com/benchmark?cpu=Intel%28R%29+Xeon%28R%29+CPU+E5-2678+v3+%40+2.50GHz

when I press h during mining, it seems the program just recognize 24 cores, which is 1 CPU

![2021-03-23 2 17 35](https://user-images.githubusercontent.com/18334656/112102249-f1c4ac00-8be2-11eb-879d-231ab6bda0a7.png)

htops shows half cores are not working

![2021-03-23 2 22 31](https://user-images.githubusercontent.com/18334656/112102434-38b2a180-8be3-11eb-9127-2cbda8c6f52d.png)

At the beginning the program said

![2021-03-23 2 18 22](https://user-images.githubusercontent.com/18334656/112102286-fbe6aa80-8be2-11eb-84de-8a5217d51459.png)

I run it in Ubuntu 16.04, **with sudo**, and this is my profile

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
        "1gb-pages": true,
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
        "max-threads-hint": 48,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
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
            "algo": null,
            "coin": null,
            "url": "donate.v2.xmrig.com:3333",
            "user": "YOUR_WALLET_ADDRESS",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
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
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}

```

# Discussion History
## kaiwu-astro | 2021-03-23T06:25:13+00:00
turning `"huge-pages-jit": false,` to `on` does not help

## SChernykh | 2021-03-23T07:18:15+00:00
It uses all 24 cores (it's cores 0-23 in Linux, 24-47 are just virtual cores on Intel CPUs with HT), you most likely need to enable huge pages and MSR mod: https://xmrig.com/docs/miner/randomx-optimization-guide/

## kaiwu-astro | 2021-03-23T08:50:13+00:00
Thanks for your reply. I have just switched on MSR, and huge pages says "supported", but in htop result, only half CPU is used.

![2021-03-23 4 47 24](https://user-images.githubusercontent.com/18334656/112118910-d0ba8600-8bf7-11eb-990b-2a02bc60a2de.png)


## SChernykh | 2021-03-23T08:56:12+00:00
You have `huge pages 0%` on one of CPUs, this is why you get low hashrate. Normally, running xmrig as root should enable huge pages, but you might need to also enable them manually: https://xmrig.com/docs/miner/hugepages - 1280 pages per NUMA node, so you need 2560 pages.

## kaiwu-astro | 2021-03-23T09:03:07+00:00
Many thanks for your help. Now the hashrate has greatly incerased. But `htop` still says CPU usage is a half, which is the same with the very beginning. Can I increase it somehow?

![2021-03-23 5 01 01](https://user-images.githubusercontent.com/18334656/112120573-5ab71e80-8bf9-11eb-90ba-4e618718054c.png)


## SChernykh | 2021-03-23T09:07:16+00:00
You have 24 cores, and XMRig runs 24 threads on 24 cores. The other 24 are virtual threads because you have CPUs with HT. You probably need to reboot and allocate a bit more huge pages because it says `huge pages 62% 15/24` in the last line.

## kaiwu-astro | 2021-03-23T09:16:15+00:00
Thanks for the solution.

I rebooted my machine and gave 5120 pages. Now the hashrate is 10057 H/s, which matches the highest hashrate (two E5-2678 v3) in the benchmark. 

Many thanks again!

## agn-7 | 2021-03-29T09:17:57+00:00
@kaiwu-astro 
The problem is `"max-threads-hint"` is not the number of threads configuration, actually it is the portion (percentage) of numbers of threads that you've set that on `48` which means 48% or half of your thread amount. So you should set it on `100` and then restart the app. 

## kaiwu-astro | 2021-03-29T09:44:17+00:00
Thanks for your reply, but unfortunately this did not help. I have 11KHashes/s when I have max-threads-hint set to 48, and 10.9KHashes/s when it is 100 and the program is restarted.
On Mar 29, 2021, 17:18 +0800, Benyamin Jafari ***@***.***>, wrote:
> @kaiwu-astro
> The problem is "max-threads-hint" is not the number of threads configuration, actually it is the portion (percentage) of numbers of threads that you've set that on 48 which means 48% or half of your thread amount. So you should set it on 100 and then restart the app.
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub, or unsubscribe.


# Action History
- Created by: kaiwu-astro | 2021-03-23T06:23:50+00:00
- Closed at: 2021-03-23T09:17:42+00:00
