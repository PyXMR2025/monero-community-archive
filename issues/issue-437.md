---
title: ARMv6 support
source_url: https://github.com/xmrig/xmrig/issues/437
author: ghost
assignees: []
labels:
- wontfix
- arm
created_at: '2018-03-11T23:16:52+00:00'
updated_at: '2018-11-05T12:57:34+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:57:34+00:00'
---

# Original Description
Are there plans to add support for ARMv6 architecture? I know hashrates on those sorts of devices will generally be low, but so is power consumption and hardware cost.

I personally have a fleet of Raspberry Pi Zeros that I'd like to put to work. I've managed to get an implementation of cpuminer-multi built and running on one of them, but I'd prefer the historically better performance of Xmrig!  I've attempted Xmrig as well, but after some modifications to flags.cmake and cpu.cmake to customize the build and bypass the CPU identification, the build still runs into problems in SSE2NEON.h if I remember correctly.

Cheers.

# Discussion History
# Action History
- Created by: ghost | 2018-03-11T23:16:52+00:00
- Closed at: 2018-11-05T12:57:34+00:00
