---
title: 'aarch63,cortex a53 android cmake error '
source_url: https://github.com/xmrig/xmrig/issues/2536
author: arunAK47AK
assignees: []
labels: []
created_at: '2021-08-13T05:41:54+00:00'
updated_at: '2021-08-14T05:44:57+00:00'
type: issue
status: closed
closed_at: '2021-08-13T10:27:59+00:00'
---

# Original Description
/root/xmrig/src/base/net/stratum/DaemonClient.cpp:68:98error: narrowing conversion of ‘-1’ from ‘int’ to ‘char’ [-Wnarrowing]
68 | 0, 0, 0, 0, 0, 127, 3, 0, 'N', 'U', 'L', 'L' };
| ^

make[2]: *** [CMakeFiles/xmrig.dir/build.make:1031: CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:137: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:103: all] Error 2





# Discussion History
## SChernykh | 2021-08-13T10:10:45+00:00
#2537 

## arunAK47AK | 2021-08-13T10:28:40+00:00
Simple use nano use replace one line script #2537 

## LouTom91 | 2021-08-14T05:44:57+00:00
The given script is not accessible

# Action History
- Created by: arunAK47AK | 2021-08-13T05:41:54+00:00
- Closed at: 2021-08-13T10:27:59+00:00
