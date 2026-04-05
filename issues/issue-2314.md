---
title: After Update no minig
source_url: https://github.com/xmrig/xmrig/issues/2314
author: Dragonheart1969
assignees: []
labels: []
created_at: '2021-04-25T19:13:26+00:00'
updated_at: '2021-05-02T16:00:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

since the update 6.12. the miner does not start anymore. I have allowed the whole folder in the defender but still no mining

![xmrig](https://user-images.githubusercontent.com/83183887/116006316-fd085e80-a60a-11eb-9aaf-1c43f7e6a509.png)




# Discussion History
## SChernykh | 2021-04-25T19:18:05+00:00
It looks like something is blocking your connection. Try another pool and/or connect to a TLS port.

## Dragonheart1969 | 2021-04-25T19:43:35+00:00
after entering a tls port the miner goes two lines further and then hangs again.
with minergate i have no problems at all, only with xmrig

![xmrig TLS 1](https://user-images.githubusercontent.com/83183887/116007261-2e832900-a60f-11eb-957e-3d84064548fd.png)
![xmrig TLS](https://user-images.githubusercontent.com/83183887/116007264-3347dd00-a60f-11eb-9595-2ef0c83e4259.png)

maybe I have an error in the config file


## Lonnegan | 2021-04-27T06:18:00+00:00
Have you tried without opencl for testing? If that doesn't help, try a different pool for testing, e.g. pool.hashvault.pro:3333

You shouldn't mine RandomX on GPU anyway! There are much more profitable algos for GPUs than RandomX!

## Spudz76 | 2021-04-27T16:34:56+00:00
Definite error in the config, "tls" is meant to be true or false, not the tls port.  You set "tls" to true and change the 5555 in the actual pool URL to the ssl port number... like `url: "xmrpool.eu:995",` with `tls: true,`

## Dragonheart1969 | 2021-04-27T17:09:01+00:00
Hello,

Thank you very much I will test it when I get home


mit freundlichen Grüßen
D. Beci

Tony Butler ***@***.***> schrieb am Di., 27. Apr. 2021, 18:35:

> Definite error in the config, "tls" is meant to be true or false, not the
> tls port. You set "tls" to true and change the 5555 in the actual pool URL
> to the ssl port number... like xmrpool.eu:995 with tls: true,
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2314#issuecomment-827747195>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AT2USD3G2RU6NMUKQTBSTN3TK3RUBANCNFSM43RSNROA>
> .
>


## Dragonheart1969 | 2021-04-30T14:57:43+00:00
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
        "max-threads-hint": 100,
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

I've tried everything possible, but the miner doesn't want to mine. I also changed the config without success. With Minergate everything goes without problems

## Dragonheart1969 | 2021-05-01T21:33:41+00:00
i will use the old version 6.10. install, this worked without any problems

## Dragonheart1969 | 2021-05-02T12:44:14+00:00
ich habe es nun mit einem anderen pool versucht, da ist das mining gar kein problem. es liegt dann wohl am pool selbst und nicht am miner.

grüße

## Spudz76 | 2021-05-02T16:00:02+00:00
Manchmal ist die Lösung erst offensichtlich, nachdem sie gefunden wurde!

Ich bin froh, dass es jetzt funktioniert.

# Action History
- Created by: Dragonheart1969 | 2021-04-25T19:13:26+00:00
