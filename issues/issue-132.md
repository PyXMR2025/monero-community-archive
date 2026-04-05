---
title: issue with --max-cpu-usage=
source_url: https://github.com/xmrig/xmrig/issues/132
author: ragekillen
assignees: []
labels:
- question
created_at: '2017-09-30T03:31:05+00:00'
updated_at: '2017-11-27T19:18:53+00:00'
type: issue
status: closed
closed_at: '2017-10-02T11:50:58+00:00'
---

# Original Description
hello i have set my .bat file with these settings
xmrig -o stratum+tcp://pool.minexmr.com:4444 -u user -p x --donate-level=5 -t 4 --max-cpu-usage=50

but my cpu is still at 100%, am i configuring it wrong or is there something wrong with the program. 

ps it was working correctly the first day but then stopped

# Discussion History
## xmrig | 2017-09-30T11:35:27+00:00
You manually specify threads count `-t 4` it overrides `--max-cpu-usage`.
Thank you.

## van7hu | 2017-11-27T17:49:47+00:00
My command is:
`xmrig -o pool.supportxmr.com:5555 -u [address] -p x --donate-level=5 --max-cpu-usage=50
`
and, cpu usage is 100% always.

## van7hu | 2017-11-27T17:51:26+00:00
Even, if I have 
`--max-cpu-usage=10`

The Cpu is always 100%

## ragekillen | 2017-11-27T19:00:09+00:00
o so you have the same issue as well glad its not only me :) 2 bad the thread was closed by xmrig

## xmrig | 2017-11-27T19:18:53+00:00
How many cores do you have? this option just change thread count.
If you have just one core, will used one thread, so it will be always 100%
For 2 cores, minimum is 50%
For 4, 25%.

# Action History
- Created by: ragekillen | 2017-09-30T03:31:05+00:00
- Closed at: 2017-10-02T11:50:58+00:00
