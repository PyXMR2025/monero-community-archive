---
title: '[on raspberry pi] fatal error: uv.h... after make'
source_url: https://github.com/xmrig/xmrig/issues/1258
author: Conan-Wolf
assignees: []
labels: []
created_at: '2019-11-02T18:18:36+00:00'
updated_at: '2019-11-02T18:24:22+00:00'
type: issue
status: closed
closed_at: '2019-11-02T18:24:22+00:00'
---

# Original Description
In file included from /home/pi/xmrig/src/base/io/Console.cpp:26:
/home/pi/xmrig/src/base/io/Console.h:32:10: fatal error: uv.h: No such file or directory
 #include <uv.h>
          ^~~~~~
how should I fix this? I am using raspberry pi 4 64 bit 

# Discussion History
## Conan-Wolf | 2019-11-02T18:24:22+00:00
https://github.com/xmrig/xmrig/issues/571
SOLVED

# Action History
- Created by: Conan-Wolf | 2019-11-02T18:18:36+00:00
- Closed at: 2019-11-02T18:24:22+00:00
