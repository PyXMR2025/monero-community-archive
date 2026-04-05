---
title: dev donate breaks miner
source_url: https://github.com/xmrig/xmrig/issues/1202
author: Gingeropolous
assignees: []
labels:
- bug
- need feedback
created_at: '2019-09-28T11:04:59+00:00'
updated_at: '2019-10-08T03:07:53+00:00'
type: issue
status: closed
closed_at: '2019-10-08T03:07:53+00:00'
---

# Original Description
running the evo branch on xmr testnet

```
[2019-09-28 05:01:29.784] dev donate started
[2019-09-28 05:01:29.784] new job from donate.ssl.xmrig.com:443 diff 1000225 algo cn/r height 1932739
[2019-09-28 05:01:29.791] CPU disabled, no suitable configuration for algo cn/r
[2019-09-28 05:02:22.807] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
```

# Discussion History
## xmrig | 2019-09-28T11:55:36+00:00
Please show config file or command line how you run miner.
Thank you.

## xmrig | 2019-09-28T12:35:37+00:00
You not use latest evo version, `CPU disabled` now looks different ` cpu  disabled (no suitable configuration found)`.

But right it a bug, miner should not stop mining if donation algorithm disabled, in normal case this issue should never happen, but there is no mainnet for `rx/0` and I don't expect someone will mine it long enough.

And it not breaks miner, after donation time is over miner switch back to user algorithm.
Thank you.

## Gingeropolous | 2019-09-28T12:44:15+00:00
it does not switch back to user algorithm. I find the miner like this:

```
 new job from donate.ssl.xmrig.com:443 diff 1000225 algo cn/r height 1932739
[2019-09-28 05:03:02.804] CPU disabled, no suitable configuration for algo cn/r
[2019-09-28 05:03:22.846] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-09-28 05:04:22.884] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-09-28 05:04:41.708] new job from donate.ssl.xmrig.com:443 diff 1000225 algo cn/r height 1932740
[2019-09-28 05:04:41.708] CPU disabled, no suitable configuration for algo cn/r
[2019-09-28 05:05:22.922] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-09-28 05:05:42.592] new job from donate.ssl.xmrig.com:443 diff 1000225 algo cn/r height 1932741
[2019-09-28 05:05:42.592] CPU disabled, no suitable configuration for algo cn/r
[2019-09-28 05:06:06.537] new job from donate.ssl.xmrig.com:443 diff 1000225 algo cn/r height 1932742
[2019-09-28 05:06:06.537] CPU disabled, no suitable configuration for algo cn/r
[2019-09-28 05:06:22.962] speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
[2019-09-28 05:06:29.784] dev donate finished
[2019-09-28 05:06:29.784] new job from 192.168.1.38:28081 diff 3043876 algo rx/test height 1310227
[2019-09-28 05:06:42.929] new job from 192.168.1.38:28081 diff 3060221 algo rx/test height 1310228
[2019-09-28 05:07:10.937] new job from 192.168.1.38:28081 diff 3073270 algo rx/test height 1310229
[2019-09-28 05:07:23.006] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:08:23.045] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:09:23.084] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:10:23.128] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:11:23.176] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:12:23.218] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:12:29.082] new job from 192.168.1.38:28081 diff 3082546 algo rx/test height 1310230
[2019-09-28 05:13:23.263] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:14:23.307] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:15:23.355] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:16:20.156] new job from 192.168.1.38:28081 diff 3090115 algo rx/test height 1310231
[2019-09-28 05:16:23.407] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:16:52.162] new job from 192.168.1.38:28081 diff 3050729 algo rx/test height 1310232
[2019-09-28 05:17:01.164] new job from 192.168.1.38:28081 diff 3054417 algo rx/test height 1310233
[2019-09-28 05:17:23.462] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:18:23.515] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:19:23.570] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:20:23.632] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:21:23.694] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:22:23.744] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:23:23.790] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:24:23.831] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:25:23.869] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:26:23.909] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:27:23.947] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:27:37.414] new job from 192.168.1.38:28081 diff 3077247 algo rx/test height 1310234
[2019-09-28 05:28:23.988] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:29:24.026] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
[2019-09-28 05:30:24.064] speed 10s/60s/15m n/a n/a n/a H/s max 6721.8 H/s
```

i just compiled evo version last night. i'll compile again.

## Gingeropolous | 2019-09-28T12:45:33+00:00
```
user@quadron:~/xmrig/build$ cat config.json 
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
    "version": 1,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": true,
        "priority": null,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "rx": [-1,-1,-1,-1,-1,-1,-1,-1,
-1,-1,-1,-1,-1,-1,-1,-1,
-1,-1,-1,-1,-1,-1,-1,-1,
-1,-1,-1,-1,-1,-1,-1,-1
],
        "rx/wow": [0, 2],
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "rx": [
            {
                "index": 0,
                "intensity": 1024,
                "worksize": 8,
                "threads": [16, 16],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 1024,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 0,
    "donate-over-proxy": 0,
    "log-file": null,
    "pools": [
        {
            "algo": "rx",
            "url": "192.168.1.38:28081",
            "user": "9x1E8RS9VaEHbGECj9XsUfPRXiSyYiBpb6MWqu3HPXTyJHVCb4ra8zrANRwL1Ky9Fu8Ux3DY6htSvWxT1Qgcr4LJEykFixf",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": true
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
```

## xmrig | 2019-09-28T13:22:16+00:00
https://github.com/xmrig/xmrig/commit/797d90c4dde46db78bf3175a825e4a981c835465#diff-148a76bf3ba9cd34736ab5e4f8c4b9d9L276 this line changed more than 1 month ago, probably you don't run `git pull` if use exists source dir.
Thank you.

## xmrig | 2019-09-28T15:13:29+00:00
Fixed.

## xmrig | 2019-09-29T15:58:18+00:00
v4.2 with fix released, please confirm issue solved.
Thank you.

# Action History
- Created by: Gingeropolous | 2019-09-28T11:04:59+00:00
- Closed at: 2019-10-08T03:07:53+00:00
