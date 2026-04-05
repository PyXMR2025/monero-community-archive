---
title: <AstroBWT_Dero::hash>:188 "an illegal memory access was encountered"
source_url: https://github.com/xmrig/xmrig/issues/2045
author: ghost
assignees: []
labels: []
created_at: '2021-01-17T08:45:10+00:00'
updated_at: '2021-02-11T13:51:01+00:00'
type: issue
status: closed
closed_at: '2021-02-11T13:51:01+00:00'
---

# Original Description
This following error is happening,
**'thread #0 failed with error <AstroBWT_Dero::hash>:188 "an illegal memory access was encountered"'**

It occcurs when i'm simply moving the command prompt window to my second display (dual screen), this happens when i'm slightly overclocking my video card as well. 

I'm working with a thunderbolt/eGPU and Nvidia CUDA 11.1 dsiplay drivers.
Here is my command line : **xmrig.exe -a astrobwt --no-cpu --cuda -o DOMAIN:PORT -u WALLET -p w=123 -k**

# Discussion History
## Spudz76 | 2021-01-24T21:30:29+00:00
What GPU though

## ghost | 2021-01-30T13:07:05+00:00
It's an Asus GTX 970

## ghost | 2021-01-30T17:15:20+00:00
Any flag to set in case of debug from command line ?

## ghost | 2021-02-11T13:51:01+00:00
Issue not resolved

# Action History
- Created by: ghost | 2021-01-17T08:45:10+00:00
- Closed at: 2021-02-11T13:51:01+00:00
