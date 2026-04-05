---
title: cannot convert argument 1 from 'LPCTSTR' to 'const wchar_t *
source_url: https://github.com/xmrig/xmrig/issues/453
author: rasta-mouse
assignees: []
labels: []
created_at: '2018-03-15T15:53:02+00:00'
updated_at: '2018-03-16T16:24:21+00:00'
type: issue
status: closed
closed_at: '2018-03-16T16:24:21+00:00'
---

# Original Description
I'm trying to build a 32-bit version of XMRig on my 64-bit Windows 10 system in Visual Studio 15 2017.

`cmake` completes fine:
```
cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS=c:\tools\github\xmrig-deps\msvc2017\x86 -DWITH_LIBCPUID=OFF -DWITH_AEON=OFF -DWITH_HTTPD=OFF
```
On `Build Solution`, I get the following error:
```
Error	C2664	'size_t wcslen(const wchar_t *)': cannot convert argument 1 from 'LPCTSTR' to 'const wchar_t *'	xmrig	c:\tools\github\xmrig\src\mem_win.cpp	91	
```
which is this line:
```
DWORD dwLen = (DWORD) wcslen(string);
```

Any help appreciated.

# Discussion History
## xmrig | 2018-03-16T01:58:21+00:00
Something messy, for 32bit you should use `-G "Visual Studio 15 2017"` without `Win64`, in that case you will get linker errors, but `Mem_win.cpp` should compiled anyway.

For 32 bit MSYS2 much faster.
I can't reproduce this issue.

## rasta-mouse | 2018-03-16T16:24:21+00:00
`-G "Visual Studio 15 2017"` fixed the issue.  Sorry for being dumb :)

# Action History
- Created by: rasta-mouse | 2018-03-15T15:53:02+00:00
- Closed at: 2018-03-16T16:24:21+00:00
