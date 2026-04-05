---
title: Ubuntu 14.10 compiling error
source_url: https://github.com/xmrig/xmrig/issues/462
author: work40
assignees: []
labels: []
created_at: '2018-03-19T10:02:34+00:00'
updated_at: '2018-03-19T10:03:00+00:00'
type: issue
status: closed
closed_at: '2018-03-19T10:03:00+00:00'
---

# Original Description
vis@LTSP:~/xmrig-proxy$ LANG=C sudo make
```
[  2%] Building CXX object CMakeFiles/xmrig-proxy.dir/src/api/Api.cpp.o
In file included from /home/vis/xmrig-proxy/src/api/ApiState.h:28:0,
                 from /home/vis/xmrig-proxy/src/api/Api.cpp:28:
/home/vis/xmrig-proxy/src/proxy/StatsData.h:87:22: error: function definition does not declare parameters
/home/vis/xmrig-proxy/src/proxy/StatsData.h:88:30: error: function definition does not declare parameters
make[2]: *** [CMakeFiles/xmrig-proxy.dir/src/api/Api.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig-proxy.dir/all] Error 2
```

# Discussion History
# Action History
- Created by: work40 | 2018-03-19T10:02:34+00:00
- Closed at: 2018-03-19T10:03:00+00:00
