---
title: Ghostrider performance on Ryzen 8-core and 16-core not so good vs 6-core and
  12-core
source_url: https://github.com/xmrig/xmrig/issues/2881
author: toy1111
assignees: []
labels: []
created_at: '2022-01-20T19:23:26+00:00'
updated_at: '2022-01-23T04:29:56+00:00'
type: issue
status: closed
closed_at: '2022-01-23T04:29:56+00:00'
---

# Original Description
From the output below during the same algo run the 6 and 12 core processors get several boosted threads. But the 8 core doesn't (sorry I no longer have output from 16-core but it showed similar). I'll guess what I'm seeing is caused by the specific CN algos in Ghostrider but why is it that 6-core and 12-core processors get a boosted threads on several (though not all) of the algos used? Are there any config improvements possible for 8/16 core processors?

3600XT
    "hashrate": {
        "total": [1634.22, 1634.13, 1589.91],
        "highest": 5764.07,
        "threads": [
            [349.14, 349.1, 335.87],
            [234.2, 234.08, 229.48],
            [234.2, 233.95, 229.44],
            [349.14, 348.96, 335.9],
            [234.2, 234.08, 229.59],
            [233.33, 233.95, 229.59]
        ]

3800XT
 "hashrate": {
        "total": [1894.41, 1893.59, null],
        "highest": 1902.13,
        "threads": [
            [237.12, 236.71, null],
            [236.26, 236.58, null],
            [236.26, 236.71, null],
            [237.12, 236.71, null],
            [237.12, 236.71, null],
            [237.12, 236.71, null],
            [237.12, 236.71, null],
            [236.26, 236.71, null]
        ]
3900XT
    "hashrate": {
        "total": [3226.47, 3227.03, 3140.84],
        "highest": 11374.69,
        "threads": [
            [343.79, 344.48, 331.57],
            [231.19, 231.05, 226.66],
            [231.19, 230.91, 226.66],
            [344.64, 344.75, 331.89],
            [231.19, 231.05, 226.64],
            [231.19, 231.18, 226.66],
            [344.64, 344.75, 331.89],
            [230.33, 230.91, 226.71],
            [231.19, 231.05, 226.72],
            [344.64, 344.48, 331.61],
            [231.19, 231.18, 226.89],
            [231.19, 231.18, 226.89]
        ]


# Discussion History
## SChernykh | 2022-01-20T23:31:12+00:00
It's because 6-core Ryzen has 32 MB cache per 6 cores, so xmrig can use more cache on 2 threads. 8-core Ryzen has the same 32 MB cache but per 8 cores. Overall hashrate is still higher on 8-core Ryzen.

## toy1111 | 2022-01-21T01:11:19+00:00
Thanks for explaining and shame on me for not seeing that. Just assumed the 3700/3800 had more cache. I see now its same answer for the 12-core vs 16-core - these have the same 64MB cache.

# Action History
- Created by: toy1111 | 2022-01-20T19:23:26+00:00
- Closed at: 2022-01-23T04:29:56+00:00
