---
title: maybe low hashrate (randomx)?
source_url: https://github.com/xmrig/xmrig/issues/3734
author: kkaze5348-ops
assignees: []
labels: []
created_at: '2025-11-16T19:18:47+00:00'
updated_at: '2025-11-17T20:36:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[2025-11-16 23:09:38.024]  miner    speed 10s/60s/15m 2683.5 2807.0 n/a H/s max 2976.2 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   405.2 |   430.8 |     n/a |
|        1 |        1 |   449.0 |   469.7 |     n/a |
|        2 |        2 |   461.8 |   479.7 |     n/a |
|        3 |        3 |   463.2 |   480.7 |     n/a |
|        4 |        4 |   450.8 |   470.0 |     n/a |
|        5 |        5 |   457.1 |   474.0 |     n/a |
|        - |        - |  2687.1 |  2805.0 |     n/a |
is this normal hashrate for Intel(R) Core(TM) i7-9700KF CPU @ 3.60GHz cpu? huge pages/msr enabled

# Discussion History
## kkaze5348-ops | 2025-11-16T19:23:29+00:00
also it never uses 8/max threads with command --cpu-max-threads-hint=100


## kkaze5348-ops | 2025-11-16T19:35:14+00:00
one more question.
is it possible to start mining with both kawpow(gpu) and randomx(cpu) on the same xmrig instance ? eg command xmrig.exe -a randomx -o stratum+tcp://monero-pool.com:3333 -u YOUR_MONERO_WALLET -p x --cuda -a kawpow -o stratum+tcp://ravencoin-pool.com:3333 -u YOUR_ETH_ADDRESS -p x

and is it recommended ? or should i use 2 xmrig instance.


## HumbleDeer | 2025-11-16T20:49:33+00:00
@kkaze5348-ops 
> is this normal hashrate for Intel(R) Core(TM) i7-9700KF CPU @ 3.60GHz cpu? huge pages/msr enabled

Impossible to tell whether this is expected hashrate without knowing your specific config settings. Include them in a codeblock —not standard text for spam formatting reasons.

> is it possible to start mining with both kawpow(gpu) and randomx(cpu) on the same xmrig instance

I believe it lets you try and even run the instance, but it won't work.

> and is it recommended ? or should i use 2 xmrig instance.

yes.

> -a kawpow -o stratum+tcp://ravencoin-pool.com:3333 -u YOUR_ETH_ADDRESS

You'd want to use a RVN address in the standard BIP0044 format. 



## kkaze5348-ops | 2025-11-16T21:35:11+00:00




> [@kkaze5348-ops](https://github.com/kkaze5348-ops)
> 
> > is this normal hashrate for Intel(R) Core(TM) i7-9700KF CPU @ 3.60GHz cpu? huge pages/msr enabled
> 
> Impossible to tell whether this is expected hashrate without knowing your specific config settings. Include them in a codeblock —not standard text for spam formatting reasons.
> 
> > is it possible to start mining with both kawpow(gpu) and randomx(cpu) on the same xmrig instance
> 
> I believe it lets you try and even run the instance, but it won't work.
> 
> > and is it recommended ? or should i use 2 xmrig instance.
> 
> yes.
> 
> > -a kawpow -o stratum+tcp://ravencoin-pool.com:3333 -u YOUR_ETH_ADDRESS
> 
> You'd want to use a RVN address in the standard BIP0044 format.


thanks for reply
thats command ive used >xmrig.exe -o POOL:PORT -u address.pw -a rx/0 -k --cpu-max-threads-hint=100.

> Impossible to tell whether this is expected hashrate without knowing your specific config settings. Include them in a codeblock —not standard text for spam formatting reasons.

wdym codeblock?


## SChernykh | 2025-11-17T08:48:45+00:00
6 threads is the correct number for this CPU: https://xmrig.com/benchmark?cpu=Intel%28R%29+Core%28TM%29+i7-9700KF+CPU+%40+3.60GHz - all results there use 6 threads.

But you get much lower hashrate than expected. Can you add a screenshot of XMRig right after it starts so I can be sure that huge pages and msr really work?

## kkaze5348-ops | 2025-11-17T16:09:09+00:00
> 6 threads is the correct number for this CPU: https://xmrig.com/benchmark?cpu=Intel%28R%29+Core%28TM%29+i7-9700KF+CPU+%40+3.60GHz - all results there use 6 threads.
> 
> But you get much lower hashrate than expected. Can you add a screenshot of XMRig right after it starts so I can be sure that huge pages and msr really work?

<img width="934" height="599" alt="Image" src="https://github.com/user-attachments/assets/4a4394ba-779f-496e-8ae6-95956c30248d" />

## kkaze5348-ops | 2025-11-17T16:10:36+00:00
i see huge pages not allocated, but if i restart pc it will allocate and use 100%. hashrate will be still max 2976.2 H/s.

(also why it dont allocate huge pages sometimes?) and is there a solution to fix it, without restarting pc ?

## kkaze5348-ops | 2025-11-17T16:32:51+00:00
and OS is windows.

## SChernykh | 2025-11-17T17:04:04+00:00
You might be limited by your memory (single memory stick running at 2667 MHz). You could try to run it at 3200 MHz and tweak the timings, but single stick will still limit the CPU. Two sticks is recommended.

## kkaze5348-ops | 2025-11-17T17:08:09+00:00
> You might be limited by your memory (single memory stick running at 2667 MHz). You could try to run it at 3200 MHz and tweak the timings, but single stick will still limit the CPU. Two sticks is recommended.

how to run it with two sticks?

oh stick you mean ram sticks? i have 1x16 i guess

## kkaze5348-ops | 2025-11-17T17:14:33+00:00
So, for one stick 1x16, hashrate is normal? it should be like that?

## kkaze5348-ops | 2025-11-17T17:29:15+00:00
and last question is how to fix huge pages allocation that sometimes it dont allocate at all

## HumbleDeer | 2025-11-17T20:36:18+00:00
You might want to consider removing your config file algorithm sections
entirely then, so it doesn't pull configs from there regarding core
allocation etc

On Mon, 17 Nov 2025, 6:29 pm kkaze5348-ops, ***@***.***>
wrote:

> *kkaze5348-ops* left a comment (xmrig/xmrig#3734)
> <https://github.com/xmrig/xmrig/issues/3734#issuecomment-3543067569>
>
> and last question is how to fix huge pages allocation that sometimes it
> dont allocate at all
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3734#issuecomment-3543067569>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AD32W6AFMC4LSJNWXYS4KBT35IAYBAVCNFSM6AAAAACMIRV7ASVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTKNBTGA3DONJWHE>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


# Action History
- Created by: kkaze5348-ops | 2025-11-16T19:18:47+00:00
