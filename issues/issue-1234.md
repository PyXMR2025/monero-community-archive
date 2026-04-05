---
title: CL_INVALID_PROGRAM
source_url: https://github.com/xmrig/xmrig/issues/1234
author: Amf1k
assignees: []
labels:
- bug
- opencl
created_at: '2019-10-11T11:35:45+00:00'
updated_at: '2019-11-29T07:57:35+00:00'
type: issue
status: closed
closed_at: '2019-11-29T07:57:35+00:00'
---

# Original Description
Radeon Settings Version - 2019.1004.1215.22045
View Release Notes - https://www.amd.com/en/support/kb/release-notes/rn-rad-win-19-10-1
Driver Packaging Version - 19.30.25.10-191004a-347338E-RadeonSoftwareAdrenalin2019
Provider - Advanced Micro Devices, Inc.
2D Driver Version - 8.1.1.1634
Direct3D® Version - 9.14.10.01410
OpenGL® Version - 26.20.11000.13571
AMD Audio Driver Version - 10.0.1.12
Vulkan™ Driver Version - 2.0.106
Vulkan™ API Version - 1.1.119
Graphics Card Manufacturer - Powered by AMD
Graphics Chipset - AMD Radeon R7 200 Series
Device ID - 683D
Vendor ID - 1002
SubSystem ID - E214
SubSystem Vendor ID - 174B
Revision ID - 00
Bus Type - PCI Express 3.0
Current Bus Settings - PCI Express 3.0 x4
BIOS Version - 015.016.000.001
BIOS Part Number - 113-21400XTHE-X03
BIOS Date - 2012/02/19 23:03
Memory Size - 1024 MB
Memory Type - GDDR5
Memory Clock - 1125 MHz
Core Clock - 1000 MHz
Total Memory Bandwidth - 72 GByte/s
Memory Bit Rate - 4.50 Gbps
2D Driver File Path - /REGISTRY/MACHINE/SYSTEM/CurrentControlSet/Control/Class/{4d36e968-e325-11ce-bfc1-08002be10318}/0004
OpenGL® API Version - 4.6
OpenCL™ API Version - 1.2

![1](https://user-images.githubusercontent.com/4735986/66648399-dc54ff80-ec44-11e9-83ae-f2c331607c14.png)
[config](https://mega.nz/#!ChlTSQiZ!39ZzwLpKmEEsESqfLwQDr4kxh0R3wbJn0iICu1pIzpE)


# Discussion History
## Amf1k | 2019-10-11T11:37:14+00:00
on xmrig-amd 2.14.6 everything starts well with a hashrate of ~130 h/s

## xmrig | 2019-10-11T14:45:43+00:00
What algorithm you try to mine? Also please show full output, right now beginning of error is truncated.
Thank you.

## Amf1k | 2019-10-14T04:49:44+00:00
[log and config](https://mega.nz/#F!mtVilIpb!PFx3DOs9ZZlDb8DxCx8zDg)
Algo - cn/r (its default config with donate pool)

## xmrig | 2019-11-15T07:24:03+00:00
This issue should be solved in dev branch.
Thank you.

## Amf1k | 2019-11-21T09:58:41+00:00
Thank you. fixed

# Action History
- Created by: Amf1k | 2019-10-11T11:35:45+00:00
- Closed at: 2019-11-29T07:57:35+00:00
