---
title: nicehash and minergate
source_url: https://github.com/xmrig/xmrig/issues/41
author: walruzperil
assignees: []
labels: []
created_at: '2017-07-18T22:02:45+00:00'
updated_at: '2017-11-08T11:36:29+00:00'
type: issue
status: closed
closed_at: '2017-07-19T23:57:31+00:00'
---

# Original Description
Hello, i try connect to: 
nicehash - xmring say 50h/s and cpu usage 90%, but on website nicehash -workers:0 (xmrig -o stratum+tcp://cryptonight.eu.nicehash.com:3355 -u 35zDPhc7Uz3qKmkfoGQELoq6rMAFDVqtC7 -p x -t 4)

minergate - xmring say n/a h/s (xmrig -o stratum+tcp://xmr.pool.minergate.com:45560 -u email@gmail.com -p x -t 4)
what i do wrong?

# Discussion History
## walruzperil | 2017-07-18T22:16:37+00:00
upd: works on nicehas, but I can not understand why there are share for so long ..
minergate still not work..

## xmrig | 2017-07-18T22:22:00+00:00
Nicehash diff to high for slow miners, I check now it give me 40000 diff, it can take a while (depends of luck) before share accepted.

Strange should work did you see messages like `use pool xmr.pool.minergate.com:45560` and `new job from xmr.pool.minergate.com:45560`?

Also what your CPU 50 h/s for 4 threads does not sound right.
Thank you.

## walruzperil | 2017-07-18T22:31:06+00:00
minergate now works, i thing this was local problems. Thank you

## leovarmak | 2017-11-08T11:36:29+00:00
@walruzperil Never use minergate. They scam.

# Action History
- Created by: walruzperil | 2017-07-18T22:02:45+00:00
- Closed at: 2017-07-19T23:57:31+00:00
