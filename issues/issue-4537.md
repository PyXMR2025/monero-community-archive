---
title: what is the use of cn_slow_hash_prehashed  here?
source_url: https://github.com/monero-project/monero/issues/4537
author: calidion
assignees: []
labels:
- invalid
created_at: '2018-10-09T06:25:23+00:00'
updated_at: '2018-10-10T16:49:02+00:00'
type: issue
status: closed
closed_at: '2018-10-10T16:49:02+00:00'
---

# Original Description
by searching cn_slow_hash_prehashed to know that it is only a definition.
```
eric@eric-laptop:~/Monero/monero$ grep cn_slow_hash_prehashed . -Rn
./src/crypto/hash.h:78:  inline void cn_slow_hash_prehashed(const void *data, std::size_t length, hash &hash, int variant = 0) {
```

# Discussion History
## moneromooo-monero | 2018-10-09T08:09:33+00:00
Is there a bug here ?

## calidion | 2018-10-10T04:21:20+00:00
@moneromooo-monero 

I am determining which function is compatible with the old cryptonight algorithm.
it seems cn_slow_hash doesn't compatible with the old cryptonight algorithm.

I have changed my code base from the original cryptonote to monero.
and tested cn_slow_hash with the following (variant, prehashed) pair:

0, 0,
0, 1,
1, 0,
1, 1

none of them worked for the old network.


## moneromooo-monero | 2018-10-10T08:40:51+00:00
Ignore prehashed, always set it to 0. variant 0 is the original CN. 1 is what monero is using now. 2 is what monero will be using from v8.

See https://github.com/monero-project/monero/pull/4218

## calidion | 2018-10-10T16:10:03+00:00
@moneromooo-monero 

Thanks.

I set the last two parameter to 0, 0 for cn_slow_hash,
but it still not work with the old network.

you can checkout code from https://github.com/vigcoin/coin

where master can not update while old branch can.


the only difference is the cn_slow_hash.


## calidion | 2018-10-10T16:38:17+00:00
@moneromooo-monero 

by `make clean` and `make` again.
the new compiled works with the old network now.

Thank you very much.

## moneromooo-monero | 2018-10-10T16:44:00+00:00
+invalid

# Action History
- Created by: calidion | 2018-10-09T06:25:23+00:00
- Closed at: 2018-10-10T16:49:02+00:00
