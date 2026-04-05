---
title: ApiState.cpp error
source_url: https://github.com/xmrig/xmrig/issues/445
author: kenarsuleyman
assignees: []
labels: []
created_at: '2018-03-14T00:24:42+00:00'
updated_at: '2018-11-05T12:57:58+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:57:58+00:00'
---

# Original Description
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.obj
C:/Users/Suleyman/Desktop/xmrig-master/src/api/ApiState.cpp: In member function 'char* ApiState::finalize(rapidjson::Document&) const':
C:/Users/Suleyman/Desktop/xmrig-master/src/api/ApiState.cpp:132:37: error: 'strdup' was not declared in this scope
     return strdup(buffer.GetString());
                                     ^
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.obj] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

I didn't modified any source code. And here is my cmake code.
cmake .. -G "Unix Makefiles" -DUV_INCLUDE_DIR="C:\Users\xxx\Desktop\libuv\include" -DUV_LIBRARY="C:\Users\xxx\Desktop\libuv\lib\i386\libuv.a" -DMHD_INCLUDE_DIR="C:\Users\xxx\Desktop\libmicrohttp\x86\MinGW\static-xp\mingw32\include" -DMHD_LIBRARY="C:\Users\xxx\Desktop\libmicrohttp\x86\MinGW\static-xp\mingw32\lib\libmicrohttpd.a"


# Discussion History
## xmrig | 2018-03-14T10:29:25+00:00
`strdup` should be declared in `#include <string.h>` but this header already added. What compiler do you use?
Thank you.

## kenarsuleyman | 2018-03-14T14:21:58+00:00
I'm using MinGW. Yeah i know that's why it looks weird.

# Action History
- Created by: kenarsuleyman | 2018-03-14T00:24:42+00:00
- Closed at: 2018-11-05T12:57:58+00:00
