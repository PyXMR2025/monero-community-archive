---
title: Mining on android using ubuntu
source_url: https://github.com/xmrig/xmrig/issues/2359
author: Clerisa
assignees: []
labels: []
created_at: '2021-05-09T08:15:30+00:00'
updated_at: '2021-05-09T11:45:00+00:00'
type: issue
status: closed
closed_at: '2021-05-09T08:22:48+00:00'
---

# Original Description
I try experiment mining using my android phone.
Realme 6 pro, ROG 2 and ROG 3.
Its work, but i don't know how to setting my configuration for mining, like how to set my cpu core for mining, its use (8 threads) make my phone lag and hot especially for ROG PHONE.😂
Let me know how to set my thread to 5 or 6
![P_20210509_160257](https://user-images.githubusercontent.com/83861587/117564887-f5ec5080-b0e0-11eb-914c-c8a49d7900d3.jpg)


# Discussion History
## SChernykh | 2021-05-09T08:20:18+00:00
If you use command line, add `--threads=5` to it: https://xmrig.com/docs/miner/command-line-options If you use config.json, find threads list for RandomX that should look like `"rx": [0, 1, 2, 3, 4, 5, 6, 7],` and remove some threads from it.

## Clerisa | 2021-05-09T08:27:18+00:00
Ty let me try its, i hope i know what doing there, i'm newbie 😂

## Monsluxe | 2021-05-09T09:35:16+00:00
Please let me know when yoyr phone is blowing up, please just think before
using xmrig on smartphone and DYOR about how dangerous and useless it is

Le dim. 9 mai 2021 à 10:27, Clerisa ***@***.***> a écrit :

> Ty let me try its, i hope i know what doing there, i'm newbie 😂
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2359#issuecomment-835742971>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AIIZ2OIEGNSVMC7LGM7B6RDTMZBPTANCNFSM44OWVPDA>
> .
>


## Clerisa | 2021-05-09T11:45:00+00:00
I know that, I'm just wondering how it works on phone 😂
I am not a man if I am afraid of danger.
That right it useless for you, but not for some people out there who don't have enough funds to build their own rig, a lot of people like that on YouTube all know the dangers of doing that, so we need proper settings so we don't endanger ourselves.

# Action History
- Created by: Clerisa | 2021-05-09T08:15:30+00:00
- Closed at: 2021-05-09T08:22:48+00:00
