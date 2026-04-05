---
title: Haven hashrate problem with AMD Zen 3 "Cezanne"
source_url: https://github.com/xmrig/xmrig/issues/2680
author: Lonnegan
assignees: []
labels: []
created_at: '2021-11-10T23:27:35+00:00'
updated_at: '2021-11-26T11:57:18+00:00'
type: issue
status: closed
closed_at: '2021-11-26T11:57:18+00:00'
---

# Original Description
Hi,

regular Zen 3 "Vermeer" based Ryzen 5000, e.g. Ryzen 5 5600X, work fine with Haven algo cn/xhv. They are hashing around 700 H/s (single CCD).

But there is another Zen 3 model out there, the Ryzen 5 5600G "Cezanne". It has an iGPU (which isn't used here so doesn't matter) and just 16 MB L3 cache instead of 32 MB. So Cezanne can only start 4 threads mining cn/xhv because of the scratchpad size (4 MB) of that algo (16 MB / 4 MB per thread = 4 threads).

That's ok and is the same as the older Zen 1 type CPUs like Ryzen 5 1600. But those old CPU are capable of hashing over 200 H/s with Haven. Cezanne instead is stuck at under 90 H/s. So there's something wrong.
![haven-cezanne](https://user-images.githubusercontent.com/60088495/141209693-083f6402-8704-4b94-bd4e-9df39e319380.png)

Other algos like Monero (rx/0; 5500 H/s) or Dero (astrobwt; 875 H/s) are behaving normal on Cezanne, the hashrates are where you would expect them for arc, threads, clock frequency and L3 cache. It's just cn/xhv which is way too slow.

How can I help debugging?

# Discussion History
## SChernykh | 2021-11-10T23:33:54+00:00
Try to run https://github.com/xmrig/xmrig/releases/tag/v6.8.1 and then compare with https://github.com/xmrig/xmrig/releases/tag/v6.8.2

## Lonnegan | 2021-11-10T23:45:44+00:00
Cool, you are on the right track! Version 6.8.1 is performing like it should and better: over 300 H/s!
![haven-cezanne-6 8 1](https://user-images.githubusercontent.com/60088495/141211325-a1d91ac8-fca5-4ad7-b7dc-950b2adc4765.png)

6.8.2 instead doesn't even start on Cezanne, crashes with no error message! Seems like the optimization done between 6.8.1 and 6.8.2 for Zen 3 "Vermeer" are somehow bad for Zen 3 "Cezanne".

The MSR mod doesn't matter. 6.8.2 crashes with and without MSR mod and 6.15.3 is slow with and even slower (73 H/s) without MSR mod.

## Lonnegan | 2021-11-11T08:17:49+00:00
Can I download the fixed binary somewhere for testing? I have the Cezanne system here only today.

# Action History
- Created by: Lonnegan | 2021-11-10T23:27:35+00:00
- Closed at: 2021-11-26T11:57:18+00:00
