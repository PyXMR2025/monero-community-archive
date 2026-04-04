---
title: Long wait for response from RPC
source_url: https://github.com/monero-project/monero/issues/4606
author: devnull00000
assignees: []
labels: []
created_at: '2018-10-15T23:20:18+00:00'
updated_at: '2018-12-18T12:49:18+00:00'
type: issue
status: closed
closed_at: '2018-12-18T12:49:18+00:00'
---

# Original Description
When using the transfer method, the answer does not come for a long time (about 10 seconds). In my application, after 8 seconds of waiting, a timeout is triggered, and the transaction is considered unsuccessful, but the transaction is completed successfully after the timeout. Perhaps the problem is in HDD. There will be an SSD on prodaction, but still I’m worried about the fact that a similar problem can happen again on the SSD, which will make the application work incorrectly. Should I worry?
p.s. 
Monero 0.13.0 "Beryllium Bullet" Release
Node on localhost
Other methods works fine

# Discussion History
## moneromooo-monero | 2018-10-16T12:41:40+00:00
There is scope for speeding this up, but if you're concerned about a spurious timeout detection, increase the timeout. Part of that time is used by waiting for the daemon to supply fake output info (so will be sped up by using a SSD), but the wallet also does some wasteful work (which won't).


## moneromooo-monero | 2018-10-19T12:06:16+00:00
https://github.com/monero-project/monero/pull/4663 will help a bit.

## moneromooo-monero | 2018-10-19T16:57:48+00:00
https://github.com/monero-project/monero/pull/4664 will help a little bit too.

## devnull00000 | 2018-10-20T12:48:20+00:00
Many thx. Tell me, can the count of sub-addresses affect the response time?

## moneromooo-monero | 2018-10-20T17:19:04+00:00
Yes for things like getbalance, which can return per address data.

## moneromooo-monero | 2018-11-02T12:12:57+00:00
Those are merged now. That's the low hanging fruits done AFAICT.

## prybus | 2018-12-01T00:03:31+00:00
@monero-project Is it posible? I have response transfer method after 120 second? This is very strange. 
Other methods works properly.


## moneromooo-monero | 2018-12-01T01:27:16+00:00
After 120 seconds, do you get an error back, or did the RPC succeed ?
Is your daemon running on a very slow machine, one with HDD (as opposed to SSD), or is it prone to swap ?
Are you using 0.13.0.4, or a recent master with the speedups ?

## moneromooo-monero | 2018-12-18T12:46:02+00:00
It should now be much faster.

+resolved

# Action History
- Created by: devnull00000 | 2018-10-15T23:20:18+00:00
- Closed at: 2018-12-18T12:49:18+00:00
