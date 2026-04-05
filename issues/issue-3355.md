---
title: 'Solo Mining Zephyr Gives Error: job error: "Invalid block template received
  from daemon.'
source_url: https://github.com/xmrig/xmrig/issues/3355
author: downystreet
assignees: []
labels:
- bug
created_at: '2023-11-14T03:27:45+00:00'
updated_at: '2023-12-04T07:01:20+00:00'
type: issue
status: closed
closed_at: '2023-11-23T15:27:21+00:00'
---

# Original Description
**Describe the bug**
Starting xmrig with "algo": "rx/0", "coin": "Zephyr", and "Daemon": True in the config.json file gives error job error: "Invalid block template received from daemon

**Expected behavior**
xmrig should start solo mining zephyr from daemon

xmrig version: 6.20.0
Tried with zephyr protocol version 1.0.3 and 1.0.4.


# Discussion History
## SChernykh | 2023-11-14T12:15:34+00:00
#3356 should fix it.

## Anaphylaxis | 2023-11-15T06:13:05+00:00
same error on 6.20.1-dev
`24.199.101.125:17767 job error: "Invalid block template received from daemon."` This is remote-node.zephyrprotocol.com
```
.\xmrig.exe --version
XMRig 6.20.1-dev
 built on Nov 15 2023 with MSVC 2022
 features: 64-bit AES

libuv/1.44.2
OpenSSL/1.1.1s
hwloc/2.9.0
```

## SChernykh | 2023-11-15T07:52:04+00:00
It works with local node. I wouldn't recommend using remote nodes for solo mining, they can be under high load.

Edit: remote node creates miner reward transaction with 3 outputs instead of 2, and XMRig thinks it's invalid. 3rd output is probably the fee taken by that remote node. I'll fix it, but I still recommend to use your own node.

## Anaphylaxis | 2023-11-15T13:09:03+00:00
I compiled zephyrd from github and ran that on my local server, I got the same error after bootstrap.
[Osiris v1.0.4](https://github.com/ZephyrProtocol/zephyr/releases/tag/v1.0.4)

## SChernykh | 2023-11-15T15:19:09+00:00
> remote node creates miner reward transaction with 3 outputs instead of 2, and XMRig thinks it's invalid. 3rd output is probably the fee taken by that remote node. I'll fix it, but I still recommend to use your own node.

#3358 should fix it.

## Anaphylaxis | 2023-11-15T20:10:06+00:00
> > remote node creates miner reward transaction with 3 outputs instead of 2, and XMRig thinks it's invalid. 3rd output is probably the fee taken by that remote node. I'll fix it, but I still recommend to use your own node.
> 
> #3358 should fix it.

sorry, I still receive `job error: "Invalid block template received from daemon."` with both remote-node.zephyrprotocol.com and my own node using zephyrd 1.0.4 using this patch.
There is no local node on Windows afaik. May install cryptonote-pool and create a 0% pool for myself

## SChernykh | 2023-11-15T20:36:27+00:00
@Anaphylaxis I've been mining for 20 minutes and it didn't give any errors: https://paste.debian.net/hidden/4ef29c32/
Zephyr network mined multiple blocks with 3 outputs in the miner tx during that time. I can't reproduce your issue anymore - maybe you're just not using the latest code.

## Anaphylaxis | 2023-11-15T20:52:50+00:00
@SChernykh strange, i cloned again, checked out to dev (Your branch is up to date with 'origin/dev'), built again, and same error with both nodes. 
https://paste.debian.net/hidden/c2897054/

## Anaphylaxis | 2023-11-15T21:14:11+00:00
It works with "--coin Zephyr". It does not work when I specify -a rx/0. Perhaps rx/0 is monero only and coin is mandatory?
Either way I'll keep using --coin from now. Thank you for your persistence and the fix

## rrboston39 | 2023-11-23T16:16:52+00:00
i dont know how?


On Thu, Nov 23, 2023, 11:28 PM xmrig ***@***.***> wrote:

> Closed #3355 <https://github.com/xmrig/xmrig/issues/3355> as completed.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3355#event-11048961653>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ASIGGVQUS7RWGGAK25GJHGLYF5TQPAVCNFSM6AAAAAA7KEJI3CVHI2DSMVQWIX3LMV45UABCJFZXG5LFIV3GK3TUJZXXI2LGNFRWC5DJN5XDWMJRGA2DQOJWGE3DKMY>
> .
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


## TIRTAGT | 2023-12-04T02:19:18+00:00
> It works with "--coin Zephyr". It does not work when I specify -a rx/0. Perhaps rx/0 is monero only and coin is mandatory? Either way I'll keep using --coin from now. Thank you for your persistence and the fix

@Anaphylaxis Because [#3558](https://github.com/SChernykh/xmrig/blob/0b59b7eb430fb843bbc37dced8f14625d91057f3/src/base/tools/cryptonote/BlockTemplate.cpp#L228-L232) implementation applied the multi output ignore only if the coin is ZEPHYR.

## Anaphylaxis | 2023-12-04T03:01:03+00:00
> > It works with "--coin Zephyr". It does not work when I specify -a rx/0. Perhaps rx/0 is monero only and coin is mandatory? Either way I'll keep using --coin from now. Thank you for your persistence and the fix
> 
> @Anaphylaxis Because [#3558](https://github.com/SChernykh/xmrig/blob/0b59b7eb430fb843bbc37dced8f14625d91057f3/src/base/tools/cryptonote/BlockTemplate.cpp#L228-L232) implementation applied the multi output ignore only if the coin is ZEPHYR.

I understand. This feels like an oversight/issue since pool mining works fine with rx/0

## SChernykh | 2023-12-04T07:01:19+00:00
Pool mining leaves this job to the pool, and XMRig just receives the standard block hashing blob which is the same for Monero and Zephyr. But solo mining block template format is different for Zephyr, which is why it doesn't work with rx/0 in command line (rx/0 defaults to Monero).

# Action History
- Created by: downystreet | 2023-11-14T03:27:45+00:00
- Closed at: 2023-11-23T15:27:21+00:00
