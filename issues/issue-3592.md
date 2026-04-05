---
title: Could you create optimization for Kawpow algo?
source_url: https://github.com/xmrig/xmrig/issues/3592
author: BonhomieBG
assignees: []
labels: []
created_at: '2024-11-29T08:50:11+00:00'
updated_at: '2024-12-05T09:47:37+00:00'
type: issue
status: closed
closed_at: '2024-12-05T09:47:37+00:00'
---

# Original Description
I been mining kawpow on my AMD gpu and the hashrate is very inconsistant. My 7900xtx going 56-59MH all the time, notible after new session program compiled.
A little bit of optimization to make it more stable would be great.

thank you so much.

# Discussion History
## SChernykh | 2024-11-29T08:56:11+00:00
Each new Kawpow program is different and has a different hashrate (some programs are longer, some are shorter). It's normal for Kawpow.

## BonhomieBG | 2024-11-29T09:15:11+00:00
Sorry to compare but I want to learn more about why does team red miner can get 59MH consistency for like 30 mins. One more noticeable different is in GPU utilization, XMRig go randomly around 1.85Ghz while the TRM is at 1.95G, the core clock limit is the same 1.97.

## BonhomieBG | 2024-11-29T09:17:38+00:00
![Screenshot from 2024-11-29 01-47-19](https://github.com/user-attachments/assets/93cb1dc6-cdad-4136-9358-de7e78883fa7)
![Screenshot from 2024-11-29 02-32-30](https://github.com/user-attachments/assets/899ff0bf-e283-4947-8dd8-476776c6a2d8)


# Action History
- Created by: BonhomieBG | 2024-11-29T08:50:11+00:00
- Closed at: 2024-12-05T09:47:37+00:00
