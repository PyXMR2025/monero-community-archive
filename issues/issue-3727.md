---
title: Lower H/s after returning to xmrig
source_url: https://github.com/xmrig/xmrig/issues/3727
author: Oliver2008926
assignees: []
labels: []
created_at: '2025-10-30T07:45:49+00:00'
updated_at: '2025-10-30T10:58:15+00:00'
type: issue
status: closed
closed_at: '2025-10-30T10:58:15+00:00'
---

# Original Description
I decided to come back to mining after a year, and I have a much lower hash rate than I had last year. I first began (last year) mining on windows and I was getting around 2-3kH/s. Then I switched to linux and I was able to reach around 5-6kH/s maybe 7kH/s. Now I decided to come back, and after setting everything up, i get around 3.5kH/s. I have the MSR and huge pages on. Im using the ryzen 5 7530U. I also checked the xmrig benchmarks and they get around 4k on 8 threads, but i kinda could and want to get more...

# Discussion History
## SChernykh | 2025-10-30T09:46:32+00:00
How many threads does XMRig use for mining when you run it? It should be 8.

## Oliver2008926 | 2025-10-30T10:07:20+00:00
Yeah I'm running 8. But I noticed something. Im pool mining since I'd have to be really lucky to get something from solomining, and im using the supportxmr pool. And they show a different hashrate compared to the xmrig (sometimes much less, sometimes much more).
And should I try solo mining with this pc or no?
Thank you

## SChernykh | 2025-10-30T10:09:07+00:00
Pool shows your hashrate based on submitted shares, it's only an estimate. It can be higher or lower than the real hashrate because of luck fluctuations.

I wouldn't recommend solo mining with this low hashrate.

## Oliver2008926 | 2025-10-30T10:58:15+00:00
Thanks man

# Action History
- Created by: Oliver2008926 | 2025-10-30T07:45:49+00:00
- Closed at: 2025-10-30T10:58:15+00:00
