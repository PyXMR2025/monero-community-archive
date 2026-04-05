---
title: Miner code doesn't validate that pool is sending block height
source_url: https://github.com/xmrig/xmrig/issues/964
author: Gingeropolous
assignees: []
labels:
- bug
- enhancement
- wontfix
created_at: '2019-03-04T04:15:24+00:00'
updated_at: '2019-08-02T13:10:40+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:10:40+00:00'
---

# Original Description
So the miner just thinks its a normal job and hashes it and then the hashes don't match. Needs better error handling. @SChernykh 

# Discussion History
## SChernykh | 2019-03-04T07:20:11+00:00
Let me guess, some pools forgot to update their code to send block height to miners? Both node-multi-hashing and node-cryptonight-hashing throw errors when block height is missing pool-side, so I can't imagine how they added it in one place (verification) and forgot to add it in another (miner jobs).

https://github.com/SChernykh/CryptonightR also has a warning:
```
NOTE for pool operators: you'll have to pass active block height with each miner job and use correct height when checking submitted shares, don't forget that stale shares use older block height
```

And it's totally normal if height is missing in miner job because all other algorithms don't use it. xmrig can only check it if algorithm is set to "cryptonight" and protocol version is >= 10 and show some warning, but technically it's not an error, it might just be some other coin.

## SChernykh | 2019-03-04T07:29:58+00:00
It's possible to add a check to Client::parseJob() though. It can check that if variant is set to cn/r then height must be > 0 and print a warning if it's not set.

## Snipa22 | 2019-03-07T18:07:11+00:00
I did forget when I was doing testing.  The miner job data store contains the block-height, but the original proto to the miner never contained height, and it didn't occur to me to check, particularly as I'd already been shoving it to the proxy, which was the last major time that I was working on client data protos.  I only noticed that this was the case when I was mucking with the miner and cross-checked a secondary pool.  As everything else exploded, I had Ginger fire off an issue, as I figured it'd be good stance for miners to be able to verify as well, as there's very little indication that the pool is not properly upgraded:
[2019-03-03 20:01:13] new job from 69.164.198.226:3333 diff 1000 algo cn/r
[2019-03-03 20:05:59] new job from killallasics.moneroworld.com:3333 diff 5000 algo cn/r height 1166308

# Action History
- Created by: Gingeropolous | 2019-03-04T04:15:24+00:00
- Closed at: 2019-08-02T13:10:40+00:00
