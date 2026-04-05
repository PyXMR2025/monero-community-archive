---
title: error compiling App.cpp on linux
source_url: https://github.com/xmrig/xmrig/issues/69
author: prismspecs
assignees: []
labels: []
created_at: '2017-08-21T21:06:35+00:00'
updated_at: '2017-09-03T03:06:11+00:00'
type: issue
status: closed
closed_at: '2017-09-03T03:06:11+00:00'
---

# Original Description
```
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
/home/desktop/Downloads/xmrig/src/App.cpp: In member function ‘int App::exec()’:
/home/desktop/Downloads/xmrig/src/App.cpp:124:36: error: ‘uv_loop_close’ was not declared in this scope
     uv_loop_close(uv_default_loop());
                                    ^
CMakeFiles/xmrig.dir/build.make:54: recipe for target 'CMakeFiles/xmrig.dir/src/App.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/App.cpp.o] Error 1
CMakeFiles/Makefile2:61: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:76: recipe for target 'all' failed
make: *** [all] Error 2
```

I was unable to get the libuv library via libuv1-dev but rather used the Synaptic Package Manager. Am I perhaps using an out of date libuv? It's version 0.10.28-6.

# Discussion History
## xmrig | 2017-08-22T08:04:17+00:00
Yep version 0.10 unsupported, you need libuv 1 (1.8.0 is minimum tested).

# Action History
- Created by: prismspecs | 2017-08-21T21:06:35+00:00
- Closed at: 2017-09-03T03:06:11+00:00
