---
title: AstroBWT crashes rig (6800 XT)
source_url: https://github.com/xmrig/xmrig/issues/2005
author: fm407
assignees: []
labels:
- bug
- opencl
created_at: '2020-12-24T23:28:11+00:00'
updated_at: '2021-04-12T14:26:33+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:26:33+00:00'
---

# Original Description
**Describe the bug**
When using astrobwt algo the rig bluscreens or freezes and then reboots

**To Reproduce**
mine Dero with 6800XT + cpu

**Expected behavior**
not crash the system

**Required data**
Windows v. 1909 latest patch level, 

* OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3188.4)
* OPENCL GPU   #0 0e:00.0 AMD Radeon RX 6800 XT (gfx1030) 2015 MHz cu:36 mem:13695/16368 MB

**Additional context**
it happens only with astrobwt algo

# Discussion History
## Spudz76 | 2020-12-25T18:09:50+00:00
AstroBWT doesn't actually work with OpenCL at all, so that is not surprising.

## fm407 | 2020-12-25T18:49:36+00:00
> AstroBWT doesn't actually work with OpenCL at all, so that is not surprising.

so, what's all of this for? https://github.com/xmrig/xmrig/pull/1602/commits/fbedf197aba11b24b3389818ffa45041d34d72d7

## SChernykh | 2020-12-25T20:56:05+00:00
It used to work before but now it crashes for me too. I guess it's a problem with newer AMD drivers.

## fm407 | 2020-12-26T03:18:54+00:00
[Details](https://i.imgur.com/6Ft72YY.png)

Not sure if its of any use, but i have attached my system specs

## SChernykh | 2020-12-27T15:45:10+00:00
https://github.com/xmrig/xmrig/pull/2009 should fix it

# Action History
- Created by: fm407 | 2020-12-24T23:28:11+00:00
- Closed at: 2021-04-12T14:26:33+00:00
