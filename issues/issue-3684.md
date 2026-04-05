---
title: prefetching BIOS settings
source_url: https://github.com/xmrig/xmrig/issues/3684
author: fenderjaguarnet
assignees: []
labels: []
created_at: '2025-07-05T15:17:41+00:00'
updated_at: '2025-07-05T19:42:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
which of these should I enable/disable?

![Image](https://github.com/user-attachments/assets/ea91b5d6-a59f-41e8-a880-3474db35800a)

# Discussion History
## SChernykh | 2025-07-05T17:59:49+00:00
You shouldn't do it in BIOS because it will permanently slow down all programs on your PC. Disabling prefetchers only helps with RandomX mining. XMRig already does it via MSR mod and it reverts the settings when it exits.

## fenderjaguarnet | 2025-07-05T19:42:45+00:00
thanks, but I only use it as a mining rig, ever. 

# Action History
- Created by: fenderjaguarnet | 2025-07-05T15:17:41+00:00
