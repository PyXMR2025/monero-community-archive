---
title: 'hi ihave problem ''login error code 6 '
source_url: https://github.com/xmrig/xmrig/issues/1211
author: youssef2019am
assignees: []
labels:
- question
created_at: '2019-09-30T20:58:13+00:00'
updated_at: '2024-01-07T21:44:16+00:00'
type: issue
status: closed
closed_at: '2019-10-08T03:07:16+00:00'
---

# Original Description
No description

# Discussion History
## youssef2019am | 2019-09-30T20:59:24+00:00
is my config 
{
    "api": {
        "id": null,
        "": null
    },
    "http": {
        "enabled": false,
        "host": "  ",
        "port": 5555,
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
        "hw-aes": null,
        "priority": null,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 1]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/gpu": [0, 1, 2, 3],
        "rx": [0, 2],
        "rx/wow": [0, 2, 1],
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD"
    },
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "url": "pool.supportxmr.com:5555",
            "user": "49ZznZoUN5iNz9bqq2gLcw8nmTHkqbCQ6DUJcWATsqisV2cSognJjpJBZ3Z54ByUfUWW25ypj3kwWJKEhS4DQFAnToQAo9U",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false
            
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}

## xmrig | 2019-09-30T21:43:06+00:00
In recent versions this error has better description: `unknown algorithm, make sure you set "algo" or "coin" option`, so you should set `"algo":"cn/r",` or (better) `"coin": "monero",` https://github.com/xmrig/xmrig/blob/master/src/config.json#L37

## ghost | 2020-04-04T18:30:27+00:00
hello i keep having the same problem and i have added "algo":"cn/r", and tried "coin": "monero",


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
    "background": false,
    "colors": true,
    "cuda-bfactor": 6,
    "cuda-bsleep": 25,
    "cuda-max-threads": 64,
    "donate-level": 5,
    "log-file": null,
    "pools": [
        {
		 "coin": "monero",
            "url": "pool.supportxmr.com:3333",
            "user": "499HYuKFWzagpS1SG6fGrsh5vHSQVPtz7XH5qvKsqsDGTxPxvtuVGV1Z7oSZADGmuHH1xvXFwdsF1MtpMemcKRu8SVvMgvV",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": -1,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "threads": [
        {
            "index": 0,
            "threads": 30,
            "blocks": 108,
            "bfactor": 6,
            "bsleep": 25,
            "sync_mode": 3,
            "affine_to_cpu": false
        }
    ],
    "user-agent": null,
    "syslog": false,
    "watch": true
}


## xmrig | 2020-04-05T04:43:37+00:00
@BigHuncho Current Monero algorithm is RandomX, not `cn/r` with supportxmr.com pool and recent version of unified miner you don't need specify `algo` or `coin` option.

You use config from xmrig-nvidia, this miner outdated and now part of unified xmrig, but use GPUs for RandomX is not best idea, please do little research.
Thank you.

## ghost | 2020-04-05T21:54:15+00:00
> 
> 
> @BigHuncho Current Monero algorithm is RandomX, not `cn/r` with supportxmr.com pool and recent version of unified miner you don't need specify `algo` or `coin` option.
> 
> You use config from xmrig-nvidia, this miner outdated and now part of unified xmrig, but use GPUs for RandomX is not best idea, please do little research.
> Thank you.

thankn you very much for this help, so what route would you recommend, i am pretty new to this and trying to learn and i know i wont make much but this is just me practicing while i get me some good mining hardware

## mp0wr | 2020-07-07T07:50:29+00:00
hi @BigHuncho 
Mine Still alerts about `coin` or `algo`.
How can this be fixed?

I used the (newer?) wizard here: 
https://xmrig.com/wizard
I skipped the optional checkboxes.

config file is shorter, and launch has fewer warnings. Looks like a 403 forbidden as well.

