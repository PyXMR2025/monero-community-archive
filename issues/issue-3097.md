---
title: 'Operation error '
source_url: https://github.com/xmrig/xmrig/issues/3097
author: Keegz420mine
assignees: []
labels: []
created_at: '2022-07-25T05:53:17+00:00'
updated_at: '2022-08-01T06:04:42+00:00'
type: issue
status: closed
closed_at: '2022-08-01T06:04:42+00:00'
---

# Original Description
**Describe the bug**
Just keep getting connection error operation canceled 
**To Reproduce**
I’ve been trying different pools and everything . Did research and says it’s something to do not responding within 20 seconds and it’s network if things time out with a support. 5555 link that shows “mining pool” and worked for me but not the rig . 

**Expected behavior**
I’ve done this on a MacBook and a shitty windows tablet as well as a work pc and worked fine but after building a good pc it pops up 

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2022-07-25T06:04:45+00:00
Try to generate config.json with https://xmrig.com/wizard and if it doesn't work, show the full config that you used.

## Keegz420mine | 2022-07-25T06:26:47+00:00
Okay I will send it over when I’m home later today . But I do generate the config.json on the wizard no issues then delete the old one and drag and drop my new one in the same folder like I’ve always done . Is it I need to download the wallet ?never had to before maybe with the new update ? But will send the config.json when I’m home 

## SChernykh | 2022-07-25T06:33:09+00:00
You don't need to have a wallet on the PC you use for mining. I need to see your config.json to check for common issues like trying to connect to TLS port without TLS enabled in config.

## Keegz420mine | 2022-07-25T17:49:10+00:00

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
        "argon2": [0, 1, 2, 3, 4, 5],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3],
            [8, 4]
        ],
        "rx": [0, 1, 2, 3, 4],
        "rx/wow": [0, 1, 2, 3, 4, 5],
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
            "coin": "XMR",
            "url": "xmr-eu1.nanopool.org:14433",
            "user": "",
            "pass": null,
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
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

## Keegz420mine | 2022-07-25T17:49:20+00:00
took my wallet address out


## Spudz76 | 2022-07-25T19:34:51+00:00
`pools->"tls": true,`

is your problem.  nanopool does not offer SSL on any ports.  also nanopool sucks anyway I'd never use them unless you have high hashrate (>16KH/s) due to high fixed diff

## SChernykh | 2022-07-25T19:36:33+00:00
This config works fine for me, so your problem is somewhere else. Maybe your ISP or antivirus block the connection. @Spudz76 nanopool offers TLS on port 14433.

## Keegz420mine | 2022-07-25T19:57:08+00:00
Think maybe a vpn would work ?


## Keegz420mine | 2022-07-25T20:06:37+00:00
Which pool do you use @Spudz76 ?

## Keegz420mine | 2022-07-25T20:15:44+00:00
Don't have antivirus just windows defender and recently did an update maybe it's that as I mentioned earlier I used my Mac to mine on the same network via Wi-Fi 

## Spudz76 | 2022-07-26T04:44:23+00:00
@Keegz420mine MoneroOcean since most of my hardware sucks at RandomX

## Keegz420mine | 2022-07-26T07:14:52+00:00
How did you set up the config?

## Keegz420mine | 2022-07-26T07:15:16+00:00
Sorry I'm pretty noob at this 😂

## Keegz420mine | 2022-07-26T08:33:10+00:00
VPN has got it working good . For now 😂 thank you for your help ! 

## Spudz76 | 2022-07-27T21:44:37+00:00
I just edit the [default config.json](https://raw.githubusercontent.com/xmrig/xmrig/master/src/config.json) since I can speak JSON in my sleep, and am familiar completely with all the options and how to set them.

## Keegz420mine | 2022-07-28T05:56:48+00:00
Hahaha I see ... I have 3 rigs at the moment and I'm struggling to add workers .... 

## Keegz420mine | 2022-07-28T06:29:28+00:00
If I'm using the wizard do I add worker iD ar the end of my wallet address ?

## Spudz76 | 2022-07-28T15:51:47+00:00
Pools have their own ways of rig-id, the `rig-id` option under `pools` in config.json is technically a protocol extension and some pools don't support (ignore) that, then they use the "old" method of adding it after a dot/colon/etc on the wallet (`user`) field.  Others take it as part of the otherwise mostly unused `pass` field.

It's entirely up to the pool how they choose to do it, what field they parse it from or what separator character they use; check pool FAQ.

`worker-id` under the `api` section is unrelated and is only used for identification within the API responses (if API is enabled) and has nothing to do with the pool or mining in general (only monitoring/data collection).

## Keegz420mine | 2022-07-28T16:51:52+00:00
Ooohh okay yea I'm using xmr pool.eu now after you said Nanopool sucks haha which yea I can see this pool is much better . I tried to adjust worker is on the config and ruined it all has to redo the whole lot but oh well if I can't get it that's okay I'll just have to monitor it individually

## Spudz76 | 2022-07-28T17:47:46+00:00
Their "Getting Started" page has all the details of how to encode the rig-id into the `user` field

```
Mining to a Monero wallet with worker id called my_rig1 (+ sign):
  YOUR_XMR_WALLET_ADDRESS+my_rig1
```

## Keegz420mine | 2022-07-28T17:51:07+00:00
Thank you so much ! Going to config this all now .... I just need to open my eyes and I'll see what I'm looking for 😂😂 but an extra set always is a good idea sometimes 😂😂

# Action History
- Created by: Keegz420mine | 2022-07-25T05:53:17+00:00
- Closed at: 2022-08-01T06:04:42+00:00
