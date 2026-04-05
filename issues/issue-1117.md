---
title: v3 and minexmr.com algo negotiation
source_url: https://github.com/xmrig/xmrig/issues/1117
author: SlavisaBakic
assignees: []
labels:
- question
created_at: '2019-08-16T09:00:09+00:00'
updated_at: '2019-08-22T13:05:13+00:00'
type: issue
status: closed
closed_at: '2019-08-19T16:43:23+00:00'
---

# Original Description
With XMRig v2.14.4 and prior I dind't have to specify algorithm in config file because "variant": -1 was enough. Now with XMRig I have to specify "algo": "cn/r" because otherwise I would get:

```
[pool.minexmr.com:4444] Unknown/unsupported algorithm "(null)" detected, reconnect
[2019-08-16 10:53:39.869] [pool.minexmr.com:4444] login error code: 6
```

Is this pool problem, XMRig v3 bug or both cause problem with algorithm negotiation?


# Discussion History
## k0ste | 2019-08-16T09:08:47+00:00
```json
// xmrig.conf
// Ansible managed: /home/napaster/leko-ansible/roles/xmrig/templates/xmrig.j2 modified on 2019-08-15 11:52:41 by napaster on novadeploy
// Do not edit manually

{
  "algo": "cryptonight",
  "syslog": true,
  "watch": false,
  "autosave": false,
  "threads": 1,
  "api": {
    "port": 8088,
    "access-token": null,
    "worker-id": null,
    "ipv6": false,
  },
  "pools": [
    {
      "keepalive": true,
      "url": "monero.napaster.name:14433",
      "pass": "x",
      "user": "<addr>",
      "variant": "-1",
      "tls": true,
    }
  ]
}
```

Also this is not detected via `dry-run`!

```shell
$ ./xmrig --dry-run -c xmrig.conf 
 * ABOUT        XMRig/3.0.0 gcc/9.1.0
 * LIBS         libuv/1.30.1 OpenSSL/1.1.1c hwloc/1.11.12
 * CPU          Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz (1) x64 AES
                L2:1.0 MB L3:8.0 MB 4C/4T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      monero.napaster.name:14433 algo auto
 * COMMANDS     hashrate, pause, resume
[2019-08-16 16:06:55.588] OK
$ echo $?
0
```

## xmrig | 2019-08-16T15:21:52+00:00
minexmr.com don't support algorithm negotiation, so you must specify this option for each pool without it. Not specified algo option is still valid configuration, `--dry-run` not perform network connections. Requred part of algorithm negotiation on pool side is very simple, just single field `"algo":"cn/r",` in each job object.

v3 don't have global option for algorithm and no default algorithm and no variant.

@k0ste you config is outdated.

## k0ste | 2019-08-17T05:56:31+00:00
@xmrig, can you write migration guide for configuration 2.14.4 -> 3.0.0? It will be help to rewrite xmrig deployments tools for new version. Thanks.

## xmrig | 2019-08-17T13:53:06+00:00
- Option `threads` replaced to `cpu` https://github.com/xmrig/xmrig/blob/master/doc/CPU.md
- Options `av`, `safe` and `max-cpu-usage` removed.
- API options changed https://github.com/xmrig/xmrig/issues/1007
- Variant option replaced to `algo`, global option `algo` removed.
- Some new options added, please check changelog and config example https://github.com/xmrig/xmrig/blob/master/src/config.json

Minimum valid config looks like:
```json
{
    "pools": [
        {
            "url": "randomx-benchmark.xmrig.com:7777"
        }
    ]
}
```

## k0ste | 2019-08-20T10:02:07+00:00
@xmrig 

What possible values for `donate-over-proxy`?
What mean `daemon` option in `pools`?
How I can use old behaviour, like: "I mine monero, xmrig please configure my algo when connected to pool"? Like this in xmrig 2:

```
{
  "algo": "cryptonight",
  "pools": [
    {
      "variant": "-1"
    }
  ]
}
```

Thanks.

## xmrig | 2019-08-20T15:08:00+00:00
Changelog contains links to corresponding issues or pull requests:
* `donate-over-proxy` https://github.com/xmrig/xmrig-proxy/issues/314
* `daemon` https://github.com/xmrig/xmrig/pull/1010#issuecomment-482632107

About last question best option for everyone: if pool supports algorithm negotiation, minimum required part for pools is very simple `"algo":"cn/r",` added to each job object, in that case algo option on miner side not required. Many pools already support it (exect some biggest) and other miners with algorithm switching.

Another option might be some option `coin` or something like that with mapping between block version and algorithm, but it no implemented right now.

Old way will be break anyway, likely next algorithm will be RandomX and this is not cryptonight.

## k0ste | 2019-08-22T12:10:58+00:00
@xmrig 
And about NUMA support, #1077 tells:

> introduce NUMA support for RandomX **and other algorithms**

But in example config.json `randomx` object not in `cpu` object. So, another algorithms is not used this option and relevant place for `numa` in `randomx` object in root of conf (e.g. is not a feature of cpu profile)?

## xmrig | 2019-08-22T13:05:13+00:00
NUMA support (threads and memory binding to proper cores/nodes) always enabled for all algorithms including RandomX if miner built with hwloc support. There is no option for disable it.

`numa` option in `randomx` object controls only RandomX specific dataset allocation, if enabled miner will use 2336 MB on each NUMA node, otherwise this memory will allocated only once.

# Action History
- Created by: SlavisaBakic | 2019-08-16T09:00:09+00:00
- Closed at: 2019-08-19T16:43:23+00:00
