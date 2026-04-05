---
title: RandomX Hashrate/RAM
source_url: https://github.com/xmrig/xmrig/issues/3049
author: vpts1202
assignees: []
labels: []
created_at: '2022-05-15T03:29:26+00:00'
updated_at: '2025-06-16T20:29:33+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:29:33+00:00'
---

# Original Description
Hello
Are any dynamic/online calculator or referencing table for correlation between RandomX  Hashrate  and server RAM available?

There is plenty mining hardware benchmarks/calculators but without RAM indications and the same model may have RAM as let say 8GB as well 16GB. That’s obvious that as bigger RAM as higher hashrate, but still I am in need for calculator or referencing table for precise estimations.


# Discussion History
## Spudz76 | 2022-05-15T03:37:40+00:00
On [xmrig benchmarks](https://xmrig.com/benchmark) you can click down into results and then (on new enough xmrigs) there is a Memory section you can click on and then it says the part numbers and what transfer rate (but not any timings like CL, but you can bet the top results were whatever gets 8ns or less CL, so like 14@3600).  You can also see if it was a server or desktop by the other section where the motherboard ID is posted (all xmrig versions).  You may have to scroll down the results to slower ones to find the top server board with server RAM result (desktops or workstations almost always beat servers).

Server RAM is usually intentionally slow and careful like 10ns CL or worse (plus ECC RDIMMs if it won't take UDIMMs) and the boards don't really offer much clocking support other than XMP or not.

## Spudz76 | 2022-05-15T03:41:46+00:00
Oh and the most important thing is the overall latency of memory accesses since it does a lot of them (mostly reads).  So if you can get all the timings shaved down on reads it helps the most, even if the write timings have to still be a bit fatter.  I only use the CL latency as a marker for the rest of the timings, it's mostly relative.  The full read cycle time may be more like 120ns but if the RAM sucks and has 10ns CL then it would be like 190ns or something total (commensurately worsening the hashrate).  Since the extra 70ns per read operation times billions is a lot of time waiting.

## vpts1202 | 2022-05-15T03:54:38+00:00
> Oh and the most important thing is the overall latency of memory accesses since it does a lot of them (mostly reads). So if you can get all the timings shaved down on reads it helps the most, even if the write timings have to still be a bit fatter. I only use the CL latency as a marker for the rest of the timings, it's mostly relative. The full read cycle time may be more like 120ns but if the RAM sucks and has 10ns CL then it would be like 190ns or something total (commensurately worsening the hashrate). Since the extra 70ns per read operation times billions is a lot of time waiting.

Thank you!
Got it.
What is the meaning memory 256GB__16of 32( 
https://xmrig.com/benchmark/3GBSo) ?
Does it mean that RAM of this model 256GB?


## Spudz76 | 2022-05-15T18:06:53+00:00
Click the header bar and it rolls out the Memory slot individual details.

`16 GB / DDR4 @ 2933 MHz / 36ASF2G72PZ-2G3B1`

and they had 16 of those (out of 32 available slots) or 256GB total.

## Spudz76 | 2022-05-15T18:14:11+00:00
2933 is of course slow compared to 3600.

Maybe if it was CL11 or CL12 @ 2933 it would be good (7.5ns or 8.18ns) but according to the part number it's CL17 (11.59ns lol eww, like I was saying about server RAM).  But you won't find "gaming" level RAM for RDIMM/server.

## vpts1202 | 2022-05-24T18:31:33+00:00
> 2933 is of course slow compared to 3600.
> 
> Maybe if it was CL11 or CL12 @ 2933 it would be good (7.5ns or 8.18ns) but according to the part number it's CL17 (11.59ns lol eww, like I was saying about server RAM). But you won't find "gaming" level RAM for RDIMM/server.

I have tried to monitor xmrig benchmarks
Still I am a bit confused, since there are huge gap in data for the same equipment but provided by different users.
Let me simplify my question : What would be the hashrate(roughly +/-, just for indication level) for VM with 16GB RAM as of now let say?
Thank you


## Spudz76 | 2022-05-24T19:18:10+00:00
Size doesn't matter as long as the dataset fits.  All that matters is how long it takes from read-request to data-in-hand (latency).

VM will always be slower than real hardware.

## Spudz76 | 2022-05-24T19:21:35+00:00
The reason the results are so spread out is a lot of things have effect on hashrate, not just RAM latency but also internal design decisions inside the CPU (thus Intels all suck compared to Ryzen for RandomX) or how stripped the OS was, etc.

# Action History
- Created by: vpts1202 | 2022-05-15T03:29:26+00:00
- Closed at: 2025-06-16T20:29:33+00:00
