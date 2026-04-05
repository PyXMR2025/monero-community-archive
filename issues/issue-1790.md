---
title: High number of Compute Errors on cn-Heavy
source_url: https://github.com/xmrig/xmrig/issues/1790
author: Vestibule22
assignees: []
labels: []
created_at: '2020-07-29T03:49:23+00:00'
updated_at: '2021-04-12T14:52:48+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:52:48+00:00'
---

# Original Description
**Describe the bug**
Upgraded to 6.3 and changed algo to cn-heavy/xhv mining with 6 RX 580s 8G.  Started fresh with new config file to compile GPU settings ran when starting fresh config file with opencl : true

**To Reproduce**
Start rig with fresh config file, stock rx 580 8G settings and let it run.  Low hashrate and after a little bit, compute errors start to pop up for all GPUs.  Running Adrenaline 2020 20.4.2 drivers. Adjustments to clock settings up or down produce compute errors as well or go unstable.

**Expected behavior**
No compute errors for GPUs while mining. 

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets) attached
 - OS: [e.g. Windows] - Windows 10 version 2004 x64
 - For GPU related issues: information about GPUs and driver version.
XFX RX 580 8G Black Edition Samsung Memory switch set to compute mode/Adrenaline setting to compute
[config file.txt](https://github.com/xmrig/xmrig/files/4992138/config.file.txt)


**Additional context**
Add any other context about the problem here.


# Discussion History
## perlsbeforeswine | 2020-07-31T14:03:17+00:00
The exact same thing occurs on Linux boxes too. I've tested on Ubuntu 18.4 and Ubuntu 20.4 with rx 580 and rx 480 GPUs.

## Vestibule22 | 2020-08-19T18:37:22+00:00
It looks like this one still hasnt been reviewed.  It is unfortunate bc I am potentially losing a lot of accepted shares due to this.  Unfortunately the pool I am on requires the most up to date Xmrig so I am stuck with this until it is addressed.  Was hoping there would be some review or at least questions from Xmrig staff...

## SChernykh | 2020-08-20T17:23:41+00:00
Config file from the first post point to etnpool.thorshammer.cc which is not a Haven pool. I've checked `cn-heavy/xhv` on my Vega 64 with 20.7.2 drivers on Windows 10 and it works fine. I don't have RX cards for testing unfortunately. You can try cleaning xmrig OpenCL cache in `%USERPROFILE%\AppData\Local\xmrig\.cache`

## Vestibule22 | 2020-08-20T17:33:00+00:00
That is correct that it is pointing at a Proxy.  That proxy is mining cn-heavy/xhv.  I have cleared my OpenCL cache, I have cleared my xmrig cache and loaded a new config file, and have adjusted my settings on the GPUs Overclocking, Underclocking, base, etc.  I will look at seeing about the drivers again and maybe there was something wrong with the download or something.

## SChernykh | 2020-08-20T18:12:19+00:00
If you're using a proxy, make sure it supports the latest Haven hard fork which increased the size of mining blob.

## Vestibule22 | 2020-08-20T19:02:50+00:00
Yes it does which was the reason that we had to update to the most recent Xmrig.  Otherwise it would not have worked.  Additionally, these compute errors did not start until upgrading to the latest Xmrig.  So all other things have been exhausted except for the review of the actual Xmrig release itself to know what is going on.

# Action History
- Created by: Vestibule22 | 2020-07-29T03:49:23+00:00
- Closed at: 2021-04-12T14:52:48+00:00
