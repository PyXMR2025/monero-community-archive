---
title: Compilation takes a very long time on raspberry pi zero w
source_url: https://github.com/monero-project/monero/issues/8674
author: MuzuWeb
assignees: []
labels: []
created_at: '2022-12-11T12:57:03+00:00'
updated_at: '2022-12-21T02:38:04+00:00'
type: issue
status: closed
closed_at: '2022-12-21T02:38:04+00:00'
---

# Original Description
Hello, i am compiling the monero CLI wallet for my raspberry pi zero w because there is no releases for armv6 and it takes a
very long time (it's been like 13 hours).
In the README file, it says to wait 4 to 6 hours, it is normal ?
Thanks in advance for answers.

# Discussion History
## selsta | 2022-12-11T13:37:04+00:00
This specific Raspberry will likely be too weak to run a monero node, it only has 512MB RAM.

## afungible | 2022-12-21T02:35:28+00:00
try only `-j `option to compile fastest (you won't be able to do anything else on PI)

OR
use make `-jN
`
The -j flag specifies how many threads you want to allot for compiling. where `N` is the max number of threads you wish to allocate. The rule of thumb is to make `N = the number of cores your CPU has`. So if you are on a dual core machine, you may use -j2, whereas on an quad-core machine, use -j4 

I use `make -j4,` for example.

EDIT: RaspberryZero I see may be single core. If its a single core, -j4 may be optimized to -j1 but you can try. 


## selsta | 2022-12-21T02:38:04+00:00
You need about 2.5GB RAM per make job. The Raspberry is single core and has 512MB RAM. -j2 wouldn't even work on it.

Closing as it's simply weak hardware.

# Action History
- Created by: MuzuWeb | 2022-12-11T12:57:03+00:00
- Closed at: 2022-12-21T02:38:04+00:00
