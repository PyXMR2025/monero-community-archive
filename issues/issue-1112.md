---
title: getblocktemplate huge performance hit on v0.10.0
source_url: https://github.com/monero-project/monero/issues/1112
author: osensei
assignees: []
labels: []
created_at: '2016-09-21T04:32:55+00:00'
updated_at: '2016-09-21T08:34:32+00:00'
type: issue
status: closed
closed_at: '2016-09-21T08:34:32+00:00'
---

# Original Description
I've done some tests in my pool with v0.10.0.

I've noticed that the calls to getblocktemplate take extremely longer on v0.10.0, and that the response time varies according to the number of transactions hanging on the tx pool.

I use haproxy as a reverse proxy between the pool and the daemons, so I can switch between daemons on the fly and see on haproxy logs how long the rpc calls are taking.

On v0.9.4 calls to getblocktemplate normally reply within ~4ms, regardless of how many transactions are held in the tx pool.

On v0.10.0, when the tx pool is empty it will reply in a similar time as v0.9.4 (i.e. ~4ms), but as TXs are being added to the tx pool, then this time starts to increase. I've seen "typical" times of ~50 ms when there are a few tx, but also times of ~120ms with 5 o 6 tx in the pool, and even ~450ms on one occasion. 

I'm sure that the time increases with the number of tx, but I also think that depending on the particular TXs on the tx pool, some times it may take longer to reply.


# Discussion History
## osensei | 2016-09-21T06:44:23+00:00
I'm seeing ~300ms now with tx pool size = 9


# Action History
- Created by: osensei | 2016-09-21T04:32:55+00:00
- Closed at: 2016-09-21T08:34:32+00:00
