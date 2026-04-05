---
title: Windows Defender Sever Alert on xmrig.exe with Program:Win32/Unwaders.A!ml
source_url: https://github.com/xmrig/xmrig/issues/1288
author: LeMoussel
assignees: []
labels:
- av
created_at: '2019-11-14T14:34:00+00:00'
updated_at: '2019-12-22T19:36:13+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:36:13+00:00'
---

# Original Description
I build `xmrig` on Win 10/VS 2019  with [prebuilt dependencies](https://github.com/xmrig/xmrig-deps/releases)
Windows Defender is detecting that `xmrig.exe` is infect by [Program:Win32/Unwaders.A!ml](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?name=Program%3aWin32%2fUnwaders.A!ml&threatid=242872)

Do you know whats up with that?

# Discussion History
## pawelantczak | 2019-11-15T21:30:19+00:00
Just whitelist xmrig folders in AV.

## Spudz76 | 2019-11-18T19:53:49+00:00
Standard idiocy due to trojan-payload miners.  "Average Moron Users" don't run miners so the safety shields all complain about them, you have to tell it you know what you're doing (whitelist all your mining source/build/run folders)

# Action History
- Created by: LeMoussel | 2019-11-14T14:34:00+00:00
- Closed at: 2019-12-22T19:36:13+00:00
