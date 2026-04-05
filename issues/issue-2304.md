---
title: 'Uplexa, unsupported algorithm '
source_url: https://github.com/xmrig/xmrig/issues/2304
author: RCTORONTO
assignees: []
labels: []
created_at: '2021-04-23T19:44:59+00:00'
updated_at: '2022-02-02T01:07:48+00:00'
type: issue
status: closed
closed_at: '2021-04-23T21:30:38+00:00'
---

# Original Description


Built the new 6.12.1 to try the Uplexa stuff on the pools... I'm doing something wrong...  Do we need to update our xmrig-cuda in order to use the uplexa stuff? or am I just not adding it to my config file improperly... I'm seeing: 

net      new job from uplexa.miner.rocks:30022 diff 1200K algo cn/upx2 height 0
nvidia   use profile  cn  (4 threads) scratchpad 128 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   0 | 04:00.0 |       750 |      50 |     15 |  0 |   0 |     93 | GeForce GTX 1050
|  1 |   1 | 84:00.0 |       648 |      36 |     18 |  0 |   0 |     81 | GeForce GTX 760
|  2 |   2 | 87:00.0 |       900 |      50 |     18 |  0 |   0 |    112 | GeForce GTX 760
|  3 |   3 | 8b:00.0 |       384 |     128 |      3 |  0 |   0 |     48 | GeForce GT 710
nvidia   thread #0 failed with error Unsupported algorithm
nvidia   thread #1 failed with error Unsupported algorithm
nvidia   thread #2 failed with error Unsupported algorithm
nvidia   thread #3 failed with error Unsupported algorithm
nvidia   thread #0 self-test failed
nvidia   thread #1 self-test failed
nvidia   thread #2 self-test failed
nvidia   thread #3 self-test failed
nvidia   disabled (failed to start threads)
net      new job from uplexa.miner.rocks:30022 diff 1200K algo cn/upx2 height 0
miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
...

my config is this:
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
        "enabled": false,
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
        "astrobwt-avx2": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": true,
        "loader": "/scripts/libxmrig-cuda-10.2.so",
        "nvml": true,
        "astrobwt": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 5,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 32,
                "blocks": 4,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 2,
                "threads": 32,
                "blocks": 6,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 3,
                "threads": 32,
                "blocks": 3,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            }
        ],
        "cn": [
            {
                "index": 0,
                "threads": 50,
                "blocks": 15,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 36,
                "blocks": 18,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 2,
                "threads": 50,
                "blocks": 18,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 3,
                "threads": 128,
                "blocks": 3,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 24,
                "blocks": 15,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 1,
                "threads": 18,
                "blocks": 18,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 2,
                "threads": 24,
                "blocks": 18,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 3,
                "threads": 68,
                "blocks": 3,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 102,
                "blocks": 15,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 72,
                "blocks": 18,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 2,
                "threads": 100,
                "blocks": 18,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 3,
                "threads": 128,
                "blocks": 3,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 15,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 4,
                "blocks": 48,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 2,
                "threads": 4,
                "blocks": 48,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 3,
                "threads": 4,
                "blocks": 8,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 50,
                "blocks": 15,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 4,
                "blocks": 48,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 2,
                "threads": 4,
                "blocks": 48,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            },
            {
                "index": 3,
                "threads": 4,
                "blocks": 8,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 10240,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 1,
                "threads": 256,
                "blocks": 12288,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 2,
                "threads": 256,
                "blocks": 12288,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 3,
                "threads": 256,
                "blocks": 2048,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
	"cn-upx2":[
	    {
		"index":0
	    },
	    {
		"index":1
	    },
	    {
		"index":2
	    }
	],
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 10,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": true
            },
            {
                "index": 1,
                "threads": 32,
                "blocks": 12,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": true
            },
            {
                "index": 2,
                "threads": 32,
                "blocks": 12,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": true
            },
            {
                "index": 3,
                "threads": 32,
                "blocks": 2,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 0,
    "pools": [
	        {
            "algo": "cn/upx2",
            "coin": null,
            "url": "uplexa.miner.rocks:30022",
            "user": "UPX1dsxFzj4ipRTyPnay5YDbMbdRFyme38xwuxfRPmfUd7kwC3T91zeNr3NmLSzHEQeXw2g5RWFsYc8y3xS9FYhr4EgPhVQHtt",
            "pass": "w=rc-g-gp",
            "rig-id": "rc-g-gp",
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        },
        {
            "algo": "cn-heavy/xhv",
            "coin": null,
            "url": "ca.haven.miner.rocks:4005",
            "user": "hvxyGTMAYGw2pU2ppW5VERDcZ5qMw4gvSgR5aYAiBVgVWc9HikKDsGBM3gv161hPzyEBdqnTtrVSDHgbd293rVAVA3KFsXCgWK",
            "pass": "w=rc-g-gp",
            "rig-id": "rc-g-gp",
            "nicehash": false,
            "keepalive": true,
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
    "print-time": 10,
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
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}



I likely have the algo name wrong or something I can't figure it out

# Discussion History
## RCTORONTO | 2021-04-23T19:51:15+00:00
Tried the Wizard to see what it said, but it doesn't support the Uplexa algo yet.

## xmrig | 2021-04-23T19:52:03+00:00
CUDA plugin must be updated to v6.12.0, the miner prints the plugin version on startup.
Thank you.


## RCTORONTO | 2021-04-23T19:54:27+00:00
Thank you, I will look at recompiling the newer one 

## RCTORONTO | 2021-04-23T20:14:03+00:00
it works now thanks again ;) I should have looked to see that the xmrig-cuda needed updating too.. my bad sorry.  

## shahnawaz6alam | 2022-02-02T01:07:48+00:00
my gpu is nvidia 710 and prosecer i7 2600 how is softwaere i run speed mining by xmr coin and eth please help me who software i dwnload my pc is sapport and high g/hs provide and speed mine please sir reply me 

# Action History
- Created by: RCTORONTO | 2021-04-23T19:44:59+00:00
- Closed at: 2021-04-23T21:30:38+00:00
