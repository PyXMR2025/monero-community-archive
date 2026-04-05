---
title: Submit invalid block when solution is found right after receiving new block
  template
source_url: https://github.com/xmrig/xmrig/issues/2609
author: philipr-za
assignees: []
labels: []
created_at: '2021-09-29T08:23:07+00:00'
updated_at: '2021-09-29T09:18:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
We are using Xmrig to merge mine Monero with Tari so we have a proxy sitting between Xmrig and a Monero Daemon.

We have observed a very intermittent bug where Xmrig is working on a block N and then when it calls `get_block_template` the Monero daemon gives it a new template for block N+1 a few milliseconds before one of the mining worker threads finds a valid solution for block N. When Xmrig then calls `submit_block` for this solution it submits the solution nonce with the newly received block N+1 template instead of block N which is was working on. This results in that solution being rejected.

My intuition is that there is a timing issue between receiving a new template, updating the mining workers and how the solution found event is combined with the current template before calling `submit_block`

**To Reproduce**
Tricky to reproduce as it seems to occur when `get_block_template` is called just before a mining worker finds a valid solution. I observe it once a day maybe on a single CPU miner.

**Expected behavior**
When a solution is found for block N it submits the nonce with block template N not block template N+1.

**Required data**
![image](https://user-images.githubusercontent.com/25514413/135229928-5681b613-1e9c-4b40-a6bc-e69a6a42c6ff.png)

 - Config file or command line (without wallets)  
[config.json.zip](https://github.com/xmrig/xmrig/files/7250124/config.json.zip)

 - OS: Mac OS X and Windows




# Discussion History
## SChernykh | 2021-09-29T08:28:53+00:00
Indeed, DaemonClient only stores a single block template. I'll look into it.

## SChernykh | 2021-09-29T08:40:28+00:00
Although it's debatable whether old templates should be submitted at all. If xmrig got a new block template, monerod will not accept old templates because blockchain already moved forward.

## SChernykh | 2021-09-29T08:47:09+00:00
~I think you have a different error on the screenshot. It says "diff 102259 vs. 103988" and the first number must be bigger than the second.~
Edit: nvm, it's correct there.

## SChernykh | 2021-09-29T09:10:05+00:00
Can you compile xmrig with `-DWITH_DEBUG_LOG=ON` in cmake params? I need to see the network traffic when it happens. My guess right now is that the node you use for self-select received a new Monero block earlier than cryptonote.social, so it is a timing issue but not in xmrig itself (having only 1 block template there didn't cause this).

## philipr-za | 2021-09-29T09:18:19+00:00
> Although it's debatable whether old templates should be submitted at all. If xmrig got a new block template, monerod will not accept old templates because blockchain already moved forward.

Ah of course this makes sense. That share is not actually useful for the monero pool. Though it makes a difference for the merge mined chain. 

I will compile with -DWITH_DEBUG_LOG=ON and see if I can catch it again.

# Action History
- Created by: philipr-za | 2021-09-29T08:23:07+00:00
