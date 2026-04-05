---
title: Cryptonight/R @ nicehash = algo cn/1 & reject
source_url: https://github.com/xmrig/xmrig/issues/989
author: ShaddyR
assignees: []
labels:
- question
created_at: '2019-03-14T11:52:10+00:00'
updated_at: '2019-04-02T15:42:26+00:00'
type: issue
status: closed
closed_at: '2019-04-01T06:17:56+00:00'
---

# Original Description
Hi.
Mining @nicehash with algo cn/r set & any "variant" option resulting random change job algo from "cn/r" to "cn/1" and reject as result. Is it nicehash issue?
Config is:
__________________________________________
{
    "algo": "cryptonight/r",
    "api": {
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "asm": true,
    "autosave": true,
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 1,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 100,
    "pools": [
        {
            "url": "cryptonightr.in.nicehash.com:3375",
            "user": "addr.wrkr",
            "pass": "x",
            "rig-id": null,
            "nicehash": true,
            "keepalive": true,
            "variant": 8,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null
        },
__________________________________________

Result is:
__________________________________________
[2019-03-14 13:43:56] new job from cryptonightr.in.nicehash.com:3375 diff 200007
 algo cn/r height 1790467
[2019-03-14 13:44:08] speed 10s/60s/15m 982.8 990.3 n/a H/s max 1054.0 H/s
[2019-03-14 13:44:35] new job from cryptonightr.in.nicehash.com:3375 diff 200007
 algo cn/r height 1790467
[2019-03-14 13:45:08] speed 10s/60s/15m 977.8 1010.7 n/a H/s max 1054.0 H/s
[2019-03-14 13:45:30] new job from cryptonightr.in.nicehash.com:3375 diff 200007
 algo cn/r height 1790467
[2019-03-14 13:45:30] new job from cryptonightr.in.nicehash.com:3375 diff 200007
 algo **cn/1** height **394971**
[2019-03-14 13:45:44] new job from cryptonightr.in.nicehash.com:3375 diff 200007
 algo **cn/1** height **394972**
[2019-03-14 13:46:07] new job from cryptonightr.in.nicehash.com:3375 diff 200007
 algo cn/r height 1790468
[2019-03-14 13:46:07] new job from cryptonightr.in.nicehash.com:3375 diff 200007
 algo cn/r height 1790468
[2019-03-14 13:46:08] speed 10s/60s/15m 1184.8 1120.1 n/a H/s max 1199.2 H/s
__________________________________________

# Discussion History
## xmrig | 2019-03-14T11:59:30+00:00
Please set `"variant": "r",` in your pools, per pool variant option overrides global variant.
Thank you.

## ShaddyR | 2019-03-14T12:11:32+00:00
That's it! Quotes! I tried to use my logic & write "r", but WITHOUT quotes resulting error! Thank you for fast response. May be you should add notes to documentation to resolve situation like this? Any way thank you and good luck!

## xmrig | 2019-03-14T12:15:52+00:00
https://github.com/xmrig/xmrig-proxy/blob/master/doc/STRATUM_EXT.md#14-algorithm-names-and-variants

Quotes, commas and other stuff is JSON format requirement.
Thank you.

## Spudz76 | 2019-04-02T15:42:26+00:00
You could find a JSON parser to test your configs for JSON-compatibility after you mangle them.
Linux has `json_pp` for example which will tell you if it's formatted anywhere near correctly.
Some also online I'm sure (search JSON Validator)

# Action History
- Created by: ShaddyR | 2019-03-14T11:52:10+00:00
- Closed at: 2019-04-01T06:17:56+00:00
