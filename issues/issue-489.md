---
title: cpu-affinity
source_url: https://github.com/xmrig/xmrig/issues/489
author: kuttkutt
assignees: []
labels: []
created_at: '2018-04-01T15:19:14+00:00'
updated_at: '2018-11-05T13:03:24+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:03:24+00:00'
---

# Original Description
Hello, 

I want to set xmrig to use cor 1, 2, 3 (Core 0 shall not be used)
In the help I found this: 

--cpu-affinity       set process affinity to CPU core(s), mask 0x3 for cores 0 and 1

So i guess this is binary coded 0x3 = 0b0011. So basically Core 1, 2, 3 should be 0b1110 = 0xE
I tried to do this in the config file:

"cpu-affinity" : "0xE",
or 
"cpu-affinity" : 14, (which is 0xE in decimal)

but there seems that always the same Cores are used.

I think I am making a mistake in Syntax. Can anyone tell me, what the correct one is to use only Core 1, 2, 3 on a 4 Core CPU?


PS: it seems to work if I do: "xmrig --cpu-affinity 0xE" - just not if I put it in the config file...

# Discussion History
## Balzhur | 2018-04-04T06:32:49+00:00
Correct syntax for config file is:
`"cpu-affinity": "0xE",	// set process affinity to CPU core(s), mask "0x3" for cores 0 and 1`

# Action History
- Created by: kuttkutt | 2018-04-01T15:19:14+00:00
- Closed at: 2018-11-05T13:03:24+00:00
