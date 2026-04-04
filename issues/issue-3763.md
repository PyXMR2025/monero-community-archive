---
title: Copy and paste error in ge_fromfe_frombytes_vartime() (crypto-ops.c) leads
  to invalid result
source_url: https://github.com/monero-project/monero/issues/3763
author: ogrebgr
assignees: []
labels: []
created_at: '2018-05-06T16:43:34+00:00'
updated_at: '2018-05-07T04:58:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In src/crypto/crypto-ops.c the function `ge_fromfe_frombytes_vartime()` probably uses old version of the code from fe_frombytes.c

On line [2225](https://github.com/monero-project/monero/blob/7ed94d312224e415dcbfe937b27e1af377725058/src/crypto/crypto-ops.c#L2225) in crypto-ops.c there is:
`int64_t h9 = load_3(s + 29) << 2;`

In `fe_frombytes.c` same [line](https://github.com/monero-project/monero/blob/7ed94d312224e415dcbfe937b27e1af377725058/src/crypto/crypto_ops_builder/ref10/fe_frombytes.c#L39) is:
`crypto_int64 h9 = (load_3(s + 29) & 8388607) << 2;`

End result is that the ge_fromfe_frombytes_vartime() gives different (wrong) result, which leads to wrong result from `hash_to_ec()`, `generate_key_image()`, etc.

Implementations in other languages use the approach from `fe_frombytes.c`.




# Discussion History
## vtnerd | 2018-05-06T23:41:46+00:00
This was _probably_ intentional - the [same commit](https://github.com/monero-project/monero/commit/175d06e75e05aa4a42269dd048516e13b5bd585e) has both versions. The `int ge_frombytes_vartime` function is doing what the other languages are doing (unpacking a compressed y-coordinate + x-signbit). The function you referenced is mapping an arbitrary field element to some ed25519 group element. The former has to be masked because the sign bit is not part of the y coordinate. Unless there is a known security issue by doing it this way, I don't see a reason to change it.

## ogrebgr | 2018-05-07T04:58:11+00:00
I hope you are right. It would be best if whoever did the commit confirms that it is intentional.

# Action History
- Created by: ogrebgr | 2018-05-06T16:43:34+00:00
