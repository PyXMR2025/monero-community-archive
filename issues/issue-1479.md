---
title: OpenCL on Raspberry Pi not working unfortunately but could it?
source_url: https://github.com/xmrig/xmrig/issues/1479
author: djbadders
assignees: []
labels: []
created_at: '2020-01-02T17:54:16+00:00'
updated_at: '2021-04-12T15:05:55+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:05:55+00:00'
---

# Original Description
**Describe the bug**
I have built xmrig on my Raspberry Pi 4 and can CPU mine albeit slowly, so wanted to see what using the GPU would give as it has a OpenCL 1.2 compatible GPU, but although I got xmrig to see the OpenCL platform it failed with the error "ocl disabled (no suitable configuration found)" and this is where I got stuck and don't know if there is a fix or not. It would be good to test the GPU performance. 

**To Reproduce**
Enable OpenCL on a Raspberry PI after installing VC4CL

**Expected behavior**
xmrig to use the GPU for hashing

**Required data**
 - Miner log as text or screenshot
![image](https://user-images.githubusercontent.com/34887832/71682812-a9746080-2d88-11ea-9c49-57b21a17a0bd.png)
 - Config file or command line (without wallets)
 - OS: Raspbian 10 buster
 - For GPU related issues: information about GPUs and driver version.
Arm 7 built in GPU - VideoCore IV GPU
Driver VC4CL 0.4

**Additional context**
Add any other context about the problem here.


# Discussion History
## ordtrogen | 2020-02-04T22:03:27+00:00
Look at the start page (https://github.com/xmrig/xmrig). I think this means on a Pi (ARM architecture), you can only CPU mine.

![image](https://user-images.githubusercontent.com/15184875/73791312-5dab4180-47a2-11ea-8a18-5a6959c5d965.png)


## grahamreeds | 2020-02-11T00:06:33+00:00
Also the Pi4 has VideoCore 6 but doe300 implementation of Open CL only supports VideoCore 4 (hence VC4CL).

# Action History
- Created by: djbadders | 2020-01-02T17:54:16+00:00
- Closed at: 2021-04-12T15:05:55+00:00
