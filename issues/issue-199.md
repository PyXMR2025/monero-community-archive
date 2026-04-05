---
title: 'xmr-stak-amd much faster with AMD Vega 56 '
source_url: https://github.com/xmrig/xmrig/issues/199
author: helbadini
assignees: []
labels: []
created_at: '2017-11-14T21:02:40+00:00'
updated_at: '2017-11-16T22:59:21+00:00'
type: issue
status: closed
closed_at: '2017-11-16T22:59:21+00:00'
---

# Original Description
Hi, 

The above easily outperforms by up to 25% with the following settings. Can these be replicated here? 

"gpu_thread_num" : 2,
"gpu_threads_conf" : [ 
    { "index" : 0, "intensity" : 2016, "worksize" : 8, "affine_to_cpu" : false },
    { "index" : 0, "intensity" : 1736, "worksize" : 8, "affine_to_cpu" : false },

Thanks!

Hugh

# Discussion History
## helbadini | 2017-11-15T22:20:50+00:00
Never mind, this works. Thanks!

    "opencl-platform": 1,
    "threads": [
        {
            "index": 0,
            "intensity": 2016,
            "worksize": 8,
            "affine_to_cpu":
			false
        },
		{
            "index": 0,
            "intensity": 1736,
            "worksize": 8,
            "affine_to_cpu": false
        },
    ],

## nazarimilad | 2017-11-15T22:28:33+00:00
Don't forget to close the issue.

# Action History
- Created by: helbadini | 2017-11-14T21:02:40+00:00
- Closed at: 2017-11-16T22:59:21+00:00
