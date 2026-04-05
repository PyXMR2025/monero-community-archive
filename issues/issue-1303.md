---
title: 'Questions: (Monero, RandomX) Performance cli-wallet vs XMRig and Configuration'
source_url: https://github.com/xmrig/xmrig/issues/1303
author: GhostTyper
assignees: []
labels:
- question
created_at: '2019-11-19T07:43:04+00:00'
updated_at: '2019-11-19T16:30:02+00:00'
type: issue
status: closed
closed_at: '2019-11-19T13:07:20+00:00'
---

# Original Description
I have some questions, because I may start solo mining XMR with the RandomX change:

1. When I setup monerod (v0.15.0.0), let it sync, configure XMRig (5.0.1) with --daemon: true: Will everything just work fine when the switch to RandomX will happen? Or do I need to restart anything when block 1978433 is reached? Or will it be likely that I even need to switch some piece of software?
1. I have a 4 CPU Intel Xeon Gold 6146 configuration. Will it be more effective to launch 4 instances (docker containers or virtual machines) where each instance is bound to one NUMA node (I then also would remove NUMA support in the kernel, etc.)? Or will it be better to avoid an hypervisor/vm or docker layer and just trust the NUMA support of XMRig?
1. How fast is XMRig compared to the mining in the cli-wallet of monero? Should I use XMRig or would mining via the wallet "be enough"?
1. Is it true, that the cli-wallet is also mining to a pool called "supportxmr-pool"? Or is this real solo mining, where I will only get XMR, when and only when my block is used?

Thank you.

# Discussion History
## xmrig | 2019-11-19T10:19:17+00:00
1. Important part of configuration is use `"coin": "monero",` option, is that option set no need do anything, eg restart or use other tools, miner will switch algorithm automatically.
2. This hardware required zero configuration, miner will use 4 datasets (2080 MB), one per NUMA node, additional layers not recommended, especially is it full featured virtual machine it can provide wrong CPU topology and miner will use not optimal config. Make sure all your CPUs has local memory.
3. Wallet can't do precise auto-configuration for complex hardware like yours. 
4. Solo mining it more like a lottery, if you found block you will got whole block, but it will take a while and maybe you never find it. https://www.supportxmr.com/ is many other is just a regular pool, you will got small piece of each pool block it much more stable and predictable.

You can use testnet pool https://rx.minexmr.com/ for check how it works.
Thank you.

## GhostTyper | 2019-11-19T11:10:15+00:00
Hi, another iteration:

1. Can you give an estimation how much slower the mining with the cli-wallet or monerod will be compared to XMRig?
1. I've already setup a public monero node. So I could clone this node 3 times and just let all of them mine. I think it doesn't make sense that monerod or the wallet is mining into a pool. Can someone confirm weather if the official monero software is mining into a pool or just "solo-mining"?
1. Another question about XMRig: Are the XMRig binaries compiled with something fancy like intel compiler?

Thank you.

## 2010phenix | 2019-11-19T11:59:21+00:00
GhostTyper, man you are strange...
I want money, I want more money but am so lazy, tell me how to have more more more money...
this is Issues tracker, use google and you find all answer.....

## GhostTyper | 2019-11-19T12:04:54+00:00
Actually I don't care about the money. That's also the reason why I would prefer solo-mining and why I consider point 2 in my last reply.

To just re-ask something for clarification doesn't hurt anybody. (Except of you obv.)

xmrig can answer those questions easily or if he can't or doesn't want to he will tell me. He doesn't need YOU for this.

## xmrig | 2019-11-19T12:25:41+00:00
Actually I little lazy to answer too, but:

1. You can check it by myself, I didn't check mining in wallet for a while.
2. Mining in wallet and standalone miner + daemon, it always solo, it common rule for all coins.
3. Performance critical code is already optimized, compiler can't change anything.

## GhostTyper | 2019-11-19T13:07:17+00:00
Thank you.

Just in case this may be interesting for somebody else. for coin=monero (cn/r), CPU only:

| Mining Speed | XMRig | monerod |
| --- | --- | --- |
| 4-CPU (4-NUMA) | 2819 H/s | 1810 H/s |
| 1-CPU (NO NUMA) | 671 H/s | 449 H/s |

Seems like NUMA-Support doesn't make a very big difference. XMRig is about 50% faster. I may re-test this with RandomX at 30th November.

# Action History
- Created by: GhostTyper | 2019-11-19T07:43:04+00:00
- Closed at: 2019-11-19T13:07:20+00:00
