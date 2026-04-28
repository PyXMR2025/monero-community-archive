---
title: EPYC 7742 (64C128T) 8x4GB 2400 MT/s Ram ~ 25% hashrate regression with rx/2
source_url: https://github.com/xmrig/xmrig/issues/3806
author: Motophan
assignees: []
labels: []
created_at: '2026-04-28T08:55:54+00:00'
updated_at: '2026-04-28T09:11:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I understand the rx/2 was made to slow down the JBOC (just a bunch of CPUs) bitmain hashboards, and they are expected to lose 30% of their hashrate, but when I did a bench for rx/2 I lost about 25%

Windows 11

rx/0 -> 45KH/s
rx/2 -> 34KH/s



# Discussion History
## SChernykh | 2026-04-28T09:11:27+00:00
This is a Zen 2 CPU. Other Zen 2 CPUs we tested didn't slow down that much: https://github.com/tevador/RandomX/blob/master/doc/design_v2.md#ryzen-9-3950x-zen-2--131w

Maybe your EPYC's power limit kicks in, because rx/2 does more than 1.5x computations per hash. Reminder that rx/2 is much heavier, so you can't compare hashrates directly. With 34 kh/s vs 45 kh/s, your CPU still does ~15% more RandomX and AES instructions per second.

Another reminder is that rx/2 was tuned for more modern CPUs: https://github.com/tevador/RandomX/blob/master/doc/design_v2.md#3-program-size-increase-from-256-to-384 so your result is expected.

# Action History
- Created by: Motophan | 2026-04-28T08:55:54+00:00
