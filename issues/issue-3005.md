---
title: 'fatal error: cannot open file ''/usr/lib/clc/kabini-amdgcn-mesa-mesa3d.bc'':
  No such file or directory'
source_url: https://github.com/xmrig/xmrig/issues/3005
author: DemonRx
assignees: []
labels: []
created_at: '2022-04-06T07:25:20+00:00'
updated_at: '2022-04-07T04:37:44+00:00'
type: issue
status: closed
closed_at: '2022-04-07T03:36:27+00:00'
---

# Original Description
This error comes up when trying to mine DERO with an AMD GPU. 

System:
  Ubuntu 21.10

GPU: 
  Kabini [Radeon HD 8400 / R3 Series]
    Advanced Micro Devices, Inc. [AMD/ATI]

Display: x11 server: X.Org 1.20.13 driver: loaded: amdgpu
OpenGL: renderer: AMD KABINI (DRM 3.41.0 5.13.0-39-generic LLVM 12.0.1) v: 4.6 Mesa 21.2.6 

Output of `./xmrig --print-platforms`:

```bash
Number of platforms:        2

  Index:                    0
  Profile:                  FULL_PROFILE
  Version:                  OpenCL 1.1 Mesa 21.2.6
  Name:                     Clover
  Vendor:                   Mesa
  Extensions:               cl_khr_icd

  Index:                    1
  Profile:                  FULL_PROFILE
  Version:                  OpenCL 1.2 AMD-APP (1445.5)
  Name:                     AMD Accelerated Parallel Processing
  Vendor:                   Advanced Micro Devices, Inc.
  Extensions:               cl_khr_icd cl_amd_event_callback cl_amd_offline_devices cl_amd_hsa 
```



# Discussion History
## Spudz76 | 2022-04-07T02:50:00+00:00
Mesa OpenCL doesn't work, use amdgpu-pro drivers.

But that might be impossible since amdgpu-pro generally doesn't support mobile/integrated chips.

Maybe the regular amdgpu driver from the kernel, with the amdgpu-pro opencl manually installed alongside, could work.

## DemonRx | 2022-04-07T03:36:27+00:00
Confirmed that, Mesa is a no-go. This is actually a laptop GPU. But i was able to resolve it specifically for my setup. Installing amdgpu-pro drivers ([amdgpu-pro-18.20-673703-ubuntu-18.04](https://www.amd.com/en/support/kb/release-notes/rn-prorad-lin-18-20)) did the trick. Also removed the *mesa-opencl-icd* package since it was of no use. 

Closing this as solved.

## Spudz76 | 2022-04-07T04:36:17+00:00
Yes I was also going to mention it probably needs an older amdgpu-pro as well, but you already used an older one and it worked out.  Anything newer than 20.40 or so generally is broken as heck unless you have the latest GPU family, in my experience.

And perhaps it's only the iGPU Vega's that amdgpu-pro won't do.  Mobile is probably okay (as proven here).

# Action History
- Created by: DemonRx | 2022-04-06T07:25:20+00:00
- Closed at: 2022-04-07T03:36:27+00:00
