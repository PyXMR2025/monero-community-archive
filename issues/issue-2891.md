---
title: CPU Affinity not working as expected with 80 cores
source_url: https://github.com/xmrig/xmrig/issues/2891
author: chadananda
assignees: []
labels:
- question
created_at: '2022-01-23T23:51:39+00:00'
updated_at: '2022-04-03T08:05:30+00:00'
type: issue
status: closed
closed_at: '2022-04-03T08:05:30+00:00'
---

# Original Description
I have a dual-Xeon E5-2698v4 with 40 physical cores, 80 total cores. The arrangement is seems to be in the order of (0-19) physical cores CPU#1, (20-39) physical cores CPU#2, (40-59) HT cores CPU#1, (60-79) HT cores CPU#2.

I have enough L2 cache to XMR-mine on 40, so I set XMRIG to use the first 40 physical cores with `--threads=40 --cpu-affinity=0x0000000000FFFFFFFFFF` and that works just as expected.

Now, I would like to experiment with using the remaining 40 HT cores for lighter-weight mining. But when I invert cpu affinity, it does not seem to work as expected, instead running a bunch of random cores. (`--threads=40 --cpu-affinity=0xFFFFFFFFFF0000000000`)

What am I missing here?

# Discussion History
## SChernykh | 2022-01-24T08:04:49+00:00
cpu affinity mask is 64 bit. If you want to set affinity for cores higher than 63, you have to use config.json

## chadananda | 2022-01-29T04:17:21+00:00
How would one set max threads in config? Seems to be a command-line only option.

## chadananda | 2022-01-29T04:35:02+00:00
And just setting affinity with an array does not seem to work either:
```
        "astrobwt": [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                     5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
```

## SChernykh | 2022-01-29T08:46:47+00:00
It works:
```
 "astrobwt": [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79],
```

# Action History
- Created by: chadananda | 2022-01-23T23:51:39+00:00
- Closed at: 2022-04-03T08:05:30+00:00
