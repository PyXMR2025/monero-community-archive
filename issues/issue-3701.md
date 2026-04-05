---
title: service WinRing0_1_2_0 already exists, but with a different service name
source_url: https://github.com/xmrig/xmrig/issues/3701
author: jekv2
assignees: []
labels: []
created_at: '2025-08-30T19:09:25+00:00'
updated_at: '2025-08-31T02:21:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I don't understand this error. How do I get rid of it?

I disable svn in uefi which is virtualization and HypervisorEnforcedCodeIntegrity registry is disabled.

<img width="935" height="127" alt="Image" src="https://github.com/user-attachments/assets/043beb5e-de84-4157-bc60-c7ea895267ee" />

# Discussion History
## SChernykh | 2025-08-30T20:07:32+00:00
It's not an error. It means there is some other software on your PC that installed this driver before XMRig. It can be something like RGB control software, or a hardware monitor and so on.

## jekv2 | 2025-08-31T00:47:58+00:00
> It's not an error. It means there is some other software on your PC that installed this driver before XMRig. It can be something like RGB control software, or a hardware monitor and so on.

I do have openrgb installed, hwinfo64, msiafterburner. Will this effect mining speed, it being installed prior?

## geekwilliams | 2025-08-31T02:21:49+00:00
It should not, since it's the same driver xmrig would've otherwise installed 

# Action History
- Created by: jekv2 | 2025-08-30T19:09:25+00:00
