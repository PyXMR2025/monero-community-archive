---
title: Support for BitMinti (RandomX based CPU coin)
source_url: https://github.com/xmrig/xmrig/issues/3751
author: cgebitcoin
assignees: []
labels: []
created_at: '2026-01-05T22:35:38+00:00'
updated_at: '2026-01-07T12:15:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello, I am the developer of BitMinti, https://github.com/cgebitcoin/bitminti. 

It is a Bitcoin fork using RandomX for PoW. We would like to ensure XMRig users can mine BitMinti easily. The algorithm is standard RandomX. RPC compatible with Bitcoin Core.

But when we run xmrig, it gives the error:

 ./xmrig -c config.json
 * ABOUT        XMRig/6.25.0 gcc/13.3.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.48.0 OpenSSL/3.0.13 hwloc/2.10.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) Platinum 8488C (1) 64-bit AES VM
                L2:2.0 MB L3:105.0 MB 1C/2T NUMA:1
 * MEMORY       4.8/7.6 GB (63%)
 * MOTHERBOARD  Amazon EC2 - m7i-flex.large
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      127.0.0.1:13338 algo rx/0 self-select btc31qprt68c9al9kqrr83u5756csuje2vf4xqn99k33
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed
[2026-01-05 22:32:16.622]  net      127.0.0.1:13338 JSON decode failed: "Missing a name for object member."

Our config:

{
    "autosave": false,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "bitcoin",
            "url": "127.0.0.1:13336",
            "user": "admin",
            "pass": "admin",
            "daemon": true,
            "daemon-poll-interval": 1000,
            "self-select": "btc31qprt68c9al9kqrr83u5756csuje2vf4xqn99k33",
            "tls": false,
            "keepalive": true
        }
    ]
}

Could you able to help that xmrig also supports BitMinti?
Regards.
Gurkan


# Discussion History
## SChernykh | 2026-01-05T23:26:07+00:00
If it is standard RandomX, XMRig already supports it. The problem is somewhere on your side, probably in the JSON encoding. Also, your pool config is wrong (self-select option is definitely wrong). Read https://xmrig.com/docs/miner/config/pool

## cgebitcoin | 2026-01-06T03:30:48+00:00
I updated my config as 

{
    "autosave": true,
    "donate-level": 5,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "algo": "rx/0",
            "url": "127.0.0.1:13337",
            "user": "btc31qprt68c9al9kqrr83u5756csuje2vf4xqn99k33",
            "daemon": true
        },
        {
            "coin": null,
            "algo": "rx/0",
            "url": "127.0.0.1:13336",
            "user": "admin",
            "pass": "admin",
            "tls": false,
            "keepalive": true,
            "nicehash": false
        }
    ]
}

and run

`./xmrig --donate-level 5 -o 127.0.0.1:13337 -u btc31qa434ga0wxvynymcekks2cvays4nkgzjxvr2207 -a rx/0 --daemon -o 127.0.0.1:13336 -u admin -p admin -k -a rx/0`

ERRORS:

[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 JSON decode failed
[2026-01-06 03:28:55.201]  net      127.0.0.1:13336 read error: "end of file"

## SChernykh | 2026-01-06T09:36:26+00:00
Are you sure that your node sends JSON at all? You need to log all the traffic to see what it actually sends to XMRig. Or maybe you can try to set `tls` to `true` first.

## cgebitcoin | 2026-01-07T06:49:44+00:00
Actually BitMinti is a Bitcoin based coin that we only change PoW to Randomx . So Does XMrig support BitCoin based coins?

## SChernykh | 2026-01-07T12:15:06+00:00
No, it doesn't. Your node needs to use the version of Stratum protocol that is supported by XMRig.

# Action History
- Created by: cgebitcoin | 2026-01-05T22:35:38+00:00
