---
title: XMRig takes a very long time to initialize the RandomX dataset getting stuck.
source_url: https://github.com/xmrig/xmrig/issues/2483
author: OdioXmrig69
assignees: []
labels: []
created_at: '2021-07-14T09:29:29+00:00'
updated_at: '2021-07-14T10:04:44+00:00'
type: issue
status: closed
closed_at: '2021-07-14T10:04:44+00:00'
---

# Original Description
**Describe the bug**
I've been trying to use XMRig recently using the embedded config that is provided inside the code.
Issue is that it never starts mining because the RandomX dataset takes a very, very long time to get initialized.

**To Reproduce**
All I did was compile the build from Visual Studio and ran it on Release mode.

**Expected behavior**
The RandomX dataset should get initialized with the message "`dataset ready`" getting written to the console.

**Required data**
![image](https://user-images.githubusercontent.com/87419256/125598616-98f7bb5b-0ed2-49d2-904a-2befc4f40ff1.png)
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
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 50,
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
            "user": "my wallet",
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
 - Windows 10 Pro 20H2

**Additional context**
Using a Intel Core i7 8700K.

Edit: I've also tried on another machine that has an Intel i9 9900K and I got the same result. The RandomX dataset takes a long time there too. 

# Discussion History
## SChernykh | 2021-07-14T09:53:55+00:00
You're running without JIT compiler, this is why it's so slow. Did you compile 32-bit binary or maybe with `-DWITH_ASM=OFF`?

## OdioXmrig69 | 2021-07-14T09:54:44+00:00
> You're running without JIT compiler, this is why it's so slow. Did you compile 32-bit binary or maybe with `-DWITH_ASM=OFF`?

I compiled with -DWITH_ASM=OFF.

## SChernykh | 2021-07-14T09:55:13+00:00
Then it will run without ASM code which JIT compiler uses. It will be very very slow.

## OdioXmrig69 | 2021-07-14T09:56:06+00:00
> Then it will run without ASM code which JIT compiler uses. It will be very very slow.

Oh, I see, I'll recompile with the ASM code on and I'll see if it takes less time.

## OdioXmrig69 | 2021-07-14T10:04:44+00:00
Yup it did. Thanks mate for the help @SChernykh

# Action History
- Created by: OdioXmrig69 | 2021-07-14T09:29:29+00:00
- Closed at: 2021-07-14T10:04:44+00:00
