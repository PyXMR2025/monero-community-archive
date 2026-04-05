---
title: 'libnvrtc.so.10.1: cannot open shared object file: No such file or directory'
source_url: https://github.com/xmrig/xmrig/issues/2822
author: CasualVeemo
assignees: []
labels: []
created_at: '2021-12-18T16:30:03+00:00'
updated_at: '2023-12-08T21:46:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
when i try running xmrig with cuda on i always get this message. my drivers are up to date and i have rtx 3070 OC LHR version.

# Discussion History
## Spudz76 | 2021-12-18T22:43:41+00:00
What does `dpkg-query -l | grep cuda` say

And which distro (`lsb_release -a`)

## detherminal | 2023-12-08T20:36:20+00:00
I encountered this one too, Fedora 38 Cuda 12.3

EDIT:

Fixed it via downloading http://archive.ubuntu.com/ubuntu/pool/multiverse/n/nvidia-cuda-toolkit/libnvrtc10.1_10.1.243-3_amd64.deb and extracting it via `ar x libnvrtc10.1_10.1.243-3_amd64.deb` then found the libnvrtc.so.10.1 and moved it near to the xmrig, it started working flawlessly.

# Action History
- Created by: CasualVeemo | 2021-12-18T16:30:03+00:00
