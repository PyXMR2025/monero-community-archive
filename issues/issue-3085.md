---
title: System crashes after running xmrig
source_url: https://github.com/xmrig/xmrig/issues/3085
author: ghost
assignees: []
labels: []
created_at: '2022-07-10T02:04:12+00:00'
updated_at: '2022-07-11T14:43:08+00:00'
type: issue
status: closed
closed_at: '2022-07-11T14:43:08+00:00'
---

# Original Description
Logs me out of my system and kills all my processes.
![error](https://user-images.githubusercontent.com/108665518/178128458-2499bd46-c066-4f99-b2ae-b4945a0acd34.png)
OS: Fedora Linux 36 | GNOME 42.2
xmrig 6.18.0 with 1gb-pages enabled
CPU: Intel 9400f 

# Discussion History
## Spudz76 | 2022-07-10T14:16:14+00:00
Nouveau is trash, use nvidia proprietary driver and it will probably not crash.

(this isn't strictly related to xmrig, everything in the crash says nouveau)

## ghost | 2022-07-11T14:43:08+00:00
You’re right. Installing the nvidia driver solved this. Thank you.

# Action History
- Created by: ghost | 2022-07-10T02:04:12+00:00
- Closed at: 2022-07-11T14:43:08+00:00
