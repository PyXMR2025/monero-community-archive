---
title: failed to load CUDA plugin when using config.json (fine from command line)
source_url: https://github.com/xmrig/xmrig/issues/1797
author: aleqx
assignees: []
labels:
- bug
- CUDA
created_at: '2020-08-02T21:51:58+00:00'
updated_at: '2021-04-12T14:51:16+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:51:16+00:00'
---

# Original Description
Ubuntu 16.04. libxmrig-cuda.so sits in the same dir as xmrig.

The following works fine (connects, mines, pools accepts shares, etc):

`./xmrig -o pool.example.com:1234 -O wallet:pass --no-cpu --cuda --cuda-loader=./libxmrig-cuda.so --keepalive --print-time=120 -a rx/0 --no-nvml`

The following doesn't work

`./xmrig -c /tmp/config.json`

Error is as follows (I also compiled 5.4, and 6.3.1, and the corresponding xmrig-cuda for each):

```
 * ABOUT        XMRig/5.5.1 gcc/5.4.0
 * LIBS         libuv/1.8.0 OpenSSL/1.0.2g hwloc/1.11.2
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Pentium(R) CPU G4400 @ 3.30GHz (1) x64 AES
                L2:0.5 MB L3:3.0 MB 2C/2T NUMA:1
 * MEMORY       3.2/15.4 GB (21%)
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.example.com:1234 algo rx/0
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled (failed to load CUDA plugin)
[2020-08-02 22:43:55.030] [pool.example.com:1234] incompatible/disabled algorithm "rx/0" detected, reconnect
[2020-08-02 22:43:55.030] [pool.example.com:1234] login error code: 6
```

Where `/tmp/config.json` is:

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
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": false,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD"
    },
    "cuda": {
        "enabled": true,
        "loader": "/home/xmrig/libxmrig-cuda.so",
        "nvml": false,
        "rx/0": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 84,
                "bfactor": 3,
                "bsleep": 5000,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 1,
                "threads": 32,
                "blocks": 84,
                "bfactor": 3,
                "bsleep": 5000,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 2,
                "threads": 32,
                "blocks": 84,
                "bfactor": 3,
                "bsleep": 5000,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 3,
                "threads": 32,
                "blocks": 84,
                "bfactor": 3,
                "bsleep": 5000,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 4,
                "threads": 32,
                "blocks": 84,
                "bfactor": 3,
                "bsleep": 5000,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 5,
                "threads": 32,
                "blocks": 84,
                "bfactor": 3,
                "bsleep": 5000,
                "affinity": -1,
                "dataset_host": false
            },
            {
                "index": 6,
                "threads": 32,
                "blocks": 84,
                "bfactor": 3,
                "bsleep": 5000,
                "affinity": -1,
                "dataset_host": false
            }
        ]
    },
    "donate-level": 0,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "rx/0",
            "coin": null,
            "url": "pool.example.com:1234",
            "user": "wallet",
            "pass": "pass",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
    "print-time": 120,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "verbose": 0,
    "watch": true
}


# Discussion History
## xmrig | 2020-08-29T04:16:43+00:00
This issue should be fixed in v6.3.3, relative paths to plugin now supported and error reporting improved.
Thank you.


## Shille88 | 2021-01-24T15:09:40+00:00
I am experiencing this problem in 6.7.2

xmrig.exe -o pool -u wallet -p x --no-cpu --cuda --cuda-loader=./xmrig-cuda.dll --keepalive --print-time=120 -a rx/0 --no-nvml

## SChernykh | 2021-01-24T20:03:15+00:00
Try `--cuda-loader=xmrig-cuda.dll` (without ./) and make sure the dll is in the same directory as xmrig

## Shille88 | 2021-01-24T20:12:05+00:00
xmrig.exe -a rx/0 -o poolurl -u wallet -p x --no-cpu --cuda --cuda-loader=xmrig-cuda.dll --keepalive --print-time=120

The files are in the same folder, otherwise I will get other kind of errors if I don't. However I am still getting this error, 

"incompatible/disabled algorithm "rx/0" detected, reconnect
login error code: 6

![Capture](https://user-images.githubusercontent.com/20015176/105642231-c9415f80-5e88-11eb-9fdc-3f1193dbe711.PNG)


## SChernykh | 2021-01-24T20:20:05+00:00
You need more than 2GB of GPU memory to mine RandomX. You can use dataset in the host memory, but it can only be turned on if you use config.json instead of the command line.

## Shille88 | 2021-01-24T20:31:31+00:00
Okay I understand. Thank you very much for the clarification. I spent several hours googling on this issue :)

## Shille88 | 2021-01-24T21:00:12+00:00
Now I am instead getting,
```
thread #0 failed with error Unsupported algorithm
thread #0 self-test failed
disabled (failed to start threads)
```