```
* ABOUT        xmrig-proxy/5.11.0 clang/11.0.3
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g
 * MODE         nicehash
 * POOL #1      pool.supportxmr.com:443 algo auto
 * BIND #1      0.0.0.0:3333
 * BIND #2      [::]:3333
 * COMMANDS     hashrate, connections, verbose, workers
 * HTTP API     127.0.0.1:18081
[2020-07-07 00:46:17.450] [pool.supportxmr.com:443] unknown algorithm, make sure you set "algo" or "coin" option
[2020-07-07 00:46:17.450] [pool.supportxmr.com:443] login error code: 6
[2020-07-07 00:46:19.447] [pool.supportxmr.com:443] unknown algorithm, make sure you set "algo" or "coin" option
[2020-07-07 00:46:19.447] [pool.supportxmr.com:443] login error code: 6
[2020-07-07 00:46:34.591] 127.0.0.1 POST /json_rpc 403 289 222ms "(null)"
[2020-07-07 00:47:17.280] 0.00 kH/s, shares: 0/0 +0, upstreams: 0, miners: 0 (max 0) +0/-0
[2020-07-07 00:47:27.584] 127.0.0.1 POST /json_rpc 403 289 212ms "(null)"
[2020-07-07 00:48:17.394] 0.00 kH/s, shares: 0/0 +0, upstreams: 0, miners: 0 (max 0) +0/-0
[2020-07-07 00:49:03.577] 127.0.0.1 POST /json_rpc 403 289 207ms "(null)"
[2020-07-07 00:49:17.464] 0.00 kH/s, shares: 0/0 +0, upstreams: 0, miners: 0 (max 0) +0/-0
```

config-new.json
```
{
    "api": {
        "worker-id": "workername"
    },
    "http": {
        "enabled": true,
        "host": "127.0.0.1",
        "port": 18081,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "donate-level": 1,
    "cpu": true,
    "opencl": true,
    "cuda": false,
    "pools": [
        {
            "url": "pool.supportxmr.com:443",
            "user": "ADDRESS",
            "pass": "workername",
            "keepalive": true,
            "tls": true
        }
    ]
}
```

## renatomb | 2020-08-03T00:57:40+00:00
> hi @BigHuncho
> Mine Still alerts about `coin` or `algo`.
> How can this be fixed?
> 
> I used the (newer?) wizard here:
> https://xmrig.com/wizard
> I skipped the optional checkboxes.
> 
> config file is shorter, and launch has fewer warnings. Looks like a 403 forbidden as well.
> 
> ```
> * ABOUT        xmrig-proxy/5.11.0 clang/11.0.3
>  * LIBS         libuv/1.38.1 OpenSSL/1.1.1g
>  * MODE         nicehash
>  * POOL #1      pool.supportxmr.com:443 algo auto
>  * BIND #1      0.0.0.0:3333
>  * BIND #2      [::]:3333
>  * COMMANDS     hashrate, connections, verbose, workers
>  * HTTP API     127.0.0.1:18081
> [2020-07-07 00:46:17.450] [pool.supportxmr.com:443] unknown algorithm, make sure you set "algo" or "coin" option
> [2020-07-07 00:46:17.450] [pool.supportxmr.com:443] login error code: 6
> [2020-07-07 00:46:19.447] [pool.supportxmr.com:443] unknown algorithm, make sure you set "algo" or "coin" option
> [2020-07-07 00:46:19.447] [pool.supportxmr.com:443] login error code: 6
> [2020-07-07 00:46:34.591] 127.0.0.1 POST /json_rpc 403 289 222ms "(null)"
> [2020-07-07 00:47:17.280] 0.00 kH/s, shares: 0/0 +0, upstreams: 0, miners: 0 (max 0) +0/-0
> [2020-07-07 00:47:27.584] 127.0.0.1 POST /json_rpc 403 289 212ms "(null)"
> [2020-07-07 00:48:17.394] 0.00 kH/s, shares: 0/0 +0, upstreams: 0, miners: 0 (max 0) +0/-0
> [2020-07-07 00:49:03.577] 127.0.0.1 POST /json_rpc 403 289 207ms "(null)"
> [2020-07-07 00:49:17.464] 0.00 kH/s, shares: 0/0 +0, upstreams: 0, miners: 0 (max 0) +0/-0
> ```
> 
> config-new.json
> 
> ```
> {
>     "api": {
>         "worker-id": "workername"
>     },
>     "http": {
>         "enabled": true,
>         "host": "127.0.0.1",
>         "port": 18081,
>         "access-token": null,
>         "restricted": true
>     },
>     "autosave": true,
>     "donate-level": 1,
>     "cpu": true,
>     "opencl": true,
>     "cuda": false,
>     "pools": [
>         {
>             "url": "pool.supportxmr.com:443",
>             "user": "ADDRESS",
>             "pass": "workername",
>             "keepalive": true,
>             "tls": true
>         }
>     ]
> }
> ```


