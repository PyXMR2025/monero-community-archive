---
title: How to optimize Xmring for RTX 40x ?
source_url: https://github.com/xmrig/xmrig/issues/3352
author: fodger
assignees: []
labels: []
created_at: '2023-11-08T12:16:04+00:00'
updated_at: '2025-06-18T22:18:38+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:18:38+00:00'
---

# Original Description
**Describe the bug**
It's lower than my cpu !!!
My i5 11400F is between ~800h/s and 3500h/s, while  my RTX 4070 is between 300h/s and 2000h/s with xmrig 6.20 and xmring cuda 6.17 ! 

Can you help please to configure ma rtx ?

Thks a lot

**To Reproduce**
Juste run something like :
`xmrig.exe -o stratum+tcp://rx.unmineable.com:3333 -u xxxxxxx -p x --cuda --huge-pages-jit --randomx-cache-qos`

**Expected behavior**
RTX gpu should be much more efficient than a core i5 11th !

**Required data**
- windows 10 pro, xmrig 6.2, cuda 6.17.

**Additional context**


# Discussion History
## SChernykh | 2023-11-08T12:50:27+00:00
It's not a bug. RandomX is a CPU algorithm, GPUs are inefficient.

# Action History
- Created by: fodger | 2023-11-08T12:16:04+00:00
- Closed at: 2025-06-18T22:18:38+00:00
