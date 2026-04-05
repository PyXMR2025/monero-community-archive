---
title: Ryzen 5 same rate with 2 threads and with 8
source_url: https://github.com/xmrig/xmrig/issues/2849
author: D0nVitalio
assignees: []
labels: []
created_at: '2021-12-30T19:57:27+00:00'
updated_at: '2021-12-31T12:51:33+00:00'
type: issue
status: closed
closed_at: '2021-12-31T12:51:32+00:00'
---

# Original Description
**Describe the bug**
Hi. If I run config without --threads=8 or with this setting hash rate is nearly the same. Why and maybe I do smth wrong? Huge pages and MSR is enabled.
[http://dl4.joxi.net/drive/2021/12/30/0052/3914/3428170/70/07ac0b983f.jpg](url)


# Discussion History
## Spudz76 | 2021-12-30T23:33:24+00:00
Hard to tell without startup output, and maybe some more info (but most of that is in the startup output).

## SChernykh | 2021-12-31T00:12:19+00:00
Ryzen 5 3400G: 4C/8T, but only 4 MB L3 cache. Don't try to run more than 2 threads, it won't help.
Edit: well, maybe try 4 threads because somehow it's faster in benchmarks: https://xmrig.com/benchmark?cpu=AMD+Ryzen+5+3400G+with+Radeon+Vega+Graphics

## D0nVitalio | 2021-12-31T12:51:32+00:00
@SChernykh thanks. Closing.

# Action History
- Created by: D0nVitalio | 2021-12-30T19:57:27+00:00
- Closed at: 2021-12-31T12:51:32+00:00
