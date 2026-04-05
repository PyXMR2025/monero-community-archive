---
title: 2.4.4 32 bit not working on Windows XP
source_url: https://github.com/xmrig/xmrig/issues/338
author: sergneo
assignees: []
labels:
- bug
created_at: '2018-01-15T08:31:04+00:00'
updated_at: '2018-03-17T02:09:31+00:00'
type: issue
status: closed
closed_at: '2018-01-20T05:47:20+00:00'
---

# Original Description
Very very sorry, but version 2.4.4 32 bit GCC has stopped working in Windows Xp and 2003, an early version 2.4.3 32 bit successfully works on these versions of Windows . I so liked XMRig CPU because it worked on older versions of Windows, and now I can still keep compatibility with older versions of the OS ?
XMRig 2.4.4
![xmrig-2 4 4](https://user-images.githubusercontent.com/27492679/34935007-742c9d00-f9ed-11e7-9c4f-20e450b88e74.jpg)

XMRig 2.4.3
![xmrig-2 4 3](https://user-images.githubusercontent.com/27492679/34935263-4f6afeac-f9ee-11e7-889b-9494714396a3.jpg)

[ConvertInterfaceIndexToLuid function](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365826(v=vs.85).aspx)
Remarks

The ConvertInterfaceIndexToLuid function is available on Windows Vista and later.

# Discussion History
## xmrig | 2018-01-15T10:27:08+00:00
I confirm bug, in version 2.4.4 libuv and libmicrohttpd updated to recent versions, probably it cause the issue.
Thank you.

## sergneo | 2018-01-15T10:56:27+00:00
Yes, the problem is in libuv. I compiled with the previous version libuv/1.14.1 from xmrig-deps-v2 and the new libmicrohttpd/0.9.58 from xmrig-deps-v2_1. Xmrig 2.4.4 successfully works on Windows Xp.

![xmrig-2 4 4-v 2](https://user-images.githubusercontent.com/27492679/34939519-1c11112c-f9fd-11e7-9aac-42e6cf4a8363.jpg)


## xmrig | 2018-01-20T05:47:20+00:00
I rebuilt and replaced `xmrig-2.4.4-gcc-win32` with older libuv version. 1.15.0 last version with Windows XP/2003 support. Also updated dependencies https://github.com/xmrig/xmrig-deps/releases/tag/v2.2
Thank you.

# Action History
- Created by: sergneo | 2018-01-15T08:31:04+00:00
- Closed at: 2018-01-20T05:47:20+00:00