try to set **`"coin": "monero"`** inside pool key:
```
"pools": [
    {
        "url": "pool.supportxmr.com:443",
        "user": "ADDRESS",
        "pass": "workername",
        "coin": "monero",
        "keepalive": true,
        "tls": true
    }
]
```

## RepLicanT-UHD | 2020-08-18T09:29:30+00:00
> > hi @BigHuncho
> > Mine Still alerts about `coin` or `algo`.
> > How can this be fixed?
> > I used the (newer?) wizard here:
> > https://xmrig.com/wizard
> > I skipped the optional checkboxes.
> > config file is shorter, and launch has fewer warnings. Looks like a 403 forbidden as well.
> > ```
> > * ABOUT        xmrig-proxy/5.11.0 clang/11.0.3
> >  * LIBS         libuv/1.38.1 OpenSSL/1.1.1g
> >  * MODE         nicehash
> >  * POOL #1      pool.supportxmr.com:443 algo auto
> >  * BIND #1      0.0.0.0:3333
> >  * BIND #2      [::]:3333
> >  * COMMANDS     hashrate, connections, verbose, workers
> >  * HTTP API     127.0.0.1:18081
> > [2020-07-07 00:46:17.450] [pool.supportxmr.com:443] unknown algorithm, make sure you set "algo" or "coin" option
> > [2020-07-07 00:46:17.450] [pool.supportxmr.com:443] login error code: 6
> > [2020-07-07 00:46:19.447] [pool.supportxmr.com:443] unknown algorithm, make sure you set "algo" or "coin" option
> > [2020-07-07 00:46:19.447] [pool.supportxmr.com:443] login error code: 6
> > [2020-07-07 00:46:34.591] 127.0.0.1 POST /json_rpc 403 289 222ms "(null)"
> > [2020-07-07 00:47:17.280] 0.00 kH/s, shares: 0/0 +0, upstreams: 0, miners: 0 (max 0) +0/-0
> > [2020-07-07 00:47:27.584] 127.0.0.1 POST /json_rpc 403 289 212ms "(null)"
> > [2020-07-07 00:48:17.394] 0.00 kH/s, shares: 0/0 +0, upstreams: 0, miners: 0 (max 0) +0/-0
> > [2020-07-07 00:49:03.577] 127.0.0.1 POST /json_rpc 403 289 207ms "(null)"
> > [2020-07-07 00:49:17.464] 0.00 kH/s, shares: 0/0 +0, upstreams: 0, miners: 0 (max 0) +0/-0
> > ```
> > 
> > 
> > config-new.json
> > ```
> > {
> >     "api": {
> >         "worker-id": "workername"
> >     },
> >     "http": {
> >         "enabled": true,
> >         "host": "127.0.0.1",
> >         "port": 18081,
> >         "access-token": null,
> >         "restricted": true
> >     },
> >     "autosave": true,
> >     "donate-level": 1,
> >     "cpu": true,
> >     "opencl": true,
> >     "cuda": false,
> >     "pools": [
> >         {
> >             "url": "pool.supportxmr.com:443",
> >             "user": "ADDRESS",
> >             "pass": "workername",
> >             "keepalive": true,
> >             "tls": true
> >         }
> >     ]
> > }
> > ```
> 
> try to set **`"coin": "monero"`** inside pool key:
> 
> ```
> "pools": [
>     {
>         "url": "pool.supportxmr.com:443",
>         "user": "ADDRESS",
>         "pass": "workername",
>         "coin": "monero",
>         "keepalive": true,
>         "tls": true
>     }
> ]
> ```

