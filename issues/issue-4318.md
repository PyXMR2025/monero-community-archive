---
title: 'fatal error: rapidjson/document.h'
source_url: https://github.com/monero-project/monero/issues/4318
author: kenken64
assignees: []
labels: []
created_at: '2018-08-31T06:19:33+00:00'
updated_at: '2018-08-31T07:52:11+00:00'
type: issue
status: closed
closed_at: '2018-08-31T07:52:11+00:00'
---

# Original Description
Trying to build master branch.

[ 40%] Building CXX object src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o
In file included from /media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/src/rpc/message.cpp:29:0:
/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/src/rpc/message.h:31:32: fatal error: rapidjson/document.h: No such file or directory
compilation terminated.
src/rpc/CMakeFiles/obj_daemon_messages.dir/build.make:62: recipe for target 'src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o' failed
make[3]: *** [src/rpc/CMakeFiles/obj_daemon_messages.dir/message.cpp.o] Error 1
make[3]: Leaving directory '/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/build/release'
CMakeFiles/Makefile2:1862: recipe for target 'src/rpc/CMakeFiles/obj_daemon_messages.dir/all' failed
make[2]: *** [src/rpc/CMakeFiles/obj_daemon_messages.dir/all] Error 2
make[2]: Leaving directory '/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/build/release'
Makefile:72: recipe for target 'release-all' failed
make: *** [release-all] Error 2


# Discussion History
## moneroexamples | 2018-08-31T06:33:22+00:00
Did you use `--recursive` option when you cloned the repo?

```
git clone --recursive https://github.com/monero-project/monero
```

## kenken64 | 2018-08-31T07:52:11+00:00
thanks !

# Action History
- Created by: kenken64 | 2018-08-31T06:19:33+00:00
- Closed at: 2018-08-31T07:52:11+00:00
