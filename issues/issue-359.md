---
title: AMD Geode Support
source_url: https://github.com/xmrig/xmrig/issues/359
author: Abaita
assignees: []
labels: []
created_at: '2018-01-24T12:04:55+00:00'
updated_at: '2018-11-05T12:46:47+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:46:47+00:00'
---

# Original Description
I am running FreeBSD 10.4 on Alix 1.c board which has an AMD Geode LX800 CPU. First i tried to compile the code using gcc but that fail at the final linking step complaining about missing atomic_... constants. Then i tried to compile using clang which worked fine but sadly it is not possible to launch the program, it end in a core.dump.
I know that the performance of the CPU is probably just about 10H/s but i am just curious if it is possible to run xmrig on a Geode CPU. That CPU is/was often used for firewalls because it has an hardware-encryption feature which could also be usefull for mining i hope. See also https://www.twam.info/hardware/alix/using-geodes-aes-engine-on-alix3d3

# Discussion History
## Abaita | 2018-01-24T20:16:03+00:00
I have added "-latomic" to build/CMakeFiles/xmrig.dir/link.txt, now it also builds using gcc but it still fails on startup:
Illegal instruction (core dumped)

## yuhong | 2018-01-25T04:43:15+00:00
doesn't look suitable. remember that Monero's AES is slightly different from normal AES.

## Abaita | 2018-01-25T19:44:50+00:00
I know that the performance is weak but it should be possible to run the code, right? Even without support of the integrated crypto-device it should be able to execute the software-aes like some people doing it on their raspberries. How can i find out by myself what that illegal instruction is? is there a debug-mode?

## yuhong | 2018-01-25T20:53:23+00:00
AFAIK the miner requires SSE2 which the Geode don't support.

## Abaita | 2018-01-26T22:34:08+00:00
ok, so basically the same issue like there was for arm in #94 . Since Geode is pretty outdated nobody will add support for it. i will look for some other use for it. thanks.

# Action History
- Created by: Abaita | 2018-01-24T12:04:55+00:00
- Closed at: 2018-11-05T12:46:47+00:00
