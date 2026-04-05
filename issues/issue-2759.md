---
title: Windows 6.16.1 GCC build loading half of CPU vs 6.161.1 MSVC build
source_url: https://github.com/xmrig/xmrig/issues/2759
author: NVMDSTEVil
assignees: []
labels: []
created_at: '2021-11-30T04:23:52+00:00'
updated_at: '2021-11-30T06:20:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Using the GCC build results in 50% cpu load.  Both builds show correct number of cores/threads but opening task manager shows only half of available threads are being used, 6.16.0 GCC works fine.  Getting better performance with MSVC build though so not like it matters? ;)

Ryzen 9 3900x/Win10.

# Discussion History
## SChernykh | 2021-11-30T06:20:10+00:00
Windows v6.16.1 GCC build has a problem with auto-tuning, it will be fixed in the next release.

# Action History
- Created by: NVMDSTEVil | 2021-11-30T04:23:52+00:00
