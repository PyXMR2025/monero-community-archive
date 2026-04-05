---
title: CryptoNightR migration guide
source_url: https://github.com/xmrig/xmrig/issues/938
author: xmrig
assignees:
- xmrig
labels:
- enhancement
- META
- algo
created_at: '2019-02-21T09:30:29+00:00'
updated_at: '2019-08-02T12:02:55+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:02:55+00:00'
---

# Original Description
**:warning: Monero will change PoW algorithm to CryptoNightR on March 9.** :warning:

### Required steps
1. **Miners and proxy should be updated to v2.13 before March 9.**
2. `variant` option on each Monero pool should be set to `-1` (automatic).

#### Notes
* If your pool support [mining algorithm negotiation](https://github.com/xmrig/xmrig-proxy/blob/dev/doc/STRATUM_EXT.md#1-mining-algorithm-negotiation), don't need change `variant` option, just update miners and proxy to v2.13.
* If you use [xmrig-proxy](https://github.com/xmrig/xmrig-proxy) change `variant` option only on proxy side.
* Internal algorithm name is `cryptonight` variant `r`, or `cryptonight/r`, `cn/r` this algorithm also known as `cryptonight` variant `4`.

#### Notes for pool operators
* New required field `height` should be added to each job object.
* Optional field `"algo":"cn/r"` recommended to allow automatic algorithm negotiation.

### Test pool
http://killallasics.moneroworld.com/

### Checklist
* [x] CPU miner is ready in [dev](https://github.com/xmrig/xmrig/commits/dev) branch.
  * [x] v2.13 released. https://github.com/xmrig/xmrig/releases/tag/v2.13.1
* [x] AMD miner ready in [dev](https://github.com/xmrig/xmrig-amd/commits/dev) branch.
  * [x] v2.13 released. https://github.com/xmrig/xmrig-amd/releases/tag/v2.13.0
* [x] NVIDIA miner is ready in [dev](https://github.com/xmrig/xmrig-nvidia/commits/dev) branch.
  * [x] v2.13 released. https://github.com/xmrig/xmrig-nvidia/releases/tag/v2.13.0
* [x] proxy is ready in [dev](https://github.com/xmrig/xmrig-proxy/commits/dev) branch.
  * [x] v2.13 released. https://github.com/xmrig/xmrig-proxy/releases/tag/v2.13.0

# Discussion History
## 2010phenix | 2019-02-21T12:40:05+00:00
Thx for your work.
can do this new algo version for Classic miner too?

## xmrig | 2019-02-21T13:05:20+00:00
@2010phenix It more complicated than before, but possible, I will do it before fork date.
Thank you.

## xmrig | 2019-02-22T03:43:28+00:00
v2.13.0 released.

## valiant1x | 2019-03-01T18:57:31+00:00
EDIT: Disregard below - pool code was bad! If anyone else experiences a similar issue, make sure height is being sent to miner!

---

@xmrig is the CryptonightR implementation in 2.13.1 verified to work with Monero on testnet? We have tested the hashes produced by xmrig against both a pool implementation of CryptonightR and a local daemon implementation, and the hash test fails in both cases. The hashes pass properly for the [hashes provided by Monero](https://github.com/monero-project/monero/blob/release-v0.13/tests/hash/tests-slow-4.txt). For example, for the given blob, xmrig hashed `ec26b037999d3c89a6f0c035f7efb96dc4191d186b7062a6ec800d9289e40300` while the pool and daemon hashed `2f7f3e52027fcbb17942275e61e3da19534bb26eb9513c4ff1a14cfb3c8722ec`.

```
Hash mismatch on test 11
Input: 0606c4efe5e3052607db63efcab1b3bb6568cd7602718f3e9d91f5d32504c4dd8257807f618ccf5c3433339c9a41bf495a99ea8e7c77660e21419897f5553d9bc9d2cb6ff56e61849e313601
Expected hash: ec26b037999d3c89a6f0c035f7efb96dc4191d186b7062a6ec800d9289e40300
Actual hash: 2f7f3e52027fcbb17942275e61e3da19534bb26eb9513c4ff1a14cfb3c8722ec
<end of output>
Test time =   1.32 sec
```
Test:
`2f7f3e52027fcbb17942275e61e3da19534bb26eb9513c4ff1a14cfb3c8722ec 0606c4efe5e3052607db63efcab1b3bb6568cd7602718f3e9d91f5d32504c4dd8257807f618ccf5c3433339c9a41bf495a99ea8e7c77660e21419897f5553d9bc9d2cb6ff56e61849e313601 801`

Of course, pool rejects all of these shares as low difficulty since they are not hashing correctly on pool side.

## xmrig | 2019-03-02T04:03:48+00:00
@valiant1x Miner internally check hash implementation for each thread for CPU miner or one time on start for GPU miners, using test hashes provided by Monero https://github.com/xmrig/xmrig/blob/master/src/crypto/CryptoNight_test.h#L72

Note about `height` field is already in "Notes for pool operators" in first comment in this issue.
Thank you.

## 2010phenix | 2019-03-03T21:08:02+00:00
about height, need add to 1.2. Extended job object
in: https://github.com/xmrig/xmrig-proxy/blob/dev/doc/STRATUM_EXT.md#12-extended-job-object


## xmrig | 2019-03-04T18:26:10+00:00
@2010phenix classic C miner is ready https://github.com/xmrig/xmrig/commits/classic might forget something.

* Only `cn/r` support added, algorithm auto-detection (by block version) and ASM should work.

## 2010phenix | 2019-03-05T00:11:17+00:00
@xmrig yes thx, checked already in run(tomorrow check more close). 
single connect to alone pool work cn/2 and cn/r but try another things:
1. start test pool cn/r 
2. block pool port 3333
3. miner start backup pool supportxmr on 5555 port
4. job add \ good share accepted but not add worker to pool

## 2010phenix | 2019-03-05T14:47:41+00:00
@xmrig testing V10 more close on Win7 x64...

1. cn/0 correct mine
2. cn/2 correct mine
3. cn/r correct mine

test what we have with hashrate(ASM part) need I think only after March 9, test pool H\s work strange...

PS if someone want look in console **height** from pool can add param to log in: https://github.com/xmrig/xmrig/blob/4fdec33c50a9262059d9cec3833e1cb80aa0c352/stats.c#L89

# Action History
- Created by: xmrig | 2019-02-21T09:30:29+00:00
- Closed at: 2019-08-02T12:02:55+00:00
