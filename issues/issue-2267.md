---
title: error "no suitable configuration found"
source_url: https://github.com/xmrig/xmrig/issues/2267
author: robinfoxnan
assignees: []
labels:
- question
- CUDA
created_at: '2021-04-15T01:28:22+00:00'
updated_at: '2022-04-03T14:51:43+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:51:43+00:00'
---

# Original Description
i compiled the cuda.dll, and config json like this:
"cuda": {
"enabled": true,
        "loader": "xmrig-cuda.dll",
        "nvml": true,
   "cn/0": false,
        "cn-lite/0": false
    }

but i got an error :
"no suitable configuration found"

Is there someone can tell me how to config the cuda config section?

Thanks a lot

# Discussion History
## Spudz76 | 2021-04-15T23:33:58+00:00
if you used latest CUDA Toolkit but have an older than Pascal GPU it won't work.  May need CUDA 10.2.

if you used the latest driver but have an older than Kepler GPU it also won't work (and you need CUDA 8.0 maximum, driver series 390 maximum for Fermi)

What's the actual output at startup / does it list the GPU?  What GPU model is it and how much memory and what algo are you trying to use?

# Action History
- Created by: robinfoxnan | 2021-04-15T01:28:22+00:00
- Closed at: 2022-04-03T14:51:43+00:00
