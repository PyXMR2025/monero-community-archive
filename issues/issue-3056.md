---
title: CAN YOU LAUNCH AN SUPPPORT FOR MINING ON AMD MI 100 GPU WITH ROCM 5.0.0/+ DRIVERS
source_url: https://github.com/xmrig/xmrig/issues/3056
author: nanmuganaiyar
assignees: []
labels: []
created_at: '2022-05-22T13:50:12+00:00'
updated_at: '2025-06-28T10:35:17+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:35:17+00:00'
---

# Original Description
Xmrig is not recognizing my amd mi100 devices i have rocm 5.0 installed and i cant and dont want to shift to amdpro gpu drivers

# Discussion History
## Spudz76 | 2022-05-22T17:32:41+00:00
ROCm has never worked so I doubt it.

I have had great luck installing amdgpu-pro and then removing the dkms component so that it runs hybrid with the normal kernel amdgpu driver but with the proprietary OpenCL layer on it.  perhaps the same trick works if you run the ROCm driver but the amdgpu-pro OpenCL parts, since the broken part of ROCm is generally the OpenCL support.

## nanmuganaiyar | 2022-05-23T10:12:35+00:00
every try will be appreciated as when im trying eth mining xmrig gets an devil eye on me

## DeeDeeRanged | 2022-05-28T08:24:29+00:00
AFAIK xmrig does not support eth and it never has.

# Action History
- Created by: nanmuganaiyar | 2022-05-22T13:50:12+00:00
- Closed at: 2025-06-28T10:35:17+00:00
