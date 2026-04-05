---
title: '[BUG] xmrig 4.6.1 beta "Invalid configuration argument" for cn-pico auto configuration'
source_url: https://github.com/xmrig/xmrig/issues/1276
author: RainbowMiner
assignees: []
labels:
- bug
created_at: '2019-11-11T18:36:48+00:00'
updated_at: '2019-11-14T07:40:44+00:00'
type: issue
status: closed
closed_at: '2019-11-14T07:40:43+00:00'
---

# Original Description

If using the auto-configuration for CryptonightTurtle aka cn-pico on GTX1070 with xmrig v4.6.1 beta, I get the following json:
```
    "cn-pico": [
    {
      "index": 0,
      "threads": 228,
      "blocks": 45,
      "bfactor": 6,
      "bsleep": 25,
      "affinity": -1
    },
```

.. which results in the following error:
![image](https://user-images.githubusercontent.com/39437538/68611453-70232100-04ba-11ea-9d0c-35c15fcec186.png)

It looks like too many threads: the maximum value seems to be 128 for "threads".






# Discussion History
## xmrig | 2019-11-12T06:40:59+00:00
Fixed https://github.com/xmrig/xmrig-cuda/commit/15b9ed65fef01de98e60c1a702cb98dcf8184593
Actually limit to 128 was already here, but i was works only arch 70+.
Thank you.

## xmrig | 2019-11-14T07:40:43+00:00
Fixed in v5.

# Action History
- Created by: RainbowMiner | 2019-11-11T18:36:48+00:00
- Closed at: 2019-11-14T07:40:43+00:00
