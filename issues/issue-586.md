---
title: XMrig not working for CryptoNightLite V1 coins
source_url: https://github.com/xmrig/xmrig/issues/586
author: vlad230
assignees: []
labels: []
created_at: '2018-04-26T13:24:12+00:00'
updated_at: '2018-06-17T18:13:51+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:13:51+00:00'
---

# Original Description
I have been trying to mine a coin using xmrig-2.6.0-beta3-gcc-win64 that is based on CryptoNightLite V1 but I get all my shares rejected. 

I have been using xmrig for some time with other coins and is working fine.

Are you going to support this new algo?

# Discussion History
## xmrig | 2018-04-26T13:49:12+00:00
What coin? I know only one `CryptoNightLite V1` at this moment and this is Turtlecoin and it work fine.

* Set global option algo: `"algo": "cryptonight-lite",`
* Set variant on each pool: `"variant": 1`  https://github.com/xmrig/xmrig/blob/master/src/config.json#L24

## vlad230 | 2018-04-27T07:13:06+00:00
Thanks a lot for the fats reply! I wasn't using the **"variant": 1** setting. It's working fine now.

Is there a detailed list of all the parameters, values & what they do, other than the comments in the config.json file?

For example some values are outdated and not specified right now (e.g. using short names for algos: cn-heavy)

# Action History
- Created by: vlad230 | 2018-04-26T13:24:12+00:00
- Closed at: 2018-06-17T18:13:51+00:00
