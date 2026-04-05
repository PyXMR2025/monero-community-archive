---
title: 'Algo ghostrider high rate rejection low difficulty shares error '
source_url: https://github.com/xmrig/xmrig/issues/3547
author: KHPak2023
assignees: []
labels: []
created_at: '2024-09-06T07:07:11+00:00'
updated_at: '2025-06-18T22:05:38+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:05:38+00:00'
---

# Original Description
**Describe the bug**
Mining thooneum coin with ghostrider algo on xmrig 6.22.0. getting very high rates of rejected shares 

![image](https://github.com/user-attachments/assets/250aa181-5796-4046-a6cb-734f35f4a185)


**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - XMRig version
    - Either the exact link to a release you downloaded from https://github.com/xmrig/xmrig/releases
    - Or the exact command lines that you used to build XMRig
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2024-09-06T07:42:48+00:00
> thooneum coin

Is not supported. They must have modified something in the Ghostrider algorithm because you get 50% invalid shares with difficulty 2 - it's no better than just random guessing. If you set difficulty to 1000, you'll get 99.9% invalid shares because they changed the algorithm.

## KHPak2023 | 2024-09-06T08:07:20+00:00
> > thooneum coin
> 
> Is not supported. They must have modified something in the Ghostrider algorithm because you get 50% invalid shares with difficulty 2 - it's no better than just random guessing. If you set difficulty to 1000, you'll get 99.9% invalid shares because they changed the algorithm.

Thanks for response. I faced same issue while mining Yerbas coin same on ghostrider algo. 

# Action History
- Created by: KHPak2023 | 2024-09-06T07:07:11+00:00
- Closed at: 2025-06-18T22:05:38+00:00
