---
title: XMrig 6.8.1 with Nicehash gets "failed to allocate RandomX dataset, switch
  to slow mode"
source_url: https://github.com/xmrig/xmrig/issues/2106
author: D0nVitalio
assignees: []
labels: []
created_at: '2021-02-15T18:38:14+00:00'
updated_at: '2021-02-16T14:54:34+00:00'
type: issue
status: closed
closed_at: '2021-02-16T14:54:34+00:00'
---

# Original Description
Hi.
**Describe the bug**
When Nicehash running and mining, I start XMrig 6.8.1 and get lower hashrate and get "failed to allocate RandomX dataset, switch to slow mode". Get 129H/s when both running and 500+H/s (without "failed to allocate..") when only XMrig running. Huge pages enabled.

**Required data**
 - OS: Win10x64, 1909.
 - For GPU related issues: rx460 4gb, driver ver.21.1.1. Nicehash uses ~75% of vram. Total ram 8gb, CPU Q9450.

Is it possible to run XMrig and Nicehash without getting slow mode?

# Discussion History
## ghost | 2021-02-16T06:08:44+00:00
Have you tried to move to 6.8.2?

## D0nVitalio | 2021-02-16T13:29:36+00:00
> Have you tried to move to 6.8.2?

Yes, just now and it is "failed"

## SChernykh | 2021-02-16T13:32:38+00:00
Reboot and try to start XMRig first, before Nicehash.

## D0nVitalio | 2021-02-16T14:52:14+00:00
> Reboot and try to start XMRig first, before Nicehash.

This was first what I did. NBMiner crashes

## D0nVitalio | 2021-02-16T14:54:16+00:00
Just tried on Win7 - works good without fails.
This issue can be closed.
Thanks

## D0nVitalio | 2021-02-16T14:54:34+00:00
+

# Action History
- Created by: D0nVitalio | 2021-02-15T18:38:14+00:00
- Closed at: 2021-02-16T14:54:34+00:00
