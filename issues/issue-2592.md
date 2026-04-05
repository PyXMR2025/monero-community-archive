---
title: Difference between XMRig-Cuda and XMRig-NVIDIA
source_url: https://github.com/xmrig/xmrig/issues/2592
author: HimDek
assignees: []
labels: []
created_at: '2021-09-20T12:34:53+00:00'
updated_at: '2021-09-22T03:12:57+00:00'
type: issue
status: closed
closed_at: '2021-09-22T03:12:57+00:00'
---

# Original Description
What exactly is [XMRig-Nvidia](https://github.com/xmrig/xmrig-nvidia), and how is it different from [XMRig-Cuda](https://github.com/xmrig/xmrig-cuda)?

# Discussion History
## Spudz76 | 2021-09-20T12:43:34+00:00
xmrig-nvidia was a separate miner that is deprecated when xmrig-cuda became a plugin for regular xmrig.

## HimDek | 2021-09-20T12:49:30+00:00
Is [XMRig-AMD](https://github.com/xmrig/xmrig-amd) deprecated too?

## Spudz76 | 2021-09-20T12:52:24+00:00
Yes.  Only exist for posterity.  Always check dates and freshness.

OpenCL (AMD) is included in main xmrig (no plugin, no separate plugin project)

Technically CUDA was also included into the main app for a while, but CUDA has weird compilation requirements so it was split to a plugin library so the main app can be compiled with today's compilers and CUDA can be compiled with gcc-5 or whatever terrible garbage it requires per CUDA Toolkit version (always changing).

## HimDek | 2021-09-20T13:01:39+00:00
Even main XMRig app has some weird requirement for compiling. I had to download sources for XMRig as well as XMRig Deps to compile in MSVCC. If XMRig Deps is required for compiling main XMRig, why are they in two different repos?

## Spudz76 | 2021-09-20T13:13:27+00:00
Because the Windows deps are all binaries and would really twerk the commit history of a code repo (cause rebase and such to take a long time for binary comparisons).  Having it split external keeps the main repo clean of binary garbage.

Linux deps are included in the main repo in source (text) form and can be compiled easily, where getting them to compile under MSVC is a real pain, so the work has been done for us in the xmrig-deps repo.

# Action History
- Created by: HimDek | 2021-09-20T12:34:53+00:00
- Closed at: 2021-09-22T03:12:57+00:00
