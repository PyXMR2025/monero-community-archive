---
title: AMD GPU memory allocation failure
source_url: https://github.com/xmrig/xmrig/issues/1603
author: d9beuD
assignees: []
labels: []
created_at: '2020-03-23T13:40:39+00:00'
updated_at: '2020-08-29T04:49:43+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:49:43+00:00'
---

# Original Description
**Describe the bug**
Since XMRig is a unified miner, I got problems mining with AMD GPU. I tired every single new release of 5.x with no fix.

**To Reproduce**
Build a rig with AMD GPUs, like 4 or 5 GPUs, run the latest version of XMRig on Windows 10.

**Expected behavior**
No error expected, just mining as it does before.

**Required data**
 
![Annotation 2020-03-23 105325](https://user-images.githubusercontent.com/53569029/77305191-e6038880-6cf5-11ea-91a6-1cfd39710307.jpg)

 - Config file or command line (without wallets) : I only enabled opencl mining and disabled CPU
 - OS: Windows 1903
 - For GPU related issues: 
  - Adrenaline 19.12.1

**Additional context**
I have absolutly no idea why I got this problem. After the memory failure, I need to force my computer to restart, because it is not responding anymore.


# Discussion History
## d9beuD | 2020-03-24T13:10:50+00:00
Ok I found out that it was my 2 R9 380 that was causing this problem because it only has 2 Go of VRAM. 

However, I still have issues, because all my 4 Go GPUs aren't mining at all. In the up-to-date Radeon Software I can see that they're not active (0%) and that the VRAM is almost full (80-85%).

# Action History
- Created by: d9beuD | 2020-03-23T13:40:39+00:00
- Closed at: 2020-08-29T04:49:43+00:00
