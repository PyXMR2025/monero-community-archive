---
title: 'Compile Error : Linking CXX executable'
source_url: https://github.com/xmrig/xmrig/issues/535
author: BearBang7
assignees: []
labels: []
created_at: '2018-04-10T17:25:26+00:00'
updated_at: '2018-11-05T13:23:40+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:23:40+00:00'
---

# Original Description
I am trying compile using msys2 on x64.
but i got a long error on scanning dependencies. [Here Full Logs](https://pastebin.com/awXyusmA).
also i tried all packages updates.
...
```
[ 97%] Building CXX object CMakeFiles/xmrig.dir/api/Httpd.cpp.obj
[100%] Linking CXX executable xmrig.exe
CMakeFiles/xmrig.dir/objects.a(ApiState.cpp.obj):ApiState.cpp:(.text+0x50c): und                                                                                                                                                                                               efined reference to `__imp_gethostname'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x2a7): undefined ref                                                                                                                                                                                               erence to `App::background()'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x2d7): undefined ref                                                                                                                                                                                               erence to `Mem::allocate(int, int, bool, bool)'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x38c): undefined ref                                                                                                                                                                                               erence to `Mem::release()'
CMakeFiles/xmrig.dir/objects.a(App.cpp.obj):App.cpp:(.text+0x391): undefined ref 
```
...

# Discussion History
# Action History
- Created by: BearBang7 | 2018-04-10T17:25:26+00:00
- Closed at: 2018-11-05T13:23:40+00:00
