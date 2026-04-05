---
title: monerod unresponsive while verifying large blocks mined by xmrig
source_url: https://github.com/seraphis-migration/monero/issues/293
author: nahuhh
assignees: []
labels: []
created_at: '2026-02-11T18:11:08+00:00'
updated_at: '2026-02-16T02:07:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When you mine a block via xmrig, the node receives and verifies it. for a large block (30mb), this can take anywhere from 10s-2mins.

here is an extreme example
new job -> block found ~14:42:00 -> xmrig stops receiving responses from monerod until 14:44:28, during which time xmrig finds more blocks on the same (stale) template, and submits them (where they get verified and rejected).

The lengthy 2minutes of unresponsive time is possibly due to xmrig submitting many mined blocks (on the same stale template) in a row. Usually its about 10-20s for a single large block. (so about 0.5s/mb)

```
                                                                         
[2026-02-11 14:41:27.388]  miner    resumed                                                                                                                                             
[2026-02-11 14:41:53.429]  net      new job from 127.0.0.1:28789 diff 105537 algo rx/0 height 2933372 (2873 tx)                                                                         
[2026-02-11 14:42:08.714]  miner    speed 10s/60s/15m 13372.3 8968.6 993.6 H/s max 26167.1 H/s                                                                                          
[2026-02-11 14:43:08.769]  miner    speed 10s/60s/15m 13425.1 13410.8 1888.9 H/s max 26167.1 H/s                                                                                        
[2026-02-11 14:44:08.808]  miner    speed 10s/60s/15m 25649.0 24452.5 3514.6 H/s max 26167.1 H/s                                                                                        
[2026-02-11 14:44:28.124]  cpu      rejected (43/39) diff 105537 "Block not accepted" (168791 ms)                                                                                       
[2026-02-11 14:44:28.124]  net      no active pools, stop mining                                                                                                                        
[2026-02-11 14:44:28.129]  cpu      accepted (44/39) diff 105537 (170887 ms)                                                                                                            
[2026-02-11 14:44:28.929]  net      use daemon 127.0.0.1:28789  127.0.0.1                                                                                                               
[2026-02-11 14:44:28.929]  net      new job from 127.0.0.1:28789 diff 105473 algo rx/0 height 2933373 (2502 tx)                                                                         
[2026-02-11 14:44:29.045]  cpu      rejected (44/40) diff 105537 "Block not accepted" (147257 ms)
[2026-02-11 14:44:29.045]  net      no active pools, stop mining
[2026-02-11 14:44:29.365]  net      use daemon 127.0.0.1:28789  127.0.0.1
[2026-02-11 14:44:29.365]  net      new job from 127.0.0.1:28789 diff 105473 algo rx/0 height 2933373 (2502 tx)
[2026-02-11 14:44:29.449]  cpu      rejected (44/41) diff 105537 "Block not accepted" (143484 ms)
[2026-02-11 14:44:29.449]  net      no active pools, stop mining
[2026-02-11 14:44:29.713]  cpu      rejected (44/42) diff 105537 "Block not accepted" (136721 ms)
[2026-02-11 14:44:29.778]  cpu      rejected (44/43) diff 105537 "Block not accepted" (135615 ms)
```

Heres a less extreme example, where it topl 4-10 seconds. It is checking for templates every 15 seconds, so the missing one at :20 tells me that a block has already been submitted. At :24 we see a 2 rejected and 1 accepted block. I don't think xmrig can know to stop mining on old template, since monerod hasnt responded withnan acceptance yet.

