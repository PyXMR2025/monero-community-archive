---
title: Very low hashrate problem with Intel Xeon E5-2680 v4
source_url: https://github.com/xmrig/xmrig/issues/3655
author: navid-haghighi
assignees: []
labels:
- question
created_at: '2025-05-04T21:14:49+00:00'
updated_at: '2025-09-18T05:31:35+00:00'
type: issue
status: closed
closed_at: '2025-06-16T15:09:22+00:00'
---

# Original Description
I have a desktop computer with a CPU: Intel Xeon E5-2680 v4 processor and RAM: 32GB 2400MHZ DDR4 Dual, Motherboard: HUANANZHI X99-BD4 , and a SSD SATA3 , GPU: Radeon HD 5450, and an 800W power supply. 

But when I open XMRig , I can't get more than 6KH hash rate. While the benchmark section of my processor says that I should get about 14 KH hash rate.
It seems that the XMRig 6.22 uses only 14 threads, while my processor has 28 threads. Also, when I look in the Task Manager, the processor usage was 60%, but I want at least 90% of the processor power to be used. Also, I ran a stability test with Prime95 software and the processor was at 100% for a long time without any stability problems. So we can conclude that the problem is with the XMRig software. 

![Image](https://github.com/user-attachments/assets/13132263-4c3e-42b4-9610-57db0239b7da)

![Image](https://github.com/user-attachments/assets/2c36d354-197e-4cef-9e7b-8d4f89d10541)


# Discussion History
## navid-haghighi | 2025-05-04T23:09:04+00:00
My Config File:


`
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18],
            [1, 20],
            [1, 22],
            [1, 24],
            [1, 26],
            [1, 21],
            [1, 23],
            [1, 25],
            [1, 27]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14],
            [1, 16]
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
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [1, 20],
            [1, 21],
            [1, 22],
            [1, 23],
            [1, 24],
            [1, 25],
            [1, 26],
            [1, 27]
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
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27]
        ],
        "cn/upx2": [
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
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15],
            [2, 16],
            [2, 17],
            [2, 18],
            [2, 19],
            [2, 20],
            [2, 21],
            [2, 22],
            [2, 23],
            [2, 24],
            [2, 25],
            [2, 26],
            [2, 27]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10],
            [8, 12],
            [8, 14],
            [8, 16],
            [8, 18],
            [8, 20],
            [8, 22],
            [8, 24],
            [8, 26]
        ],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow"
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
            "algo": "rx/0",
            "coin": null,
            "url": "pool.supportxmr.com:3333",
            "user": "**********",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
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
`

## SChernykh | 2025-05-05T06:37:41+00:00
This is normal hashrate for this CPU. The best result for this model is ~7 kh/s per CPU - and this is in well-tuned and overclocked systems. If you just add more threads, you will run out of L3 cache and hashrate will be lower. You can get a bit higher hashrate if you use 4 memory sticks (this CPU has 4-channel memory).

## navid-haghighi | 2025-05-05T09:04:22+00:00
> This is normal hashrate for this CPU. The best result for this model is ~7 kh/s per CPU - and this is in well-tuned and overclocked systems. If you just add more threads, you will run out of L3 cache and hashrate will be lower. You can get a bit higher hashrate if you use 4 memory sticks (this CPU has 4-channel memory).

So why does the benchmark section of XMRig.com say that this processor can have a hashrate of up to 14 KHs?

![Image](https://github.com/user-attachments/assets/c104228f-4336-4e78-9473-829b0c54a1d5)

https://xmrig.com/benchmark

## SChernykh | 2025-05-05T09:05:44+00:00
This is dual CPU systems. Divide it by 2 if you have only one CPU.

## navid-haghighi | 2025-05-13T21:09:48+00:00
Does anyone else have any ideas? Is there a way to enable more than 14 threads on my 28-thread processor?

## ChaseYY01 | 2025-05-30T09:20:26+00:00
I think your hashrate is normal. Generally speaking, the first time XMRig runs, it will automatically optimize. In the RandomX Benchmark, the highest hashrate for a single CPU is about 7KH, and it also uses 14 threads. If you want to modify the number of threads used yourself, you can find "rx": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26] in the Config File and change it to "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]. However, I think the hashrate will likely decrease. You can try it.

## irwanto82 | 2025-09-18T05:31:34+00:00
> Does anyone else have any ideas? Is there a way to enable more than 14 threads on my 28-thread processor?

according Memory size requirements 
2080 MB per NUMA node for dataset, 1 NUMA node usually equal to 1 CPU socket, the miner show number of nodes on startup.
256 MB for cache on first NUMA node.
256 KB of L2 cache and 2 MB of L3 cache per 1 mining thread.

your L3 36MB <> requirement 28 x 2MB = 48MB
your L2 3.5MB <> requirement 28 x 256KB = about 7MB

3.5MB / 256KB = 13,671875 max 14 threads


# Action History
- Created by: navid-haghighi | 2025-05-04T21:14:49+00:00
- Closed at: 2025-06-16T15:09:22+00:00
