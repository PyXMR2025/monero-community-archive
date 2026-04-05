---
title: RunTime Error 64x 86x
source_url: https://github.com/xmrig/xmrig/issues/826
author: AhmedZeus
assignees: []
labels:
- question
created_at: '2018-10-19T23:44:55+00:00'
updated_at: '2018-10-20T04:40:47+00:00'
type: issue
status: closed
closed_at: '2018-10-20T04:40:47+00:00'
---

# Original Description
i get this error for 64x  , 86x release 

Updated MSYS2 , Using last Deps. and Using this command for 64x

cmake .. -G "Unix Makefiles" -DWITH_HTTPD=OFF  -DWITH_AEON=OFF -DCMAKE_BUILD_TYPE=Release -DUV_INCLUDE_DIR="C:\Users\xxx\Downloads\lib\gcc\x64\include" -DUV_LIBRARY="C:\Users\xxx\Downloads\lib\gcc\x64\lib\libuv.a" 


https://image.ibb.co/nOSA1L/asdsad.png

https://image.ibb.co/fHXcgL/ewqeqwewqrbb.png


# Discussion History
## xmrig | 2018-10-20T04:40:47+00:00
Follow instructions https://github.com/xmrig/xmrig/wiki/Windows-Build use xmrig-deps or build static libuv.
Thank you.

# Action History
- Created by: AhmedZeus | 2018-10-19T23:44:55+00:00
- Closed at: 2018-10-20T04:40:47+00:00