```
                                                                                              
[2026-02-11 16:57:47.913]  miner    resumed                                                                                                                                             
[2026-02-11 16:57:50.584]  net      new job from 127.0.0.1:28789 diff 105132 algo rx/0 height 2933378 (2887 tx)                                                                         
[2026-02-11 16:58:05.907]  net      new job from 127.0.0.1:28789 diff 105132 algo rx/0 height 2933378 (2887 tx)                                                                         
[2026-02-11 16:58:24.338]  cpu      rejected (5/17) diff 105132 "Block not accepted" (17957 ms)                                                                                         
[2026-02-11 16:58:24.338]  net      no active pools, stop mining                                                                                                                        
[2026-02-11 16:58:24.342]  cpu      accepted (6/17) diff 105132 (14605 ms)                                                                                                              
[2026-02-11 16:58:24.436]  cpu      rejected (6/18) diff 105132 "Block not accepted" (14395 ms)                                                                                         
[2026-02-11 16:58:26.774]  net      use daemon 127.0.0.1:28789  127.0.0.1                                                                                                               
[2026-02-11 16:58:26.774]  net      new job from 127.0.0.1:28789 diff 105043 algo rx/0 height 2933379 (2895 tx)                                                                         
[2026-02-11 16:58:26.776]  net      new job from 127.0.0.1:28789 diff 105043 algo rx/0 height 2933379 (2895 tx)                                                                         
[2026-02-11 16:58:26.813]  miner    paused, press  r  to resume                                                                                                                         
[2026-02-11 16:58:27.200]  cpu      rejected (6/19) diff 105132 "Block not accepted" (14817 ms)                                                                                         
[2026-02-11 16:58:27.200]  net      no active pools, stop mining                                                                                                                        
[2026-02-11 16:58:32.483]  net      use daemon 127.0.0.1:28789  127.0.0.1                                                                                                               
[2026-02-11 16:58:32.483]  net      new job from 127.0.0.1:28789 diff 105043 algo rx/0 height 2933379 (2895 tx)  
```

During unresponsive time, monerod has a ton of logs (probably mpre than 100k lines) of
```
2026-02-11 17:58:43.270 D DB map size:     876138557440                                     
2026-02-11 17:58:43.270 D Space used:      87525380096                                      
2026-02-11 17:58:43.270 D Space remaining: 788613177344                                     
2026-02-11 17:58:43.270 D Size threshold:  0                                                                                                                                            
2026-02-11 17:58:43.270 D Percent used: 9.9899  Percent threshold: 90.000
```

and before that

```
2026-02-11 17:58:15.360 [RPC1]  DEBUG   txpool  src/cryptonote_core/tx_pool.cpp:1696      would decrease coinbase to 1.825060331041                                                     
2026-02-11 17:58:15.360 [RPC1]  DEBUG   txpool  src/cryptonote_core/tx_pool.cpp:1662    Considering <379e3b992aea36f966915dee3f78b690f6013cf11576b57dc01707e69f7830a5>, weight 12101, cu
rrent block weight 25559183/35995436, current coinbase 1.825314850130, relay method 4                                                                                                   
2026-02-11 17:58:15.361 [RPC1]  DEBUG   txpool  src/cryptonote_core/tx_pool.cpp:1696      would decrease coinbase to 1.825060331041                                                     
2026-02-11 17:58:15.361 [RPC1]  DEBUG   txpool  src/cryptonote_core/tx_pool.cpp:1763    Block template filled with 2665 txes, weight 25559183/35995436, coinbase 1.825314850130 (includi
ng 1.331210792000 in fees)
```

# Discussion History
## j-berman | 2026-02-12T00:34:47+00:00
@nahuhh can you by chance upload the monerod logs here? Maybe worth compressing. From that snippet, it definitely sounds like DB resizing is the issue

## j-berman | 2026-02-12T23:25:09+00:00
How many wallets are pointing to your daemon?

I have a local env setup that's spamming a local daemon from 10 wallets, unrelated to stressnet. Here are my relevant logs showing these resizings:

