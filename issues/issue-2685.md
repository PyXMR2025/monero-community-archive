---
title: 'Killed? '
source_url: https://github.com/xmrig/xmrig/issues/2685
author: Cotternn
assignees: []
labels: []
created_at: '2021-11-11T12:22:47+00:00'
updated_at: '2021-11-11T13:59:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Does not Mine

**To Reproduce**
cd termux-ubuntu
cd xmrig
cd build
THE Mining Command


**Expected behavior**
Mine dogecoin? 

**Required data**
 
![Screenshot_20211111_201819_com termux](https://user-images.githubusercontent.com/94116533/141297323-a9cbdac1-cf11-4876-8e6c-b8735f4b5987.jpg)


**Additional context**
Add any other context about the problem here.
![Screenshot_20211111_201819_com termux](https://user-images.githubusercontent.com/94116533/141296964-e100d39b-f90c-4ec1-be6d-41c9a4152f25.jpg)


# Discussion History
## SChernykh | 2021-11-11T12:36:18+00:00
> Mine dogecoin?

What?

## Lonnegan | 2021-11-11T13:59:30+00:00
The RAM of your device is already 96% full BEFORE you try to start xmrig. How should xmrig allocate 2 GB RAM for RandomX when just 0,1 GB are free (and your device has got only 2.6 GB altogether)?

Besides: Dogecoin uses Scrypt as PoW algo, not RandomX. xmrig does not support the Scrypt algo.

# Action History
- Created by: Cotternn | 2021-11-11T12:22:47+00:00
