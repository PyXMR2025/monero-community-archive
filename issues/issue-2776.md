---
title: is it normal?  0 coin after 3 days mining
source_url: https://github.com/xmrig/xmrig/issues/2776
author: jj449
assignees: []
labels:
- question
created_at: '2021-12-03T01:10:05+00:00'
updated_at: '2022-01-02T06:27:17+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:04:28+00:00'
---

# Original Description
Sorry , i am new here .  It looks like it's mining , right ? 

[2021-12-03 01:02:10.284]  cpu      accepted (11/0) diff 141902 (192 ms)
[2021-12-03 01:02:24.409]  net      new job from monerohash.com:9999 diff 212853 algo rx/0 height 2506406 (3 tx)
[2021-12-03 01:02:45.406]  miner    speed 10s/60s/15m 1295.8 1291.8 n/a H/s max 1488.2 H/s
[2021-12-03 01:03:05.390]  cpu      accepted (12/0) diff 212853 (191 ms)
[2021-12-03 01:03:11.765]  cpu      accepted (13/0) diff 212853 (192 ms)
[2021-12-03 01:03:19.577]  net      new job from monerohash.com:9999 diff 212853 algo rx/0 height 2506407 (4 tx)
[2021-12-03 01:03:24.434]  net      new job from monerohash.com:9999 diff 314051 algo rx/0 height 2506407 (4 tx)
[2021-12-03 01:03:45.570]  miner    speed 10s/60s/15m 1127.0 1188.6 n/a H/s max 1488.2 H/s
[2021-12-03 01:04:24.456]  net      new job from monerohash.com:9999 diff 193589 algo rx/0 height 2506407 (4 tx)
[2021-12-03 01:04:45.736]  miner    speed 10s/60s/15m 1255.9 1264.1 n/a H/s max 1488.2 H/s
[2021-12-03 01:05:24.482]  net      new job from monerohash.com:9999 diff 145193 algo rx/0 height 2506407 (4 tx)
[2021-12-03 01:05:45.918]  miner    speed 10s/60s/15m 1179.3 1244.0 n/a H/s max 1488.2 H/s


But, there is no any coin appear in my MyMonero wallet , after 3 days , is it norml ? just need more time ?

# Discussion History
## Spudz76 | 2021-12-03T04:31:33+00:00
Go to [the pool website](https://monerohash.com/)

Scroll all the way down.

Paste wallet id string.

Observe stats there, and check pool FAQ for payout rules.

Your wallet only gets a dump when the pool pending balance hits payout level.

If you want semi often stream of payouts use p2pool and the small sidechain.  Otherwise mine at a pool for month(s) until anything will arrive on your wallet.

## Lonnegan | 2021-12-03T06:48:24+00:00
Your hashrate is 1400 H/s? With current difficulty it'll take almost one year (!) until you reach the 0.5 XMR payout limit of that pool!

Moreover, MoneroHash is a very small pool, and it pays according to the PROP method. That means you only get a reward at all when the pool finds a block. As a small pool, this happens only rarely, on average every 2-4 days. If you are a casual miner and do not mine 24/7, it can happen that you are not online when the pool finds a block. Then you get nothing. As a casual miner with such a low hashrate, I would mine at a PPS pool. There you get a reward for every returned share, regardless of whether the pool finds a block in the time or not.

## koitsu | 2022-01-02T06:27:17+00:00
I realise this ticket is closed, but I wanted to comment on something that's more educational (and applicable) to the OP @jj449 . This is *in addition* to what Spudz said.

Yes, it's very possible that for 3 days you have no payouts.  Good pool services display when the last time a block was found somewhere on their website (ex. MoneroHash, under section "Our Pool", "Block Found"; HeroMiners, under Section "Pool Mining", "Blocks Found" and "Block Found Every").  For further example, the last time a block was found (as of this writing) on HeroMiners was 7 days ago (!!!).  It happens.

The short of it is: as long as you see XMRig saying "new job from {pool/service}" and "accepted", then XMRig is actively working on something.  You can press "h" to see your active hashrate, and "c" to make sure that you have an active TCP session to the pool/service.

# Action History
- Created by: jj449 | 2021-12-03T01:10:05+00:00
- Closed at: 2021-12-19T15:04:28+00:00