```
[0m[0;36m2026-02-12 20:19:24.452	I [0;36m[127.0.0.1:35430 INC] calling /getblocks.bin
[0m[0;32m2026-02-12 20:19:24.453	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:24.453	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:24.453	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:24.453	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:24.453	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;32m2026-02-12 20:19:24.454	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:24.454	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:24.454	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:24.454	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:24.454	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;32m2026-02-12 20:19:24.454	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:24.454	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:24.454	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:24.454	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:24.454	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;36m2026-02-12 20:19:24.454	I [0;36mHTTP [127.0.0.1] POST /getblocks.bin
[0m[0;36m2026-02-12 20:19:24.455	I [0;36m[127.0.0.1:35496 INC] calling /getblocks.bin
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:24.455	D [0;32mSpace remaining: 351331454976
...
[0m[0;32m2026-02-12 20:19:36.765	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
...
[0m[0;32m2026-02-12 20:19:41.238	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:41.238	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:41.238	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:41.239	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;32m2026-02-12 20:19:41.242	D [0;32mon_get_blocks: 3 blocks, 4371 txes, size 1351197
[0m[0;32m2026-02-12 20:19:41.246	D [0;32m/getblocks.bin() processed with 0/3242/4ms
[0m[0;32m2026-02-12 20:19:41.247	D [0;32mon_get_blocks: 3 blocks, 4371 txes, size 1351197
[0m[0;32m2026-02-12 20:19:41.253	D [0;32m/getblocks.bin() processed with 0/3243/5ms
[0m[0;36m2026-02-12 20:19:42.285	I [0;36mCleaned up 0 stale requests
[0m[0;32m2026-02-12 20:19:45.285	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:45.285	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:45.285	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:45.285	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:45.285	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;32m2026-02-12 20:19:45.369	D [0;32mDB map size:     352846790656
[0m[0;32m2026-02-12 20:19:45.369	D [0;32mSpace used:      1515335680
[0m[0;32m2026-02-12 20:19:45.369	D [0;32mSpace remaining: 351331454976
[0m[0;32m2026-02-12 20:19:45.369	D [0;32mSize threshold:  0
[0m[0;32m2026-02-12 20:19:45.369	D [0;32mPercent used: 0.4295  Percent threshold: 90.0000
[0m[0;32m2026-02-12 20:19:45.370	D [0;32mQueueing 368 transaction(s) for Dandelion++ fluffing
[0m[0;33m2026-02-12 20:19:45.371	W [0;33mUnable to send transaction(s), no available connections
[0m[0;36m2026-02-12 20:19:46.316	I [0;36mHTTP [127.0.0.1] POST /json_rpc
[0m[0;36m2026-02-12 20:19:46.316	I [0;36m[127.0.0.1:35510 INC] Calling RPC method get_fee_estimate
[0m[0;32m2026-02-12 20:19:46.316	D [0;32m/json_rpc[get_fee_estimate] processed with 0/0/0ms
```

These calls to `/getblocks.bin` are slow for each wallet (~3s per wallet). `/getblocks.bin` grabs the blockchain lock, which prevents the daemon from doing anything else during that time. Perhaps your wallets are refreshing calling the slow blocking call to `/getblocks.bin` preventing the daemon from making progress on block production?

If it's not wallets calling `/getblocks.bin`, then logs from your `monerod` would help us see what is responsible for all those db resizings.

One thing to check could be something like this: spin up a separate stressnet daemon that your wallets use, and separate from a stressnet daemon that xmrig points to to mine with. 

There's a long-time outstanding task item for upstream to use a read-write (rw) lock that would allow multiple readers at once to read simultaneously, which would help on this exact thing I'm seeing. I'll also look a bit more into this db resizing I'm seeing and see why this call is taking 3s.

## j-berman | 2026-02-13T18:09:07+00:00
> I'll also look a bit more into this db resizing I'm seeing and see why this call is taking 3s.

Parsing pool txs [here](https://github.com/monero-project/monero/blob/f99ee72d4b5065ddcaba2b74fcc6c8dc9be385dc/src/cryptonote_core/tx_pool.cpp#L634) takes ~60% of the time when serving the request. Then fetching the pool tx blobs seems to take the rest. The DB map size stuff looks like a red herring.

Parsed tx blobs could theoretically be cached in memory, but that's an eh idea imo, since it establishes a larger memory footprint for monerod.

So my hypothesis remains: the unresponsiveness seems caused by many wallets at once requesting the latest pool state via `/getblocks.bin`. And the best immediate move forward for that is probably a rw lock to allow many concurrent readers.

## j-berman | 2026-02-16T02:07:51+00:00
Another alternative route here is to serve tx blobs without parsing them, but the tx blobs stored in the `txpool_blob` table may be pruned or unpruned. If unpruned (the default), then we'd have to do some parsing to get the pruned blobs, plus we've wasted time reading all that extra data from the db. Therefore we'd probably want to do some db restructuring and store pruned blobs and prunable data in separate tables.

Summarizing my view...

**Short term solution** (@nahuhh can do this): users mining should use a separate node for mining, and a separate node that wallets point to.

**Medium term solution**: a rw lock that allows many concurrent readers (test that behavior and confirm it speeds up calls in this instance).

**Long term solution**: store pool tx blobs in 2 distinct tables (`pool_txs_pruned` and `pool_txs_prunable`), then just fetch blobs from the db and serve to the client *without* parsing. This requires a db migration.

# Action History
- Created by: nahuhh | 2026-02-11T18:11:08+00:00
