---
title: WinRing0x64.sys CVE
source_url: https://github.com/xmrig/xmrig/issues/3573
author: Cyrix126
assignees: []
labels: []
created_at: '2024-10-30T06:32:30+00:00'
updated_at: '2025-06-16T19:33:18+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:33:18+00:00'
---

# Original Description
**Describe the bug**
The current WinRing0x64.sys last update is [5 years old](https://github.com/xmrig/xmrig/commits/master/bin/WinRing0).
There has been a security issue https://www.cvedetails.com/cve/CVE-2020-14979/ that has been discovered since.
The latest code source version seems to be hosted here https://github.com/GermanAizek/WinRing0

The issue that can prevent an update of WinRing0x64.sys is that the file needs to be signed by an EV  where current driver will not get flagged by MS since it wasn't a requirement back then. AFAIK there is no release of the driver updated and signed currently.

**Additional context**
https://github.com/GermanAizek/WinRing0/issues/9
https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/issues/984

# Discussion History
## SChernykh | 2024-10-30T07:49:13+00:00
The fix in https://github.com/GermanAizek/WinRing0/commit/c80b8cd119eeb8c0d50a639c7e90dbedafde336e disables all user access to the driver. Only the internal OS account `NT_AUTHORITY\SYSTEM` can access it after this change. This will not work with XMRig's use-case even if they manage to sign the driver.

# Action History
- Created by: Cyrix126 | 2024-10-30T06:32:30+00:00
- Closed at: 2025-06-16T19:33:18+00:00
