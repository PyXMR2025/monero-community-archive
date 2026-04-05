---
title: Can I set up XMRig without connecting to the pool but mine fake coins through
  localhost as a pool?
source_url: https://github.com/xmrig/xmrig/issues/663
author: mikegscott
assignees: []
labels:
- wontfix
created_at: '2018-05-29T23:19:38+00:00'
updated_at: '2018-11-05T13:50:37+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:50:37+00:00'
---

# Original Description
I am trying to set up XMRig miner but mining is blocked in my network. What I at least need to do is to set up XMRig mining but mine fake coins or just run mining algorithm without mining anything real (without pool username etc). 

# Discussion History
## QwertyJack | 2018-05-29T23:41:24+00:00
Is that testing mode?
BTW Why to do that？

## mikegscott | 2018-05-29T23:45:51+00:00
Yeah you can say testing mode. I just want to simulate a local pool (or simulate mining) to see how does it affect computer resources. 

## QwertyJack | 2018-05-30T01:08:19+00:00
As far as I know, xmrig does not support testing mode. Without instructions from a pool, the worker may not work at all.

## ghost | 2018-05-30T13:01:17+00:00
Are you a hacker ? Yes you can !
You must capture TCP message from miner to pool then replay it , something like that :
Step 1 : run `nc -nlvp 5555`
Step 2 : run xmrig with pool address point to 127.0.0.1:5555
As soon as xmrig send login data, paste pool message you captured to `nc`
Some thing like ...
```
{"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"469034036669300","job":{"blob":"0707bab9bad8055c251f7e881ec59bd1f0dbaacc48e3d1891d18ec563a7e6267f6790f35b76ab200000000adda882ee51010cf471542312801822bad8ddaf781dd02ff36442a66da05b5c60a","job_id":"782489939570474","target":"7b5e0400"},"status":"OK"}}
```
Sorry for my bad English



## mikegscott | 2018-05-30T16:14:37+00:00
Can you elaborate a bit more? I will be using windows operating system for mining. 

is there another option where I can download an entire blockchain of monero and start computing based on that? what would be the best way to go? 

## ghost | 2018-05-31T02:48:30+00:00
hmm , you should make a new cryptonight coin instead

# Action History
- Created by: mikegscott | 2018-05-29T23:19:38+00:00
- Closed at: 2018-11-05T13:50:37+00:00
