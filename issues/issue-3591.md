---
title: Can you add config option for pause on % of CPU usage?
source_url: https://github.com/xmrig/xmrig/issues/3591
author: alanhasgari
assignees: []
labels:
- question
created_at: '2024-11-26T14:02:53+00:00'
updated_at: '2025-06-16T19:34:32+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:34:32+00:00'
---

# Original Description
I run xmrig on my personal PC, but also have a few background apps that occasionally cycle and cause usage spikes even when unattended. When this happens, sometimes the PC will just lock up and freeze until manual reboot.

It would be great if we could see a config option to have xmrig pause when PC goes above a certain CPU usage percentage, then resume when CPU usage falls below that threshold.

Example; 

Xmrig pause above 75%, then resume below 75%.

Could such an option work?

Thanks;

# Discussion History
## SChernykh | 2024-11-26T21:33:10+00:00
Your PC shouldn't lock up and freeze. It's most likely unstable. You can set `priority` in config.json to 1, and XMRig will run with lowest priority: https://xmrig.com/docs/miner/config/cpu#priority

## alanhasgari | 2024-11-27T00:13:40+00:00
Thanks for the reply.

When I set the priority to anything below Normal, the hashrate drops, even had xmrig crash the one time.

This issue I'm having doesn't exist on Windows 7 or 10, didn't exist in 11 until 24H2; none of the apps are unstable, but the way Windows is handling the processes is quite frustrating.

My suggestion could be one way to solve this. You may very well ignore this suggestion, but I thought I'd mention it.

Thanks;

# Action History
- Created by: alanhasgari | 2024-11-26T14:02:53+00:00
- Closed at: 2025-06-16T19:34:32+00:00