Thx a lot! It helped.

## JoshTofu | 2024-01-07T07:18:46+00:00
hmm... I'm a complete newb to this stuff, but I can't join any mining pools. here's my config right now:

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
            "algo": cn/r,
            "coin": monero,
            "url": "donate.v2.xmrig.com:3333",
            "user": "48umZax9EVmFkP9VmDxV8cjk59FRoPoq4EaKFUSWRrZTc7kUogstVFDhkiBCJDqFQsgNKYKAoZZvtFNW7JvXuYexLkS33YM",
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

In my terminal it's saying " [2024-01-07 00:16:06.394]  net      xmr-us-east1.nanopool.org:10300 unknown algorithm, make sure you set "algo" or "coin" option
[2024-01-07 00:16:06.394]  net      xmr-us-east1.nanopool.org:10300 login error code: 6"

sorry if I sound like a dumbass, I just wanted to do this for fun.

## geekwilliams | 2024-01-07T08:53:00+00:00
> hmm... I'm a complete newb to this stuff, but I can't join any mining pools. here's my config right now:
> 
> 
> 
> {
> 
>     "api": {
> 
>         "id": null,
> 
>         "worker-id": null
> 
>     },
> 
>     "http": {
> 
>         "enabled": false,
> 
>         "host": "127.0.0.1",
> 
>         "port": 0,
> 
>         "access-token": null,
> 
>         "restricted": true
> 
>     },
> 
>     "autosave": true,
> 
>     "background": false,
> 
>     "colors": true,
> 
>     "title": true,
> 
>     "randomx": {
> 
>         "init": -1,
> 
>         "init-avx2": -1,
> 
>         "mode": "auto",
> 
>         "1gb-pages": false,
> 
>         "rdmsr": true,
> 
>         "wrmsr": true,
> 
>         "cache_qos": false,
> 
>         "numa": true,
> 
>         "scratchpad_prefetch_mode": 1
> 
>     },
> 
>     "cpu": {
> 
>         "enabled": true,
> 
>         "huge-pages": true,
> 
>         "huge-pages-jit": false,
> 
>         "hw-aes": null,
> 
>         "priority": null,
> 
>         "memory-pool": false,
> 
>         "yield": true,
> 
>         "max-threads-hint": 100,
> 
>         "asm": true,
> 
>         "argon2-impl": null,
> 
>         "cn/0": false,
> 
>         "cn-lite/0": false
> 
>     },
> 
>     "opencl": {
> 
>         "enabled": false,
> 
>         "cache": true,
> 
>         "loader": null,
> 
>         "platform": "AMD",
> 
>         "adl": true,
> 
>         "cn/0": false,
> 
>         "cn-lite/0": false
> 
>     },
> 
>     "cuda": {
> 
>         "enabled": false,
> 
>         "loader": null,
> 
>         "nvml": true,
> 
>         "cn/0": false,
> 
>         "cn-lite/0": false
> 
>     },
> 
>     "donate-level": 1,
> 
>     "donate-over-proxy": 1,
> 
>     "log-file": null,
> 
>     "pools": [
> 
>         {
> 
>             "algo": cn/r,
> 
>             "coin": monero,
> 
>             "url": "donate.v2.xmrig.com:3333",
> 
>             "user": "48umZax9EVmFkP9VmDxV8cjk59FRoPoq4EaKFUSWRrZTc7kUogstVFDhkiBCJDqFQsgNKYKAoZZvtFNW7JvXuYexLkS33YM",
> 
>             "pass": "x",
> 
>             "rig-id": null,
> 
>             "nicehash": false,
> 
>             "keepalive": false,
> 
>             "enabled": true,
> 
>             "tls": false,
> 
>             "tls-fingerprint": null,
> 
>             "daemon": false,
> 
>             "socks5": null,
> 
>             "self-select": null,
> 
>             "submit-to-origin": false
> 
>         }
> 
>     ],
> 
>     "print-time": 60,
> 
>     "health-print-time": 60,
> 
>     "dmi": true,
> 
>     "retries": 5,
> 
>     "retry-pause": 5,
> 
>     "syslog": false,
> 
>     "tls": {
> 
>         "enabled": false,
> 
>         "protocols": null,
> 
>         "cert": null,
> 
>         "cert_key": null,
> 
>         "ciphers": null,
> 
>         "ciphersuites": null,
> 
>         "dhparam": null
> 
>     },
> 
>     "dns": {
> 
>         "ipv6": false,
> 
>         "ttl": 30
> 
>     },
> 
>     "user-agent": null,
> 
>     "verbose": 0,
> 
>     "watch": true,
> 
>     "pause-on-battery": false,
> 
>     "pause-on-active": false
> 
> }
> 
> 
> 
> In my terminal it's saying " [2024-01-07 00:16:06.394]  net      xmr-us-east1.nanopool.org:10300 unknown algorithm, make sure you set "algo" or "coin" option
> 
> [2024-01-07 00:16:06.394]  net      xmr-us-east1.nanopool.org:10300 login error code: 6"
> 
> 
> 
> sorry if I sound like a dumbass, I just wanted to do this for fun.

