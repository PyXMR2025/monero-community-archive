---
title: Change Console to Windows
source_url: https://github.com/xmrig/xmrig/issues/443
author: MaxMarkMuster
assignees: []
labels:
- invalid
created_at: '2018-03-12T20:31:29+00:00'
updated_at: '2018-03-14T22:28:36+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:28:36+00:00'
---

# Original Description
I'm trying to stop the console pop up.
I changed >Linker >System >SubSystem from Console to Windows and get the following error.

- Error LNK2001	unresolved external symbol   WinMain xmrig   C:\xmrig-master\build\LIBCMT.lib(exe_winmain.obj)	1	

- Error LNK1120 1 unresolved externals	xmrig  C:\xmrig-master\build\Release\xmrig.exe	1

Any ideas on how to resolve this. Thanks.




# Discussion History
## kenarsuleyman | 2018-03-14T14:30:21+00:00
What about using hidden option included in xmrig?

## MaxMarkMuster | 2018-03-14T18:06:36+00:00
That works, but it blinks on start up. I would like to make it less noticeable. Thanks for helping though.

## xmrig | 2018-03-14T18:14:45+00:00
Equivalent for this:
`Linker >System >SubSystem from Console to Windows` is add `WIN32` after xmrig https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L213 but if you use MSVC you need also change entry point.
Thank you.

## xmrig | 2018-03-14T22:28:36+00:00
Anyway it not a issue, I close it.

# Action History
- Created by: MaxMarkMuster | 2018-03-12T20:31:29+00:00
- Closed at: 2018-03-14T22:28:36+00:00
