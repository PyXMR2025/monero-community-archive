---
title: Scheduled mining pause
source_url: https://github.com/xmrig/xmrig/issues/2696
author: jututt
assignees: []
labels: []
created_at: '2021-11-15T15:46:12+00:00'
updated_at: '2025-01-26T03:51:47+00:00'
type: issue
status: closed
closed_at: '2025-01-26T03:51:47+00:00'
---

# Original Description
I'd like this feature to be implemented: scheduled pause of mining of x minutes every xxx minutes,
i.e. adding `"scheduled-pause": 5, 120,` in `config.json` would pause mining for 5 minutes every two hours of working.

Thus to give a break to cpu, fans, power supplies

# Discussion History
## SChernykh | 2021-11-15T18:28:15+00:00
It's a bad idea. Constant load is better for hardware longevity. Thermal cycles when it switches between full load and idle are bad.

## SEVENID | 2022-12-17T04:35:48+00:00
Good idea: this way you can mine at night or when your electricity is cheaper without using cron or systemd units.

# Action History
- Created by: jututt | 2021-11-15T15:46:12+00:00
- Closed at: 2025-01-26T03:51:47+00:00
