---
title: Testnet doesn't work for 0.9.4 beyond 800500
source_url: https://github.com/monero-project/monero/issues/1231
author: arnuschky
assignees: []
labels: []
created_at: '2016-10-16T22:18:24+00:00'
updated_at: '2016-11-01T16:45:35+00:00'
type: issue
status: closed
closed_at: '2016-11-01T16:45:35+00:00'
---

# Original Description
Trying to use testnet with 0.9.4. It somehow doesn't work beyond block 800500:

```
2016-Oct-17 00:05:04.099748 [P2P7][x.x.x.x:28080 OUT]Sync data returned unknown top block: 800500 -> 821989 [21489 blocks (14 days) behind] 
```

This continues until all nodes block mine. What so special about block 800500? So no testnet for older versions?


# Discussion History
## moneroexamples | 2016-10-17T05:51:09+00:00
Only RingCT txs are accepted. Maybe that's why. Upgrade your monero to 0.10 version.


## ghost | 2016-10-17T21:07:49+00:00
That's not true. The last hardfork (v3) made coinbase more standardised. Next (v4) makes ringct voluntary and finally September 2017 is when normal tx will be fully replaced by ringct tx. 


## ghost | 2016-10-17T21:09:09+00:00
That said, a hard fork generally means that old issues will no longer be supported, so if this issue disappears when you upgrade to v0.10 then I'm afraid...please try upgrading to 0.10


## moneromooo-monero | 2016-10-17T22:26:32+00:00
800500 is the coinbase thing indeed, but only rct are being accepted now (except with unmixable stuff, where pre-rct is still allowed). But yes, update needed.


## luigi1111 | 2016-11-01T16:45:35+00:00
Testnet is on v5 currently. Need 0.10 or newer.


# Action History
- Created by: arnuschky | 2016-10-16T22:18:24+00:00
- Closed at: 2016-11-01T16:45:35+00:00
