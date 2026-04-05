---
title: WHY IS the Hash rate of 7840HS with DDR5 5600MEMS lower than which of 5800H
  DDR4 3200?
source_url: https://github.com/xmrig/xmrig/issues/3375
author: JemZhu
assignees: []
labels: []
created_at: '2023-12-07T17:11:34+00:00'
updated_at: '2025-06-16T19:55:26+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:55:26+00:00'
---

# Original Description
7840HS +32G DDR5 5600  hash rate is 4.7k H/s.
my another old laptop with 5800H + 32G DDR4 @ 3200Mhz, it's hash rate is 5.6K H/s?

both computers are win11 OS and with HUGE PAGES ON and ADMIN authurity.

Anyone knows why?

# Discussion History
## SlavisaBakic | 2023-12-07T20:23:30+00:00
What models of laptops exactly? Cooling and max power consumption have huge imact on CPU performance in laptops. 

## SChernykh | 2023-12-07T20:58:59+00:00
Hashrate depends most on the L3 cache size available, then on memory latency. These 2 CPUs have the same number of cores/threads and the same L3 cache size. But DDR4-3200 can have better latency than DDR5-5600 because of better timings.

## JemZhu | 2023-12-08T04:07:08+00:00
> What models of laptops exactly? Cooling and max power consumption have huge imact on CPU performance in laptops.

5800H lenovo R9000P @ balance mode, 7840hs Beelink Mini PC @ TDP 65W,

## SlavisaBakic | 2023-12-08T10:53:36+00:00
My guess is that Legion of your have better cooling than Beelink and higher power limit but only way to determine it is to run xmrig and monitor temepratures and power consumption in HWInfo.

## MedMall | 2024-03-12T15:45:24+00:00
> But DDR4-3200 can have better latency than DDR5-5600 because of better timings.

Does this mean that, all other things being equal, the hashrate on DDR4 will be higher than on DDR5, because in the first case the latency is always lower?



# Action History
- Created by: JemZhu | 2023-12-07T17:11:34+00:00
- Closed at: 2025-06-16T19:55:26+00:00
