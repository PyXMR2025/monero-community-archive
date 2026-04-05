---
title: Embedded Config
source_url: https://github.com/xmrig/xmrig/issues/2183
author: hirdeshsaxena
assignees: []
labels: []
created_at: '2021-03-16T01:18:09+00:00'
updated_at: '2021-04-12T13:57:57+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:57:57+00:00'
---

# Original Description
Hello Embedded Config not working 

I have made the changes in Use cmake option -DWITH_EMBEDDED_CONFIG=ON  in cmakelists.txt

and entered data in \src\core\config\Config_default.h

but not working still crash have to provide external config.json to run

is there anything i am missing

i have gone through this https://github.com/xmrig/xmrig/issues/1152 but did nt understand have to delete whole function or just the after bracket line 

using cmake and VS to build and release

Please help thanks

# Discussion History
## hirdeshsaxena | 2021-03-16T02:18:51+00:00
Solved https://github.com/xmrig/xmrig/issues/957#issuecomment-468890667

# Action History
- Created by: hirdeshsaxena | 2021-03-16T01:18:09+00:00
- Closed at: 2021-04-12T13:57:57+00:00
