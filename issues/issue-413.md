---
title: 'Ryzen 2400G '
source_url: https://github.com/xmrig/xmrig/issues/413
author: yangsystem
assignees: []
labels:
- wontfix
created_at: '2018-02-24T12:13:05+00:00'
updated_at: '2018-11-05T12:57:13+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:57:13+00:00'
---

# Original Description
I am unable to mine with the GPU. If I start xmrig-amd system crushes after 5 seconds.
I have all latest drivers from amd website. video chip is vega11.

# Discussion History
## g5-freemen | 2018-03-03T12:49:14+00:00
try diffent miner, use Nicehash miner legacy for example just to check which miners can work with your GPU (and make sure that your system drivers works OK)

## xmrig | 2018-11-05T12:57:13+00:00
This CPU bad choice for CPU and/or GPU mining, low amount of CPU cache, blue screen of death with high intensity, recent versions of xmrig-amd skip this GPU from autoconfig.

# Action History
- Created by: yangsystem | 2018-02-24T12:13:05+00:00
- Closed at: 2018-11-05T12:57:13+00:00
