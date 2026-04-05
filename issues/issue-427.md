---
title: Implement support for the CryptoNight-Dark hashing algorithm from Bitnote.
source_url: https://github.com/xmrig/xmrig/issues/427
author: cmarshall108
assignees: []
labels:
- enhancement
- wontfix
created_at: '2018-03-03T20:27:55+00:00'
updated_at: '2018-11-05T07:13:17+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:13:17+00:00'
---

# Original Description
https://github.com/xbn-project/bitnote/commit/04cdf674c0a852cb13c0c7922447c13388899158

# Discussion History
## xmrig | 2018-03-04T05:33:51+00:00
Is any test pool and/or any reference hash values available?
Thank you.

## xcn-project | 2018-03-05T22:00:33+00:00
@xmrig Here are a few blocks mined using the CryptoNight-Dark PoW algorithm change. The algorithm uses a 0.5 MiB scratchpad (or 1 << 19 = 524288). Blocks below height three are using the original CryptoNight algorithm with the 2 MiB scratchpad (or 1 << 21 = 2097152).

```
height 0, timestamp 1518745759, cumul_dif 1, cumul_size 78
id		<fb58cea5fcd8e26da8fadb0ff0003d83c3d496e5c7a3a55dc9be06d3e5ec4657>
difficulty		1, nonce 10000, tx_count 0
height 1, timestamp 1520288059, cumul_dif 2, cumul_size 80
id		<3a76be2325e56785f481241e521321b7bd74a1c88b66c2bf576089c4fbe7655d>
difficulty		1, nonce 3048861600, tx_count 0
height 2, timestamp 1520288059, cumul_dif 3, cumul_size 226
id		<b6e2cb70c2e9d83dad7faae462c43f2c039906b5400e5a4cf4f68276da58eb73>
difficulty		1, nonce 4169887703, tx_count 0
height 3, timestamp 1520288059, cumul_dif 4, cumul_size 226
id		<6e8dda75b73e8afd1897734711ac03a6eedc010881d7e65b2f6dff9550cca0c9>
difficulty		1, nonce 927501127, tx_count 0
height 4, timestamp 1520288059, cumul_dif 5, cumul_size 226
id		<324d40a1309e63ae0f8ff6b355419a69b664c623606cfe65b77218915cbd4cfd>
difficulty		1, nonce 3602721895, tx_count 0
height 5, timestamp 1520288059, cumul_dif 8, cumul_size 226
id		<82f2a05fd7f2e21b94af356fd58fb3683b657be52616a9f21aa662c11ad64e5c>
difficulty		3, nonce 1003506166, tx_count 0
height 6, timestamp 1520288059, cumul_dif 13, cumul_size 226
id		<379e59b7b692562eccf1c3ca821142a48d34729ea8505a2aedb3276c03cd4971>
difficulty		5, nonce 1240861488, tx_count 0
height 7, timestamp 1520288060, cumul_dif 26, cumul_size 226
id		<42143a5bf470e8f6eac6fc1c683f2cfd5837b7d735afddf455cd7054f54e619f>
difficulty		13, nonce 284377345, tx_count 0
height 8, timestamp 1520288060, cumul_dif 49, cumul_size 226
id		<88bbdf42c083cd5adde16560012d30014a34bf592c155d92afe9104935f0f9aa>
difficulty		23, nonce 3202951480, tx_count 0
height 9, timestamp 1520288061, cumul_dif 102, cumul_size 226
id		<7b1f1e97fba658f8ce1abb9d17846197ee59590533fed3d758af8c69757b3ab9>
difficulty		53, nonce 857070854, tx_count 0
height 10, timestamp 1520288062, cumul_dif 200, cumul_size 226
id		<752edd44fc2fc5a1c8ce2d6ec00d62e17929fdcd49f90a6bc9f3ab1f14f85366>
difficulty		98, nonce 1801850846, tx_count 0
height 11, timestamp 1520288067, cumul_dif 417, cumul_size 226
id		<f86a9c604d1033063d2b36d54107e577b39075c2a5606970d7fd7448409555ed>
difficulty		217, nonce 1717723900, tx_count 0
height 12, timestamp 1520288079, cumul_dif 827, cumul_size 226
id		<0a10e997325a6a0a9805c49b8341203ad59bca147b48747772bba7ad152fe64c>
difficulty		410, nonce 1956689872, tx_count 0
height 13, timestamp 1520288097, cumul_dif 1717, cumul_size 226
id		<4bc1c2c708ca92fb1c9863a7c8f270d44d1c2b7cd5ccef60eaf9b2bd96628f9f>
difficulty		890, nonce 2582645791, tx_count 0
height 14, timestamp 1520288127, cumul_dif 3095, cumul_size 226
id		<5988b5ae7521e35f62bfb895a210fc37a8f87bb135381c8f7b63850ab591c13a>
difficulty		1378, nonce 1547393996, tx_count 0
```
You can also refer to the latest source code here, https://github.com/xbn-project/bitnote/blob/master/src/crypto/slow-hash.c

## xcn-project | 2018-03-06T11:43:36+00:00
Also see, https://github.com/xbn-project/bitnote/issues/3

# Action History
- Created by: cmarshall108 | 2018-03-03T20:27:55+00:00
- Closed at: 2018-11-05T07:13:17+00:00
