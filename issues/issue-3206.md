---
title: FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW despite running in administrative
  mode.
source_url: https://github.com/xmrig/xmrig/issues/3206
author: dogunbound
assignees: []
labels: []
created_at: '2023-02-02T01:51:58+00:00'
updated_at: '2024-01-06T23:03:04+00:00'
type: issue
status: closed
closed_at: '2023-02-02T13:33:16+00:00'
---

# Original Description
**Describe the bug**
cannot set MSR 0x000001a4 to 0x00000000000000f <- cannot set memory addresses for whatever reason.
FAILED TO APLY MSR MOD, HASHRATE WILL BE LOW

**To Reproduce**
I don't know how to reproduce it reliably across many systems, I just know my system is having this error.

**Expected behavior**
MSR mod is applied

**Required data**
https://user-images.githubusercontent.com/64436119/216211534-0bab0c14-8ea7-4b93-9d74-4ea0e9d4e022.mp4


There might be something I missed. Maybe there is a flag or argument I can pass into xmrig that changes how MSR works that I do not know of.


# Discussion History
## SChernykh | 2023-02-02T06:36:15+00:00
It's running in a VM - MSR mod doesn't work in a VM. You have to disable memory integrity: https://www.elevenforum.com/t/enable-or-disable-core-isolation-memory-integrity-in-windows-11.4942/
If it doesn't help, disable Secure Boot in BIOS.

## dogunbound | 2023-02-02T13:33:16+00:00
Awesome. I didn't know windows 11 ran a VM be default. It works now!

## codercodingthecode | 2024-01-06T23:03:03+00:00
Not quite, memory integrity is disabled, I'm running in Admin mode and still display VM

# Action History
- Created by: dogunbound | 2023-02-02T01:51:58+00:00
- Closed at: 2023-02-02T13:33:16+00:00
