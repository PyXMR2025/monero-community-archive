---
title: Unspecified launch faillure
source_url: https://github.com/xmrig/xmrig/issues/621
author: Qurmo
assignees: []
labels: []
created_at: '2018-05-09T17:25:57+00:00'
updated_at: '2018-08-04T07:50:33+00:00'
type: issue
status: closed
closed_at: '2018-08-04T07:50:33+00:00'
---

# Original Description
![xmrig error](https://user-images.githubusercontent.com/32374369/39829401-984f51ac-53be-11e8-9345-757717f6f85d.jpg)
I get message as displayed in the picture.  both with CUDA 8 as CUDA 9 version on Windows 10.  What am I doing wrong?

# Discussion History
## aka-lex | 2018-05-09T17:40:30+00:00
reduce threads and / or boost bfactor

## Qurmo | 2018-05-09T18:03:24+00:00
and how do I do that?  sorry kinda a beginner in this :s 


## aka-lex | 2018-05-10T06:31:40+00:00
```
    "threads": [
        {
            "index": 0,
            "threads": 30,
            "blocks": 24,
            "bfactor": 6,
            "bsleep": 25,
            "affine_to_cpu": false
        }
    ], 
```
change the values in the configuration file of the miner.
in the threads section

## Qurmo | 2018-05-10T09:31:59+00:00
do you have to equally downgrade them or just 1 is enough?  ex: only the number off threads?
I presume, that Blocks means the number off blocks he keeps on hold to hash?  but what does bfactor and bsleep do?

# Action History
- Created by: Qurmo | 2018-05-09T17:25:57+00:00
- Closed at: 2018-08-04T07:50:33+00:00