Here is my entire config
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
		"enabled": false,
		"huge-pages": true,
		"huge-pages-jit": false,
		"hw-aes": null,
		"priority": null,
		"memory-pool": false,
		"yield": true,
		"asm": true,
		"argon2-impl": null,
		"astrobwt-max-size": 550,
		"astrobwt-avx2": false,
		"argon2": [
			0,
			1,
			2,
			3,
			4,
			5,
			6,
			7
		],
		"astrobwt": [
			0,
			1,
			2,
			3,
			4,
			5,
			6,
			7
		],
		"cn": [
			[
				1,
				0
			],
			[
				1,
				1
			],
			[
				1,
				2
			],
			[
				1,
				3
			],
			[
				1,
				4
			],
			[
				1,
				5
			],
			[
				1,
				6
			],
			[
				1,
				7
			]
		],
		"cn-heavy": [
			[
				1,
				0
			],
			[
				1,
				1
			],
			[
				1,
				2
			]
		],
		"cn-lite": [
			[
				1,
				0
			],
			[
				1,
				1
			],
			[
				1,
				2
			],
			[
				1,
				3
			],
			[
				1,
				4
			],
			[
				1,
				5
			],
			[
				1,
				6
			],
			[
				1,
				7
			]
		],
		"cn-pico": [
			[
				2,
				0
			],
			[
				2,
				1
			],
			[
				2,
				2
			],
			[
				2,
				3
			],
			[
				2,
				4
			],
			[
				2,
				5
			],
			[
				2,
				6
			],
			[
				2,
				7
			]
		],
		"rx": [
			0,
			1,
			2,
			3,
			4,
			5,
			6,
			7
		],
		"rx/wow": [
			0,
			1,
			2,
			3,
			4,
			5,
			6,
			7
		],
		"cn/0": false,
		"cn-lite/0": false,
		"kawpow": false,
		"rx/arq": "rx/wow",
		"rx/keva": "rx/wow"
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
		"enabled": true,
		"loader": null,
		"nvml": true,
		"cn": [
			{
				"index": 0,
				"threads": 18,
				"blocks": 16,
				"bfactor": 6,
				"bsleep": 25,
				"affinity": -1
			}
		],
		"cn-heavy": [
			{
				"index": 0,
				"threads": 10,
				"blocks": 16,
				"bfactor": 6,
				"bsleep": 25,
				"affinity": -1
			}
		],
		"cn-lite": [
			{
				"index": 0,
				"threads": 38,
				"blocks": 16,
				"bfactor": 6,
				"bsleep": 25,
				"affinity": -1
			}
		],
		"cn-pico": [
			{
				"index": 0,
				"threads": 4,
				"blocks": 64,
				"bfactor": 6,
				"bsleep": 25,
				"affinity": -1
			}
		],
		"cn/2": [
			{
				"index": 0,
				"threads": 4,
				"blocks": 64,
				"bfactor": 6,
				"bsleep": 25,
				"affinity": -1
			}
		],
		"rx/0": [
			{
				"index": 0,
				"threads": 32,
				"blocks": 84,
				"bfactor": 3,
				"bsleep": 5000,
				"affinity": -1,
				"dataset_host": true
			}
		],
		"cn/0": false,
		"cn-lite/0": false
	},
	"log-file": null,
	"donate-level": 1,
	"donate-over-proxy": 1,
	"pools": [
		{
			"algo": "rx/0",
			"coin": null,
			"url": "pool.minexmr.com:4444",
			"user": "wallet",
			"pass": "x",
			"rig-id": null,
			"nicehash": false,
			"keepalive": false,
			"enabled": true,
			"tls": false,
			"tls-fingerprint": null,
			"daemon": false,
			"socks5": null,
			"self-select": null
		}
	],
	"retries": 5,
	"retry-pause": 5,
	"print-time": 60,
	"health-print-time": 60,
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
	"pause-on-battery": false
}
```

![Capture2](https://user-images.githubusercontent.com/20015176/105643411-03622f80-5e90-11eb-957e-653ed683ecb4.PNG)


## Spudz76 | 2021-01-24T21:06:38+00:00
RandomX (all flavors), AstroBWT, and KawPow are disabled (in the plugin) with CUDA less than 9.0
They simply don't work with CUDA 8.0 (and Fermi cores don't work with anything newer than 8)

Compile main miner with those also disabled, or set all of them to `false` in your config.

I mine Fermi's still but you have to be on a pool that pays out XMR for whatever other algo a Fermi can process (CN-Heavy/XHV or CN-GPU work well).  Unless you actually want Haven or RYO coins for some reason.  MoneroOcean has a fork of the miner that autoswitches coin type per profitability, and re-includes CN-GPU (was dropped from official quite a while back, but works well on Fermi's), and they pay out in XMR.

Also RandomX on GPUs is rather pointless, on purpose, even if you got it to process the rate would be totally useless for the watts.  Better off running a space heater and throwing dollars into it.

## Shille88 | 2021-01-24T21:33:04+00:00
Thanks for the info and suggestions. I am still new to this so i am trying my way forward. The MoneroOcean fork seem to work well. 

## ghost | 2021-02-08T09:05:16+00:00
I always suggest to use --coin monero (or the one you want to mine) instead of --algo. This will permit to xmrig to use the best algo for your machine.

# Action History
- Created by: aleqx | 2020-08-02T21:51:58+00:00
- Closed at: 2021-04-12T14:51:16+00:00
