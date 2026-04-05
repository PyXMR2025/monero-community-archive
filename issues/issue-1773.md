---
title: Performance Degradation on Kawpow With Latest Release - GTX 1080
source_url: https://github.com/xmrig/xmrig/issues/1773
author: breadsax
assignees: []
labels:
- CUDA
- kawpow
created_at: '2020-07-12T21:33:46+00:00'
updated_at: '2021-04-12T14:53:41+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:53:41+00:00'
---

# Original Description
I first noticed this building from source on Windows with Visual Studio 2019 and Cuda 11 latest release. I then ran the binary from the latest xmrig release with the latest cuda extension release and confirmed it wasn't just my compilation.

Performance went from 17 MH/S to 13 MH/S.

These cards are not great mining cards, but I am at a loss as to why this is happening. Cards on another rig had very nice increases when I compiled from source with the software above.

Any thoughts?

# Discussion History
## SChernykh | 2020-07-13T09:09:31+00:00
@breadsax Can you try setting `"threads" : 128` for KawPow in config.json? This is the only major thing that changed with the latest release (increased from 128 to 256).

P.S. Maybe you need to update drivers as CUDA 11 requires latest NVIDIA drivers to work properly.

## breadsax | 2020-07-13T21:58:19+00:00
Hello @SChernykh and thank you for your response.

I did some more testing today and found that it is the latest version of the CUDA plugin causing this. Do you have an example config file for changing the number of threads for kawpow or can this be changed from the command line syntax?

I am using the latest Nvidia driver 451.67

Thank you.

# Action History
- Created by: breadsax | 2020-07-12T21:33:46+00:00
- Closed at: 2021-04-12T14:53:41+00:00
