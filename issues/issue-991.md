---
title: Optimal Config for E31270 with v2.14.1
source_url: https://github.com/xmrig/xmrig/issues/991
author: drayzen
assignees: []
labels: []
created_at: '2019-03-15T11:54:55+00:00'
updated_at: '2019-08-02T11:58:25+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:58:25+00:00'
---

# Original Description
A few months ago I was typically getting 500-550H/s with an E31270.
A couple of versions back it dropped substantially to ~300-350H/s and having just updated to v2.14.1 it appears to have dropped again.
I've previously used the below config with CPU affinity set to cores 4-7.
I've run it now using default config to see if possibly my config was the problem but it's switching between using cn/r and cn/rwz getting ~200-320 H/s, pretty much the same as with my config, while it used to be much more consistent.

Is this performance now normal, and is my below config still optimal for an E31270 and syntax correct for v2.14.1?

{
    "algo": "cryptonight",
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
    "cpu-affinity": "0xF0",
    "cpu-priority": null,
    "donate-level": 1,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 75,
    "pools": [
        {
            "url": "url",
            "user": "user",
            "pass": "pass",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": -1,
            "tls": true,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "threads": [
        {
            "low_power_mode": 1,
            "affine_to_cpu": 4,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 5,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 6,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": 7,
            "asm": true
        }
    ],
    "user-agent": null,
    "watch": false
}

# Discussion History
## Spudz76 | 2019-03-18T15:55:11+00:00
CN was fast (still is) try a run with variant 0 and see if it's your previous 512ish (which seems correct/ideal for that model)
CN2v2 fork hurt older CPU cores a bit more than newer ones, that drop is about right for CN2v1->v2 fork (October?)
SandyBridge has no AVX2 which hurts CN-R worse than other algos, thus your next kick in the pants.

I run a lot of Sandy/Ivy Bridges and they all had about the same changes.
I run a few better/newer things they had much less magnitude of loss, but still lost I'd estimate 10% each fork.

I have been running meta-miner and it jumps me around rwz/wow/trtl/r for the most part, which I take as a sign that my reduced performance is about the same as everyone else (still jumping in the game) otherwise I expect it would never select coins I am worse than average at finding, and change less often.

CN-Pico works best with packed cache and stacked threads, which is about double what autoconfig sets up.  So for 8M cache and 4cores do 8 threads per core thus two threads each same affinity (0,0,1,1,2,2,3,3) and low_power_mode at 4 on all of them.  That brings it into the mix otherwise it will never select it.

I don't use the global affinity hex thing it never seemed to do anything, just the thread-level ones.

# Action History
- Created by: drayzen | 2019-03-15T11:54:55+00:00
- Closed at: 2019-08-02T11:58:25+00:00
