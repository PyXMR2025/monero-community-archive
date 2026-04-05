---
title: v5.2.0 - send buffer overflow
source_url: https://github.com/xmrig/xmrig/issues/1421
author: trasherdk
assignees: []
labels:
- bug
created_at: '2019-12-15T11:53:23+00:00'
updated_at: '2019-12-17T07:02:33+00:00'
type: issue
status: closed
closed_at: '2019-12-17T07:02:33+00:00'
---

# Original Description
While mining `RandomX` against [monero-pool](https://github.com/jtgrassie/monero-pool), with stratum `self-select` active.

[pool](http://ghost-m1.fumlersoft.dk:8002)
[pool-ui](http://ghost-m1.fumlersoft.dk:8003/)

I see a bunch of `[localhost:8002] send failed: "send buffer overflow: 2446 > 2046"`
This is in connection with a large `block-template`, in this case 1831 chars.

The hardware:
```
 * ABOUT        XMRig/5.2.0 gcc/5.5.0
 * LIBS         libuv/1.23.2 OpenSSL/1.0.2t hwloc/2.1.0rc2-git
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Xeon(R) CPU E3-1230 v5 @ 3.40GHz (1) x64 AES
                L2:1.0 MB L3:32.0 MB 4C/4T NUMA:1
 * MEMORY       3.0/7.8 GB (38%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      localhost:8002 coin monero self-select localhost:18081
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2019-12-15 05:40:35.705]  net  use pool localhost:8002  127.0.0.1
[2019-12-15 05:40:35.711]  net  new job from localhost:8002 diff 50000 algo rx/0 height 1989167
[2019-12-15 05:40:35.715]  rx   cannot set MSR 0x01a4 to 0x0006
[2019-12-15 05:40:35.715]  rx   init dataset algo rx/0 (4 threads) seed be68fd3de3de1e2e...
[2019-12-15 05:40:35.715]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2019-12-15 05:40:43.270]  rx   dataset ready (7555 ms)
[2019-12-15 05:40:43.270]  cpu  use profile  rx  (4 threads) scratchpad 2048 KB
[2019-12-15 05:40:43.331]  cpu  READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (61 ms)
```
Here's a typical section of the log:
```
[2019-12-15 11:37:08.033]  cpu  accepted (209/0) diff 131828 (28 ms)
[2019-12-15 11:37:08.917] speed 10s/60s/15m 1147.1 1130.0 1132.6 H/s max 1163.6 H/s
[2019-12-15 11:37:38.955] speed 10s/60s/15m 1153.5 1135.8 1132.9 H/s max 1163.6 H/s
[2019-12-15 11:38:09.000] speed 10s/60s/15m 1100.6 1134.7 1132.3 H/s max 1163.6 H/s
[2019-12-15 11:38:39.045] speed 10s/60s/15m 1132.5 1127.5 1133.7 H/s max 1163.6 H/s
[2019-12-15 11:38:42.783] [localhost:8002] send failed: "send buffer overflow: 2190 > 2046"
[2019-12-15 11:38:42.783]  net  no active pools, stop mining
[2019-12-15 11:38:48.409]  net  use pool localhost:8002  127.0.0.1
[2019-12-15 11:38:48.420] [localhost:8002] send failed: "send buffer overflow: 2190 > 2046"
[2019-12-15 11:38:48.420]  net  no active pools, stop mining
[2019-12-15 11:38:54.412]  net  use pool localhost:8002  127.0.0.1
[2019-12-15 11:38:54.432] [localhost:8002] send failed: "send buffer overflow: 2254 > 2046"
[2019-12-15 11:38:54.432]  net  no active pools, stop mining
[2019-12-15 11:39:00.416]  net  use pool localhost:8002  127.0.0.1
[2019-12-15 11:39:00.437] [localhost:8002] send failed: "send buffer overflow: 2254 > 2046"
[2019-12-15 11:39:00.437]  net  no active pools, stop mining
[2019-12-15 11:39:06.425]  net  use pool localhost:8002  127.0.0.1
[2019-12-15 11:39:06.445] [localhost:8002] send failed: "send buffer overflow: 2254 > 2046"
[2019-12-15 11:39:06.445]  net  no active pools, stop mining
[2019-12-15 11:39:09.085] speed 10s/60s/15m n/a 1134.4 1133.4 H/s max 1163.6 H/s
[2019-12-15 11:39:12.430]  net  use pool localhost:8002  127.0.0.1
[2019-12-15 11:39:12.436]  net  new job from localhost:8002 diff 50000 algo rx/0 height 1989329
[2019-12-15 11:39:25.615]  net  new job from localhost:8002 diff 50000 algo rx/0 height 1989330
[2019-12-15 11:39:39.134] speed 10s/60s/15m 1118.0 568.6 1095.7 H/s max 1163.6 H/s
[2019-12-15 11:40:09.170] speed 10s/60s/15m 1036.8 1116.7 1094.3 H/s max 1163.6 H/s
[2019-12-15 11:40:25.398]  net  new job from localhost:8002 diff 50000 algo rx/0 height 1989331
[2019-12-15 11:40:38.952]  cpu  accepted (210/0) diff 50000 (51 ms)
```
The corresponding `monero-pool` log:
```
2019-12-15 11:38:42 INFO  src/pool.c:1688: Fetching new block template
2019-12-15 11:38:42 TRACE src/pool.c:1435: Payload: {"jsonrpc":"2.0","id":"0","method":"get_block_template","params":{"wallet_address":"44ch1jLCFmuHpsq6QMCWxMXMGbMdrEF9AHiMrzqBjPc5WyToE2eoXqEJZV7GpVMPxxCxBewpG9FCjY1riMccS6f8Fq6v5iV","reserve_size":17}}
2019-12-15 11:38:42 TRACE src/pool.c:1435: Payload: {"jsonrpc":"2.0","id":"0","method":"get_block_headers_range","params":{"start_height":1989258,"end_height":1989267}}
2019-12-15 11:38:42 TRACE src/pool.c:1513: Got block template: 
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "blockhashing_blob": "0c0cb29ad8ef058f0109787e4aeabdfb790d0476336d659c9b48a4d3826a13860ba28cdb3f5beb0000000002647756cdb4980eda0b4648d53f15e5e76575d73aa7eeee9fa7bf190af1818219",
    "blocktemplate_blob": "0c0cb29ad8ef058f0109787e4aeabdfb790d0476336d659c9b48a4d3826a13860ba28cdb3f5beb00000000028cb67901ffd0b57901a0c6a1bacf3c02a3b596062e6e65d072ace5504d7e9fb94f588c890ef67a06ae545ca6d7bfb5ae34019d859bd68adacf8194609e113dcc524dc856bc44d471a2eb5dad44967f148969021100000000000000000000000000000000000018cc76d80d4d4a07419474b2b50f15d7a89ea2679fc0bcced107fae8f7f48100209cbf10b04e3395c0b80d80cc4ca3cefc7c009d28b7ec730e850686076fbce7e1c5f3b546ef8c85680d1a0b40e97774003ff42537cd3eb6a3aeb998a5950bf1f59662edbddb3273d4f1399ff656204c2c7fe630bdb6df87e71409f9ae0b805cce133608780094ae86637ab13be769054e2063433a618dc5e9c15653ac6075b70058f14dfa1f38171aab68d29e6f246da67eeebbd2fb45e2a6f00053847e6362e96d88dbebf4e7d90a0c153a7bc0579c86609f068ae44f23d057d2c595ba736885952967a0f8d10696d103ac977c4dc35d55431f2a8d84b21845e69b6a04ffe576d2d831ad02c8ea248d03d1fcd318b363521bf3298e0725d623abdec989dfbd62fa03760bc0a45f01c5b482e17d92a8909c11bce2d66ff5f1c7441a919a5769993cfa01f821a6eb825ee05a7efed7af27044ba2a6c3ac339e86ee5d45659030457c95bc36cba0ce3613267b84266ea4a1a14840348bf5ac38e9c229d3981da2b610d13391be8742ba6faeac87b7e3a48c287345bcbd8028b8c567013105dc2df19aaba25997ea52388ed2eb00e821cbc998a777d7eaa33099d4bc03ac61a2d85e7497106916722bb0a825e9c6e4580e02badbdc1be1be3ceb29eccf1a6d5a50f92863159ab8ea318fd1e136dd2459a4da0928d5a5189fd5c84be56a6305ed5685316f24abc5d29077138080444395cd953562f5639ae03df3e39bf31f5c4c42a3b47b91f0cbfc547100a270ab61b18a2026eafeb1d0ad00fbe2dd0c46a56186689b6fc6ccc5e83bd8cf37813ffc77237e219ea0b479bd8a55a64fcbb58f73e473eed5a7287df607a38e65f56831d64e180772ea3593148ba11ddc5e1b8b9de14fdf1ecc5e1e196e8a6dc5008f4fd2b192a36538e1611785f2d65b9b090fd2848fc16ca7b640194deff7a9ac2e099fc28aa9c9ab2f6fb6643e022a6c04061376bf5410d0f7c45fb9823d6c330f129ed2bc27136e1f1f6db0a339f182b2950976256535f4a2edaaa324f6da3917613d5dfe3eb44dd9b35db333076e5be6747cc03e",
    "difficulty": 109482361561,
    "difficulty_top64": 0,
    "expected_reward": 2082912887584,
    "height": 1989328,
    "next_seed_hash": "",
    "prev_hash": "8f0109787e4aeabdfb790d0476336d659c9b48a4d3826a13860ba28cdb3f5beb",
    "reserved_offset": 128,
    "seed_hash": "be68fd3de3de1e2ed52e3b8f6be5ef8c6565a88bd3d88c936425b63696b7eaeb",
    "seed_height": 1988608,
    "status": "OK",
    "untrusted": false,
    "wide_difficulty": "0x197da842d9"
  }
}
2019-12-15 11:38:42 TRACE src/pool.c:838: Recycle block template at height: 1989324
2019-12-15 11:38:42 TRACE src/pool.c:1282: Variant: 6
2019-12-15 11:38:42 DEBUG src/pool.c:859: Client 87e1282b66054cf3b8602c875dfef0d6 target now 140703
2019-12-15 11:38:42 TRACE src/pool.c:1146: Client job: {"jsonrpc":"2.0","method":"job","params":{"id":"87e1282b66054cf3b8602c875dfef0d6","job_id":"743fd9d2b50b40338ccc8a31eb4f3ae3","target":"3d770000","extra_nonce":"b500000081b4ba43", "pool_wallet":"44ch1jLCFmuHpsq6QMCWxMXMGbMdrEF9AHiMrzqBjPc5WyToE2eoXqEJZV7GpVMPxxCxBewpG9FCjY1riMccS6f8Fq6v5iV","seed_hash":"","next_seed_hash":""}}

2019-12-15 11:38:42 DEBUG src/pool.c:715: Processing blocks
2019-12-15 11:38:42 TRACE src/pool.c:743: Processing block at height 1989258
2019-12-15 11:38:42 TRACE src/pool.c:753: No stored block at height 1989258
...
2019-12-15 11:38:42 TRACE src/pool.c:743: Processing block at height 1989267
2019-12-15 11:38:42 TRACE src/pool.c:753: No stored block at height 1989267
2019-12-15 11:38:42 DEBUG src/pool.c:2602: Client disconnected. Removing.
2019-12-15 11:38:48 INFO  src/pool.c:2000: New client connected
2019-12-15 11:38:48 TRACE src/pool.c:2087: Client login for mode: self-select
2019-12-15 11:38:48 DEBUG src/pool.c:859: Client 94221feda86545edb729a0daba62e8c3 target now 50000
2019-12-15 11:38:48 TRACE src/pool.c:1146: Client job: {"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"94221feda86545edb729a0daba62e8c3","job":{"job_id":"5339e3acdd994ceea6cb689f2d69595f","target":"8b4f0100","extra_nonce":"b600000081b4ba43", "pool_wallet":"44ch1jLCFmuHpsq6QMCWxMXMGbMdrEF9AHiMrzqBjPc5WyToE2eoXqEJZV7GpVMPxxCxBewpG9FCjY1riMccS6f8Fq6v5iV","seed_hash":"","next_seed_hash":""},"status":"OK"}}

2019-12-15 11:38:48 DEBUG src/pool.c:2602: Client disconnected. Removing.
2019-12-15 11:38:54 INFO  src/pool.c:2000: New client connected
2019-12-15 11:38:54 TRACE src/pool.c:2087: Client login for mode: self-select
2019-12-15 11:38:54 DEBUG src/pool.c:859: Client 95d68a0b1aba40f9b77163500938d4a3 target now 50000
2019-12-15 11:38:54 TRACE src/pool.c:1146: Client job: {"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"95d68a0b1aba40f9b77163500938d4a3","job":{"job_id":"4e90966d2c294fe59c5d71f3a0e65907","target":"8b4f0100","extra_nonce":"b700000081b4ba43", "pool_wallet":"44ch1jLCFmuHpsq6QMCWxMXMGbMdrEF9AHiMrzqBjPc5WyToE2eoXqEJZV7GpVMPxxCxBewpG9FCjY1riMccS6f8Fq6v5iV","seed_hash":"","next_seed_hash":""},"status":"OK"}}

2019-12-15 11:38:54 DEBUG src/pool.c:2602: Client disconnected. Removing.
```


# Discussion History
## xmrig | 2019-12-15T11:57:52+00:00
Already fixed #1418 and fix included to v5.3.0.
Thank you.

## trasherdk | 2019-12-15T12:04:58+00:00
Cool. While I was setting up a clone, looking at the source code, jtgrassie made the PR :^)

## xmrig | 2019-12-16T07:10:48+00:00
Fixed (again) in dev branch.
Thank you.

## trasherdk | 2019-12-17T07:02:33+00:00
So far, no problems running the `dev` branch version.

# Action History
- Created by: trasherdk | 2019-12-15T11:53:23+00:00
- Closed at: 2019-12-17T07:02:33+00:00