Did you have a specific pool in mind you were trying to join? 

## JoshTofu | 2024-01-07T18:48:12+00:00
> > hmm... I'm a complete newb to this stuff, but I can't join any mining pools. here's my config right now:
> > {
> > ```
> > "api": {
> > 
> >     "id": null,
> > 
> >     "worker-id": null
> > 
> > },
> > 
> > "http": {
> > 
> >     "enabled": false,
> > 
> >     "host": "127.0.0.1",
> > 
> >     "port": 0,
> > 
> >     "access-token": null,
> > 
> >     "restricted": true
> > 
> > },
> > 
> > "autosave": true,
> > 
> > "background": false,
> > 
> > "colors": true,
> > 
> > "title": true,
> > 
> > "randomx": {
> > 
> >     "init": -1,
> > 
> >     "init-avx2": -1,
> > 
> >     "mode": "auto",
> > 
> >     "1gb-pages": false,
> > 
> >     "rdmsr": true,
> > 
> >     "wrmsr": true,
> > 
> >     "cache_qos": false,
> > 
> >     "numa": true,
> > 
> >     "scratchpad_prefetch_mode": 1
> > 
> > },
> > 
> > "cpu": {
> > 
> >     "enabled": true,
> > 
> >     "huge-pages": true,
> > 
> >     "huge-pages-jit": false,
> > 
> >     "hw-aes": null,
> > 
> >     "priority": null,
> > 
> >     "memory-pool": false,
> > 
> >     "yield": true,
> > 
> >     "max-threads-hint": 100,
> > 
> >     "asm": true,
> > 
> >     "argon2-impl": null,
> > 
> >     "cn/0": false,
> > 
> >     "cn-lite/0": false
> > 
> > },
> > 
> > "opencl": {
> > 
> >     "enabled": false,
> > 
> >     "cache": true,
> > 
> >     "loader": null,
> > 
> >     "platform": "AMD",
> > 
> >     "adl": true,
> > 
> >     "cn/0": false,
> > 
> >     "cn-lite/0": false
> > 
> > },
> > 
> > "cuda": {
> > 
> >     "enabled": false,
> > 
> >     "loader": null,
> > 
> >     "nvml": true,
> > 
> >     "cn/0": false,
> > 
> >     "cn-lite/0": false
> > 
> > },
> > 
> > "donate-level": 1,
> > 
> > "donate-over-proxy": 1,
> > 
> > "log-file": null,
> > 
> > "pools": [
> > 
> >     {
> > 
> >         "algo": cn/r,
> > 
> >         "coin": monero,
> > 
> >         "url": "donate.v2.xmrig.com:3333",
> > 
> >         "user": "48umZax9EVmFkP9VmDxV8cjk59FRoPoq4EaKFUSWRrZTc7kUogstVFDhkiBCJDqFQsgNKYKAoZZvtFNW7JvXuYexLkS33YM",
> > 
> >         "pass": "x",
> > 
> >         "rig-id": null,
> > 
> >         "nicehash": false,
> > 
> >         "keepalive": false,
> > 
> >         "enabled": true,
> > 
> >         "tls": false,
> > 
> >         "tls-fingerprint": null,
> > 
> >         "daemon": false,
> > 
> >         "socks5": null,
> > 
> >         "self-select": null,
> > 
> >         "submit-to-origin": false
> > 
> >     }
> > 
> > ],
> > 
> > "print-time": 60,
> > 
> > "health-print-time": 60,
> > 
> > "dmi": true,
> > 
> > "retries": 5,
> > 
> > "retry-pause": 5,
> > 
> > "syslog": false,
> > 
> > "tls": {
> > 
> >     "enabled": false,
> > 
> >     "protocols": null,
> > 
> >     "cert": null,
> > 
> >     "cert_key": null,
> > 
> >     "ciphers": null,
> > 
> >     "ciphersuites": null,
> > 
> >     "dhparam": null
> > 
> > },
> > 
> > "dns": {
> > 
> >     "ipv6": false,
> > 
> >     "ttl": 30
> > 
> > },
> > 
> > "user-agent": null,
> > 
> > "verbose": 0,
> > 
> > "watch": true,
> > 
> > "pause-on-battery": false,
> > 
> > "pause-on-active": false
> > ```
> > 
> > 
> >     
> >       
> >     
> > 
> >       
> >     
> > 
> >     
> >   
> > }
> > In my terminal it's saying " [2024-01-07 00:16:06.394]  net      xmr-us-east1.nanopool.org:10300 unknown algorithm, make sure you set "algo" or "coin" option
> > [2024-01-07 00:16:06.394]  net      xmr-us-east1.nanopool.org:10300 login error code: 6"
> > sorry if I sound like a dumbass, I just wanted to do this for fun.
> 
> Did you have a specific pool in mind you were trying to join?

