---
title: Ryzen 9 3600 monero hashrate drop to aroun 400h
source_url: https://github.com/xmrig/xmrig/issues/1762
author: miningbazos
assignees: []
labels:
- stability
created_at: '2020-07-03T07:23:02+00:00'
updated_at: '2021-01-19T09:51:11+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:47:03+00:00'
---

# Original Description
Dear

Its happening on more computers with windows 10. I’m running Ryzen 9 3600x which is mining monero around 12000h/s normally. But after few days or sometimes few hours it drop to around 400hs. But CPU is still fully occupied by xmrig. It’s enough to CTrl+c to stop mine and run it again and its back to full speed for next couple of days usually. Temperatures are OK.

Please is there any command  switch which will auto restart mining if hashrate drop below some level? Or any idea what can I do with this?

Thanks

![image](

![](https://user-images.githubusercontent.com/67778617/86442762-8febab80-bd0e-11ea-9e12-930b7744c549.png)
)


# Discussion History
## SChernykh | 2020-07-04T07:50:08+00:00
This is a known issue with Windows scheduler, try setting `-1` for core number for all `rx/0` threads in config.json. See #1721, #1393, https://github.com/xmrig/xmrig/issues/1506#issuecomment-597624636 for more information.

## xmrig | 2020-08-31T05:47:03+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

## kaxak | 2021-01-19T09:51:10+00:00
I disabled PBO (Precision Boost Overdrive) in the bios and that problem gone.

# Action History
- Created by: miningbazos | 2020-07-03T07:23:02+00:00
- Closed at: 2020-08-31T05:47:03+00:00
