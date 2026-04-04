---
title: Cannot sync up with blockchain
source_url: https://github.com/monero-project/monero/issues/6748
author: Mladia
assignees: []
labels: []
created_at: '2020-08-06T16:39:40+00:00'
updated_at: '2020-08-06T17:10:04+00:00'
type: issue
status: closed
closed_at: '2020-08-06T17:10:03+00:00'
---

# Original Description
From quite some time I was not able to sync up using monerod. 
I think this is the problem, is there a way of fixing it, besides starting the whole sync from scratch.
```
2020-08-06 16:25:48.730	E Block recognized as orphaned and rejected, id = <b825f846efd7262f58d5c4a1f7efb72ddfa3e236c129facf4ce474204c19288a>, height 2131257, parent in alt 0, parent in main 0 (parent <993317d5a3ef7558db66a2dfbb758548e5eb6436f0c5e4b693a6535d97ff3e3f>, current top <4780067c4bcb8dd404889ed408aad96e6fbaf0dd632cc3042eb1b7624c9fa5d0>, chain height 2131256)
2020-08-06 16:25:48.730	I [88.198.0.148:18080 OUT] Block received at sync phase was marked as orphaned, dropping connection
```
I am running 
```/usr/bin/monerod --data-dir /run/media/Data/.monero --check-updates disabled --max-concurrency 2  --log-level "1,*msg*:INFO,*net*:DEBUG"``` on Arch with the latest version from the Arch repos v0.16.0.1-release.
Here is a link to bigger part of the log https://gist.github.com/Mladia/84015e45d3455cfeb1bfb64116213dd8#file-gistfile1-txt.



# Discussion History
## moneromooo-monero | 2020-08-06T16:48:21+00:00
Looks like a corrupted chain. Resync is the only safe way to fix. Theoretically it's possible that popping enough blocks would fix, but it's (1) not certain as it depends on the corruption details and (2) we don't know how far to pop as we don't know all the corrupted data.

## Mladia | 2020-08-06T17:10:03+00:00
All right. Thanks.

# Action History
- Created by: Mladia | 2020-08-06T16:39:40+00:00
- Closed at: 2020-08-06T17:10:03+00:00
