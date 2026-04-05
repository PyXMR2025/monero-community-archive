---
title: Job refused for MSR secor upgrade
source_url: https://github.com/xmrig/xmrig/issues/913
author: gnock
assignees: []
labels:
- bug
created_at: '2019-01-18T12:23:50+00:00'
updated_at: '2019-01-19T17:43:08+00:00'
type: issue
status: closed
closed_at: '2019-01-19T17:43:08+00:00'
---

# Original Description
Hi,

The core team (I'm part of it) updated the dependencies and a testpool is available at testnet.masaricoin.com for the next Masari protocol upgrade.
I used it to test the new version but the new protocol included a modification in the PoW blob (it now includes the uncle hash at the end or 0000...). 

Example of a new job:
```
{"blob":"080890e686e205cd922e0f103343fd31a7e257a68f95a782c4cf891daedce3ecf28e842e3b277800000000b425d70df725a5484d24730993c8a53ae3f3520eac8a74986112c501e34ca05e010000000000000000000000000000000000000000000000000000000000000000","job_id":"15NCpG6pOIwc5b+2nWdJM4PLof1I","target":"37894100","id":"6e315a64-90c1-4974-9ade-130ff4b95ff9"}
```

That modification makes the job to be refused (and unable to connect to). The problem is located at this position : https://github.com/xmrig/xmrig/blob/a1f19305f402f62dfc7d26961591d5ae0947fc56/src/common/net/Job.cpp#L112

Also, I wasn't able to mine correctly (no problems with xtl-stak, fork of xmr-stak) by selecting as algo "cn/half", I may have forget a parameter (sorry I'm not a miner).

You can use the testnet address 6dRJk2wif2c1nGWYEkd1k49D88SEg49E95j9YE4jb8SyAiB6aTwRBqcN2jndBB19zaAr9ZNrWGjKgLa6dJcL7EXFKAWhSFw to mine on the pool mentionned above (port 3333).

The new variant is 8 if it's needed.

Thanks in advance
Gnock

# Discussion History
## xmrig | 2019-01-18T14:51:20+00:00
I increase max blob size to 128, not sure it enough in future or not, current blob size is 108 bytes it may bigger of not?

Minimum config:
```json
{
    "algo": "cryptonight",
    "pools": [
        {
            "url": "testnet.masaricoin.com:3333",
            "user": "6dRJk2wif2c1nGWYEkd1k49D88SEg49E95j9YE4jb8SyAiB6aTwRBqcN2jndBB19zaAr9ZNrWGjKgLa6dJcL7EXFKAWhSFw",
            "pass": "x",
            "variant": "msr"
        }
    ]
}
```

For Masari better use variant `msr` it will be automatically changed to `cn/half` when blob version reached 8
Thank you.

## gnock | 2019-01-18T16:21:51+00:00
The blob size is not supposed to increase "for now" (so in the current protocol version). It may in a future but, well, will see in due time ^^.

Thanks you for your fast correction, i just tried and it works fine !


## xmrig | 2019-01-19T17:43:08+00:00
Fixed in v2.9.4 release.
https://github.com/xmrig/xmrig/releases/tag/v2.9.4
https://github.com/xmrig/xmrig-amd/releases/tag/v2.9.4
https://github.com/xmrig/xmrig-nvidia/releases/tag/v2.9.4
https://github.com/xmrig/xmrig-proxy/releases/tag/v2.9.4

# Action History
- Created by: gnock | 2019-01-18T12:23:50+00:00
- Closed at: 2019-01-19T17:43:08+00:00
