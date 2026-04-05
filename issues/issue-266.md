---
title: 'Could NOT find mhd (missing: MHD_INCLUDE_DIR MHD_LIBRARY) '
source_url: https://github.com/xmrig/xmrig/issues/266
author: coozgan
assignees: []
labels: []
created_at: '2017-12-16T03:31:35+00:00'
updated_at: '2018-03-14T23:39:12+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:39:12+00:00'
---

# Original Description

Im using macos sierra 

and Im stock with the `cmake .. ` command as it is prompting me this problem
```
-- Could NOT find mhd (missing: MHD_INCLUDE_DIR MHD_LIBRARY) 
CMake Error at CMakeLists.txt:195 (message):
  microhttpd NOT found: use `-DWITH_HTTPD=OFF` to build without http deamon
  support


-- Configuring incomplete, errors occurred!

```

# Discussion History
## spidero | 2017-12-16T17:33:28+00:00
apt install libmicrohttpd-dev

# Action History
- Created by: coozgan | 2017-12-16T03:31:35+00:00
- Closed at: 2018-03-14T23:39:12+00:00
