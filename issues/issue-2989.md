---
title: After the benchmark what can i do
source_url: https://github.com/xmrig/xmrig/issues/2989
author: Noeleth
assignees: []
labels: []
created_at: '2022-03-24T11:16:53+00:00'
updated_at: '2022-03-24T12:22:55+00:00'
type: issue
status: closed
closed_at: '2022-03-24T12:22:55+00:00'
---

# Original Description
hi, i geet the monero ocean xmrig, i donwloaded it and did the benchmark, having this json

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
        "init-avx2": 0,
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
        "memory-pool": true,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 2, 4, 6, 5, 7],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 5],
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
        "cn/2": [
            [1, 0],
            [1, 2],
            [1, 4]
        ],
        "cn/gpu": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
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
            [8, 4]
        ],
        "panthera": [0, 2, 4, 6],
        "rx": [0, 2, 4],
        "rx/arq": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 2, 4, 6, 5, 7],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn-lite/0": false,
        "cn/0": false,
        "panthera": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "astrobwt": false,
        "cn-lite/0": false,
        "cn/0": false,
        "panthera": false
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "gulf.moneroocean.stream:10128",
            "user": "87DutJKDeuBNqbkqTKNQEf76V4SKsU1wP3njJhPSu9hC7UwwG7JqTZC6BR1j94SH7Rafp5WvvGZ7dihxfDRYGJUd6VuFDSt",
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
    "watch": true,
    "rebench-algo": false,
    "bench-algo-time": 20,
    "algo-min-time": 0,
    "algo-perf": {
        "cn/0": 145.5926735352274,
        "cn/1": 140.37822111388195,
        "cn/2": 140.37822111388195,
        "cn/r": 140.37822111388195,
        "cn/fast": 280.7564422277639,
        "cn/half": 280.7564422277639,
        "cn/xao": 140.37822111388195,
        "cn/rto": 140.37822111388195,
        "cn/rwz": 187.17096148517592,
        "cn/zls": 187.17096148517592,
        "cn/double": 70.18911055694097,
        "cn/ccx": 291.1853470704548,
        "cn-lite/0": 670.9222980409421,
        "cn-lite/1": 670.9222980409421,
        "cn-heavy/xhv": 59.7186034392913,
        "cn-pico": 5095.208070617907,
        "cn-pico/tlo": 5095.208070617907,
        "cn/gpu": 53.253839935327406,
        "rx/0": 1703.2312035971975,
        "rx/arq": 13196.864478114478,
        "rx/graft": 1616.59333752357,
        "rx/sfx": 1703.2312035971975,
        "panthera": 2575.3295668549904,
        "argon2/chukwav2": 3298.2161594963272,
        "astrobwt": 291.6450978362149,
        "ghostrider": 247.25997369574748
    },
    "pause-on-battery": false,
    "pause-on-active": false
}


on the algo perf i saw that rx/arq obtain "rx/arq": 13196.864478114478, ok but at the finish of the benhmark the xmrig selected astrobwt and i stop it nd run again, but select astrobwt continuously. if i want to change to rx/arq algo, how can i do for it?

if someone can help me to o the new json file to run ill apreciate. thanks for all your help

# Discussion History
## SChernykh | 2022-03-24T12:00:05+00:00
You're asking in the wrong place. MoneroOcean fork is not the official xmrig.

## Noeleth | 2022-03-24T12:22:52+00:00
> You're asking in the wrong place. MoneroOcean fork is not the official xmrig.

Thanks. I put it in to the monero site.

# Action History
- Created by: Noeleth | 2022-03-24T11:16:53+00:00
- Closed at: 2022-03-24T12:22:55+00:00
