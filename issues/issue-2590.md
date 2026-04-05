---
title: 'How to mine with nvidia gtx 1050 '
source_url: https://github.com/xmrig/xmrig/issues/2590
author: TheGipset
assignees: []
labels: []
created_at: '2021-09-19T05:58:46+00:00'
updated_at: '2021-09-27T13:06:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I want to mine with nvidia gtx 1050, i enabled CUDA at wizard, and when xmrig started, it says "CUDA (disabled) cant found module" something like that, i have downloaded CUDA plugin on getmonero.org but i have no idea to use it. Can someone explain to me

# Discussion History
## Spudz76 | 2021-09-19T13:16:18+00:00
For Windows you get the plugin from [xmrig-cuda releases](https://github.com/xmrig/xmrig-cuda/releases)

For Linux you build the plugin from the source in the same repository.

`nvidia-smi` from a shell will show what version of CUDA is in your driver in its header:
```
| NVIDIA-SMI 460.91.03    Driver Version: 460.91.03    CUDA Version: 11.2     |
```

Simply get the release that is built for equal or less than the version of CUDA your driver provides.

Put the dll from that into the same place xmrig.exe is.

## Kelvets | 2021-09-27T02:15:10+00:00
As far as I know, Monero is not efficient to be mined with GPUs, it is optimized to be mined much faster with your processor. You probably shouldn't be using the 1050 for Monero, there are better coins to be mined with that.

## Spudz76 | 2021-09-27T13:06:50+00:00
Good thing `xmrig` mines a whole lot more than just RandomX then huh.

# Action History
- Created by: TheGipset | 2021-09-19T05:58:46+00:00
