---
title: add cryptonight-webchain algo
source_url: https://github.com/xmrig/xmrig/issues/775
author: akaRevGit
assignees: []
labels:
- enhancement
- algo
created_at: '2018-10-04T09:58:18+00:00'
updated_at: '2019-08-02T12:49:28+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:49:28+00:00'
---

# Original Description
pls, add cryptonight-webchain algo in  new version
https://bitcointalk.org/index.php?topic=3649170.0

# Discussion History
## 2010phenix | 2018-10-04T11:20:28+00:00
@akaRevGit they already use xmrig https://github.com/webchain-network/webchain-miner

## LearnMiner | 2018-10-04T12:28:59+00:00
> @akaRevGit they already use xmrig https://github.com/webchain-network/webchain-miner

What is the difference with xmrig?

## xmrig | 2018-10-04T13:26:34+00:00
#### Quick overview:
* Changes in algorithm is trivial, one number replaced with other.
* Looks like some changes in stratum protocol too, it accept much larger blob.

#### About xmrig fork:
* Only `cryptonight-webchain` algo supported all others algorithms ripped off.
* Donation address changed as well, but no reason to fix it, I can't handle it anyway.
* Nicehash support also ripped off, so it will not work with xmrig-proxy.

#### Resolution
* I will look into it again after October 18, code is frozen, only bugfixes accepted before Monero fork.
* If non trivial changes required on network level, I will not add this coin.

## marki555 | 2018-12-03T21:42:24+00:00
Hi, did you review the needed changes?

# Action History
- Created by: akaRevGit | 2018-10-04T09:58:18+00:00
- Closed at: 2019-08-02T12:49:28+00:00
