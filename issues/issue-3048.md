---
title: Lenovo ThinkCentre with i5 4590T
source_url: https://github.com/xmrig/xmrig/issues/3048
author: mrgreen3
assignees: []
labels: []
created_at: '2022-05-11T18:30:58+00:00'
updated_at: '2025-06-28T10:36:49+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:36:49+00:00'
---

# Original Description
Am running Xmrig on an intel 4590T with 8Gb of ram solar powered miner. Currently I can only get one core running, so am using 25% of cpu power. Tried adding --threads=2 to command line but had no effect. 

Have searched online but not found any real answer, other than adding more threads.

Is the cpu just not up to the job? Or do I need more ram? 

# Discussion History
## Spudz76 | 2022-05-11T19:55:32+00:00
`threads` commandline option (and other "hints") only work if it is generating new profiles.

So you have to first edit the `config.json` and find the `cpu` section and then within that find the algorithm profiles and remove them.  Then run the very next time with the threads option and it will force all algorithms to use that many threads.  Note if you are algo-switching (such as on MoneroOcean) then `threads` will force even algorithms that would only select one thread, to use two, and enable algorithms that won't work.  This is because `threads` makes a `"*"` algorithm profile.

So really the ideal method (I use) is to run once with no options, make a copy of that config.json to like config-full.json, and then go find those same thread profiles (specifically the one that applies to your algo if you're running a single one / not switching) and remove a number from each array.  Normal should use 3 threads for rx/0 on that CPU.  So you make one with 1, 2, 3 threads in the profile, and save them to be dropped-in as active config.json.  You could also then automate the copying-over of the three levels as it watches your available solar input, and xmrig will reload a changed/replaced config.json "on the fly".

## mrgreen3 | 2022-05-12T07:34:30+00:00
Removed algos from cpu section and tried --threads=2 again and still have same result.

`2022-05-12 09:28:23.319]  cpu      use argon2 implementation AVX2`

Little confused about the array option (may need to read up more on that)

As a test I was just trying to mine DOGE coin, so far no real luck. 

Thank you for help.

## mrgreen3 | 2022-05-16T09:31:02+00:00
So after searching online I found something that worked.

`"rx": [0,1],`

This simple change allowed me to have two cores running, temps are up so rig will need some extra cooling.

# Action History
- Created by: mrgreen3 | 2022-05-11T18:30:58+00:00
- Closed at: 2025-06-28T10:36:49+00:00