yeah, https://p2pool.io/#pool    https://pool.kryptex.com/en/xmr and https://xmr.nanopool.org/ I am able to join https://moneroocean.stream/ though.  maybe I put in the wrong command? or the link wrong? heres what I ran:  (working one - /xmrig -o gulf.moneroocean.stream:10128 -u 48umZax9EVmFkP9VmDxV8cjk59FRoPoq4EaKFUSWRrZTc7kUogstVFDhkiBCJDqFQsgNKYKAoZZvtFNW7JvXuYexLkS33YM -p OMEN162022) (ones that I can;t join - ./xmrig -o xmr-us-west1.nanopool.org:10300 -u 48umZax9EVmFkP9VmDxV8cjk59FRoPoq4EaKFUSWRrZTc7kUogstVFDhkiBCJDqFQsgNKYKAoZZvtFNW7JvXuYexLkS33YM -p OMEN162022) thank you!

## geekwilliams | 2024-01-07T21:38:18+00:00
For the nanopool address try adding -a rx/0  to the command and see if it works. It looks like nanopool doesn't have algo negotiation

## geekwilliams | 2024-01-07T21:44:15+00:00
The kryptex pool xmrig command looks like this: 

xmrig --coin XMR --url  
"xmr.kryptex.network:7777" --user 
"WALLET_ADDRESS/WORKER_NAME"

If you're just starting out, I'd recommend trying moneroocean or the other two we've mentioned. P2pool requires a bit more advanced setup, which is still great for learning, but harder to start out with. They have a video guide [here](https://www.youtube.com/watch?v=NbxbRu-2GWI) to get started. 

# Action History
- Created by: youssef2019am | 2019-09-30T20:58:13+00:00
- Closed at: 2019-10-08T03:07:16+00:00
