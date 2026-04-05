---
title: Why does xmrig don't support BTV?
source_url: https://github.com/xmrig/xmrig/issues/650
author: Allin1920
assignees: []
labels: []
created_at: '2018-05-26T16:01:52+00:00'
updated_at: '2018-05-26T18:08:41+00:00'
type: issue
status: closed
closed_at: '2018-05-26T18:08:24+00:00'
---

# Original Description
Why does xmrig don't support BTV?
Http://www.uupool.cn/course/btv
Pool: btv.uupool.cn:9501
-u 1661dUzs2uD4q4cFhALPZTLXxHQ8eRDkq1
But https://github.com/bitcoinvote/cpuminer-multi support.
Minerd -a cryptonight -o stratum+tcp://btv.uupool.cn:9501 -u 1661dUzs2uD4q4cFhALPZTLXxHQ8eRDkq1.worker1 -p x
I can't understand.

Cpuminer-multi is sending data at {"Id": 2, "method": "mining.authorize", "params": "[1661dUzs2uD4q4cFhALPZTLXxHQ8eRDkq1", "X"].

# Discussion History
## xmrig | 2018-05-26T16:43:24+00:00
This coin use stratum protocol which not compatible with all other cryptonight coins, `mining.authorize` is invalid method for cryptonight stratum protocol.

https://github.com/bitcoinvote/cpuminer-multi Of course it support BTV because if forked by BTV team.

Also http://www.uupool.cn/course/btv looks down from my location.

# Action History
- Created by: Allin1920 | 2018-05-26T16:01:52+00:00
- Closed at: 2018-05-26T18:08:24+00:00
