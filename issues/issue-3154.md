---
title: Unable to connect to pool xmrig on ubuntu 18.04
source_url: https://github.com/xmrig/xmrig/issues/3154
author: k7n2g
assignees: []
labels:
- question
created_at: '2022-11-03T14:35:49+00:00'
updated_at: '2022-12-13T14:15:00+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:15:00+00:00'
---

# Original Description
Hi the windows version connects to the pool with no problem, But can't get xmrig on ubuntu to connect to the pool any help appreciated from you guys.

Ubuntu 18.04 
version": "3.0.0
Used advanced build ./scripts/build_deps.sh

Installed no problems  but won't connect to pool  this is pool miner generate configuration,

"pool_list": [
    {
        "pool_address": "144.91.116.226:8117:5555",
        "wallet_address": "YOUR_WALLET_ADDRESS",
        "rig_id": "x",
        "pool_password": "x",
        "use_nicehash": false,
        "use_tls": false, /* Set to true if you are using an SSL port */
        "tls_fingerprint": "",
        "pool_weight": 1
    },
],
"currency": "cryptonight",

[](url) https://qbitminerspool.com

Pool: 144.91.116.226:5555
![Screenshot_12](https://user-images.githubusercontent.com/56478550/199743790-d094ff55-feb3-4973-b028-02bf7142e9a0.png)

i am using the derogold  algo cn/upx2 because xmrig wont use cn/0 or 1 as algo

This is my config.json file 

{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": true,
        "host": "127.0.0.1",
        "port": 8070,
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
        "mode": "fast",
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
            [1, 2],
            [1, 3]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
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
            [8, 2],
            [8, 3]
        ],
        "rx": [-1, -1],
        "rx/wow": [0, 1, 2, 3],
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
            "algo": "cn/upx2",
            "coin": "coin",
	   "url": "144.91.116.226:5555",
           "user": "QBC9VpKJVzY4P63hqJgd4yELKqhJM2opD7cyLN7TJrxvfodPRFoF3nC9wptGVFxnSTZ1M6pimFWRrWDvrckAUsLn9cKgoy8Tak",
            "rig_id": "null",
            "pass": "x",            
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": true,
            "socks5": null,
            "self-select": true,
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
        "enabled": true,
        "protocols": null,
        "cert": "cert.pem",
        "cert_key": "cert_key.pem",
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


# Discussion History
## SChernykh | 2022-11-03T14:40:16+00:00
`"daemon": true,` set this to `false`
`"coin": "coin",` this is definitely wrong, it's better to just remove this line.

## k7n2g | 2022-11-03T14:52:49+00:00
Thanks for the reply have done that now i get:

144.91.116.226:5555 read error: "end of file"
[2022-11-03 15:51:45.170]  net      144.91.116.226:5555 read error: "end of file"
[2022-11-03 15:51:50.176]  net      144.91.116.226:5555 read error: "end of file"


## k7n2g | 2022-11-03T15:00:38+00:00
I changed tls  to false,  now get

  * POOL #1      144.91.116.226:5555 algo cn/upx2
[2022-11-03 15:58:27.141]  net      use pool 144.91.116.226:5555  144.91.116.226
[2022-11-03 15:58:27.141]  net      new job from 144.91.116.226:5555 diff 25000 algo cn/upx2 height 119660 (1 tx)
[2022-11-03 15:58:27.141]  cpu      use profile  cn/upx2  (4 threads) scratchpad 128 KB
[2022-11-03 15:58:27.157]  cpu      READY threads 4/4 (8) huge pages 100% 4/4 memory 1024 KB (17 ms)
[2022-11-03 15:58:30.196]  cpu      rejected (0/1) diff 25000 "Rejected share: invalid result" (55 ms)
[2022-11-03 15:58:32.105]  cpu      rejected (0/2) diff 25000 "Rejected share: invalid result" (42 ms)
[2022-11-03 15:58:32.555]  cpu      rejected (0/3) diff 25000 "Rejected share: invalid result" (48 ms)
[2022-11-03 15:58:35.825]  cpu      rejected (0/4) diff 25000 "Rejected share: invalid result" (45 ms)
[2022-11-03 15:58:37.259]  cpu      rejected (0/5) diff 25000 "Rejected share: invalid result" (46 ms)


## SChernykh | 2022-11-03T15:01:55+00:00
Are you 100% sure it uses `cn/upx2` algorithm and not some obscure modification of that algorithm?

## k7n2g | 2022-11-03T15:03:37+00:00
i have tried most other algos no luck i think this is the algo that Derogold now uses but i am not 100% sure 

## Spudz76 | 2022-11-03T15:12:43+00:00
What does it do when you leave both `algo` and `coin` unset/false (now that it actually talks to the pool)?  Then it "should" autodetect based on what the pool sends as a job, if it's supported and recognizable.

## Spudz76 | 2022-11-03T15:15:39+00:00
OH! You have to re-enable `cn/0` by changing:
```
"cn/0": false,
```
to:
```
"cn/0": "cn",
```

## k7n2g | 2022-11-03T15:18:25+00:00
disabled (no suitable configuration found)

will add back and change cn/0

## SChernykh | 2022-11-03T15:26:05+00:00
According to https://miningpoolstats.stream/derogold it uses `cn/upx`, but there are no pools (solo only). So I'm not sure what pool you're using and if it's set up properly.

## k7n2g | 2022-11-03T15:27:54+00:00
  Many thanks Spudz76  the cn/0  solved it we are now mining to the Qbit pool   i wonder how we can add Qbit currency to the miner is that possible 

[2022-11-03 16:24:08.978]  net      new job from 144.91.116.226:5555 diff 17442 algo cn/0 height 121257 (1 tx)
[2022-11-03 16:24:18.583]  net      new job from 144.91.116.226:5555 diff 10679 algo cn/0 height 121257 (1 tx)
[2022-11-03 16:24:30.563]  cpu      accepted (2/0) diff 10679 (45 ms)
[2022-11-03 16:24:36.136]  miner    speed 10s/60s/15m 125.2 123.4 n/a H/s max 130.5 H/s
[2022-11-03 16:24:48.582]  net      new job from 144.91.116.226:5555 diff 21358 algo cn/0 height 121257 (1 tx)


## SChernykh | 2022-11-03T15:29:38+00:00
You don't need to add it, it uses cn/0 which is already supported by xmrig. Also, how is derogold related to all this?

## Spudz76 | 2022-11-03T15:30:11+00:00
Even if Qbit was known to the miner it would just point to the disabled by default `cn/0` profile and act like it's unsupported.  Unless you knew to go link it back to the base `"cn"` profile, and set the algo, but by then you don't need to use shortcuts by coin/currency name.

## k7n2g | 2022-11-03T15:35:13+00:00
we were trying to mine on the derogold chain and on the Qbit Blockchain we seem to have fixed this now we have a multipool arrangement in the works and we want to use xmrig for all mining if it pans out  as we are working on the payment vehicle for Qbit currency we want all users to use the tools we know work and xmrig works

# Action History
- Created by: k7n2g | 2022-11-03T14:35:49+00:00
- Closed at: 2022-12-13T14:15:00+00:00
