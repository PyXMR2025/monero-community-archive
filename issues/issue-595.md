---
title: compilation error
source_url: https://github.com/xmrig/xmrig/issues/595
author: IxanaxI
assignees: []
labels: []
created_at: '2018-04-30T13:46:54+00:00'
updated_at: '2018-11-05T13:32:41+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:32:41+00:00'
---

# Original Description

![-qp7r4okk9q](https://user-images.githubusercontent.com/38859222/39430363-54c82d70-4c96-11e8-967a-6e38e4a2097b.jpg)

Windiws 10 

# Discussion History
## ghost | 2018-04-30T15:35:30+00:00
The error depends file not founded. You downloaded https://github.com/xmrig/xmrig-deps ?
If yes and error shows again try manual edit CMakeCache (in build dir) and find this: UV_LIBRARY:FILEPATH and UV_INCLUDE_DIR:PATH lines. Change my path to you **full** library path. And build without MHD (cmake .. -G "Unix Makefiles" -DWITH_HTTPD=OFF ...)

Example:
```
//Path to a file.
UV_INCLUDE_DIR:PATH=C:/Code/xmrig/xmrig/deps/x86/include

//Path to a library.
UV_LIBRARY:FILEPATH=C:/Code/xmrig/xmrig/deps/x86/lib/libuv.lib
```

## IxanaxI | 2018-04-30T15:59:29+00:00
no, I downloaded https://github.com/xmrig/xmrig

## ghost | 2018-04-30T17:31:29+00:00
@IxanaxI, first download https://github.com/xmrig/xmrig-deps and unpack.
Select what build you need (x86 or x64). And run a command line on xmrig dir:

`mkdir mybild && cd mybild && cmake .. cmake .. -G "Unix Makefiles" -DWITH_HTTPD=OFF -DXMRIG_DEPS=paste_path
`
Example path: C:/xmrig/xmrig-deps/x86
If you get error - use my first post.

## oneoy | 2018-05-16T11:04:46+00:00
区CMD里编译  笨蛋

# Action History
- Created by: IxanaxI | 2018-04-30T13:46:54+00:00
- Closed at: 2018-11-05T13:32:41+00:00
