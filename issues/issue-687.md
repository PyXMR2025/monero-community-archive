---
title: Console -> Windows SubSystem errors
source_url: https://github.com/xmrig/xmrig/issues/687
author: mateuszji
assignees: []
labels: []
created_at: '2018-06-09T12:08:54+00:00'
updated_at: '2018-06-17T17:53:15+00:00'
type: issue
status: closed
closed_at: '2018-06-17T17:53:15+00:00'
---

# Original Description
I changed >Linker >System >SubSystem from Console to Windows and get the following error.
Error	LNK2001	unresolved external symbol WinMain	xmrig	C:\xmrig-master\build\LIBCMT.lib(exe_winmain.obj)	1	
Error	LNK1120	1 unresolved externals	xmrig	C:\xmrig-master\build\Release\xmrig.exe	1	


I'm using MSVC 2017, should I add mainCRTStartup to EntryPoint? What next?

# Discussion History
# Action History
- Created by: mateuszji | 2018-06-09T12:08:54+00:00
- Closed at: 2018-06-17T17:53:15+00:00
