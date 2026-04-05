---
title: '"Illegal instruction" error running on armv8'
source_url: https://github.com/xmrig/xmrig/issues/230
author: claritise
assignees:
- xmrig
labels:
- enhancement
- arm
created_at: '2017-11-30T00:05:44+00:00'
updated_at: '2019-02-03T17:28:03+00:00'
type: issue
status: closed
closed_at: '2019-02-03T17:28:03+00:00'
---

# Original Description
This is on a pi3 with a 64 bit distro, compiled on the same pi. Not sure what is going wrong.

# Discussion History
## xmrig | 2017-11-30T00:08:29+00:00
Please show `cat /proc/cpuinfo` output. And what distro do you use?
Thank you.

## claritise | 2017-11-30T00:10:28+00:00
```pi@raspberrypi:~/xmrig$ cat /proc/cpuinfo
processor	: 0
BogoMIPS	: 38.40
Features	: fp asimd evtstrm crc32 cpuid
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

processor	: 1
BogoMIPS	: 38.40
Features	: fp asimd evtstrm crc32 cpuid
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

processor	: 2
BogoMIPS	: 38.40
Features	: fp asimd evtstrm crc32 cpuid
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4

processor	: 3
BogoMIPS	: 38.40
Features	: fp asimd evtstrm crc32 cpuid
CPU implementer	: 0x41
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0xd03
CPU revision	: 4
`

This is the distro 
https://github.com/bamarni/pi64

## xmrig | 2017-11-30T00:18:23+00:00
All right, hardware AES not supported. Currently ARM version lacks support for detect CPU features. So you need use software AES implementation, please add command line option `--av 3` or change `"av": 3,` in config file.

## claritise | 2017-11-30T00:19:21+00:00
Perfect!

## xmrig | 2019-02-03T17:28:03+00:00
Merge with #749 

# Action History
- Created by: claritise | 2017-11-30T00:05:44+00:00
- Closed at: 2019-02-03T17:28:03+00:00
