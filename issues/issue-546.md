---
title: 'Out of memory on secound GPU   : Newbie Question'
source_url: https://github.com/xmrig/xmrig/issues/546
author: cat12d12
assignees: []
labels: []
created_at: '2018-04-12T15:51:34+00:00'
updated_at: '2018-11-05T06:59:30+00:00'
type: issue
status: closed
closed_at: '2018-11-05T06:59:30+00:00'
---

# Original Description
I cannot seem to get this to run via Awesome miner... can anyone advise simple instructions . i think i need to set some variables but where ? and what values? i don't understand

This is the  report  when i run the diags in awesome... it works if i run it on another machine with a single 1050 TI  card but on the bigger rig with multiple cards  it fails and says out of memory..


>  * VERSIONS:     XMRig/2.5.2 libuv/1.19.2 CUDA/9.10 MSVC/2015
>  * CPU:          Intel(R) Pentium(R) CPU G4560 @ 3.50GHz (1) x64 AES-NI
>  * GPU #0:       GeForce GTX 1080 Ti @ 1657/5505 MHz 54x84 6x25 arch:61 SMX:28
>  * GPU #1:       GeForce GTX 1080 Ti @ 1657/5505 MHz 54x84 6x25 arch:61 SMX:28
>  * GPU #2:       GeForce GTX 1080 Ti @ 1657/5505 MHz 54x84 6x25 arch:61 SMX:28
>  * GPU #3:       GeForce GTX 1080 Ti @ 1657/5505 MHz 54x84 6x25 arch:61 SMX:28
>  * GPU #4:       GeForce GTX 1050 Ti @ 1392/3504 MHz 36x18 8x25 arch:61 SMX:6
>  * GPU #5:       GeForce GTX 1050 Ti @ 1392/3504 MHz 36x18 8x25 arch:61 SMX:6
>  * ALGO:         cryptonight, donate=1%
>  * POOL #1:      europe.cryptonight-hub.miningpoolhub.com:20580
>  * API PORT:     4029
>  * COMMANDS:     'h' hashrate, 'e' health, 'p' pause, 'r' resume
> [2018-04-12 12:22:08] use pool europe.cryptonight-hub.miningpoolhub.com:20580 172.104.76.21
> [2018-04-12 12:22:08] new job from europe.cryptonight-hub.miningpoolhub.com:20580 diff 97281

**> [CUDA] Error gpu 2: <cryptonight_extra_cpu_init>:230 "out of memory"**
 

# Discussion History
# Action History
- Created by: cat12d12 | 2018-04-12T15:51:34+00:00
- Closed at: 2018-11-05T06:59:30+00:00
