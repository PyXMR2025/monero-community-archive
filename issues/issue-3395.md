---
title: MSR MOD not enabled, Windows 10
source_url: https://github.com/xmrig/xmrig/issues/3395
author: ghost
assignees: []
labels: []
created_at: '2023-12-31T17:14:18+00:00'
updated_at: '2023-12-31T17:47:28+00:00'
type: issue
status: closed
closed_at: '2023-12-31T17:47:28+00:00'
---

# Original Description
I keep getting the "FAILED TO APPLY MSR MOD" text when running the minew on my new Windows 10 pro laptop.
I've disabled all of the visualization, turned off Memory Integrity, and even took off SafeBoot in the BIOS; but I still get this problem. Capped around 140 h/s because of it.
![20231231_113201](https://github.com/xmrig/xmrig/assets/155317548/925e3d82-27e9-4d16-afa5-ee6c5aa650b6)
Is there a way to fix this, or am I f'ed?

# Discussion History
## SChernykh | 2023-12-31T17:21:02+00:00
Celeron N4100 doesn't support MSR.

## ghost | 2023-12-31T17:35:41+00:00
> Celeron N4100 doesn't support MSR.

Really? Darn. Thank you

# Action History
- Created by: ghost | 2023-12-31T17:14:18+00:00
- Closed at: 2023-12-31T17:47:28+00:00
